import sys, os, math, subprocess, wave
sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter, ImageFont
from engine import *

os.chdir(ROOT + "/s1e8")
SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(81)
E1 = ROOT + "/s1e1/"

SUB = {
 "P01": "لغز امبارح: اللي قالوا أستاذ فهمي... صح! القلم الأحمر كان في جيبه.",
 "P02": "خلاص. الليلة هندخل الدور السابع، مهما حصل!",
 "P03": "من غير الكشكول؟ ...أنا مش عارف أحسبها.",
 "P04": "بصوا... البواب داخل جوه بمفتاحه!",
 "P05": "مشي... بس الباب لسه مفتوح!",
 "P06": "يلا... قبل ما حد يشوفنا. ثقوا فيا!",
 "P07": "تلاتين سنة... وكل حاجة زي ما هي.",
 "P08": "الراديو اشتغل لوحده!",
 "P09": "استنوا... بصوا على الحيطة.",
 "P10": "فيه حاجة ناقصة هنا...",
 "P11": "لغز النهارده: إيه الحاجة الناقصة في الأوضة؟ اكتبوا في الكومنتات!",
 "P12": "والبكرة اللي بره الشباك دي... ليه مربوط فيها حاجة؟",
 "P13": "الباب! حد قفل علينا من بره!",
 "P14": "إحنا محبوسين... في الدور السابع.",
}
WHO = {"P01": "tota", "P02": "shatta", "P03": "zalata", "P04": "tota", "P05": "zalata", "P06": "shatta",
       "P07": "zalata", "P08": "shatta", "P09": "tota", "P10": "zalata", "P11": "tota", "P12": "tota",
       "P13": "shatta", "P14": "zalata"}
EXPR = {"P01": "happy", "P02": "angry", "P03": "sad", "P04": "scared", "P05": "scared", "P06": [(0, "scared"), (0.6, "angry")],
        "P07": "neutral", "P08": "shock", "P09": "neutral", "P10": "flat", "P11": [(0, "neutral"), (0.6, "smug")],
        "P12": "neutral", "P13": "shock", "P14": "scared"}
ARMS = {"P01": "point", "P02": "hips", "P03": "down", "P04": "point", "P05": "point", "P06": "point", "P07": "down",
        "P08": "up", "P09": "point", "P10": "point", "P11": "point", "P12": "point", "P13": "up", "P14": "scared"}

AUD = {k: load_audio(f"audio/{k}.mp3") for k in SUB}
ENV = {k: envelope(v) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}
SFXF = {n: load_audio(f"sfx/{n}.mp3") for n in ("whoosh", "creak", "slam", "radio", "lock")}

lines, sfx, shots, jumps, shakes = [], [], [], {}, []
def say(t, k): lines.append((t, k)); return t + DUR[k]
def fx(t, n, g=1.0): sfx.append((t, n, g))
def jump(w, t): jumps.setdefault(w, []).append(t)
def shot(set_, s, e, c0, c1=None, **kw):
    shots.append(dict(set=set_, start=s, end=e, c0=c0, c1=c1 or c0, **kw))
def cut(t, g=0.45): fx(t - 0.12, "whoosh", g)
KIDS = ("shatta", "zalata", "tota")

BED = {"shatta": (620, 1030, 2.4), "zalata": (960, 1030, 2.4), "tota": (1300, 1030, 2.4)}
D7 = {"tota": (240, 1030, 1.9), "shatta": (410, 1030, 1.9), "zalata": (585, 1030, 1.9)}
APT = {"tota": (700, 1000, 2.0), "shatta": (940, 1010, 2.0), "zalata": (1180, 1000, 2.0)}
def CU(who, pos, z=2.2, dx=0):
    x, y, s = pos; S = s * CH[who]["scale"]
    if who == "tota": z *= 1.3
    hy = y - 190 * S
    return (x + dx, hy + H / (2 * z) - 1.45 * 46 * S - 25, z)

t = 0.0
# ===== 0. HOOK: door 7 ajar =====
fx(0.3, "creak", 1.2)
shot("door7", 0, 3.0, (1330, 560, 1.6), (1330, 600, 2.4), hookdoor=True, dark=True)
t = 3.0
cut(t, 0.6); fx(t, "boom", 0.7); shot("title", t, t + 1.6, None); t += 1.6
# ===== 1. bedroom: answer + decision =====
cut(t, 0.4); s = t; t += 0.15
P01_T = t; t = say(t, "P01") + 0.12
shot("bedroom", s, t, CU("tota", BED["tota"], 1.9), CU("tota", BED["tota"], 2.25))
s = t; t = say(t, "P02") + 0.1
shot("bedroom", s, t, CU("shatta", BED["shatta"], 1.6), CU("shatta", BED["shatta"], 2.4), ease="crash")
s = t; P03_T = t; t = say(t, "P03") + 0.35
shot("bedroom", s, t, CU("zalata", BED["zalata"], 2.0), CU("zalata", BED["zalata"], 2.2), cloud=True)
# ===== 2. door 7 stakeout =====
cut(t, 0.5); D0 = t
BW = (t + 0.2, t + 2.0)   # Bondo walks to the door
UNLOCK = t + 2.1; fx(UNLOCK, "lock", 0.7); fx(UNLOCK + 0.5, "creak", 0.9)
INSIDE = (t + 2.7, t + 5.6)
for i, dt in enumerate((0, .22, .44, 1.0, 1.42, 1.84, 2.3, 2.52, 2.74)): fx(INSIDE[0] + 0.1 + dt, "mknock", 0.55)
shot("door7", t, INSIDE[0], (960, 560, 1.0), (1050, 560, 1.08))
s = INSIDE[0]; t = say(s + 0.1, "P04") + 0.1
shot("door7", s, INSIDE[1], (420, 690, 1.75), (420, 690, 1.9))
t = INSIDE[1]
OUT = (t, t + 1.8)
shot("door7", t, OUT[1], (1150, 600, 1.15), (1100, 600, 1.1))
t = OUT[1]; s = t; t = say(t, "P05") + 0.1
shot("door7", s, t, (1330, 620, 2.0), (1330, 620, 2.3), doorglow=True)
s = t; t = say(t, "P06") + 0.15
shot("door7", s, t, CU("shatta", D7["shatta"], 2.3), CU("shatta", D7["shatta"], 2.5))
# ===== 3. inside apartment 7 =====
cut(t, 0.6); ENTER = (t, t + 2.2); fx(t + 0.1, "creak", 1.1)
shot("apt", t, ENTER[1], (960, 540, 1.0), (980, 560, 1.08))
t = ENTER[1]; s = t; t = say(t, "P07") + 0.25
shot("apt", s, t, CU("zalata", APT["zalata"], 2.0), CU("zalata", APT["zalata"], 2.2))
FOOT = (t, t + 2.4); fx(t + 0.3, "sting", 0.7)
shot("apt", t, FOOT[1], (1330, 780, 2.2), (1260, 760, 2.5), foot=True); t = FOOT[1]
CLOCKSW = (t, t + 2.0)
for i in range(5): fx(t + 0.2 + i * 0.4, "tock", 1.0)
shot("apt", t, CLOCKSW[1], (630, 170, 2.6), (630, 170, 3.0), clock=True); t = CLOCKSW[1]
RADIO = t; fx(t, "radio", 1.6); fx(t + 0.9, "radio", 1.2); shakes.append((t, 12))
for w_ in KIDS: jump(w_, t + 0.05)
shot("apt", t, t + 0.9, (615, 430, 2.6), (615, 430, 3.2), ease="crash")
t += 0.9; s = t; t = say(t, "P08") + 0.25
shot("apt", s, t, CU("shatta", APT["shatta"], 1.8), CU("shatta", APT["shatta"], 2.3))
RADIO_OFF = t
s = t; t = say(t, "P09") + 0.1
shot("apt", s, t, CU("tota", APT["tota"], 2.0), CU("tota", APT["tota"], 2.2))
s = t; WALL = t; t = say(t, "P10") + 0.4
shot("apt", s, t, (945, 300, 2.0), (945, 260, 2.6), patch=True)
fx(s + 0.2, "sting", 0.9)
PUZ = t; s = t; t = say(t, "P11") + 0.6; PUZ_END = t
shot("apt", s, t, CU("tota", APT["tota"], 2.3), CU("tota", APT["tota"], 2.6))
s = t; P12_T = t; t = say(t, "P12") + 0.4
shot("apt", s, t, (1640, 230, 2.4), (1670, 215, 3.2), pulley=True)
# ===== 4. locked in =====
STEPS_OUT = (t, t + 1.4); SLAM = t + 1.5
fx(SLAM, "slam", 1.3); fx(SLAM + 0.35, "lock", 1.4); shakes.append((SLAM, 16))
for w_ in KIDS: jump(w_, SLAM + 0.05)
shot("apt", t, SLAM + 1.0, (960, 560, 1.05), (900, 580, 1.15))
t = SLAM + 1.0
KEYHOLE = (t, t + 1.6)
shot("keyhole", t, KEYHOLE[1], None); t = KEYHOLE[1]
s = t; t = say(t, "P13") + 0.1
shot("apt", s, t, CU("shatta", (260, 1000, 2.1), 2.0), CU("shatta", (260, 1000, 2.1), 2.4), rattle=True)
s = t; t = say(t, "P14") + 0.5
shot("apt", s, t, CU("zalata", APT["zalata"], 2.3), CU("zalata", APT["zalata"], 2.6), dark=True)
WALLK = [t + dt for dt in (0, .22, .44, 1.0, 1.42, 1.84, 2.3, 2.52, 2.74)]
for k_ in WALLK: fx(k_, "mknock", 1.1)
fx(t, "sting", 1.1)
shot("apt", t, WALLK[-1] + 0.8, (945, 330, 1.6), (945, 300, 2.4), patch=True, wallk=True, dark=True)
for w_ in KIDS: jump(w_, WALLK[0])
t = WALLK[-1] + 0.8
fx(t, "boom", 1.0); shot("black", t, t + 0.5, None); t += 0.5
shot("endcard", t, t + 3.2, None); t += 3.2
TOTAL = t

STEPS = []
def contacts(t0, t1, rate, g0=0.7, g1=0.7, jingle=False):
    n = math.ceil(t0 * rate / math.pi)
    while True:
        tc = n * math.pi / rate
        if tc >= t1: break
        if tc >= t0: STEPS.append((tc, g0 + (g1 - g0) * (tc - t0) / max(1e-3, t1 - t0), jingle))
        n += 1
contacts(BW[0], BW[1], 7, 0.5, 0.8, True)
contacts(OUT[0], OUT[1], 7, 0.8, 0.3, True)
contacts(ENTER[0], ENTER[1], 7, 0.25, 0.25)
contacts(STEPS_OUT[0], STEPS_OUT[1] + 0.2, 6, 0.4, 1.0)

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

_bed = Image.open(E1 + "bg/bedroom_clean.png").convert("RGB")
SRCBG = {"bedroom": ImageChops.multiply(ImageEnhance.Brightness(_bed).enhance(1.55), Image.new("RGB", _bed.size, (255, 236, 205))),
         "door7": Image.open(ROOT + "/s1e2/bg/door7.png").convert("RGB"),
         "apt": Image.open("bg/apt7_raw.png").convert("RGB")}
TINT = {"bedroom": (255, 240, 225), "door7": (175, 190, 255), "apt": (170, 185, 235)}
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
    if sh.get("rattle"): shake = max(shake, 7)
    if sh.get("wallk") and any(0 <= tt - k_ < 0.1 for k_ in WALLK): shake = max(shake, 6)
    cw, ch = W / z, H / z
    if sh["set"] != "bedroom":
        cx += math.sin(tt * 0.9) * 6 + math.sin(tt * 2.3) * 2.5; cy += math.sin(tt * 1.3 + 1) * 4
    x0 = min(max(cx - cw / 2, 0), W - cw); y0 = min(max(cy - ch / 2, 0), H - ch)
    if shake:
        x0 = min(max(x0 + rng.normal(0, shake / z), 0), W - cw); y0 = min(max(y0 + rng.normal(0, shake / z), 0), H - ch)
    return x0, y0, z

def actors(set_, tt, sh):
    A = []
    if set_ == "bedroom":
        for who, (x, y, s) in BED.items():
            a = dict(who=who, x=x, y=y, s=s, look={"shatta": 1, "zalata": 0, "tota": -1}[who], expr="neutral")
            if who == "zalata": a["expr"] = "sad"
            A.append(a)
    elif set_ == "door7":
        for who, (x, y, s) in D7.items():
            A.append(dict(who=who, x=x, y=y, s=s, look=1, expr="scared", arms="down"))
        if BW[0] <= tt < INSIDE[0] + 0.4:
            k = min(1, (tt - BW[0]) / (BW[1] - BW[0]))
            al = 1.0 if tt < INSIDE[0] else max(0, 1 - (tt - INSIDE[0]) / 0.4)
            A.append(dict(who="bondo2", x=lerp(2100, 1330, ease(k)), y=1000, s=2.2, look=-1 if k < 1 else 1, held="lantern",
                          arms="hold" if tt < UNLOCK - 0.2 or tt > UNLOCK + 0.4 else "point", walk=tt * 7 if k < 1 else None, alpha=al, expr="flat"))
        if OUT[0] <= tt < OUT[1]:
            k = (tt - OUT[0]) / (OUT[1] - OUT[0])
            A.append(dict(who="bondo2", x=lerp(1330, 2150, ease(k)), y=1000, s=2.2, look=1, held="lantern", arms="hold", walk=tt * 7,
                          alpha=min(1, (tt - OUT[0]) / 0.3), expr="sad"))
    elif set_ == "apt":
        for who, (x, y, s) in APT.items():
            a = dict(who=who, x=x, y=y, s=s, look=0, expr="scared")
            if tt < ENTER[1]:
                k = (tt - ENTER[0]) / (ENTER[1] - ENTER[0]); off = {"tota": 0, "shatta": 0.15, "zalata": 0.3}[who]
                kk = min(1, max(0, (k - off) / 0.7))
                a["x"] = lerp(-150, x, ease(kk)); a["y"] = lerp(870, y, ease(kk)); a["s"] = lerp(1.6, s, ease(kk)); a["walk"] = tt * 7 if kk < 1 else None
                a["look"] = 1
            if who == "tota": a["held"] = "torch"; a["arms"] = "hold"
            if who == "zalata" and tt >= P12_T: a["look"] = 1
            if tt >= SLAM:
                a["expr"] = "shock"; a["arms"] = "scared"; a["look"] = -1; a["held"] = None
                if who == "shatta" and tt >= KEYHOLE[1] - 0.01: a["x"], a["y"], a["s"] = 260, 1000, 2.1; a["arms"] = "up"; a["lean"] = math.sin(tt * 18) * 0.8
            if tt >= RADIO and tt < RADIO_OFF + 0.6: a["expr"] = "shock"; a["arms"] = "scared" if who != "tota" else "hold"
            A.append(a)
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

def draw_scene_chars(set_, tt, cam, sh):
    x0, y0, z = cam
    layer = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(layer)
    k, lt = line_at(tt); lights = []; hand = None
    insert = sh.get("foot") or sh.get("clock")
    if insert: hand = (W * 0.1, H * 1.05)
    for a in ([] if insert else sorted(actors(set_, tt, sh), key=lambda a: a["s"])):
        who = a["who"]; talking = k is not None and WHO[k] == who
        expr = a.get("expr", "neutral")
        if talking: expr = expr_of(k, lt)
        mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
        arms = a.get("arms", "down")
        if talking: arms = ARMS.get(k, "talk" if arms == "down" else arms)
        if a.get("held") in ("torch", "lantern") and not (talking and arms == "point" and who != "tota"): arms = "hold" if not (talking and who == "tota" and ARMS.get(k) == "point") else "point"
        bob = abs(math.sin(a["walk"])) * 5 * a["s"] if a.get("walk") is not None else 0
        wy = a["y"] - jump_off(who, tt) - bob
        shiver = math.sin(tt * 60) * 2.5 if expr in ("scared", "shock") and who in KIDS else 0
        blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11
        X = (a["x"] + shiver - x0) * z; Y = (wy - y0) * z; s = a["s"] * z
        target = p; L = None
        if a.get("alpha", 1) < 1: L = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); target = P(L)
        target.ell(X, (a["y"] - y0) * z + 4 * s, 46 * s, 9 * s, (0, 0, 0, 110), None)
        draw_char(target, who, X, Y, s, expr, mouth, a.get("look", 0), blink, arms, tt, a.get("held"), a.get("lean", 0), a.get("walk"))
        if L is not None:
            al_ = a["alpha"]; L.putalpha(L.getchannel("A").point(lambda v: int(v * al_))); layer = Image.alpha_composite(layer, L); p = P(layer)
        S = s * CH[who]["scale"]
        if who == "bondo2": lights.append((X + 46 * S, Y - 75 * S, 380 * z, 0.9 * a.get("alpha", 1), (1.0, 0.75, 0.45)))
        if who == "tota" and a.get("held") == "torch":
            hand = (X + (84 if arms == "point" else 46) * S, Y - (140 if arms == "point" else 104) * S)
    if sh.get("cloud") and set_ == "bedroom":   # gloomy rain cloud over Zalata
        x, y, s = BED["zalata"]; S = s * z; cx = (x - x0) * z; cy = (y - y0) * z - 330 * S
        bob = math.sin(tt * 3) * 4 * S
        for dx, r in ((-38, 30), (0, 40), (40, 30), (-15, 28), (20, 26)):
            p.ell(cx + dx * S, cy + bob, r * S, r * 0.75 * S, (110, 115, 130, 255), INK, 2.5 * S)
        for i in range(6):
            u = ((tt * 1.6 + i * 0.37) % 1)
            dx = (-45 + i * 18) * S
            p.line([(cx + dx, cy + 26 * S + u * 110 * S), (cx + dx - 3 * S, cy + 40 * S + u * 110 * S)], (120, 170, 255, 220), 3 * S)
    return layer, lights, hand

def tint_layer(layer, tint, lvl):
    rgb = layer.convert("RGB"); al = layer.getchannel("A")
    c = tuple(int((v * 0.55 + 255 * 0.45) * min(1.0, lvl)) for v in tint)
    rgb = ImageChops.multiply(rgb, Image.new("RGB", rgb.size, c))
    out = rgb.convert("RGBA"); out.putalpha(al); return out

LW, LH = W // 8, H // 8
gy, gx = np.mgrid[0:LH, 0:LW] * 8.0
def glow(X, Y, R): return np.exp(-((gx - X) ** 2 + (gy - Y) ** 2) / (R * R))

def torch_target(sh, tt, cam):
    x0, y0, z = cam
    if sh.get("foot"): wx, wy = 1300, 800
    elif sh.get("clock"): wx, wy = 630, 180
    elif sh.get("patch") or (WALL <= tt < PUZ): wx, wy = 945, 260
    elif sh.get("pulley"): wx, wy = 1660, 230
    elif RADIO <= tt < RADIO_OFF: wx, wy = 615, 440
    else: wx, wy = 900 + math.sin(tt * 0.8) * 240, 420 + math.sin(tt * 1.3) * 60
    return (wx - x0) * z, (wy - y0) * z, 300 * z

def light_map(set_, sh, tt, cam, lights, hand):
    x0, y0, z = cam; W3 = lambda px, py: ((px - x0) * z, (py - y0) * z)
    if set_ == "door7":
        m = np.full((LH, LW, 3), 0.42, np.float32) * np.array([0.8, 0.9, 1.05], np.float32)
        X, Y = W3(150, 860); m += 0.45 * glow(X, Y, 520 * z)[..., None] * np.array([0.8, 0.9, 1.0], np.float32)
        if sh.get("hookdoor") or sh.get("doorglow") or tt >= UNLOCK + 0.5:
            fl = 0.75 + 0.25 * math.sin(tt * 27) * math.sin(tt * 6)
            X, Y = W3(1290, 520); m += 1.1 * fl * glow(X, Y, 260 * z)[..., None] * np.array([1.0, 0.75, 0.45], np.float32)
    else:
        m = np.full((LH, LW, 3), 0.3, np.float32) * np.array([0.75, 0.85, 1.1], np.float32)
        X, Y = W3(1650, 300); m += 0.9 * glow(X, Y, 520 * z)[..., None] * np.array([0.75, 0.85, 1.1], np.float32)
        if RADIO <= tt < RADIO_OFF:
            fl = 0.6 + 0.4 * (int(tt * 15) % 2)
            X, Y = W3(615, 445); m += 1.4 * fl * glow(X, Y, 200 * z)[..., None] * np.array([1.0, 0.6, 0.25], np.float32)
    for X, Y, R, inten, col in lights:
        m += inten * glow(X, Y, R)[..., None] * np.array(col, np.float32)
    spot = None
    if hand and set_ == "apt" and tt < SLAM + 0.2:
        tx, ty, R = torch_target(sh, tt, cam); spot = glow(tx, ty, R)
        m += 1.8 * spot[..., None] * np.array([1.0, 0.97, 0.85], np.float32)
        m += 0.35 * glow(hand[0], hand[1], 240 * z)[..., None] * np.array([1.0, 0.95, 0.85], np.float32)
    return Image.fromarray((np.clip(m / 1.4, 0, 1) * 255).astype(np.uint8), "RGB").resize((W, H), Image.BILINEAR), spot

DUST = rng.uniform(-1, 1, (50, 3))
def moonbeams(fr, tt, cam):
    x0, y0, z = cam
    ov = Image.new("L", (W // 2, H // 2), 0); d = ImageDraw.Draw(ov)
    for i, (a, b) in enumerate(((1560, 1700), (1620, 1760), (1680, 1820))):
        p1 = ((a - x0) * z / 2, (60 - y0) * z / 2); p2 = ((b - x0) * z / 2, (60 - y0) * z / 2)
        p3 = ((b - 900 - x0) * z / 2, (1000 - y0) * z / 2); p4 = ((a - 1000 - x0) * z / 2, (1000 - y0) * z / 2)
        d.polygon([p1, p2, p3, p4], fill=26)
    ov = ov.filter(ImageFilter.GaussianBlur(10)).resize((W, H), Image.BILINEAR)
    fr.paste(Image.new("RGB", (W, H), (190, 210, 255)), (0, 0), ov)
    dd = ImageDraw.Draw(fr, "RGBA")
    for i, (a, b, c) in enumerate(DUST):
        u = (a * 0.5 + 0.5 + tt * 0.02 * (1 + c)) % 1
        wx = lerp(1650, 900, u) + b * 150; wy = lerp(80, 980, u) + math.sin(tt + i) * 20
        X, Y = (wx - x0) * z, (wy - y0) * z; r = (1.2 + abs(c) * 1.6) * min(2, z)
        dd.ellipse([X - r, Y - r, X + r, Y + r], fill=(220, 230, 255, int(90 + 60 * c)))

def draw_beam(fr, sh, tt, cam, hand):
    if not hand or tt >= SLAM + 0.2: return
    tx, ty, R = torch_target(sh, tt, cam)
    ov = Image.new("L", (W // 2, H // 2), 0); d = ImageDraw.Draw(ov)
    hx, hy = hand[0] / 2, hand[1] / 2; ang = math.atan2(ty - hand[1], tx - hand[0]); w_ = R * 0.6 / 2
    px, py = -math.sin(ang) * w_, math.cos(ang) * w_
    d.polygon([(hx, hy), (tx / 2 + px, ty / 2 + py), (tx / 2 - px, ty / 2 - py)], fill=44)
    ov = ov.filter(ImageFilter.GaussianBlur(14)).resize((W, H), Image.BILINEAR)
    fr.paste(Image.new("RGB", (W, H), (255, 248, 220)), (0, 0), ov)

def door_props(img, tt, cam, sh):
    x0, y0, z = cam; S = SS * z; d = ImageDraw.Draw(img, "RGBA")
    if sh.get("hookdoor") or sh.get("doorglow") or tt >= UNLOCK + 0.5:
        k = 1.0 if (sh.get("hookdoor") or tt >= OUT[0]) else min(1, (tt - UNLOCK - 0.5) / 0.6)
        if sh.get("hookdoor"): k = min(1, tt / 2.5)
        gapw = (20 + 40 * k)
        fl = 0.75 + 0.25 * math.sin(tt * 27) * math.sin(tt * 6)
        X0, X1 = (1280 - x0) * S, (1280 + gapw - x0) * S
        d.rectangle([X0, (150 - y0) * S, X1, (780 - y0) * S], fill=(255, 205, 130, int(230 * fl)))
        d.polygon([(X0, (780 - y0) * S), (X1, (780 - y0) * S), (X1 + 160 * S, (900 - y0) * S), (X0 - 40 * S, (900 - y0) * S)], fill=(255, 205, 130, int(60 * fl)))

def apt_props(img, tt, cam, sh):
    x0, y0, z = cam; S = SS * z; d = ImageDraw.Draw(img, "RGBA")
    if RADIO <= tt < RADIO_OFF:   # radio dial glow
        X, Y = (615 - x0) * S, (440 - y0) * S
        d.rectangle([X - 40 * S, Y - 12 * S, X + 40 * S, Y + 12 * S], fill=(255, 170, 60, 200 if int(tt * 15) % 2 else 120))
    if sh.get("patch"):
        a_ = int(150 + 100 * math.sin(tt * 6))
        d.rectangle([(825 - x0) * S, (144 - y0) * S, (1065 - x0) * S, (336 - y0) * S], outline=(255, 214, 90, a_), width=max(2, int(6 * S)))
        X, Y = (945 - x0) * S, (120 - y0) * S
        if int(tt * 4) % 2: d.line([(X - 14 * S, Y), (X + 14 * S, Y)], fill=(255, 255, 220, 220), width=max(1, int(3 * S)))
    if sh.get("wallk"):
        for k_ in WALLK:
            u = tt - k_
            if 0 <= u < 0.6:
                for i in range(10):
                    px = (845 + i * 22 - x0) * S; py = (336 + u * 300 + (i % 3) * 10 - y0) * S
                    d.ellipse([px - 3 * S, py - 3 * S, px + 3 * S, py + 3 * S], fill=(200, 190, 170, int(220 * (1 - u / 0.6))))
    if sh.get("foot"):   # fresh footprints in the dust leading to the wall
        k = (tt - FOOT[0]) / (FOOT[1] - FOOT[0])
        for i in range(9):
            if k < i / 12: continue
            fxw = 1520 - i * 55; fyw = 860 - i * 15 + (12 if i % 2 else -12)
            X, Y = (fxw - x0) * S, (fyw - y0) * S
            d.ellipse([X - 20 * S, Y - 9 * S, X + 20 * S, Y + 9 * S], fill=(18, 15, 12, 235))
            d.ellipse([X - 31 * S, Y - 7 * S, X - 17 * S, Y + 7 * S], fill=(18, 15, 12, 220))
    if sh.get("clock"):   # stopped pendulum suddenly swings
        u = tt - CLOCKSW[0]; ang = math.sin(u * math.pi * 2.5) * 0.35 * min(1, u / 0.3)
        X, Y = (630 - x0) * S, (180 - y0) * S; L_ = 90 * S
        ex, ey = X + math.sin(ang) * L_, Y + math.cos(ang) * L_
        d.line([(X, Y), (ex, ey)], fill=(200, 170, 90, 255), width=max(2, int(3 * S)))
        d.ellipse([ex - 12 * S, ey - 12 * S, ex + 12 * S, ey + 12 * S], fill=(210, 180, 90, 255), outline=(80, 60, 20, 255), width=max(1, int(2 * S)))
    if sh.get("pulley"):   # rolled paper tied on the pulley rope
        X, Y = (1672 - x0) * S, (290 - y0) * S
        d.line([(X, (215 - y0) * S), (X, Y)], fill=(170, 150, 110, 255), width=max(1, int(2 * S)))
        d.rounded_rectangle([X - 9 * S, Y, X + 9 * S, Y + 46 * S], int(6 * S), fill=(232, 222, 190, 255), outline=(60, 50, 30, 255), width=max(1, int(2 * S)))
        d.line([(X - 9 * S, Y + 20 * S), (X + 9 * S, Y + 20 * S)], fill=(150, 40, 40, 255), width=max(1, int(3 * S)))
        if int(tt * 5) % 2: d.line([(X + 18 * S, Y - 10 * S), (X + 18 * S, Y + 10 * S)], fill=(255, 255, 220, 230), width=max(1, int(2 * S)))

def bg_frame(set_, cam):
    x0, y0, z = cam; src = SRCBG[set_]; sw, sh = src.size; f = sw / W
    box = (x0 * f, y0 * f, (x0 + W / z) * f, (y0 + H / z) * f)
    if z > 1.6:
        b = tuple(int(v) for v in box); b = (max(0, b[0] - 20), max(0, b[1] - 20), min(sw, b[2] + 20), min(sh, b[3] + 20))
        part = src.crop(b).filter(ImageFilter.GaussianBlur(min(3, (z - 1.5) * 1.3)))
        box = (box[0] - b[0], box[1] - b[1], box[2] - b[0], box[3] - b[1]); src = part
    return src.resize((SSW, SSH), Image.BICUBIC, box=box)

def keyhole(tt):
    k = (tt - KEYHOLE[0]) / (KEYHOLE[1] - KEYHOLE[0])
    fr = Image.new("RGB", (W, H), (34, 22, 14)); d = ImageDraw.Draw(fr)
    for i in range(0, W, 7): d.line([(i, 0), (i + math.sin(i * 0.05) * 30, H)], fill=(40 + (i * 13) % 12, 26, 16), width=3)
    cx, cy = W / 2, H / 2
    d.rounded_rectangle([cx - 160, cy - 260, cx + 160, cy + 260], 30, fill=(110, 90, 50), outline=(60, 45, 20), width=6)
    d.ellipse([cx - 45, cy - 120, cx + 45, cy - 30], fill=(4, 4, 6)); d.polygon([(cx - 30, cy - 50), (cx + 30, cy - 50), (cx + 18, cy + 60), (cx - 18, cy + 60)], fill=(4, 4, 6))
    if int(tt * 3) % 2 and k > 0.3:
        g = Image.new("L", (W, H), 0); ImageDraw.Draw(g).ellipse([cx - 30, cy - 105, cx + 30, cy - 45], fill=200)
        fr.paste(Image.new("RGB", (W, H), (255, 40, 30)), (0, 0), g.filter(ImageFilter.GaussianBlur(10)))
        d.ellipse([cx - 6, cy - 81, cx + 6, cy - 69], fill=(255, 80, 60))
    a = np.asarray(fr, np.float32) * (np.asarray(VIG_DARK, np.float32) / 255)
    return Image.fromarray(a.astype(np.uint8))

def card(name, tt, sh):
    k = (tt - sh["start"]) / (sh["end"] - sh["start"])
    fr = Image.new("RGB", (W, H), (8, 8, 12))
    g = lambda c: tuple(int(v * min(1, k * 4)) for v in c)
    if name == "title":
        text(fr, W / 2, H / 2 - 80, "عمارة نعناعة", 110, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 + 50, "سر الدور السابع", 64, g((230, 230, 230)))
        text(fr, W / 2, H / 2 + 145, "الحلقة 8: الدور السابع", 48, g((210, 210, 210)))
    elif name == "endcard":
        text(fr, W / 2, H / 2 - 60, "الحلقة 9 بكرة", 104, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 + 70, "مين اللي قفل الباب؟ اكتب في الكومنتات", 48, g((230, 230, 230)))
    elif name == "keyhole": return keyhole(tt)
    return fr

def hud(fr, tt, v=False):
    sc = 0.85 if v else 1.0; cx = 540 if v else W / 2
    if P01_T + 1.6 <= tt < P01_T + DUR["P01"]:
        d = ImageDraw.Draw(fr, "RGBA"); y = 1700 if v else 120
        d.rounded_rectangle([cx - 420 * sc, y - 50 * sc, cx + 420 * sc, y + 50 * sc], int(22 * sc), fill=(20, 60, 30, 220), outline=(120, 230, 120, 255), width=4)
        text(fr, cx, y, "إجابة امبارح: فهمي... والقلم الأحمر ✓", int(42 * sc), (200, 255, 200))

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
    text(bgv, 540, 420, "الحلقة 8: الدور السابع", 52, (235, 235, 235))
    k, _ = line_at(tt)
    if k:
        for i, l in enumerate(wrap(SUB[k])[:4]): text(bgv, 540, 1290 + i * 80, l, 60, sw=6)
    hud(bgv, tt, True)
    if PUZ <= tt < PUZ_END:
        d.rounded_rectangle([40, 1640, 1040, 1800], 26, fill=(20, 20, 30), outline=(255, 214, 90), width=5)
        text(bgv, 540, 1695, "لغز الحلقة: إيه الناقص في الأوضة؟", 50, (255, 214, 90))
        text(bgv, 540, 1758, "اكتب حلّك في الكومنتات", 42)
    return bgv

def finish(fr, tt, dark=False):
    fr = ImageChops.multiply(fr, VIG_DARK if dark else VIG)
    a = np.asarray(fr, np.float32)
    g = GRAIN[int(tt * FPS) % len(GRAIN)]
    g = np.repeat(np.repeat(g, 2, 0), 2, 1)[..., None]
    return Image.fromarray(np.clip(a + g, 0, 255).astype(np.uint8))

def frame(tt):
    sh = shot_at(tt); set_ = sh["set"]
    if set_ in ("title", "endcard", "keyhole"): return finish(card(set_, tt, sh), tt)
    if set_ == "black": return Image.new("RGB", (W, H), (0, 0, 0))
    cam = cam_at(sh, tt)
    img = bg_frame(set_, cam)
    if set_ == "door7": door_props(img, tt, cam, sh)
    if set_ == "apt": apt_props(img, tt, cam, sh)
    layer, lights, hand = draw_scene_chars(set_, tt, cam, sh)
    layer = tint_layer(layer, TINT[set_], 1.0 if set_ == "bedroom" else 0.95)
    img.paste(layer, (0, 0), layer)
    fr = img.resize((W, H), Image.LANCZOS)
    if set_ != "bedroom":
        lm, spot = light_map(set_, sh, tt, cam, lights, hand)
        fr = ImageChops.multiply(fr, lm); fr = ImageEnhance.Brightness(fr).enhance(1.65)
        if spot is not None:
            sp = Image.fromarray((np.clip(spot, 0, 1) * 255).astype(np.uint8)).resize((W, H), Image.BILINEAR)
            fr = Image.composite(ImageChops.screen(fr, Image.new("RGB", (W, H), (100, 96, 80))), fr, sp)
        if set_ == "apt": moonbeams(fr, tt, cam); draw_beam(fr, sh, tt, cam, hand)
    if RADIO <= tt < RADIO + 0.25 and set_ == "apt":
        fr = ImageEnhance.Brightness(fr).enhance(1.5)
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
            d.rounded_rectangle([W / 2 - 600, 60, W / 2 + 600, 175], 24, fill=(20, 20, 30, 215), outline=(255, 214, 90, 255), width=4)
            text(h, W / 2, 117, "لغز الحلقة: إيه الحاجة الناقصة في الأوضة؟ اكتب في الكومنتات", 36, (255, 214, 90))
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
        if s_["set"] == "bedroom": env[int(s_["start"] * SR):int(s_["end"] * SR)] = 0.35
    env = np.convolve(env, np.ones(4410) / 4410, mode="same")
    mix_into(buf, dr * env, 0, 1.1)
    r = np.random.default_rng(9); ts = np.arange(int(SR * 1.6)) / SR
    k_ = sfx_knock()
    S = {"boom": sfx_boom(), **SFXF}
    mk = np.convolve(k_, np.ones(30) / 30, mode="same") * 1.4   # muffled knock (through a wall)
    S["mknock"] = mk
    tk = np.arange(int(SR * 0.15)) / SR
    S["tock"] = (np.sin(2 * np.pi * 900 * tk) * np.exp(-tk * 60) * 0.5 + r.normal(0, 1, len(tk)) * np.exp(-tk * 150) * 0.3)
    S["sting"] = (np.sin(2 * np.pi * (1200 + 80 * np.sin(ts * 40)) * ts) * 0.08 + np.sin(2 * np.pi * 1263 * ts) * 0.06
                  + np.sin(2 * np.pi * 55 * ts) * 0.4) * np.exp(-ts * 1.8)
    for t0, n, g in sfx:
        if n in S: mix_into(buf, S[n], t0, g)
    tsx = np.arange(int(SR * 0.25)) / SR; jt = np.arange(int(SR * 0.3)) / SR
    for i, (st, g, jing) in enumerate(STEPS):
        nz = np.convolve(r.normal(0, 1, len(tsx)), np.ones(12) / 12, mode="same")
        mix_into(buf, (np.sin(2 * np.pi * 80 * tsx) * np.exp(-tsx * 30) * 0.9 + nz * np.exp(-tsx * 25) * 0.9) * 0.6, st, g)
        if jing and i % 2 == 0:
            jj = sum(np.sin(2 * np.pi * f * jt + r.uniform(0, 6)) * np.exp(-jt * (18 + 6 * j)) for j, f in enumerate(r.uniform(3200, 6800, 4)))
            mix_into(buf, jj * 0.05, st + 0.02, g)
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
        mux("h.mp4", "sirr_eldor_elsabe3_ep8.mp4"); mux("v.mp4", "sirr_eldor_elsabe3_ep8_vertical.mp4")
        print("done")
