#!/bin/bash
# Renders the horizontal picture + audio of every Season-2 episode -> s2eN/movie_src.mp4 (skips ones already done)
R="$(cd "$(dirname "$0")/../.." && pwd)"; PY="${PY:-python3}"; set -e
for n in ${EPS:-1 2 3 4 5 6 7 8 9 10}; do
  D="$R/s2e$n"; [ -f "$D/movie_src.mp4" ] && { echo "ep$n already rendered"; continue; }
  echo "== ep$n start $(date +%T)"
  "$PY" "$R/movie/s2/render_h.py" $n 0 2 > "$D/mh0.log" 2>&1 &
  P0=$!
  "$PY" "$R/movie/s2/render_h.py" $n 1 2 > "$D/mh1.log" 2>&1
  wait $P0
  "$PY" "$R/movie/s2/render_h.py" $n audio > "$D/mha.log" 2>&1
  (cd "$D" && printf "file 'mh_0.mp4'\nfile 'mh_1.mp4'\n" > mh_list.txt && \
   ffmpeg -y -v error -f concat -safe 0 -i mh_list.txt -i mix.wav -map 0:v -map 1:a -c:v copy -af loudnorm=I=-15:TP=-1.5 \
     -c:a aac -b:a 192k -ar 44100 -ac 2 -shortest movie_src.mp4 && rm -f mh_0.mp4 mh_1.mp4 mh_list.txt)
  echo "== ep$n done $(date +%T)"
done
echo ALL_DONE
