#!/bin/bash
# Final movie = hook -> title -> character intro -> all kept episode segments
set -e; cd /home/claude/movie
{ echo "file 'hook/hook.mp4'"; echo "file 'seg/title.mp4'"; echo "file 'intro/intro.mp4'"; for f in $(ls seg/s*.mp4 | sort); do echo "file '$f'"; done; } > list_final.txt
ffmpeg -v error -y -f concat -safe 0 -i list_final.txt -c:v libx264 -preset veryfast -crf 22 -maxrate 3400k -bufsize 6800k -pix_fmt yuv420p -c:a aac -b:a 160k -ar 44100 -ac 2 -movflags +faststart "عمارة نعناعة - سر الدور السابع (الفيلم الكامل).mp4"
