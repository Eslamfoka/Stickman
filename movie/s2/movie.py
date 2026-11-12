# Season 2 «سر البدروم» — full-season movie: hook -> title -> all 10 episodes (titles, audience puzzles,
# follow CTAs + phone inserts, endcards and "yesterday's puzzle" talk-to-camera removed).
# Needs s2eN/movie_src.mp4 for every episode (bash movie/s2/render_all.sh).
# Usage: python movie/s2/movie.py [segs|hook|title|assemble|all]
import sys, os, json, subprocess
sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file()))
from paths import ROOT, DELIVERY
M = ROOT + "/movie/s2"; os.makedirs(M + "/seg", exist_ok=True); os.makedirs(M + "/hook", exist_ok=True)
SRC = lambda n: f"{ROOT}/s2e{n}/movie_src.mp4"
NAMES = {1: "باب البدروم", 2: "الصوت اللي تحت الأرض", 3: "الباشا", 4: "النزول", 5: "صفيح", 6: "الأسطوانة",
         7: "فهمي التايب", 8: "ليلة البدروم", 9: "الصندوق", 10: "أغنية العمارة"}
# cut ranges (episode seconds, on shot boundaries from `python epN.py times`)
CUTS = {
 1: [(7.21, 9.21), (20.9, 26.38), (94.05, 100.05), (149.28, 999)],          # title, "لغز امبارح" to camera, puzzle, black+endcard
 2: [(23.77, 25.77), (31.07, 35.96), (89.94, 96.12), (151.21, 999)],
 3: [(38.51, 40.51), (151.57, 159.03), (187.45, 999)],
 4: [(20.13, 22.13), (124.38, 130.32), (144.4, 999)],
 5: [(7.02, 9.02), (78.15, 88.79), (137.67, 999)],                          # puzzle + follow CTA + phone insert
 6: [(12.0, 14.0), (103.39, 115.16), (135.42, 999)],
 7: [(6.98, 8.98), (52.94, 66.25), (132.37, 999)],
 8: [(6.96, 15.74), (100.2, 113.43), (125.07, 999)],                        # title + vote result to camera
 9: [(9.66, 11.66), (93.82, 105.52), (114.22, 999)],
 10: [(8.98, 10.98), (89.91, 95.27), (97.67, 101.19)],                     # keep the season-end card «الموسم التالت قريباً»
}
HOOK = [  # (ep, start, dur) strongest moments of the season, original episode times
 (2, 142.5, 4.3),   # Pasha: «العمارة دي هاخدها ولو بالعافية»
 (4, 138.1, 3.8),   # «الملاية بتتحرك» + red eyes
 (5, 5.25, 1.9),    # «عفريت حديد!!!»
 (7, 40.1, 2.6),    # «الحيطة بتتشرخ!»
 (8, 63.7, 2.6),    # «دخلاء! وضع الحراسة»
 (9, 63.75, 2.7),   # «الروبوت! يا ماما!»
 (9, 105.85, 4.9),  # Pasha: «هات اللودر… العمارة دي هتتهد الصبح»
]
ENC = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "17", "-pix_fmt", "yuv420p", "-r", "24",
       "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2"]
dur = lambda f: float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                                     capture_output=True, text=True).stdout)

def clip(src, a, d, out):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a}", "-t", f"{d}", "-i", src,
                    "-af", f"afade=t=in:d=0.03,afade=t=out:st={max(0, d - 0.05):.3f}:d=0.05", *ENC, out], check=True)

def segs():
    out = []
    for n, cuts in CUTS.items():
        D = dur(SRC(n)); t = 0.0
        for a, b in sorted(cuts):
            if a - t > 0.05: out.append((n, t, a))
            t = min(b, D)
        if D - t > 0.05: out.append((n, t, D))
    for i, (n, a, b) in enumerate(out): clip(SRC(n), a, b - a, f"{M}/seg/s{i:02d}.mp4")
    json.dump(out, open(M + "/segs.json", "w", encoding="utf-8"))
    print(len(out), "segments,", round(sum(b - a for _, a, b in out) / 60, 2), "min")

def hook():
    for i, (n, a, d) in enumerate(HOOK): clip(SRC(n), a, d, f"{M}/hook/h{i}.mp4")
    open(M + "/hook/l.txt", "w", encoding="utf-8").write("".join(f"file 'h{i}.mp4'\n" for i in range(len(HOOK))))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", M + "/hook/l.txt", "-c", "copy", M + "/hook/hook.mp4"], check=True)

def title():
    os.chdir(M); sys.path.insert(0, ROOT + "/s1e1")
    from engine import text, W, H
    from PIL import Image, ImageDraw, ImageFilter
    fr = Image.new("RGB", (W, H), (6, 10, 12))
    g = Image.new("L", (W, H), 0); ImageDraw.Draw(g).ellipse([W/2-760, H/2-320, W/2+760, H/2+320], fill=80)
    fr.paste(Image.new("RGB", (W, H), (20, 110, 90)), (0, 0), g.filter(ImageFilter.GaussianBlur(130)))
    text(fr, W/2, H/2-160, "عمارة نعناعة", 140, (255, 214, 90), (40, 10, 10), 7)
    text(fr, W/2, H/2+10, "الموسم التاني: سر البدروم", 84, (235, 235, 235))
    text(fr, W/2, H/2+140, "الفيلم كامل", 56, (200, 220, 210))
    fr.save("title.png")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "7.21", "-t", "2.0", "-i", SRC(1), "-vn", "-ac", "2", "-ar", "44100",
                    "-af", "apad=pad_dur=1.0,afade=t=out:st=2.4:d=0.6", "-c:a", "pcm_s16le", "title_a.wav"], check=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", "24", "-t", "3.0", "-i", "title.png", "-i", "title_a.wav",
                    "-vf", "fade=in:st=0:d=0.4,fade=out:st=2.6:d=0.4,format=yuv420p", *ENC, "-t", "3.0", "seg/title.mp4"], check=True)

def assemble():
    sys.path.insert(0, ROOT + "/publish"); from final_encode import encode, DENOISE
    parts = ["hook/hook.mp4", "seg/title.mp4"] + [f"seg/s{i:02d}.mp4" for i in range(len(json.load(open(M + "/segs.json", encoding="utf-8"))))]
    open(M + "/list.txt", "w", encoding="utf-8").write("".join(f"file '{p}'\n" for p in parts))
    raw = M + "/movie_raw.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", M + "/list.txt", "-c", "copy", raw], check=True)
    os.makedirs(DELIVERY + "/s2", exist_ok=True)
    out = DELIVERY + "/s2/عمارة نعناعة م2 - سر البدروم (الفيلم كامل).mp4"
    encode(raw, out, 26, DENOISE); os.remove(raw)   # 23 without denoise = 617 MB (> 400 MB send cap)
    # YouTube chapters
    t = dur(M + "/hook/hook.mp4") + dur(M + "/seg/title.mp4"); seen = {}; ch = ["00:00 البداية"]
    for i, (n, a, b) in enumerate(json.load(open(M + "/segs.json", encoding="utf-8"))):
        if n not in seen:
            seen[n] = 1; s = int(t); ch.append(f"{s // 60:02d}:{s % 60:02d} الحلقة {n} — {NAMES[n]}")
        t += dur(f"{M}/seg/s{i:02d}.mp4")
    open(M + "/chapters.txt", "w", encoding="utf-8").write("\n".join(ch) + "\n"); print("\n".join(ch))
    print("TOTAL", round(dur(out) / 60, 2), "min")

if __name__ == "__main__":
    step = sys.argv[1] if len(sys.argv) > 1 else "all"
    for name, fn in [("segs", segs), ("hook", hook), ("title", title), ("assemble", assemble)]:
        if step in (name, "all"): fn()
