import sys, os, math, subprocess, wave
sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter
from engine import *

os.chdir(ROOT + "/movie/intro")
SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(7)

CAST = [
 ("shatta", "شطة", "المندفع... وبيخاف من العتمة", "torch", [(0, "happy"), (0.35, "scared"), (0.62, "happy")], "hips"),
 ("zalata", "زلطة", "العقل اللي حاسبها بالقلم", "nbpen", [(0, "flat"), (0.6, "smug")], "hold"),
 ("tota", "توتة", "عينها على كل التفاصيل", None, [(0, "happy"), (0.55, "smug")], "point"),
 ("nana", "الحاجة نعناعة", "كبيرة العمارة... وصاحبة الشبشب", "slipper", [(0, "neutral"), (0.55, "angry")], "up"),
 ("bondo2", "عم بندق", "البواب اللي عمره ما بينام", "lantern", [(0, "sleepy"), (0.6, "smug")], "hold"),
 ("fahmy", "أستاذ فهمي", "الجار الجديد... ظريف زيادة عن اللزوم", "tray", [(0, "happy"), (0.7, "smug")], "hold"),
 ("sawsan", "طنط سوسن", "أشهر لايف في العمارة", "phone", [(0, "happy")], "up"),
]
AUD = {c[0]: load_audio(f"audio/{c[0]}.mp3") for c in CAST}
ENV = {k: envelope(v) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}

POP, HOLD = 0.55, 0.55
segs = []; t = 0.0
for c in CAST:
    d = POP + DUR[c[0]] + HOLD
    segs.append(dict(c=c, start=t, end=t + d, line=t + POP)); t += d
TEASE = (t, t + 3.2); t += 3.2
GROUP = (t, t + 3.6); t += 3.6
TOTAL = t

_lob = Image.open(ROOT + "/s1e1/bg/lobby.png").convert("RGB").resize((W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(14))
yy, xx = np.mgrid[0:H, 0:W]
vg = 1 - 0.6 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) ** 1.2
VIG = Image.fromarray((np.clip(vg, 0.2, 1) * 255).astype(np.uint8)).convert("RGB")
ANG = np.arctan2(yy - 560, xx - 1300)
GRAIN = [np.random.default_rng(i).normal(0, 4.0, (H // 2, W // 2)).astype(np.float32) for i in range(6)]

def ease_back(k):
    k = min(1, max(0, k)); c1 = 1.70158; c3 = c1 + 1
    return 1 + c3 * (k - 1) ** 3 + c1 * (k - 1) ** 2
def kk(tt, a, b): return min(1, max(0, (tt - a) / max(1e-3, b - a)))

def bg(col, tt):
    base = ImageChops.multiply(_lob, Image.new("RGB", (W, H), tuple(int(80 + v * 0.7) for v in col)))
    rays = (np.sin(ANG * 12 + tt * 0.8) > 0.55).astype(np.float32) * 0.22
    a = np.asarray(base, np.float32) + rays[..., None] * np.array(col, np.float32)
    im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(im, "RGBA")
    for i in range(9):   # moving diagonal stripes
        x = ((tt * 260 + i * 260) % (W + 600)) - 300
        d.polygon([(x, 0), (x + 60, 0), (x - 340, H), (x - 400, H)], fill=(255, 255, 255, 14))
    return im

def expr_of(spec, k):
    cur = spec[0][1]
    for f, ex in spec:
        if k >= f: cur = ex
    return cur

def char_layer(who, x, y, s, expr, mouth, arms, held, tt, look=0, sil=False):
    L = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(L)
    p.ell(x, y + 4 * s, 46 * s, 9 * s, (0, 0, 0, 120), None)
    blink = ((tt + (hash(who) % 7) * 0.37) % 3.4) < 0.1 and expr != "sleepy"
    draw_char(p, who, x, y, s, expr, mouth, look, blink, arms, tt, held)
    if sil:
        al = L.getchannel("A"); L = Image.new("RGBA", L.size, (6, 6, 8, 255)); L.putalpha(al)
    return L.resize((W, H), Image.LANCZOS)

def name_card(fr, name, tag, col, k, tt):
    d = ImageDraw.Draw(fr, "RGBA")
    e = ease_back(k); x = -500 + (620 + 500) * e
    bright = tuple(min(255, int(v * 1.25 + 40)) for v in col)
    d.rounded_rectangle([x - 470, 380, x + 470, 640], 36, fill=(10, 10, 16, 200), outline=bright + (255,), width=6)
    d.rectangle([x - 470, 600, x + 470, 640], fill=bright + (255,))
    text(fr, x, 470, name, 120 if len(name) < 8 else 96, bright, (20, 10, 10), 7)
    text(fr, x, 568, tag, 40, (240, 240, 240), (10, 10, 10), 3)
    for i in range(6):   # sparkles around the card
        a = tt * 2 + i * 1.05; sx = x + math.cos(a) * 520; sy = 510 + math.sin(a * 1.3) * 170
        r = 8 + 4 * math.sin(tt * 6 + i)
        d.line([(sx - r, sy), (sx + r, sy)], fill=(255, 250, 220, 200), width=3); d.line([(sx, sy - r), (sx, sy + r)], fill=(255, 250, 220, 200), width=3)

def finish(fr, tt):
    fr = ImageChops.multiply(fr, VIG)
    a = np.asarray(fr, np.float32); g = GRAIN[int(tt * FPS) % 6]
    return Image.fromarray(np.clip(a + np.repeat(np.repeat(g, 2, 0), 2, 1)[..., None], 0, 255).astype(np.uint8))

def frame(tt):
    for sg in segs:
        if sg["start"] <= tt < sg["end"]: break
    else: sg = None
    if sg:
        who, name, tag, held, spec, arms = sg["c"]; col = CH[who]["shirt"]
        fr = bg(col, tt)
        k = kk(tt, sg["start"], sg["start"] + POP)
        x = 2400 + (1330 - 2400) * ease_back(k)
        lt = tt - sg["line"]; talking = 0 <= lt < DUR[who]
        mouth = float(ENV[who][min(int(lt * FPS) + 2, len(ENV[who]) - 1)]) if talking else 0.0
        expr = expr_of(spec, max(0, lt) / DUR[who])
        a_ = arms
        if who == "nana" and lt / DUR[who] < 0.55: a_ = "hips"; held_ = None
        else: held_ = held
        if who == "tota" and lt / DUR[who] > 0.6: a_ = "point"
        bob = abs(math.sin(tt * 3)) * 6
        L = char_layer(who, x, 1050 - bob, 3.1 * (1 / CH[who]["scale"]) ** 0.6, expr, mouth, a_, held_, tt, look=-1 if k < 1 else 0)
        if who == "bondo2":
            g = Image.new("L", (W, H), 0); ImageDraw.Draw(g).ellipse([x - 40, 560, x + 300, 900], fill=120)
            fr.paste(Image.new("RGB", (W, H), (255, 190, 110)), (0, 0), g.filter(ImageFilter.GaussianBlur(60)))
        fr.paste(L, (0, 0), L)
        if who == "sawsan" and lt > 0:
            d = ImageDraw.Draw(fr, "RGBA"); d.rounded_rectangle([1560, 300, 1760, 360], 14, fill=(220, 30, 40, 235))
            d.ellipse([1580, 318, 1604, 342], fill=(255, 255, 255, 255))
            ImageDraw.Draw(fr).text((1680, 330), "LIVE", fill=(255, 255, 255), anchor="mm", font=__import__("PIL.ImageFont", fromlist=["x"]).truetype(FONT, 34))
        name_card(fr, name, tag, col, kk(tt, sg["start"] + 0.15, sg["start"] + POP + 0.25), tt)
        e = tt - sg["start"]
        if e < 0.12: fr = Image.blend(fr, Image.new("RGB", (W, H), (255, 255, 255)), 1 - e / 0.12)
        return finish(fr, tt)
    if TEASE[0] <= tt < TEASE[1]:
        k = kk(tt, TEASE[0], TEASE[1])
        fr = Image.new("RGB", (W, H), (6, 6, 10))
        g = Image.new("L", (W, H), 0); ImageDraw.Draw(g).ellipse([W / 2 - 520, 120, W / 2 + 520, 1100], fill=int(230 * min(1, k * 3)))
        fr.paste(Image.new("RGB", (W, H), (120, 145, 210)), (0, 0), g.filter(ImageFilter.GaussianBlur(90)))
        L = char_layer("roshdy", W / 2, 1000, 2.6, "neutral", 0, "hold", "paper", tt, sil=True)
        fr.paste(L, (0, 0), L)
        if int(tt * 7) % 5: text(fr, W / 2, 230, "؟", 160, (255, 214, 90), (30, 10, 10), 6)
        if k > 0.12: text(fr, W / 2, 1010, "وفيه حد كمان... مستخبي في الحكاية", 58, (235, 235, 235), (10, 10, 10), 5)
        return finish(fr, tt)
    k = kk(tt, GROUP[0], GROUP[1])
    fr = bg((255, 200, 90), tt)
    order = ["fahmy", "bondo2", "nana", "tota", "shatta", "zalata", "sawsan"]
    for i, who in enumerate(order):
        ki = kk(tt, GROUP[0] + i * 0.08, GROUP[0] + 0.5 + i * 0.08)
        x = 260 + i * 233; y = 1060 + (1 - ease_back(ki)) * 500 - abs(math.sin(tt * 4 + i)) * 10
        L = char_layer(who, x, y, 1.75, "smug" if who == "fahmy" else "happy", 0, "up" if who not in ("fahmy", "bondo2") else "hips", None, tt)
        fr.paste(L, (0, 0), L)
    text(fr, W / 2, 190, "عمارة نعناعة", 130, (255, 214, 90), (40, 10, 10), 7)
    if k > 0.3: text(fr, W / 2, 330, "يلا نبدأ الحكاية!", 70, (255, 255, 255), (10, 10, 10), 5)
    return finish(fr, tt)

def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR; buf = np.zeros(n, np.float32)
    bpm = 112; beat = 60 / bpm; tb = np.arange(int(SR * 0.25)) / SR
    kick = np.sin(2 * np.pi * (55 + 90 * np.exp(-tb * 30)) * tb) * np.exp(-tb * 12) * 0.5
    hat = np.random.default_rng(3).normal(0, 1, int(SR * 0.05)) * np.exp(-np.arange(int(SR * 0.05)) / SR * 90) * 0.08
    bassn = [55, 55, 65.4, 49]
    for i in range(int(TEASE[0] / beat)):
        t0 = i * beat
        mix_into(buf, kick, t0, 0.55 if i % 2 == 0 else 0.0)
        mix_into(buf, hat, t0 + beat / 2, 1.0)
        f = bassn[(i // 4) % 4]; tbb = np.arange(int(SR * beat * 0.9)) / SR
        mix_into(buf, np.sin(2 * np.pi * f * tbb) * np.exp(-tbb * 3) * 0.16, t0, 1.0)
    for i in range(int((GROUP[1] - GROUP[0]) / (beat / 2))):
        t0 = GROUP[0] + i * beat / 2; f = [523.25, 659.25, 783.99, 1046.5][i % 4]; tt_ = np.arange(int(SR * 0.4)) / SR
        mix_into(buf, np.sin(2 * np.pi * f * tt_) * np.exp(-tt_ * 6) * 0.08, t0, 1.0)
    wh = load_audio(ROOT + "/s1e9/sfx/whoosh.mp3")
    for sg in segs:
        mix_into(buf, wh, max(0, sg["start"] - 0.05), 0.7)
        mix_into(buf, AUD[sg["c"][0]], sg["line"], 1.0)
    ts = np.arange(int(SR * 2.5)) / SR
    sting = (np.sin(2 * np.pi * 1200 * ts) * 0.06 + np.sin(2 * np.pi * 55 * ts) * 0.45) * np.exp(-ts * 1.4)
    mix_into(buf, sting, TEASE[0] + 0.1, 1.0)
    mix_into(buf, load_audio(ROOT + "/s1e10/sfx/cheer.mp3"), GROUP[0] + 0.2, 0.9)
    buf = buf[:int(TOTAL * SR)]; buf = np.clip(buf / np.abs(buf).max() * 0.95, -1, 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((buf * 32767).astype(np.int16).tobytes())

if __name__ == "__main__":
    print("TOTAL", round(TOTAL, 1))
    if sys.argv[1:2] == ["stills"]:
        for v in sys.argv[2:]: frame(float(v)).save(f"still_{float(v):.1f}.png")
    else:
        build_audio()
        pr = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                               "-i", "mix.wav", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
                               "-af", "loudnorm=I=-15:TP=-1.5", "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2", "-shortest", "intro.mp4"],
                              stdin=subprocess.PIPE)
        for i in range(int(TOTAL * FPS)):
            pr.stdin.write(frame(i / FPS).tobytes())
        pr.stdin.close(); pr.wait(); print("done")
