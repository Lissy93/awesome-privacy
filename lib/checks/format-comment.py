"""Aggregates findings from all check jobs into a formatted PR comment."""

import json
import os
import sys

ARTIFACTS_DIR = "/tmp/artifacts"
OUTPUT_DIR = "/tmp/pr-meta"

CONTRIBUTING = "https://github.com/Lissy93/awesome-privacy/blob/main/.github/CONTRIBUTING.md"

COMMENT_TEMPLATE = """<!-- pr-check-bot -->
Hello @{user}

Thank you for contributing to Awesome Privacy! We will review your PR shortly. In the meantime, please ensure that your submission is inline with our guidelines in our [Contributing Requirements]({contributing}).

Looks like there could be some issues in your PR. Please double check that:

{findings}

> [!NOTE]
> I am a bot, and sometimes make mistakes in my suggestions. But a human will review your submission shortly!"""


def load_findings(filename):
    """Load a findings JSON array from the artifacts directory, or empty list on error."""
    try:
        with open(os.path.join(ARTIFACTS_DIR, filename)) as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception:
        return []


def collect_findings():
    """Gather all findings in display order: compliance, data, project."""
    all_findings = []
    all_findings.extend(load_findings("findings-compliance.json"))
    all_findings.extend(load_findings("findings-data.json"))
    all_findings.extend(load_findings("findings-project.json"))
    return all_findings


def format_comment(findings, user):
    """Build the markdown comment from findings."""
    bullet_list = "\n".join(f"- {f}" for f in findings)
    return COMMENT_TEMPLATE.format(
        user=user, contributing=CONTRIBUTING, findings=bullet_list,
    )


def write_step_summary(findings):
    """Write a summary to GITHUB_STEP_SUMMARY."""
    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_file:
        return
    lines = ["## PR Check Summary\n"]
    if findings:
        lines.append(f"⚠️ Found {len(findings)} issue(s):\n")
        for f in findings:
            lines.append(f"- {f}")
    else:
        lines.append("✅ All checks passed.\n")
    with open(summary_file, "a") as f:
        f.write("\n".join(lines) + "\n")


def main():
    try:
        user = os.environ.get("PR_USER", "contributor")
        pr_number = os.environ.get("PR_NUMBER", "")
        run_id = os.environ.get("RUN_ID", "")

        os.makedirs(OUTPUT_DIR, exist_ok=True)

        if pr_number:
            with open(os.path.join(OUTPUT_DIR, "number.txt"), "w") as f:
                f.write(pr_number)
        if run_id:
            with open(os.path.join(OUTPUT_DIR, "run-id.txt"), "w") as f:
                f.write(run_id)

        findings = collect_findings()
        write_step_summary(findings)

        if findings:
            comment = format_comment(findings, user)
            with open(os.path.join(OUTPUT_DIR, "comment.md"), "w") as f:
                f.write(comment)
    except Exception:
        pass

    sys.exit(0)


if __name__ == "__main__":
    main()
