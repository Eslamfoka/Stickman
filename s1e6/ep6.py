import sys, os, math, subprocess, wave
sys.path.insert(0, "/home/claude/s1e1")
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter, ImageFont
from engine import *

os.chdir("/home/claude/s1e6")
SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(61)

SUB = {
 "L01": "استنوا! الخبط ده... مش زي بعضه!",
 "L02": "لغز امبارح: اللي قالوا السماعات... صح. ست سماعات، وكلهم فيهم نفس اللمبة الحمرا.",
 "L03": "الخبط التقيل جاي من السماعة... لكن الخبط الخفيف ده، إيد بني آدم!",
 "L04": "الكشكول! الورقة طارت!",
 "L05": "أنا هجيبها! ثقوا فيا!",
 "L06": "شطة! حاسب السور!",
 "L07": "جبتها... بس أنا مش هبص لتحت تاني أبدا.",
 "L08": "حد طالع! استخبوا ورا خزان المية!",
 "L09": "أيوه يا باشا... الخطة ماشية. أسبوع واحد بس، والسكان كلهم هيبيعوا.",
 "L10": "تاني الخبط ده؟! ...مين بيلعب من ورايا؟",
 "L11": "زلطة، اكتب بسرعة! خط ونقطة... نقطة وخط...",
 "L12": "لغز النهارده: فكوا الشفرة معايا! الحرف الأول N، والتاني A... كملوا الكلمة في الكومنتات!",
 "L13": "N... A... N... A. نانا؟",
 "L14": "نانا... يعني نعناعة! الرسالة لتيتا!",
 "L15": "بتعملوا إيه فوق السطوح في نص الليل؟!",
 "L16": "رشدي؟...",
}
WHO = {"L01": "tota", "L02": "zalata", "L03": "tota", "L04": "zalata", "L05": "shatta", "L06": "tota",
       "L07": "shatta", "L08": "zalata", "L09": "fahmy", "L10": "fahmy", "L11": "tota", "L12": "tota",
       "L13": "zalata", "L14": "tota", "L15": "nana", "L16": "nana"}
EXPR = {"L01": "shock", "L02": [(0, "flat"), (0.6, "smug")], "L03": "neutral", "L04": "shock", "L05": "angry",
        "L06": "shock", "L07": [(0, "scared"), (0.5, "sad")], "L08": "scared", "L09": "smug", "L10": "angry",
        "L11": "neutral", "L12": [(0, "neutral"), (0.6, "smug")], "L13": "neutral", "L14": "shock",
        "L15": "angry", "L16": "sad"}
ARMS = {"L01": "up", "L02": "talk", "L03": "point", "L04": "up", "L05": "point", "L06": "up", "L07": "down",
        "L08": "point", "L09": "hold", "L10": "hold", "L11": "point", "L12": "point", "L13": "hold", "L14": "up",
        "L15": "up", "L16": "down"}

AUD = {k: load_audio(f"audio/{k}.mp3") for k in SUB}
ENV = {k: envelope(v) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}
SFXF = {n: load_audio(f"sfx/{n}.mp3") for n in ("whoosh", "creak", "slam", "wind")}

lines, sfx, shots, jumps, shakes = [], [], [], {}, []
def say(t, k): lines.append((t, k)); return t + DUR[k]
def fx(t, n, g=1.0): sfx.append((t, n, g))
def jump(w, t): jumps.setdefault(w, []).append(t)
def shot(set_, s, e, c0, c1=None, **kw):
    shots.append(dict(set=set_, start=s, end=e, c0=c0, c1=c1 or c0, **kw))
def cut(t, g=0.45): fx(t - 0.12, "whoosh", g)
KIDS = ("shatta", "zalata", "tota")

POS = {"tota": (480, 1040, 2.1), "shatta": (700, 1040, 2.1), "zalata": (1360, 1040, 2.1)}
HIDE = {"tota": (1560, 1210, 2.5), "shatta": (1720, 1225, 2.5), "zalata": (1880, 1210, 2.5)}
DOOR = (205, 690)
VENT = (1000, 630)
def CU(who, z=2.2, dx=0, pos=None):
    x, y, s = pos or POS[who]; S = s * CH[who]["scale"]
    if who == "tota": z *= 1.3
    hy = y - 190 * S
    return (x + dx, hy + H / (2 * z) - 1.45 * 46 * S - 25, z)

def morse(t0, code, g=1.0):
    out = []; t = t0
    for ch in code:
        if ch == " ": t += 0.35; continue
        out.append((t, "dot" if ch == "." else "dash")); fx(t, "tap" if ch == "." else "tapl", g)
        t += 0.22 if ch == "." else 0.42
    return out, t

t = 0.0
# ===== 0. HOOK: vent =====
HEAVY = [0.35, 0.95, 1.55]
for k_ in HEAVY: fx(k_, "hknock", 1.1); shakes.append((k_, 10))
TAPS1, t = morse(2.3, "-. .-", 0.9)
shot("roof", 0, t + 0.15, (1000, 640, 2.4), (1000, 640, 2.8), hook=True)
t += 0.15; s = t; t = say(t, "L01") + 0.1
shot("roof", s, t, CU("tota", 2.0), CU("tota", 2.2))
cut(t, 0.6); fx(t, "boom", 0.7); shot("title", t, t + 1.6, None); t += 1.6
# ===== 1. answer + two kinds =====
cut(t, 0.4); s = t; t += 0.1
L02_T = t; t = say(t, "L02") + 0.1
shot("roof", s, t, CU("zalata", 2.0), CU("zalata", 2.25))
s = t; L03_T = t; t = say(t, "L03") + 0.15
shot("roof", s, t, (800, 640, 1.2), (820, 630, 1.3), kinds=True)
# ===== 2. wind & the page =====
GUST = t; fx(t, "wind", 1.4); fx(t + 0.5, "wind", 1.0)
PAGE = (t + 0.15, t + 1.8)
s = t; t += 0.35; t = say(t, "L04") + 0.05
shot("roof", s, t, (1150, 760, 1.5), (1250, 680, 1.4))
RUN = (t, t + 1.3)
s = t; t = say(t, "L05") + 0.1
shot("roof", s, max(t, RUN[1]), (950, 760, 1.05), (1150, 650, 1.35))
t = max(t, RUN[1])
EDGE = t; fx(t, "sting", 1.0); fx(t + 0.1, "creak", 0.6)
s = t; t = say(t, "L06") + 0.1
shot("roof", s, t, CU("shatta", 2.0, pos=(1250, 665, 1.3)), CU("shatta", 3.0, pos=(1250, 665, 1.3)), edge=True)
CATCH = t; fx(t, "whoosh", 0.9); jump("shatta", t)
shot("roof", t, t + 1.2, (1200, 620, 1.6), (1200, 640, 1.7)); t += 1.2
s = t; t = say(t, "L07") + 0.2
shot("roof", s, t, CU("shatta", 2.2, pos=(1180, 690, 1.35)), CU("shatta", 2.4, pos=(1180, 690, 1.35)))
# ===== 3. Fahmy on the roof =====
DOORC = t; fx(t, "creak", 1.3); fx(t, "sting", 0.7)
shot("roof", t, t + 0.9, (300, 520, 1.8), (260, 500, 2.0)); t += 0.9
s = t; t = say(t, "L08") + 0.05
shot("roof", s, t, CU("zalata", 2.3, pos=(1300, 700, 1.35)), CU("zalata", 2.5, pos=(1300, 700, 1.35)))
HIDE_T = t; fx(t, "whoosh", 0.8)
FAH = (t, t + 2.2)
shot("roof", t, FAH[1], (960, 600, 1.0), (920, 620, 1.1), hidden=True)
t = FAH[1]; s = t; t = say(t, "L09") + 0.15
shot("roof", s, t, CU("fahmy", 2.0, pos=(900, 770, 1.5)), CU("fahmy", 2.3, pos=(900, 770, 1.5)), hidden=True, phone=True)
TAPS2, t2 = morse(t + 0.1, "-. .- -. .-", 1.0)
shot("roof", t, t2 + 0.2, (1000, 640, 2.2), (1000, 640, 2.6), hidden=True)
t = t2 + 0.2
s = t; t = say(t, "L10") + 0.1
shot("roof", s, t, CU("fahmy", 2.4, pos=(900, 770, 1.5)), CU("fahmy", 2.7, pos=(900, 770, 1.5)), hidden=True, phone=True)
FAHOUT = (t, t + 1.4); fx(t + 1.3, "slam", 1.0)
shot("roof", t, FAHOUT[1] + 0.2, (960, 600, 1.0), (980, 600, 1.05), hidden=True)
t = FAHOUT[1] + 0.2
# ===== 4. decode =====
cut(t, 0.4); s = t; L11_T = t; t = say(t, "L11") + 0.15
shot("roof", s, t, (920, 700, 1.15), (900, 690, 1.25), decode=True)
PUZ = t; s = t; t = say(t, "L12") + 0.6; PUZ_END = t
shot("roof", s, t, CU("tota", 2.3), CU("tota", 2.6), decode=True)
s = t; L13_T = t; t = say(t, "L13") + 0.15
shot("roof", s, t, CU("zalata", 2.1), CU("zalata", 2.4), decode=True)
s = t; t = say(t, "L14") + 0.1
shot("roof", s, t, CU("tota", 2.2), CU("tota", 2.6), ease="crash")
# ===== 5. Nana =====
NANA_IN = t; fx(t, "creak", 1.4); fx(t + 0.1, "sting", 1.0)
for w_ in KIDS: jump(w_, t + 0.35)
s = t; t += 0.25; t = say(t, "L15") + 0.2
shot("roof", s, t, (700, 640, 1.05), (520, 600, 1.25))
NB = (t, t + 1.6); fx(t + 0.2, "sting", 0.6)
shot("notebook", t, t + 1.6, None); t += 1.6
s = t; DROP = t + 0.2; t = say(t + 0.3, "L16") + 0.9
shot("roof", s, t, CU("nana", 2.2, pos=(330, 760, 1.6)), CU("nana", 3.0, pos=(330, 760, 1.6)), dark=True)
fx(DROP + 0.4, "thud", 0.8)
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
contacts(RUN[0], RUN[1], 10, 0.5, 0.4)
contacts(FAH[0] + 0.3, FAH[1], 6, 0.35, 0.6)
contacts(FAHOUT[0], FAHOUT[1], 6, 0.6, 0.3)

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

SRC = Image.open("bg/roof_raw.png").convert("RGB")
TINT = (175, 190, 240)
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
    if sh.get("edge"): shake = max(shake, 3)
    cw, ch = W / z, H / z
    cx += math.sin(tt * 0.9) * 6 + math.sin(tt * 2.3) * 2.5; cy += math.sin(tt * 1.3 + 1) * 4
    x0 = min(max(cx - cw / 2, 0), W - cw); y0 = min(max(cy - ch / 2, 0), H - ch)
    if shake:
        x0 = min(max(x0 + rng.normal(0, shake / z), 0), W - cw); y0 = min(max(y0 + rng.normal(0, shake / z), 0), H - ch)
    return x0, y0, z

# ---------------- actors ----------------
def kid_state(who, tt, sh):
    x, y, s = POS[who]
    a = dict(who=who, x=x, y=y, s=s, look=0, expr="neutral")
    if who == "zalata": a["held"] = "notebook"
    if tt < GUST: a["expr"] = "scared" if tt < L02_T else "neutral"
    if who == "shatta" and tt >= RUN[0]:
        k = min(1, (tt - RUN[0]) / (RUN[1] - RUN[0]))
        a["x"], a["y"], a["s"] = lerp(700, 1250, ease(k)), lerp(1040, 665, ease(k)), lerp(2.1, 1.3, ease(k))
        a["walk"] = tt * 12 if k < 1 else None; a["look"] = 1; a["arms"] = "point"
        if tt >= EDGE and tt < CATCH:
            a["lean"] = math.sin(tt * 9) * 1.4; a["arms"] = "up"; a["expr"] = "shock"
        if tt >= CATCH: a["held"] = "paper"; a["arms"] = "hold"; a["x"], a["y"], a["s"] = 1180, 690, 1.35; a["expr"] = "scared"
    if who == "zalata" and tt >= EDGE + 0.9:
        k = min(1, (tt - EDGE - 0.9) / 0.9)
        a["x"], a["y"], a["s"] = lerp(1360, 1110, ease(k)), lerp(1040, 715, ease(k)), lerp(2.1, 1.38, ease(k))
        a["walk"] = tt * 12 if k < 1 else None; a["look"] = 1
        if tt >= CATCH: a["x"], a["y"], a["s"] = 1110, 715, 1.38
    if who == "tota" and EDGE - 1 <= tt < DOORC: a["arms"] = "scared"; a["expr"] = "shock"
    if tt >= DOORC and tt < HIDE_T:
        a["expr"] = "scared"
        if who == "tota": a["x"], a["y"], a["s"] = 1430, 730, 1.4
        if who == "shatta": a["x"], a["y"], a["s"] = 1180, 690, 1.35
        if who == "zalata": a["x"], a["y"], a["s"] = 1300, 700, 1.35
    if sh.get("hidden"):
        a["x"], a["y"], a["s"] = HIDE[who]; a["look"] = -1; a["expr"] = "scared"; a["arms"] = "down"; a["held"] = None
    if tt >= FAHOUT[1] and not sh.get("hidden"):
        a["x"], a["y"], a["s"] = POS[who]; a["lean"] = 0; a["walk"] = None; a["look"] = 0; a["expr"] = "neutral"
        a["arms"] = "down"; a["held"] = "notebook" if who == "zalata" else ("paper" if who == "shatta" else None)
    if tt >= NANA_IN: a["expr"] = "shock"; a["look"] = -1; a["arms"] = "scared"
    if who == "zalata" and tt >= L11_T and not sh.get("hidden"): a["held"] = "notebook"
    return a

def actors(tt, sh):
    A = [kid_state(w, tt, sh) for w in KIDS]
    if FAH[0] <= tt < FAHOUT[1]:
        if tt < FAH[1]:
            k = (tt - FAH[0]) / (FAH[1] - FAH[0]); x, y, s = lerp(DOOR[0], 900, ease(k)), lerp(690, 770, ease(k)), lerp(1.25, 1.5, ease(k)); wk = tt * 6
        elif tt < FAHOUT[0]: x, y, s, wk = 900, 770, 1.5, None
        else:
            k = (tt - FAHOUT[0]) / (FAHOUT[1] - FAHOUT[0]); x, y, s = lerp(900, DOOR[0], ease(k)), lerp(770, 690, ease(k)), lerp(1.5, 1.25, ease(k)); wk = tt * 6
        A.append(dict(who="fahmy", x=x, y=y, s=s, look=1 if tt < FAHOUT[0] else -1, held="phone", arms="hold", expr="smug", walk=wk))
    if tt >= NANA_IN:
        k = min(1, (tt - NANA_IN) / 1.2)
        held = "slipper" if tt < DROP else None
        A.append(dict(who="nana", x=lerp(DOOR[0], 330, ease(k)), y=lerp(690, 760, ease(k)), s=lerp(1.4, 1.6, ease(k)), look=1,
                      held=held, arms="up" if tt < NB[0] else "down", expr="angry" if tt < NB[0] else "sad",
                      walk=tt * 6 if k < 1 else None))
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

def draw_scene_chars(tt, cam, sh):
    x0, y0, z = cam
    layer = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(layer)
    lights = []
    k, lt = line_at(tt)
    acts = [] if sh.get("hook") else sorted(actors(tt, sh), key=lambda a: a["s"])
    if sh.get("edge"): acts = [a for a in acts if a["who"] == "shatta"]
    for a in acts:
        who = a["who"]; talking = k is not None and WHO[k] == who
        expr = a.get("expr", "neutral")
        if talking: expr = expr_of(k, lt)
        mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
        arms = a.get("arms", "down")
        if talking and not sh.get("hidden"): arms = ARMS.get(k, "talk" if arms == "down" else arms)
        if who == "fahmy": arms = "hold"
        if who == "nana" and a.get("held") == "slipper": arms = "up"
        bob = abs(math.sin(a["walk"])) * 5 * a["s"] if a.get("walk") is not None else 0
        wy = a["y"] - jump_off(who, tt) - bob
        shiver = math.sin(tt * 60) * 2.5 if expr in ("scared", "shock") and who in KIDS else 0
        blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11
        X = (a["x"] + shiver - x0) * z; Y = (wy - y0) * z; s = a["s"] * z
        p.ell(X, (a["y"] - y0) * z + 4 * s, 46 * s, 9 * s, (0, 0, 0, 110), None)
        draw_char(p, who, X, Y, s, expr, mouth, a.get("look", 0), blink, arms, tt, a.get("held"),
                  a.get("lean", 0), a.get("walk"))
        S = s * CH[who]["scale"]
        if who == "fahmy":
            lights.append((X + 46 * S, Y - 120 * S, 230 * z, 1.0, (0.75, 0.9, 1.25)))
        if who == "nana" and DROP <= tt < DROP + 0.6:   # slipper falling
            u = tt - DROP; sx_, sy_ = X + 72 * S, Y - 186 * S + 1600 * u * u * z
            if sy_ < Y: p.ell(sx_, sy_, 9 * S, 18 * S, (60, 140, 200, 255), INK, 2 * S)
    return layer, lights

def tint_layer(layer, tint, lvl):
    rgb = layer.convert("RGB"); al = layer.getchannel("A")
    c = tuple(int((v * 0.55 + 255 * 0.45) * min(1.0, lvl)) for v in tint)
    rgb = ImageChops.multiply(rgb, Image.new("RGB", rgb.size, c))
    out = rgb.convert("RGBA"); out.putalpha(al); return out

LW, LH = W // 8, H // 8
gy, gx = np.mgrid[0:LH, 0:LW] * 8.0
def glow(X, Y, R): return np.exp(-((gx - X) ** 2 + (gy - Y) ** 2) / (R * R))

def light_map(sh, tt, cam, lights):
    x0, y0, z = cam
    m = np.full((LH, LW, 3), 0.55, np.float32) * np.array([0.8, 0.88, 1.05], np.float32)
    W3 = lambda px, py: ((px - x0) * z, (py - y0) * z)
    door_on = 0.55
    if DOORC <= tt < DOORC + 0.9 or NANA_IN <= tt < NANA_IN + 1.5: door_on = 1.1 + 0.2 * math.sin(tt * 40)
    X, Y = W3(216, 240); m += door_on * glow(X, Y, 380 * z)[..., None] * np.array([1.0, 0.8, 0.5], np.float32)
    X, Y = W3(1500, 50); m += 0.35 * glow(X, Y, 500 * z)[..., None] * np.array([0.8, 0.9, 1.1], np.float32)
    for k_ in HEAVY:
        if 0 <= tt - k_ < 0.5:
            X, Y = W3(VENT[0], VENT[1]); m += 1.4 * (1 - (tt - k_) / 0.5) * glow(X, Y, 300 * z)[..., None] * np.array([1.0, 0.15, 0.1], np.float32)
    for X, Y, R, inten, col in lights:
        m += inten * glow(X, Y, R)[..., None] * np.array(col, np.float32)
    mm = np.clip(m / 1.4, 0, 1)
    return Image.fromarray((mm * 255).astype(np.uint8), "RGB").resize((W, H), Image.BILINEAR)

def bg_frame(cam):
    x0, y0, z = cam; sw, sh = SRC.size; f = sw / W; src = SRC
    box = (x0 * f, y0 * f, (x0 + W / z) * f, (y0 + H / z) * f)
    if z > 1.5:
        b = tuple(int(v) for v in box); b = (max(0, b[0] - 20), max(0, b[1] - 20), min(sw, b[2] + 20), min(sh, b[3] + 20))
        part = src.crop(b).filter(ImageFilter.GaussianBlur(min(4, (z - 1.4) * 1.6)))
        box = (box[0] - b[0], box[1] - b[1], box[2] - b[0], box[3] - b[1]); src = part
    return src.resize((SSW, SSH), Image.BICUBIC, box=box)

def draw_page(img, tt, cam):
    if not (PAGE[0] <= tt < CATCH): return
    x0, y0, z = cam; S = SS * z
    k = min(1, (tt - PAGE[0]) / (PAGE[1] - PAGE[0]))
    if k < 1: wx, wy = lerp(1400, 1290, ease(k)), lerp(880, 560, k) - math.sin(k * math.pi) * 160
    else: wx, wy = 1290 + math.sin(tt * 7) * 18, 560 + math.sin(tt * 5) * 10
    ang = tt * 7; w_, h_ = 34, 44
    pts = [(-w_, -h_), (w_, -h_ * 0.8), (w_, h_), (-w_, h_ * 0.9)]
    ca, sa = math.cos(ang), math.sin(ang) * 0.5
    poly = [((wx + px * ca - py * sa - x0) * S, (wy + px * sa + py * ca - y0) * S) for px, py in pts]
    d = ImageDraw.Draw(img); d.polygon(poly, fill=(245, 242, 228), outline=(40, 40, 40))

def draw_wind(fr, tt):
    if not GUST <= tt < GUST + 1.6: return
    d = ImageDraw.Draw(fr, "RGBA"); u = tt - GUST
    for i in range(14):
        y = 120 + i * 65 + math.sin(i * 3.1) * 20; x = ((u * 2400 + i * 260) % (W + 600)) - 300
        d.line([(x, y), (x + 220, y - 8)], fill=(220, 230, 255, int(90 * (1 - u / 1.6))), width=3)

def led_bg(img, tt, cam):
    x0, y0, z = cam
    if int(tt * 2) % 2: return
    X, Y = (1040 - x0) * z * SS, (600 - y0) * z * SS
    g = Image.new("L", img.size, 0); ImageDraw.Draw(g).ellipse([X - 26 * z * SS, Y - 26 * z * SS, X + 26 * z * SS, Y + 26 * z * SS], fill=170)
    img.paste(Image.new("RGB", img.size, (255, 40, 30)), (0, 0), g.filter(ImageFilter.GaussianBlur(10 * z * SS)))
    ImageDraw.Draw(img).ellipse([X - 5 * z * SS, Y - 5 * z * SS, X + 5 * z * SS, Y + 5 * z * SS], fill=(255, 80, 60))

def draw_vent_led(fr, tt, cam):
    x0, y0, z = cam
    if int(tt * 2) % 2: return
    X, Y = (1040 - x0) * z, (600 - y0) * z
    g = Image.new("L", (W, H), 0); ImageDraw.Draw(g).ellipse([X - 22 * z, Y - 22 * z, X + 22 * z, Y + 22 * z], fill=140)
    fr.paste(Image.new("RGB", (W, H), (255, 40, 30)), (0, 0), g.filter(ImageFilter.GaussianBlur(9 * z)))
    ImageDraw.Draw(fr).ellipse([X - 4 * z, Y - 4 * z, X + 4 * z, Y + 4 * z], fill=(255, 60, 40))

# ---------------- HUD ----------------
def ltr(img, x, y, s, size, fill, stroke=(10, 10, 10), sw=4):
    ImageDraw.Draw(img).text((x, y), s, font=ImageFont.truetype(FONT, size), fill=fill, anchor="mm",
                             direction="ltr", stroke_width=sw, stroke_fill=stroke)

def morse_strip(fr, tt, taps, groups, y=90, scale=1.0, cx=W / 2, letters=None):
    d = ImageDraw.Draw(fr, "RGBA")
    n = sum(1 for tp, _ in taps if tt >= tp)
    widths = [26 if k_ == "dot" else 54 for _, k_ in taps]
    total = sum(widths) * scale + 18 * scale * (len(taps) - 1) + 40 * scale * (len(groups) - 1)
    x = cx - total / 2
    d.rounded_rectangle([x - 34 * scale, y - 48 * scale, x + total + 34 * scale, y + 48 * scale], int(22 * scale),
                        fill=(10, 10, 20, 210), outline=(255, 214, 90, 255), width=3)
    i = 0; centers = []
    for gi, gsz in enumerate(groups):
        gx0 = x
        for j in range(gsz):
            wdt = widths[i] * scale; col = (255, 214, 90, 255) if i < n else (90, 90, 100, 160)
            if taps[i][1] == "dot": d.ellipse([x, y - 13 * scale, x + wdt, y + 13 * scale], fill=col)
            else: d.rounded_rectangle([x, y - 10 * scale, x + wdt, y + 10 * scale], int(8 * scale), fill=col)
            x += wdt + 18 * scale; i += 1
        centers.append((gx0 + x - 18 * scale) / 2)
        x += 40 * scale
    if letters:
        for c_, L_ in zip(centers, letters):
            ltr(fr, c_, y + 95 * scale, L_, int(70 * scale), (255, 90, 70) if L_ != "?" else (200, 200, 210), (20, 0, 0), 5)

def decode_table(fr, x, y, scale=1.0):
    d = ImageDraw.Draw(fr, "RGBA")
    rows = [("N", "-."), ("A", ".-"), ("E", "."), ("T", "-"), ("S", "..."), ("O", "---")]
    d.rounded_rectangle([x, y, x + 300 * scale, y + 330 * scale], int(18 * scale), fill=(12, 12, 22, 220), outline=(255, 214, 90, 255), width=3)
    text(fr, x + 150 * scale, y + 30 * scale, "جدول المورس", int(30 * scale), (255, 214, 90))
    for i, (L_, c_) in enumerate(rows):
        yy_ = y + 80 * scale + i * 42 * scale
        ltr(fr, x + 60 * scale, yy_, L_, int(34 * scale), (240, 240, 240), (0, 0, 0), 2)
        xx_ = x + 120 * scale
        for ch in c_:
            if ch == ".": d.ellipse([xx_, yy_ - 8 * scale, xx_ + 16 * scale, yy_ + 8 * scale], fill=(255, 214, 90)); xx_ += 28 * scale
            else: d.rounded_rectangle([xx_, yy_ - 6 * scale, xx_ + 40 * scale, yy_ + 6 * scale], 4, fill=(255, 214, 90)); xx_ += 52 * scale

def kinds_hud(fr, tt, scale=1.0, y=150, cx=W / 2):
    if not L03_T + 0.3 <= tt < L03_T + DUR["L03"] + 0.1: return
    d = ImageDraw.Draw(fr, "RGBA")
    for i, (lab, col) in enumerate((("تقيل = سماعة", (255, 80, 70)), ("خفيف = إيد", (120, 220, 255)))):
        if tt < L03_T + 0.3 + i * DUR["L03"] * 0.5: continue
        x = cx + (-300 if i == 0 else 300) * scale
        d.rounded_rectangle([x - 260 * scale, y - 55 * scale, x + 260 * scale, y + 55 * scale], int(22 * scale), fill=(12, 12, 22, 215), outline=col + (255,), width=4)
        text(fr, x, y, lab, int(46 * scale), col)

def hud(fr, tt, sh, v=False):
    sc = 0.8 if v else 1.0; cx = 540 if v else W / 2
    if tt < TAPS1[-1][0] + 1.0 and tt >= TAPS1[0][0] - 0.05:
        morse_strip(fr, tt, TAPS1, [2, 2], y=(480 if v else 90), scale=sc, cx=cx)
    if TAPS2[0][0] - 0.05 <= tt < PUZ_END + 6 and tt < NANA_IN:
        letters = None
        if tt >= PUZ: letters = ["N", "A", "?", "?"]
        if tt >= L13_T:
            n_ = min(4, int((tt - L13_T) / (DUR["L13"] * 0.17)) + 1); letters = ["N", "A", "N", "A"][:n_] + ["?"] * (4 - n_)
        morse_strip(fr, tt, TAPS2, [2, 2, 2, 2], y=(480 if v else 90), scale=sc, cx=cx, letters=letters)
    if sh.get("decode") and not v: decode_table(fr, 40, 260)
    kinds_hud(fr, tt, sc, y=(1700 if v else 300), cx=cx)
    if L02_T + 1.5 <= tt < L02_T + DUR["L02"]:
        d = ImageDraw.Draw(fr, "RGBA"); y = 1700 if v else 120
        d.rounded_rectangle([cx - 420 * sc, y - 50 * sc, cx + 420 * sc, y + 50 * sc], int(22 * sc), fill=(20, 60, 30, 220), outline=(120, 230, 120, 255), width=4)
        text(fr, cx, y, "إجابة امبارح: 6 سماعات ونفس اللمبة الحمرا ✓", int(38 * sc), (200, 255, 200))

def card(name, tt, sh):
    k = (tt - sh["start"]) / (sh["end"] - sh["start"])
    fr = Image.new("RGB", (W, H), (8, 8, 12))
    g = lambda c: tuple(int(v * min(1, k * 4)) for v in c)
    if name == "title":
        text(fr, W / 2, H / 2 - 80, "عمارة نعناعة", 110, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 + 50, "سر الدور السابع", 64, g((230, 230, 230)))
        text(fr, W / 2, H / 2 + 145, "الحلقة 6: رسالة بالخبط", 48, g((210, 210, 210)))
    elif name == "endcard":
        text(fr, W / 2, H / 2 - 60, "الحلقة 7 بكرة", 104, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 + 70, "مين هو رشدي؟ اكتب في الكومنتات", 48, g((230, 230, 230)))
    elif name == "notebook":
        fr = Image.new("RGB", (W, H), (20, 18, 22)); d = ImageDraw.Draw(fr)
        sc = 1 + 0.06 * k
        x0_, y0_, x1_, y1_ = W / 2 - 560 * sc, H / 2 - 360 * sc, W / 2 + 560 * sc, H / 2 + 360 * sc
        d.rectangle([x0_, y0_, x1_, y1_], fill=(246, 242, 226))
        for i in range(9): d.line([(x0_ + 30, y0_ + 110 * sc + i * 70 * sc), (x1_ - 30, y0_ + 110 * sc + i * 70 * sc)], fill=(170, 200, 230), width=2)
        morse_strip(fr, 999, [(0, "dash"), (0, "dot"), (0, "dot"), (0, "dash")] * 2, [2, 2, 2, 2], y=H / 2 - 120 * sc, scale=1.3 * sc, cx=W / 2,
                    letters=["N", "A", "N", "A"])
        ltr(fr, W / 2, H / 2 + 200 * sc, "NANA = ?", int(90 * sc), (30, 30, 120), (246, 242, 226), 1)
        fr = Image.fromarray((np.asarray(fr, np.float32) * (np.asarray(VIG_DARK, np.float32) / 255)).astype(np.uint8))
        a = min(1, max(0, (k - 0.35) / 0.4))
        if a > 0:   # Nana's shadow falls over the page
            sh_ = Image.new("L", (W, H), 0); ImageDraw.Draw(sh_).ellipse([W * 0.55, -200, W * 1.3, H * 1.2], fill=int(170 * a))
            fr.paste(Image.new("RGB", (W, H), (5, 5, 10)), (0, 0), sh_.filter(ImageFilter.GaussianBlur(60)))
    return fr

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

def vertical(fr, tt, sh):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = ImageEnhance.Brightness(small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.35)
    bgv.paste(fr.resize((1080, 608), Image.LANCZOS), (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(255, 214, 90)); d.rectangle([0, 1168, 1080, 1171], fill=(255, 214, 90))
    text(bgv, 540, 260, "سر الدور السابع", 92, (255, 214, 90), (40, 10, 10), 6)
    text(bgv, 540, 375, "الحلقة 6: رسالة بالخبط", 52, (235, 235, 235))
    k, _ = line_at(tt)
    if k:
        for i, l in enumerate(wrap(SUB[k])[:4]): text(bgv, 540, 1290 + i * 80, l, 60, sw=6)
    if sh["set"] == "roof": hud(bgv, tt, sh, v=True)
    if PUZ <= tt < PUZ_END:
        d.rounded_rectangle([40, 1640, 1040, 1800], 26, fill=(20, 20, 30), outline=(255, 214, 90), width=5)
        text(bgv, 540, 1695, "لغز الحلقة: كمّل فك الشفرة!", 50, (255, 214, 90))
        text(bgv, 540, 1758, "اكتب الكلمة في الكومنتات", 42)
    return bgv

def finish(fr, tt, dark=False):
    fr = ImageChops.multiply(fr, VIG_DARK if dark else VIG)
    a = np.asarray(fr, np.float32)
    g = GRAIN[int(tt * FPS) % len(GRAIN)]
    g = np.repeat(np.repeat(g, 2, 0), 2, 1)[..., None]
    return Image.fromarray(np.clip(a + g, 0, 255).astype(np.uint8))

def frame(tt):
    sh = shot_at(tt); set_ = sh["set"]
    if set_ in ("title", "endcard", "notebook"): return finish(card(set_, tt, sh), tt), sh
    if set_ == "black": return Image.new("RGB", (W, H), (0, 0, 0)), sh
    cam = cam_at(sh, tt)
    img = bg_frame(cam)
    draw_page(img, tt, cam)
    led_bg(img, tt, cam)
    layer, lights = draw_scene_chars(tt, cam, sh)
    layer = tint_layer(layer, TINT, 0.95)
    img.paste(layer, (0, 0), layer)
    fr = img.resize((W, H), Image.LANCZOS)
    fr = ImageChops.multiply(fr, light_map(sh, tt, cam, lights)); fr = ImageEnhance.Brightness(fr).enhance(1.55)
    draw_wind(fr, tt)
    if sh.get("edge"):   # vertigo: drifting city below
        d = ImageDraw.Draw(fr, "RGBA")
        d.rectangle([0, 0, W, H], outline=(255, 60, 50, int(80 + 60 * math.sin(tt * 12))), width=14)
    return finish(fr, tt, sh.get("dark")), sh

def render(out_h, out_v, stills=None):
    fh = fv = None
    if not stills:
        mk = lambda w, h, o: subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}",
                                   "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "19",
                                   "-pix_fmt", "yuv420p", o], stdin=subprocess.PIPE)
        fh = mk(W, H, out_h); fv = mk(1080, 1920, out_v)
    times = stills or [i / FPS for i in range(int(TOTAL * FPS))]
    for i, tt in enumerate(times):
        base, sh = frame(tt)
        h = base.copy()
        if sh["set"] == "roof": hud(h, tt, sh)
        if PUZ <= tt < PUZ_END:
            d = ImageDraw.Draw(h, "RGBA")
            d.rounded_rectangle([W / 2 - 560, 830, W / 2 + 560, 905], 22, fill=(20, 20, 30, 215), outline=(255, 214, 90, 255), width=4)
            text(h, W / 2, 867, "لغز الحلقة: كمّل فك الشفرة! اكتب الكلمة في الكومنتات", 34, (255, 214, 90))
        subtitle(h, tt)
        if stills:
            h.save(f"still_h_{tt:.1f}.png"); vertical(base, tt, sh).save(f"still_v_{tt:.1f}.png")
        else:
            fh.stdin.write(h.tobytes()); fv.stdin.write(vertical(base, tt, sh).tobytes())
        if i % 240 == 0: print("frame", i, flush=True)
    if fh:
        fh.stdin.close(); fv.stdin.close(); fh.wait(); fv.wait()

def build_audio(path="mix.wav"):
    buf = np.zeros(int(TOTAL * SR) + SR * 3, dtype=np.float32)
    mix_into(buf, drone(TOTAL + 1), 0, 1.0)
    r = np.random.default_rng(9)
    wn = np.convolve(r.normal(0, 1, int(SR * (TOTAL + 1))), np.ones(60) / 60, mode="same") * 0.05   # rooftop air
    mix_into(buf, wn.astype(np.float32), 0, 1.0)
    ts = np.arange(int(SR * 1.6)) / SR
    k_ = sfx_knock()
    S = {"knock": k_, "boom": sfx_boom(), **SFXF}
    S["hknock"] = k_ * 1.4 + sfx_boom()[:len(k_)] * 0.7
    tt_ = np.arange(int(SR * 0.12)) / SR
    tap = (np.sin(2 * np.pi * 420 * tt_) * np.exp(-tt_ * 60) + r.normal(0, 1, len(tt_)) * np.exp(-tt_ * 120) * 0.4) * 0.55
    S["tap"] = tap
    tl = np.arange(int(SR * 0.3)) / SR
    S["tapl"] = np.concatenate([tap, np.zeros(1, np.float32)])[:len(tl)] if False else (np.sin(2 * np.pi * 380 * tl) * np.exp(-tl * 14) * 0.5 + r.normal(0, 1, len(tl)) * np.exp(-tl * 18) * 0.15)
    S["sting"] = (np.sin(2 * np.pi * (1200 + 80 * np.sin(ts * 40)) * ts) * 0.08 + np.sin(2 * np.pi * 1263 * ts) * 0.06
                  + np.sin(2 * np.pi * 55 * ts) * 0.4) * np.exp(-ts * 1.8)
    S["thud"] = k_ * 0.5
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
        mux("h.mp4", "sirr_eldor_elsabe3_ep6.mp4"); mux("v.mp4", "sirr_eldor_elsabe3_ep6_vertical.mp4")
        print("done")
