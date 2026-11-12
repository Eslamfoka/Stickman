import sys, os; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
"""Season-1 vertical recap reel (~85 s) for TikTok / Reels / Shorts on movie day.
cover (0.5 s) -> strongest beats of ep1..ep10 (no spoiler of the final reveal) -> end card «الحكاية كاملة على يوتيوب».
Needs the vertical episode renders: s1eN/sirr_eldor_elsabe3_epN_vertical.mp4 (cd s1eN && python epN.py).
Run: python movie/recap.py
"""
import subprocess

CLIPS = [  # (episode, start, end) in the vertical render timeline
    (1, 4.6, 8.5),     # 12:00 knocks + power cut scream
    (1, 12.7, 17.0),   # «الصوت جاي من فوق... من الدور السابع!»
    (2, 33.8, 40.1),   # key «سبعة... تلاتين»
    (3, 58.6, 61.8),   # doorman with the key going up
    (3, 69.3, 74.0),   # morse knocks pattern
    (4, 46.5, 52.1),   # long shadow on the wall
    (4, 70.1, 77.6),   # «شطة... يا شطة...»
    (5, 21.3, 27.1),   # Fahmy arrives
    (5, 76.2, 79.8),   # «أنا عندي مفاتيح... لكل الأبواب»
    (6, 41.0, 47.3),   # «أيوه يا باشا... الخطة ماشية»
    (6, 73.0, 77.3),   # NANA = نعناعة
    (7, 40.6, 43.4),   # notebook stolen
    (8, 61.8, 67.9),   # locked in the 7th floor
    (9, 44.2, 46.4),   # silhouette «عفريت!»
    (9, 83.6, 88.0),   # «الخبط بتاع الساعة اتناشر... ده مش أنا»
    (9, 100.0, 107.3), # «العمارة هتتباع بكرة الصبح» — «بكرة الصبح؟!»
    (10, 50.5, 53.3),  # «النور راح... وأنا لوحدي»
]
CARD_DUR = 3.5
OUT_DIR = DELIVERY + "/s1_shorts"; os.makedirs(OUT_DIR, exist_ok=True)
OUT = OUT_DIR + "/عمارة نعناعة - الموسم الأول في دقيقة ونص (ملخص طولي).mp4"
TMP = ROOT + "/movie/recap"; os.makedirs(TMP, exist_ok=True)

# --- brand helpers + thumbnail functions from publish/build.py (definitions only) ---
src = open(ROOT + "/publish/build.py", encoding="utf-8").read().split("\nposts = [")[0]
sys.argv = [ROOT + "/publish/build.py"]; g = {"__name__": "recap", "__file__": ROOT + "/publish/build.py"}
exec(compile(src, "build.py", "exec"), g)
g["badge_text"] = lambda it: "ملخص"
item = dict(id="nanaa_s1_recap", series="nanaa_s1", kind="recap", ep=None, headline=["الحكاية", "كلها!"],
            bg=g["S1"] + "1/bg/lobby_1080.png", figs=[("zalata", 3.0, "shock", 0.6, -1, "up", None, None, None, 1750),
                                                     ("shatta", 4.2, "shock", 0.9, -1, "up", None, None, None, 1300)])
g["thumb_cover"](item)
cover = ROOT + "/publish/thumbs/nanaa_s1_recap_cover.jpg"

# end card
Image, ImageDraw, lz, logo = g["Image"], g["ImageDraw"], g["lz"], g["logo"]
card = g["render_bg"](item, 1080, 1920)
shade = Image.new("RGBA", (1080, 1920), (0, 0, 0, 150)); card.alpha_composite(shade)
logo(card, 540, 330, 120)
lz(card, 540, 760, "مين ورا الخبط؟", 150, (255, 255, 255), ow=18, iw=7)
lz(card, 540, 1000, "الحكاية كاملة", 130, g["GOLD"], ow=16, iw=6)
lz(card, 540, 1190, "على يوتيوب", 130, g["GOLD"], ow=16, iw=6)
from PIL import ImageFont
ImageDraw.Draw(card).text((540, 1560), "@shattawzalata", font=ImageFont.truetype(ROOT + "/brand/fonts/DejaVuSans-Bold.ttf", 66),
                          fill=(255, 255, 255), anchor="mm", stroke_width=5, stroke_fill=(45, 12, 8))
card.convert("RGB").save(TMP + "/card.png")

# --- assemble ---
args = ["ffmpeg", "-y", "-v", "error", "-loop", "1", "-t", "1", "-i", cover]
fc = ["[0:v]scale=1080:1920,setsar=1,fps=24,format=yuv420p,trim=duration=0.5,setpts=PTS-STARTPTS[v0]",
      "anullsrc=r=44100:cl=mono,atrim=duration=0.5,asetpts=PTS-STARTPTS[a0]"]
pads = "[v0][a0]"
for i, (n, a, b) in enumerate(CLIPS, 1):
    d = b - a
    args += ["-ss", f"{a:.3f}", "-t", f"{d:.3f}", "-i", f"{ROOT}/s1e{n}/sirr_eldor_elsabe3_ep{n}_vertical.mp4"]
    fc.append(f"[{i}:v]fps=24,format=yuv420p,setsar=1,setpts=PTS-STARTPTS[v{i}]")
    fc.append(f"[{i}:a]aformat=channel_layouts=mono:sample_rates=44100,asetpts=PTS-STARTPTS,"
              f"afade=t=in:d=0.04,afade=t=out:st={d - 0.08:.3f}:d=0.08[a{i}]")
    pads += f"[v{i}][a{i}]"
k = len(CLIPS) + 1
args += ["-loop", "1", "-t", str(CARD_DUR), "-i", TMP + "/card.png"]
fc.append(f"[{k}:v]scale=1080:1920,setsar=1,fps=24,format=yuv420p,fade=t=in:d=0.25,setpts=PTS-STARTPTS[v{k}]")
fc.append(f"sine=f=110:d={CARD_DUR},volume=0.25,afade=t=in:d=0.05,afade=t=out:st={CARD_DUR - 1.2}:d=1.2,aformat=channel_layouts=mono:sample_rates=44100[a{k}]")
pads += f"[v{k}][a{k}]"
fc.append(f"{pads}concat=n={k + 1}:v=1:a=1[v][ac]")
fc.append("[ac]loudnorm=I=-14:TP=-1.5[a]")
args += ["-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-tune", "animation",
         "-crf", "21", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-movflags", "+faststart", OUT]
subprocess.run(args, check=True)
dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", OUT], capture_output=True, text=True).stdout.strip()
print("✔", OUT, dur, "s")
