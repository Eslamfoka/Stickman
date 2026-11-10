# Thumbnails (1280x720) for the 6 trend parts: strongest frame + big title + part badge
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
import sys, os
from PIL import Image, ImageDraw, ImageEnhance
OUT = DELIVERY + "/trend/thumbs"; os.makedirs(OUT, exist_ok=True)
PICK = {1: ("SHOT_[0] + 1.2", "جوووون!"), 2: ("BOMB + 1.0", "كوكو خلصان؟!"), 3: ("THROW + 0.2", "شطة طالع!"),
        4: ("MUNCH + 1.0", "لازم يعتذر!"), 5: ("NO + 0.8", "مش راجع!"), 6: ("SLEEP + DUR['P603'] + 1.2", "الإقالة!")}
COL = {1: (255, 214, 90), 2: (255, 90, 80), 3: (255, 90, 80), 4: (255, 214, 90), 5: (120, 190, 255), 6: (255, 90, 80)}
for n in range(1, 7):
    ns = {"__name__": "thumb", "__file__": os.path.abspath(f"part{n}.py")}
    exec(open(f"part{n}.py", encoding="utf-8").read(), ns)
    tt = eval(PICK[n][0], ns)
    fr = ns["frame"](tt)
    fr = ImageEnhance.Contrast(ImageEnhance.Color(fr).enhance(1.25)).enhance(1.1)
    d = ImageDraw.Draw(fr, "RGBA")
    d.rectangle([0, 820, 1920, 1080], fill=(0, 0, 0, 150))
    T = ns["text"]
    T(fr, 960, 905, PICK[n][1], 150, COL[n], (10, 5, 5), 10)
    T(fr, 960, 1025, ns["SERIES"], 56, (255, 255, 255), (10, 5, 5), 5)
    d.rounded_rectangle([60, 50, 400, 160], 24, fill=(205, 35, 45, 240))
    T(fr, 230, 105, f"الحلقة {n}", 60, (255, 255, 255), (60, 0, 0), 3)
    d.rounded_rectangle([1560, 50, 1860, 150], 24, fill=(255, 214, 90, 240))
    T(fr, 1710, 100, "شطة وزلطة", 44, (60, 15, 5), (255, 214, 90), 1)
    fr.resize((1280, 720), Image.LANCZOS).save(f"{OUT}/thumb_{n}.jpg", quality=92)
    print(n, round(tt, 1))
