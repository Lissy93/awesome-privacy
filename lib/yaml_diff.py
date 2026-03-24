"""Shared utilities for diffing awesome-privacy.yml across git refs."""

import os
import subprocess
import sys

import yaml

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_yaml_at_ref(ref, cwd=None):
    """Load awesome-privacy.yml from a git ref. Returns None on failure."""
    cwd = cwd or PROJECT_ROOT
    try:
        result = subprocess.run(
            ["git", "show", f"{ref}:awesome-privacy.yml"],
            capture_output=True, text=True, check=True, cwd=cwd,
        )
        return yaml.safe_load(result.stdout)
    except subprocess.CalledProcessError:
        return None
    except yaml.YAMLError as e:
        print(f"  YAML parse error at {ref}: {e}", file=sys.stderr)
        return None


def build_index(data, depth):
    """Build a keyed index at the given depth (3=services, 2=sections, 1=categories)."""
    index = {}
    for cat in (data.get("categories") or []):
        cn = cat.get("name", "")
        if depth == 1:
            index[cn] = {k: v for k, v in cat.items() if k != "sections"}
            continue
        for sec in (cat.get("sections") or []):
            sn = sec.get("name", "")
            if depth == 2:
                index[(cn, sn)] = {k: v for k, v in sec.items() if k != "services"}
                continue
            for svc in (sec.get("services") or []):
                index[(cn, sn, svc.get("name", ""))] = svc
    return index


def diff_index(base_idx, head_idx):
    """Return (added_keys, removed_keys, modified_keys_with_changed_fields)."""
    base_keys, head_keys = set(base_idx), set(head_idx)
    added = sorted(head_keys - base_keys)
    removed = sorted(base_keys - head_keys)
    modified = []
    for key in sorted(base_keys & head_keys):
        if base_idx[key] != head_idx[key]:
            all_fields = set(base_idx[key]) | set(head_idx[key])
            changed = sorted(f for f in all_fields if base_idx[key].get(f) != head_idx[key].get(f))
            modified.append((key, changed))
    return added, removed, modified
