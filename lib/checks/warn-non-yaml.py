"""
Warns when a PR modifies files other than awesome-privacy.yml.
This is expected for Website Update or Misc PRs, but may need extra review.
"""

import argparse
import os
import subprocess
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

YAML_FILE = "awesome-privacy.yml"

# ANSI color helpers
_use_color = sys.stderr.isatty() and not os.environ.get("NO_COLOR")
yellow = (lambda s: f"\033[33m{s}\033[0m") if _use_color else (lambda s: s)


def main():
    parser = argparse.ArgumentParser(description="Warn about non-YAML file changes")
    parser.add_argument("--base-ref", required=True, help="Base git ref to diff against")
    args = parser.parse_args()

    result = subprocess.run(
        ["git", "diff", "--name-only", f"{args.base_ref}..HEAD"],
        capture_output=True, text=True, check=True,
        cwd=PROJECT_ROOT,
    )

    changed_files = [f for f in result.stdout.strip().splitlines() if f]
    non_yaml = [f for f in changed_files if f != YAML_FILE]

    if not non_yaml:
        return

    print(yellow("This PR modifies files other than awesome-privacy.yml:"), file=sys.stderr)
    for f in non_yaml:
        print(f"  {f}", file=sys.stderr)

    # Write step summary
    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_file:
        lines = [
            "## Non-YAML Changes Warning\n",
            "This PR modifies files other than `awesome-privacy.yml`:\n",
        ]
        for f in non_yaml:
            lines.append(f"- `{f}`")
        lines.append("")
        lines.append("> **Note:** Most PRs should only modify `awesome-privacy.yml`. "
                      "Non-YAML changes may require additional review.\n")
        with open(summary_file, "a") as f:
            f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
