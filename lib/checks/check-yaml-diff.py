"""
Analyzes the diff between base and head versions of awesome-privacy.yml.
Enforces the single-entry rule: only one service addition/amendment/removal per PR.
Outputs a JSON diff to /tmp/pr-diff.json and writes a step summary.
"""

import argparse
import json
import os
import subprocess
import sys

import yaml

# Paths (relative to project root)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(PROJECT_ROOT, "awesome-privacy.yml")
DIFF_OUTPUT_PATH = "/tmp/pr-diff.json"

# Exit codes
EXIT_PASS = 0
EXIT_RULE_VIOLATION = 1
EXIT_RUNTIME_ERROR = 2

# ANSI color helpers
_use_color = sys.stderr.isatty() and not os.environ.get("NO_COLOR")
red = (lambda s: f"\033[31m{s}\033[0m") if _use_color else (lambda s: s)
green = (lambda s: f"\033[32m{s}\033[0m") if _use_color else (lambda s: s)
yellow = (lambda s: f"\033[33m{s}\033[0m") if _use_color else (lambda s: s)
dim = (lambda s: f"\033[2m{s}\033[0m") if _use_color else (lambda s: s)


def load_base_yaml(base_ref):
    """Load the YAML from the base ref using git show."""
    try:
        result = subprocess.run(
            ["git", "show", f"{base_ref}:awesome-privacy.yml"],
            capture_output=True, text=True, check=True,
            cwd=PROJECT_ROOT,
        )
        return yaml.safe_load(result.stdout)
    except subprocess.CalledProcessError:
        # File doesn't exist in base (completely new file)
        print(yellow("Warning: awesome-privacy.yml not found in base ref, treating as empty"), file=sys.stderr)
        return {"categories": []}
    except yaml.YAMLError as e:
        print(red(f"Failed to parse base YAML: {e}"), file=sys.stderr)
        sys.exit(EXIT_RUNTIME_ERROR)


def load_head_yaml():
    """Load the YAML from the current working tree."""
    try:
        with open(DATA_PATH, "r") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(red(f"File not found: {DATA_PATH}"), file=sys.stderr)
        sys.exit(EXIT_RUNTIME_ERROR)
    except yaml.YAMLError as e:
        print(red(f"Failed to parse head YAML: {e}"), file=sys.stderr)
        sys.exit(EXIT_RUNTIME_ERROR)


def build_service_index(data):
    """Build a dict keyed by (category, section, service_name) -> service dict."""
    index = {}
    for cat in data.get("categories", []):
        cat_name = cat.get("name", "")
        for sec in cat.get("sections", []):
            sec_name = sec.get("name", "")
            for svc in sec.get("services", []):
                svc_name = svc.get("name", "")
                key = (cat_name, sec_name, svc_name)
                index[key] = svc
    return index


def build_section_index(data):
    """Build a dict keyed by (category, section) -> section metadata (excluding services)."""
    index = {}
    for cat in data.get("categories", []):
        cat_name = cat.get("name", "")
        for sec in cat.get("sections", []):
            sec_name = sec.get("name", "")
            key = (cat_name, sec_name)
            meta = {k: v for k, v in sec.items() if k != "services"}
            index[key] = meta
    return index


def build_category_index(data):
    """Build a dict keyed by category_name -> category metadata (excluding sections)."""
    index = {}
    for cat in data.get("categories", []):
        cat_name = cat.get("name", "")
        meta = {k: v for k, v in cat.items() if k != "sections"}
        index[cat_name] = meta
    return index


def diff_services(base_data, head_data):
    """Find added, removed, and modified services."""
    base_idx = build_service_index(base_data)
    head_idx = build_service_index(head_data)

    base_keys = set(base_idx.keys())
    head_keys = set(head_idx.keys())

    added = []
    for key in sorted(head_keys - base_keys):
        added.append({
            "category": key[0],
            "section": key[1],
            "service": key[2],
            "fields": head_idx[key],
        })

    removed = []
    for key in sorted(base_keys - head_keys):
        removed.append({
            "category": key[0],
            "section": key[1],
            "service": key[2],
        })

    modified = []
    for key in sorted(base_keys & head_keys):
        base_svc = base_idx[key]
        head_svc = head_idx[key]
        if base_svc != head_svc:
            changed_fields = []
            all_fields = set(base_svc.keys()) | set(head_svc.keys())
            for field in sorted(all_fields):
                old_val = base_svc.get(field)
                new_val = head_svc.get(field)
                if old_val != new_val:
                    changed_fields.append(field)
            modified.append({
                "category": key[0],
                "section": key[1],
                "service": key[2],
                "changed_fields": changed_fields,
            })

    return added, removed, modified


def diff_sections(base_data, head_data):
    """Find section-level metadata changes (intro, wordOfWarning, etc.)."""
    base_idx = build_section_index(base_data)
    head_idx = build_section_index(head_data)

    base_keys = set(base_idx.keys())
    head_keys = set(head_idx.keys())

    changes = []

    # New sections
    for key in sorted(head_keys - base_keys):
        changes.append({
            "category": key[0],
            "section": key[1],
            "change_type": "added_section",
        })

    # Removed sections
    for key in sorted(base_keys - head_keys):
        changes.append({
            "category": key[0],
            "section": key[1],
            "change_type": "removed_section",
        })

    # Modified section metadata
    for key in sorted(base_keys & head_keys):
        base_meta = base_idx[key]
        head_meta = head_idx[key]
        if base_meta != head_meta:
            changed_fields = []
            all_fields = set(base_meta.keys()) | set(head_meta.keys())
            for field in sorted(all_fields):
                if base_meta.get(field) != head_meta.get(field):
                    changed_fields.append(field)
            changes.append({
                "category": key[0],
                "section": key[1],
                "change_type": "modified_section_metadata",
                "changed_fields": changed_fields,
            })

    return changes


def diff_categories(base_data, head_data):
    """Find structural category changes."""
    base_idx = build_category_index(base_data)
    head_idx = build_category_index(head_data)

    base_keys = set(base_idx.keys())
    head_keys = set(head_idx.keys())

    changes = []

    for name in sorted(head_keys - base_keys):
        changes.append({"category": name, "change_type": "added_category"})

    for name in sorted(base_keys - head_keys):
        changes.append({"category": name, "change_type": "removed_category"})

    return changes


def write_github_output(name, value):
    """Write a value to $GITHUB_OUTPUT."""
    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a") as f:
            f.write(f"{name}={value}\n")


def write_step_summary(diff_result):
    """Write a Markdown summary to $GITHUB_STEP_SUMMARY."""
    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_file:
        return

    lines = ["## YAML Diff Analysis\n"]

    added = diff_result["services"]["added"]
    removed = diff_result["services"]["removed"]
    modified = diff_result["services"]["modified"]
    section_changes = diff_result["sections"]
    category_changes = diff_result["categories"]

    if not added and not removed and not modified and not section_changes and not category_changes:
        lines.append("No changes detected in `awesome-privacy.yml`.\n")
    else:
        lines.append("| Type | Category | Section | Service | Details |")
        lines.append("|------|----------|---------|---------|---------|")

        for svc in added:
            lines.append(f"| Added | {svc['category']} | {svc['section']} | {svc['service']} | New service |")

        for svc in removed:
            lines.append(f"| Removed | {svc['category']} | {svc['section']} | {svc['service']} | Service removed |")

        for svc in modified:
            fields = ", ".join(svc["changed_fields"])
            lines.append(f"| Modified | {svc['category']} | {svc['section']} | {svc['service']} | Changed: {fields} |")

        for change in section_changes:
            detail = change["change_type"].replace("_", " ").title()
            fields = ", ".join(change.get("changed_fields", []))
            if fields:
                detail += f" ({fields})"
            lines.append(f"| Section | {change['category']} | {change['section']} | - | {detail} |")

        for change in category_changes:
            detail = change["change_type"].replace("_", " ").title()
            lines.append(f"| Category | {change['category']} | - | - | {detail} |")

        lines.append("")

    with open(summary_file, "a") as f:
        f.write("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Analyze YAML diff for PR checks")
    parser.add_argument("--base-ref", required=True, help="Base git ref (SHA or branch) to diff against")
    args = parser.parse_args()

    # Load both versions
    base_data = load_base_yaml(args.base_ref)
    head_data = load_head_yaml()

    # Compute diffs
    added, removed, modified = diff_services(base_data, head_data)
    section_changes = diff_sections(base_data, head_data)
    category_changes = diff_categories(base_data, head_data)

    # Build result
    diff_result = {
        "services": {
            "added": added,
            "removed": removed,
            "modified": modified,
        },
        "sections": section_changes,
        "categories": category_changes,
    }

    # Write diff JSON
    with open(DIFF_OUTPUT_PATH, "w") as f:
        json.dump(diff_result, f, indent=2)
    print(f"Diff written to {DIFF_OUTPUT_PATH}")

    # Determine if there are service-level changes
    has_service_changes = bool(added or removed or modified)
    write_github_output("has_service_changes", str(has_service_changes).lower())

    # Write step summary
    write_step_summary(diff_result)

    # Enforce single-entry rule
    service_change_count = len(added) + len(removed) + len(modified)

    if service_change_count > 1:
        print(red("Single-entry rule violation: PRs must contain only one service change."), file=sys.stderr)
        print(red(f"Found {service_change_count} service-level changes:"), file=sys.stderr)
        for svc in added:
            print(f"  + Added: {svc['category']} > {svc['section']} > {svc['service']}", file=sys.stderr)
        for svc in removed:
            print(f"  - Removed: {svc['category']} > {svc['section']} > {svc['service']}", file=sys.stderr)
        for svc in modified:
            fields = ", ".join(svc["changed_fields"])
            print(f"  ~ Modified: {svc['category']} > {svc['section']} > {svc['service']} ({fields})", file=sys.stderr)
        sys.exit(EXIT_RULE_VIOLATION)

    # If no service changes, check section-level changes
    if service_change_count == 0 and len(section_changes) > 1:
        print(red("Single-entry rule violation: PRs must contain only one section-level change."), file=sys.stderr)
        print(red(f"Found {len(section_changes)} section-level changes:"), file=sys.stderr)
        for change in section_changes:
            detail = change["change_type"].replace("_", " ")
            fields = change.get("changed_fields", [])
            extra = f" ({', '.join(fields)})" if fields else ""
            print(f"  ~ {change['category']} > {change['section']}: {detail}{extra}", file=sys.stderr)
        sys.exit(EXIT_RULE_VIOLATION)

    # Summary
    total = service_change_count + len(section_changes) + len(category_changes)
    if total == 0:
        print(green("No changes detected in awesome-privacy.yml"))
    else:
        print(green(f"Single-entry rule passed. {service_change_count} service change(s), "
                     f"{len(section_changes)} section change(s), {len(category_changes)} category change(s)."))
    sys.exit(EXIT_PASS)


if __name__ == "__main__":
    main()
