"""Aggregates findings from all check jobs into a formatted PR comment."""

import json
import os
import sys
from datetime import datetime, timezone

ARTIFACTS_DIR = "/tmp/artifacts"
OUTPUT_DIR = "/tmp/pr-meta"

REPO_URL = "https://github.com/Lissy93/awesome-privacy"
CONTRIBUTING = f"{REPO_URL}/blob/main/.github/CONTRIBUTING.md"
DIFF_SUMMARY_PATH = os.path.join(ARTIFACTS_DIR, "pr-diff-summary.md")
REPO_STATS_PATH = os.path.join(ARTIFACTS_DIR, "repo-stats.md")


def load_repo_stats():
    """Load the repo stats markdown, or None if unavailable."""
    try:
        with open(REPO_STATS_PATH) as f:
            content = f.read().strip()
            return content if content else None
    except Exception:
        return None


def load_findings(filename):
    """Load a findings JSON array from the artifacts directory, or empty list on error."""
    try:
        with open(os.path.join(ARTIFACTS_DIR, filename)) as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception:
        return []


def normalize_finding(f):
    """Return {"msg": str, "level": str} from a dict or plain string."""
    if isinstance(f, dict):
        return {"msg": str(f.get("msg", "")), "level": f.get("level", "warning")}
    return {"msg": str(f), "level": "warning"}


def collect_findings():
    """Gather all findings, split into (errors, warnings) lists of message strings."""
    raw = []
    raw.extend(load_findings("findings-compliance.json"))
    raw.extend(load_findings("findings-data.json"))
    raw.extend(load_findings("findings-project.json"))
    errors = []
    warnings = []
    for f in raw:
        normalized = normalize_finding(f)
        if normalized["level"] == "error":
            errors.append(normalized["msg"])
        else:
            warnings.append(normalized["msg"])
    return errors, warnings


def load_diff_summary():
    """Load the pre-formatted diff summary, or None if unavailable."""
    try:
        with open(DIFF_SUMMARY_PATH) as f:
            content = f.read().strip()
            return content if content else None
    except Exception:
        return None


def _extract_changes_bullets(diff_summary):
    """Re-format bullet lines from the diff summary with a blue circle prefix."""
    if not diff_summary:
        return None
    bullets = []
    for line in diff_summary.splitlines():
        if line.startswith("- "):
            bullets.append(f"- \U0001f535 {line[2:]}")
    return "\n".join(bullets) if bullets else None


def format_comment(findings, user, changes_summary, run_id, repo_stats=None):
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
        parts.append("> \u2705 All our automated checks have passed.")

    if changes_summary:
        parts.append(
            f"<details><summary>Summary of Changes:</summary>\n\n"
            f"{changes_summary}\n</details>"
        )

    if repo_stats:
        parts.append(
            f"<details><summary>Submission Info</summary>\n\n"
            f"{repo_stats}\n</details>"
        )

    if run_id:
        parts.append(
            f'<sup>For full details, please see workflow run '
            f'<a href="{REPO_URL}/actions/runs/{run_id}">{run_id}</a></sup>'
        )

    return "\n\n".join(parts) + "\n"


def write_step_summary(errors, warnings, user, pr_number, run_id, changes_summary,
                       repo_stats=None):
    """Write a structured summary to GITHUB_STEP_SUMMARY."""
    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_file:
        return

    lines = ["## Status Check Results\n"]

    # Summary sentence
    ne, nw = len(errors), len(warnings)
    lines.append("### Summary\n")
    if ne and nw:
        lines.append(
            f"There are {ne} error(s) which must be resolved before this PR can be"
            f" reviewed, as well as {nw} warning(s) which need to be addressed or"
            f" justified.\n"
        )
    elif ne:
        lines.append(
            f"There are {ne} error(s) which must be resolved before this PR can be"
            f" reviewed.\n"
        )
    elif nw:
        lines.append(
            f"There were no errors but {nw} warning(s) which need to be addressed"
            f" or justified before the PR can be merged.\n"
        )
    else:
        lines.append(
            "All checks are passing, with no errors and no warnings \U0001f389\n"
            "A maintainer has been notified, and will review the submission shortly.\n"
        )

    # Errors
    lines.append("### Errors\n")
    if errors:
        for e in errors:
            lines.append(f"- \U0001f534 {e}")
    else:
        lines.append("\u2705 None")
    lines.append("")

    # Warnings
    lines.append("### Warnings\n")
    if warnings:
        for w in warnings:
            lines.append(f"- \U0001f7e1 {w}")
    else:
        lines.append("\u2705 None")
    lines.append("")

    # Meta Info
    lines.append("### Meta Info\n")
    now = datetime.now(timezone.utc)
    timestamp = now.strftime("%H:%M UTC on %d %b %Y")
    if pr_number:
        lines.append(
            f"This workflow run was triggered at {timestamp}"
            f" for PR #{pr_number} which was opened by @{user}\n"
        )
    else:
        lines.append(
            f"This workflow run was triggered at {timestamp} by @{user}\n"
        )

    if changes_summary:
        lines.append("The PR introduces the following changes:\n")
        lines.append(f"{changes_summary}\n")

    if repo_stats:
        lines.append("#### Submission Info\n")
        lines.append(f"{repo_stats}\n")

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

        errors, warnings = collect_findings()
        all_findings = errors + warnings
        with open(os.path.join(OUTPUT_DIR, "findings-count.txt"), "w") as f:
            f.write(str(len(all_findings)))
        changes_summary = load_diff_summary()
        changes_bullets = _extract_changes_bullets(changes_summary)
        repo_stats = load_repo_stats()
        write_step_summary(errors, warnings, user, pr_number, run_id, changes_bullets,
                           repo_stats)

        comment = format_comment(all_findings, user, changes_summary, run_id, repo_stats)
        with open(os.path.join(OUTPUT_DIR, "comment.md"), "w") as f:
            f.write(comment)
    except Exception:
        pass

    sys.exit(0)


if __name__ == "__main__":
    main()
