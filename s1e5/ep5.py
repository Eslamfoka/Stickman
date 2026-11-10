import sys, os, math, subprocess, wave
sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter, ImageFont
from engine import *

os.chdir(ROOT + "/s1e5")
SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(51)
E1 = ROOT + "/s1e1/"

SUB = {
 "K01": "عفريت!",
 "K02": "دي قطة يا شطة.",
 "K03": "طب لو دي... مين اللي كان بينادي عليا؟!",
 "K04": "بصوا فوق... فيه نور أحمر صغير في فتحة التهوية!",
 "K05": "لغز امبارح: اللي قالوا قصير... إجابتكو صح! الضل كان طويل، بس صاحبه قصير.",
 "K06": "صباح الفل يا حلوين! أنا أستاذ فهمي، جاركم الجديد في الدور الخامس!",
 "K07": "الحلويات دي تحفة يا أستاذ فهمي!",
 "K08": "محدش بيسكن في العمارة دي... إلا لو وراه حاجة.",
 "K09": "ما تشغلوش بالكم يا حلوين! اطلعوا عندي، عندي حاجات حلوة كتير.",
 "K10": "ست سماعات في أوضة واحدة... أنا حاسبها: ده مش طبيعي.",
 "K11": "واللمبة الحمرا اللي في السماعة... نفس اللي شفناها في فتحة التهوية!",
 "K12": "لغز النهارده: إيه الغريب في بيت أستاذ فهمي؟ اكتبوا في الكومنتات!",
 "K13": "أنا آسف! الكرتونة وقعت لوحدها!",
 "K14": "سيبها! ...ما تشغلوش بالكم يا حلوين.",
 "K15": "شفتوا المفتاح اللي وقع؟ مكتوب عليه سبعة... تلاتين.",
 "K16": "بس المفتاح ده مع البواب! يبقى إزاي معاه هو كمان؟!",
 "K17": "أنا عندي مفاتيح... لكل الأبواب.",
}
WHO = {"K01": "shatta", "K02": "zalata", "K03": "shatta", "K04": "tota", "K05": "tota", "K06": "fahmy",
       "K07": "shatta", "K08": "bondo2", "K09": "fahmy", "K10": "zalata", "K11": "tota", "K12": "tota",
       "K13": "shatta", "K14": "fahmy", "K15": "zalata", "K16": "shatta", "K17": "fahmy"}
EXPR = {"K01": "shock", "K02": "flat", "K03": "scared", "K04": "scared", "K05": "happy", "K06": "happy",
        "K07": "happy", "K08": "angry", "K09": [(0, "happy"), (0.6, "smug")], "K10": "flat",
        "K11": [(0, "neutral"), (0.4, "shock")], "K12": [(0, "neutral"), (0.6, "smug")], "K13": "scared",
        "K14": [(0, "shout"), (0.35, "smug")], "K15": "shock", "K16": "scared", "K17": "smug"}
ARMS = {"K01": "up", "K03": "scared", "K04": "point", "K05": "point", "K06": "hold", "K07": "hold", "K08": "hips",
        "K09": "hold", "K10": "point", "K11": "point", "K12": "point", "K13": "up", "K14": "point", "K16": "scared",
        "K17": "hold"}

AUD = {k: load_audio(f"audio/{k}.mp3") for k in SUB}
ENV = {k: envelope(v) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}
SFXF = {n: load_audio(f"sfx/{n}.mp3") for n in ("whoosh", "cat", "slam", "chips", "creak")}

lines, sfx, shots, jumps, shakes = [], [], [], {}, []
def say(t, k): lines.append((t, k)); return t + DUR[k]
def fx(t, n, g=1.0): sfx.append((t, n, g))
def jump(w, t): jumps.setdefault(w, []).append(t)
def shot(set_, s, e, c0, c1=None, **kw):
    shots.append(dict(set=set_, start=s, end=e, c0=c0, c1=c1 or c0, **kw))
def cut(t, g=0.45): fx(t - 0.12, "whoosh", g)
KIDS = ("shatta", "zalata", "tota")

POS = {
 "stairs": {"tota": (830, 1060, 2.0), "shatta": (1060, 1040, 2.0), "zalata": (1290, 1060, 2.0)},
 "bedroom": {"shatta": (620, 1030, 2.4), "zalata": (960, 1030, 2.4), "tota": (1300, 1030, 2.4)},
 "lobby": {"tota": (300, 1080, 2.2), "shatta": (530, 1070, 2.2), "zalata": (760, 1080, 2.2)},
 "fahmy": {"tota": (380, 1050, 2.1), "shatta": (610, 1045, 2.1), "zalata": (840, 1050, 2.1)},
}
FAHMY_HOME = (1360, 1045, 2.4)
def CU(set_, who, z=2.2, dx=0, pos=None):
    x, y, s = pos or POS[set_][who]; S = s * CH[who]["scale"]
    if who == "tota": z *= 1.3
    hy = y - 190 * S
    return (x + dx, hy + H / (2 * z) - 1.45 * 46 * S - 25, z)

t = 0.0
# ===== 0. HOOK: green eyes -> cat =====
CAT = 0.55; fx(CAT - 0.05, "cat", 1.2); shakes.append((CAT + 0.1, 14))
for w_ in KIDS: jump(w_, CAT + 0.1)
t = say(CAT + 0.15, "K01") + 0.05
shot("stairs", 0, t, (1000, 600, 2.1), (1060, 600, 1.3), blackout=True, ease="crash")
TORCH2 = t; fx(t, "click", 1.0)
RUNCAT = (t, t + 1.1)
s = t; t += 0.35; t = say(t, "K02") + 0.1
shot("stairs", s, t, (1060, 640, 1.15), (1060, 640, 1.22), torch=True)
s = t; t = say(t, "K03") + 0.1
shot("stairs", s, t, CU("stairs", "shatta", 2.1), CU("stairs", "shatta", 2.4), torch=True)
s = t; K04_T = t; t = say(t, "K04") + 0.25
mid = K04_T + 0.9
shot("stairs", s, mid, CU("stairs", "tota", 2.0), CU("stairs", "tota", 2.15), torch=True, up=True)
shot("stairs", mid, t, (1150, 150, 2.2), (1170, 110, 3.0), torch=True, up=True, vent=True)
fx(mid + 0.1, "sting", 1.0)
cut(t, 0.6); fx(t, "boom", 0.7); shot("title", t, t + 1.6, None); t += 1.6
# ===== 1. MORNING answer =====
cut(t, 0.4); s = t; t += 0.15
K05_T = t; t = say(t, "K05") + 0.15
shot("bedroom", s, t, CU("bedroom", "tota", 1.9), CU("bedroom", "tota", 2.25))
# ===== 2. LOBBY: Fahmy arrives =====
cut(t, 0.45)
ARRIVE = (t, t + 2.2); fx(t + 0.1, "steps_f", 1.0)
shot("lobby", t, t + 2.2, (960, 640, 1.05), (1060, 660, 1.15))
t += 2.2; s = t
t = say(t, "K06") + 0.1
shot("lobby", s, t, CU("lobby", "fahmy", 2.0, pos=(1250, 1070, 2.4)), CU("lobby", "fahmy", 2.3, pos=(1250, 1070, 2.4)))
FREEZE = (t, t + 1.3); fx(t, "sting", 1.0); fx(t, "shutter", 1.0)
shot("lobby", t, t + 1.3, (1000, 660, 1.2), (1000, 660, 1.24), freeze=True); t += 1.3
s = t; t = say(t, "K07") + 0.1
CHEW = (s, t)
shot("lobby", s, t, CU("lobby", "shatta", 2.1), CU("lobby", "shatta", 2.3))
BONDO_IN = t - 0.6; fx(BONDO_IN, "steps_b", 0.8)
s = t; t = say(t, "K08") + 0.15
shot("lobby", s, t, CU("lobby", "bondo2", 2.0, pos=(250, 1080, 2.3)), CU("lobby", "bondo2", 2.2, pos=(250, 1080, 2.3)))
s = t; t = say(t, "K09") + 0.15
shot("lobby", s, t, (1050, 640, 1.2), (1150, 620, 1.45))
# ===== 3. FAHMY'S APARTMENT =====
cut(t, 0.6); APT0 = t; fx(t, "door", 0.8)
shot("fahmy", t, t + 1.4, (960, 540, 1.0), (980, 520, 1.08)); t += 1.4
s = t; K10_T = t; t = say(t, "K10") + 0.15
shot("fahmy", s, t, (1110, 420, 1.55), (1160, 410, 1.7), count=True)
COUNT = [K10_T + 0.1 + i * 0.32 for i in range(6)]
for c_ in COUNT: fx(c_, "tick", 1.2)
s = t; K11_T = t; t = say(t, "K11") + 0.15
mid = K11_T + DUR["K11"] * 0.35
shot("fahmy", s, mid, CU("fahmy", "tota", 2.0), CU("fahmy", "tota", 2.2))
shot("fahmy", mid, t, (1050, 290, 3.0), (1050, 280, 3.6), led=True)
fx(mid, "sting", 0.8)
PUZ = t; s = t; t = say(t, "K12") + 0.6; PUZ_END = t
shot("fahmy", s, t, CU("fahmy", "tota", 2.3), CU("fahmy", "tota", 2.6))
BUMP = t + 0.5; fx(BUMP, "slam", 1.2); fx(BUMP + 0.12, "keys", 1.2); shakes.append((BUMP, 14))
for w_ in KIDS + ("fahmy",): jump(w_, BUMP + 0.02)
shot("fahmy", t, t + 1.5, (960, 640, 1.1), (900, 700, 1.3)); t += 1.5
s = t; t = say(t, "K13") + 0.05
shot("fahmy", s, t, CU("fahmy", "shatta", 2.1), CU("fahmy", "shatta", 2.3))
s = t; GRAB = t + 0.15; t = say(t, "K14") + 0.15
shot("fahmy", s, t, CU("fahmy", "fahmy", 1.6, pos=FAHMY_HOME), CU("fahmy", "fahmy", 2.6, pos=(1200, 1045, 2.4)), ease="crash")
fx(GRAB, "whoosh", 0.8)
s = t; t = say(t, "K15") + 0.2
shot("keycard", s, t, None)
s = t; t = say(t, "K16") + 0.15
shot("fahmy", s, t, CU("fahmy", "shatta", 2.2), CU("fahmy", "shatta", 2.6))
APP0 = t; APP1 = t + 2.0; fx(t, "steps_f", 1.2)
shot("fahmy", t, APP1 + 0.1, (960, 560, 1.0), (960, 540, 1.06), red=True)
t = APP1 + 0.1; t = say(t, "K17") + 0.2
shot("fahmy", APP1 + 0.1, t, (960, 540, 1.06), (960, 520, 1.15), red=True, dark=True)
KN = [t + i * 0.45 for i in range(3)]
for k_ in KN: fx(k_, "knock", 1.2); shakes.append((k_, 12))
t = KN[-1] + 0.6
shot("fahmy", KN[0], t, (960, 520, 1.15), (960, 500, 1.2), red=True, dark=True, flash=True)
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
contacts(ARRIVE[0], ARRIVE[1], 7, 0.4, 0.8, True)
contacts(BONDO_IN, BONDO_IN + 1.0, 7, 0.6, 0.6)
contacts(APP0, APP1, 5, 0.6, 1.6, True)

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
_lob = Image.open(E1 + "bg/lobby_1080.png").convert("RGB")
def _lamp_off(img):
    sw, sh_ = img.size; f = sw / W
    Y, X = np.mgrid[0:sh_, 0:sw]
    g = np.exp(-(((X - 471 * f) / (230 * f)) ** 2 + ((Y - 260 * f) / (300 * f)) ** 2))
    g2 = np.exp(-(((X - 471 * f) / (40 * f)) ** 2 + ((Y - 201 * f) / (40 * f)) ** 2))
    a = np.asarray(img, np.float32) * (1 - 0.55 * g - 0.4 * g2)[..., None] * 0.8
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
SRCBG = {"bedroom": ImageChops.multiply(ImageEnhance.Brightness(_bed).enhance(1.55), Image.new("RGB", _bed.size, (255, 236, 205))),
         "stairs": _lamp_off(Image.open(E1 + "bg/stairs_1080.png").convert("RGB")),
         "lobby": ImageChops.multiply(ImageEnhance.Brightness(_lob).enhance(1.7), Image.new("RGB", _lob.size, (255, 238, 210))),
         "fahmy": Image.open("bg/fahmy_raw.png").convert("RGB")}
TINT = {"bedroom": (255, 240, 225), "stairs": (175, 185, 235), "lobby": (255, 245, 230), "fahmy": (255, 225, 190)}
yy, xx = np.mgrid[0:H, 0:W]
vg = 1 - 0.55 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) ** 1.2
VIG = Image.fromarray((np.clip(vg, 0.25, 1) * 255).astype(np.uint8)).convert("RGB")
vg2 = np.clip(1 - 0.9 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2), 0.12, 1)
VIG_DARK = Image.fromarray((vg2 * 255).astype(np.uint8)).convert("RGB")
GRAIN = [np.random.default_rng(i).normal(0, 5.0, (H // 2, W // 2)).astype(np.float32) for i in range(6)]
LEDS = [(700, 330), (800, 505), (1050, 265), (1150, 385), (1370, 520), (1510, 355)]
VENT = (1170, 95)

def cam_at(sh, tt):
    k = ease((tt - sh["start"]) / max(0.01, sh["end"] - sh["start"]), sh.get("ease"))
    c = [a + (b - a) * k for a, b in zip(sh["c0"], sh["c1"])]
    if sh.get("freeze"): c = list(sh["c0"])
    shake = 0
    for st, amp in shakes:
        if 0 <= tt - st < 0.4: shake = max(shake, amp * (1 - (tt - st) / 0.4))
    cx, cy, z = c; cw, ch = W / z, H / z
    if sh["set"] != "bedroom" and not sh.get("freeze"):
        cx += math.sin(tt * 0.9) * 6 + math.sin(tt * 2.3) * 2.5; cy += math.sin(tt * 1.3 + 1) * 4
    x0 = min(max(cx - cw / 2, 0), W - cw); y0 = min(max(cy - ch / 2, 0), H - ch)
    if shake:
        x0 = min(max(x0 + rng.normal(0, shake / z), 0), W - cw); y0 = min(max(y0 + rng.normal(0, shake / z), 0), H - ch)
    return x0, y0, z

# ---------------- actors ----------------
def fahmy_state(set_, tt):
    if set_ == "lobby":
        if tt < ARRIVE[0]: return None
        k = min(1, (tt - ARRIVE[0]) / (ARRIVE[1] - ARRIVE[0]))
        x, y, s = lerp(980, 1250, ease(k)), lerp(720, 1070, ease(k)), lerp(1.5, 2.4, ease(k))
        return dict(x=x, y=y, s=s, look=-1, held="tray", arms="hold", walk=tt * 7 if k < 1 else None,
                    expr="happy" if tt < FREEZE[0] else "smug")
    if set_ == "fahmy":
        x, y, s = FAHMY_HOME
        a = dict(x=x, y=y, s=s, look=-1, held="tray", arms="hold", expr="smug")
        if tt >= BUMP: a["held"] = None; a["expr"] = "shock"
        if tt >= GRAB - 0.1:
            k = min(1, (tt - GRAB + 0.1) / 0.35); a["x"] = lerp(x, 1200, ease(k)); a["held"] = "keys"; a["expr"] = "angry"
        if tt >= GRAB + 0.9: a["expr"] = "smug"
        if tt >= APP0:
            k = ease(min(1, (tt - APP0) / (APP1 - APP0)))
            a["x"] = lerp(1200, 960, k); a["y"] = lerp(1045, 1950, k); a["s"] = lerp(2.4, 9.0, k ** 1.3)
            a["walk"] = (tt - APP0) * 5 if tt < APP1 else None; a["look"] = 0; a["expr"] = "smug"; a["held"] = "keys"
        return a
    return None

def actors(set_, tt, sh):
    A = []
    if set_ in POS:
        for who, (x, y, s) in POS[set_].items():
            a = dict(who=who, x=x, y=y, s=s, look=0, expr="neutral")
            if set_ == "stairs":
                a["expr"] = "scared"
                if who == "tota": a["held"] = "torch"; a["arms"] = "point" if sh.get("up") else "hold"
                else: a["arms"] = "scared"
            if set_ == "bedroom":
                a["look"] = {"shatta": 1, "zalata": 0, "tota": -1}[who]
                if who == "zalata": a["held"] = "notebook"
            if set_ == "lobby":
                a["look"] = 1
                if who == "shatta" and tt >= ARRIVE[1]: a["held"] = "sweet"; a["arms"] = "hold"
                if who == "zalata": a["held"] = "notebook"
                if who == "tota" and tt >= FREEZE[0]: a["expr"] = "smug"
            if set_ == "fahmy":
                a["look"] = 1
                if who == "zalata": a["held"] = "notebook"
                if tt >= BUMP: a["expr"] = "scared"
                if tt >= APP0: a["expr"] = "shock"; a["arms"] = "scared"
                if who == "shatta" and BUMP - 0.4 <= tt < BUMP + 0.2: a["lean"] = 1.0; a["arms"] = "point"
            A.append(a)
    f = fahmy_state(set_, tt)
    if f: f["who"] = "fahmy"; A.append(f)
    if set_ == "lobby" and tt >= BONDO_IN:
        k = min(1, (tt - BONDO_IN) / 1.0)
        A.append(dict(who="bondo2", x=lerp(-160, 90, ease(k)), y=1080, s=2.3, look=1, expr="angry",
                      walk=tt * 7 if k < 1 else None, arms="hips"))
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

def draw_scene_chars(set_, tt, cam, sh):
    x0, y0, z = cam
    layer = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(layer)
    hand = None
    k, lt = line_at(tt)
    for a in sorted(actors(set_, tt, sh), key=lambda a: a["s"]):
        who = a["who"]; talking = k is not None and WHO[k] == who
        expr = a.get("expr", "neutral")
        if talking: expr = expr_of(k, lt)
        mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
        if who == "shatta" and CHEW[0] <= tt < CHEW[1]: mouth = max(mouth * 0.7, 0.22 * abs(math.sin(tt * 13)))
        arms = a.get("arms", "down")
        if talking: arms = ARMS.get(k, "talk" if arms == "down" else arms)
        if talking and a.get("held") in ("torch", "tray", "sweet") and arms not in ("point",): arms = "hold"
        if talking and who == "tota" and a.get("held") == "torch": arms = "point" if sh.get("up") else "hold"
        bob = abs(math.sin(a["walk"])) * 5 * a["s"] if a.get("walk") is not None else 0
        wy = a["y"] - jump_off(who, tt) - bob
        shiver = math.sin(tt * 60) * 2.5 if expr in ("scared", "shock") and who not in ("bondo2", "fahmy") else 0
        blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11
        X = (a["x"] + shiver - x0) * z; Y = (wy - y0) * z; s = a["s"] * z
        p.ell(X, (a["y"] - y0) * z + 4 * s, 46 * s, 9 * s, (0, 0, 0, 110), None)
        draw_char(p, who, X, Y, s, expr, mouth, a.get("look", 0), blink, arms, tt, a.get("held"),
                  a.get("lean", 0), a.get("walk"))
        if who == "tota" and a.get("held") == "torch":
            S = s * CH[who]["scale"]
            hand = (X + (84 if arms == "point" else 46) * S, Y - (140 if arms == "point" else 104) * S)
    return layer, hand

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
    if sh.get("up"): wx, wy, r = VENT[0], VENT[1] + 60, 300
    elif tt < RUNCAT[1]:
        k = (tt - RUNCAT[0]) / (RUNCAT[1] - RUNCAT[0]); wx, wy, r = lerp(1000, 1800, k), 1030, 330
    else: wx, wy, r = 1060 + math.sin(tt * 1.7) * 40, 760, 380
    return (wx - x0) * z, (wy - y0) * z, r * z

def light_map_stairs(sh, tt, cam, hand):
    m = np.full((LH, LW, 3), 0.16, np.float32) * np.array([0.85, 0.9, 1.0], np.float32)
    spot = None
    if hand:
        tx, ty, R = torch_target(sh, tt, cam, hand)
        spot = glow(tx, ty, R)
        m += 2.3 * spot[..., None] * np.array([1.0, 0.97, 0.85], np.float32)
        m += 0.4 * glow(hand[0], hand[1], 260 * cam[2])[..., None] * np.array([1.0, 0.95, 0.85], np.float32)
    mm = np.clip(m / 1.5, 0, 1)
    return Image.fromarray((mm * 255).astype(np.uint8), "RGB").resize((W, H), Image.BILINEAR), spot

DUST = rng.uniform(-1, 1, (40, 3))
def draw_beam(fr, sh, tt, cam, hand):
    if not hand: return
    tx, ty, R = torch_target(sh, tt, cam, hand)
    ov = Image.new("L", (W // 2, H // 2), 0); d = ImageDraw.Draw(ov)
    hx, hy = hand[0] / 2, hand[1] / 2; ang = math.atan2(ty - hand[1], tx - hand[0]); w_ = R * 0.6 / 2
    px, py = -math.sin(ang) * w_, math.cos(ang) * w_
    d.polygon([(hx, hy), (tx / 2 + px, ty / 2 + py), (tx / 2 - px, ty / 2 - py)], fill=46)
    ov = ov.filter(ImageFilter.GaussianBlur(14)).resize((W, H), Image.BILINEAR)
    fr.paste(Image.new("RGB", (W, H), (255, 248, 220)), (0, 0), ov)
    dd = ImageDraw.Draw(fr, "RGBA")
    for i, (a, b, c) in enumerate(DUST):
        u = (a * 0.5 + 0.5 + tt * 0.03 * (1 + c)) % 1
        qx = hand[0] + (tx - hand[0]) * u + px * 2 * b * u; qy = hand[1] + (ty - hand[1]) * u + py * 2 * b * u
        r = 1.2 + abs(c) * 1.8
        dd.ellipse([qx - r, qy - r, qx + r, qy + r], fill=(255, 245, 210, int(110 * u)))

def draw_cat_shape(d, X, Y, sc, col, eyes=True, blinkk=1.0):
    S = sc
    d.ellipse([X - 55 * S, Y - 30 * S, X + 55 * S, Y + 30 * S], fill=col)
    d.ellipse([X + 30 * S, Y - 58 * S, X + 86 * S, Y - 4 * S], fill=col)
    d.polygon([(X + 34 * S, Y - 44 * S), (X + 40 * S, Y - 80 * S), (X + 56 * S, Y - 50 * S)], fill=col)
    d.polygon([(X + 62 * S, Y - 50 * S), (X + 78 * S, Y - 80 * S), (X + 84 * S, Y - 44 * S)], fill=col)
    d.line([(X - 52 * S, Y - 4 * S), (X - 96 * S, Y - 52 * S)], fill=col, width=max(2, int(10 * S)))
    for lx in (-35, -12, 18, 40):
        d.line([(X + lx * S, Y + 20 * S), (X + (lx + 6) * S, Y + 52 * S)], fill=col, width=max(2, int(9 * S)))
    if eyes:
        for ex in (50, 68):
            d.ellipse([X + (ex - 6) * S, Y - 36 * S, X + (ex + 6) * S, Y - (36 - 12 * blinkk) * S], fill=(200, 230, 90))

def eyes_only(sh, tt, cam):
    x0, y0, z = cam
    img = Image.new("RGBA", (SSW, SSH), (3, 3, 6, 255)); p = P(img)
    for a in actors("stairs", tt, sh):
        if a["who"] not in KIDS: continue
        X, hy, S = head_screen(a, x0, y0, z, tt)
        big = True; er = 12 * S; ey = hy + 2 * S
        look = 1.0 if tt < CAT else math.sin(tt * 9) * 0.8
        for sx in (-1, 1):
            ex = X + sx * 15 * S
            p.ell(ex, ey, er * 0.82, er, (238, 238, 238, 255), None)
            p.ell(ex + look * 4 * S, ey + 1.5 * S, 2.6 * S, 2.6 * S, (5, 5, 5, 255), None)
    fr = img.convert("RGB").resize((W, H), Image.LANCZOS)
    d = ImageDraw.Draw(fr)
    X, hy, S = head_screen(dict(who="shatta", x=935, y=930, s=2.0), x0, y0, z, tt)
    X /= 1.0; hy /= 1.0
    if tt < CAT:
        for sx in (-1, 1):
            ex = X + sx * 20 * S; d.ellipse([ex - 13 * S, hy - 9 * S, ex + 13 * S, hy + 9 * S], fill=(200, 230, 90))
            d.ellipse([ex - 2.5 * S, hy - 8 * S, ex + 2.5 * S, hy + 8 * S], fill=(10, 10, 5))
    else:
        k = min(1, (tt - CAT) / 0.45)
        if k < 1:   # leaps at the camera
            sc = (1 + 9 * k * k) * S / 1.6
            draw_cat_shape(d, lerp(X, W * 0.55, k) - 40 * sc, lerp(hy, H * 0.6, k) + 40 * sc, sc, (34, 34, 42))
        else:
            fr = Image.new("RGB", (W, H), (34, 34, 42)) if tt < CAT + 0.55 else fr
    return fr

def draw_lobby_props(img, cam, tt):
    x0, y0, z = cam; d = ImageDraw.Draw(img); S = SS * z
    for bx, by, w, h in ((1500, 870, 230, 170), (1700, 900, 190, 140), (1580, 740, 170, 130), (1380, 930, 150, 110)):
        X0, Y0 = (bx - x0) * S, (by - y0) * S; Wd, Hd = w * S, h * S
        d.rectangle([X0, Y0, X0 + Wd, Y0 + Hd], fill=(176, 132, 82), outline=(60, 40, 20), width=max(2, int(3 * S)))
        d.rectangle([X0 + Wd * 0.44, Y0, X0 + Wd * 0.56, Y0 + Hd], fill=(205, 180, 120))
        d.line([(X0, Y0 + Hd * 0.18), (X0 + Wd, Y0 + Hd * 0.18)], fill=(120, 85, 50), width=max(1, int(2 * S)))

def draw_apartment_props(img, cam, tt, sh):
    x0, y0, z = cam; d = ImageDraw.Draw(img, "RGBA"); S = SS * z
    W2 = lambda px, py: ((px - x0) * S, (py - y0) * S)
    # carton next to Shatta that gets knocked over
    bx, by = 930, 1000; ang = 0.0
    if tt >= BUMP: ang = min(1, (tt - BUMP) / 0.3) * math.pi / 2 * 0.95
    w, h = 140, 120
    pts = [(0, 0), (w, 0), (w, -h), (0, -h)]
    ca, sa = math.cos(ang), math.sin(ang)
    poly = [W2(bx + px * ca - py * sa, by + px * sa + py * ca) for px, py in pts]
    d.polygon(poly, fill=(176, 132, 82, 255), outline=(60, 40, 20, 255))
    d.line([poly[0], poly[2]], fill=(205, 180, 120, 255), width=max(1, int(3 * S)))
    # keys sliding on the floor (until Fahmy grabs them)
    if BUMP + 0.1 <= tt < GRAB + 0.15:
        k = min(1, (tt - BUMP - 0.1) / 0.5)
        kx, ky = lerp(1080, 1170, 1 - (1 - k) ** 2), 1030
        X, Y = W2(kx, ky); r = 9 * S
        d.ellipse([X - r, Y - r, X + r, Y + r], outline=(225, 185, 70, 255), width=max(2, int(3 * S)))
        d.line([(X + r, Y), (X + r * 3.2, Y + r * 0.4)], fill=(225, 185, 70, 255), width=max(2, int(4 * S)))
        d.line([(X - r * 0.4, Y + r), (X - r * 1.4, Y + r * 3)], fill=(200, 200, 210, 255), width=max(2, int(4 * S)))
        if int(tt * 10) % 2: d.line([(X + r * 2, Y - r * 3), (X + r * 2, Y - r)], fill=(255, 250, 200, 220), width=max(1, int(2 * S)))

def led_glow(fr, cam, tt, sh):
    x0, y0, z = cam
    if sh["set"] == "fahmy":
        on = (int(tt * 2) % 2 == 0) or sh.get("led")
        if sh.get("flash") and any(0 <= tt - k_ < 0.25 for k_ in KN): on = True
        if not on: return fr
        gl = Image.new("L", (W, H), 0); d = ImageDraw.Draw(gl); dd = ImageDraw.Draw(fr)
        big = 2.2 if sh.get("flash") and any(0 <= tt - k_ < 0.25 for k_ in KN) else 1.0
        for lx, ly in LEDS:
            X, Y = (lx - x0) * z, (ly - y0) * z; r = 5 * z
            d.ellipse([X - 28 * z * big, Y - 28 * z * big, X + 28 * z * big, Y + 28 * z * big], fill=120)
            dd.ellipse([X - r, Y - r, X + r, Y + r], fill=(255, 40, 30))
        fr.paste(Image.new("RGB", (W, H), (255, 40, 30)), (0, 0), gl.filter(ImageFilter.GaussianBlur(14 * z)))
    if sh.get("vent"):
        X, Y = (VENT[0] - x0) * z, (VENT[1] - y0) * z
        dd = ImageDraw.Draw(fr)
        dd.rectangle([X - 70 * z, Y - 34 * z, X + 70 * z, Y + 34 * z], outline=(60, 60, 66), width=max(2, int(4 * z)))
        for i in range(6): dd.line([(X - 62 * z, Y - 26 * z + i * 10 * z), (X + 62 * z, Y - 26 * z + i * 10 * z)], fill=(40, 40, 46), width=max(1, int(3 * z)))
        if int(tt * 2.5) % 2 == 0:
            g = Image.new("L", (W, H), 0); ImageDraw.Draw(g).ellipse([X + 30 * z, Y - 6 * z, X + 70 * z, Y + 34 * z], fill=150)
            fr.paste(Image.new("RGB", (W, H), (255, 40, 30)), (0, 0), g.filter(ImageFilter.GaussianBlur(10 * z)))
            dd.ellipse([X + 45 * z, Y + 9 * z, X + 55 * z, Y + 19 * z], fill=(255, 60, 40))
    return fr

def bg_frame(set_, cam):
    x0, y0, z = cam; src = SRCBG[set_]; sw, sh = src.size; f = sw / W
    box = (x0 * f, y0 * f, (x0 + W / z) * f, (y0 + H / z) * f)
    if z > 1.5:
        b = tuple(int(v) for v in box); b = (max(0, b[0] - 20), max(0, b[1] - 20), min(sw, b[2] + 20), min(sh, b[3] + 20))
        part = src.crop(b).filter(ImageFilter.GaussianBlur(min(4, (z - 1.4) * 1.6)))
        box = (box[0] - b[0], box[1] - b[1], box[2] - b[0], box[3] - b[1]); src = part
    return src.resize((SSW, SSH), Image.BICUBIC, box=box)

# ---------------- cards / HUD ----------------
def card(name, tt, sh):
    k = (tt - sh["start"]) / (sh["end"] - sh["start"])
    fr = Image.new("RGB", (W, H), (8, 8, 12))
    g = lambda c: tuple(int(v * min(1, k * 4)) for v in c)
    if name == "title":
        text(fr, W / 2, H / 2 - 80, "عمارة نعناعة", 110, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 + 50, "سر الدور السابع", 64, g((230, 230, 230)))
        text(fr, W / 2, H / 2 + 145, "الحلقة 5: الجار الجديد", 48, g((210, 210, 210)))
    elif name == "endcard":
        text(fr, W / 2, H / 2 - 60, "الحلقة 6 بكرة", 104, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 + 70, "إيه الغريب في بيت أستاذ فهمي؟ اكتب في الكومنتات", 46, g((230, 230, 230)))
    elif name == "keycard":
        fr = Image.new("RGB", (W, H), (14, 12, 10)); L = Image.new("RGBA", (SSW, SSH)); p = P(L)
        sc = 1 + 0.08 * k; cx, cy = 960, 470; gold = (220, 178, 70, 255); dark = (120, 90, 30, 255)
        p.ell(cx - 330 * sc, cy, 110 * sc, 110 * sc, None, gold, 34 * sc)
        p.rect(cx - 230 * sc, cy - 28 * sc, cx + 420 * sc, cy + 28 * sc, gold, dark, 5 * sc)
        for i, hgt in enumerate((70, 45, 85)):
            p.rect(cx + (250 + i * 55) * sc, cy + 28 * sc, cx + (290 + i * 55) * sc, cy + (28 + hgt) * sc, gold, dark, 5 * sc)
        fr = fr.convert("RGBA"); fr.alpha_composite(L.resize((W, H), Image.LANCZOS)); fr = fr.convert("RGB")
        ImageDraw.Draw(fr).text((cx + 60 * sc, cy), "7 - 30", font=ImageFont.truetype(FONT, int(64 * sc)), fill=(90, 60, 15),
                                anchor="mm", direction="ltr", stroke_width=2, stroke_fill=(240, 210, 120))
        gx_ = cx - 200 + 700 * ((tt * 0.8) % 1)
        gl = Image.new("L", (W, H), 0); ImageDraw.Draw(gl).polygon([(gx_, 300), (gx_ + 60, 300), (gx_ - 40, 650), (gx_ - 100, 650)], fill=90)
        fr.paste(Image.new("RGB", (W, H), (255, 245, 210)), (0, 0), gl.filter(ImageFilter.GaussianBlur(12)))
        a = np.asarray(fr, np.float32) * (np.asarray(VIG_DARK, np.float32) / 255); fr = Image.fromarray(a.astype(np.uint8))
    return fr

def detective(fr, tt, cam):
    k = (tt - FREEZE[0]) / (FREEZE[1] - FREEZE[0])
    fr = ImageEnhance.Color(fr).enhance(0.15)
    fr = ImageEnhance.Contrast(fr).enhance(1.25)
    x0, y0, z = cam
    f = fahmy_state("lobby", FREEZE[0]); X, hy, S = head_screen(dict(f, who="fahmy"), x0, y0, z, FREEZE[0])
    top = hy - 60 * S; bot = (f["y"] - y0) * z
    d = ImageDraw.Draw(fr, "RGBA"); a = min(1, k * 4)
    d.ellipse([X - 170 * S / 2.4, top - 20, X + 170 * S / 2.4, bot + 20], outline=(230, 40, 40, int(255 * a)), width=8)
    s2 = POS["lobby"]["shatta"]; Xs, hys, Ss = head_screen(dict(who="shatta", x=s2[0], y=s2[1], s=s2[2]), x0, y0, z, FREEZE[0])
    if k > 0.25:
        for yv in (top, hys - 46 * Ss):
            d.line([(Xs - 40, yv), (X + 120, yv)], fill=(255, 214, 90, 230), width=4)
        text(fr, X + 230, top - 40, "قصير...؟", 64, (255, 80, 70), (20, 0, 0), 6)
    d.rectangle([0, 0, W, 14], fill=(0, 0, 0)); d.rectangle([0, H - 14, W, H], fill=(0, 0, 0))
    return fr

def count_overlay(fr, tt, cam):
    x0, y0, z = cam; d = ImageDraw.Draw(fr, "RGBA")
    for i, c_ in enumerate(COUNT):
        if tt >= c_:
            lx, ly = LEDS[i]; X, Y = (lx - x0) * z, (ly - y0) * z - 60 * z
            pop = 1 + 0.4 * max(0, 1 - (tt - c_) / 0.15)
            r = 30 * pop
            d.ellipse([X - r, Y - r, X + r, Y + r], fill=(255, 214, 90, 235), outline=(40, 20, 0, 255), width=3)
            text(fr, X, Y, str(i + 1), int(40 * pop), (30, 20, 0), (255, 214, 90), 1)

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

def answer_badge(fr, tt, x=W / 2, y=110, scale=1.0):
    if not (K05_T + 1.6 <= tt < K05_T + DUR["K05"]): return
    d = ImageDraw.Draw(fr, "RGBA")
    d.rounded_rectangle([x - 380 * scale, y - 50 * scale, x + 380 * scale, y + 50 * scale], int(24 * scale), fill=(20, 60, 30, 220), outline=(120, 230, 120, 255), width=4)
    text(fr, x, y, "إجابة لغز امبارح: صاحب الضل قصير ✓", int(42 * scale), (200, 255, 200))

def vertical(fr, tt):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = ImageEnhance.Brightness(small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.35)
    bgv.paste(fr.resize((1080, 608), Image.LANCZOS), (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(255, 214, 90)); d.rectangle([0, 1168, 1080, 1171], fill=(255, 214, 90))
    text(bgv, 540, 300, "سر الدور السابع", 92, (255, 214, 90), (40, 10, 10), 6)
    text(bgv, 540, 420, "الحلقة 5: الجار الجديد", 52, (235, 235, 235))
    k, _ = line_at(tt)
    if k:
        for i, l in enumerate(wrap(SUB[k])[:4]): text(bgv, 540, 1290 + i * 80, l, 60, sw=6)
    answer_badge(bgv, tt, 540, 1700, 1.25)
    if PUZ <= tt < PUZ_END:
        d.rounded_rectangle([40, 1640, 1040, 1800], 26, fill=(20, 20, 30), outline=(255, 214, 90), width=5)
        text(bgv, 540, 1695, "لغز الحلقة: إيه الغريب في بيت فهمي؟", 46, (255, 214, 90))
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
    if set_ in ("title", "endcard", "keycard"): return finish(card(set_, tt, sh), tt)
    if set_ == "black": return Image.new("RGB", (W, H), (0, 0, 0))
    cam = cam_at(sh, tt)
    if sh.get("freeze"): cam = cam_at(sh, FREEZE[0]); tt_draw = FREEZE[0]
    else: tt_draw = tt
    if sh.get("blackout"): return finish(eyes_only(sh, tt, cam), tt)
    img = bg_frame(set_, cam)
    if set_ == "lobby": draw_lobby_props(img, cam, tt_draw)
    if set_ == "fahmy": draw_apartment_props(img, cam, tt_draw, sh)
    layer, hand = draw_scene_chars(set_, tt_draw, cam, sh)
    layer = tint_layer(layer, TINT[set_], 1.0 if set_ in ("bedroom", "lobby") else 0.95)
    img.paste(layer, (0, 0), layer)
    if set_ == "stairs" and tt < RUNCAT[1] + 0.3:   # cat running away across the floor
        k = (tt - RUNCAT[0]) / (RUNCAT[1] - RUNCAT[0])
        if 0 <= k < 1.2:
            x0, y0, z = cam
            draw_cat_shape(ImageDraw.Draw(img), ((lerp(1000, 2000, k)) - x0) * z * SS, ((1000 - y0) * z) * SS, 1.3 * z * SS, (20, 20, 26), True)
    fr = img.resize((W, H), Image.LANCZOS)
    if set_ == "stairs":
        lm, spot = light_map_stairs(sh, tt, cam, hand)
        fr = ImageChops.multiply(fr, lm); fr = ImageEnhance.Brightness(fr).enhance(1.7)
        if spot is not None:
            sp = Image.fromarray((np.clip(spot, 0, 1) * 255).astype(np.uint8)).resize((W, H), Image.BILINEAR)
            fr = Image.composite(ImageChops.screen(fr, Image.new("RGB", (W, H), (110, 104, 86))), fr, sp)
        draw_beam(fr, sh, tt, cam, hand)
    if set_ == "fahmy":
        if sh.get("red"):
            k = min(1, (tt - APP0) / 1.5)
            fr = ImageChops.multiply(fr, Image.new("RGB", (W, H), (255, int(lerp(255, 120, k)), int(lerp(255, 110, k)))))
        fr = led_glow(fr, cam, tt, sh)
    if sh.get("vent"): fr = led_glow(fr, cam, tt, sh)
    if sh.get("count"): count_overlay(fr, tt, cam)
    if sh.get("freeze"): fr = detective(fr, tt, cam)
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
        answer_badge(h, tt)
        if PUZ <= tt < PUZ_END:
            d = ImageDraw.Draw(h, "RGBA")
            d.rounded_rectangle([W / 2 - 620, 60, W / 2 + 620, 180], 24, fill=(20, 20, 30, 215), outline=(255, 214, 90, 255), width=4)
            text(h, W / 2, 120, "لغز الحلقة: إيه الغريب في بيت أستاذ فهمي؟ اكتب في الكومنتات", 38, (255, 214, 90))
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
    dr = drone(TOTAL + 1)
    # lighter ambience in the daytime lobby / morning
    env = np.ones(len(dr), np.float32)
    for s_ in shots:
        if s_["set"] in ("bedroom", "lobby"):
            env[int(s_["start"] * SR):int(s_["end"] * SR)] = 0.35
    env = np.convolve(env, np.ones(4410) / 4410, mode="same")
    mix_into(buf, dr * env, 0, 1.0)
    r = np.random.default_rng(9)
    ts = np.arange(int(SR * 1.6)) / SR
    S = {"knock": sfx_knock() * 1.2, "boom": sfx_boom(), "tick": sfx_tick() * 2.2, **SFXF}
    tc = np.arange(int(SR * 0.06)) / SR
    S["click"] = r.normal(0, 1, len(tc)) * np.exp(-tc * 140) * 0.7
    S["sting"] = (np.sin(2 * np.pi * (1200 + 80 * np.sin(ts * 40)) * ts) * 0.08 + np.sin(2 * np.pi * 1263 * ts) * 0.06
                  + np.sin(2 * np.pi * 55 * ts) * 0.4) * np.exp(-ts * 1.8)
    tsh = np.arange(int(SR * 0.25)) / SR
    S["shutter"] = (r.normal(0, 1, len(tsh)) * (np.exp(-tsh * 60) + 0.6 * np.exp(-np.maximum(0, tsh - 0.08) * 70) * (tsh > 0.08))) * 0.5
    jt = np.arange(int(SR * 0.6)) / SR
    S["keys"] = sum(np.sin(2 * np.pi * f * jt + r.uniform(0, 6)) * np.exp(-jt * (9 + 3 * j)) * (jt > j * 0.04)
                    for j, f in enumerate(r.uniform(2800, 7000, 8))) * 0.08
    S["door"] = sfx_knock() * 0.4
    for t0, n, g in sfx:
        if n in S: mix_into(buf, S[n], t0, g)
    tsx = np.arange(int(SR * 0.25)) / SR
    for i, (st, g, jing) in enumerate(STEPS):
        nz = np.convolve(r.normal(0, 1, len(tsx)), np.ones(12) / 12, mode="same")
        step = (np.sin(2 * np.pi * 85 * tsx) * np.exp(-tsx * 32) * 0.9 + nz * np.exp(-tsx * 26) * 0.9) * 0.6
        mix_into(buf, step, st, g)
        if jing and i % 2 == 0:
            jj = sum(np.sin(2 * np.pi * f * jt[:int(SR * 0.3)] + r.uniform(0, 6)) * np.exp(-jt[:int(SR * 0.3)] * (18 + 6 * j)) for j, f in enumerate(r.uniform(3200, 6800, 4)))
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
        mux("h.mp4", "sirr_eldor_elsabe3_ep5.mp4"); mux("v.mp4", "sirr_eldor_elsabe3_ep5_vertical.mp4")
        print("done")
