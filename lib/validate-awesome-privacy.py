import json
import os
import sys

import yaml
from jsonschema import Draft7Validator

# Paths (relative to project root)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(PROJECT_ROOT, "awesome-privacy.yml")
SCHEMA_PATH = os.path.join(PROJECT_ROOT, "lib/schema.json")

# Exit codes
EXIT_VALID = 0
EXIT_VALIDATION_ERRORS = 1
EXIT_RUNTIME_ERROR = 2

MAX_ERRORS = 20

# ANSI color helpers (disabled when NO_COLOR is set or stderr is not a TTY)
_use_color = sys.stderr.isatty() and not os.environ.get("NO_COLOR")
red = (lambda s: f"\033[31m{s}\033[0m") if _use_color else (lambda s: s)
green = (lambda s: f"\033[32m{s}\033[0m") if _use_color else (lambda s: s)
yellow = (lambda s: f"\033[33m{s}\033[0m") if _use_color else (lambda s: s)
dim = (lambda s: f"\033[2m{s}\033[0m") if _use_color else (lambda s: s)


def resolve_path(data, path_parts):
    """Walk the data along path_parts, replacing indices with 'name' values."""
    segments = []
    current = data
    for part in path_parts:
        if isinstance(current, dict) and part in current:
            current = current[part]
            if isinstance(current, dict) and "name" in current:
                segments.append(current["name"])
            elif not isinstance(part, int):
                pass  # skip dict keys like 'categories', 'sections', 'services'
        elif isinstance(current, list) and isinstance(part, int) and part < len(current):
            current = current[part]
            if isinstance(current, dict) and "name" in current:
                segments.append(current["name"])
            else:
                segments.append(str(part))
        else:
            segments.append(str(part))
            break
    return " > ".join(segments) if segments else "(root)"


def load_yaml(path):
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(red(f"File not found: {path}"), file=sys.stderr)
        sys.exit(EXIT_RUNTIME_ERROR)
    except yaml.YAMLError as e:
        print(red(f"Failed to parse YAML: {e}"), file=sys.stderr)
        sys.exit(EXIT_RUNTIME_ERROR)


def load_schema(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(red(f"File not found: {path}"), file=sys.stderr)
        sys.exit(EXIT_RUNTIME_ERROR)
    except json.JSONDecodeError as e:
        print(red(f"Failed to parse JSON schema: {e}"), file=sys.stderr)
        sys.exit(EXIT_RUNTIME_ERROR)


def validate(data, schema):
    validator = Draft7Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
    formatted = []
    for error in errors:
        location = resolve_path(data, list(error.path))
        formatted.append(f"{location}: {error.message}")
    return formatted


def main():
    data = load_yaml(DATA_PATH)
    schema = load_schema(SCHEMA_PATH)
    errors = validate(data, schema)

    if errors:
        shown = errors[:MAX_ERRORS]
        for msg in shown:
            print(red("ERROR") + " " + msg, file=sys.stderr)
        if len(errors) > MAX_ERRORS:
            print(dim(f"...and {len(errors) - MAX_ERRORS} more"), file=sys.stderr)
        print(red(f"Validation failed: {len(errors)} error(s)"), file=sys.stderr)
        sys.exit(EXIT_VALIDATION_ERRORS)

    # Gather stats
    categories = data.get("categories", [])
    num_categories = len(categories)
    num_sections = sum(len(c.get("sections", [])) for c in categories)
    num_services = sum(
        len(s.get("services", []))
        for c in categories
        for s in c.get("sections", [])
    )
    print(green(f"Valid! {num_categories} categories, {num_sections} sections, {num_services} services"))
    sys.exit(EXIT_VALID)


if __name__ == "__main__":
    main()
