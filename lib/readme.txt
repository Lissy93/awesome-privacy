This directory contains all the core logic and automations for awesome-privacy.
Primarily used to process awesome-privacy, build the readme, and validate PRs.

For some background, all listing data lives in awesome-privacy.yml.
This file is the single source of truth, used to:
- Populate the list in the readme
- Build the pages in the website
- Power the database for the API


Usage
-----
From the root of this project, run:
- `make install_lib_deps` for pip install
- `make validate` to validate all data
- `make gen_readme` to build the readme


Scripts and Files Listing
-------------------------
awesome-privacy-readme-gen.py
  > Generates and inserts readme content for all listings into the readme
validate-awesome-privacy.py
  > Validates awesome-privacy.yml against schema.json
schema.json
  > The JSON Schema defining the structure and data types of awesome-privacy.yml.
requirements.txt
  > Python dependencies (Just PyYAML, jsonschema and requests)
checks/
  > Scripts which run via GH Actions, when PRs are opened to validate submissions

File listing for lib/checks/
  detect-changes.py
    > Checks if and what was changed in awesome-privacy.yml
  check-readme-edits.py
    > Sanity check to fail PRs modifying parts of the readme directly
  check-pr-meta.py
    > Validates PR title and body to ensure required info is specified
  check-yaml-diff.py
    > Diffs the base and head versions of awesome-privacy.yml, and builds an index
  check-additions.py
    > Validates additions against data quality rules / requirements
  check-project.py
    > Checks project health (URL reachability, repo health, security alerts, etc)
  make-info-stats.py
    > Fetches contextual info about submitted services for reviewer convenience.
  format-comment.py
    > Collects all findings from the three check jobs, and assembles the PR comment
  prepare-comment.py
    > Decides whether to create, update, or skip the bot comment on the PR.
  check-review-ready.py
    > Assigns maintainers to review, once all essential checks pass


License
-------
Licensed under MIT © Alicia Sykes <alicia@omg.lol> 2026
https://github.com/Lissy93/awesome-privacy/blob/main/LICENSE