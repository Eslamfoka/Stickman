import sys, os, math, subprocess, wave
sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter
from engine import *

os.chdir(ROOT + "/s1e4")
SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(41)
E1 = ROOT + "/s1e1/"

SUB = {
 "J00": "أنا شايفكم.",
 "J01": "الساعة اتناشر يا ولاد... مكانكم في السرير.",
 "J02": "واللي بيخبط... مش أنا لوحدي.",
 "J03": "لغز امبارح: الخبط ده شفرة مورس، يعني رسالة بالخبط! ومعناها إشارة استغاثة... SOS!",
 "J04": "يعني البواب بيستنجد بحد فوق؟",
 "J05": "أو حد فوق هو اللي بيستنجد بيه. أنا حاسبها بالقلم... خمسين في المية.",
 "J06": "الليلة هنطلع لحد الباب. ثقوا فيا المرة دي!",
 "J07": "النور قطع!",
 "J08": "ولعوا الكشاف بسرعة!",
 "J09": "شفتوا الضل اللي عدى على الحيطة؟",
 "J10": "كان طويل... طويل أوي!",
 "J11": "لأ، استنوا... الكشاف كان تحت. والنور لما بييجي من تحت، بيخلي الضل أطول من صاحبه.",
 "J12": "لغز النهارده: صاحب الضل ده كان طويل، ولا قصير؟ اكتبوا في الكومنتات!",
 "J13": "الكشاف فصل... أنا كنت حاسبها.",
 "J14": "شطة... يا شطة...",
 "J15": "إنتو سامعين؟... حد بينادي عليا باسمي!",
 "J16": "شطة... تعالى.",
}
WHO = {"J00": "bondo2", "J01": "bondo2", "J02": "bondo2", "J03": "tota", "J04": "shatta", "J05": "zalata",
       "J06": "shatta", "J07": "shatta", "J08": "tota", "J09": "zalata", "J10": "shatta", "J11": "tota",
       "J12": "tota", "J13": "zalata", "J14": "ghost", "J15": "shatta", "J16": "ghost"}
EXPR = {"J00": "angry", "J01": "angry", "J02": "sad", "J03": "happy", "J04": "neutral",
        "J05": [(0, "flat"), (0.65, "smug")], "J06": "angry", "J07": "shock", "J08": "scared", "J09": "scared",
        "J10": "shock", "J11": [(0, "neutral"), (0.5, "smug")], "J12": [(0, "neutral"), (0.6, "smug")],
        "J13": "flat", "J14": "neutral", "J15": "scared", "J16": "neutral"}
ARMS = {"J01": "point", "J03": "point", "J04": "talk", "J05": "talk", "J06": "hips", "J07": "up",
        "J09": "point", "J10": "up", "J11": "hold", "J12": "hold"}

AUD = {k: load_audio(f"audio/{k}.mp3") for k in SUB}
ENV = {k: envelope(v) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}
SFXF = {n: load_audio(f"sfx/{n}.mp3") for n in ("whoosh", "creak", "bulb", "slam")}

lines, sfx, shots, jumps, shakes = [], [], [], {}, []
def say(t, k): lines.append((t, k)); return t + DUR[k]
def fx(t, n, g=1.0): sfx.append((t, n, g))
def jump(w, t): jumps.setdefault(w, []).append(t)
def shot(set_, s, e, c0, c1=None, **kw):
    shots.append(dict(set=set_, start=s, end=e, c0=c0, c1=c1 or c0, **kw))
def cut(t, g=0.45): fx(t - 0.12, "whoosh", g)
KIDS = ("shatta", "zalata", "tota")

POS = {
 "bedroom": {"shatta": (620, 1030, 2.4), "zalata": (960, 1030, 2.4), "tota": (1300, 1030, 2.4)},
 "door7": {"tota": (240, 1030, 1.9), "shatta": (410, 1030, 1.9), "zalata": (585, 1030, 1.9)},
 "stairs": {"tota": (830, 1060, 2.0), "shatta": (1060, 1040, 2.0), "zalata": (1290, 1060, 2.0)},
}
def CU(set_, who, z=2.2, dx=0):
    x, y, s = POS[set_][who]; S = s * CH[who]["scale"]
    if who == "tota": z *= 1.3
    hy = y - 190 * S
    return (x + dx, hy + H / (2 * z) - 1.45 * 46 * S - 25, z)

t = 0.0
# ===== 0. HOOK (door 7) =====
t = 0.1; t = say(t, "J00") + 0.2
shot("door7", 0, t, (960, 540, 1.04), (960, 520, 1.15), dark=True)
BACK = t; fx(t, "sting", 0.5)
t = say(t + 0.1, "J01") + 0.15
shot("door7", BACK, t, (820, 620, 1.25), (840, 610, 1.35))
LEAVE0 = t
t = say(t, "J02") + 0.1
shot("door7", LEAVE0, t, (960, 560, 1.0), (1000, 560, 1.06))
DOORLIGHT = t; fx(t, "sting", 1.0); fx(t + 0.1, "knock", 0.5); fx(t + 0.45, "knock", 0.5)
for w_ in KIDS: jump(w_, t + 0.15)
shot("door7", t, t + 1.8, (1150, 640, 1.2), (1330, 720, 1.9)); t += 1.8
cut(t, 0.6); fx(t, "boom", 0.7); shot("title", t, t + 1.7, None); t += 1.7
# ===== 1. MORNING =====
cut(t, 0.4); s = t; t += 0.2
J03_T = t; t = say(t, "J03") + 0.15
shot("bedroom", s, t, CU("bedroom", "tota", 1.9), CU("bedroom", "tota", 2.25))
SOS = (J03_T + 1.0, t)
s = t; t = say(t, "J04") + 0.1
shot("bedroom", s, t, CU("bedroom", "shatta", 2.0), CU("bedroom", "shatta", 2.3))
s = t; t = say(t, "J05") + 0.25
shot("bedroom", s, t, (800, 560, 1.45), (820, 545, 1.62))
# ===== card =====
cut(t, 0.5); CLOCK = t; shot("card_clock", t, t + 1.4, None)
for i in range(3): fx(t + 0.2 + i * 0.4, "tick", 1.0)
t += 1.4
# ===== 2. STAIRS =====
CLIMB = (t, t + 1.9)
shot("stairs", t, t + 1.9, (1060, 640, 1.05), (1060, 660, 1.15))
t += 1.9
CREAK = t; fx(t, "creak", 1.2)
shot("stairs", t, t + 1.3, CU("stairs", "shatta", 2.0), CU("stairs", "shatta", 2.6), ease="crash"); t += 1.3
s = t; t = say(t, "J06") + 0.15
shot("stairs", s, t, (1060, 620, 1.3), (1060, 600, 1.4))
HK = [t + 0.2 + i * 0.5 for i in range(3)]
for k_ in HK: fx(k_, "hknock", 1.0); shakes.append((k_, 16))
for w_ in KIDS: jump(w_, HK[0] + 0.05)
BULB0 = HK[-1] + 0.5; fx(BULB0, "bulb", 1.4)
POP = BULB0 + 0.75
shot("stairs", t, POP + 0.35, (760, 560, 1.15), (700, 470, 1.35), dust=True)
t = POP + 0.35
BLACK0 = t
t += 0.2; t = say(t, "J07") + 0.1
t = say(t, "J08") + 0.15
shot("stairs", BLACK0, t, (1060, 600, 1.1), blackout=True)
TORCH_ON = t; fx(t, "click", 1.0)
SHADOW = (t + 0.55, t + 2.15); fx(SHADOW[0] - 0.1, "sting", 1.0); fx(SHADOW[0], "whoosh", 0.9)
SLAM = SHADOW[1] + 0.15; fx(SLAM, "slam", 1.3); shakes.append((SLAM, 12))
for w_ in KIDS: jump(w_, SHADOW[0] + 0.3); jump(w_, SLAM + 0.05)
shot("stairs", t, SLAM + 1.2, (720, 520, 1.15), (640, 480, 1.3), torch=True)
t = SLAM + 1.2; s = t
t = say(t, "J09") + 0.1
shot("stairs", s, t, CU("stairs", "zalata", 2.2), CU("stairs", "zalata", 2.35), torch=True)
s = t; t = say(t, "J10") + 0.15
shot("stairs", s, t, CU("stairs", "shatta", 1.8), CU("stairs", "shatta", 2.5), torch=True, ease="crash")
s = t; J11_T = t; t = say(t, "J11") + 0.2
shot("stairs", s, t, CU("stairs", "tota", 2.1), CU("stairs", "tota", 2.3), torch=True, under=True)
DIAG = (J11_T + DUR["J11"] * 0.35, t)
PUZ = t; s = t; t = say(t, "J12") + 0.8; PUZ_END = t
shot("stairs", s, t, CU("stairs", "tota", 2.3), CU("stairs", "tota", 2.6), torch=True, under=True)
FLICK = (t, t + 1.0); fx(t, "flicker", 1.0)
shot("stairs", t, t + 1.0, (1060, 620, 1.12), (1060, 620, 1.18), torch=True); t += 1.0
DARK2 = t; fx(t, "click", 0.7)
t += 0.35; t = say(t, "J13") + 0.5
GH1 = t; t = say(t, "J14") - 0.7
t += 0.15; J15_T = t; t = say(t, "J15") + 0.3
GH2 = t; t = say(t, "J16") - 1.0
EYES5 = t; fx(t, "sting", 1.1)
t += 1.1
shot("stairs", DARK2, GH1, (1060, 600, 1.1), (1060, 600, 1.2), blackout=True)
shot("stairs", GH1, J15_T, (1060, 600, 1.25), (1080, 580, 1.5), blackout=True)
shot("stairs", J15_T, EYES5, CU("stairs", "shatta", 2.0), CU("stairs", "shatta", 2.4), blackout=True)
shot("stairs", EYES5, t, CU("stairs", "shatta", 2.4), (1000, 600, 2.1), blackout=True)
fx(t, "boom", 1.0); shot("black", t, t + 0.5, None); t += 0.5
shot("endcard", t, t + 3.2, None); t += 3.2
TOTAL = t

STEPS = []
def contacts(t0, t1, rate, g0=0.7, g1=0.7, jingle=True):
    n = math.ceil(t0 * rate / math.pi)
    while True:
        tc = n * math.pi / rate
        if tc >= t1: break
        if tc >= t0: STEPS.append((tc, g0 + (g1 - g0) * (tc - t0) / max(1e-3, t1 - t0), jingle))
        n += 1
contacts(LEAVE0, DOORLIGHT, 7, 0.8, 0.35)
contacts(CLIMB[0], CLIMB[1], 8, 0.25, 0.25, False)

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

# ---------------- backgrounds ----------------
_bed = Image.open(E1 + "bg/bedroom_clean.png").convert("RGB")
SRCBG = {"bedroom": ImageChops.multiply(ImageEnhance.Brightness(_bed).enhance(1.55), Image.new("RGB", _bed.size, (255, 236, 205))),
         "stairs": Image.open(E1 + "bg/stairs_1080.png").convert("RGB"),
         "door7": Image.open(ROOT + "/s1e2/bg/door7.png").convert("RGB")}
def _lamp_off(img):
    sw, sh_ = img.size; f = sw / W
    Y, X = np.mgrid[0:sh_, 0:sw]
    g = np.exp(-(((X - 471 * f) / (230 * f)) ** 2 + ((Y - 260 * f) / (300 * f)) ** 2))
    g2 = np.exp(-(((X - 471 * f) / (40 * f)) ** 2 + ((Y - 201 * f) / (40 * f)) ** 2))
    a = np.asarray(img, np.float32) * (1 - 0.55 * g - 0.4 * g2)[..., None] * 0.8
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
SRCBG["stairs_off"] = _lamp_off(SRCBG["stairs"])
TINT = {"bedroom": (255, 240, 225), "stairs": (175, 185, 235), "door7": (175, 190, 255)}
yy, xx = np.mgrid[0:H, 0:W]
vg = 1 - 0.55 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) ** 1.2
VIG = Image.fromarray((np.clip(vg, 0.25, 1) * 255).astype(np.uint8)).convert("RGB")
vg2 = np.clip(1 - 0.9 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2), 0.12, 1)
VIG_DARK = Image.fromarray((vg2 * 255).astype(np.uint8)).convert("RGB")
GRAIN = [np.random.default_rng(i).normal(0, 5.5, (H // 2, W // 2)).astype(np.float32) for i in range(6)]

def cam_at(sh, tt):
    k = ease((tt - sh["start"]) / max(0.01, sh["end"] - sh["start"]), sh.get("ease"))
    c = [a + (b - a) * k for a, b in zip(sh["c0"], sh["c1"])]
    shake = 0
    for st, amp in shakes:
        if 0 <= tt - st < 0.4: shake = max(shake, amp * (1 - (tt - st) / 0.4))
    cx, cy, z = c; cw, ch = W / z, H / z
    if sh["set"] != "bedroom":   # handheld feel
        cx += math.sin(tt * 0.9) * 6 + math.sin(tt * 2.3) * 2.5; cy += math.sin(tt * 1.3 + 1) * 4
    x0 = min(max(cx - cw / 2, 0), W - cw); y0 = min(max(cy - ch / 2, 0), H - ch)
    if shake:
        x0 = min(max(x0 + rng.normal(0, shake / z), 0), W - cw); y0 = min(max(y0 + rng.normal(0, shake / z), 0), H - ch)
    return x0, y0, z

# ---------------- actors ----------------
def bondo_state(set_, tt):
    if set_ != "door7": return None
    if tt < BACK: return dict(x=980, y=2050, s=8.5, look=0, expr="angry")
    if tt < LEAVE0: return dict(x=1100, y=1010, s=2.2, look=-1, expr="angry")
    k = min(1, (tt - LEAVE0) / (DOORLIGHT - LEAVE0 + 0.3))
    if k >= 1: return None
    return dict(x=lerp(1100, 2150, ease(k) * 0.6 + k * 0.4), y=1010, s=2.2, look=1, walk=tt * 7, expr="sad")

def kid_expr(set_, who, tt):
    if set_ == "bedroom": return "smug" if who == "tota" else "neutral"
    if set_ == "door7": return "shock" if tt >= DOORLIGHT else "scared"
    if set_ == "stairs":
        if tt < CREAK: return "neutral" if who != "shatta" else "angry"
        if tt < HK[0]: return "scared" if tt < CREAK + 1.3 else "neutral"
        return "scared" if tt < SLAM else "shock" if tt < SLAM + 1.0 else "scared"
    return "neutral"

def actors(set_, tt):
    A = []
    if set_ in POS:
        for who, (x, y, s) in POS[set_].items():
            a = dict(who=who, x=x, y=y, s=s, look=0, expr=kid_expr(set_, who, tt))
            if set_ == "bedroom":
                a["look"] = {"shatta": 1, "zalata": 0, "tota": -1}[who]
                if who == "zalata": a["held"] = "notebook"
            if set_ == "door7":
                a["look"] = 1; a["arms"] = "scared" if tt >= DOORLIGHT else "down"
            if set_ == "stairs":
                a["look"] = 0
                if tt < CLIMB[1]:
                    k = (tt - CLIMB[0]) / (CLIMB[1] - CLIMB[0]); a["y"] = y + 170 * (1 - k); a["s"] = s * (1.08 - 0.08 * k)
                    a["walk"] = tt * 8 + hash(who) % 3
                if who == "tota" and tt >= TORCH_ON: a["held"] = "torch"; a["arms"] = "hold"
                if tt >= HK[0] and who != "tota": a["arms"] = "scared"
                if CREAK <= tt < CREAK + 1.3: a["arms"] = "scared"
            A.append(a)
    b = bondo_state(set_, tt)
    if b: b["who"] = "bondo2"; b.setdefault("held", "lantern"); b.setdefault("arms", "hold"); A.append(b)
    return A

def jump_off(who, tt):
    for j in jumps.get(who, []):
        if 0 <= tt - j < 0.4: return math.sin((tt - j) / 0.4 * math.pi) * 55
    return 0

def expr_of(k, lt):
    e = EXPR[k]
    if isinstance(e, str): return e
    cur = e[0][1]
    for f, ex in e:
        if lt / DUR[k] >= f: cur = ex
    return cur

def head_screen(a, x0, y0, z, tt):
    S = a["s"] * CH[a["who"]]["scale"] * z
    X = (a["x"] - x0) * z; Y = (a["y"] - jump_off(a["who"], tt) - y0) * z
    return X, Y - 190 * S, S

def draw_scene_chars(set_, tt, cam):
    x0, y0, z = cam
    layer = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(layer)
    lights = []
    k, lt = line_at(tt)
    for a in sorted(actors(set_, tt), key=lambda a: a["s"]):
        who = a["who"]; talking = k is not None and WHO[k] == who
        expr = a.get("expr", "neutral")
        if talking: expr = expr_of(k, lt)
        mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
        arms = a.get("arms", "down")
        if talking: arms = ARMS.get(k, "talk" if arms == "down" else arms)
        if talking and a.get("held") == "torch": arms = "hold"
        bob = abs(math.sin(a["walk"])) * 5 * a["s"] if a.get("walk") is not None else 0
        wy = a["y"] - jump_off(who, tt) - bob
        shiver = math.sin(tt * 60) * 2.5 if expr in ("scared", "shock") and who != "bondo2" else 0
        blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11
        X = (a["x"] + shiver - x0) * z; Y = (wy - y0) * z; s = a["s"] * z
        p.ell(X, (a["y"] - y0) * z + 4 * s, 46 * s, 9 * s, (0, 0, 0, 110), None)
        draw_char(p, who, X, Y, s, expr, mouth, a.get("look", 0), blink, arms, tt, a.get("held"),
                  a.get("lean", 0), a.get("walk"))
        if who == "bondo2":
            S = s
            lights.append((X + 46 * S, Y - 75 * S, 430 * z * a["s"] / 2.2, 0.95, (1.0, 0.75, 0.45)))
        if who == "tota" and a.get("held") == "torch":
            S = s * CH[who]["scale"]
            lights.append(("hand", X + 46 * S, Y - 104 * S))
    return layer, lights

def tint_layer(layer, tint, lvl):
    rgb = layer.convert("RGB"); al = layer.getchannel("A")
    c = tuple(int((v * 0.55 + 255 * 0.45) * min(1.0, lvl)) for v in tint)
    rgb = ImageChops.multiply(rgb, Image.new("RGB", rgb.size, c))
    out = rgb.convert("RGBA"); out.putalpha(al); return out

LW, LH = W // 8, H // 8
gy, gx = np.mgrid[0:LH, 0:LW] * 8.0
def glow(X, Y, R): return np.exp(-((gx - X) ** 2 + (gy - Y) ** 2) / (R * R))

def torch_target(sh, tt, cam, hand):
    x0, y0, z = cam
    if sh.get("under"):   # held under chin, pointing up at her face
        hx, hy = hand; return hx - 40 * z, hy - 260 * z, 300 * z
    wob = math.sin(tt * 2.1) * 30
    if TORCH_ON <= tt < TORCH_ON + 0.5:   # sweep up to wall
        k = (tt - TORCH_ON) / 0.5; wx, wy = lerp(900, 420, ease(k)), lerp(900, 430, ease(k))
    else: wx, wy = 420 + wob, 430 + wob * 0.5
    return (wx - x0) * z, (wy - y0) * z, 330 * z

def shadow_mask(tt, cam, full=False):
    if not SHADOW[0] <= tt < SHADOW[1]: return None
    x0, y0, z = cam; k = (tt - SHADOW[0]) / (SHADOW[1] - SHADOW[0])
    wx = lerp(1050, -150, k); q = 1 if full else 8
    L = Image.new("L", (W // q, H // q), 0); d = ImageDraw.Draw(L)
    f = lambda px, py: (((px - x0) * z) / q, ((py - y0) * z) / q)
    hx, hy = f(wx, 210); r = 42 * z / q
    d.ellipse([hx - r, hy - r * 1.25, hx + r, hy + r * 1.25], fill=255)
    d.polygon([f(wx - 20, 255), f(wx + 20, 255), f(wx + 26, 290), f(wx - 26, 290)], fill=255)
    d.polygon([f(wx - 58, 290), f(wx + 58, 290), f(wx + 80, 1000), f(wx - 80, 1000)], fill=255)
    d.polygon([f(wx - 52, 300), f(wx - 170, 560), f(wx - 145, 580), f(wx - 40, 360)], fill=255)
    d.polygon([f(wx + 52, 300), f(wx + 150, 520), f(wx + 128, 540), f(wx + 40, 360)], fill=255)
    if full: return L.filter(ImageFilter.GaussianBlur(3))
    return np.asarray(L, np.float32) / 255

def light_map(set_, sh, tt, cam, lights):
    x0, y0, z = cam
    W3 = lambda px, py: ((px - x0) * z, (py - y0) * z)
    m = np.zeros((LH, LW, 3), np.float32)
    amb = {"stairs": 0.42, "door7": 0.5}[set_]
    col_amb = np.array([0.85, 0.9, 1.0], np.float32)
    torch = sh.get("torch")
    fixed = []
    if set_ == "door7":
        fixed = [(150, 860, 520, 0.45, (0.8, 0.9, 1.0))]
        if tt < BACK: fixed.append((980, 1000, 520, 0.6, (1.0, 0.75, 0.45)))
        if tt >= DOORLIGHT:
            fl = 0.75 + 0.25 * math.sin(tt * 31) * math.sin(tt * 7)
            fixed.append((1330, 800, 260, 1.1 * fl, (1.0, 0.8, 0.5)))
    if set_ == "stairs":
        if torch: amb = 0.16
        else:
            lamp = 0.5
            if tt >= BULB0 and tt < POP: lamp *= 0.3 + 0.7 * (int(tt * 30) % 3 != 0) * (0.6 + 0.4 * math.sin(tt * 90))
            if tt >= POP: lamp = 0
            if HK[0] <= tt < BULB0: lamp *= 0.75 + 0.25 * math.sin(tt * 40)
            fixed = [(471, 201, 380, lamp, (1.0, 0.85, 0.6)), (1050, 120, 420, 0.3, (0.8, 0.9, 1.0))]
            if POP <= tt < POP + 0.12: amb = 1.2
    m += amb * col_amb
    for wx, wy, r, inten, col in fixed:
        X, Y = W3(wx, wy); m += inten * glow(X, Y, r * z)[..., None] * np.array(col, np.float32)
    hand = None
    for L in lights:
        if L[0] == "hand": hand = (L[1] / 1.0, L[2] / 1.0); continue
        X, Y, R, inten, col = L
        fl = 0.92 + 0.08 * math.sin(tt * 23) * math.sin(tt * 7)
        m += inten * fl * glow(X, Y, R)[..., None] * np.array(col, np.float32)
    spot = None
    if torch and hand:
        on = 1.0
        if FLICK[0] <= tt < FLICK[1]: on = 1.0 if (int(tt * 17) % 3) else 0.15
        tx, ty, R = torch_target(sh, tt, cam, hand)
        spot = glow(tx, ty, R) * on
        m += 2.3 * spot[..., None] * np.array([1.0, 0.97, 0.85], np.float32)
        m += 0.35 * on * glow(hand[0], hand[1], 260 * z)[..., None] * np.array([1.0, 0.95, 0.85], np.float32)
    mm = np.clip(m / 1.5, 0, 1)
    return Image.fromarray((mm * 255).astype(np.uint8), "RGB").resize((W, H), Image.BILINEAR), spot, hand

DUST = rng.uniform(-1, 1, (40, 3))
def draw_particles(fr, sh, tt, cam):
    d = ImageDraw.Draw(fr, "RGBA"); x0, y0, z = cam
    if sh.get("dust"):   # ceiling dust after heavy knocks
        for k_ in HK:
            u = tt - k_
            if 0 <= u < 1.6:
                for i, (a, b, c) in enumerate(DUST):
                    px = (a * 0.5 + 0.5) * W + math.sin(u * 3 + i) * 8; py = -20 + (b * 0.5 + 0.5) * 80 + u * (260 + c * 90) + 0.5 * 300 * u * u
                    r = 1.5 + abs(c) * 2.5
                    d.ellipse([px - r, py - r, px + r, py + r], fill=(205, 195, 175, int(200 * (1 - u / 1.6))))
    if sh["set"] == "stairs" and POP <= tt < POP + 0.7:   # bulb sparks
        u = tt - POP; lx, ly = (471 - x0) * z, (201 - y0) * z
        for i, (a, b, c) in enumerate(DUST[:26]):
            px = lx + a * 260 * u * z; py = ly + (b * 120 - 60) * u * z + 900 * u * u
            r = 2 + abs(c) * 2
            d.ellipse([px - r, py - r, px + r, py + r], fill=(255, 200 + int(40 * c), 90, int(255 * (1 - u / 0.7))))

def draw_beam(fr, sh, tt, cam, hand):
    if not hand: return
    if FLICK[0] <= tt < FLICK[1] and not (int(tt * 17) % 3): return
    tx, ty, R = torch_target(sh, tt, cam, hand)
    ov = Image.new("L", (W // 2, H // 2), 0); d = ImageDraw.Draw(ov)
    hx, hy = hand[0] / 2, hand[1] / 2; ang = math.atan2(ty - hand[1], tx - hand[0]); w_ = R * 0.6 / 2
    px, py = -math.sin(ang) * w_, math.cos(ang) * w_
    d.polygon([(hx, hy), (tx / 2 + px, ty / 2 + py), (tx / 2 - px, ty / 2 - py)], fill=46)
    ov = ov.filter(ImageFilter.GaussianBlur(14)).resize((W, H), Image.BILINEAR)
    fr.paste(Image.new("RGB", (W, H), (255, 248, 220)), (0, 0), ov)
    dd = ImageDraw.Draw(fr, "RGBA")
    for i, (a, b, c) in enumerate(DUST):   # motes floating in the beam
        u = (a * 0.5 + 0.5 + tt * 0.03 * (1 + c)) % 1
        qx = hand[0] + (tx - hand[0]) * u + px * 2 * b * u; qy = hand[1] + (ty - hand[1]) * u + py * 2 * b * u
        r = 1.2 + abs(c) * 1.8
        dd.ellipse([qx - r, qy - r, qx + r, qy + r], fill=(255, 245, 210, int(110 * u)))

def draw_doorlight(fr, tt, cam):
    if tt < DOORLIGHT: return
    x0, y0, z = cam; d = ImageDraw.Draw(fr, "RGBA")
    fl = 0.7 + 0.3 * math.sin(tt * 31) * math.sin(tt * 7)
    a_ = int(255 * min(1, (tt - DOORLIGHT) / 0.15) * fl)
    X0, X1 = (1185 - x0) * z, (1480 - x0) * z; Y = (785 - y0) * z
    d.polygon([(X0, Y - 4 * z), (X1, Y - 4 * z), (X1 + 120 * z, Y + 60 * z), (X0 - 120 * z, Y + 60 * z)], fill=(255, 210, 120, a_ // 5))
    d.rectangle([X0, Y - 6 * z, X1, Y], fill=(255, 225, 150, a_))

def bg_frame(set_, cam):
    x0, y0, z = cam; src = SRCBG[set_ + ("_off" if set_ == "stairs" and CUR_T[0] >= POP else "")]; sw, sh = src.size; f = sw / W
    box = (x0 * f, y0 * f, (x0 + W / z) * f, (y0 + H / z) * f)
    if z > 1.5:
        b = tuple(int(v) for v in box); b = (max(0, b[0] - 20), max(0, b[1] - 20), min(sw, b[2] + 20), min(sh, b[3] + 20))
        part = src.crop(b).filter(ImageFilter.GaussianBlur((z - 1.4) * 2.2))
        box = (box[0] - b[0], box[1] - b[1], box[2] - b[0], box[3] - b[1]); src = part
    return src.resize((SSW, SSH), Image.BICUBIC, box=box)

# ---------------- eyes in the dark ----------------
def eyes_only(sh, tt, cam):
    x0, y0, z = cam
    img = Image.new("RGBA", (SSW, SSH), (3, 3, 6, 255)); p = P(img)
    k, lt = line_at(tt)
    look_r = tt >= GH1
    for a in actors("stairs", tt):
        X, hy, S = head_screen(a, x0, y0, z, tt)
        who = a["who"]
        dart = math.sin(tt * 3 + hash(who) % 5) * (0.8 if tt < TORCH_ON else 0.3)
        look = 1.0 if look_r else dart
        if who == "shatta" and tt >= EYES5: look = 1.0
        blink = ((tt + (hash(who) % 7) * 0.37) % 3.1) < 0.12
        flat = who == "zalata" and k == "J13"
        big = tt >= GH1 or (k in ("J07", "J08"))
        er = (12 if big else 9) * S; ey = hy + 2 * S
        for sx in (-1, 1):
            ex = X + sx * 15 * S
            if blink:
                p.arc(ex, ey, 8 * S, 5 * S, 0, 180, (230, 230, 230, 255), 3 * S); continue
            p.ell(ex, ey, er * 0.82, er, (238, 238, 238, 255), None)
            pr = (2.6 if big else 4.2) * S
            p.ell(ex + look * 4 * S, ey + 1.5 * S, pr, pr, (5, 5, 5, 255), None)
            if flat:
                p.rect(ex - er, ey - er - 2, ex + er, ey, (3, 3, 6, 255), None)
                p.line([(ex - er * 0.85, ey), (ex + er * 0.85, ey)], (200, 200, 200, 255), 2.5 * S)
    if tt >= EYES5:   # a fifth pair opens behind Shatta
        u = min(1, (tt - EYES5) / 0.35)
        X, hy, S = head_screen(dict(who="shatta", x=935, y=930, s=2.0), x0, y0, z, tt)
        for sx in (-1, 1):
            ex = X + sx * 20 * S; ey = hy
            p.ell(ex, ey, 13 * S, 9 * S * u + 0.5, (200, 230, 90, 255), None)
            p.ell(ex, ey, 2.5 * S, 8 * S * u + 0.5, (10, 10, 5, 255), None)
    fr = img.convert("RGB").resize((W, H), Image.LANCZOS)
    if tt >= EYES5:
        X, hy, S = head_screen(dict(who="shatta", x=935, y=930, s=2.0), x0, y0, z, tt)
        g = Image.new("L", (W, H), 0); ImageDraw.Draw(g).ellipse([X - 90, hy - 40, X + 90, hy + 40], fill=90)
        fr.paste(Image.new("RGB", (W, H), (150, 200, 60)), (0, 0), g.filter(ImageFilter.GaussianBlur(30)))
    return fr

# ---------------- cards / HUD ----------------
def card(name, tt, sh):
    k = (tt - sh["start"]) / (sh["end"] - sh["start"])
    fr = Image.new("RGB", (W, H), (8, 8, 12))
    g = lambda c: tuple(int(v * min(1, k * 4)) for v in c)
    if name == "card_clock":
        fr = Image.new("RGB", (W, H), (8, 10, 22)); L = Image.new("RGBA", (SSW, SSH)); p = P(L)
        cx, cy, r = 960, 450, 230
        p.ell(cx, cy, r, r, (240, 236, 220, 255), INK, 8)
        for i in range(12):
            a = i / 12 * 2 * math.pi
            p.line([(cx + math.sin(a) * r * 0.82, cy - math.cos(a) * r * 0.82), (cx + math.sin(a) * r * 0.92, cy - math.cos(a) * r * 0.92)], INK, 6)
        mins = 59 + min(1, k * 1.25)
        am = mins / 60 * 2 * math.pi; ah = (11 + mins / 60) / 12 * 2 * math.pi
        p.line([(cx, cy), (cx + math.sin(am) * r * 0.78, cy - math.cos(am) * r * 0.78)], INK, 12)
        p.line([(cx, cy), (cx + math.sin(ah) * r * 0.5, cy - math.cos(ah) * r * 0.5)], INK, 18)
        fr = fr.convert("RGBA"); fr.alpha_composite(L.resize((W, H), Image.LANCZOS)); fr = fr.convert("RGB")
        text(fr, W / 2, 790, "الليلة اللي بعدها...", 84, (200, 210, 255), (0, 0, 20), 6)
    elif name == "title":
        text(fr, W / 2, H / 2 - 80, "عمارة نعناعة", 110, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 + 50, "سر الدور السابع", 64, g((230, 230, 230)))
        text(fr, W / 2, H / 2 + 145, "الحلقة 4: ليلة انقطاع النور", 48, g((210, 210, 210)))
    elif name == "endcard":
        text(fr, W / 2, H / 2 - 60, "الحلقة 5 بكرة", 104, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 + 70, "مين اللي بينادي على شطة؟ اكتب في الكومنتات", 48, g((230, 230, 230)))
    return fr

def morse_sos(fr, tt, y=110, scale=1.0, cx=W / 2):
    if not (J03_T + 0.3 <= tt < SOS[1]): return
    d = ImageDraw.Draw(fr, "RGBA"); n = min(9, int((tt - J03_T - 0.3) / 0.12) + 1)
    sym = ["d"] * 3 + ["l"] * 3 + ["d"] * 3
    gap = 64 * scale; total = 9 * gap + 2 * 40 * scale; x = cx - total / 2
    d.rounded_rectangle([x - 30 * scale, y - 46 * scale, x + total + 10 * scale, y + 46 * scale], int(20 * scale), fill=(10, 10, 20, 200), outline=(255, 214, 90, 255), width=3)
    for i, sy in enumerate(sym):
        xi = x + i * gap + (i // 3) * 40 * scale + 10 * scale
        col = (255, 214, 90, 255) if i < n else (90, 90, 100, 160)
        if sy == "d": d.ellipse([xi, y - 12 * scale, xi + 24 * scale, y + 12 * scale], fill=col)
        else: d.rounded_rectangle([xi - 6 * scale, y - 9 * scale, xi + 42 * scale, y + 9 * scale], int(8 * scale), fill=col)
    if tt >= SOS[0]:
        a_ = min(1, (tt - SOS[0]) / 0.25); pop = 1 + 0.25 * max(0, 1 - (tt - SOS[0]) / 0.2)
        for j, ch_ in enumerate("SOS"):
            xi = x + j * (3 * gap + 40 * scale) + 1.5 * gap - 6 * scale
            text(fr, xi, y + 95 * scale, ch_, int(80 * scale * pop), (255, 90, 70, int(255 * a_)), (20, 0, 0), 6)

def diagram(fr, tt, x=1340, y=60, w=540, h=320, scale=1.0):
    if not DIAG[0] <= tt < DIAG[1]: return
    a_ = min(1, (tt - DIAG[0]) / 0.3)
    d = ImageDraw.Draw(fr, "RGBA"); S = lambda v: v * scale
    d.rounded_rectangle([x, y, x + S(w), y + S(h)], int(S(22)), fill=(12, 12, 22, int(225 * a_)), outline=(255, 214, 90, int(255 * a_)), width=3)
    fx_ = x + S(70); fy = y + S(250)
    d.line([(x + S(20), fy + S(20)), (x + S(w - 20), fy + S(20))], fill=(160, 160, 170, 255), width=3)
    wallx = x + S(w - 70); d.line([(wallx, y + S(30)), (wallx, fy + S(20))], fill=(160, 160, 170, 255), width=4)
    d.rounded_rectangle([fx_ - S(18), fy, fx_ + S(18), fy + S(16)], 4, fill=(250, 220, 90, 255))
    px = x + S(240); head = fy - S(60)
    d.ellipse([px - S(14), head - S(14), px + S(14), head + S(14)], fill=(240, 240, 240, 255))
    d.line([(px, head + S(14)), (px, fy + S(20))], fill=(240, 240, 240, 255), width=4)
    k = min(1, (tt - DIAG[0]) / 1.2)
    tipy = fy - (fy - head) * (wallx - fx_) / (px - fx_)
    ex_ = fx_ + (wallx - fx_) * k; ey_ = fy + (tipy - fy) * k
    d.line([(fx_, fy), (ex_, ey_)], fill=(255, 230, 120, 230), width=3)
    if k >= 1:
        d.rectangle([wallx - S(10), tipy, wallx, fy + S(20)], fill=(30, 30, 40, 255), outline=(255, 90, 70, 255), width=2)
        text(fr, x + S(w / 2), y + S(40), "نور من تحت = ضل أطول", int(S(34)), (255, 214, 90), (0, 0, 0), 3)

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
    text(bgv, 540, 420, "الحلقة 4: ليلة انقطاع النور", 50, (235, 235, 235))
    k, _ = line_at(tt)
    if k:
        for i, l in enumerate(wrap(SUB[k])[:4]): text(bgv, 540, 1290 + i * 80, l, 60, sw=6)
    morse_sos(bgv, tt, y=470, scale=0.75, cx=540)
    diagram(bgv, tt, x=270, y=1600, scale=1.0)
    if PUZ <= tt < PUZ_END:
        d.rounded_rectangle([40, 1640, 1040, 1800], 26, fill=(20, 20, 30), outline=(255, 214, 90), width=5)
        text(bgv, 540, 1695, "لغز الحلقة: صاحب الضل كان طويل ولا قصير؟", 44, (255, 214, 90))
        text(bgv, 540, 1758, "اكتب حلّك في الكومنتات", 42)
    return bgv

def finish(fr, tt, dark=False):
    fr = ImageChops.multiply(fr, VIG_DARK if dark else VIG)
    a = np.asarray(fr, np.float32)
    g = GRAIN[int(tt * FPS) % len(GRAIN)]
    g = np.repeat(np.repeat(g, 2, 0), 2, 1)[..., None]
    return Image.fromarray(np.clip(a + g, 0, 255).astype(np.uint8))

CUR_T = [0.0]
def frame(tt):
    CUR_T[0] = tt
    sh = shot_at(tt); set_ = sh["set"]
    if set_ in ("card_clock", "title", "endcard"): return finish(card(set_, tt, sh), tt)
    if set_ == "black": return Image.new("RGB", (W, H), (0, 0, 0))
    cam = cam_at(sh, tt)
    if sh.get("blackout"): return finish(eyes_only(sh, tt, cam), tt)
    img = bg_frame(set_, cam)
    layer, lights = draw_scene_chars(set_, tt, cam)
    layer = tint_layer(layer, TINT[set_], 1.0 if set_ == "bedroom" else 0.95)
    img.paste(layer, (0, 0), layer)
    fr = img.resize((W, H), Image.LANCZOS)
    hand = None
    if set_ != "bedroom":
        lights_w = []
        for L in lights:
            if L[0] == "hand": lights_w.append(L)
            else: lights_w.append(L)
        lm, spot, hand = light_map(set_, sh, tt, cam, lights_w)
        fr = ImageChops.multiply(fr, lm)
        fr = ImageEnhance.Brightness(fr).enhance(1.7)
        if set_ == "door7": draw_doorlight(fr, tt, cam)
        if sh.get("torch") and spot is not None:
            sp = Image.fromarray((np.clip(spot, 0, 1) * 255).astype(np.uint8)).resize((W, H), Image.BILINEAR)
            fr = Image.composite(ImageChops.screen(fr, Image.new("RGB", (W, H), (120, 112, 92))), fr, sp)
            smk = shadow_mask(tt, cam, full=True)
            if smk is not None:
                al = ImageChops.multiply(smk, sp.point(lambda v: min(255, int(v * 1.8))))
                fr = Image.composite(Image.new("RGB", (W, H), (8, 8, 12)), fr, al.point(lambda v: int(v * 0.9)))
        if sh.get("torch"): draw_beam(fr, sh, tt, cam, hand)
        draw_particles(fr, sh, tt, cam)
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
        h = base.copy()
        morse_sos(h, tt); diagram(h, tt)
        if PUZ <= tt < PUZ_END:
            d = ImageDraw.Draw(h, "RGBA")
            d.rounded_rectangle([W / 2 - 640, 60, W / 2 + 640, 180], 24, fill=(20, 20, 30, 215), outline=(255, 214, 90, 255), width=4)
            text(h, W / 2, 120, "لغز الحلقة: صاحب الضل كان طويل ولا قصير؟ اكتب في الكومنتات", 36, (255, 214, 90))
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
    mix_into(buf, drone(TOTAL + 1), 0, 1.0)
    r = np.random.default_rng(9)
    ts = np.arange(int(SR * 1.6)) / SR
    S = {"knock": sfx_knock(), "boom": sfx_boom(), "tick": sfx_tick() * 2.0, "powercut": sfx_powercut(), **SFXF}
    _k = sfx_knock(); S["hknock"] = _k * 1.3 + sfx_boom()[:len(_k)] * 0.6
    tc = np.arange(int(SR * 0.06)) / SR
    S["click"] = r.normal(0, 1, len(tc)) * np.exp(-tc * 140) * 0.7
    S["sting"] = (np.sin(2 * np.pi * (1200 + 80 * np.sin(ts * 40)) * ts) * 0.08 + np.sin(2 * np.pi * 1263 * ts) * 0.06
                  + np.sin(2 * np.pi * 55 * ts) * 0.4) * np.exp(-ts * 1.8)
    fl = np.zeros(int(SR * 1.0), np.float32)
    for i in range(7): mix_into(fl, S["click"] * 0.8, i * 0.14 + r.uniform(0, 0.04), 1.0)
    tb = np.arange(len(fl)) / SR; fl += np.sin(2 * np.pi * 120 * tb) * 0.05 * (np.sin(tb * 60) > 0)
    S["flicker"] = fl
    for t0, n, g in sfx: mix_into(buf, S[n], t0, g)
    tsx = np.arange(int(SR * 0.25)) / SR
    for i, (st, g, jing) in enumerate(STEPS):
        nz = np.convolve(r.normal(0, 1, len(tsx)), np.ones(12) / 12, mode="same")
        step = (np.sin(2 * np.pi * 75 * tsx) * np.exp(-tsx * 30) * 0.9 + nz * np.exp(-tsx * 25) * 0.9) * 0.6
        mix_into(buf, step, st, g)
        if jing and i % 2 == 0:
            jt = np.arange(int(SR * 0.3)) / SR
            jj = sum(np.sin(2 * np.pi * f * jt + r.uniform(0, 6)) * np.exp(-jt * (18 + 6 * j)) for j, f in enumerate(r.uniform(3200, 6800, 4)))
            mix_into(buf, jj * 0.05, st + 0.02, g)
    for st, k in lines: mix_into(buf, AUD[k], st, 1.0)
    # silence the drone hard during blackout for tension
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
        mux("h.mp4", "sirr_eldor_elsabe3_ep4.mp4"); mux("v.mp4", "sirr_eldor_elsabe3_ep4_vertical.mp4")
        print("done")
