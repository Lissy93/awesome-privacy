"""Checks PR metadata: title format, draft status, template completeness, and checkboxes."""

import json
import logging
import os
import re
import subprocess
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s [%(filename)s] %(message)s",
    stream=sys.stderr,
)

FINDINGS_PATH = "/tmp/findings-compliance.json"

BAD_TITLES = {"update readme.md", "update awesome-privacy.yml"}

TITLE_MSG = (
    "The pull request title does not follow the format defined in our guidelines."
    " Please rename it to `[Add/Remove/Update] [software name] in [software section]`"
)
DRAFT_MSG = (
    "Please avoid opening WIP pull requests."
    " Your PR should be 100% ready and complete before submitting"
)
TEMPLATE_MSG = (
    "Please fill in pull request template in full."
    " You can find a copy of this"
    " [here](https://github.com/Lissy93/awesome-privacy/blob/main/.github/PULL_REQUEST_TEMPLATE.md)"
)
CHECKBOX_MSG = (
    "Ensure you have completed the checklist (put a tick the checkboxes with `[x]`),"
    " to confirm that you've read the contributing guidelines, checked your submission,"
    " indicated your affiliation and agree to follow our CoC"
)
README_MSG = (
    "Do not edit the README directly. This file is auto-generated from the"
    " content in `awesome-privacy.yml`, and so your changes will be overridden!"
    " Instead, only modify the YAML file, and be sure to follow our Contributing Guidelines."
)
BOT_MSG = (
    "Submissions are only accepted from humans."
    " This PR appears to have been authored by a bot or AI assistant."
)

_BOT_AUTHOR_RE = re.compile(
    r"(?:noreply@anthropic\.com|devin-ai-integration|copilot-swe-agent|noreply@cursor\.com)",
    re.IGNORECASE,
)


def extract_section(body, header):
    """Extract content between a ### header and the next delimiter."""
    pattern = rf"###\s*{re.escape(header)}\s*\n(.*?)(?=\n---|\n###|\Z)"
    match = re.search(pattern, body, re.DOTALL)
    return match.group(1) if match else None


def strip_html_comments(text):
    """Remove HTML comments from text."""
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL).strip()


def check_title(title):
    """Return a finding if the PR title matches a known-bad pattern."""
    if title and title.strip().lower() in BAD_TITLES:
        return TITLE_MSG
    return None


def check_draft(draft_str):
    """Return a finding if the PR is in draft state."""
    if str(draft_str).lower() == "true":
        return DRAFT_MSG
    return None


def check_template(body):
    """Return a finding if required template sections are missing or empty."""
    for header in ("Type", "Changes", "Checklist"):
        content = extract_section(body, header)
        if content is None or not strip_html_comments(content):
            return TEMPLATE_MSG
    return None


def check_checkboxes(body):
    """Return a finding if any checklist checkboxes are unchecked."""
    section = extract_section(body, "Checklist")
    if section is None:
        return None
    checked = re.findall(r"- \[x\]", section, re.IGNORECASE)
    unchecked = re.findall(r"- \[ \]", section)
    if not checked and not unchecked:
        return None
    if unchecked:
        return CHECKBOX_MSG
    return None


def check_bot_coauthors(base_ref):
    """Return a finding if any commit in the PR has a bot author or co-author."""
    if not base_ref:
        return None
    try:
        result = subprocess.run(
            ["git", "log", f"{base_ref}..HEAD", "--format=%aN <%aE>%n%B"],
            capture_output=True, text=True, timeout=30,
        )
        if result.returncode != 0:
            return None
        if _BOT_AUTHOR_RE.search(result.stdout):
            return BOT_MSG
    except Exception as exc:
        logging.warning("check_bot_coauthors error: %s", exc)
    return None


def check_readme(readme_failed):
    """Return a finding if the README check reported a failure."""
    if readme_failed == "true":
        return README_MSG
    return None


def write_findings(findings):
    """Write the findings list to the output JSON file."""
    with open(FINDINGS_PATH, "w") as f:
        json.dump(findings, f)


def main():
    findings = []
    critical = False
    try:
        title = os.environ.get("PR_TITLE", "")
        body = os.environ.get("PR_BODY", "")
        draft = os.environ.get("PR_DRAFT", "false")
        readme_failed = os.environ.get("README_FAILED", "false")
        base_ref = os.environ.get("BASE_REF", "")

        finding = check_bot_coauthors(base_ref)
        if finding:
            findings.append(finding)

        finding = check_title(title)
        if finding:
            findings.append({"msg": finding, "level": "error"})
            critical = True

        finding = check_draft(draft)
        if finding:
            findings.append(finding)

        if not body or not body.strip():
            findings.append({"msg": TEMPLATE_MSG, "level": "error"})
            critical = True
        else:
            finding = check_template(body)
            if finding:
                findings.append({"msg": finding, "level": "error"})
                critical = True
            finding = check_checkboxes(body)
            if finding:
                findings.append({"msg": finding, "level": "error"})
                critical = True

        finding = check_readme(readme_failed)
        if finding:
            findings.append({"msg": finding, "level": "error"})
    except Exception as exc:
        logging.error("Unhandled error in main: %s", exc, exc_info=True)

    logging.info("Writing %d finding(s) to %s", len(findings), FINDINGS_PATH)
    write_findings(findings)
    sys.exit(1 if critical else 0)


if __name__ == "__main__":
    main()
