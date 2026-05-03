#!/usr/bin/env python3
"""Read lychee JSON report and emit a GitHub Actions matrix payload: {"include":[...]}."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

MAX_MATRIX = 50

TARGET_PREFIXES = ("docs/", "README.md", "CONTRIBUTING.md")


def _is_target_path(p: str) -> bool:
    n = p.replace("\\", "/").lstrip("./")
    return n == "README.md" or n == "CONTRIBUTING.md" or n.startswith("docs/")


def _entry_maps(data: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    out: list[tuple[str, dict[str, Any]]] = []
    for key in ("error_map", "timeout_map"):
        m = data.get(key) or {}
        if not isinstance(m, dict):
            continue
        for file_path, items in m.items():
            if not isinstance(items, list):
                continue
            for item in items:
                if isinstance(item, dict) and item.get("url"):
                    out.append((str(file_path), item))
    return out


def _make_id(path: str, url: str, line: int) -> str:
    h = hashlib.sha256(f"{path}\0{url}\0{line}".encode()).hexdigest()[:12]
    return h


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: lychee_failures_matrix.py <lychee-report.json>", file=sys.stderr)
        return 1
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"missing report: {path}", file=sys.stderr)
        return 1
    data = json.loads(path.read_text(encoding="utf-8"))
    seen: set[tuple[str, str, int]] = set()
    include: list[dict[str, Any]] = []

    for file_path, item in _entry_maps(data):
        fp = file_path.replace("\\", "/").lstrip("./")
        if not _is_target_path(fp):
            continue
        url = str(item["url"])
        span = item.get("span") or {}
        line = int(span.get("line") or 0)
        detail = ""
        status = item.get("status") or {}
        if isinstance(status, dict):
            detail = str(status.get("text") or status.get("details") or "")
        dedupe = (fp, url, line)
        if dedupe in seen:
            continue
        seen.add(dedupe)
        eid = _make_id(fp, url, line)
        include.append(
            {
                "id": eid,
                "path": fp,
                "url": url,
                "line": line,
                "detail": detail[:500],
            }
        )

    include = include[:MAX_MATRIX]
    print(json.dumps({"include": include}, ensure_ascii=False))
    print(f"Emitted {len(include)} matrix entries (cap {MAX_MATRIX})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
