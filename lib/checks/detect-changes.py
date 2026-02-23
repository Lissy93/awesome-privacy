"""
Detects which files changed between the PR base and HEAD.
Sets GitHub Actions output: yaml_changed.
"""

import argparse
import os
import subprocess
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

YAML_FILE = "awesome-privacy.yml"


def write_github_output(name, value):
    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a") as f:
            f.write(f"{name}={value}\n")


def main():
    parser = argparse.ArgumentParser(description="Detect changed files in a PR")
    parser.add_argument("--base-ref", required=True, help="Base git ref to diff against")
    args = parser.parse_args()

    result = subprocess.run(
        ["git", "diff", "--name-only", f"{args.base_ref}..HEAD"],
        capture_output=True, text=True, check=True,
        cwd=PROJECT_ROOT,
    )

    changed_files = [f for f in result.stdout.strip().splitlines() if f]

    print("Changed files:")
    for f in changed_files:
        print(f"  {f}")

    yaml_changed = YAML_FILE in changed_files
    write_github_output("yaml_changed", str(yaml_changed).lower())
    print(f"yaml_changed={yaml_changed}")


if __name__ == "__main__":
    main()
