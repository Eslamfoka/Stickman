import sys, os, math, subprocess, wave
sys.path.insert(0, "/home/claude/s1e1")
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter
from engine import *

os.chdir("/home/claude/s1e3")
SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(31)
E1 = "/home/claude/s1e1/"

SUB = {
 "H00": "مين اللي طالع على السلم ده؟!",
 "H01": "اللي قالوا الدور السابع، من تلاتين سنة... برافو عليكو! إجابتكو صح!",
 "H02": "المفتاح اتسرق! كان تحت المخدة، والشباك كان مفتوح!",
 "H03": "الأوضة في الدور التاني. يعني الحرامي يا إما بيطير... يا إما من جوه العمارة.",
 "H04": "وأنا شفت ده على الشباك... خيط أبيض، من جلابية!",
 "H05": "جلابية؟! مفيش حد بيلبس جلابية في العمارة غير...",
 "H06": "البواب.",
 "H07": "خلاص. الليلة هنستناه، ونشوف بيعمل إيه.",
 "H08": "شطة! بطل تاكل شيبسي! صوته مسموع لحد السطوح!",
 "H09": "أنا باكل بالراحة والله...",
 "H10": "بصوا... الدكة فاضية! البواب مش نايم!",
 "H11": "ماسك المفتاح... وطالع لفوق.",
 "H12": "تلاتة سريعين... تلاتة طوال... وتلاتة سريعين تاني!",
 "H13": "لغز النهارده: الخبط ده معناه إيه؟ اكتبوا في الكومنتات!",
 "H14": "هاتشو!",
 "H15": "أنا شايفكم.",
}
WHO = {"H00": "shatta", "H01": "tota", "H02": "shatta", "H03": "zalata", "H04": "tota", "H05": "shatta",
       "H06": "zalata", "H07": "shatta", "H08": "zalata", "H09": "shatta", "H10": "tota", "H11": "zalata",
       "H12": "tota", "H13": "tota", "H14": "shatta", "H15": "bondo2"}
EXPR = {"H00": "scared", "H01": [(0, "happy")], "H02": [(0, "scared"), (0.45, "shock")], "H03": "flat",
        "H04": [(0, "neutral"), (0.55, "happy")], "H05": "shock", "H06": [(0, "flat"), (0.6, "smug")],
        "H07": "angry", "H08": "angry", "H09": "happy", "H10": "scared", "H11": "scared", "H12": "scared",
        "H13": [(0, "neutral"), (0.6, "smug")], "H14": "shock", "H15": "angry"}
ARMS = {"H01": "point", "H02": "up", "H04": "point", "H05": "up", "H06": "point", "H07": "hips",
        "H08": "shush", "H10": "point", "H11": "point", "H13": "point", "H14": "scared"}

AUD = {k: load_audio(f"audio/{k}.mp3") for k in SUB}
ENV = {k: envelope(v) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}
SFXF = {n: load_audio(f"sfx/{n}.mp3") for n in ("footsteps", "chips", "whoosh")}

lines, sfx, shots, jumps, shakes = [], [], [], {}, []
def say(t, k): lines.append((t, k)); return t + DUR[k]
def fx(t, n, g=1.0): sfx.append((t, n, g))
def jump(w, t): jumps.setdefault(w, []).append(t)
def shot(set_, s, e, c0, c1=None, **kw):
    shots.append(dict(set=set_, start=s, end=e, c0=c0, c1=c1 or c0, **kw))
def cut(t, g=0.45): fx(t - 0.12, "whoosh", g)

# ---------------- layouts (world coords 1920x1080) ----------------
POS = {
 "bedroom": {"shatta": (620, 1030, 2.4), "zalata": (960, 1030, 2.4), "tota": (1300, 1030, 2.4)},
 "stairs": {"shatta": (250, 1240, 3.0), "tota": (520, 1290, 3.0)},
 "lobby": {"tota": (230, 1170, 2.3), "shatta": (470, 1170, 2.3), "zalata": (720, 1170, 2.3)},
 "door7": {"tota": (240, 1030, 1.9), "shatta": (410, 1030, 1.9), "zalata": (585, 1030, 1.9)},
}
def CU(set_, who, z=2.2, dx=0):
    x, y, s = POS[set_][who]; S = s * CH[who]["scale"]
    if who == "tota": z *= 1.3
    hy = y - 190 * S
    return (x + dx, hy + H / (2 * z) - 1.45 * 46 * S - 25, z)

t = 0.0
# ================= 1. HOOK: stairs (flash-forward) =================
CLIMB = (0.2, 5.4)
fx(0.2, "steps", 1.0)
shot("stairs", 0, 1.45, (960, 540, 1.0), (960, 520, 1.08))
t = 1.45; H00_T = t
t = say(t, "H00") + 0.25
shot("stairs", 1.45, t, CU("stairs", "shatta", 2.1), CU("stairs", "shatta", 2.35))
TURN0 = CLIMB[1] + 0.1
shot("stairs", t, TURN0 + 0.9, (1150, 520, 1.6), (1100, 360, 1.85))
t = TURN0 + 0.9
fx(TURN0 + 0.05, "sting", 0.7)
cut(t, 0.6)
# ================= title =================
fx(t, "boom", 0.7); shot("title", t, t + 2.3, None); t += 2.3
# ================= 2. MORNING =================
cut(t, 0.4)
MORN0 = t; t += 0.35
s = t; t = say(t, "H01") + 0.15
shot("bedroom", MORN0, t, CU("bedroom", "tota", 1.9), CU("bedroom", "tota", 2.2))
ANS = (s + 1.2, t)
cut(t); s = t; t += 0.05
H02_T = t; t = say(t, "H02") + 0.15; shakes.append((H02_T, 10))
jump("shatta", H02_T + 0.05)
mid = H02_T + DUR["H02"] * 0.42
shot("bedroom", s, mid, CU("bedroom", "shatta", 1.9), CU("bedroom", "shatta", 2.4))
shot("bedroom", mid, t, (790, 450, 3.0), (790, 440, 3.3), mark="pillow")
cut(t, 0.3); s = t
t = say(t, "H03") + 0.2
shot("bedroom", s, t, (800, 560, 1.45), (810, 545, 1.6))
s = t; H04_T = t; t = say(t, "H04") + 0.2
mid = H04_T + DUR["H04"] * 0.45
shot("bedroom", s, mid, CU("bedroom", "tota", 2.1), CU("bedroom", "tota", 2.3))
shot("bedroom", mid, t, (420, 260, 2.7), (440, 270, 3.1), mark="thread")
s = t; H05_T = t; t = say(t, "H05") + 0.15
shot("bedroom", s, t, CU("bedroom", "shatta", 1.25), CU("bedroom", "shatta", 2.5), ease="crash")
s = t; H06_T = t; fx(t + 0.05, "boom", 0.9); shakes.append((t + 0.05, 8))
t = say(t, "H06") + 0.25
shot("bedroom", s, t, CU("bedroom", "zalata", 2.6), CU("bedroom", "zalata", 3.1), dark=True)
FLASH = (t, t + 0.75); fx(t, "sting", 0.9)
shot("flash", t, t + 0.75, (960, 540, 1.0), (960, 540, 1.12)); t += 0.75
cut(t, 0.35); s = t; t += 0.2
H07_T = t; t = say(t, "H07") + 0.3
shot("bedroom", s, t, (960, 560, 1.1), (960, 560, 1.22))
# ================= 3. MONTAGE =================
for nm, d in (("card_torch", 0.85), ("card_chips", 0.85), ("card_note", 1.05)):
    cut(t, 0.55); shot(nm, t, t + d, None)
    if nm == "card_torch": fx(t + 0.35, "click", 0.8)
    if nm == "card_chips": fx(t + 0.2, "chips", 0.6)
    if nm == "card_note": fx(t + 0.2, "paper", 0.6)
    t += d
CLOCK = t; shot("card_clock", t, t + 1.6, None)
for i in range(4): fx(t + 0.2 + i * 0.35, "tick", 1.0)
t += 1.6
# ================= 4. STAKEOUT (lobby night) =================
S0 = t
shot("lobby", t, t + 0.9, (900, 600, 1.05), (880, 620, 1.1))
shot("lobby", t + 0.9, t + 1.9, CU("lobby", "shatta", 1.9, dx=40), CU("lobby", "shatta", 2.05, dx=40))
CHEW = [(t + 0.25, t + 1.9)]
t += 1.9
s = t; t = say(t, "H08") + 0.15
shot("lobby", s, t, CU("lobby", "zalata", 2.3), CU("lobby", "zalata", 2.45))
CHEW.append((t, t + 0.85)); s = t; t += 0.6
t = say(t, "H09") + 0.25
shot("lobby", s, t, CU("lobby", "shatta", 2.3), CU("lobby", "shatta", 2.5))
s = t; H10_T = t; t = say(t, "H10") + 0.25
mid = H10_T + DUR["H10"] * 0.38
shot("lobby", s, mid, CU("lobby", "tota", 2.3), CU("lobby", "tota", 2.45))
shot("lobby", mid, t, (420, 520, 2.0), (420, 520, 2.25), pov=True)
fx(mid + 0.1, "sting", 0.5)
# bondo walks door -> stairs -> up
BW0 = t; BW1 = t + 2.4
fx(t + 0.1, "steps", 1.0)
shot("lobby", t, t + 2.7, (1060, 600, 1.05), (1150, 560, 1.15))
t += 2.7; s = t
t = say(t, "H11") + 0.1
shot("lobby", s, t, CU("lobby", "zalata", 2.1, dx=60), CU("lobby", "zalata", 2.3, dx=60), glowpass=True)
BW2 = t + 1.1
shot("lobby", t, BW2 + 0.6, (1300, 480, 1.35), (1420, 400, 1.55))
t = BW2 + 0.6
cut(t, 0.5)
# ================= 5. DOOR 7 =================
D0 = t
BD_ARR = (t, t + 1.5)
fx(t + 0.05, "steps", 0.8)
shot("door7", t, t + 1.8, (960, 560, 1.0), (1000, 560, 1.1))
t += 1.8
KN = []
for dt in (0, 0.22, 0.44): KN.append(t + dt)
for dt in (1.15, 1.85, 2.55): KN.append(t + dt)
for dt in (3.3, 3.52, 3.74): KN.append(t + dt)
for k_ in KN: fx(k_, "knock", 1.0)
shot("door7", t - 0.1, t + 0.95, (1220, 600, 1.8), (1220, 600, 1.95))
shot("door7", t + 0.95, t + 3.05, (420, 690, 1.75), (420, 690, 1.95))
shot("door7", t + 3.05, t + 4.3, (1220, 600, 1.95), (1220, 600, 2.1))
for w_ in ("shatta", "zalata", "tota"): jump(w_, t + 0.05)
t += 4.3
s = t; t = say(t, "H12") + 0.2
shot("door7", s, t, CU("door7", "tota", 2.4), CU("door7", "tota", 2.6))
PUZ = t; s = t; t = say(t, "H13") + 1.0; PUZ_END = t
shot("door7", s, t, CU("door7", "tota", 2.6), CU("door7", "tota", 2.9))
# silence beat, bondo listening at door
shot("door7", t, t + 1.1, (960, 560, 1.0), (980, 560, 1.06)); t += 1.1
H14_T = t; t = say(t, "H14") + 0.05; shakes.append((H14_T + 0.15, 16)); jump("shatta", H14_T + 0.15)
shot("door7", H14_T - 0.05, t, CU("door7", "shatta", 2.3), CU("door7", "shatta", 2.0))
FREEZE = t; fx(t + 0.1, "sting", 1.0)
shot("door7", t, t + 1.3, (1100, 560, 1.6), (1100, 540, 1.9)); t += 1.3
APP0 = t; APP1 = t + 2.6
fx(t, "steps_slow", 1.0)
shot("door7", t, APP1, (960, 560, 1.0), (960, 560, 1.04))
t = APP1 + 0.15
H15_T = t; t = say(t, "H15") + 0.5
shot("door7", APP1, t, (960, 540, 1.04), (960, 520, 1.15), dark=True)
fx(t, "boom", 1.0); shot("black", t, t + 0.6, None); t += 0.6
shot("endcard", t, t + 3.4, None); t += 3.4
TOTAL = t

EAT_P = 0.8
BITES = []
for a_, b_ in CHEW:
    n = 0
    while a_ + (n + 0.6) * EAT_P < b_: BITES.append(a_ + (n + 0.6) * EAT_P); n += 1
def eat_phase(tt):
    for a_, b_ in CHEW:
        if a_ <= tt < b_: return ((tt - a_) / EAT_P) % 1
    return None

STEPS = []
def contacts(t0, t1, rate, g0=0.7, g1=0.7, off=0.0):
    n = math.ceil((t0 * rate - off) / math.pi)
    while True:
        tc = (n * math.pi + off) / rate
        if tc >= t1: break
        if tc >= t0: STEPS.append((tc, g0 + (g1 - g0) * (tc - t0) / max(1e-3, t1 - t0)))
        n += 1
contacts(CLIMB[0], CLIMB[1], 7, 0.9, 0.55)
contacts(BW0, BW2, 7, 0.7, 0.5)
contacts(BD_ARR[0], BD_ARR[1], 7, 0.6, 0.8)
contacts(APP0, APP1, 5, 0.8, 1.6, off=APP0 * 5)

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

# ---------------- backgrounds ----------------
SRCBG = {"bedroom": ImageChops.multiply(ImageEnhance.Brightness(Image.open(E1 + "bg/bedroom_clean.png").convert("RGB")).enhance(1.55),
                                        Image.new("RGB", Image.open(E1 + "bg/bedroom_clean.png").size, (255, 236, 205))),
         "stairs": Image.open(E1 + "bg/stairs_1080.png").convert("RGB"),
         "lobby": Image.open(E1 + "bg/lobby_1080.png").convert("RGB"),
         "door7": Image.open("/home/claude/s1e2/bg/door7.png").convert("RGB")}
TINT = {"bedroom": (255, 240, 225), "stairs": (175, 185, 235), "lobby": (165, 180, 240), "door7": (175, 190, 255),
        "flash": (255, 70, 60)}
AMB = {"stairs": 0.45, "lobby": 0.5, "door7": 0.5}
yy, xx = np.mgrid[0:H, 0:W]
vg = 1 - 0.55 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) ** 1.2
VIG = Image.fromarray((np.clip(vg, 0.25, 1) * 255).astype(np.uint8)).convert("RGB")
vg2 = np.clip(1 - 0.9 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2), 0.12, 1)
VIG_DARK = Image.fromarray((vg2 * 255).astype(np.uint8)).convert("RGB")

def cam_at(sh, tt):
    k = ease((tt - sh["start"]) / max(0.01, sh["end"] - sh["start"]), sh.get("ease"))
    c = [a + (b - a) * k for a, b in zip(sh["c0"], sh["c1"])]
    shake = 0
    for st, amp in shakes:
        if 0 <= tt - st < 0.35: shake = max(shake, amp * (1 - (tt - st) / 0.35))
    if shot_at(tt)["set"] == "door7" and any(0 <= tt - k_ < 0.12 for k_ in KN):
        shake = max(shake, 6)
    cx, cy, z = c; cw, ch = W / z, H / z
    x0 = min(max(cx - cw / 2, 0), W - cw); y0 = min(max(cy - ch / 2, 0), H - ch)
    if shake:
        x0 = min(max(x0 + rng.normal(0, shake / z), 0), W - cw); y0 = min(max(y0 + rng.normal(0, shake / z), 0), H - ch)
    return x0, y0, z

# ---------------- actors ----------------
def lerp(a, b, k): return a + (b - a) * k
def path(pts, k):
    """pts: list of (x,y,s); k in 0..1 across segments with equal time"""
    n = len(pts) - 1; k = min(max(k, 0), 0.9999) * n; i = int(k); f = k - i
    return tuple(lerp(pts[i][j], pts[i + 1][j], f) for j in range(3))

def bondo_state(set_, tt):
    """returns dict or None"""
    if set_ == "stairs":
        k = (tt - CLIMB[0]) / (CLIMB[1] - CLIMB[0])
        x, y, s = path([(1260, 1120, 2.6), (1170, 680, 1.6), (1090, 470, 1.25)], k)
        walking = 0 <= k < 1
        look = 1 if tt < TURN0 else -1
        return dict(x=x, y=y, s=s, walk=tt * 7 if walking else None, look=look, sil=True, expr="angry")
    if set_ == "lobby":
        if tt < BW0 or tt > BW2 + 0.6: return None
        if tt < BW1:
            k = (tt - BW0) / (BW1 - BW0); x, y, s = path([(1000, 720, 1.45), (1460, 690, 1.4)], k)
        else:
            k = (tt - BW1) / (BW2 - BW1); x, y, s = path([(1460, 690, 1.4), (1540, 520, 1.15), (1600, 360, 0.9)], k)
        al = 1.0 if tt < BW2 else max(0, 1 - (tt - BW2) / 0.5)
        return dict(x=x, y=y, s=s, walk=tt * 7 if tt < BW2 else None, look=1, alpha=al, expr="angry", key=True)
    if set_ == "door7":
        if tt < BD_ARR[1]:
            k = (tt - BD_ARR[0]) / (BD_ARR[1] - BD_ARR[0]); x = lerp(760, 1100, ease(k)); return dict(x=x, y=1010, s=2.2, walk=tt * 7, look=1, expr="angry")
        if tt < APP0:
            look = 1 if tt < FREEZE + 0.35 else (1 - 2 * min(1, (tt - FREEZE - 0.35) / 0.3))
            knock = any(0 <= tt - k_ < 0.16 for k_ in KN)
            arms = "point" if (KN[0] - 0.2 <= tt < KN[-1] + 0.3 and knock) else "hold"
            return dict(x=1100, y=1010, s=2.2, look=look, arms=arms, expr="angry" if tt < FREEZE else "angry",
                        lean=0.6 if knock else 0)
        k = ease(min(1, (tt - APP0) / (APP1 - APP0)))
        x = lerp(1100, 980, k); y = lerp(1010, 2050, k); s = lerp(2.2, 8.5, k ** 1.4)
        return dict(x=x, y=y, s=s, walk=(tt - APP0) * 5 if tt < APP1 else None, look=0, expr="angry")
    if set_ == "flash":
        return dict(x=960, y=1700, s=6.3, look=0, expr="angry")
    return None

def kid_expr(set_, who, tt):
    if set_ == "bedroom":
        if tt >= H07_T: return {"shatta": "angry", "zalata": "smug", "tota": "happy"}[who]
        if tt >= H05_T: return "shock" if who != "zalata" else "flat"
        if who == "tota": return "smug"
        return "neutral"
    if set_ == "door7" and tt >= FREEZE: return "shock"
    if set_ == "lobby" and BW0 <= tt: return "scared"
    if set_ == "door7" and any(0 <= tt - k_ < 1.0 for k_ in KN): return "scared"
    return "scared" if set_ in ("stairs",) else "neutral"

def actors(set_, tt, pov=False):
    A = []
    if set_ in POS and not pov:
        for who, (x, y, s) in POS[set_].items():
            a = dict(who=who, x=x, y=y, s=s, look=0, expr=kid_expr(set_, who, tt))
            if set_ == "bedroom":
                a["look"] = {"shatta": 1, "zalata": 0, "tota": -1}[who]
                if who == "zalata": a["held"] = "notebook"
            if set_ == "stairs": a["look"] = 1; a["arms"] = "scared"
            if set_ == "lobby":
                a["look"] = 1
                if who == "shatta": a["held"] = "chipsbag"; a["arms"] = "hold"
                if who == "zalata": a["held"] = "notebook"
                if who == "tota": a["held"] = "torch"; a["arms"] = "hold"
                if BW0 <= tt: a["arms"] = "scared"; a["held"] = "chipsbag" if who == "shatta" else None
            if set_ == "door7":
                a["look"] = 1
                if tt >= FREEZE: a["arms"] = "scared"
            A.append(a)
    b = bondo_state(set_, tt)
    if b: b["who"] = "bondo2"; b.setdefault("held", "lantern"); b.setdefault("arms", "hold"); A.append(b)
    return A

def jump_off(who, tt):
    for j in jumps.get(who, []):
        if 0 <= tt - j < 0.4: return math.sin((tt - j) / 0.4 * math.pi) * 60
    return 0

def expr_of(k, lt):
    e = EXPR[k]
    if isinstance(e, str): return e
    cur = e[0][1]
    for f, ex in e:
        if lt / DUR[k] >= f: cur = ex
    return cur

def lantern_world(a):
    S = a["s"] * CH["bondo2"]["scale"]
    return a["x"] + 46 * S, a["y"] - 75 * S

def draw_scene_chars(set_, tt, cam, pov=False):
    x0, y0, z = cam
    layer = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(layer)
    sil = None; lights = []
    k, lt = line_at(tt)
    acts = sorted(actors(set_, tt, pov), key=lambda a: a["s"])
    for a in acts:
        who = a["who"]; talking = k is not None and WHO[k] == who
        expr = a.get("expr", "neutral")
        if talking: expr = expr_of(k, lt)
        mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
        eat = eat_phase(tt) if who == "shatta" and set_ == "lobby" and not talking else None
        if eat is not None:
            expr = "happy"
            mouth = 0.3 * abs(math.sin((eat - 0.6) * 22)) if eat >= 0.6 else (0.45 if 0.45 <= eat < 0.6 else 0)
        if talking and k == "H09": mouth = max(mouth * 0.6, 0.25 * abs(math.sin(tt * 14)))
        arms = a.get("arms", "down")
        if talking: arms = ARMS.get(k, "talk" if arms == "down" else arms)
        if talking and a.get("held") in ("chips", "chipsbag", "torch") and arms not in ("scared",): arms = "hold"
        bob = abs(math.sin(a["walk"])) * 5 * a["s"] if a.get("walk") is not None else 0
        wy = a["y"] - jump_off(who, tt) - bob
        shiver = math.sin(tt * 60) * 2.5 if expr in ("scared", "shock") and who != "bondo2" else 0
        blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11
        X = (a["x"] + shiver - x0) * z; Y = (wy - y0) * z; s = a["s"] * z
        target = p
        if a.get("sil") or a.get("alpha", 1) < 1:
            sil = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); target = P(sil)
        target.ell(X, (a["y"] - y0) * z + 4 * s / a["s"] * a["s"], 46 * s, 9 * s, (0, 0, 0, 110), None)
        draw_char(target, who, X, Y, s, expr, mouth, a.get("look", 0), blink, arms, tt, a.get("held"),
                  a.get("lean", 0), a.get("walk"), eat)
        if who == "shatta" and set_ == "lobby":
            for bt in BITES:
                u = tt - bt
                if 0 <= u < 0.6:
                    S_ = s; mx, my = X + 6 * S_, Y - 160 * S_
                    for j in range(7):
                        vx = (j - 3) * 22 * S_; vy = -60 * S_ + (j % 3) * 15 * S_
                        px = mx + vx * u; py = my + vy * u + 500 * S_ * u * u
                        r_ = (2.2 + (j % 3)) * S_
                        target.ell(px, py, r_, r_ * 0.8, (240, 190, 70, 255), (150, 100, 20, 255), 0.8 * S_)
        if who == "bondo2":
            S = s * CH[who]["scale"]
            if a.get("key"):
                kx, ky = X - 36 * S, Y - 64 * S
                target.ell(kx, ky + 8 * S, 6 * S, 6 * S, None, (230, 190, 70, 255), 3 * S)
                target.line([(kx, ky + 14 * S), (kx, ky + 30 * S)], (230, 190, 70, 255), 3 * S)
            lx, ly = lantern_world(dict(x=a["x"], y=wy, s=a["s"]))
            lights.append(((lx - x0) * z, (ly - y0) * z, 430 * z * a["s"] / 2.2 if who else 0, a.get("alpha", 1)))
        if target is not p:
            if a.get("sil"):
                al = sil.getchannel("A")
                sil = Image.new("RGBA", sil.size, (6, 6, 12, 255)); sil.putalpha(al.point(lambda v: int(v * 0.95)))
                lx, ly, _, _ = lights[-1]; P(sil).ell(lx, ly, 10 * s, 14 * s, (255, 220, 130, 255), None)
            if a.get("alpha", 1) < 1:
                al_ = a["alpha"]; sil.putalpha(sil.getchannel("A").point(lambda v: int(v * al_)))
            layer = Image.alpha_composite(layer, sil); p = P(layer)
    return layer, lights

def tint_layer(layer, tint, lvl):
    rgb = layer.convert("RGB"); al = layer.getchannel("A")
    c = tuple(int((v * 0.55 + 255 * 0.45) * min(1.0, lvl)) for v in tint)
    rgb = ImageChops.multiply(rgb, Image.new("RGB", rgb.size, c))
    out = rgb.convert("RGBA"); out.putalpha(al); return out

LW, LH = W // 8, H // 8
gy, gx = np.mgrid[0:LH, 0:LW] * 8
def light_map(set_, tt, cam, lights):
    amb = AMB[set_]
    m = np.full((LH, LW), amb, np.float32)
    x0, y0, z = cam
    fixed = []
    if set_ == "stairs": fixed = [(471, 201, 380), (1050, 120, 420)]
    if set_ == "lobby": fixed = [(380, 30, 600), (1545, 30, 250)]
    if set_ == "door7": fixed = [(150, 860, 520)] + ([(980, 1000, 520)] if tt >= APP0 + 1.2 else [])
    for fx_, fy_, r in fixed:
        X, Y = (fx_ - x0) * z, (fy_ - y0) * z; R = r * z
        m += 0.45 * np.exp(-((gx - X) ** 2 + (gy - Y) ** 2) / (R * R))
    for X, Y, R, al in lights:
        fl = 0.92 + 0.08 * math.sin(tt * 23) * math.sin(tt * 7)
        m += 0.95 * al * fl * np.exp(-((gx - X) ** 2 + (gy - Y) ** 2) / (R * R))
    warm = np.zeros((LH, LW, 3), np.float32)
    for X, Y, R, al in lights:
        g = al * np.exp(-((gx - X) ** 2 + (gy - Y) ** 2) / (R * R * 0.6))
        warm += g[..., None] * np.array([0.28, 0.12, -0.08])
    mm = np.clip(m[..., None] + warm, 0, 1.6)
    return Image.fromarray((np.clip(mm / 1.6, 0, 1) * 255).astype(np.uint8)).resize((W, H), Image.BILINEAR)

DUST = rng.uniform(-1, 1, (28, 3))
def draw_dust(fr, tt, lights):
    d = ImageDraw.Draw(fr, "RGBA")
    for X, Y, R, al in lights:
        for i, (u, v, w) in enumerate(DUST):
            px = X + (u * 0.6 + 0.05 * math.sin(tt * 0.7 + i)) * R
            py = Y + ((v + tt * 0.06 * (1 + w)) % 2 - 1) * R * 0.6
            r = 1.5 + abs(w) * 2.2
            a = int(120 * al * max(0, 1 - math.hypot(px - X, py - Y) / R))
            d.ellipse([px - r, py - r, px + r, py + r], fill=(255, 235, 190, a))

def bg_frame(set_, cam, sharp=False):
    x0, y0, z = cam; src = SRCBG[set_]; sw, sh = src.size; f = sw / W
    box = (x0 * f, y0 * f, (x0 + W / z) * f, (y0 + H / z) * f)
    if z > 1.5 and not sharp:
        b = tuple(int(v) for v in box); b = (max(0, b[0] - 20), max(0, b[1] - 20), min(sw, b[2] + 20), min(sh, b[3] + 20))
        part = src.crop(b).filter(ImageFilter.GaussianBlur((z - 1.4) * 2.2))
        box = (box[0] - b[0], box[1] - b[1], box[2] - b[0], box[3] - b[1]); src = part
    img = src.resize((SSW, SSH), Image.BICUBIC, box=box)
    return img

def overlay_mark(img, set_, sh, tt, cam):
    x0, y0, z = cam; d = ImageDraw.Draw(img, "RGBA"); S = lambda v: int(v * SS)
    k = min(1, (tt - sh["start"]) / 0.5)
    if sh.get("mark") == "pillow":
        cx, cy = (790 - x0) * z, (430 - y0) * z; r = 230
        d.arc([S(cx - r), S(cy - r * 0.6), S(cx + r), S(cy + r * 0.6)], -90, -90 + 360 * k, fill=(230, 40, 40, 255), width=S(10))
        if k >= 1: text(img, S(cx), S(cy - r * 0.85), "فاضي!", S(70), (255, 80, 70), (20, 0, 0), S(6))
    if sh.get("mark") == "thread":
        bx, by = (505 - x0) * z, (240 - y0) * z
        pts = []
        for i in range(12):
            u = i / 11; pts.append((S(bx + 10 * u * z + math.sin(tt * 6 + u * 5) * 9 * u * z), S(by + u * 70 * z)))
        d.line(pts, fill=(255, 255, 255, 255), width=S(9)); r = 20 + 8 * math.sin(tt * 10)
        gx_, gy_ = pts[-1]
        d.line([(gx_ - S(r), gy_), (gx_ + S(r), gy_)], fill=(255, 255, 220, 220), width=S(3))
        d.line([(gx_, gy_ - S(r)), (gx_, gy_ + S(r))], fill=(255, 255, 220, 220), width=S(3))
        if k >= 1:
            d.arc([S(bx - 120), S(by - 60), S(bx + 140), S(by + 190 * z / 2.7 + 80)], 0, 360, fill=(255, 214, 90, 255), width=S(7))

# ---------------- cards ----------------
def speed_bg(col, tt):
    fr = Image.new("RGB", (W, H), col); d = ImageDraw.Draw(fr)
    for i in range(36):
        a = i / 36 * 2 * math.pi + tt * 0.6
        d.polygon([(W / 2, H / 2), (W / 2 + math.cos(a) * 2200, H / 2 + math.sin(a) * 2200),
                   (W / 2 + math.cos(a + 0.07) * 2200, H / 2 + math.sin(a + 0.07) * 2200)],
                  fill=tuple(max(0, c - 28) for c in col))
    return fr

def card(name, tt, sh):
    k = (tt - sh["start"]) / (sh["end"] - sh["start"])
    pop = min(1, k * 5); sc = 0.6 + 0.4 * (1 - (1 - pop) ** 3) + 0.05 * k
    if name == "card_torch":
        fr = speed_bg((255, 200, 60), tt); L = Image.new("RGBA", (SSW, SSH)); p = P(L)
        cx, cy = 960, 560; s = 3.2 * sc
        p.rect(cx - 140 * s, cy - 32 * s, cx + 60 * s, cy + 32 * s, (60, 60, 75, 255), INK, 4 * s, 10 * s)
        p.poly([(cx + 60 * s, cy - 32 * s), (cx + 120 * s, cy - 58 * s), (cx + 120 * s, cy + 58 * s), (cx + 60 * s, cy + 32 * s)], (90, 90, 105, 255), INK, 4 * s)
        if k > 0.4:
            p.poly([(cx + 120 * s, cy - 58 * s), (cx + 420 * s, cy - 200 * s), (cx + 420 * s, cy + 200 * s), (cx + 120 * s, cy + 58 * s)], (255, 255, 210, 170), None)
        fr = fr.convert("RGBA"); fr.alpha_composite(L.resize((W, H), Image.LANCZOS)); fr = fr.convert("RGB")
        text(fr, W / 2, 170, "كشاف ✓", 96, (255, 255, 255), (60, 30, 0), 8)
    elif name == "card_chips":
        fr = speed_bg((235, 70, 60), tt); L = Image.new("RGBA", (SSW, SSH)); p = P(L)
        cx, cy = 960, 600; s = 3.4 * sc
        p.poly([(cx - 70 * s, cy - 110 * s), (cx + 70 * s, cy - 110 * s), (cx + 58 * s, cy + 100 * s), (cx - 58 * s, cy + 100 * s)], (255, 214, 60, 255), INK, 4 * s)
        p.ell(cx, cy, 36 * s, 36 * s, (240, 120, 40, 255), INK, 3 * s)
        fr = fr.convert("RGBA"); fr.alpha_composite(L.resize((W, H), Image.LANCZOS)); fr = fr.convert("RGB")
        text(fr, W / 2, 150, "شيبسي ✓ (؟!)", 96, (255, 255, 255), (60, 0, 0), 8)
    elif name == "card_note":
        fr = speed_bg((90, 160, 60), tt); L = Image.new("RGBA", (SSW, SSH)); p = P(L)
        cx, cy = 960, 560; s = 2.2 * sc
        p.rect(cx - 230 * s, cy - 170 * s, cx + 230 * s, cy + 170 * s, (252, 250, 236, 255), INK, 4 * s, 8 * s)
        for i in range(6): p.line([(cx - 200 * s, cy - 90 * s + i * 45 * s), (cx + 200 * s, cy - 90 * s + i * 45 * s)], (150, 190, 230, 255), 2 * s)
        fr = fr.convert("RGBA"); fr.alpha_composite(L.resize((W, H), Image.LANCZOS)); fr = fr.convert("RGB")
        text(fr, W / 2, 400, "خطة المراقبة", int(70 * sc), (30, 30, 30), (252, 250, 236), 2)
        steps = ["١- نستخبى ورا الزرعة", "٢- محدش يتكلم", "٣- شطة ميكلش"]
        for i, st in enumerate(steps):
            if k > 0.25 + i * 0.2: text(fr, W / 2, 520 + i * 90, st, int(54 * sc), (40, 40, 120), (252, 250, 236), 2)
    elif name == "card_clock":
        fr = Image.new("RGB", (W, H), (8, 10, 22)); L = Image.new("RGBA", (SSW, SSH)); p = P(L)
        cx, cy, r = 960, 470, 230
        p.ell(cx, cy, r, r, (240, 236, 220, 255), INK, 8)
        for i in range(12):
            a = i / 12 * 2 * math.pi
            p.line([(cx + math.sin(a) * r * 0.82, cy - math.cos(a) * r * 0.82), (cx + math.sin(a) * r * 0.92, cy - math.cos(a) * r * 0.92)], INK, 6)
        ang = -0.25 + min(1, k * 1.2) * 0.25
        p.line([(cx, cy), (cx + math.sin(ang) * r * 0.75, cy - math.cos(ang) * r * 0.75)], INK, 12)
        p.line([(cx, cy), (cx + math.sin(ang * 0.08) * r * 0.5, cy - math.cos(ang * 0.08) * r * 0.5)], INK, 16)
        fr = fr.convert("RGBA"); fr.alpha_composite(L.resize((W, H), Image.LANCZOS)); fr = fr.convert("RGB")
        text(fr, W / 2, 820, "الساعة 12 بالليل...", 90, (200, 210, 255), (0, 0, 20), 6)
    else:
        fr = Image.new("RGB", (W, H), (8, 8, 12))
        g = lambda c: tuple(int(v * min(1, k * 3)) for v in c)
        if name == "title":
            text(fr, W / 2, H / 2 - 80, "عمارة نعناعة", 110, g((255, 214, 90)), (40, 10, 10), 6)
            text(fr, W / 2, H / 2 + 50, "سر الدور السابع", 64, g((230, 230, 230)))
            text(fr, W / 2, H / 2 + 145, "الحلقة 3: عم بندق مش بينام ليه؟", 48, g((210, 210, 210)))
        elif name == "endcard":
            text(fr, W / 2, H / 2 - 60, "الحلقة 4 بكرة", 104, g((255, 214, 90)), (40, 10, 10), 6)
            text(fr, W / 2, H / 2 + 70, "الخبط ده معناه إيه؟ اكتب حلّك في الكومنتات", 48, g((230, 230, 230)))
    return fr

# ---------------- morse HUD ----------------
def morse_hud(fr, tt, y=70, scale=1.0, cx=W / 2):
    if not (KN[0] - 0.05 <= tt < PUZ_END): return
    n = sum(1 for k_ in KN if tt >= k_)
    d = ImageDraw.Draw(fr, "RGBA")
    sym = ["d"] * 3 + ["l"] * 3 + ["d"] * 3
    gap = 64 * scale; total = 9 * gap + 2 * 40 * scale; x = cx - total / 2
    d.rounded_rectangle([x - 30 * scale, y - 42 * scale, x + total + 10 * scale, y + 42 * scale], int(20 * scale), fill=(10, 10, 20, 190), outline=(255, 214, 90, 255), width=3)
    for i, sy in enumerate(sym):
        xi = x + i * gap + (i // 3) * 40 * scale + 10 * scale
        on = i < n; col = (255, 214, 90, 255) if on else (90, 90, 100, 160)
        if sy == "d": d.ellipse([xi, y - 12 * scale, xi + 24 * scale, y + 12 * scale], fill=col)
        else: d.rounded_rectangle([xi - 6 * scale, y - 9 * scale, xi + 42 * scale, y + 9 * scale], int(8 * scale), fill=col)

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
    text(bgv, 540, 420, "الحلقة 3: عم بندق مش بينام ليه؟", 48, (235, 235, 235))
    k, _ = line_at(tt)
    if k:
        for i, l in enumerate(wrap(SUB[k])[:4]): text(bgv, 540, 1290 + i * 80, l, 60, sw=6)
    morse_hud(bgv, tt, y=490, scale=0.8, cx=540)
    if PUZ <= tt < PUZ_END:
        d.rounded_rectangle([60, 1640, 1020, 1800], 26, fill=(20, 20, 30), outline=(255, 214, 90), width=5)
        text(bgv, 540, 1695, "لغز الحلقة: الخبط ده معناه إيه؟", 48, (255, 214, 90))
        text(bgv, 540, 1758, "اكتب حلّك في الكومنتات", 42)
    return bgv

def frame(tt):
    sh = shot_at(tt); set_ = sh["set"]
    if set_.startswith("card") or set_ in ("title", "endcard"):
        return card(set_, tt, sh)
    if set_ == "black": return Image.new("RGB", (W, H), (0, 0, 0))
    cam = cam_at(sh, tt)
    if set_ == "flash":
        img = Image.new("RGB", (SSW, SSH), (40, 0, 0))
        layer, lights = draw_scene_chars("flash", tt, cam)
        layer = tint_layer(layer, TINT["flash"], 1.0); img.paste(layer, (0, 0), layer)
        fr = img.resize((W, H), Image.LANCZOS); fr = ImageChops.multiply(fr, VIG_DARK)
        if int(tt * 24) % 3 == 0: fr = ImageEnhance.Brightness(fr).enhance(1.4)
        return fr
    img = bg_frame(set_, cam, bool(sh.get("mark")))
    layer, lights = draw_scene_chars(set_, tt, cam, sh.get("pov", False) or bool(sh.get("mark")))
    lvl = 1.0 if set_ == "bedroom" else 0.95
    layer = tint_layer(layer, TINT[set_], lvl)
    img.paste(layer, (0, 0), layer)
    overlay_mark(img, set_, sh, tt, cam)
    fr = img.resize((W, H), Image.LANCZOS)
    if set_ in AMB:
        if sh.get("glowpass"):
            k = (tt - sh["start"]) / (sh["end"] - sh["start"])
            lights = lights + [(1500 - 900 * k, 500, 700, 0.8)]
        fr = ImageChops.multiply(fr, light_map(set_, tt, cam, lights).convert("RGB"))
        fr = ImageEnhance.Brightness(fr).enhance(1.6)
        draw_dust(fr, tt, lights)
    fr = ImageChops.multiply(fr, VIG_DARK if sh.get("dark") else VIG)
    fade_in = min(1, (tt - sh["start"]) / 0.12) if set_ == "stairs" and sh["start"] == 0 else 1
    if fade_in < 1: fr = Image.blend(Image.new("RGB", (W, H)), fr, fade_in)
    return fr

def render(out_h, out_v, stills=None, t0=0, t1=None):
    fh = fv = None
    if not stills:
        mk = lambda w, h, o: subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}",
                                   "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "19",
                                   "-pix_fmt", "yuv420p", o], stdin=subprocess.PIPE)
        fh = mk(W, H, out_h); fv = mk(1080, 1920, out_v)
    t1 = t1 or TOTAL
    times = stills or [i / FPS for i in range(int(t0 * FPS), int(t1 * FPS))]
    for i, tt in enumerate(times):
        base = frame(tt)
        h = base.copy()
        morse_hud(h, tt)
        if PUZ <= tt < PUZ_END:
            d = ImageDraw.Draw(h, "RGBA")
            d.rounded_rectangle([W / 2 - 600, 140, W / 2 + 600, 260], 24, fill=(20, 20, 30, 215), outline=(255, 214, 90, 255), width=4)
            text(h, W / 2, 200, "لغز الحلقة: الخبط ده معناه إيه؟ اكتب في الكومنتات", 42, (255, 214, 90))
        if ANS[0] <= tt < ANS[1]:
            d = ImageDraw.Draw(h, "RGBA")
            d.rounded_rectangle([W / 2 - 560, 50, W / 2 + 560, 170], 24, fill=(20, 60, 30, 220), outline=(120, 230, 120, 255), width=4)
            text(h, W / 2, 110, "إجابة لغز امبارح: الدور السابع مقفول من 30 سنة ✓", 42, (200, 255, 200))
        subtitle(h, tt)
        if stills:
            h.save(f"still_h_{tt:.1f}.png"); vertical(base, tt).save(f"still_v_{tt:.1f}.png")
        else:
            fh.stdin.write(h.tobytes()); fv.stdin.write(vertical(base, tt).tobytes())
        if i % 240 == 0: print("frame", i, flush=True)
    if fh:
        fh.stdin.close(); fv.stdin.close(); fh.wait(); fv.wait()

def steps_sfx(n, gap, g):
    return [(i * gap, g * (0.75 + 0.25 * (i % 2))) for i in range(n)]

def build_audio(path="mix.wav"):
    buf = np.zeros(int(TOTAL * SR) + SR * 3, dtype=np.float32)
    dr = drone(TOTAL + 1)
    mix_into(buf, dr, 0, 0.9)
    thud = sfx_knock() * 0.35
    S = {"knock": sfx_knock(), "boom": sfx_boom(), "tick": sfx_tick() * 2.0, "paper": sfx_paper(), **SFXF}
    tt_ = np.arange(int(SR * 0.08)) / SR
    S["click"] = np.random.default_rng(5).normal(0, 1, len(tt_)) * np.exp(-tt_ * 120) * 0.6
    ts = np.arange(int(SR * 1.6)) / SR
    S["sting"] = (np.sin(2 * np.pi * (1200 + 80 * np.sin(ts * 40)) * ts) * 0.08 + np.sin(2 * np.pi * 1263 * ts) * 0.06
                  + np.sin(2 * np.pi * 55 * ts) * 0.4) * np.exp(-ts * 1.8)
    for t0, n, g in sfx:
        if n in ("steps", "steps_slow"): continue
        else:
            mix_into(buf, S[n], t0, g)
    r = np.random.default_rng(9); ts = np.arange(int(SR * 0.25)) / SR
    for i, (st, g) in enumerate(STEPS):
        nz = np.convolve(r.normal(0, 1, len(ts)), np.ones(12) / 12, mode="same")
        step = (np.sin(2 * np.pi * 75 * ts) * np.exp(-ts * 30) * 0.9 + nz * np.exp(-ts * 25) * 0.9) * 0.6
        mix_into(buf, step, st, g)
        if i % 2 == 0:
            jt = np.arange(int(SR * 0.3)) / SR
            jing = sum(np.sin(2 * np.pi * f * jt + r.uniform(0, 6)) * np.exp(-jt * (18 + 6 * j)) for j, f in enumerate(r.uniform(3200, 6800, 4)))
            mix_into(buf, jing * 0.05, st + 0.02, g)
    ch = SFXF["chips"]; e = np.convolve(np.abs(ch), np.ones(2000) / 2000, mode="same"); pk = int(np.argmax(e))
    crunch = ch[max(0, pk - int(SR * 0.05)): pk + int(SR * 0.35)].copy(); crunch *= np.hanning(len(crunch)) ** 0.3
    for bt in BITES: mix_into(buf, crunch, bt - 0.02, 1.1)
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
        mux("h.mp4", "sirr_eldor_elsabe3_ep3.mp4"); mux("v.mp4", "sirr_eldor_elsabe3_ep3_vertical.mp4")
        print("done")
