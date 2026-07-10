# Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE.
# SPDX-License-Identifier: MIT
"""Release gate (RR-B-15): required files, forbidden paths, forbidden
content, version agreement (RR-B-09). Exits non-zero on any failure.

Runs standalone inside the release repo (jgs-archi-mcp) via
.github/workflows/validate.yml, and can also be run from the dev repo against
a staged tree to sanity-check before pushing.
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

REQUIRED = [
    "LICENSE", "COPYRIGHT", "NOTICE", "README.md", "CHANGELOG.md",
    "SECURITY.md", "CITATION.cff", "RELEASE-INFO.txt",
    "docs/index.html",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
]

# Directory names that must never appear as a path SEGMENT (the Java source
# and test bundles). Deliberately excludes bare substring matching: the
# .archiplugin binaries in bin/ legitimately carry "net.vheerden.archi.mcp"
# in their filename (the OSGi bundle ID naming convention), and that is not
# a leak.
FORBIDDEN_DIR_NAMES = {"net.vheerden.archi.mcp", "net.vheerden.archi.mcp.tests"}
FORBIDDEN_PATH_PARTS = ["__pycache__", ".pytest_cache", ".ruff_cache", ".venv", ".bak"]

FORBIDDEN_SUFFIXES = {".java", ".class"}

FORBIDDEN_CONTENT = [
    re.compile(r"BEGIN [A-Z ]*PRIVATE KEY"),
    re.compile(r"CONFIDENTIAL"),
]

SCAN_GLOBS = ["*.md", "*.txt", "*.cff", "docs/**/*.md", "docs/**/*.html",
              ".github/**/*.yml", ".github/**/*.yaml"]

BINARY_SUFFIXES = {".woff2", ".png", ".jpg", ".ico", ".gif", ".pdf", ".zip", ".archiplugin"}


def main() -> int:
    fails: list[str] = []

    for f in REQUIRED:
        if not (ROOT / f).is_file():
            fails.append(f"required file missing: {f}")

    try:
        tracked = subprocess.run(
            ["git", "ls-files"], capture_output=True, text=True, check=True, cwd=ROOT,
        ).stdout.splitlines()
    except Exception:
        tracked = [str(p.relative_to(ROOT)) for p in ROOT.rglob("*") if p.is_file()]

    for f in tracked:
        if any(part in f for part in FORBIDDEN_PATH_PARTS):
            fails.append(f"forbidden tracked path: {f}")
        if any(seg in FORBIDDEN_DIR_NAMES for seg in pathlib.Path(f).parts):
            fails.append(f"forbidden tracked path: {f}")
        if pathlib.Path(f).suffix.lower() in FORBIDDEN_SUFFIXES:
            fails.append(f"forbidden file type: {f}")

    self_path = pathlib.Path(__file__).resolve()
    for g in SCAN_GLOBS:
        for path in ROOT.glob(g):
            if not path.is_file():
                continue
            if path.resolve() == self_path:
                continue
            if path.suffix.lower() in BINARY_SUFFIXES:
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            for pat in FORBIDDEN_CONTENT:
                if pat.search(text):
                    fails.append(f"forbidden content ({pat.pattern}) in {path.relative_to(ROOT)}")

    version = None
    release_info = ROOT / "RELEASE-INFO.txt"
    if release_info.exists():
        m = re.search(r"Version:\s*(\S+)", release_info.read_text(encoding="utf-8"))
        if m:
            version = m.group(1)

    citation = ROOT / "CITATION.cff"
    if version and citation.exists():
        m = re.search(r"^version:\s*(\S+)", citation.read_text(encoding="utf-8"), re.MULTILINE)
        if m and m.group(1) != version:
            fails.append(f"version mismatch: RELEASE-INFO.txt={version}, CITATION.cff={m.group(1)}")

    if fails:
        print("RELEASE GATE FAILED:", file=sys.stderr)
        for f in fails:
            print(f"  - {f}", file=sys.stderr)
        return 1

    print("Release gate: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
