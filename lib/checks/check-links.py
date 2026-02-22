"""
Validates URLs and metadata for added/modified services in a PR.
Reads the diff JSON produced by check-yaml-diff.py.
All checks are warnings only -- this script never fails (exit 0).
"""

import argparse
import json
import os
import sys

import requests
import yaml

# Paths (relative to project root)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(PROJECT_ROOT, "awesome-privacy.yml")

# Exit codes
EXIT_PASS = 0
EXIT_RUNTIME_ERROR = 2

# ANSI color helpers
_use_color = sys.stderr.isatty() and not os.environ.get("NO_COLOR")
red = (lambda s: f"\033[31m{s}\033[0m") if _use_color else (lambda s: s)
green = (lambda s: f"\033[32m{s}\033[0m") if _use_color else (lambda s: s)
yellow = (lambda s: f"\033[33m{s}\033[0m") if _use_color else (lambda s: s)

TIMEOUT = 10
USER_AGENT = "awesome-privacy-ci/1.0"
DESC_MIN_LEN = 50
DESC_MAX_LEN = 250


def check_url(url, label):
    """Check if a URL is reachable. Returns (ok, message)."""
    try:
        resp = requests.head(
            url,
            timeout=TIMEOUT,
            allow_redirects=True,
            headers={"User-Agent": USER_AGENT},
        )
        if resp.status_code >= 400:
            # Retry with GET -- some servers reject HEAD
            resp = requests.get(
                url,
                timeout=TIMEOUT,
                allow_redirects=True,
                headers={"User-Agent": USER_AGENT},
                stream=True,
            )
            resp.close()
        if resp.status_code >= 400:
            return False, f"{label}: HTTP {resp.status_code} for {url}"
        return True, None
    except requests.RequestException as e:
        return False, f"{label}: Connection error for {url} ({type(e).__name__})"


def check_service(service_data, service_name, category, section):
    """Run all checks on a single service. Returns list of warning strings."""
    warnings = []
    name_prefix = f"{category} > {section} > {service_name}"

    # Check url
    url = service_data.get("url")
    if url:
        ok, msg = check_url(url, "url")
        if not ok:
            warnings.append(f"{name_prefix}: {msg}")
    else:
        warnings.append(f"{name_prefix}: missing required field 'url'")

    # Check icon
    icon = service_data.get("icon")
    if icon:
        ok, msg = check_url(icon, "icon")
        if not ok:
            warnings.append(f"{name_prefix}: {msg}")
    else:
        warnings.append(f"{name_prefix}: missing 'icon' field (recommended by contributing guide)")

    # Check iosApp
    ios_app = service_data.get("iosApp")
    if ios_app:
        ok, msg = check_url(ios_app, "iosApp")
        if not ok:
            warnings.append(f"{name_prefix}: {msg}")

    # Check github
    github = service_data.get("github")
    if github:
        github_url = f"https://github.com/{github}"
        ok, msg = check_url(github_url, "github")
        if not ok:
            warnings.append(f"{name_prefix}: {msg}")

    # Check description length
    desc = service_data.get("description", "")
    desc_stripped = desc.strip()
    desc_len = len(desc_stripped)
    if desc_len < DESC_MIN_LEN:
        warnings.append(f"{name_prefix}: description too short ({desc_len} chars, minimum {DESC_MIN_LEN})")
    elif desc_len > DESC_MAX_LEN:
        warnings.append(f"{name_prefix}: description too long ({desc_len} chars, maximum {DESC_MAX_LEN})")

    return warnings


def find_service_in_head(category, section, service_name):
    """Look up a service in the head YAML by category/section/service name."""
    try:
        with open(DATA_PATH, "r") as f:
            data = yaml.safe_load(f)
        for cat in data.get("categories", []):
            if cat.get("name") == category:
                for sec in cat.get("sections", []):
                    if sec.get("name") == section:
                        for svc in sec.get("services", []):
                            if svc.get("name") == service_name:
                                return svc
    except Exception:
        pass
    return None


def write_step_summary(all_warnings, services_checked):
    """Write a Markdown summary to $GITHUB_STEP_SUMMARY."""
    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_file:
        return

    lines = ["## Link Validation\n"]

    if not services_checked:
        lines.append("No services to check.\n")
    elif not all_warnings:
        lines.append(f"All checks passed for {services_checked} service(s).\n")
    else:
        lines.append(f"Checked {services_checked} service(s), found {len(all_warnings)} warning(s):\n")
        lines.append("| Warning |")
        lines.append("|---------|")
        for w in all_warnings:
            escaped = w.replace("|", "\\|")
            lines.append(f"| {escaped} |")
        lines.append("")
        lines.append("> **Note:** Link warnings are informational only and do not fail the check. "
                      "URLs may be temporarily down or block automated requests.\n")

    with open(summary_file, "a") as f:
        f.write("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Validate links for added/modified services")
    parser.add_argument("--diff-json", required=True, help="Path to the diff JSON file")
    args = parser.parse_args()

    # Load diff
    try:
        with open(args.diff_json, "r") as f:
            diff = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(red(f"Failed to load diff JSON: {e}"), file=sys.stderr)
        sys.exit(EXIT_RUNTIME_ERROR)

    all_warnings = []
    services_checked = 0

    # Check added services
    for svc in diff.get("services", {}).get("added", []):
        services_checked += 1
        warnings = check_service(
            svc.get("fields", {}),
            svc["service"],
            svc["category"],
            svc["section"],
        )
        all_warnings.extend(warnings)

    # Check modified services -- only if they have URL-related field changes
    for svc in diff.get("services", {}).get("modified", []):
        url_fields = {"url", "icon", "iosApp", "github", "description"}
        changed = set(svc.get("changed_fields", []))
        if changed & url_fields:
            services_checked += 1
            head_svc = find_service_in_head(svc["category"], svc["section"], svc["service"])
            if head_svc:
                warnings = check_service(
                    head_svc,
                    svc["service"],
                    svc["category"],
                    svc["section"],
                )
                all_warnings.extend(warnings)

    # Print results
    if all_warnings:
        print(yellow(f"Link validation: {len(all_warnings)} warning(s)"), file=sys.stderr)
        for w in all_warnings:
            print(f"  {yellow('WARNING')} {w}", file=sys.stderr)
    else:
        print(green(f"Link validation passed. {services_checked} service(s) checked."))

    write_step_summary(all_warnings, services_checked)
    sys.exit(EXIT_PASS)


if __name__ == "__main__":
    main()
