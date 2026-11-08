# movie title card image -> seg/title.mp4 (audio = ep1 title sting 9.06s..12.06s)
import sys, subprocess, os; sys.path.insert(0, "/home/claude/s1e1"); os.chdir("/home/claude/movie")
from engine import text, W, H
from PIL import Image, ImageDraw, ImageFilter
fr = Image.new("RGB", (W, H), (8, 8, 12))
g = Image.new("L", (W, H), 0); ImageDraw.Draw(g).ellipse([W/2-700, H/2-300, W/2+700, H/2+300], fill=70)
fr.paste(Image.new("RGB", (W, H), (120, 60, 20)), (0, 0), g.filter(ImageFilter.GaussianBlur(120)))
text(fr, W/2, H/2-130, "عمارة نعناعة", 140, (255, 214, 90), (40, 10, 10), 7)
text(fr, W/2, H/2+30, "سر الدور السابع", 84, (235, 235, 235))
text(fr, W/2, H/2+150, "الفيلم الكامل", 56, (210, 210, 210))
fr.save("title.png")
subprocess.run("ffmpeg -v error -y -ss 9.06 -t 3.0 -i /home/claude/s1e1/sirr_eldor_elsabe3_ep1.mp4 -vn -ac 2 -ar 44100 -c:a pcm_s16le title_a.wav", shell=True, check=True)
subprocess.run("ffmpeg -v error -y -loop 1 -framerate 24 -t 3.0 -i title.png -i title_a.wav -vf 'fade=in:st=0:d=0.4,fade=out:st=2.6:d=0.4,format=yuv420p' -c:v libx264 -preset veryfast -crf 18 -c:a aac -b:a 192k -ar 44100 -ac 2 -shortest seg/title.mp4", shell=True, check=True)
