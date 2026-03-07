"""Decides whether a PR is ready for maintainer review.

Conditions: 2+ approvals from external contributors AND all CI checks passing.

Reads:
  pr-meta/reviews.json       — array of {user, state} from GitHub API
  pr-meta/check-runs.json    — array of {status, conclusion} from GitHub API
  pr-meta/already-notified.txt — "true" if notification comment already exists

Writes:
  pr-meta/action.txt         — "notify" or "skip"
"""

import json
import os

WORK_DIR = "pr-meta"
MAINTAINER = "Lissy93"
REQUIRED_APPROVALS = 2
PASSING_CONCLUSIONS = {"success", "skipped", "neutral"}


def read_json(filename):
    """Load a JSON file from the work directory, or empty list on error."""
    try:
        with open(os.path.join(WORK_DIR, filename)) as f:
            return json.load(f)
    except Exception:
        return []


def count_external_approvals(reviews):
    """Count unique non-maintainer users who approved."""
    approvers = {
        r["user"]
        for r in reviews
        if r.get("state") == "APPROVED"
        and r.get("user", "").lower() != MAINTAINER.lower()
    }
    return len(approvers)


def all_checks_passing(check_runs):
    """Return True if every check run completed successfully."""
    if not check_runs:
        return False
    return all(
        cr.get("status") == "completed"
        and cr.get("conclusion") in PASSING_CONCLUSIONS
        for cr in check_runs
    )


def already_notified():
    """Return True if the notification comment already exists on the PR."""
    try:
        with open(os.path.join(WORK_DIR, "already-notified.txt")) as f:
            return f.read().strip().lower() == "true"
    except Exception:
        return False


def write_action(action):
    os.makedirs(WORK_DIR, exist_ok=True)
    with open(os.path.join(WORK_DIR, "action.txt"), "w") as f:
        f.write(action)


def main():
    if already_notified():
        write_action("skip")
        return

    reviews = read_json("reviews.json")
    approvals = count_external_approvals(reviews)

    if approvals < REQUIRED_APPROVALS:
        write_action("skip")
        return

    check_runs = read_json("check-runs.json")
    if not all_checks_passing(check_runs):
        write_action("skip")
        return

    write_action("notify")


if __name__ == "__main__":
    main()
