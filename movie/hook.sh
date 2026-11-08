#!/bin/bash
# 17s hook montage from the strongest moments of the season
set -e; mkdir -p /home/claude/movie/hook; cd /home/claude/movie/hook
clip(){ ffmpeg -v error -y -ss $2 -t $3 -i /home/claude/s1e$1/sirr_eldor_elsabe3_ep$1.mp4 -af "afade=t=in:d=0.03,afade=t=out:st=$(python3 -c "print($3-0.05)"):d=0.05" -c:v libx264 -preset veryfast -crf 18 -pix_fmt yuv420p -r 24 -c:a aac -b:a 192k -ar 44100 -ac 2 $4.mp4; }
clip 1 4.6 3.9 h1      # 12:00 knocks + power cut scream
clip 4 43.6 1.6 h2     # shadow on the stairs wall
clip 8 58.9 1.6 h3     # door slams on them in apt 7
clip 9 44.25 2.1 h4    # silhouette in the doorway + "عفريت!"
clip 10 64.4 1.3 h5    # basement main switch sparks
clip 10 117.9 1.6 h6   # slipper flying at Fahmy
clip 9 101.7 3.4 h7    # Fahmy: "العمارة هتتباع بكرة الصبح"
clip 9 108.2 1.9 h8    # Fahmy looks up, eye glint
(for i in 1 2 3 4 5 6 7 8; do echo "file 'h$i.mp4'"; done) > l.txt
ffmpeg -v error -y -f concat -safe 0 -i l.txt -c copy hook.mp4
