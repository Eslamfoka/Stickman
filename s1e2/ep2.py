import sys, os, math, subprocess, wave
sys.path.insert(0, "/home/claude/s1e1")
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter, ImageFont
from engine import *

SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(11)
E1 = "/home/claude/s1e1/"

SUB = {
 "E01": "في الحلقة اللي فاتت... الورقة دي اتحطت تحت باب شطة. واللي قالوا ست خبطات... إجابتكو صح! تلاتة وتلاتة.",
 "E02": "يا جماعة! الورقة لسه عندي! يعني اللي كتبها عارف أوضتي!",
 "E03": "أو إنك كتبتها وإنت نايم. أنا حاسبها بالقلم... احتمال عشرين في المية.",
 "E04": "بصوا... صندوق البوسطة بتاع شقة سبعة. محدش فتحه من سنين... بس التراب عليه ممسوح.",
 "E05": "عفريت!",
 "E06": "دي قطة يا شطة.",
 "E07": "استنوا! فيه حاجة لامعة جوه... مفتاح! ومكتوب عليه: سبعة... تلاتين.",
 "E08": "بتدوروا على حاجة يا ولاد؟",
 "E09": "إحنا؟ لا أبدا يا عمو بندق! إحنا بنعد... البوسطة!",
 "E10": "المفتاح رجع... بعد تلاتين سنة.",
 "E11": "لغز النهارده: سبعة وتلاتين، يبقوا إيه؟ اكتبوا في الكومنتات!",
 "E12": "أنا هحط المفتاح في الباب... واحد... اتنين...",
 "E13": "مش داخل. يعني المفتاح ده... مالوش باب.",
 "E14": "اجروا!",
 "E15": "خلاص... المفتاح تحت المخدة، ومحدش هيعرف مكانه.",
 "E16": "المفتاح... المفتاح راح فين؟",
}
WHO = {"E01": "tota", "E02": "shatta", "E03": "zalata", "E04": "tota", "E05": "shatta", "E06": "zalata",
       "E07": "tota", "E08": "bondo2", "E09": "shatta", "E10": "bondo2", "E11": "tota", "E12": "shatta",
       "E13": "zalata", "E14": "shatta", "E15": "shatta", "E16": "shatta"}
EXPR = {"E01": "happy", "E02": "scared", "E03": "flat", "E04": "neutral", "E05": "shock", "E06": "flat",
        "E07": "happy", "E08": "angry", "E09": "scared", "E10": "sad", "E11": "happy", "E12": "scared",
        "E13": "flat", "E14": "shock", "E15": "happy", "E16": "shock"}

def load_or_silence(k):
    p = f"audio/{k}.mp3"
    if os.path.exists(p): return load_audio(p)
    return np.zeros(int(SR * 1.6), np.float32)
AUD = {k: load_or_silence(k) for k in SUB}
ENV = {k: envelope(v) if v.any() else np.zeros(60) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}
SFXF = {n: load_audio(f"sfx/{n}.mp3") for n in ("cat", "key", "wind")}

lines, sfx, knocks, shots, jumps = [], [], [], [], {}
def say(t, k): lines.append((t, k)); return t + DUR[k]
def knock(t, g=1.0): sfx.append((t, "knock", g)); knocks.append(t)
def jump(w, t): jumps.setdefault(w, []).append(t)

t = 0.0
# 1 recap (bedroom morning)
s = t; t += 0.4
E01_T = t; t = say(t, "E01") + 0.3
INS1 = (E01_T + 1.1, E01_T + 2.9)
t = say(t, "E02") + 0.3
t = say(t, "E03") + 0.6
shots.append(dict(start=s, end=t, name="morning"))
# title
sfx.append((t, "boom", 0.7)); shots.append(dict(start=t, end=t + 2.6, name="title")); t += 2.6
# 2 lobby
s = t; t += 0.5
t = say(t, "E04") + 0.5
CAT = t; sfx.append((t - 0.15, "cat", 1.0)); jump("shatta", t + 0.3); jump("zalata", t + 0.35); jump("tota", t + 0.4)
t += 0.45
t = say(t, "E05") + 0.9
t = say(t, "E06") + 0.4
KEY = t; t = say(t, "E07") + 0.5
BONDO_IN = t; sfx.append((t, "boom", 0.6)); jump("shatta", t + 0.1); jump("tota", t + 0.15)
t += 0.7
t = say(t, "E08") + 0.3
t = say(t, "E09") + 0.4
BONDO_OUT0 = t
t = say(t, "E10") + 0.6
BONDO_OUT1 = t
PUZ = t; t = say(t, "E11") + 2.0; PUZ_END = t - 0.2
shots.append(dict(start=s, end=t, name="lobby"))
# 3 door7
s = t; t += 0.8
t = say(t, "E12") + 0.2
sfx.append((t, "key", 1.0)); KEYJAM = t; t += 1.6
t = say(t, "E13") + 0.6
DOORK = t
for i in range(3): knock(t + i * 0.45)
jump("shatta", t + 0.95); jump("zalata", t + 1.0); jump("tota", t + 1.0)
t += 1.4
t = say(t, "E14")
RUN = t; t += 1.4
shots.append(dict(start=s, end=t, name="door7"))
# 4 bedroom night
s = t; t += 0.5
t = say(t, "E15") + 0.6
CARD3 = (t, t + 1.6); t += 1.6
sfx.append((t, "wind", 1.0)); WIN = t; t += 1.4
t = say(t, "E16") + 0.4
SHADOW = t
for i in range(3): knock(t + 0.9 + i * 0.4, 0.55)
TAPS = t + 0.9
t += 2.4
shots.append(dict(start=s, end=t, name="night"))
sfx.append((t, "boom", 0.7)); shots.append(dict(start=t, end=t + 3.2, name="endcard")); t += 3.2
TOTAL = t

def shot_at(tt):
    for s_ in shots:
        if s_["start"] <= tt < s_["end"]: return s_
    return shots[-1]
def line_at(tt):
    for st, k in lines:
        if st <= tt < st + DUR[k]: return k, tt - st
    return None, 0

def load_bg(p): return Image.open(p).convert("RGB").resize((SSW, SSH), Image.LANCZOS)
BG = {"morning": ImageEnhance.Brightness(load_bg(E1 + "bg/bedroom_clean.png")).enhance(1.25),
      "lobby": load_bg(E1 + "bg/lobby_1080.png"), "door7": load_bg("bg/door7.png"),
      "night": load_bg(E1 + "bg/bedroom_clean.png")}
TINT = {"morning": (255, 240, 225), "lobby": (225, 235, 215), "door7": (190, 205, 255), "night": (165, 185, 255)}
yy, xx = np.mgrid[0:H, 0:W]
vg = 1 - 0.55 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) ** 1.2
VIG = Image.fromarray((np.clip(vg, 0.25, 1) * 255).astype(np.uint8)).convert("RGB")

def light_level(name, tt):
    if name == "lobby": return 0.95 if (int(tt * 7) % 23) != 0 else 0.55
    if name == "door7":
        f = 0.8 + 0.05 * math.sin(tt * 13)
        if DOORK <= tt < DOORK + 1.4: f *= 0.55 + 0.45 * (int(tt * 16) % 2)
        return f
    if name == "night":
        return 0.7 if tt < WIN else 0.6
    return 1.0

def actors(name, tt):
    A = []
    if name == "morning":
        A += [dict(who="shatta", x=560, y=1030, s=2.4, look=1, held="paper", arms="hold"),
              dict(who="zalata", x=900, y=1030, s=2.4, look=-1, held="notebook"),
              dict(who="tota", x=1240, y=1030, s=2.4, look=-1)]
    elif name == "lobby":
        A += [dict(who="tota", x=360, y=1030, s=2.3, look=1),
              dict(who="shatta", x=640, y=1030, s=2.3, look=-1),
              dict(who="zalata", x=920, y=1030, s=2.3, look=-1, held="notebook")]
        if tt >= KEY + 1.5: A[0]["held"] = "key"; A[0]["arms"] = "hold"
        if BONDO_IN <= tt < BONDO_OUT1 + 0.6:
            a = min(1, (tt - BONDO_IN) / 0.35)
            x = 1350 + 500 * max(0, (tt - BONDO_OUT0) / (BONDO_OUT1 - BONDO_OUT0 + 0.6))
            if tt > BONDO_OUT0: a = max(0, 1 - (tt - BONDO_OUT0) / (BONDO_OUT1 - BONDO_OUT0 + 0.6))
            A.append(dict(who="bondo2", x=x, y=1030, s=2.3, look=-1, arms="hips", alpha=a, expr="angry"))
    elif name == "door7":
        dx = 0
        if tt >= RUN: dx = -1600 * min(1, (tt - RUN) / 1.0)
        A += [dict(who="tota", x=520 + dx, y=1030, s=2.3, look=1, held="torch", arms="hold"),
              dict(who="zalata", x=800 + dx, y=1030, s=2.3, look=1, held="notebook"),
              dict(who="shatta", x=1100 + dx * 0.9, y=1030, s=2.3, look=1,
                   arms="point" if KEYJAM - 2 <= tt < DOORK + 0.8 else "down", held="key" if tt < RUN else None)]
        if tt >= RUN:
            for a in A: a["arms"] = "scared"; a["expr"] = "shock"
    elif name == "night":
        A.append(dict(who="shatta", x=960, y=1030, s=2.4, look=-1))
    return A

def jump_off(who, tt):
    for j in jumps.get(who, []):
        if 0 <= tt - j < 0.4: return math.sin((tt - j) / 0.4 * math.pi) * 60
    return 0

def draw_actors(name, tt):
    layer = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0))
    k, lt = line_at(tt); focus = None
    for a in actors(name, tt):
        who = a["who"]; talking = k is not None and WHO[k] == who
        expr = a.get("expr", "neutral")
        scare = any(0 <= tt - x < 2.0 for x in knocks + [CAT, BONDO_IN])
        if scare and who != "bondo2": expr = "scared"
        if who == "tota" and not talking and not scare: expr = "smug"
        if name == "night" and tt >= SHADOW: expr = "shock"
        if talking: expr = EXPR[k]
        mouth = float(ENV[k][min(int(lt * FPS), len(ENV[k]) - 1)]) if talking else 0.0
        arms = a.get("arms", "down")
        if talking and arms == "down": arms = "talk"
        if talking and k in ("E02", "E05", "E14"): arms = "up" if k != "E14" else "scared"
        if talking and k in ("E04", "E11", "E01"): arms = "point"
        y = a["y"] - jump_off(who, tt)
        shiver = math.sin(tt * 60) * 2.5 if expr in ("scared", "shock") else 0
        blink = ((tt + hash(who) % 7 * 0.37) % 3.6) < 0.11
        L = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(L); s = a["s"]
        p.ell(a["x"], a["y"] + 4, 46 * s, 9 * s, (0, 0, 0, 110), None)
        tt_run = tt * (3 if name == "door7" and tt >= RUN else 1)
        draw_char(p, who, a["x"] + shiver, y, s, expr, mouth, a.get("look", 0), blink, arms, tt_run, a.get("held"))
        al = a.get("alpha", 1.0)
        if al < 1: L.putalpha(L.getchannel("A").point(lambda v: int(v * al)))
        layer = Image.alpha_composite(layer, L)
        if talking: focus = (a["x"], y - 200 * s * CH[who]["scale"], s)
    return layer, focus

def tint_layer(layer, tint, lvl):
    rgb = layer.convert("RGB"); al = layer.getchannel("A")
    c = tuple(int((v * 0.55 + 255 * 0.45) * min(1.0, lvl * 1.05)) for v in tint)
    rgb = ImageChops.multiply(rgb, Image.new("RGB", rgb.size, c))
    out = rgb.convert("RGBA"); out.putalpha(al); return out

def draw_cat(img, tt):
    k = (tt - CAT) / 0.55
    if not 0 <= k < 1.0: return
    d = ImageDraw.Draw(img); S = lambda v: int(v * SS)
    x = 420 + 700 * k; y = 300 + 200 * k - 300 * math.sin(k * math.pi) * 0.6; sc = 1.0 + 3.5 * k
    d.ellipse([S(x - 50 * sc), S(y - 28 * sc), S(x + 50 * sc), S(y + 28 * sc)], fill=(15, 15, 18))
    d.ellipse([S(x + 30 * sc), S(y - 50 * sc), S(x + 80 * sc), S(y)], fill=(15, 15, 18))
    d.polygon([(S(x + 34 * sc), S(y - 40 * sc)), (S(x + 40 * sc), S(y - 70 * sc)), (S(x + 52 * sc), S(y - 46 * sc))], fill=(15, 15, 18))
    d.polygon([(S(x + 60 * sc), S(y - 46 * sc)), (S(x + 74 * sc), S(y - 70 * sc)), (S(x + 78 * sc), S(y - 40 * sc))], fill=(15, 15, 18))
    for ex in (48, 64):
        d.ellipse([S(x + ex * sc - 5 * sc), S(y - 30 * sc), S(x + ex * sc + 5 * sc), S(y - 20 * sc)], fill=(250, 220, 40))
    d.line([(S(x - 50 * sc), S(y)), (S(x - 90 * sc), S(y - 50 * sc))], fill=(15, 15, 18), width=S(8 * sc))

def draw_key_glint(img, tt):
    if not KEY + 2.0 <= tt < KEY + 4.5: return
    d = ImageDraw.Draw(img, "RGBA"); S = lambda v: int(v * SS)
    r = 22 + 10 * math.sin(tt * 12); cx, cy = 455, 760
    d.line([(S(cx - r), S(cy)), (S(cx + r), S(cy))], fill=(255, 240, 160, 230), width=S(4))
    d.line([(S(cx), S(cy - r)), (S(cx), S(cy + r))], fill=(255, 240, 160, 230), width=S(4))

def draw_torch(img, tt, name):
    if name != "door7" or tt >= RUN: return
    ov = Image.new("L", (SSW, SSH), 0); d = ImageDraw.Draw(ov); S = lambda v: int(v * SS)
    tx, ty = 600, 740; ex = 1330 + 30 * math.sin(tt * 1.7); ey = 470
    d.polygon([(S(tx), S(ty)), (S(ex - 220), S(ey - 260)), (S(ex + 220), S(ey + 260))], fill=70)
    ov = ov.filter(ImageFilter.GaussianBlur(S(30)))
    img.paste(Image.new("RGB", img.size, (210, 225, 255)), (0, 0), ov)

def draw_shadow(img, tt):
    if not SHADOW <= tt < SHADOW + 1.2: return
    k = (tt - SHADOW) / 1.2
    L = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(L); S = lambda v: int(v * SS)
    x = -80 + 420 * k
    d.ellipse([S(x - 45), S(120), S(x + 45), S(210)], fill=(5, 5, 10, 220))
    d.polygon([(S(x - 70), S(450)), (S(x - 40), S(200)), (S(x + 40), S(200)), (S(x + 70), S(450))], fill=(5, 5, 10, 220))
    img.paste(L, (0, 0), L)

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

PAPER_IMG = Image.open("/home/claude/s1e2/paper_closeup.png").convert("RGB") if os.path.exists("/home/claude/s1e2/paper_closeup.png") else None

def wrap(s, n=26):
    out = [""]
    for w_ in s.split(" "):
        if len(out[-1]) + len(w_) + 1 > n and out[-1]: out.append(w_)
        else: out[-1] = (out[-1] + " " + w_).strip()
    return out

def vertical(fr, tt):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = ImageEnhance.Brightness(small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.35)
    bgv.paste(fr.resize((1080, 608), Image.LANCZOS), (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(255, 214, 90)); d.rectangle([0, 1168, 1080, 1171], fill=(255, 214, 90))
    text(bgv, 540, 330, "سر الدور السابع", 92, (255, 214, 90), (40, 10, 10), 6)
    text(bgv, 540, 450, "الحلقة 2: المفتاح اللي مالوش باب", 50, (235, 235, 235))
    k, _ = line_at(tt)
    if k:
        for i, l in enumerate(wrap(SUB[k])[:4]): text(bgv, 540, 1300 + i * 80, l, 60, sw=6)
    if PUZ <= tt < PUZ_END:
        d.rounded_rectangle([60, 1640, 1020, 1800], 26, fill=(20, 20, 30), outline=(255, 214, 90), width=5)
        text(bgv, 540, 1695, "لغز الحلقة: سبعة وتلاتين يبقوا إيه؟", 46, (255, 214, 90))
        text(bgv, 540, 1758, "اكتب حلّك في الكومنتات", 42)
    return bgv

def render(out, mode="h", stills=None):
    cams = {}; ff = None
    OW, OH = (W, H) if mode == "h" else (1080, 1920)
    if not stills:
        ff = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{OW}x{OH}",
                               "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "19",
                               "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    times = stills or [i / FPS for i in range(int(TOTAL * FPS))]
    for tt in times:
        sh = shot_at(tt); name = sh["name"]
        if name in ("title", "endcard"):
            fr = Image.new("RGB", (W, H), (8, 8, 12)); k = min(1, (tt - sh["start"]) / 0.6)
            g = lambda c: tuple(int(v * k) for v in c)
            if name == "title":
                text(fr, W / 2, H / 2 - 70, "عمارة نعناعة", 110, g((255, 214, 90)), (40, 10, 10), 6)
                text(fr, W / 2, H / 2 + 60, "سر الدور السابع", 64, g((230, 230, 230)))
                text(fr, W / 2, H / 2 + 150, "الحلقة 2: المفتاح اللي مالوش باب", 44, g((200, 200, 200)))
            else:
                text(fr, W / 2, H / 2 - 30, "الحلقة 3 بكرة", 100, g((255, 214, 90)), (40, 10, 10), 6)
                text(fr, W / 2, H / 2 + 90, "مين اللي أخد المفتاح؟ اكتب في الكومنتات", 46, g((230, 230, 230)))
        elif name == "morning" and PAPER_IMG and INS1[0] <= tt < INS1[1]:
            fr = ImageChops.multiply(PAPER_IMG, VIG)
            if mode == "h": subtitle(fr, tt)
        elif name == "night" and CARD3[0] <= tt < CARD3[1]:
            fr = Image.new("RGB", (W, H), (6, 6, 10))
            text(fr, W / 2, H / 2, "الساعة 3 الفجر...", 80, (200, 200, 220))
        else:
            lvl = light_level(name, tt)
            bg = BG[name] if lvl > 0.99 else ImageEnhance.Brightness(BG[name]).enhance(lvl)
            img = bg.copy()
            if name == "night": draw_shadow(img, tt)
            draw_torch(img, tt, name)
            layer, focus = draw_actors(name, tt)
            layer = tint_layer(layer, TINT[name], lvl)
            img.paste(layer, (0, 0), layer)
            if name == "lobby": draw_cat(img, tt); draw_key_glint(img, tt)
            cam = cams.setdefault(name, Cam())
            if name == "lobby" and CAT - 0.2 <= tt < CAT + 1.2: cam.go(500, 450, 1.35, 0.25)
            elif name == "lobby" and PUZ <= tt < PUZ_END: cam.go(360, 640, 1.5, 0.08)
            elif name == "door7" and tt < RUN and KEYJAM - 1 <= tt < DOORK + 1.4: cam.go(1250, 560, 1.5, 0.07)
            elif name == "night" and tt >= SHADOW: cam.go(960, 1030 - 480 + 60, 2.5, 0.2)
            elif focus:
                fx, fy, s_ = focus; cam.go(fx, fy + 140, 1.18, 0.06)
            else: cam.go(W / 2, H / 2, 1.0, 0.05)
            shake = 0
            for kn in knocks + [CAT, BONDO_IN]:
                if 0 <= tt - kn < 0.25: shake = 14 * (1 - (tt - kn) / 0.25)
            fr = ImageChops.multiply(cam.crop(img, shake), VIG)
            if name == "lobby" and PUZ <= tt < PUZ_END and mode == "h":
                d = ImageDraw.Draw(fr, "RGBA")
                d.rounded_rectangle([W / 2 - 640, 60, W / 2 + 640, 200], 24, fill=(20, 20, 30, 210), outline=(255, 214, 90, 255), width=4)
                text(fr, W / 2, 130, "لغز الحلقة: سبعة وتلاتين يبقوا إيه؟ اكتب في الكومنتات", 40, (255, 214, 90))
            fade = min(1, (tt - sh["start"]) / 0.35, (sh["end"] - tt) / 0.35)
            if fade < 1: fr = Image.blend(Image.new("RGB", (W, H)), fr, max(0, fade))
            if mode == "h": subtitle(fr, tt)
        if mode == "v": fr = vertical(fr, tt)
        if stills: fr.save(f"still_{mode}_{tt:.1f}.png")
        else: ff.stdin.write(fr.tobytes())
    if ff: ff.stdin.close(); ff.wait()

def build_audio(path="mix.wav"):
    buf = np.zeros(int(TOTAL * SR) + SR, dtype=np.float32)
    mix_into(buf, drone(TOTAL + 1), 0, 0.9)
    S = {"knock": sfx_knock(), "boom": sfx_boom(), **SFXF}
    for tt, k, g in sfx: mix_into(buf, S[k], tt, g)
    for st, k in lines: mix_into(buf, AUD[k], st, 1.0)
    buf = np.clip(buf / max(1e-6, np.abs(buf).max()) * 0.95, -1, 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((buf * 32767).astype(np.int16).tobytes())

def mux(v, out):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", v, "-i", "mix.wav", "-c:v", "copy", "-af",
                    "loudnorm=I=-15:TP=-1.5", "-c:a", "aac", "-b:a", "192k", "-shortest", out], check=True)

if __name__ == "__main__":
    print("TOTAL", round(TOTAL, 1), [(s_["name"], round(s_["start"], 1)) for s_ in shots])
    if sys.argv[1:2] == ["stills"]:
        render(None, "h", [float(v) for v in sys.argv[2:]])
    else:
        build_audio()
        render("v.mp4", "v"); mux("v.mp4", "sirr_eldor_elsabe3_ep2_vertical.mp4")
        render("h.mp4", "h"); mux("h.mp4", "sirr_eldor_elsabe3_ep2.mp4")
        print("done")
