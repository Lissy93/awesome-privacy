"""Validates data quality for added/modified services using the diff JSON."""

import json
import os
import sys

import yaml

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(PROJECT_ROOT, "awesome-privacy.yml")
DIFF_PATH = "/tmp/pr-diff.json"
FINDINGS_PATH = "/tmp/findings-data.json"

REQUIRED_FIELDS = ("name", "description", "url", "icon")

CONTRIBUTING = "https://github.com/Lissy93/awesome-privacy/blob/main/.github/CONTRIBUTING.md"

SCHEMA_MSG = (
    "Some of the schema checks have failed. Please check that your addition"
    " contains all the required fields, with acceptable values, nothing"
    " additional and that it is following valid YAML syntax"
)
MULTIPLE_MSG = "Please make just one addition per pull request"
MISSING_TPL = (
    "Did you include all required fields? Looks like {fields} is missing or"
    f" invalid. Please see the [required fields]({CONTRIBUTING}#service-fields)"
    " for available fields."
)
POSITION_MSG = (
    "New entries must be added to the end of the section, unless otherwise requested"
)
OPENSOURCE_MSG = (
    "You indicated this app/service is not open source. This will likely make"
    " it ineligible for listing on Awesome Privacy in accordance with our"
    f" [Requirements]({CONTRIBUTING}#requirements)."
    " Please ensure that this is justified in your PR body."
)


def load_json(path):
    """Load JSON from a file, returning None on any error."""
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return None


def load_yaml_data(path):
    """Load YAML from a file, returning None on any error."""
    try:
        with open(path) as f:
            return yaml.safe_load(f)
    except Exception:
        return None


def find_section_services(head, category, section):
    """Return the services list for a category/section pair, or None."""
    for cat in head.get("categories", []):
        if cat.get("name") == category:
            for sec in cat.get("sections", []):
                if sec.get("name") == section:
                    return sec.get("services", [])
    return None


def find_service_fields(head, category, section, service_name):
    """Look up a service's fields in the head YAML."""
    services = find_section_services(head, category, section)
    if services:
        for svc in services:
            if svc.get("name") == service_name:
                return svc
    return None


def check_required_fields(diff, head):
    """Return a finding if any added/modified service is missing required fields."""
    missing = set()
    for svc in diff.get("services", {}).get("added", []):
        fields = svc.get("fields", {})
        for f in REQUIRED_FIELDS:
            if not fields.get(f):
                missing.add(f)
    for svc in diff.get("services", {}).get("modified", []):
        if not head:
            continue
        fields = find_service_fields(
            head, svc["category"], svc["section"], svc["service"]
        )
        if fields:
            for f in REQUIRED_FIELDS:
                if not fields.get(f):
                    missing.add(f)
    if missing:
        names = ", ".join(f"`{f}`" for f in sorted(missing))
        return MISSING_TPL.format(fields=names)
    return None


def check_position(diff, head):
    """Return a finding if a newly added service is not at the end of its section."""
    if not head:
        return None
    for svc in diff.get("services", {}).get("added", []):
        services = find_section_services(head, svc["category"], svc["section"])
        if services and services[-1].get("name") != svc["service"]:
            return POSITION_MSG
    return None


def check_open_source(diff):
    """Return a finding if an added service has openSource missing or not true."""
    for svc in diff.get("services", {}).get("added", []):
        fields = svc.get("fields", {})
        if fields.get("openSource") is not True:
            return OPENSOURCE_MSG
    return None


def check_single_entry(diff):
    """Return a finding if the diff contains multiple service or section changes."""
    services = diff.get("services", {})
    svc_count = (
        len(services.get("added", []))
        + len(services.get("removed", []))
        + len(services.get("modified", []))
    )
    if svc_count > 1:
        return MULTIPLE_MSG
    if svc_count == 0:
        sec_count = len(diff.get("sections", []))
        if sec_count > 1:
            return MULTIPLE_MSG
    return None


def main():
    findings = []
    try:
        if os.environ.get("SCHEMA_OUTCOME") == "failure":
            findings.append(SCHEMA_MSG)

        diff = load_json(DIFF_PATH)
        head = load_yaml_data(DATA_PATH)

        if diff:
            finding = check_single_entry(diff)
            if finding:
                findings.append(finding)

            finding = check_required_fields(diff, head)
            if finding:
                findings.append(finding)

            finding = check_position(diff, head)
            if finding:
                findings.append(finding)

            finding = check_open_source(diff)
            if finding:
                findings.append(finding)
    except Exception:
        pass

    with open(FINDINGS_PATH, "w") as f:
        json.dump(findings, f)
    sys.exit(0)


if __name__ == "__main__":
    main()
