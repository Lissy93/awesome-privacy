"""
Fails if the PR directly edits the auto-generated section of the README.
The generated section is between <!-- awesome-privacy-start --> and <!-- awesome-privacy-end -->.
"""

import argparse
import os
import re
import subprocess
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
README_PATH = ".github/README.md"
README_ABS = os.path.join(PROJECT_ROOT, README_PATH)

# Exit codes
EXIT_PASS = 0
EXIT_FAIL = 1
EXIT_RUNTIME_ERROR = 2

# ANSI color helpers
_use_color = sys.stderr.isatty() and not os.environ.get("NO_COLOR")
red = (lambda s: f"\033[31m{s}\033[0m") if _use_color else (lambda s: s)
green = (lambda s: f"\033[32m{s}\033[0m") if _use_color else (lambda s: s)


def get_changed_files(base_ref):
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{base_ref}..HEAD"],
        capture_output=True, text=True, check=True,
        cwd=PROJECT_ROOT,
    )
    return result.stdout.strip().splitlines()


def get_marker_lines():
    """Find the line numbers of the start/end markers in the README."""
    try:
        with open(README_ABS, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return None, None

    start_line = None
    end_line = None
    for i, line in enumerate(lines, start=1):
        if "<!-- awesome-privacy-start -->" in line:
            start_line = i
        if "<!-- awesome-privacy-end -->" in line:
            end_line = i

    return start_line, end_line


def get_changed_line_numbers(base_ref):
    """Parse git diff hunk headers to find which lines were changed in the README."""
    result = subprocess.run(
        ["git", "diff", "-U0", f"{base_ref}..HEAD", "--", README_PATH],
        capture_output=True, text=True, check=True,
        cwd=PROJECT_ROOT,
    )

    changed_lines = []
    for line in result.stdout.splitlines():
        # Match hunk headers like @@ -10,5 +12,7 @@
        match = re.match(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@", line)
        if match:
            start = int(match.group(1))
            count = int(match.group(2)) if match.group(2) else 1
            for n in range(start, start + count):
                changed_lines.append(n)

    return changed_lines


def write_step_summary():
    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_file:
        return

    lines = [
        "## Direct README Edit Detected\n",
        "This PR directly modifies the auto-generated section of `.github/README.md` "
        "(between `<!-- awesome-privacy-start -->` and `<!-- awesome-privacy-end -->`).\n",
        "**Please edit `awesome-privacy.yml` instead.** The README is regenerated automatically from that file.\n",
    ]

    with open(summary_file, "a") as f:
        f.write("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Check for direct README edits to generated section")
    parser.add_argument("--base-ref", required=True, help="Base git ref to diff against")
    args = parser.parse_args()

    # Skip if README wasn't changed
    changed_files = get_changed_files(args.base_ref)
    if README_PATH not in changed_files:
        print(green("README not modified, skipping."))
        sys.exit(EXIT_PASS)

    # Find marker lines
    start_line, end_line = get_marker_lines()
    if start_line is None or end_line is None:
        print("Could not find generated-section markers in README, skipping check.")
        sys.exit(EXIT_PASS)

    # Check if any changed lines fall within the generated section
    changed_lines = get_changed_line_numbers(args.base_ref)
    for line_num in changed_lines:
        if start_line <= line_num <= end_line:
            print(red("Direct edits to the generated section of the README are not allowed."), file=sys.stderr)
            print(red("Edit awesome-privacy.yml instead and the README will be regenerated."), file=sys.stderr)
            write_step_summary()
            sys.exit(EXIT_FAIL)

    print(green("README changes are outside the generated section, OK."))
    sys.exit(EXIT_PASS)


if __name__ == "__main__":
    main()
