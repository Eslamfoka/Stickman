import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
import sys, math, subprocess, wave
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter
from engine import *

SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(7)

# ---------------- lines ----------------
SUB = {
 "L00": "آآآه! النور قطع!",
 "L01": "سامعين؟ الصوت جاي من فوق... من الدور السابع!",
 "L02": "الدور السابع مقفول بقاله تلاتين سنة يا شطة. يعني احتمال إن فيه حد فوق... صفر.",
 "L03": "...أنا هعيد الحسبة.",
 "L04": "الخبط ده مش عشوائي. اسمعوا كويس... تلات خبطات، وبعدين سكوت.",
 "L05": "محدش هيطلع فوق. فاهمين؟ محدش!",
 "L06": "يا تيتا! خضيتينا! هو مين اللي فوق؟",
 "L07": "...مفيش حد. يلا، كل واحد على سريره.",
 "L08": "أنا طالع أشوف. بكرة الساعة اتناشر بالظبط. ثقوا فيا المرة دي!",
 "L09": "آخر مرة قالها، العمارة كلها اتشبشبت.",
 "L10": "وأنا جاية معاكو. إنتو مش هتعرفوا تعدوا الخبط صح من غيري.",
 "L11": "وإنتو كمان! عدوا الخبط معانا، واكتبوا في الكومنتات... كام خبطة سمعتو؟",
 "L12": "بدأت تاني يا رشدي؟... إنت بدأت تاني.",
 "L13": "«ما تطلعوش»... مين اللي كتب دي؟",
}
WHO = {"L00": "shatta", "L01": "shatta", "L02": "zalata", "L03": "zalata", "L04": "tota", "L05": "nana",
       "L06": "shatta", "L07": "nana", "L08": "shatta", "L09": "zalata", "L10": "tota", "L11": "tota",
       "L12": "bondo2", "L13": "shatta"}
EXPR = {"L00": "shock", "L01": "scared", "L02": "flat", "L03": "flat", "L04": "neutral", "L05": "angry",
        "L06": "shock", "L07": "sad", "L08": "happy", "L09": "flat", "L10": "smug", "L11": "happy",
        "L12": "sad", "L13": "scared"}
AUD = {k: load_audio(f"audio/{k}.mp3") for k in SUB}
ENV = {k: envelope(v) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}

# ---------------- timeline ----------------
lines = []      # (start, key)
sfx = []        # (t, kind)
knocks = []     # times (for shake / reactions)
shots = []      # dict(start,end,name)
jumps = {}      # who -> [times]
def say(t, k):
    lines.append((t, k)); return t + DUR[k]
def knock(t):
    sfx.append((t, "knock")); knocks.append(t)
def jump(who, t): jumps.setdefault(who, []).append(t)

t = 0.0
# COLD OPEN
s0 = t
for i in range(3): sfx.append((0.3 + i * 0.75, "tick"))
for k in (2.4, 2.85, 3.3, 4.4, 4.85, 5.3): knock(k)
sfx.append((5.9, "powercut")); POWER_CUT = 6.0
jump("shatta", 6.25)
t = say(6.3, "L00") + 0.6
shots.append(dict(start=s0, end=t, name="cold"))
# TITLE
sfx.append((t, "boom")); shots.append(dict(start=t, end=t + 3.0, name="title")); t += 3.0
# SCENE 1
s1 = t; t += 0.7
t = say(t, "L01") + 0.3
t = say(t, "L02") + 0.5
SC1_KNOCK = t
for i in range(3): knock(t + i * 0.45)
t += 0.45 * 2 + 1.1
t = say(t, "L03") + 0.3
t = say(t, "L04") + 0.5
NANA_IN = t - 0.6
t = say(t, "L05") + 0.25
jump("shatta", t)
t = say(t, "L06") + 0.3
t = say(t, "L07") + 0.9
shots.append(dict(start=s1, end=t, name="living"))
# SCENE 2
s2 = t; t += 0.6
t = say(t, "L08") + 0.3
t = say(t, "L09") + 0.3
t = say(t, "L10") + 0.4
PUZ = t
t = say(t, "L11") + 2.2
PUZ_END = t - 0.2
shots.append(dict(start=s2, end=t, name="bedroom"))
# SCENE 3
s3 = t; t += 1.4
t = say(t, "L12") + 1.0
shots.append(dict(start=s3, end=t, name="lobby"))
# ENDING
s4 = t
PAPER = t + 0.5; sfx.append((PAPER, "paper"))
t += 2.0
t = say(t, "L13") + 0.5
DOOR_KNOCK = t; knock(t); jump("shatta", t + 0.05)
t += 1.5
shots.append(dict(start=s4, end=t, name="ending"))
sfx.append((t, "boom")); shots.append(dict(start=t, end=t + 3.2, name="endcard")); t += 3.2
TOTAL = t

READ = next(st for st, k in lines if k == "L13")
INSERT = (READ - 0.15, READ + 1.75)

def make_paper():
    im = Image.new("RGB", (W, H), (14, 16, 26))
    nz = (np.random.default_rng(5).normal(0, 1, (H, W)) * 6).astype(np.int16)
    base = np.zeros((H, W, 3), np.int16) + np.array([14, 16, 26], np.int16)
    im = Image.fromarray(np.clip(base + nz[..., None], 0, 255).astype(np.uint8))
    pl = Image.new("RGBA", (1300, 820), (0, 0, 0, 0)); d = ImageDraw.Draw(pl)
    edge = [(20, 30), (400, 10), (800, 34), (1280, 14), (1270, 420), (1290, 800), (850, 790), (420, 810), (10, 795), (28, 400)]
    d.polygon(edge, fill=(232, 222, 196, 255))
    pn = (np.random.default_rng(6).normal(0, 1, (820, 1300)) * 7).astype(np.int16)
    arr = np.array(pl).astype(np.int16); arr[..., :3] = np.clip(arr[..., :3] + pn[..., None], 0, 255)
    pl = Image.fromarray(arr.astype(np.uint8)); d = ImageDraw.Draw(pl)
    d.line([(650, 20), (640, 800)], fill=(200, 188, 160, 255), width=3)
    d.line([(20, 410), (1280, 400)], fill=(205, 192, 165, 255), width=3)
    f = ImageFont.truetype(FONT, 175)
    for dx, dy in ((0, 0), (3, 2), (-2, 3)):
        d.text((650 + dx, 400 + dy), "ما تطلعوش", font=f, fill=(150, 10, 10, 230), anchor="mm",
               direction="rtl", language="ar")
    d.text((650, 400), "ما تطلعوش", font=f, fill=(185, 18, 18, 255), anchor="mm", direction="rtl", language="ar")
    pl = pl.rotate(-5, resample=Image.BICUBIC, expand=True)
    im.paste(pl, ((W - pl.width) // 2, (H - pl.height) // 2), pl)
    return im
PAPER_IMG = make_paper()

def paper_frame(tt):
    k = (tt - INSERT[0]) / (INSERT[1] - INSERT[0])
    z = 1.0 + 0.12 * k
    cw, ch = W / z, H / z
    ox = (W - cw) / 2 + math.sin(tt * 17) * 6; oy = (H - ch) / 2 + math.cos(tt * 13) * 5
    fr = PAPER_IMG.crop((int(ox), int(oy), int(ox + cw), int(oy + ch))).resize((W, H), Image.LANCZOS)
    fr = ImageEnhance.Brightness(fr).enhance(0.92 + 0.08 * math.sin(tt * 31))
    return ImageChops.multiply(fr, VIG)

def shot_at(tt):
    for s in shots:
        if s["start"] <= tt < s["end"]: return s
    return shots[-1]

def line_at(tt):
    for st, k in lines:
        if st <= tt < st + DUR[k]: return k, tt - st
    return None, 0

# ---------------- backgrounds ----------------
def load_bg(path):
    return Image.open(path).convert("RGB").resize((SSW, SSH), Image.LANCZOS)
BG = {"cold": load_bg("bg/stairs_1080.png"), "living": load_bg("bg/living_1080.png"),
      "bedroom": load_bg("bg/bedroom_clean.png"), "ending": load_bg("bg/bedroom_clean.png"),
      "lobby": load_bg("bg/lobby_1080.png")}
# vignette
yy, xx = np.mgrid[0:H, 0:W]
vg = 1 - 0.55 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) ** 1.2
VIG = Image.fromarray((np.clip(vg, 0.25, 1) * 255).astype(np.uint8)).convert("RGB")

TINT = {"cold": (255, 225, 180), "living": (255, 196, 140), "bedroom": (165, 185, 255),
        "ending": (165, 185, 255), "lobby": (210, 235, 210)}

def light_level(name, tt):
    if name == "cold":
        if tt < POWER_CUT - 0.1: return 1.0
        if tt < POWER_CUT + 0.25: return 0.15 + 0.85 * (int(tt * 30) % 2)
        return 0.32
    if name == "living":
        f = 0.85 + 0.08 * math.sin(tt * 9) + 0.05 * math.sin(tt * 23)
        if SC1_KNOCK <= tt < SC1_KNOCK + 1.6: f *= 0.6 + 0.4 * (int(tt * 18) % 2)
        return f
    if name == "lobby":
        return 0.9 if (int(tt * 7) % 23) != 0 else 0.45
    return 0.9

# ---------------- actors per shot ----------------
def actors(name, tt):
    A = []
    if name == "cold":
        A.append(dict(who="shatta", x=640, y=1030, s=2.3, look=1, arms="scared" if tt > 2.4 else "down",
                      expr="scared" if tt > 2.4 else "neutral"))
    elif name == "living":
        A += [dict(who="shatta", x=520, y=1030, s=2.4, look=1),
              dict(who="zalata", x=860, y=1030, s=2.4, look=-1, held="notebook"),
              dict(who="tota", x=1180, y=1030, s=2.4, look=-1)]
        if tt >= NANA_IN:
            a = min(1, (tt - NANA_IN) / 0.8)
            A.append(dict(who="nana", x=1580, y=1030, s=2.45, look=-1, arms="hips", alpha=a))
    elif name == "bedroom":
        A += [dict(who="shatta", x=620, y=1030, s=2.4, look=1),
              dict(who="zalata", x=960, y=1030, s=2.4, look=-1, held="notebook"),
              dict(who="tota", x=1280, y=1030, s=2.4, look=-1, held="torch")]
    elif name == "lobby":
        A.append(dict(who="bondo2", x=430, y=860, s=2.1, look=1, held="key", arms="hold", expr="sad"))
    elif name == "ending":
        A.append(dict(who="shatta", x=1080, y=1015, s=2.25, look=1,
                      held="paper" if tt > PAPER + 1.3 else None,
                      arms="hold" if tt > PAPER + 1.3 else "down"))
    return A

def jump_off(who, tt):
    for j in jumps.get(who, []):
        if 0 <= tt - j < 0.4:
            return math.sin((tt - j) / 0.4 * math.pi) * 55
    return 0

def draw_actors(name, tt):
    layer = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0))
    k, lt = line_at(tt)
    focus = None
    for a in actors(name, tt):
        who = a["who"]
        talking = k is not None and WHO[k] == who
        expr = a.get("expr", "neutral")
        recent_knock = any(0 <= tt - kn < 2.2 for kn in knocks)
        if recent_knock and name in ("living", "ending", "cold"): expr = "scared"
        if who == "tota" and not talking and not recent_knock: expr = "smug"
        if talking: expr = EXPR[k]
        mouth = 0.0
        if talking:
            e = ENV[k]; fi = int(lt * FPS)
            mouth = float(e[min(fi, len(e) - 1)])
        arms = a.get("arms", "down")
        if talking and arms == "down": arms = "talk"
        if talking and k == "L01": arms = "scared"
        if talking and k == "L08": arms = "up"
        if talking and k == "L11": arms = "point"
        if talking and k == "L05": arms = "point"
        if name == "living" and who == "shatta" and SC1_KNOCK <= tt < SC1_KNOCK + 2: arms = "scared"
        y = a["y"] - jump_off(who, tt)
        shiver = math.sin(tt * 60) * 2.5 if expr in ("scared", "shock") else 0
        blink = ((tt + hash(who) % 7 * 0.37) % 3.6) < 0.11
        al = a.get("alpha", 1.0)
        L = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(L)
        s = a["s"]
        p.ell(a["x"], a["y"] + 4, 46 * s, 9 * s, (0, 0, 0, 110), None)  # shadow
        draw_char(p, who, a["x"] + shiver, y, s, expr, mouth, a.get("look", 0), blink, arms, tt, a.get("held"))
        if al < 1:
            alpha = L.getchannel("A").point(lambda v: int(v * al))
            L.putalpha(alpha)
        layer = Image.alpha_composite(layer, L)
        if talking:
            hs = s * CH[who]["scale"]
            focus = (a["x"], y - 200 * hs, s)
    return layer, focus

def tint_layer(layer, tint, lvl):
    rgb = layer.convert("RGB"); al = layer.getchannel("A")
    c = tuple(int((v * 0.55 + 255 * 0.45) * min(1.0, lvl * 1.05)) for v in tint)
    rgb = ImageChops.multiply(rgb, Image.new("RGB", rgb.size, c))
    out = rgb.convert("RGBA"); out.putalpha(al)
    return out

# ---------------- camera ----------------
class Cam:
    def __init__(s): s.cx, s.cy, s.z = W / 2, H / 2, 1.0
    def go(s, tx, ty, tz, a=0.07):
        s.z += (tz - s.z) * a; s.cx += (tx - s.cx) * a; s.cy += (ty - s.cy) * a
    def crop(s, img, shake=0.0):
        z = s.z; cw, ch = W / z, H / z
        x0 = min(max(s.cx - cw / 2, 0), W - cw); y0 = min(max(s.cy - ch / 2, 0), H - ch)
        if shake:
            x0 = min(max(x0 + rng.normal(0, shake), 0), W - cw); y0 = min(max(y0 + rng.normal(0, shake), 0), H - ch)
        box = tuple(int(v * SS) for v in (x0, y0, x0 + cw, y0 + ch))
        return img.crop(box).resize((W, H), Image.LANCZOS)

def subtitle(img, tt):
    k, _ = line_at(tt)
    if not k: return
    s = SUB[k]
    if len(s) > 44:
        sp = [i for i, ch in enumerate(s) if ch == " "]; cut = min(sp, key=lambda i: abs(i - len(s) // 2))
        text(img, W / 2, H - 125, s[:cut], 46, sw=5); text(img, W / 2, H - 62, s[cut + 1:], 46, sw=5)
    else:
        text(img, W / 2, H - 70, s, 46, sw=5)

def render(t0=0, t1=None, out="video.mp4", stills=None, mode="h"):
    t1 = TOTAL if t1 is None else t1
    cams = {}
    ff = None
    if not stills:
        OW, OH = (W, H) if mode == "h" else (1080, 1920)
        ff = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{OW}x{OH}",
                               "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "19",
                               "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    times = stills if stills else [t0 + i / FPS for i in range(int((t1 - t0) * FPS))]
    for tt in times:
        sh = shot_at(tt); name = sh["name"]
        if name in ("title", "endcard"):
            fr = Image.new("RGB", (W, H), (8, 8, 12))
            k = min(1, (tt - sh["start"]) / 0.6)
            col = tuple(int(c * k) for c in (255, 214, 90))
            if name == "title":
                text(fr, W / 2, H / 2 - 70, "عمارة نعناعة", 110, col, (40, 10, 10), 6)
                text(fr, W / 2, H / 2 + 60, "سر الدور السابع", 64, tuple(int(c * k) for c in (230, 230, 230)))
                text(fr, W / 2, H / 2 + 150, "الحلقة 1: الصوت اللي في السقف", 44, tuple(int(c * k) for c in (200, 200, 200)))
            else:
                text(fr, W / 2, H / 2 - 30, "الحلقة 2 بكرة", 100, col, (40, 10, 10), 6)
                text(fr, W / 2, H / 2 + 90, "اكتب حلّك في الكومنتات", 48, tuple(int(c * k) for c in (230, 230, 230)))
        elif name == "ending" and INSERT[0] <= tt < INSERT[1]:
            fr = paper_frame(tt)
            cams.setdefault(name, Cam())
            if mode == "h": subtitle(fr, tt)
        else:
            lvl = light_level(name, tt)
            bg = BG[name]
            if lvl < 0.99:
                bg = ImageEnhance.Brightness(bg).enhance(lvl)
            layer, focus = draw_actors(name, tt)
            layer = tint_layer(layer, TINT[name], lvl)
            img = bg.copy(); img.paste(layer, (0, 0), layer)
            if name == "living":   # candle glow
                d = ImageDraw.Draw(img, "RGBA")
                r = int((60 + 6 * math.sin(tt * 11)) * SS)
                cx, cy = int(795 * SS), int(482 * SS)
                for i in range(6, 0, -1):
                    d.ellipse([cx - r * i // 2, cy - r * i // 2, cx + r * i // 2, cy + r * i // 2], fill=(255, 170, 80, 7))
            if name == "ending" and tt >= PAPER:
                d = ImageDraw.Draw(img)
                k = min(1, (tt - PAPER) / 0.9)
                if tt < PAPER + 1.3:
                    px = 1600 - 230 * k; py = 1000 + 40 * k
                    d.polygon([(int((px - 50) * SS), int(py * SS)), (int((px + 50) * SS), int((py - 6) * SS)),
                               (int((px + 56) * SS), int((py + 24) * SS)), (int((px - 46) * SS), int((py + 30) * SS))],
                              fill=(220, 215, 195))
            cam = cams.setdefault(name, Cam())
            if name == "cold":
                cam.go(700, 560, 1.0 + 0.05 * (tt - sh["start"]) / 9, 0.05)
            elif name == "ending" and tt >= DOOR_KNOCK:
                cam.go(1080, 1015 - 200 * 2.25 + 50, 2.6, 0.22)
            elif name == "lobby":
                cam.go(560, 520, 1.0 + 0.35 * min(1, (tt - sh["start"]) / 5), 0.06)
            elif name == "bedroom" and PUZ <= tt < PUZ_END:
                cam.go(1280, 640, 1.45, 0.08)
            elif focus:
                fx, fy, s = focus; cam.go(fx, fy + 140, 1.18, 0.06)
            else:
                cam.go(W / 2, H / 2, 1.0, 0.05)
            shake = 0
            for kn in knocks:
                if 0 <= tt - kn < 0.25: shake = 14 * (1 - (tt - kn) / 0.25)
            fr = cam.crop(img, shake)
            fr = ImageChops.multiply(fr, VIG)
            if name == "bedroom" and PUZ <= tt < PUZ_END and mode == "h":
                d = ImageDraw.Draw(fr, "RGBA")
                d.rounded_rectangle([W / 2 - 640, 60, W / 2 + 640, 200], 24, fill=(20, 20, 30, 210), outline=(255, 214, 90, 255), width=4)
                text(fr, W / 2, 130, "لغز الحلقة: كام خبطة سمعت؟ اكتب في الكومنتات", 40, (255, 214, 90))
            fade = min(1, (tt - sh["start"]) / 0.35, (sh["end"] - tt) / 0.35)
            if name == "ending" and tt > sh["end"] - 0.3: fade = 0
            if fade < 1: fr = Image.blend(Image.new("RGB", (W, H)), fr, max(0, fade))
            if mode == "h": subtitle(fr, tt)
        if mode == "v":
            fr = vertical(fr, tt)
        if stills:
            fr.save(f"still_{mode}_{tt:.1f}.png")
        else:
            ff.stdin.write(fr.tobytes())
    if ff: ff.stdin.close(); ff.wait()

def wrap(s, n=26):
    words = s.split(" "); out = [""]
    for w_ in words:
        if len(out[-1]) + len(w_) + 1 > n and out[-1]: out.append(w_)
        else: out[-1] = (out[-1] + " " + w_).strip()
    return out

def vertical(fr, tt):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)
    bgv = ImageEnhance.Brightness(bgv).enhance(0.35)
    main = fr.resize((1080, 608), Image.LANCZOS)
    bgv.paste(main, (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(255, 214, 90)); d.rectangle([0, 1168, 1080, 1171], fill=(255, 214, 90))
    text(bgv, 540, 330, "سر الدور السابع", 92, (255, 214, 90), (40, 10, 10), 6)
    text(bgv, 540, 450, "الحلقة 1: الصوت اللي في السقف", 50, (235, 235, 235))
    k, _ = line_at(tt)
    if k:
        ls = wrap(SUB[k])
        y0 = 1300
        for i, l in enumerate(ls[:4]):
            text(bgv, 540, y0 + i * 80, l, 60, sw=6)
    if PUZ <= tt < PUZ_END:
        d.rounded_rectangle([60, 1640, 1020, 1800], 26, fill=(20, 20, 30), outline=(255, 214, 90), width=5)
        text(bgv, 540, 1695, "لغز الحلقة: كام خبطة سمعت؟", 50, (255, 214, 90))
        text(bgv, 540, 1758, "اكتب حلّك في الكومنتات", 42)
    return bgv

def build_audio(path="mix.wav"):
    buf = np.zeros(int(TOTAL * SR) + SR, dtype=np.float32)
    mix_into(buf, drone(TOTAL + 1), 0, 0.9)
    S = {"knock": sfx_knock(), "tick": sfx_tick(), "powercut": sfx_powercut(), "paper": sfx_paper(), "boom": sfx_boom()}
    G = {"knock": 1.0, "tick": 0.8, "powercut": 0.7, "paper": 0.8, "boom": 0.7}
    for tt, k in sfx: mix_into(buf, S[k], tt, G[k])
    for st, k in lines: mix_into(buf, AUD[k], st, 1.0)
    buf = np.clip(buf / max(1e-6, np.abs(buf).max()) * 0.95, -1, 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((buf * 32767).astype(np.int16).tobytes())

if __name__ == "__main__":
    print("TOTAL", round(TOTAL, 2), [(s["name"], round(s["start"], 1)) for s in shots])
    if sys.argv[1:2] == ["stills"]:
        render(stills=[float(v) for v in sys.argv[2:]], mode="v"); render(stills=[float(v) for v in sys.argv[2:]])
    else:
        build_audio()
        render(out="video_v.mp4", mode="v")
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", "video_v.mp4", "-i", "mix.wav", "-c:v", "copy",
                        "-af", "loudnorm=I=-15:TP=-1.5", "-c:a", "aac", "-b:a", "192k", "-shortest",
                        "sirr_eldor_elsabe3_ep1_vertical.mp4"], check=True)
        render(out="video.mp4")
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", "video.mp4", "-i", "mix.wav", "-c:v", "copy",
                        "-af", "loudnorm=I=-15:TP=-1.5", "-c:a", "aac", "-b:a", "192k", "-shortest",
                        "sirr_eldor_elsabe3_ep1.mp4"], check=True)
        print("done")
