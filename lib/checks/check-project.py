"""Checks project health: URL reachability, GitHub repo stars, activity, and author match."""

import json
import os
import sys
from datetime import datetime, timezone

import requests
import yaml

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(PROJECT_ROOT, "awesome-privacy.yml")
DIFF_PATH = "/tmp/pr-diff.json"
FINDINGS_PATH = "/tmp/findings-project.json"

TIMEOUT = 10
USER_AGENT = "awesome-privacy-ci/1.0"
MIN_STARS = 100
INACTIVE_DAYS = 90
MIN_AGE_DAYS = 120
AI_COMMIT_THRESHOLD = 5
AI_BOT_AUTHORS = [
    "noreply@anthropic.com",
    "devin-ai-integration[bot]",
]

LINK_MSG = (
    "Our automated checks were unable to verify the link(s) you included"
    " were reachable, so please double check this yourself"
)
AUTHOR_MSG = (
    "Looks like you are the author of this package. Please ensure that you"
    " have clearly disclosed this in your PR body for transparency"
)
STARS_MSG = (
    "It looks like your submission is adding a quite small project."
    " In some circumstances we may ask you to resubmit this once the project"
    " is more mature and has a proven track record of good practices and maintenance."
)
ACTIVITY_MSG = (
    "Please confirm that the project you are adding is actively maintained,"
    " as it looks to not have had any recent updates in the past 3 months."
)
MATURITY_MSG = (
    "This project appears to be quite new (created less than 4 months ago)."
    " Repositories should have a proven track record before listing."
)
AI_CODE_MSG = (
    "This project appears to contain AI-generated code."
    " Additional care will be needed when reviewing the submission."
)
FORK_MSG = (
    "The GitHub link in this listing is a fork."
    " Please confirm it's the correct (and actively maintained) repository"
)
LICENSE_MSG = (
    "There doesn't appear to be a license included in the project's GitHub repo"
)
ARCHIVED_MSG = (
    "The GitHub project linked has been archived."
    " Additions must be actively maintained."
)
SECURITY_MSG = (
    "This project has open security vulnerabilities (critical or high severity)"
    " flagged by GitHub Dependabot. Please verify these have been addressed"
)


def load_diff(path):
    """Load the diff JSON, returning None on any error."""
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return None


def check_url(url):
    """Return True if the URL is reachable, True on any error (no false positives)."""
    try:
        resp = requests.head(
            url, timeout=TIMEOUT, allow_redirects=True,
            headers={"User-Agent": USER_AGENT},
        )
        if resp.status_code >= 400:
            resp = requests.get(
                url, timeout=TIMEOUT, allow_redirects=True,
                headers={"User-Agent": USER_AGENT}, stream=True,
            )
            resp.close()
        return resp.status_code < 400
    except Exception:
        return True


def parse_github_field(value):
    """Parse a github field into (owner, repo), or (None, None) on failure."""
    if not value:
        return None, None
    if value.startswith("https://github.com/"):
        parts = value.removeprefix("https://github.com/").strip("/").split("/")
        if len(parts) >= 2:
            return parts[0], parts[1]
        return None, None
    if "/" in value:
        parts = value.split("/")
        if len(parts) == 2:
            return parts[0], parts[1]
    return None, None


def fetch_repo(owner, repo, token):
    """Fetch GitHub repo metadata, returning None on any error."""
    try:
        headers = {"Accept": "application/vnd.github.v3+json", "User-Agent": USER_AGENT}
        if token:
            headers["Authorization"] = f"token {token}"
        resp = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}",
            headers=headers, timeout=TIMEOUT,
        )
        if resp.status_code == 200:
            return resp.json()
    except Exception:
        pass
    return None


def load_yaml_data():
    """Load the head YAML, returning None on any error."""
    try:
        with open(DATA_PATH) as f:
            return yaml.safe_load(f)
    except Exception:
        return None


def find_service_in_head(head, category, section, service_name):
    """Look up a service in the head YAML by path."""
    if not head:
        return None
    for cat in head.get("categories", []):
        if cat.get("name") == category:
            for sec in cat.get("sections", []):
                if sec.get("name") == section:
                    for svc in sec.get("services", []):
                        if svc.get("name") == service_name:
                            return svc
    return None


def get_services(diff, key):
    """Safely extract a service list from the diff."""
    return diff.get("services", {}).get(key, [])


def check_links(diff, head):
    """Return LINK_MSG if any service URL or icon URL is unreachable."""
    for svc in get_services(diff, "added"):
        fields = svc.get("fields", {})
        url = fields.get("url")
        if url and not check_url(url):
            return LINK_MSG
        icon = fields.get("icon")
        if icon and not check_url(icon):
            return LINK_MSG
    for svc in get_services(diff, "modified"):
        changed = svc.get("changed_fields", [])
        if "url" not in changed and "icon" not in changed:
            continue
        head_svc = find_service_in_head(
            head, svc["category"], svc["section"], svc["service"]
        )
        if head_svc:
            if "url" in changed:
                url = head_svc.get("url")
                if url and not check_url(url):
                    return LINK_MSG
            if "icon" in changed:
                icon = head_svc.get("icon")
                if icon and not check_url(icon):
                    return LINK_MSG
    return None


def check_ai_commits(owner, repo, token):
    """Return AI_CODE_MSG if recent commits contain significant AI bot activity."""
    try:
        headers = {"Accept": "application/vnd.github.v3+json", "User-Agent": USER_AGENT}
        if token:
            headers["Authorization"] = f"token {token}"
        resp = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/commits",
            headers=headers, timeout=TIMEOUT, params={"per_page": 100},
        )
        if resp.status_code != 200:
            return None
        bot_set = {a.lower() for a in AI_BOT_AUTHORS}
        count = 0
        for commit in resp.json():
            author = commit.get("commit", {}).get("author", {})
            email = (author.get("email") or "").lower()
            name = (author.get("name") or "").lower()
            if email in bot_set or name in bot_set:
                count += 1
        if count >= AI_COMMIT_THRESHOLD:
            return AI_CODE_MSG
    except Exception:
        pass
    return None


def check_security_alerts(owner, repo, token):
    """Return SECURITY_MSG if the repo has open critical/high Dependabot alerts."""
    try:
        headers = {"Accept": "application/vnd.github.v3+json", "User-Agent": USER_AGENT}
        if token:
            headers["Authorization"] = f"token {token}"
        resp = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/dependabot/alerts",
            headers=headers, timeout=TIMEOUT,
            params={"state": "open", "severity": "critical,high", "per_page": 1},
        )
        if resp.status_code == 200 and resp.json():
            return SECURITY_MSG
    except Exception:
        pass
    return None


def check_repo_signals(diff, pr_user, token):
    """Check GitHub repo author match, stars, and activity for added services."""
    findings = []
    if not token:
        return findings
    cache = {}
    for svc in get_services(diff, "added"):
        gh = svc.get("fields", {}).get("github")
        owner, repo = parse_github_field(gh)
        if not owner:
            continue
        cache_key = f"{owner}/{repo}"
        if cache_key not in cache:
            cache[cache_key] = fetch_repo(owner, repo, token)
        data = cache[cache_key]
        if not data:
            continue

        repo_owner = data.get("owner", {})
        if (
            pr_user
            and repo_owner.get("type") == "User"
            and repo_owner.get("login", "").lower() == pr_user.lower()
            and AUTHOR_MSG not in findings
        ):
            findings.append(AUTHOR_MSG)

        stars = data.get("stargazers_count", 0)
        if stars < MIN_STARS and STARS_MSG not in findings:
            findings.append(STARS_MSG)

        if data.get("fork") and FORK_MSG not in findings:
            findings.append(FORK_MSG)

        if not data.get("license") and LICENSE_MSG not in findings:
            findings.append(LICENSE_MSG)

        if data.get("archived") and ARCHIVED_MSG not in findings:
            findings.append(ARCHIVED_MSG)

        pushed = data.get("pushed_at")
        if pushed and ACTIVITY_MSG not in findings:
            try:
                pushed_dt = datetime.fromisoformat(pushed.replace("Z", "+00:00"))
                now = datetime.now(timezone.utc)
                if (now - pushed_dt).days > INACTIVE_DAYS:
                    findings.append(ACTIVITY_MSG)
            except Exception:
                pass

        created = data.get("created_at")
        if created and MATURITY_MSG not in findings:
            try:
                created_dt = datetime.fromisoformat(created.replace("Z", "+00:00"))
                now = datetime.now(timezone.utc)
                if (now - created_dt).days < MIN_AGE_DAYS:
                    findings.append(MATURITY_MSG)
            except Exception:
                pass

        if AI_CODE_MSG not in findings:
            finding = check_ai_commits(owner, repo, token)
            if finding:
                findings.append(finding)

        if SECURITY_MSG not in findings:
            finding = check_security_alerts(owner, repo, token)
            if finding:
                findings.append(finding)

    return findings


def main():
    findings = []
    try:
        diff = load_diff(DIFF_PATH)
        if not diff:
            with open(FINDINGS_PATH, "w") as f:
                json.dump(findings, f)
            sys.exit(0)

        head = load_yaml_data()
        finding = check_links(diff, head)
        if finding:
            findings.append(finding)

        pr_user = os.environ.get("PR_USER", "")
        token = os.environ.get("GITHUB_TOKEN", "")
        findings.extend(check_repo_signals(diff, pr_user, token))
    except Exception:
        pass

    with open(FINDINGS_PATH, "w") as f:
        json.dump(findings, f)
    sys.exit(0)


if __name__ == "__main__":
    main()
