"""Aggregates findings from all check jobs into a formatted PR comment."""

import json
import os
import sys

ARTIFACTS_DIR = "/tmp/artifacts"
OUTPUT_DIR = "/tmp/pr-meta"

REPO_URL = "https://github.com/Lissy93/awesome-privacy"
CONTRIBUTING = f"{REPO_URL}/blob/main/.github/CONTRIBUTING.md"
DIFF_SUMMARY_PATH = os.path.join(ARTIFACTS_DIR, "pr-diff-summary.md")


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


def load_diff_summary():
    """Load the pre-formatted diff summary, or None if unavailable."""
    try:
        with open(DIFF_SUMMARY_PATH) as f:
            content = f.read().strip()
            return content if content else None
    except Exception:
        return None


def format_comment(findings, user, changes_summary, run_id):
    """Build the markdown comment."""
    parts = [
        f"<!-- pr-check-bot -->\nHello @{user}\n",
        f"Thank you for contributing to Awesome Privacy! We will review your "
        f"submission shortly. In the meantime, please ensure all changes are "
        f"correct and inline with our [Contributing Requirements]({CONTRIBUTING}).\n",
    ]

    if findings:
        bullet_list = "\n".join(f"- {f}" for f in findings)
        parts.append(
            f"Our automated checks detected some issues:\n\n{bullet_list}\n\n"
            f"> [!NOTE]\n"
            f"> I am a bot, and sometimes make mistakes in my suggestions. "
            f"But a human will review your submission shortly!"
        )
    else:
        parts.append("> ✅ All our automated checks have passed.")

    if changes_summary:
        parts.append(
            f"<details><summary>Summary of Changes:</summary>\n\n"
            f"{changes_summary}\n</details>"
        )

    if run_id:
        parts.append(
            f'<sup>For full details, please see workflow run '
            f'<a href="{REPO_URL}/actions/runs/{run_id}">{run_id}</a></sup>'
        )

    return "\n\n".join(parts) + "\n"


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
        with open(os.path.join(OUTPUT_DIR, "findings-count.txt"), "w") as f:
            f.write(str(len(findings)))
        changes_summary = load_diff_summary()
        write_step_summary(findings)

        comment = format_comment(findings, user, changes_summary, run_id)
        with open(os.path.join(OUTPUT_DIR, "comment.md"), "w") as f:
            f.write(comment)
    except Exception:
        pass

    sys.exit(0)


if __name__ == "__main__":
    main()
