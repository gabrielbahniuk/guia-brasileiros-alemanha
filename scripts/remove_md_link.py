#!/usr/bin/env python3
"""
Remove a single markdown [text](url) for the given URL.

If line (1-based) > 0, only that line is edited; otherwise the first line containing the link.

Exit codes: 0 changed, 2 no match, 1 error.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


def link_pattern(url: str) -> re.Pattern[str]:
    return re.compile(r"\[(?P<text>[^\]]*)\]\(" + re.escape(url) + r"\)")


def remove_link_from_line(line: str, url: str) -> tuple[str | None, bool]:
    pat = link_pattern(url)
    if not pat.search(line):
        return line, False
    new = pat.sub("", line)
    new = re.sub(r"[ \t]{2,}", " ", new).rstrip()
    new = re.sub(r"\|\s+\|", "| - |", new)
    stripped = new.strip()
    if stripped in {"", "-", "*"} or re.fullmatch(r"[-*]\s*", stripped):
        return None, True
    return new, True


def apply(path: Path, url: str, line_no: int) -> bool:
    original = path.read_text(encoding="utf-8")
    ends_with_nl = original.endswith("\n")
    lines = original.splitlines()
    pat = link_pattern(url)
    if not pat.search(original):
        return False

    def try_idx(idx: int) -> bool:
        nonlocal lines
        if idx < 0 or idx >= len(lines):
            return False
        new_val, did = remove_link_from_line(lines[idx], url)
        if not did:
            return False
        if new_val is None:
            del lines[idx]
        else:
            lines[idx] = new_val
        return True

    changed = False
    if line_no > 0 and line_no <= len(lines):
        if try_idx(line_no - 1):
            changed = True

    if not changed:
        for i in range(len(lines)):
            if pat.search(lines[i]) and try_idx(i):
                changed = True
                break

    if not changed:
        new_text, n = pat.subn("", original, count=1)
        if n == 0:
            return False
        path.write_text(new_text, encoding="utf-8")
        return True

    body = "\n".join(lines)
    if ends_with_nl or body:
        body += "\n"
    path.write_text(body, encoding="utf-8")
    return True


def main() -> int:
    if len(sys.argv) < 3:
        print("usage: remove_md_link.py <path> <url> [line]", file=sys.stderr)
        return 1
    file_path = Path(sys.argv[1])
    url = sys.argv[2]
    line_no = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    if not file_path.is_file():
        print(f"not a file: {file_path}", file=sys.stderr)
        return 1
    try:
        ok = apply(file_path, url, line_no)
    except OSError as e:
        print(e, file=sys.stderr)
        return 1
    return 0 if ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
