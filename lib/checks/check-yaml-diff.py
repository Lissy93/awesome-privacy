"""Analyzes the diff between base and head versions of awesome-privacy.yml.
Enforces the single-entry rule and outputs a JSON diff to /tmp/pr-diff.json.
"""

import argparse
import json
import os
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from yaml_diff import build_index, diff_index, load_yaml_at_ref

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(PROJECT_ROOT, "awesome-privacy.yml")
DIFF_OUTPUT_PATH = "/tmp/pr-diff.json"
SUMMARY_OUTPUT_PATH = "/tmp/pr-diff-summary.md"

EXIT_PASS = 0
EXIT_RULE_VIOLATION = 1
EXIT_RUNTIME_ERROR = 2

_use_color = sys.stderr.isatty() and not os.environ.get("NO_COLOR")
red = (lambda s: f"\033[31m{s}\033[0m") if _use_color else (lambda s: s)
green = (lambda s: f"\033[32m{s}\033[0m") if _use_color else (lambda s: s)
yellow = (lambda s: f"\033[33m{s}\033[0m") if _use_color else (lambda s: s)


def load_base_yaml(base_ref):
    """Load the YAML from the base ref using git show."""
    data = load_yaml_at_ref(base_ref, PROJECT_ROOT)
    if data is None:
        print(yellow("awesome-privacy.yml not found in base ref, treating as empty"), file=sys.stderr)
        return {"categories": []}
    return data


def load_head_yaml():
    """Load the YAML from the current working tree."""
    try:
        with open(DATA_PATH) as f:
            return yaml.safe_load(f)
    except (FileNotFoundError, yaml.YAMLError) as e:
        print(red(f"Failed to load head YAML: {e}"), file=sys.stderr)
        sys.exit(EXIT_RUNTIME_ERROR)


def write_github_output(name, value):
    """Write a value to $GITHUB_OUTPUT."""
    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a") as f:
            f.write(f"{name}={value}\n")


def find_duplicate_names(data):
    """Find duplicate service names within the same section."""
    duplicates = []
    for cat in data.get("categories", []):
        cn = cat.get("name", "")
        for sec in cat.get("sections", []):
            sn = sec.get("name", "")
            seen = {}
            for svc in sec.get("services", []):
                name = svc.get("name", "")
                if name in seen:
                    duplicates.append((cn, sn, name))
                else:
                    seen[name] = True
    return duplicates


def fmt_path(key):
    """Format a tuple key as a readable path."""
    return " → ".join(key) if isinstance(key, tuple) else key


def format_diff_bullets(diff_result):
    """Build bullet-point lines summarizing all changes. Returns list of strings or empty list."""
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
    for dup in diff_result.get("duplicates", []):
        bullets.append(
            f"- ⚠️ Duplicate service name **{dup['service']}** "
            f"in {dup['category']} → {dup['section']}"
        )

    return bullets


def write_diff_summary(diff_result):
    """Write the bullet-point summary to a file for downstream consumers."""
    bullets = format_diff_bullets(diff_result)
    if bullets:
        with open(SUMMARY_OUTPUT_PATH, "w") as f:
            f.write("\n".join(bullets) + "\n")



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

    duplicates = find_duplicate_names(head)
    dup_entries = [{"category": d[0], "section": d[1], "service": d[2]}
                   for d in duplicates]

    diff_result = {
        "services": {"added": added, "removed": removed, "modified": modified},
        "sections": sections,
        "categories": categories,
        "duplicates": dup_entries,
    }

    with open(DIFF_OUTPUT_PATH, "w") as f:
        json.dump(diff_result, f, indent=2)

    write_github_output("has_service_changes", str(bool(added or removed or modified)).lower())
    write_diff_summary(diff_result)

    added_count = len(added)
    if added_count > 1:
        print(red(f"Single-entry rule violation: {added_count} service additions found."), file=sys.stderr)
        sys.exit(EXIT_RULE_VIOLATION)
    added_sections = [s for s in sections if s["change_type"] == "added_section"]
    if added_count == 0 and len(added_sections) > 1:
        print(red(f"Single-entry rule violation: {len(added_sections)} section additions found."), file=sys.stderr)
        sys.exit(EXIT_RULE_VIOLATION)

    if duplicates:
        names = ", ".join(f"{d[2]} (in {d[0]} → {d[1]})" for d in duplicates)
        print(red(f"Duplicate service names found: {names}"), file=sys.stderr)
        sys.exit(EXIT_RULE_VIOLATION)

    total = len(added) + len(removed) + len(modified)
    print(green(f"Single-entry rule passed. {total} service "
                f"({added_count} added), {len(sections)} section, "
                f"{len(categories)} category change(s)."))
    sys.exit(EXIT_PASS)


if __name__ == "__main__":
    main()
