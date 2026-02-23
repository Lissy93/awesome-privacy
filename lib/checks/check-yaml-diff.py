"""Analyzes the diff between base and head versions of awesome-privacy.yml.
Enforces the single-entry rule and outputs a JSON diff to /tmp/pr-diff.json.
"""

import argparse
import json
import os
import subprocess
import sys

import yaml

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(PROJECT_ROOT, "awesome-privacy.yml")
DIFF_OUTPUT_PATH = "/tmp/pr-diff.json"

EXIT_PASS = 0
EXIT_RULE_VIOLATION = 1
EXIT_RUNTIME_ERROR = 2

_use_color = sys.stderr.isatty() and not os.environ.get("NO_COLOR")
red = (lambda s: f"\033[31m{s}\033[0m") if _use_color else (lambda s: s)
green = (lambda s: f"\033[32m{s}\033[0m") if _use_color else (lambda s: s)
yellow = (lambda s: f"\033[33m{s}\033[0m") if _use_color else (lambda s: s)


def load_base_yaml(base_ref):
    """Load the YAML from the base ref using git show."""
    try:
        result = subprocess.run(
            ["git", "show", f"{base_ref}:awesome-privacy.yml"],
            capture_output=True, text=True, check=True, cwd=PROJECT_ROOT,
        )
        return yaml.safe_load(result.stdout)
    except subprocess.CalledProcessError:
        print(yellow("awesome-privacy.yml not found in base ref, treating as empty"), file=sys.stderr)
        return {"categories": []}
    except yaml.YAMLError as e:
        print(red(f"Failed to parse base YAML: {e}"), file=sys.stderr)
        sys.exit(EXIT_RUNTIME_ERROR)


def load_head_yaml():
    """Load the YAML from the current working tree."""
    try:
        with open(DATA_PATH) as f:
            return yaml.safe_load(f)
    except (FileNotFoundError, yaml.YAMLError) as e:
        print(red(f"Failed to load head YAML: {e}"), file=sys.stderr)
        sys.exit(EXIT_RUNTIME_ERROR)


def build_index(data, depth):
    """Build a keyed index at the given depth (3=services, 2=sections, 1=categories)."""
    index = {}
    for cat in data.get("categories", []):
        cn = cat.get("name", "")
        if depth == 1:
            index[cn] = {k: v for k, v in cat.items() if k != "sections"}
            continue
        for sec in cat.get("sections", []):
            sn = sec.get("name", "")
            if depth == 2:
                index[(cn, sn)] = {k: v for k, v in sec.items() if k != "services"}
                continue
            for svc in sec.get("services", []):
                index[(cn, sn, svc.get("name", ""))] = svc
    return index


def diff_index(base_idx, head_idx):
    """Return (added_keys, removed_keys, modified_keys_with_changed_fields)."""
    base_keys, head_keys = set(base_idx), set(head_idx)
    added = sorted(head_keys - base_keys)
    removed = sorted(base_keys - head_keys)
    modified = []
    for key in sorted(base_keys & head_keys):
        if base_idx[key] != head_idx[key]:
            all_fields = set(base_idx[key]) | set(head_idx[key])
            changed = sorted(f for f in all_fields if base_idx[key].get(f) != head_idx[key].get(f))
            modified.append((key, changed))
    return added, removed, modified


def write_github_output(name, value):
    """Write a value to $GITHUB_OUTPUT."""
    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a") as f:
            f.write(f"{name}={value}\n")


def fmt_path(key):
    """Format a tuple key as a readable path."""
    return " → ".join(key) if isinstance(key, tuple) else key


def write_step_summary(diff_result):
    """Write a bullet-point Markdown summary to $GITHUB_STEP_SUMMARY."""
    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_file:
        return

    lines = ["## YAML Diff Analysis\n"]
    bullets = []

    for svc in diff_result["services"]["added"]:
        bullets.append(f"- Added **{svc['service']}** in {svc['category']} → {svc['section']}")
    for svc in diff_result["services"]["removed"]:
        bullets.append(f"- Removed **{svc['service']}** from {svc['category']} → {svc['section']}")
    for svc in diff_result["services"]["modified"]:
        fields = ", ".join(f"`{f}`" for f in svc["changed_fields"])
        bullets.append(f"- Modified {fields} in {svc['category']} → {svc['section']} → {svc['service']}")
    for change in diff_result["sections"]:
        ct = change["change_type"]
        path = f"{change['category']} → {change['section']}"
        if ct == "added_section":
            bullets.append(f"- Added section **{change['section']}** in {change['category']}")
        elif ct == "removed_section":
            bullets.append(f"- Removed section **{change['section']}** from {change['category']}")
        else:
            fields = ", ".join(f"`{f}`" for f in change.get("changed_fields", []))
            bullets.append(f"- Modified section metadata ({fields}) in {path}")
    for change in diff_result["categories"]:
        if change["change_type"] == "added_category":
            bullets.append(f"- Added category **{change['category']}**")
        else:
            bullets.append(f"- Removed category **{change['category']}**")

    if bullets:
        lines.extend(bullets)
    else:
        lines.append("No changes detected in `awesome-privacy.yml`.")

    with open(summary_file, "a") as f:
        f.write("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", required=True)
    args = parser.parse_args()

    base = load_base_yaml(args.base_ref)
    head = load_head_yaml()

    svc_added, svc_removed, svc_modified = diff_index(
        build_index(base, 3), build_index(head, 3),
    )
    sec_added, sec_removed, sec_modified = diff_index(
        build_index(base, 2), build_index(head, 2),
    )
    cat_added, cat_removed, _ = diff_index(
        build_index(base, 1), build_index(head, 1),
    )

    added = [{"category": k[0], "section": k[1], "service": k[2],
              "fields": build_index(head, 3)[k]} for k in svc_added]
    removed = [{"category": k[0], "section": k[1], "service": k[2]} for k in svc_removed]
    modified = [{"category": k[0], "section": k[1], "service": k[2],
                 "changed_fields": cf} for k, cf in svc_modified]

    sections = []
    for k in sec_added:
        sections.append({"category": k[0], "section": k[1], "change_type": "added_section"})
    for k in sec_removed:
        sections.append({"category": k[0], "section": k[1], "change_type": "removed_section"})
    for k, cf in sec_modified:
        sections.append({"category": k[0], "section": k[1],
                         "change_type": "modified_section_metadata", "changed_fields": cf})

    categories = []
    for k in cat_added:
        categories.append({"category": k, "change_type": "added_category"})
    for k in cat_removed:
        categories.append({"category": k, "change_type": "removed_category"})

    diff_result = {
        "services": {"added": added, "removed": removed, "modified": modified},
        "sections": sections,
        "categories": categories,
    }

    with open(DIFF_OUTPUT_PATH, "w") as f:
        json.dump(diff_result, f, indent=2)

    write_github_output("has_service_changes", str(bool(added or removed or modified)).lower())
    write_step_summary(diff_result)

    added_count = len(added)
    if added_count > 1:
        print(red(f"Single-entry rule violation: {added_count} service additions found."), file=sys.stderr)
        sys.exit(EXIT_RULE_VIOLATION)
    if added_count == 0 and len(sections) > 1:
        print(red(f"Single-entry rule violation: {len(sections)} section changes found."), file=sys.stderr)
        sys.exit(EXIT_RULE_VIOLATION)

    total = len(added) + len(removed) + len(modified)
    print(green(f"Single-entry rule passed. {total} service "
                f"({added_count} added), {len(sections)} section, "
                f"{len(categories)} category change(s)."))
    sys.exit(EXIT_PASS)


if __name__ == "__main__":
    main()
