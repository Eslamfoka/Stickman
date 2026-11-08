import sys, os, math, subprocess, wave
sys.path.insert(0, "/home/claude/s1e1")
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter, ImageFont
from engine import *

os.chdir("/home/claude/s1e7")
SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(71)
E1 = "/home/claude/s1e1/"

SUB = {
 "N00": "رشدي؟...",
 "N01": "...مفيش. يلا، كل واحد على سريره، حالا!",
 "N02": "تيتا عارفة رشدي... أنا متأكد.",
 "N03": "لغز امبارح: اللي كتبوا نانا... برافو عليكو! الرسالة كانت لتيتا نعناعة.",
 "N04": "كل الأدلة هنا في الكشكول: الخبط، والسماعات، والمفتاح.",
 "N05": "هحطه على الدكة ثانية واحدة، وأربط الجزمة.",
 "N06": "صباح الفل يا حلوين! ...أيوه يا باشا، أنا في المدخل.",
 "N07": "الأرض دي مش بتنضف أبدا...",
 "N08": "يا ولاد! محدش يلعب في المدخل!",
 "N09": "الكشكول... الكشكول اتسرق!",
 "N10": "مين اللي خده؟! كلكم كنتوا هنا!",
 "N11": "أنا؟ أنا كنت بكلم الباشا في التليفون.",
 "N12": "أنا كنت بكنس.",
 "N13": "وأنا هسرق كشكول؟! يا ولد!",
 "N14": "استنوا... أنا شفت حاجة غريبة.",
 "N15": "لغز النهارده: مين الحرامي؟ ركزوا في التفاصيل... واكتبوا في الكومنتات!",
 "N16": "سامحني يا رشدي... تلاتين سنة وأنا ساكتة.",
}
WHO = {"N00": "nana", "N01": "nana", "N02": "shatta", "N03": "tota", "N04": "zalata", "N05": "zalata",
       "N06": "fahmy", "N07": "bondo2", "N08": "nana", "N09": "zalata", "N10": "shatta", "N11": "fahmy",
       "N12": "bondo2", "N13": "nana", "N14": "tota", "N15": "tota", "N16": "nana"}
EXPR = {"N00": "sad", "N01": [(0, "sad"), (0.4, "angry")], "N02": "smug", "N03": "happy", "N04": "smug",
        "N05": "neutral", "N06": "happy", "N07": "flat", "N08": "angry", "N09": "shock", "N10": "angry",
        "N11": [(0, "happy"), (0.5, "smug")], "N12": "flat", "N13": "angry", "N14": "neutral",
        "N15": [(0, "neutral"), (0.6, "smug")], "N16": "sad"}
ARMS = {"N01": "point", "N03": "point", "N04": "hold", "N05": "talk", "N06": "hold", "N08": "point",
        "N09": "up", "N10": "point", "N11": "hold", "N12": "hold", "N13": "hips", "N14": "point", "N15": "point",
        "N16": "hold"}

AUD = {k: load_audio(f"audio/{k}.mp3") for k in SUB}
ENV = {k: envelope(v) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}
SFXF = {n: load_audio(f"sfx/{n}.mp3") for n in ("whoosh", "creak", "slam", "cat", "footsteps")}

lines, sfx, shots, jumps, shakes = [], [], [], {}, []
def say(t, k): lines.append((t, k)); return t + DUR[k]
def fx(t, n, g=1.0): sfx.append((t, n, g))
def jump(w, t): jumps.setdefault(w, []).append(t)
def shot(set_, s, e, c0, c1=None, **kw):
    shots.append(dict(set=set_, start=s, end=e, c0=c0, c1=c1 or c0, **kw))
def cut(t, g=0.45): fx(t - 0.12, "whoosh", g)
KIDS = ("shatta", "zalata", "tota")

def CU(who, pos, z=2.2, dx=0):
    x, y, s = pos; S = s * CH[who]["scale"]
    if who == "tota": z *= 1.3
    hy = y - 190 * S
    return (x + dx, hy + H / (2 * z) - 1.45 * 46 * S - 25, z)

ROOF = {"tota": (480, 1040, 2.1), "shatta": (700, 1040, 2.1), "zalata": (900, 1050, 2.1), "nana": (330, 760, 1.6)}
LOB = {"zalata": (760, 1070, 2.2), "tota": (1480, 1080, 2.2), "shatta": (1700, 1080, 2.2)}
FAH_P, BON_P, NAN_P = (560, 900, 1.9), (1300, 830, 1.75), (1080, 900, 1.9)
BENCH_NB = (430, 575)

t = 0.0
# ===== 0. HOOK (roof) =====
t = say(0.15, "N00") + 0.25
shot("roof", 0, t, CU("nana", ROOF["nana"], 2.6), CU("nana", ROOF["nana"], 3.0), dark=True)
s = t; t = say(t, "N01") + 0.15
shot("roof", s, t, (600, 760, 1.25), (560, 760, 1.35))
WALK = (t, t + 2.6)
s = t; t = say(t + 0.2, "N02") + 0.3
shot("roof", s, max(t, WALK[1]), CU("shatta", (600, 900, 1.8), 2.0), CU("shatta", (430, 820, 1.6), 2.2))
t = max(t, WALK[1])
cut(t, 0.6); fx(t, "boom", 0.7); shot("title", t, t + 1.6, None); t += 1.6
# ===== 1. LOBBY morning =====
cut(t, 0.4); s = t; t += 0.15
N03_T = t; t = say(t, "N03") + 0.15
shot("lobby", s, t, CU("tota", LOB["tota"], 1.9), CU("tota", LOB["tota"], 2.2))
s = t; N04_T = t; t = say(t, "N04") + 0.1
shot("lobby", s, t, CU("zalata", LOB["zalata"], 2.0), CU("zalata", LOB["zalata"], 2.3), icons=True)
s = t; N05_T = t; t = say(t, "N05") + 0.1
PUT = N05_T + 1.0
shot("lobby", s, t, (560, 720, 1.5), (520, 700, 1.6))
ENTER = (t - 0.6, t + 2.6)
fx(ENTER[0], "creak", 0.6)
s = t; t = say(t + 0.3, "N06") + 0.1
shot("lobby", s, t, (950, 680, 1.05), (900, 690, 1.12))
s = t; t = say(t, "N07") + 0.05
shot("lobby", s, t, CU("bondo2", BON_P, 2.1), CU("bondo2", BON_P, 2.3))
s = t; t = say(t, "N08") + 0.1
shot("lobby", s, t, CU("nana", NAN_P, 2.1), CU("nana", NAN_P, 2.3))
CATWALK = (t, t + 1.6); fx(t + 0.5, "cat", 0.9)
shot("lobby", t, t + 1.6, (480, 600, 1.9), (440, 600, 2.1)); t += 1.6
# ===== blackout =====
BLACK = (t, t + 3.2); fx(t, "powercut", 1.0)
fx(t + 0.8, "steps_q", 1.0); fx(t + 1.5, "paper", 1.0); fx(t + 2.1, "cat", 0.8)
shot("lobby", t, BLACK[1], (960, 600, 1.0), blackout=True); t = BLACK[1]
LIGHTS = t; fx(t, "click", 1.0); fx(t + 0.15, "sting", 1.2)
shot("lobby", t, t + 1.2, (480, 600, 1.9), (440, 600, 2.4), ease="crash"); t += 1.2
s = t; t = say(t, "N09") + 0.05
shot("lobby", s, t, CU("zalata", LOB["zalata"], 2.2), CU("zalata", LOB["zalata"], 2.6), ease="crash")
shakes.append((s + 0.3, 8))
s = t; t = say(t, "N10") + 0.15
shot("lobby", s, t, (1300, 700, 1.1), (1200, 690, 1.2))
LINEUP = t; fx(t, "sting", 0.9); fx(t, "shutter", 1.0)
shot("lineup", t, t + 1.4, None, hl=None); t += 1.4
for who_, key in (("fahmy", "N11"), ("bondo2", "N12"), ("nana", "N13")):
    s = t; t = say(t, key) + 0.12
    shot("lineup", s, t, None, hl=who_)
s = t; fx(t + 0.1, "cat", 1.0); t += 1.1
shot("lineup", s, t, None, hl="cat")
s = t; N14_T = t; t = say(t, "N14") + 0.05
shot("lobby", s, t, CU("tota", LOB["tota"], 2.1), CU("tota", LOB["tota"], 2.4))
CLUE = (t, t + 0.55); fx(t, "whoosh", 0.8); fx(t + 0.05, "sting", 0.7)
shot("lobby", t, CLUE[1], (FAH_P[0] + 30, FAH_P[1] - 200, 4.2), (FAH_P[0] + 30, FAH_P[1] - 200, 4.6), clue=True)
t = CLUE[1]
PUZ = t; s = t; t = say(t, "N15") + 0.6; PUZ_END = t
shot("lobby", s, t, CU("tota", LOB["tota"], 2.3), CU("tota", LOB["tota"], 2.6))
# ===== 2. NIGHT: Nana alone =====
cut(t, 0.5); NIGHT = t
shot("living", t, t + 1.6, (760, 500, 1.0), (700, 520, 1.1)); t += 1.6
s = t; t = say(t + 0.3, "N16") + 0.7
shot("living", s, t, CU("nana", (620, 860, 1.8), 2.2), CU("nana", (620, 860, 1.8), 2.8), dark=True)
PHOTO = (t, t + 4.2); fx(t + 0.1, "sting", 0.8); fx(t + 2.4, "boom", 0.9)
shot("photo", t, PHOTO[1], None); t = PHOTO[1]
fx(t, "boom", 1.0); shot("black", t, t + 0.5, None); t += 0.5
shot("endcard", t, t + 3.2, None); t += 3.2
TOTAL = t

STEPS = []
def contacts(t0, t1, rate, g0=0.7, g1=0.7):
    n = math.ceil(t0 * rate / math.pi)
    while True:
        tc = n * math.pi / rate
        if tc >= t1: break
        if tc >= t0: STEPS.append((tc, g0 + (g1 - g0) * (tc - t0) / max(1e-3, t1 - t0)))
        n += 1
contacts(WALK[0], WALK[1], 7, 0.3, 0.3)
contacts(ENTER[0], ENTER[1], 7, 0.45, 0.6)
contacts(BLACK[0] + 0.8, BLACK[0] + 1.6, 14, 0.7, 0.7)

def shot_at(tt):
    for s_ in shots:
        if s_["start"] <= tt < s_["end"]: return s_
    return shots[-1]
def line_at(tt):
    for st, k in lines:
        if st <= tt < st + DUR[k]: return k, tt - st
    return None, 0
def ease(k, kind=None):
    k = min(1, max(0, k))
    if kind == "crash": return 1 - (1 - min(1, k * 3.5)) ** 3
    return k * k * (3 - 2 * k)
def lerp(a, b, k): return a + (b - a) * k

_lob = Image.open(E1 + "bg/lobby_1080.png").convert("RGB")
SRCBG = {"roof": Image.open("/home/claude/s1e6/bg/roof_raw.png").convert("RGB"),
         "lobby": ImageChops.multiply(ImageEnhance.Brightness(_lob).enhance(1.7), Image.new("RGB", _lob.size, (255, 238, 210))),
         "living": Image.open(E1 + "bg/living_1080.png").convert("RGB")}
TINT = {"roof": (175, 190, 240), "lobby": (255, 245, 230), "living": (255, 205, 150)}
yy, xx = np.mgrid[0:H, 0:W]
vg = 1 - 0.55 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) ** 1.2
VIG = Image.fromarray((np.clip(vg, 0.25, 1) * 255).astype(np.uint8)).convert("RGB")
vg2 = np.clip(1 - 0.9 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2), 0.12, 1)
VIG_DARK = Image.fromarray((vg2 * 255).astype(np.uint8)).convert("RGB")
GRAIN = [np.random.default_rng(i).normal(0, 5.0, (H // 2, W // 2)).astype(np.float32) for i in range(6)]

def cam_at(sh, tt):
    k = ease((tt - sh["start"]) / max(0.01, sh["end"] - sh["start"]), sh.get("ease"))
    cx, cy, z = [a + (b - a) * k for a, b in zip(sh["c0"], sh["c1"])]
    shake = 0
    for st, amp in shakes:
        if 0 <= tt - st < 0.4: shake = max(shake, amp * (1 - (tt - st) / 0.4))
    cw, ch = W / z, H / z
    cx += math.sin(tt * 0.9) * 6 + math.sin(tt * 2.3) * 2.5; cy += math.sin(tt * 1.3 + 1) * 4
    x0 = min(max(cx - cw / 2, 0), W - cw); y0 = min(max(cy - ch / 2, 0), H - ch)
    if shake:
        x0 = min(max(x0 + rng.normal(0, shake / z), 0), W - cw); y0 = min(max(y0 + rng.normal(0, shake / z), 0), H - ch)
    return x0, y0, z

# ---------------- actors ----------------
def actors(set_, tt):
    A = []
    if set_ == "roof":
        for who in KIDS:
            x, y, s = ROOF[who]
            a = dict(who=who, x=x, y=y, s=s, look=-1, expr="scared" if tt < WALK[0] else "neutral")
            if who == "zalata": a["held"] = "notebook"
            if tt >= WALK[0]:
                k = min(1, (tt - WALK[0]) / (WALK[1] - WALK[0]))
                a["x"] = lerp(x, x - 330, k); a["y"] = lerp(y, y - 200, k); a["s"] = lerp(s, s * 0.78, k); a["walk"] = tt * 7 + hash(who) % 3
                if who == "shatta": a["expr"] = "smug"; a["look"] = 1
            A.append(a)
        x, y, s = ROOF["nana"]
        A.append(dict(who="nana", x=x, y=y, s=s, look=1, expr="sad", arms="down" if tt < WALK[0] else "point"))
        if tt >= WALK[0] + 0.6: A[-1]["x"] = lerp(x, 200, min(1, (tt - WALK[0] - 0.6) / 1.4)); A[-1]["walk"] = tt * 6
    elif set_ == "lobby":
        for who in KIDS:
            x, y, s = LOB[who]
            a = dict(who=who, x=x, y=y, s=s, look=-1 if who != "zalata" else 0, expr="neutral")
            if who == "zalata":
                a["held"] = "nbpen" if tt < PUT else None
                if PUT <= tt < LIGHTS: a["lean"] = 1.2; a["arms"] = "down"
            if tt >= LIGHTS: a["expr"] = "shock"; a["arms"] = "scared" if who != "tota" else "down"
            if who == "tota" and tt >= N14_T: a["expr"] = "smug"; a["arms"] = "down"
            A.append(a)
        if tt >= ENTER[0]:
            k = min(1, (tt - ENTER[0]) / (ENTER[1] - ENTER[0]))
            fx_, fy_, fs_ = lerp(980, FAH_P[0], ease(k)), lerp(700, FAH_P[1], ease(k)), lerp(1.4, FAH_P[2], ease(k))
            A.append(dict(who="fahmy", x=fx_, y=fy_, s=fs_, look=-1, held="phone", arms="hold", expr="happy",
                          walk=tt * 7 if k < 1 else None, pen=tt >= LIGHTS))
            A.append(dict(who="bondo2", x=BON_P[0] + math.sin(tt * 3) * 25, y=BON_P[1], s=BON_P[2], look=-1, held="broom",
                          arms="hold", expr="flat"))
            kn = min(1, (tt - ENTER[0] - 0.8) / 2.0) if tt > ENTER[0] + 0.8 else 0
            A.append(dict(who="nana", x=lerp(1500, NAN_P[0], ease(kn)), y=lerp(700, NAN_P[1], ease(kn)), s=lerp(1.4, NAN_P[2], ease(kn)),
                          look=-1, held="basket", arms="hold", expr="angry", walk=tt * 6 if 0 < kn < 1 else None))
            if tt >= LIGHTS:
                for a in A[-3:]: a["expr"] = "shock" if a["who"] != "fahmy" else "smug"
    elif set_ == "living":
        A.append(dict(who="nana", x=620, y=860, s=1.8, look=0, held="photo", arms="hold", expr="sad"))
    return A

def jump_off(who, tt):
    for j in jumps.get(who, []):
        if 0 <= tt - j < 0.4: return math.sin((tt - j) / 0.4 * math.pi) * 50
    return 0

def expr_of(k, lt):
    e = EXPR[k]
    if isinstance(e, str): return e
    cur = e[0][1]
    for f, ex in e:
        if lt / DUR[k] >= f: cur = ex
    return cur

def head_screen(a, x0, y0, z):
    S = a["s"] * CH[a["who"]]["scale"] * z
    return (a["x"] - x0) * z, (a["y"] - y0) * z - 190 * S, S

def draw_scene_chars(set_, tt, cam, sh):
    x0, y0, z = cam
    layer = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(layer)
    k, lt = line_at(tt)
    for a in sorted(actors(set_, tt), key=lambda a: a["s"]):
        who = a["who"]; talking = k is not None and WHO[k] == who
        expr = a.get("expr", "neutral")
        if talking: expr = expr_of(k, lt)
        mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
        arms = a.get("arms", "down")
        if talking: arms = ARMS.get(k, "talk" if arms == "down" else arms)
        if a.get("held") in ("phone", "broom", "basket", "photo") : arms = "hold"
        bob = abs(math.sin(a["walk"])) * 5 * a["s"] if a.get("walk") is not None else 0
        wy = a["y"] - jump_off(who, tt) - bob
        shiver = math.sin(tt * 60) * 2.5 if expr in ("scared", "shock") and who in KIDS else 0
        blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11
        X = (a["x"] + shiver - x0) * z; Y = (wy - y0) * z; s = a["s"] * z
        p.ell(X, (a["y"] - y0) * z + 4 * s, 46 * s, 9 * s, (0, 0, 0, 110), None)
        draw_char(p, who, X, Y, s, expr, mouth, a.get("look", 0), blink, arms, tt, a.get("held"), a.get("lean", 0), a.get("walk"))
        S = s * CH[who]["scale"]
        if a.get("pen"):   # Zalata's red pen in Fahmy's breast pocket (the clue)
            px, py = X + 15 * S, Y - 122 * S
            p.line([(px, py - 9 * S), (px, py + 7 * S)], (220, 30, 30, 255), 3 * S)
            p.ell(px, py - 9 * S, 2 * S, 2 * S, (240, 240, 240, 255), None)
        if set_ == "living" and tt >= NIGHT + 2.4:   # tears
            for i in range(2):
                u = ((tt * 0.9 + i * 0.5) % 1)
                ex = X + (-15 if i == 0 else 15) * S; ey = Y - 188 * S + u * 40 * S
                p.ell(ex, ey, 2.5 * S, 4 * S, (150, 200, 255, int(220 * (1 - u))), None)
    return layer

def tint_layer(layer, tint, lvl):
    rgb = layer.convert("RGB"); al = layer.getchannel("A")
    c = tuple(int((v * 0.55 + 255 * 0.45) * min(1.0, lvl)) for v in tint)
    rgb = ImageChops.multiply(rgb, Image.new("RGB", rgb.size, c))
    out = rgb.convert("RGBA"); out.putalpha(al); return out

LW, LH = W // 8, H // 8
gy, gx = np.mgrid[0:LH, 0:LW] * 8.0
def glow(X, Y, R): return np.exp(-((gx - X) ** 2 + (gy - Y) ** 2) / (R * R))
def light_map(set_, tt, cam):
    x0, y0, z = cam; W3 = lambda px, py: ((px - x0) * z, (py - y0) * z)
    if set_ == "roof":
        m = np.full((LH, LW, 3), 0.55, np.float32) * np.array([0.8, 0.88, 1.05], np.float32)
        X, Y = W3(216, 240); m += 0.8 * glow(X, Y, 380 * z)[..., None] * np.array([1.0, 0.8, 0.5], np.float32)
    else:
        m = np.full((LH, LW, 3), 0.28, np.float32) * np.array([0.9, 0.8, 0.7], np.float32)
        fl = 0.9 + 0.1 * math.sin(tt * 13) * math.sin(tt * 5.3)
        X, Y = W3(789, 505); m += 1.3 * fl * glow(X, Y, 520 * z)[..., None] * np.array([1.0, 0.75, 0.45], np.float32)
    return Image.fromarray((np.clip(m / 1.4, 0, 1) * 255).astype(np.uint8), "RGB").resize((W, H), Image.BILINEAR)

def bg_frame(set_, cam):
    x0, y0, z = cam; src = SRCBG[set_]; sw, sh = src.size; f = sw / W
    box = (x0 * f, y0 * f, (x0 + W / z) * f, (y0 + H / z) * f)
    if z > 1.5:
        b = tuple(int(v) for v in box); b = (max(0, b[0] - 20), max(0, b[1] - 20), min(sw, b[2] + 20), min(sh, b[3] + 20))
        part = src.crop(b).filter(ImageFilter.GaussianBlur(min(4, (z - 1.4) * 1.6)))
        box = (box[0] - b[0], box[1] - b[1], box[2] - b[0], box[3] - b[1]); src = part
    return src.resize((SSW, SSH), Image.BICUBIC, box=box)

def draw_cat_shape(d, X, Y, sc, col, eyes=True):
    S = sc
    d.ellipse([X - 55 * S, Y - 30 * S, X + 55 * S, Y + 30 * S], fill=col)
    d.ellipse([X + 30 * S, Y - 58 * S, X + 86 * S, Y - 4 * S], fill=col)
    d.polygon([(X + 34 * S, Y - 44 * S), (X + 40 * S, Y - 80 * S), (X + 56 * S, Y - 50 * S)], fill=col)
    d.polygon([(X + 62 * S, Y - 50 * S), (X + 78 * S, Y - 80 * S), (X + 84 * S, Y - 44 * S)], fill=col)
    d.line([(X - 52 * S, Y - 4 * S), (X - 96 * S, Y - 52 * S)], fill=col, width=max(2, int(10 * S)))
    for lx in (-35, -12, 18, 40):
        d.line([(X + lx * S, Y + 20 * S), (X + (lx + 6) * S, Y + 52 * S)], fill=col, width=max(2, int(9 * S)))
    if eyes:
        for ex in (50, 68): d.ellipse([X + (ex - 6) * S, Y - 36 * S, X + (ex + 6) * S, Y - 24 * S], fill=(200, 230, 90))

def bench_props(img, tt, cam):
    x0, y0, z = cam; S = SS * z; d = ImageDraw.Draw(img)
    if PUT <= tt < BLACK[0] + 1.5:   # notebook on the bench
        X, Y = (BENCH_NB[0] - x0) * S, (BENCH_NB[1] - y0) * S
        d.polygon([(X - 46 * S, Y - 6 * S), (X + 40 * S, Y - 14 * S), (X + 52 * S, Y + 6 * S), (X - 34 * S, Y + 14 * S)], fill=(250, 248, 230), outline=(30, 30, 30))
        d.line([(X + 30 * S, Y - 18 * S), (X + 44 * S, Y + 2 * S)], fill=(220, 30, 30), width=max(2, int(4 * S)))
    if CATWALK[0] <= tt < CATWALK[1] + 0.5:
        k = (tt - CATWALK[0]) / (CATWALK[1] - CATWALK[0])
        cx = lerp(150, 640, min(1, k)); cy = 545 - abs(math.sin(k * 20)) * 4
        draw_cat_shape(d, (cx - x0) * S, (cy - y0) * S, 0.55 * S, (24, 24, 30))

def eyes_dark(tt, cam):
    x0, y0, z = cam
    img = Image.new("RGBA", (SSW, SSH), (3, 3, 6, 255)); p = P(img)
    u = (tt - BLACK[0]) / (BLACK[1] - BLACK[0])
    for a in actors("lobby", BLACK[0] - 0.01):
        X, hy, S = head_screen(a, x0, y0, z)
        if a["who"] == "fahmy":   # one pair of eyes sneaks to the bench and back
            k = max(0, min(1, (u - 0.25) / 0.25)) if u < 0.5 else max(0, 1 - (u - 0.6) / 0.25)
            X = lerp(X, (BENCH_NB[0] + 40 - x0) * z, ease(k)); hy = lerp(hy, (BENCH_NB[1] - 120 - y0) * z, ease(k))
        look = math.sin(tt * 7 + hash(a["who"]) % 5) * 0.8
        er = 11 * S; ey = hy + 2 * S
        blink = ((tt + (hash(a["who"]) % 7) * 0.37) % 2.1) < 0.12
        for sx in (-1, 1):
            ex = X + sx * 15 * S
            if blink: continue
            p.ell(ex, ey, er * 0.82, er, (236, 236, 236, 255), None)
            p.ell(ex + look * 4 * S, ey + 1.5 * S, 2.8 * S, 2.8 * S, (5, 5, 5, 255), None)
    cx = (430 - x0) * z; cy = (520 - y0) * z
    if 0.55 < u < 0.85:
        for ex in (-10, 10): p.ell(cx + ex * z, cy, 7 * z, 5 * z, (200, 230, 90, 255), None)
    return img.convert("RGB").resize((W, H), Image.LANCZOS)

# ---------------- cards ----------------
SUSPECTS = [("fahmy", "أستاذ فهمي"), ("bondo2", "عم بندق"), ("nana", "تيتا"), ("cat", "القطة")]
def lineup(tt, sh):
    k = (tt - LINEUP) / 0.5
    fr = Image.new("RGB", (W, H), (16, 14, 20)); d = ImageDraw.Draw(fr)
    for i in range(0, W, 60): d.line([(i, 0), (i, H)], fill=(24, 22, 30), width=2)
    text(fr, W / 2, 110, "مين الحرامي؟", 96, (255, 214, 90), (40, 10, 10), 6)
    L = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(L)
    for i, (who, name) in enumerate(SUSPECTS):
        cx = 300 + i * 440; cy = 560
        slide = min(1, max(0, k * 4 - i * 0.6))
        oy = (1 - ease(slide)) * 700
        hl = sh.get("hl") == who
        col = (255, 214, 90, 255) if hl else (90, 90, 110, 255)
        p.rect(cx - 190, cy - 300 + oy, cx + 190, cy + 250 + oy, (34, 32, 44, 255), col, 8 if hl else 4, 18)
        if who == "cat":
            dd = ImageDraw.Draw(L); draw_cat_shape(dd, (cx - 30) * SS, (cy + 40 + oy) * SS, 2.1 * SS, (20, 20, 26, 255))
        else:
            pen = who == "fahmy"
            draw_char(p, who, cx, cy + 300 + oy, {"fahmy": 2.9, "bondo2": 2.25, "nana": 2.35}[who], "smug" if who == "fahmy" else ("angry" if who == "nana" else "flat"),
                      0.0, 0, False, "down", tt, None)
            if pen:
                S = 2.9 * CH[who]["scale"]; px, py = cx + 15 * S, cy + 300 + oy - 122 * S
                p.line([(px, py - 9 * S), (px, py + 7 * S)], (220, 30, 30, 255), 3 * S)
    fr = fr.convert("RGBA"); fr.alpha_composite(L.resize((W, H), Image.LANCZOS)); fr = fr.convert("RGB")
    for i, (who, name) in enumerate(SUSPECTS):
        cx = 300 + i * 440; slide = min(1, max(0, k * 4 - i * 0.6)); oy = (1 - ease(slide)) * 700
        hl = sh.get("hl") == who
        text(fr, cx, 860 + oy, name, 52, (255, 214, 90) if hl else (220, 220, 220))
        if not hl: text(fr, cx + 140, 330 + oy, "؟", 90, (255, 80, 70), (20, 0, 0), 5)
    if sh.get("hl"):
        dk = Image.new("L", (W, H), 120); dd = ImageDraw.Draw(dk)
        i = [w for w, _ in SUSPECTS].index(sh["hl"]); cx = 300 + i * 440
        dd.rounded_rectangle([cx - 200, 270, cx + 200, 820], 20, fill=0)
        fr.paste(Image.new("RGB", (W, H), (0, 0, 0)), (0, 0), dk)
    return fr

def photo_card(tt):
    k = (tt - PHOTO[0]) / (PHOTO[1] - PHOTO[0])
    fr = Image.new("RGB", (W, H), (14, 10, 8))
    L = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(L)
    p.rect(560, 160, 1360, 920, (110, 70, 35, 255), INK, 8, 6)
    p.rect(600, 200, 1320, 880, (225, 200, 160, 255), None)
    draw_char(p, "youngnana", 830, 860, 2.6, "happy", 0, 1, False, "down", 0, None)
    draw_char(p, "roshdy", 1100, 860, 2.6, "happy", 0, -1, False, "hold", 0, "key")
    ph = L.resize((W, H), Image.LANCZOS)
    a = np.asarray(ph).astype(np.float32)
    g = a[..., :3].mean(-1, keepdims=True)
    sep = np.concatenate([g * 1.07, g * 0.9, g * 0.68], -1)
    a[..., :3] = np.clip(sep, 0, 255)
    ph = Image.fromarray(a.astype(np.uint8), "RGBA")
    fr = fr.convert("RGBA"); fr.alpha_composite(ph); fr = fr.convert("RGB")
    z = 1 + 1.4 * ease(min(1, max(0, (k - 0.45) / 0.45)))
    S = 2.6; kx, ky = 1100 + 46 * S, 860 - 104 * S - 6
    cw, ch = W / z, H / z
    x0 = lerp(0, kx - cw / 2, min(1, z - 1)); y0 = lerp(0, ky - ch / 2, min(1, z - 1))
    x0 = min(max(x0, 0), W - cw); y0 = min(max(y0, 0), H - ch)
    fr = fr.resize((W, H), Image.LANCZOS, box=(x0, y0, x0 + cw, y0 + ch))
    if k > 0.62:
        X = (kx - x0) * z; Y = (ky - y0) * z
        dd = ImageDraw.Draw(fr); r = 70 + 10 * math.sin(tt * 10)
        dd.ellipse([X - r * 1.6, Y - r, X + r * 1.6, Y + r * 1.6], outline=(255, 60, 50), width=8)
        ImageDraw.Draw(fr).text((X + 200, Y - 120), "7 - 30", font=ImageFont.truetype(FONT, 90), fill=(255, 214, 90), anchor="mm",
                                direction="ltr", stroke_width=6, stroke_fill=(40, 10, 10))
    fr = Image.fromarray((np.asarray(fr, np.float32) * (np.asarray(VIG_DARK, np.float32) / 255)).astype(np.uint8))
    return fr

def card(name, tt, sh):
    k = (tt - sh["start"]) / (sh["end"] - sh["start"])
    fr = Image.new("RGB", (W, H), (8, 8, 12))
    g = lambda c: tuple(int(v * min(1, k * 4)) for v in c)
    if name == "title":
        text(fr, W / 2, H / 2 - 80, "عمارة نعناعة", 110, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 + 50, "سر الدور السابع", 64, g((230, 230, 230)))
        text(fr, W / 2, H / 2 + 145, "الحلقة 7: الكشكول اتسرق", 48, g((210, 210, 210)))
    elif name == "endcard":
        text(fr, W / 2, H / 2 - 60, "الحلقة 8 بكرة", 104, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 + 70, "مين الحرامي؟ اكتب في الكومنتات", 48, g((230, 230, 230)))
    elif name == "lineup": return lineup(tt, sh)
    elif name == "photo": return photo_card(tt)
    return fr

def hud(fr, tt, v=False):
    sc = 0.85 if v else 1.0; cx = 540 if v else W / 2
    if N03_T + 1.4 <= tt < N03_T + DUR["N03"]:
        d = ImageDraw.Draw(fr, "RGBA"); y = 1700 if v else 120
        d.rounded_rectangle([cx - 380 * sc, y - 50 * sc, cx + 380 * sc, y + 50 * sc], int(22 * sc), fill=(20, 60, 30, 220), outline=(120, 230, 120, 255), width=4)
        text(fr, cx, y, "إجابة امبارح: NANA = نعناعة ✓", int(42 * sc), (200, 255, 200))
    if N04_T + 1.4 <= tt < N04_T + DUR["N04"] + 0.1:
        labs = ["الخبط", "السماعات", "المفتاح"]; d = ImageDraw.Draw(fr, "RGBA"); y = 1700 if v else 120
        for i, lb in enumerate(labs):
            if tt < N04_T + 1.4 + i * 0.9: continue
            x = cx + (i - 1) * 300 * sc
            d.rounded_rectangle([x - 130 * sc, y - 45 * sc, x + 130 * sc, y + 45 * sc], int(20 * sc), fill=(12, 12, 22, 220), outline=(255, 214, 90, 255), width=3)
            text(fr, x, y, lb, int(40 * sc), (255, 214, 90))

def subtitle(img, tt):
    k, _ = line_at(tt)
    if not k: return
    s = SUB[k]
    if len(s) > 44:
        sp = [i for i, ch in enumerate(s) if ch == " "]; c = min(sp, key=lambda i: abs(i - len(s) // 2))
        text(img, W / 2, H - 125, s[:c], 48, sw=5); text(img, W / 2, H - 60, s[c + 1:], 48, sw=5)
    else:
        text(img, W / 2, H - 70, s, 48, sw=5)

def wrap(s, n=24):
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
    text(bgv, 540, 300, "سر الدور السابع", 92, (255, 214, 90), (40, 10, 10), 6)
    text(bgv, 540, 420, "الحلقة 7: الكشكول اتسرق", 52, (235, 235, 235))
    k, _ = line_at(tt)
    if k:
        for i, l in enumerate(wrap(SUB[k])[:4]): text(bgv, 540, 1290 + i * 80, l, 60, sw=6)
    hud(bgv, tt, True)
    if PUZ <= tt < PUZ_END:
        d.rounded_rectangle([40, 1640, 1040, 1800], 26, fill=(20, 20, 30), outline=(255, 214, 90), width=5)
        text(bgv, 540, 1695, "لغز الحلقة: مين الحرامي؟", 52, (255, 214, 90))
        text(bgv, 540, 1758, "ركز في التفاصيل... واكتب في الكومنتات", 40)
    return bgv

def finish(fr, tt, dark=False):
    fr = ImageChops.multiply(fr, VIG_DARK if dark else VIG)
    a = np.asarray(fr, np.float32)
    g = GRAIN[int(tt * FPS) % len(GRAIN)]
    g = np.repeat(np.repeat(g, 2, 0), 2, 1)[..., None]
    return Image.fromarray(np.clip(a + g, 0, 255).astype(np.uint8))

def frame(tt):
    sh = shot_at(tt); set_ = sh["set"]
    if set_ in ("title", "endcard", "lineup", "photo"): return finish(card(set_, tt, sh), tt)
    if set_ == "black": return Image.new("RGB", (W, H), (0, 0, 0))
    cam = cam_at(sh, tt)
    if sh.get("blackout"): return finish(eyes_dark(tt, cam), tt)
    img = bg_frame(set_, cam)
    if set_ == "lobby": bench_props(img, tt, cam)
    layer = draw_scene_chars(set_, tt, cam, sh)
    layer = tint_layer(layer, TINT[set_], 1.0 if set_ == "lobby" else 0.95)
    img.paste(layer, (0, 0), layer)
    fr = img.resize((W, H), Image.LANCZOS)
    if set_ in ("roof", "living"):
        fr = ImageChops.multiply(fr, light_map(set_, tt, cam)); fr = ImageEnhance.Brightness(fr).enhance(1.6)
    if set_ == "lobby" and LIGHTS <= tt < LIGHTS + 0.5:   # lights flicker back on
        if int((tt - LIGHTS) * 20) % 3 == 0: fr = ImageEnhance.Brightness(fr).enhance(0.25)
    if sh.get("clue"):
        d = ImageDraw.Draw(fr, "RGBA")
        d.rectangle([0, 0, W, H], outline=(255, 214, 90, 200), width=16)
        fr = ImageEnhance.Contrast(fr).enhance(1.2)
    return finish(fr, tt, sh.get("dark"))

def render(out_h, out_v, stills=None):
    fh = fv = None
    if not stills:
        mk = lambda w, h, o: subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}",
                                   "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "19",
                                   "-pix_fmt", "yuv420p", o], stdin=subprocess.PIPE)
        fh = mk(W, H, out_h); fv = mk(1080, 1920, out_v)
    times = stills or [i / FPS for i in range(int(TOTAL * FPS))]
    for i, tt in enumerate(times):
        base = frame(tt)
        h = base.copy(); hud(h, tt)
        if PUZ <= tt < PUZ_END:
            d = ImageDraw.Draw(h, "RGBA")
            d.rounded_rectangle([W / 2 - 560, 60, W / 2 + 560, 175], 24, fill=(20, 20, 30, 215), outline=(255, 214, 90, 255), width=4)
            text(h, W / 2, 117, "لغز الحلقة: مين الحرامي؟ ركز في التفاصيل!", 42, (255, 214, 90))
        subtitle(h, tt)
        if stills:
            h.save(f"still_h_{tt:.1f}.png"); vertical(base, tt).save(f"still_v_{tt:.1f}.png")
        else:
            fh.stdin.write(h.tobytes()); fv.stdin.write(vertical(base, tt).tobytes())
        if i % 240 == 0: print("frame", i, flush=True)
    if fh:
        fh.stdin.close(); fv.stdin.close(); fh.wait(); fv.wait()

def build_audio(path="mix.wav"):
    buf = np.zeros(int(TOTAL * SR) + SR * 3, dtype=np.float32)
    dr = drone(TOTAL + 1); env = np.ones(len(dr), np.float32)
    for s_ in shots:
        if s_["set"] in ("lobby", "lineup") and not s_.get("blackout"):
            env[int(s_["start"] * SR):int(s_["end"] * SR)] = 0.35
    env = np.convolve(env, np.ones(4410) / 4410, mode="same")
    mix_into(buf, dr * env, 0, 1.0)
    r = np.random.default_rng(9); ts = np.arange(int(SR * 1.6)) / SR
    S = {"boom": sfx_boom(), "tick": sfx_tick() * 2.0, "powercut": sfx_powercut(), "paper": sfx_paper() * 1.3, **SFXF}
    tc = np.arange(int(SR * 0.06)) / SR
    S["click"] = r.normal(0, 1, len(tc)) * np.exp(-tc * 140) * 0.7
    S["sting"] = (np.sin(2 * np.pi * (1200 + 80 * np.sin(ts * 40)) * ts) * 0.08 + np.sin(2 * np.pi * 1263 * ts) * 0.06
                  + np.sin(2 * np.pi * 55 * ts) * 0.4) * np.exp(-ts * 1.8)
    tsh = np.arange(int(SR * 0.25)) / SR
    S["shutter"] = (r.normal(0, 1, len(tsh)) * (np.exp(-tsh * 60) + 0.6 * np.exp(-np.maximum(0, tsh - 0.08) * 70) * (tsh > 0.08))) * 0.5
    for t0, n, g in sfx:
        if n in S: mix_into(buf, S[n], t0, g)
    tsx = np.arange(int(SR * 0.25)) / SR
    for st, g in STEPS:
        nz = np.convolve(r.normal(0, 1, len(tsx)), np.ones(12) / 12, mode="same")
        mix_into(buf, (np.sin(2 * np.pi * 85 * tsx) * np.exp(-tsx * 32) * 0.9 + nz * np.exp(-tsx * 26) * 0.9) * 0.6, st, g)
    for st, k in lines: mix_into(buf, AUD[k], st, 1.0)
    buf = buf[:int(TOTAL * SR)]
    buf = np.clip(buf / max(1e-6, np.abs(buf).max()) * 0.95, -1, 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((buf * 32767).astype(np.int16).tobytes())

def mux(v, out):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", v, "-i", "mix.wav", "-c:v", "copy", "-af",
                    "loudnorm=I=-15:TP=-1.5", "-c:a", "aac", "-b:a", "192k", "-shortest", out], check=True)

if __name__ == "__main__":
    print("TOTAL", round(TOTAL, 1))
    if sys.argv[1:2] == ["stills"]:
        render(None, None, [float(v) for v in sys.argv[2:]])
    else:
        build_audio()
        render("h.mp4", "v.mp4")
        mux("h.mp4", "sirr_eldor_elsabe3_ep7.mp4"); mux("v.mp4", "sirr_eldor_elsabe3_ep7_vertical.mp4")
        print("done")
