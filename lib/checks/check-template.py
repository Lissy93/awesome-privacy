"""
Checks PR body against the pull request template.
Reads the PR body from the PR_BODY environment variable (avoids shell injection).
Exits with code 1 for severe violations (empty body, missing required sections).
"""

import os
import re
import sys

# Exit codes
EXIT_PASS = 0
EXIT_FAIL = 1
EXIT_RUNTIME_ERROR = 2

# Warnings that should cause a hard failure
CRITICAL_WARNINGS = {
    "PR body is empty or not provided",
    "Type section is missing",
    "Type section is empty",
    "Changes section is missing",
    "Changes section is empty",
    "Checklist section is missing",
    "Checklist section does not contain any checkbox items",
}

# ANSI color helpers
_use_color = sys.stderr.isatty() and not os.environ.get("NO_COLOR")
red = (lambda s: f"\033[31m{s}\033[0m") if _use_color else (lambda s: s)
green = (lambda s: f"\033[32m{s}\033[0m") if _use_color else (lambda s: s)
yellow = (lambda s: f"\033[33m{s}\033[0m") if _use_color else (lambda s: s)

# Valid PR types from the template
VALID_TYPES = {"Addition", "Amendment", "Removal", "Spelling or Grammar", "Website Update", "Misc"}

# Raw template text that indicates an unfilled section
RAW_TYPE_LINE = "Addition / Amendment / Removal / Spelling or Grammar / Website Update / Misc"


def strip_html_comments(text):
    """Remove <!-- ... --> comments from text."""
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL).strip()


def extract_section(body, header):
    """Extract content between a ### header and the next --- or ### header."""
    pattern = rf"###\s*{re.escape(header)}\s*\n(.*?)(?=\n---|\n###|\Z)"
    match = re.search(pattern, body, re.DOTALL)
    if match:
        return match.group(1)
    return None


def check_type_section(content):
    """Check the Type section. Returns list of warning strings."""
    warnings = []

    if content is None:
        warnings.append("Type section is missing")
        return warnings

    cleaned = strip_html_comments(content).strip()

    if not cleaned:
        warnings.append("Type section is empty")
        return warnings

    # Check for raw template text (unchanged)
    if RAW_TYPE_LINE in cleaned:
        warnings.append("Type section appears unchanged from the template -- please select one type")
        return warnings

    # Check how many valid types are present
    found_types = [t for t in VALID_TYPES if t in cleaned]

    if len(found_types) == 0:
        warnings.append(f"Type section does not contain a recognized type. Expected one of: {', '.join(sorted(VALID_TYPES))}")
    elif len(found_types) > 1:
        warnings.append(f"Type section contains multiple types ({', '.join(found_types)}) -- please select only one")

    return warnings


def check_text_section(content, section_name):
    """Check a text section (Changes, Supporting Material, Affiliation). Returns list of warnings."""
    warnings = []

    if content is None:
        warnings.append(f"{section_name} section is missing")
        return warnings

    cleaned = strip_html_comments(content).strip()

    if not cleaned:
        warnings.append(f"{section_name} section is empty")

    return warnings


def check_checklist(content):
    """Check the Checklist section. Returns list of warnings."""
    warnings = []

    if content is None:
        warnings.append("Checklist section is missing")
        return warnings

    checked = re.findall(r"- \[x\]", content, re.IGNORECASE)
    unchecked = re.findall(r"- \[ \]", content)

    total = len(checked) + len(unchecked)

    if total == 0:
        warnings.append("Checklist section does not contain any checkbox items")
        return warnings

    if unchecked:
        warnings.append(f"Checklist has {len(unchecked)} unchecked item(s) out of {total}")

    return warnings


def has_critical_warnings(warnings):
    """Return True if any warning is a critical (hard-fail) violation."""
    return any(w in CRITICAL_WARNINGS for w in warnings)


def write_step_summary(all_warnings):
    """Write a Markdown summary to $GITHUB_STEP_SUMMARY."""
    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_file:
        return

    lines = ["## PR Template Check\n"]

    if not all_warnings:
        lines.append("All template checks passed.\n")
    else:
        critical = has_critical_warnings(all_warnings)
        lines.append(f"Found {len(all_warnings)} warning(s):\n")
        for w in all_warnings:
            lines.append(f"- {w}")
        lines.append("")
        if critical:
            lines.append("> **Error:** One or more required sections are missing or empty. "
                          "Please fill out the PR template before this check can pass.\n")
        else:
            lines.append("> **Note:** Template warnings are informational and do not fail the check. "
                          "Reviewers will verify compliance.\n")

    with open(summary_file, "a") as f:
        f.write("\n".join(lines) + "\n")


def main():
    pr_body = os.environ.get("PR_BODY")

    if pr_body is None or pr_body.strip() == "":
        all_warnings = [
            "PR body is empty or not provided",
            "Type section is missing",
            "Changes section is missing",
            "Supporting Material section is missing",
            "Affiliation section is missing",
            "Checklist section is missing",
        ]
        print(yellow(f"PR template check: {len(all_warnings)} warning(s)"), file=sys.stderr)
        for w in all_warnings:
            print(f"  {yellow('WARNING')} {w}", file=sys.stderr)
        write_step_summary(all_warnings)
        sys.exit(EXIT_FAIL)

    all_warnings = []

    # Check each section
    type_content = extract_section(pr_body, "Type")
    all_warnings.extend(check_type_section(type_content))

    changes_content = extract_section(pr_body, "Changes")
    all_warnings.extend(check_text_section(changes_content, "Changes"))

    supporting_content = extract_section(pr_body, "Supporting Material")
    all_warnings.extend(check_text_section(supporting_content, "Supporting Material"))

    affiliation_content = extract_section(pr_body, "Affiliation")
    all_warnings.extend(check_text_section(affiliation_content, "Affiliation"))

    checklist_content = extract_section(pr_body, "Checklist")
    all_warnings.extend(check_checklist(checklist_content))

    # Print results
    if all_warnings:
        print(yellow(f"PR template check: {len(all_warnings)} warning(s)"), file=sys.stderr)
        for w in all_warnings:
            print(f"  {yellow('WARNING')} {w}", file=sys.stderr)
    else:
        print(green("PR template check passed."))

    write_step_summary(all_warnings)
    if has_critical_warnings(all_warnings):
        sys.exit(EXIT_FAIL)
    sys.exit(EXIT_PASS)


if __name__ == "__main__":
    main()
