#!/bin/bash
# Joins parts 1..6 into one movie (horizontal + vertical), re-encoding for clean joins.
cd /home/claude/repo/Stickman/trend/01
for x in h v; do
  args=""; f=""
  for i in 1 2 3 4 5 6; do args="$args -i part${i}_$x.mp4"; f="$f[$((i-1)):v][$((i-1)):a]"; done
  ffmpeg -v error -y $args -filter_complex "${f}concat=n=6:v=1:a=1[v][a]" -map "[v]" -map "[a]" \
    -c:v libx264 -preset veryfast -crf 21 -pix_fmt yuv420p -c:a aac -b:a 192k movie_$x.mp4
done
D=/home/claude/delivery/trend
cp movie_h.mp4 "$D/أزمة منتخب العمارة - الفيلم كامل (عرض).mp4"
cp movie_v.mp4 "$D/أزمة منتخب العمارة - الفيلم كامل (طولي).mp4"
ffprobe -v error -show_entries format=duration -of csv=p=0 movie_h.mp4
