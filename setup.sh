#!/bin/bash
# Scripts no longer need /home/claude symlinks: each one finds the repo root via s1e1/paths.py.
# This only creates the delivery folders (override location with NANAA_DELIVERY).
R="$(cd "$(dirname "$0")" && pwd)"
D="${NANAA_DELIVERY:-$R/delivery}"
mkdir -p "$D/yt" "$D/tt" "$D/trend"
echo "ok — now: cd s1eN && python3 epN.py  (Windows: python; ep1: ep.py)"
