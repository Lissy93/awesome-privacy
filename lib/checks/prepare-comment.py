"""Decides whether to create, update, or skip the PR bot comment.

Reads:
  pr-meta/comment.md          — new comment from format-comment.py
  pr-meta/findings-count.txt  — number of findings (from format-comment.py)
  pr-meta/existing-comment.md — current bot comment on the PR (from workflow)

Writes:
  pr-meta/action.txt          — "create", "update", or "skip"
  pr-meta/final-comment.md    — the body to post or update with
"""

import os
import re

WORK_DIR = "pr-meta"


def read_file(path):
    """Read a file and return its stripped content, or None if missing/empty."""
    try:
        with open(path) as f:
            content = f.read().strip()
            return content if content else None
    except Exception:
        return None


def read_findings_count(new_body):
    """Return the findings count from findings-count.txt, or by counting bullets."""
    raw = read_file(os.path.join(WORK_DIR, "findings-count.txt"))
    if raw is not None:
        try:
            return int(raw)
        except ValueError:
            pass
    # Fallback: count bullet lines before <details> (diff summary has its own bullets)
    body_before_details = new_body.split("<details>")[0]
    return len(re.findall(r"^- .+$", body_before_details, re.MULTILINE))


def _was_already_passing(existing_body):
    """Check if the most recent state in the comment is already all-clear."""
    # If there's a previous "all passing" edit, the last state was passing
    if re.search(r"^Edit(?: \d+)?: All checks are (now passing|passing now)", existing_body, re.MULTILINE):
        return True
    # If there are no edits at all, check the original comment body
    if not re.search(r"^Edit(?: \d+)?:", existing_body, re.MULTILINE):
        return "All our automated checks have passed" in existing_body
    return False


def _previous_failing_count(existing_body):
    """Extract the findings count from the most recent state in the comment."""
    # Check edit lines first (most recent state)
    matches = re.findall(r"^Edit(?: \d+)?: (\d+) checks? (?:is|are) still failing", existing_body, re.MULTILINE)
    if matches:
        return int(matches[-1])
    # No edits — count bullets in the original comment (before <details>)
    if not re.search(r"^Edit(?: \d+)?:", existing_body, re.MULTILINE):
        body_before_details = existing_body.split("<details>")[0]
        bullets = re.findall(r"^- .+$", body_before_details, re.MULTILINE)
        return len(bullets) if bullets else None
    return None


def build_edit_line(existing_body, findings_count, check_run_id, repo):
    """Build the edit line to append, or None if nothing to do."""
    run_tag = f"<!-- run:{check_run_id} -->"

    # Idempotency: this run was already processed
    if run_tag in existing_body:
        return None

    # Skip if the state hasn't changed
    if findings_count == 0 and _was_already_passing(existing_body):
        return None
    if findings_count > 0 and _previous_failing_count(existing_body) == findings_count:
        return None

    # Count previous edits to determine the next number
    edits = re.findall(r"^Edit(?: \d+)?:", existing_body, re.MULTILINE)
    edit_count = len(edits)
    next_edit = edit_count + 1

    run_url = f"https://github.com/{repo}/actions/runs/{check_run_id}"

    if findings_count == 0:
        if edit_count == 0:
            return f"Edit: All checks are now passing \U0001f389 {run_tag}"
        return f"Edit {next_edit}: All checks are passing now \u2705 {run_tag}"

    verb = "check is" if findings_count == 1 else "checks are"
    return (
        f"Edit {next_edit}: {findings_count} {verb} still failing, "
        f"see [here]({run_url}) for details {run_tag}"
    )


def write_output(action, body=""):
    """Write action.txt and (optionally) final-comment.md."""
    os.makedirs(WORK_DIR, exist_ok=True)
    with open(os.path.join(WORK_DIR, "action.txt"), "w") as f:
        f.write(action)
    if body:
        with open(os.path.join(WORK_DIR, "final-comment.md"), "w") as f:
            f.write(body)


def main():
    check_run_id = os.environ.get("CHECK_RUN_ID", "")
    repo = os.environ.get("GITHUB_REPOSITORY", "")

    new_body = read_file(os.path.join(WORK_DIR, "comment.md"))
    if not new_body:
        write_output("skip")
        return

    existing_body = read_file(os.path.join(WORK_DIR, "existing-comment.md"))

    # No existing comment — create a new one
    if not existing_body:
        write_output("create", new_body)
        return

    # Existing comment — build an edit line to append
    if not check_run_id:
        write_output("skip")
        return

    findings_count = read_findings_count(new_body)
    edit_line = build_edit_line(existing_body, findings_count, check_run_id, repo)

    if not edit_line:
        write_output("skip")
        return

    updated = existing_body.rstrip() + "\n\n" + edit_line
    write_output("update", updated)


if __name__ == "__main__":
    main()
