"""Checks project health: URL reachability, GitHub repo stars, activity, and author match."""

import json
import logging
import os
import re
import sys
from datetime import datetime, timedelta, timezone

import requests
import yaml

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s [%(filename)s] %(message)s",
    stream=sys.stderr,
)

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(PROJECT_ROOT, "awesome-privacy.yml")
DIFF_PATH = "/tmp/pr-diff.json"
FINDINGS_PATH = "/tmp/findings-project.json"

TIMEOUT = 10
USER_AGENT = "awesome-privacy-ci/1.0"
MIN_STARS = 100
INACTIVE_DAYS = 90
MIN_AGE_DAYS = 120
AI_COMMIT_RATIO = 0.2
AI_BOT_AUTHORS = [
    "noreply@anthropic.com",
    "devin-ai-integration[bot]",
    "copilot-swe-agent.github.com",
    "noreply@cursor.com",
]
SPAM_AWESOME_THRESHOLD = 3
SPAM_DISTINCT_REPO_THRESHOLD = 7
SPAM_WINDOW_DAYS = 2
NEW_ACCOUNT_DAYS = 14

LINK_MSG = (
    "The link(s) you included seem to be returning a 404."
    " Please double check all URLs listed are valid and publicly accessible"
)
AUTHOR_MSG = (
    "Looks like you are the author of this package. Please ensure that you"
    " have clearly disclosed this in your PR body for transparency"
)
STARS_MSG = (
    "It looks like your submission is quite a small project without a lot of users yet."
    " In some circumstances we may ask you to resubmit this once the project"
    " is more mature and has a proven track record of good practices and maintenance."
)
ACTIVITY_MSG = (
    "Please confirm that the project you are adding is actively maintained,"
    " as it looks to not have had any recent updates in the past 3 months."
)
MATURITY_MSG = (
    "This project appears to be quite new (created less than 4 months ago)."
    " Repositories should have a proven track record before listing,"
    " and at least 16 weeks since first stable release."
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
    " Additions must be actively maintained"
)
SECURITY_MSG = (
    "This project has open security vulnerabilities (critical or high severity)"
    " flagged by GitHub Dependabot. Please verify these have been addressed"
)
SPAM_AWESOME_MSG = (
    "You have made many similar submissions on other awesome-* repos today."
    " Please ensure that your submission is actually a good fit for awesome-privacy"
)
SPAM_MANY_MSG = (
    "The submitter of this PR appears to have been previously flagged as a spammer."
    " Caution is needed when reviewing this PR"
)
NEW_ACCOUNT_MSG = (
    "This user has only just joined GitHub."
    " New accounts submitting to awesome lists can be a spam signal, careful review needed"
)
DUPLICATE_URL_MSG = (
    "The URL for this submission already exists in another listing."
    " Please check that this is not a duplicate entry"
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
        if resp.status_code >= 400:
            logging.warning("URL check failed for %s (HTTP %d)", url, resp.status_code)
        return resp.status_code < 400
    except Exception as exc:
        logging.warning("URL check error for %s: %s", url, exc)
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


def _gh_get(path, token, params=None, label=""):
    """GET a GitHub API endpoint. Returns parsed JSON on 200, None otherwise."""
    headers = {"Accept": "application/vnd.github.v3+json", "User-Agent": USER_AGENT}
    if token:
        headers["Authorization"] = f"token {token}"
    try:
        resp = requests.get(
            f"https://api.github.com{path}",
            headers=headers, timeout=TIMEOUT, params=params,
        )
        remaining = resp.headers.get("X-RateLimit-Remaining")
        if remaining is not None:
            try:
                if int(remaining) < 100:
                    logging.warning("[%s] GitHub rate limit low: %s/%s remaining",
                                    label, remaining, resp.headers.get("X-RateLimit-Limit"))
            except ValueError:
                pass
        if resp.status_code == 200:
            return resp.json()
        logging.warning("[%s] HTTP %d from %s", label, resp.status_code, path)
    except Exception as exc:
        logging.warning("[%s] request error for %s: %s", label, path, exc)
    return None


def fetch_repo(owner, repo, token):
    """Fetch GitHub repo metadata, returning None on any error."""
    return _gh_get(f"/repos/{owner}/{repo}", token, label="repos")


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


def _commit_has_bot(commit, bot_set):
    """Check if a commit was authored or co-authored by a known AI bot."""
    author = commit.get("commit", {}).get("author", {})
    email = (author.get("email") or "").lower()
    name = (author.get("name") or "").lower()
    if email in bot_set or name in bot_set:
        return True
    message = (commit.get("commit", {}).get("message") or "").lower()
    for line in message.splitlines():
        if line.strip().startswith("co-authored-by:"):
            if any(bot in line for bot in bot_set):
                return True
    return False


def check_ai_commits(owner, repo, token):
    """Return AI_CODE_MSG if recent commits contain significant AI bot activity."""
    commits = _gh_get(f"/repos/{owner}/{repo}/commits", token,
                      params={"per_page": 100}, label="commits")
    if not commits:
        return None
    bot_set = {a.lower() for a in AI_BOT_AUTHORS}
    count = sum(1 for c in commits if _commit_has_bot(c, bot_set))
    if count / len(commits) >= AI_COMMIT_RATIO:
        return AI_CODE_MSG
    return None


def check_security_alerts(owner, repo, token):
    """Return SECURITY_MSG if the repo has open critical/high Dependabot alerts."""
    alerts = _gh_get(f"/repos/{owner}/{repo}/dependabot/alerts", token,
                     params={"state": "open", "severity": "critical,high", "per_page": 1},
                     label="dependabot")
    if alerts:
        return SECURITY_MSG
    return None


def check_spam_prs(pr_user, token):
    """Return list of spam findings based on recent PR activity."""
    if not pr_user or not token:
        logging.warning("check_spam_prs skipped: %s", "no PR_USER" if not pr_user else "no GITHUB_TOKEN")
        return []
    try:
        since = (datetime.now(timezone.utc) - timedelta(days=SPAM_WINDOW_DAYS)).strftime("%Y-%m-%d")
        data = _gh_get("/search/issues", token,
                       params={"q": f"type:pr author:{pr_user} created:>={since}", "per_page": 100},
                       label="spam")
        if not data:
            return []
        items = data.get("items", [])
        logging.info("check_spam_prs: %d total PRs for %s (fetched %d)",
                     data.get("total_count", 0), pr_user, len(items))
        this_repo = os.environ.get("GITHUB_REPOSITORY", "Lissy93/awesome-privacy").lower()
        awesome_count = 0
        distinct_repos = set()
        for item in items:
            repo_url = item.get("repository_url", "")
            # repository_url looks like https://api.github.com/repos/owner/repo-name
            repo_full = "/".join(repo_url.rstrip("/").split("/")[-2:]).lower()
            if repo_full == this_repo:
                continue
            distinct_repos.add(repo_full)
            repo_name = repo_url.rstrip("/").split("/")[-1].lower()
            if repo_name.startswith("awesome-"):
                awesome_count += 1
        logging.info("check_spam_prs: %d awesome-* PRs, %d distinct repos",
                     awesome_count, len(distinct_repos))
        findings = []
        if awesome_count >= SPAM_AWESOME_THRESHOLD:
            findings.append(SPAM_AWESOME_MSG)
        if len(distinct_repos) >= SPAM_DISTINCT_REPO_THRESHOLD:
            findings.append(SPAM_MANY_MSG)
        return findings
    except Exception as exc:
        logging.warning("check_spam_prs error for %s: %s", pr_user, exc)
        return []


def check_new_account(pr_user, token):
    """Return NEW_ACCOUNT_MSG if the PR author's GitHub account is very new."""
    if not pr_user or not token:
        return None
    data = _gh_get(f"/users/{pr_user}", token, label="user")
    if not data:
        return None
    created = data.get("created_at")
    if not created:
        return None
    try:
        created_dt = datetime.fromisoformat(created.replace("Z", "+00:00"))
        if (datetime.now(timezone.utc) - created_dt).days < NEW_ACCOUNT_DAYS:
            return NEW_ACCOUNT_MSG
    except Exception:
        pass
    return None


def check_duplicate_urls(diff, head):
    """Return DUPLICATE_URL_MSG if an added service's URL already exists in the YAML."""
    if not head:
        return None
    # Count how many times each URL appears in the head YAML
    url_counts = {}
    for cat in head.get("categories", []):
        for sec in cat.get("sections", []):
            for svc in sec.get("services", []):
                url = svc.get("url", "").rstrip("/").lower()
                if url:
                    url_counts[url] = url_counts.get(url, 0) + 1
    # The added service is in head already, so a count > 1 means a duplicate exists
    for svc in get_services(diff, "added"):
        url = svc.get("fields", {}).get("url", "").rstrip("/").lower()
        if url and url_counts.get(url, 0) > 1:
            return DUPLICATE_URL_MSG
    return None


_DISCLOSURE_RE = re.compile(
    r"i am the author|i'm the author|my project|i created|i develop"
    r"|i maintain|i built|my own project|i made|author of|maintainer of",
    re.IGNORECASE,
)


def _pr_discloses_authorship(pr_body):
    """Return True if the PR body already discloses the submitter is the author."""
    return bool(pr_body and _DISCLOSURE_RE.search(pr_body))


def check_repo_signals(diff, pr_user, token, pr_body=""):
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
            and not _pr_discloses_authorship(pr_body)
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
        pr_user = os.environ.get("PR_USER", "")
        token = os.environ.get("GITHUB_TOKEN", "")
        logging.info("PR_USER=%s, GITHUB_TOKEN=%s", pr_user or "(empty)", "present" if token else "MISSING")

        diff = load_diff(DIFF_PATH)
        if not diff:
            logging.info("No diff file at %s, nothing to check", DIFF_PATH)
            with open(FINDINGS_PATH, "w") as f:
                json.dump(findings, f)
            sys.exit(0)

        head = load_yaml_data()
        finding = check_links(diff, head)
        if finding:
            findings.append(finding)

        pr_body = os.environ.get("PR_BODY", "")

        findings.extend(check_spam_prs(pr_user, token))

        finding = check_new_account(pr_user, token)
        if finding:
            findings.append(finding)

        finding = check_duplicate_urls(diff, head)
        if finding:
            findings.append(finding)

        findings.extend(check_repo_signals(diff, pr_user, token, pr_body))
    except Exception as exc:
        logging.error("Unhandled error in main: %s", exc, exc_info=True)

    logging.info("Writing %d finding(s) to %s", len(findings), FINDINGS_PATH)
    with open(FINDINGS_PATH, "w") as f:
        json.dump(findings, f)
    sys.exit(0)


if __name__ == "__main__":
    main()
