#!/bin/bash
# Recreate the original /home/claude layout (all scripts use absolute paths)
R="$(cd "$(dirname "$0")" && pwd)"
for d in s1e1 s1e2 s1e3 s1e4 s1e5 s1e6 s1e7 s1e8 s1e9 s1e10 s2 movie promo voices; do
  [ -e "/home/claude/$d" ] || ln -s "$R/$d" "/home/claude/$d"
done
mkdir -p /home/claude/delivery/yt /home/claude/delivery/tt
echo "ok — now: cd /home/claude/s1eN && python3 epN.py   (ep1: ep.py)"
