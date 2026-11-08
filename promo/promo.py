import sys, os, math, subprocess, wave
sys.path.insert(0, "/home/claude/s1e1")
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter, ImageFont
from engine import *

os.chdir("/home/claude/promo")
SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(202)

def A(name):
    a = load_audio(f"audio/{name}.mp3")
    if name == "SCREAM":
        a = a[int(0.47 * SR):]
    return a
NAMES = ["SW1", "SW2", "RO1", "RO2", "RO3", "RO4", "RO5", "NA1", "SH1", "ZA1", "SCREAM"]
AUD = {k: A(k) for k in NAMES}
ENV = {k: envelope(v) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}
SUB = {"SW1": "عاجل... عاجل يا متابعين! بعد ما مسكنا أستاذ فهمي... فيه صوت جاي من البدروم!", "SW2": "...إيه ده؟",
       "RO1": "نعناعة... يا أختي.", "RO2": "لو الجواب ده وصلك... يبقى العيال عرفوا السر.", "RO3": "بس فيه سر تاني... أكبر بكتير.",
       "RO4": "تحت... في البدروم.", "RO5": "افتحوه... بس ما تفتحوهوش بالليل.", "NA1": "محدش هينزل البدروم!",
       "SH1": "ثقوا فيا... المرة دي بجد!", "ZA1": "احتمال نرجع: خمسين في المية.", "SCREAM": ""}
WHO = {"SW1": "sawsan", "SW2": "sawsan", "NA1": "nana", "SH1": "shatta", "ZA1": "zalata", "SCREAM": "shatta"}

lines, sfx, segs = [], [], []
def say(t, k): lines.append((t, k)); return t + DUR[k]
def fx(t, n, g=1.0): sfx.append((t, n, g))
def seg(name, s, e, **kw): segs.append(dict(name=name, start=s, end=e, **kw))

t = 0.0
CC1 = (0.0, 7.0); seg("cctv1", *CC1)
fx(0.0, "hum", 1.0); fx(2.0, "buzz", 1.0); fx(5.4, "mknock", 1.4); fx(5.9, "mknock", 1.6)
t = 7.0; GL1 = (t, t + 0.4); seg("glitch", *GL1); fx(t, "static", 1.0); t += 0.4
NEWS0 = t; fx(t, "newsjingle", 1.0)
SW1_T = t + 0.4; t = say(SW1_T, "SW1")
KN = [t + 0.25, t + 0.6]; [fx(k_, "knock", 1.5) for k_ in KN]
SW2_T = KN[1] + 0.45; t = say(SW2_T, "SW2") + 0.35
seg("news", NEWS0, t)
LOST = (t, t + 1.3); seg("lost", *LOST); fx(t, "static", 1.3); t = LOST[1]
seg("black", t, t + 0.3); t += 0.3
LET0 = t; fx(t, "sting", 0.7)
RO_T = {}
blocks = [("letter", "RO1"), ("flash", "RO2"), ("window", "RO3"), ("lobby", "RO4"), ("door", "RO5")]
for name, k in blocks:
    s = t; RO_T[k] = t + 0.35; t = say(RO_T[k], k) + 0.45
    seg(name, s, t)
    fx(s, "whoosh", 0.35)
LET1 = t
fast = [("nana", "NA1"), ("shatta", "SH1"), ("zalata", "ZA1")]
FAST0 = t
for i, (who, k) in enumerate(fast):
    s = t; t = say(t + 0.2, k) + 0.25
    seg("cu_" + who, s, t)
    for j in range(2 + i): fx(s + 0.05 + j * (0.35 - i * 0.07), "knock", 1.0 + 0.2 * i)
CC2 = (t, t + 3.6); seg("cctv2", *CC2); fx(t, "static", 0.8); fx(t, "hum", 1.0)
DOOR_OPEN = t + 0.8; fx(DOOR_OPEN, "creak", 1.3)
POP = t + 2.3; say(POP, "SCREAM"); fx(POP, "boom", 0.6)
t = CC2[1]
seg("glitch", t, t + 0.35); fx(t, "static", 1.2); t += 0.35
TITLE = (t, t + 5.0); seg("title", *TITLE); fx(t, "boom", 1.2); fx(t + 0.1, "sting", 1.0); t = TITLE[1]
TOTAL = t

def kk(tt, a, b): return min(1, max(0, (tt - a) / max(1e-3, b - a)))
def ease(k): k = min(1, max(0, k)); return k * k * (3 - 2 * k)
def line_at(tt):
    for st, k in lines:
        if st <= tt < st + DUR[k]: return k, tt - st
    return None, 0

def load(p): return Image.open(p).convert("RGB").resize((W, H), Image.LANCZOS)
BG = {"basement": load("/home/claude/s1e10/bg/basement.png"), "living": load("/home/claude/s1e1/bg/living.png"),
      "flash": load("/home/claude/s1e9/bg/flash.png"), "window": load("/home/claude/s1e9/bg/window.png"),
      "morning": load("/home/claude/s1e10/bg/morning.png"), "bedroom": load("/home/claude/s1e1/bg/bedroom_clean.png"),
      "roof": load("/home/claude/s1e6/bg/roof_raw.png")}
def cam(img, cx, cy, z):
    cw, ch = W / z, H / z; x0 = min(max(cx - cw / 2, 0), W - cw); y0 = min(max(cy - ch / 2, 0), H - ch)
    return img.resize((W, H), Image.BICUBIC, box=(x0, y0, x0 + cw, y0 + ch)), (x0, y0, z)
def tint(img, lvl, col): return ImageChops.multiply(ImageEnhance.Brightness(img).enhance(lvl), Image.new("RGB", img.size, col))

yy, xx = np.mgrid[0:H, 0:W]
vg = np.clip(1 - 0.85 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2), 0.1, 1)
VIG = Image.fromarray((vg * 255).astype(np.uint8)).convert("RGB")
NOISE = [np.random.default_rng(i).normal(0, 1, (H // 2, W // 2)).astype(np.float32) for i in range(8)]
SCAN = Image.fromarray(np.tile(((np.arange(H) % 4 < 2) * 40 + 215).astype(np.uint8)[:, None], (1, W))).convert("RGB")

def ltr(img, x, y, s, size, fill, anchor="lm", sw=2):
    ImageDraw.Draw(img).text((x, y), s, font=ImageFont.truetype(FONT, size), fill=fill, anchor=anchor, direction="ltr", stroke_width=sw, stroke_fill=(0, 0, 0))

def char(img, who, x, y, s, expr, mouth=0.0, arms="down", held=None, look=0, tt=0.0, sil=False, blur=0):
    L = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(L)
    blink = ((tt + (hash(who) % 7) * 0.37) % 3.4) < 0.1 and expr not in ("sleepy",)
    draw_char(p, who, x, y, s, expr, mouth, look, blink, arms, tt, held)
    L = L.resize((W, H), Image.LANCZOS)
    if sil:
        al = L.getchannel("A"); L = Image.new("RGBA", L.size, (5, 5, 6, 255)); L.putalpha(al)
    if blur: L = L.filter(ImageFilter.GaussianBlur(blur))
    img.paste(L, (0, 0), L)

def mouth_of(who, tt):
    k, lt = line_at(tt)
    if k and WHO.get(k) == who: return float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)])
    return 0.0

def cctv(fr, tt, label="CAM 03"):
    g = ImageEnhance.Contrast(fr.convert("L")).enhance(1.25)
    a = np.asarray(g, np.float32) * 0.85
    n = NOISE[int(tt * FPS) % 8]; a += np.repeat(np.repeat(n, 2, 0), 2, 1) * 16
    if int(tt * FPS) % 37 == 0: a[rng.integers(0, H - 40):, :] *= 0.6
    im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).convert("RGB")
    im = ImageChops.multiply(ImageChops.multiply(im, SCAN), VIG)
    im = ImageChops.multiply(im, Image.new("RGB", (W, H), (205, 230, 205)))
    d = ImageDraw.Draw(im)
    if int(tt * 2) % 2: d.ellipse([70, 66, 102, 98], fill=(230, 30, 30))
    ltr(im, 120, 82, "REC", 40, (240, 240, 240))
    ltr(im, W - 70, 82, f"{label}  B1", 40, (240, 240, 240), anchor="rm")
    s = int(7 + tt) % 60
    ltr(im, 70, H - 80, f"2026-11-09   03:12:{s:02d} AM", 40, (240, 240, 240))
    text(im, W - 210, H - 82, "البدروم", 44, (240, 240, 240), (0, 0, 0), 3)
    for c in ((60, 50), (W - 60, 50), (60, H - 50), (W - 60, H - 50)):
        sx = 1 if c[0] < W / 2 else -1; sy = 1 if c[1] < H / 2 else -1
        d.line([c, (c[0] + sx * 70, c[1])], fill=(230, 230, 230), width=4); d.line([c, (c[0], c[1] + sy * 70)], fill=(230, 230, 230), width=4)
    return im

def glitch(tt):
    a = np.asarray(Image.new("RGB", (W, H), (0, 0, 0))).astype(np.float32)
    n = NOISE[int(tt * 60) % 8]; v = np.repeat(np.repeat(n, 2, 0), 2, 1) * 90 + 110
    im = Image.fromarray(np.clip(np.stack([v, v * 0.9, v * 1.1], -1), 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(im)
    for i in range(10):
        y = rng.integers(0, H); d.rectangle([0, y, W, y + rng.integers(4, 40)], fill=tuple(int(x) for x in rng.integers(0, 255, 3)))
    return im

def news(tt):
    fr, _ = cam(BG["living"], 960, 560, 1.12 + 0.05 * kk(tt, NEWS0, SW2_T))
    fr = tint(fr, 1.3, (255, 238, 222))
    frozen = tt >= KN[0]
    k, lt = line_at(tt)
    expr = "shock" if frozen else "happy"
    bob = 0 if frozen else abs(math.sin(tt * 3)) * 8
    char(fr, "sawsan", 960, 1110 - bob, 2.9, expr, mouth_of("sawsan", tt), "talk" if not frozen else "scared", None, 0, tt)
    if frozen and tt < KN[1] + 0.3:
        fr = fr.transform(fr.size, Image.AFFINE, (1, 0, rng.normal(0, 8), 0, 1, rng.normal(0, 8)))
    d = ImageDraw.Draw(fr, "RGBA")
    d.rectangle([0, 850, W, 935], fill=(170, 20, 25, 235)); d.rectangle([0, 935, W, 990], fill=(15, 15, 25, 235))
    d.rectangle([W - 330, 850, W, 935], fill=(255, 214, 60, 255))
    text(fr, W - 165, 893, "عاجل", 60, (120, 10, 10), (255, 214, 60), 0)
    text(fr, W - 820, 893, "أصوات غريبة من بدروم عمارة نعناعة", 46, (255, 255, 255), (120, 0, 0), 2)
    tick = "الجيران مش نايمين  •  البواب: أنا صاحي أهو  •  فهمي اتمسك امبارح  •  إيه اللي في البدروم؟  •  "
    off = (tt * 220) % 1600
    for i in range(-1, 3):
        text(fr, -400 + off + i * 1600, 962, tick, 34, (230, 230, 230), (0, 0, 0), 0, anchor="lm")
    d.rounded_rectangle([60, 60, 330, 125], 14, fill=(220, 30, 40, 240)); d.ellipse([82, 80, 108, 106], fill=(255, 255, 255))
    ltr(fr, 125, 93, "LIVE", 42, (255, 255, 255), sw=0)
    d.rounded_rectangle([350, 60, 820, 125], 14, fill=(0, 0, 0, 160))
    text(fr, 585, 93, "طنط سوسن لايف", 40, (255, 214, 90), (0, 0, 0), 0)
    return fr

def lost(tt):
    cols = [(192, 192, 192), (192, 192, 0), (0, 192, 192), (0, 192, 0), (192, 0, 192), (192, 0, 0), (0, 0, 192)]
    fr = Image.new("RGB", (W, H)); d = ImageDraw.Draw(fr)
    for i, c in enumerate(cols): d.rectangle([i * W / 7, 0, (i + 1) * W / 7, H * 0.72], fill=c)
    d.rectangle([0, H * 0.72, W, H], fill=(20, 20, 20))
    a = np.asarray(fr, np.float32) + np.repeat(np.repeat(NOISE[int(tt * 30) % 8], 2, 0), 2, 1)[..., None] * 30
    fr = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    ImageDraw.Draw(fr, "RGBA").rounded_rectangle([W / 2 - 420, H / 2 - 90, W / 2 + 420, H / 2 + 90], 20, fill=(0, 0, 0, 220))
    text(fr, W / 2, H / 2, "الإرسال اتقطع", 90, (255, 255, 255), (0, 0, 0), 0)
    return fr

def sepia(fr, tt):
    g = np.asarray(fr.convert("L"), np.float32) / 255
    out = np.stack([g * 268, g * 220, g * 170], -1) * (0.93 + 0.07 * math.sin(tt * 37)) + np.array([18, 10, 0])
    im = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)); d = ImageDraw.Draw(im, "RGBA"); r = np.random.default_rng(int(tt * FPS))
    for _ in range(3):
        x = r.uniform(0, W); d.line([(x, 0), (x + r.uniform(-20, 20), H)], fill=(40, 30, 20, int(r.uniform(30, 90))), width=2)
    return im

def letter(tt, s):
    k = kk(tt, s["start"], s["end"])
    fr = Image.new("RGB", (W, H), (60, 38, 20)); d = ImageDraw.Draw(fr)
    for i in range(0, W, 9): d.line([(i, 0), (i + math.sin(i * 0.03) * 25, H)], fill=(70 + (i * 7) % 12, 44, 24), width=4)
    z = 1 + 0.15 * k; cx, cy = W / 2, H / 2 + 10; pw, ph = 600 * z, 400 * z
    d.polygon([(cx - pw, cy - ph), (cx + pw, cy - ph + 14), (cx + pw - 10, cy + ph), (cx - pw + 8, cy + ph - 12)], fill=(238, 224, 190), outline=(120, 95, 60))
    d.rectangle([cx + pw - 190 * z, cy - ph + 40 * z, cx + pw - 50 * z, cy - ph + 200 * z], fill=(190, 60, 50), outline=(120, 30, 20), width=4)
    text(fr, cx, cy - 160 * z, "يا نعناعة يا أختي...", int(70 * z), (40, 40, 90), (238, 224, 190), 0)
    for i in range(4):
        y = cy - 40 * z + i * 70 * z; d.line([(cx - 420 * z, y), (cx + 420 * z - i * 60 * z, y)], fill=(90, 90, 130), width=max(2, int(4 * z)))
    text(fr, cx + 300 * z, cy + 290 * z, "رشدي", int(60 * z), (40, 40, 90), (238, 224, 190), 0)
    g = Image.new("L", (W, H), 0); fl = 0.85 + 0.15 * math.sin(tt * 13) * math.sin(tt * 5)
    ImageDraw.Draw(g).ellipse([cx - 900, cy - 700, cx + 900, cy + 700], fill=int(255 * fl))
    fr = Image.composite(fr, ImageEnhance.Brightness(fr).enhance(0.35), g.filter(ImageFilter.GaussianBlur(160)))
    return fr

def frame(tt):
    s = next((x for x in segs if x["start"] <= tt < x["end"]), segs[-1]); n = s["name"]; k = kk(tt, s["start"], s["end"])
    if n == "cctv1":
        fr, c = cam(BG["basement"], 960, 540, 1.04 + 0.03 * k)
        fl = 1.0 if not (2.0 < tt < 3.2) else (0.45 if int(tt * 14) % 3 == 0 else 1.0)
        fr = ImageEnhance.Brightness(fr).enhance(1.9 * fl)
        if 3.4 < tt < 5.8:
            u = kk(tt, 3.4, 5.8); char(fr, "roshdy", 500 + 900 * u, 950, 3.0, "neutral", 0, "hold", None, 1, tt, sil=True, blur=6)
        if any(0 <= tt - k_ < 0.12 for k_ in (5.4, 5.9)): fr = fr.transform(fr.size, Image.AFFINE, (1, 0, rng.normal(0, 10), 0, 1, rng.normal(0, 10)))
        return cctv(fr, tt)
    if n == "glitch": return glitch(tt)
    if n == "news": return news(tt)
    if n == "lost": return lost(tt)
    if n == "black": return Image.new("RGB", (W, H))
    if n == "letter": fr = letter(tt, s)
    elif n == "flash":
        fr, _ = cam(BG["flash"], 1000, 540, 1.05 + 0.12 * k)
        u = ease(kk(tt, s["start"] + 1.0, s["end"]))
        char(fr, "youngnana", 640, 960, 1.6, "happy", 0, "down", None, 1, tt)
        char(fr, "roshdy", 980 + 450 * u, 960, 1.6, "smug", 0, "hold", "paper", 1, tt)
        fr = sepia(fr, tt)
    elif n == "window":
        fr, _ = cam(BG["window"], 1000, 420 + 260 * ease(k), 1.15)
        fr = tint(fr, 1.5, (180, 195, 245))
    elif n == "lobby":
        fr, _ = cam(BG["morning"], 900 + 760 * ease(k), 600 + 120 * ease(k), 1.0 + 1.0 * ease(k))
        fr = tint(fr, 0.8, (130, 150, 215))
    elif n == "door":
        fr, _ = cam(BG["morning"], 1680, 760, 2.6 + 0.4 * k)
        fr = tint(fr, 0.65, (120, 140, 210))
        g = Image.new("L", (W, H), 0); fl = 0.7 + 0.3 * math.sin(tt * 23) * math.sin(tt * 7)
        ImageDraw.Draw(g).rectangle([W / 2 - 420, H - 160, W / 2 + 420, H - 120], fill=int(255 * fl))
        fr.paste(Image.new("RGB", (W, H), (255, 190, 110)), (0, 0), g.filter(ImageFilter.GaussianBlur(26)))
    elif n.startswith("cu_"):
        who = n[3:]
        if who == "nana":
            fr, _ = cam(BG["living"], 960, 540, 1.3); fr = tint(fr, 0.9, (255, 220, 190))
            char(fr, "nana", 960, 1280, 3.6, "angry", mouth_of("nana", tt), "up", "slipper", 0, tt)
        elif who == "shatta":
            fr, _ = cam(BG["bedroom"], 900, 520, 1.3); fr = tint(fr, 0.55, (200, 190, 255))
            char(fr, "shatta", 960, 1300, 3.6, "angry", mouth_of("shatta", tt), "hold", "torch", 0, tt)
            g = Image.new("L", (W, H), 0); ImageDraw.Draw(g).ellipse([700, 250, 1300, 800], fill=110)
            fr.paste(Image.new("RGB", (W, H), (255, 240, 200)), (0, 0), g.filter(ImageFilter.GaussianBlur(90)))
        else:
            fr, _ = cam(BG["roof"], 960, 520, 1.25); fr = tint(fr, 0.85, (170, 185, 240))
            char(fr, "zalata", 960, 1300, 3.6, "flat", mouth_of("zalata", tt), "hold", "nbpen", 0, tt)
        z = 1 + 0.06 * k
        fr = fr.resize((int(W * z), int(H * z)), Image.BILINEAR).crop((int(W * (z - 1) / 2), int(H * (z - 1) / 2), int(W * (z - 1) / 2) + W, int(H * (z - 1) / 2) + H))
    elif n == "cctv2":
        fr, _ = cam(BG["basement"], 300, 560, 1.6)
        fr = ImageEnhance.Brightness(fr).enhance(1.7)
        if tt >= DOOR_OPEN:
            u = kk(tt, DOOR_OPEN, DOOR_OPEN + 1.2)
            g = Image.new("L", (W, H), 0); ImageDraw.Draw(g).polygon([(560, 120), (560 + 260 * u, 150), (560 + 260 * u, 900), (560, 960)], fill=int(200 * u))
            fr.paste(Image.new("RGB", (W, H), (255, 255, 255)), (0, 0), g.filter(ImageFilter.GaussianBlur(10)))
        if tt >= POP:
            u = kk(tt, POP, POP + 0.15)
            char(fr, "shatta", 960, 2700 - 600 * u, 9.0, "shock", mouth_of("shatta", tt) * 0 + 0.9, "up", None, 0, tt)
            fr = fr.transform(fr.size, Image.AFFINE, (1, 0, rng.normal(0, 14), 0, 1, rng.normal(0, 14)))
        return cctv(fr, tt, "CAM 04")
    elif n == "title":
        fr = Image.new("RGB", (W, H), (6, 6, 10))
        g = Image.new("L", (W, H), 0); ImageDraw.Draw(g).rectangle([W / 2 - 520, H - 200, W / 2 + 520, H - 150], fill=255)
        fr.paste(Image.new("RGB", (W, H), (255, 180, 90)), (0, 0), g.filter(ImageFilter.GaussianBlur(60)))
        a = min(1, k * 5); col = lambda c: tuple(int(v * a) for v in c)
        text(fr, W / 2, 250, "عمارة نعناعة", 120, col((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, 420, "الموسم التاني", 70, col((235, 235, 235)), (0, 0, 0), 4)
        if k > 0.18:
            sc = 1 + 0.5 * max(0, 1 - (k - 0.18) * 8)
            text(fr, W / 2, 600, "سر البدروم", int(170 * sc), (230, 60, 50), (20, 0, 0), 8)
        if k > 0.45: text(fr, W / 2, 790, "قريباً", 80, (255, 255, 255), (0, 0, 0), 4)
        d = ImageDraw.Draw(fr, "RGBA")
        for i in range(40):
            u = (tt * 0.05 + i * 0.137) % 1; x = (i * 211) % W; y = H - u * H
            d.ellipse([x - 2, y - 2, x + 2, y + 2], fill=(255, 220, 160, int(180 * (1 - u))))
        return fr
    a = np.asarray(ImageChops.multiply(fr, VIG), np.float32) + np.repeat(np.repeat(NOISE[int(tt * FPS) % 8], 2, 0), 2, 1)[..., None] * 4
    fr = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    e = tt - s["start"]
    if e < 0.1: fr = Image.blend(fr, Image.new("RGB", (W, H)), 1 - e / 0.1)
    return fr

def subtitle(img, tt, v=False):
    k, _ = line_at(tt)
    if not k or not SUB[k]: return
    s = SUB[k]
    if v:
        words = s.split(" "); out = [""]
        for w_ in words:
            if len(out[-1]) + len(w_) + 1 > 24 and out[-1]: out.append(w_)
            else: out[-1] = (out[-1] + " " + w_).strip()
        for i, l in enumerate(out[:4]): text(img, 540, 1290 + i * 80, l, 60, sw=6)
        return
    y0 = 1015 if k in ("SW1", "SW2") else H - 70
    if k in ("SW1", "SW2"): y0 = 250
    if len(s) > 44:
        sp = [i for i, ch in enumerate(s) if ch == " "]; c = min(sp, key=lambda i: abs(i - len(s) // 2))
        text(img, W / 2, y0 - 55, s[:c], 48, sw=5); text(img, W / 2, y0, s[c + 1:], 48, sw=5)
    else:
        text(img, W / 2, y0, s, 48, sw=5)

def vertical(fr, tt):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = ImageEnhance.Brightness(small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.35)
    bgv.paste(fr.resize((1080, 608), Image.LANCZOS), (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(230, 60, 50)); d.rectangle([0, 1168, 1080, 1171], fill=(230, 60, 50))
    text(bgv, 540, 300, "عمارة نعناعة", 92, (255, 214, 90), (40, 10, 10), 6)
    text(bgv, 540, 420, "الموسم التاني: سر البدروم", 56, (235, 235, 235))
    subtitle(bgv, tt, True)
    return bgv

def build_audio(path="mix.wav"):
    buf = np.zeros(int(TOTAL * SR) + SR * 3, np.float32)
    ts = np.arange(int(SR * TOTAL)) / SR
    dr = drone(TOTAL + 1)[:len(ts)]; env = np.ones(len(ts), np.float32)
    a, b = int(NEWS0 * SR), int(LOST[0] * SR); env[a:b] = 0.15
    mix_into(buf, dr * np.convolve(env, np.ones(4410) / 4410, mode="same"), 0, 1.3)
    r = np.random.default_rng(5)
    t2 = np.arange(int(SR * 1.6)) / SR
    S = {"boom": sfx_boom(), "knock": sfx_knock() * 1.3,
         "sting": (np.sin(2 * np.pi * (1200 + 80 * np.sin(t2 * 40)) * t2) * 0.08 + np.sin(2 * np.pi * 55 * t2) * 0.45) * np.exp(-t2 * 1.8),
         "static": np.convolve(r.normal(0, 1, int(SR * 0.5)), np.ones(3) / 3, mode="same") * 0.35,
         "hum": (np.sin(2 * np.pi * 60 * np.arange(int(SR * 3.6)) / SR) * 0.05 + r.normal(0, 1, int(SR * 3.6)) * 0.02),
         "buzz": np.sign(np.sin(2 * np.pi * 100 * np.arange(int(SR * 1.2)) / SR)) * 0.05 * (np.sin(np.arange(int(SR * 1.2)) / SR * 40) > 0),
         "creak": load_audio("sfx/creak.mp3"), "whoosh": load_audio("sfx/whoosh.mp3")}
    S["mknock"] = np.convolve(S["knock"], np.ones(30) / 30, mode="same") * 1.3
    tj = np.arange(int(SR * 0.5)) / SR
    S["newsjingle"] = sum(np.sin(2 * np.pi * f * tj) * np.exp(-tj * 5) * 0.12 * (tj > i * 0.12) for i, f in enumerate((660, 880, 1320)))
    for t0, n, g in sfx:
        if n in S: mix_into(buf, S[n], t0, g)
    tb = np.arange(int(SR * 0.3)) / SR; hb = np.sin(2 * np.pi * 50 * tb) * np.exp(-tb * 18) * 0.5
    x = LET0 + 0.3
    while x < LET1:
        mix_into(buf, hb, x, 1.0); mix_into(buf, hb, x + 0.28, 0.6); x += 1.05
    for st, k in lines:
        a_ = AUD[k]
        if k.startswith("RO"):
            e = np.zeros(len(a_) + int(SR * 0.6), np.float32); e[:len(a_)] += a_
            for d_, g_ in ((0.09, 0.25), (0.2, 0.12)): i_ = int(d_ * SR); e[i_:i_ + len(a_)] += a_ * g_
            a_ = e
        mix_into(buf, a_, st, 1.0)
    buf = buf[:int(TOTAL * SR)]; buf = np.clip(buf / np.abs(buf).max() * 0.95, -1, 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((buf * 32767).astype(np.int16).tobytes())

if __name__ == "__main__":
    print("TOTAL", round(TOTAL, 1)); [print(x["name"], round(x["start"], 1), round(x["end"], 1)) for x in segs] if sys.argv[1:2] == ["times"] else None
    if sys.argv[1:2] == ["stills"]:
        for v in sys.argv[2:]:
            h = frame(float(v)); subtitle(h, float(v)); h.save(f"still_{float(v):.1f}.png")
    elif not sys.argv[1:]:
        build_audio()
        mk = lambda w_, h_, o: subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w_}x{h_}", "-r", str(FPS), "-i", "-",
                                                 "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-pix_fmt", "yuv420p", o], stdin=subprocess.PIPE)
        fh = mk(W, H, "h.mp4"); fv = mk(1080, 1920, "v.mp4")
        for i in range(int(TOTAL * FPS)):
            tt = i / FPS; base = frame(tt); h = base.copy(); subtitle(h, tt)
            fh.stdin.write(h.tobytes()); fv.stdin.write(vertical(base, tt).tobytes())
        fh.stdin.close(); fv.stdin.close(); fh.wait(); fv.wait()
        for vin, out in (("h.mp4", "اعلان الموسم التاني - سر البدروم.mp4"), ("v.mp4", "اعلان الموسم التاني - سر البدروم (تيك توك).mp4")):
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", vin, "-i", "mix.wav", "-c:v", "copy", "-af", "loudnorm=I=-14:TP=-1.5",
                            "-c:a", "aac", "-b:a", "192k", "-shortest", out], check=True)
        print("done")
