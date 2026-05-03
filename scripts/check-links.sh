#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if command -v lychee >/dev/null 2>&1; then
  exec lychee \
    --config lychee.toml \
    --root-dir "$ROOT" \
    --verbose \
    --no-progress \
    "./docs/**/*.md" "./README.md" "./CONTRIBUTING.md"
fi

if command -v docker >/dev/null 2>&1; then
  exec docker run --rm -v "$ROOT:/work" -w /work lycheeverse/lychee:latest \
    --config /work/lychee.toml \
    --root-dir /work \
    --verbose \
    --no-progress \
    "./docs/**/*.md" "./README.md" "./CONTRIBUTING.md"
fi

echo "Install lychee to run this script." >&2
exit 1
