import sys, os, math, subprocess, wave
sys.path.insert(0, "/home/claude/s1e1")
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter, ImageFont
from engine import *

os.chdir("/home/claude/s1e9")
SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(91)
E1 = "/home/claude/s1e1/"
EPT = "الحلقة 9: اللي ورا الباب"

SUB = {
 "Q01": "الحيطة... الحيطة بتخبط تاني!",
 "Q02": "لغز امبارح: الحاجة الناقصة في الأوضة... الصورة! شوفوا مكانها على الحيطة.",
 "Q03": "نفس الصورة اللي تيتا كانت بتعيط عليها. يعني حد خدها من هنا.",
 "Q04": "اسكتوا! ده مورس... بيقول: جاي... جاي!",
 "Q05": "مين اللي جاي؟! أنا مش هستنى. هنزل بالبكرة! ثقوا فيا!",
 "Q06": "إحنا في الدور السابع يا شطة. أنا حاسبها بالقلم... هتنزل أسرع من الأسانسير. وإحنا معندناش أسانسير!",
 "Q07": "الكشاف... الكشاف بيطفي!",
 "Q08": "عفريت!",
 "Q09": "اهدوا يا ولاد... أنا صاحي أهو.",
 "Q10": "يعني إنت اللي قفلت علينا الباب؟",
 "Q11": "لا يا ابني... أنا اللي فتحت. اسمعوني كويس.",
 "Q12": "المكان ده كان بتاع رشدي... أخو الحاجة نعناعة. قبل ما يسافر من تلاتين سنة، خبى هنا سر كبير.",
 "Q13": "سر إيه؟",
 "Q14": "إن العمارة دي بتاعة السكان كلهم. ومن يومها وأنا بدور عليه كل ليلة، وبخبط بالمورس... زي ما اتفقنا.",
 "Q15": "يعني الخبط كله كان إنت! خضتنا يا راجل!",
 "Q16": "لا يا ابني... الخبط بتاع الساعة اتناشر... ده مش أنا.",
 "Q17": "لغز النهارده: مين اللي قفل علينا الباب؟ الدليل في إيدي... اكتبوا في الكومنتات!",
 "Q18": "أيوه... كله ماشي زي ما اتفقنا. العمارة هتتباع بكرة الصبح.",
 "Q19": "بكرة الصبح؟!",
}
WHO = {"Q01": "shatta", "Q02": "tota", "Q03": "zalata", "Q04": "tota", "Q05": "shatta", "Q06": "zalata", "Q07": "tota",
       "Q08": "shatta", "Q09": "bondo2", "Q10": "zalata", "Q11": "bondo2", "Q12": "bondo2", "Q13": "tota", "Q14": "bondo2",
       "Q15": "shatta", "Q16": "bondo2", "Q17": "tota", "Q18": "fahmy", "Q19": "zalata"}
EXPR = {"Q01": "scared", "Q02": [(0, "neutral"), (0.55, "happy")], "Q03": "flat", "Q04": [(0, "neutral"), (0.45, "scared")],
        "Q05": "shock", "Q06": "flat", "Q07": "scared", "Q08": "shock", "Q09": "sleepy", "Q10": "flat", "Q11": "neutral",
        "Q12": "sad", "Q13": "neutral", "Q14": "neutral", "Q15": "happy", "Q16": "scared", "Q17": [(0, "neutral"), (0.6, "smug")],
        "Q18": "smug", "Q19": "shock"}
ARMS = {"Q01": "scared", "Q02": "point", "Q03": "down", "Q04": "hold", "Q05": "up", "Q06": "point", "Q07": "hold", "Q08": "up",
        "Q09": "hold", "Q10": "hips", "Q11": "hold", "Q12": "hold", "Q13": "hold", "Q14": "hold", "Q15": "talk", "Q16": "hold",
        "Q17": "point", "Q18": "shush", "Q19": "scared"}

AUD = {k: load_audio(f"audio/{k}.mp3") for k in SUB}
# Fahmy overheard down the stairwell: echo + slight low-pass
_a = AUD["Q18"]; _e = np.zeros(len(_a) + int(SR * 1.2), np.float32); _e[:len(_a)] += _a
for d_, g_ in ((0.16, 0.38), (0.33, 0.24), (0.52, 0.14), (0.75, 0.07)):
    i_ = int(d_ * SR); _e[i_:i_ + len(_a)] += _a * g_
AUD["Q18"] = np.convolve(_e, np.ones(5) / 5, mode="same") * 0.85
ENV = {k: envelope(v) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}
DUR["Q18"] = len(_a) / SR
SFXF = {n: load_audio(f"sfx/{n}.mp3") for n in ("whoosh", "creak", "slam", "lock", "wind", "crinkle")}

lines, sfx, shots, jumps, shakes = [], [], [], {}, []
def say(t, k): lines.append((t, k)); return t + DUR[k]
def fx(t, n, g=1.0): sfx.append((t, n, g))
def jump(w, t): jumps.setdefault(w, []).append(t)
def shot(set_, s, e, c0, c1=None, **kw):
    shots.append(dict(set=set_, start=s, end=e, c0=c0, c1=c1 or c0, **kw))
def cut(t, g=0.45): fx(t - 0.12, "whoosh", g)
KIDS = ("shatta", "zalata", "tota")

APT = {"tota": (700, 1000, 2.0), "shatta": (940, 1010, 2.0), "zalata": (1180, 1000, 2.0)}
D7 = {"tota": (240, 1030, 1.9), "shatta": (410, 1030, 1.9), "zalata": (585, 1030, 1.9)}
BONDO_POS = (430, 1005, 2.15)
FAHMY_CU = (820, 1010, 2.4)
WRAP = (860, 1030)
def CU(who, pos, z=2.2, dx=0):
    x, y, s = pos; S = s * CH[who]["scale"]
    if who == "tota": z *= 1.3; dx -= 70
    hy = y - 190 * S
    return (x + dx, hy + H / (2 * z) - 1.45 * 46 * S - 25, z)

t = 0.0
# ===== 0. HOOK: knocking wall in the dark =====
WALLK = [0.35 + d for d in (0, .22, .44, 1.0, 1.42, 1.84, 2.3, 2.52, 2.74)]
for k_ in WALLK: fx(k_, "mknock", 1.15)
fx(0.2, "sting", 0.8)
shot("apt", 0, 3.4, (945, 380, 1.3), (945, 300, 2.1), patch=True, wallk=True, dark=True)
for w_ in KIDS: jump(w_, WALLK[0])
t = 3.4; s = t; t = say(t + 0.05, "Q01") + 0.15
shot("apt", s, t, CU("shatta", APT["shatta"], 1.7), CU("shatta", APT["shatta"], 2.4), ease="crash", dark=True)
cut(t, 0.6); fx(t, "boom", 0.7); shot("title", t, t + 1.6, None); t += 1.6
# ===== 1. answer: the missing photo =====
cut(t, 0.4); s = t; t += 0.1
Q02_T = t; t = say(t, "Q02") + 0.1
shot("apt", s, t, CU("tota", APT["tota"], 1.9), CU("tota", APT["tota"], 2.2))
GHOST = (t, t + 1.9); fx(t + 0.1, "sting", 0.7)
shot("apt", t, GHOST[1], (945, 250, 2.3), (945, 240, 3.0), patch=True, ghost=True); t = GHOST[1]
s = t; t = say(t, "Q03") + 0.2
shot("apt", s, t, CU("zalata", APT["zalata"], 2.0), CU("zalata", APT["zalata"], 2.3))
# ===== 2. morse: "coming" =====
K2 = [t + 0.15 + d for d in (0, .18, .36, .9, 1.35, 1.8, 2.3, 2.48, 3.0, 3.18)]
for k_ in K2: fx(k_, "mknock", 1.0)
s = t; Q04_T = t + 0.6; t = say(Q04_T, "Q04")
t = max(t, K2[-1] + 0.3) + 0.5
shot("apt", s, t, (940, 420, 1.15), (900, 440, 1.35), wallk2=True)
fx(t - 0.4, "sting", 0.9)
# ===== 3. Shatta tries the pulley =====
s = t; t = say(t, "Q05") + 0.05
shot("apt", s, t, CU("shatta", APT["shatta"], 1.6), CU("shatta", APT["shatta"], 2.5), ease="crash")
RUN = (t, t + 1.1)
shot("apt", t, RUN[1], (1250, 560, 1.15), (1400, 540, 1.25)); t = RUN[1]
cut(t, 0.6); WIN = (t, 0)
fx(t, "wind", 1.4); fx(t + 0.5, "creak", 0.9); fx(t + 2.6, "wind", 1.1)
WIN_PULL = t + 1.3
s = t; t = say(t + 1.2, "Q06")
YANK = t + 0.05; fx(YANK, "whoosh", 1.0); fx(YANK + 0.3, "boom", 0.35); shakes.append((YANK + 0.3, 14))
t = YANK + 0.7; WIN = (s, t)
shot("window", s, t, (980, 520, 1.0), (1000, 640, 1.3))
# ===== 4. torch dies, darkness, the door opens =====
cut(t, 0.4); s = t; Q07_T = t; t = say(t, "Q07") + 0.15
shot("apt", s, t, CU("tota", APT["tota"], 1.9), CU("tota", APT["tota"], 2.2), dark=True)
TORCH_OFF = t; fx(t, "tick", 1.5)
BLACK = (t, t + 2.3); fx(t + 0.7, "lock", 1.3); fx(t + 1.6, "creak", 1.3)
shot("apt", t, BLACK[1], (960, 560, 1.15), blackout=True); t = BLACK[1]
DOOR_OPEN = t - 0.6
SIL = (t, t + 2.6)
Q08_T = t + 0.75; say(Q08_T, "Q08"); shakes.append((Q08_T, 14))
for w_ in KIDS: jump(w_, Q08_T)
fx(t + 0.05, "sting", 1.1)
shot("apt", t, SIL[1], (620, 560, 1.15), (520, 580, 1.28)); t = SIL[1]
BW = (t, t + 1.1)
s = t; t = say(t + 0.9, "Q09") + 0.15
shot("apt", s, t, (560, 560, 1.15), (500, 560, 1.4))
s = t; t = say(t, "Q10") + 0.1
shot("apt", s, t, CU("zalata", APT["zalata"], 2.0), CU("zalata", APT["zalata"], 2.25))
s = t; t = say(t, "Q11") + 0.2
shot("apt", s, t, CU("bondo2", BONDO_POS, 1.9), CU("bondo2", BONDO_POS, 2.2))
# ===== 5. flashback =====
cut(t, 0.7); FLASH = (t, 0); t += 0.35
s = FLASH[0]; t = say(t, "Q12") + 0.4; FLASH = (s, t)
WALK_R = (s + 5.0, s + 7.6)
shot("flash", s, t, (900, 540, 1.05), (1120, 520, 1.2), flash=True)
cut(t, 0.6); s = t; t = say(t + 0.1, "Q13") + 0.1
shot("apt", s, t, CU("tota", APT["tota"], 2.0), CU("tota", APT["tota"], 2.3))
s = t; t = say(t, "Q14"); mid = s + 3.9
shot("apt", s, mid, CU("bondo2", BONDO_POS, 2.0), CU("bondo2", BONDO_POS, 2.3))
shot("apt", mid, t + 0.2, (820, 600, 1.05), (860, 580, 1.2)); t += 0.2
s = t; t = say(t, "Q15") + 0.1
shot("apt", s, t, CU("shatta", APT["shatta"], 1.9), CU("shatta", APT["shatta"], 2.2))
s = t; Q16_T = t; fx(t + 2.0, "sting", 1.2); t = say(t, "Q16") + 0.2
shot("apt", s, t, CU("bondo2", BONDO_POS, 1.8), CU("bondo2", BONDO_POS, 2.9), dark=True)
REACT = (t, t + 1.2); fx(t, "boom", 0.6)
for w_ in KIDS: jump(w_, t + 0.05)
shot("apt", t, REACT[1], (940, 600, 1.25), (940, 600, 1.12), dark=True); t = REACT[1]
# ===== 6. the clue =====
STEP = t + 0.25; fx(STEP, "crinkle", 1.4)
shot("apt", t, t + 0.9, (900, 640, 1.4)); t += 0.9
INS = (t, t + 1.9); fx(t + 0.2, "sting", 0.8)
shot("apt", t, INS[1], (WRAP[0], 980, 3.0), (WRAP[0], 1000, 3.9), wrap=True); t = INS[1]
PICK = t
PUZ = t; s = t; t = say(t + 0.1, "Q17") + 0.6; PUZ_END = t
shot("apt", s, t, CU("tota", APT["tota"], 2.1), CU("tota", APT["tota"], 2.5))
# ===== 7. ending: the stairwell =====
cut(t, 0.6); s = t; t += 1.5
shot("door7", s, t, (420, 640, 1.35), (380, 660, 1.5)); PEEK = (s, t)
s = t; t = say(t + 0.3, "Q18") + 0.9
shot("well", s, t, (960, 560, 1.0), (990, 700, 2.0), ease=None)
s = t; t = say(t, "Q19") + 0.2
shot("door7", s, t, CU("zalata", D7["zalata"], 2.1), CU("zalata", D7["zalata"], 2.6), ease="crash")
LOOKUP = t + 1.0; fx(LOOKUP, "sting", 1.2)
shot("stairs", t, t + 2.6, CU("fahmy", FAHMY_CU, 1.6), CU("fahmy", FAHMY_CU, 2.6), dark=True); t += 2.6
fx(t, "boom", 1.0); shot("black", t, t + 0.5, None); t += 0.5
shot("endcard", t, t + 3.4, None); t += 3.4
TOTAL = t

STEPS = []
def contacts(t0, t1, rate, g0=0.7, g1=0.7, jingle=False):
    n = math.ceil(t0 * rate / math.pi)
    while True:
        tc = n * math.pi / rate
        if tc >= t1: break
        if tc >= t0: STEPS.append((tc, g0 + (g1 - g0) * (tc - t0) / max(1e-3, t1 - t0), jingle))
        n += 1
contacts(RUN[0], RUN[1], 9, 0.6, 0.6)
contacts(BW[0], BW[1], 7, 0.6, 0.9, True)

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
def kk(tt, a, b): return min(1, max(0, (tt - a) / max(1e-3, b - a)))

def night(img, lvl=1.0, tint=(255, 255, 255)):
    return ImageChops.multiply(ImageEnhance.Brightness(img).enhance(lvl), Image.new("RGB", img.size, tint))
_flash = Image.open("bg/flash.png").convert("RGB")
SRCBG = {"apt": Image.open("/home/claude/s1e8/bg/apt7_raw.png").convert("RGB"),
         "door7": Image.open("/home/claude/s1e2/bg/door7.png").convert("RGB"),
         "window": Image.open("bg/window.png").convert("RGB"),
         "well": Image.open("bg/well.png").convert("RGB"),
         "flash": _flash,
         "stairs": night(Image.open(E1 + "bg/stairs.png").convert("RGB"), 0.55, (150, 165, 215))}
TINT = {"apt": (170, 185, 235), "door7": (175, 190, 255), "window": (165, 180, 240), "well": (175, 185, 235),
        "flash": (255, 245, 225), "stairs": (160, 170, 220)}
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
    if sh.get("wallk") and any(0 <= tt - k_ < 0.1 for k_ in WALLK): shake = max(shake, 7)
    if sh.get("wallk2") and any(0 <= tt - k_ < 0.1 for k_ in K2): shake = max(shake, 5)
    if sh["set"] == "window": shake = max(shake, 2.5 + 2.5 * math.sin(tt * 1.7) ** 2)
    cw, ch = W / z, H / z
    if not sh.get("flash"):
        cx += math.sin(tt * 0.9) * 6 + math.sin(tt * 2.3) * 2.5; cy += math.sin(tt * 1.3 + 1) * 4
    x0 = min(max(cx - cw / 2, 0), W - cw); y0 = min(max(cy - ch / 2, 0), H - ch)
    if shake:
        x0 = min(max(x0 + rng.normal(0, shake / z), 0), W - cw); y0 = min(max(y0 + rng.normal(0, shake / z), 0), H - ch)
    return x0, y0, z

def actors(set_, tt, sh):
    A = []
    if set_ == "apt":
        for who, (x, y, s) in APT.items():
            a = dict(who=who, x=x, y=y, s=s, look=0, expr="scared", arms="down")
            if who == "tota" and tt < TORCH_OFF: a["held"] = "torch"; a["arms"] = "hold"
            if who == "tota" and tt >= PICK: a["held"] = "sweet"
            if who == "shatta" and RUN[0] <= tt < RUN[1] + 0.01:
                k = kk(tt, RUN[0], RUN[1]); a["x"] = lerp(x, 1780, ease(k)); a["walk"] = tt * 9; a["look"] = 1; a["arms"] = "up"
            if tt >= DOOR_OPEN:
                a["look"] = -1
                if tt < BW[1] + 1.0: a["expr"] = "shock"; a["arms"] = "scared"
                elif tt < Q16_T + 1.8: a["expr"] = "neutral" if who != "zalata" else "flat"
                else: a["expr"] = "shock"; a["arms"] = "scared"
                if PICK - 2.8 <= tt and tt >= REACT[1]: a["expr"] = "scared"
            if who == "shatta" and STEP - 0.3 <= tt < PICK:
                a["x"] = lerp(x, WRAP[0] + 55, ease(kk(tt, STEP - 0.3, STEP))); a["look"] = 0
            if who == "tota" and tt >= PICK: a["look"] = 0
            A.append(a)
        if tt >= DOOR_OPEN:
            if tt < BW[0]:
                A.append(dict(who="bondo2", x=175, y=1005, s=2.15, look=1, held="lantern", arms="hold", sil=True,
                              alpha=kk(tt, DOOR_OPEN, DOOR_OPEN + 0.5), expr="flat"))
            else:
                k = kk(tt, BW[0], BW[1])
                A.append(dict(who="bondo2", x=lerp(175, BONDO_POS[0], ease(k)), y=1005, s=2.15, look=1, held="lantern", arms="hold",
                              walk=tt * 7 if k < 1 else None, expr="scared" if tt >= Q16_T else ("sad" if FLASH[0] <= tt < FLASH[1] + 6 else "flat")))
    elif set_ == "window":
        k = kk(tt, YANK, YANK + 0.35)
        sway = math.sin(tt * 2.1) * 0.5
        A.append(dict(who="shatta", x=lerp(905, 560, ease(k)), y=lerp(1350, 1700, ease(k)), s=3.2, look=1, expr="shock" if tt < WIN_PULL + 0.4 else "scared",
                      arms="point", lean=0.8 + sway if k < 0.01 else -0.6))
        kz = kk(tt, WIN_PULL, WIN_PULL + 0.5)
        if tt >= WIN_PULL:
            A.append(dict(who="zalata", x=lerp(-350, 300, ease(kz)) - 260 * ease(k), y=1420, s=3.0, look=1, expr="flat", arms="point"))
    elif set_ == "flash":
        k = kk(tt, WALK_R[0], WALK_R[1])
        A.append(dict(who="youngnana", x=720, y=935, s=1.75, look=1, expr="happy", arms="down"))
        A.append(dict(who="roshdy", x=lerp(1020, 1480, ease(k)), y=935, s=1.75, look=1 if k > 0 else -1, expr="smug" if k > 0 else "happy",
                      held="paper", arms="hold", walk=tt * 7 if 0 < k < 1 else None))
    elif set_ == "door7":
        for who, (x, y, s) in D7.items():
            a = dict(who=who, x=x, y=y, s=s, look=-1, expr="scared", arms="down")
            if who == "tota": a["arms"] = "shush"; a["held"] = "sweet"
            A.append(a)
    elif set_ == "well":
        A.append(dict(who="fahmy", x=990, y=800, s=0.55, look=0, expr="smug", arms="shush", held="phone"))
    elif set_ == "stairs":
        x, y, s = FAHMY_CU
        up = tt >= LOOKUP
        A.append(dict(who="fahmy", x=x, y=y, s=s, look=1 if not up else 0, expr="neutral" if not up else "smug",
                      arms="shush" if not up else "down", held="phone"))
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

def torch_level(tt):
    if tt >= TORCH_OFF: return 0.0
    if tt >= Q07_T:
        r = (math.sin(tt * 47) + math.sin(tt * 31.7) + math.sin(tt * 13)) / 3
        return max(0.0, 0.55 + 0.6 * r) * (1 - kk(tt, Q07_T, TORCH_OFF) * 0.4)
    return 1.0

def draw_scene_chars(set_, tt, cam, sh):
    x0, y0, z = cam
    layer = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(layer)
    k, lt = line_at(tt); lights = []; hand = None
    insert = sh.get("ghost") or sh.get("wrap") or (sh.get("patch") and set_ == "apt")
    for a in ([] if insert else sorted(actors(set_, tt, sh), key=lambda a: a["s"])):
        who = a["who"]; talking = k is not None and WHO[k] == who and not (set_ == "flash")
        expr = a.get("expr", "neutral")
        if talking: expr = expr_of(k, lt)
        mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
        arms = a.get("arms", "down")
        if talking and who != "bondo2": arms = ARMS.get(k, "talk" if arms == "down" else arms)
        if set_ == "window": arms = a["arms"]
        if a.get("held") == "torch": arms = "point" if (talking and ARMS.get(k) == "point") else "hold"
        bob = abs(math.sin(a["walk"])) * 5 * a["s"] if a.get("walk") is not None else 0
        wy = a["y"] - jump_off(who, tt) - bob
        shiver = math.sin(tt * 60) * 2.5 if expr in ("scared", "shock") and who in KIDS else 0
        blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11 and expr != "sleepy"
        X = (a["x"] + shiver - x0) * z; Y = (wy - y0) * z; s = a["s"] * z
        target = p; L = None
        if a.get("alpha", 1) < 1 or a.get("sil"): L = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); target = P(L)
        target.ell(X, (a["y"] - y0) * z + 4 * s, 46 * s, 9 * s, (0, 0, 0, 110), None)
        draw_char(target, who, X, Y, s, expr, mouth, a.get("look", 0), blink, arms, tt, a.get("held"), a.get("lean", 0), a.get("walk"))
        if L is not None:
            al_ = a.get("alpha", 1)
            if a.get("sil"):
                rgb = Image.new("RGB", L.size, (10, 9, 12)); al = L.getchannel("A")
                L = rgb.convert("RGBA"); L.putalpha(al)
            L.putalpha(L.getchannel("A").point(lambda v: int(v * al_))); layer = Image.alpha_composite(layer, L); p = P(layer)
        S = s * CH[who]["scale"]
        if who == "bondo2": lights.append((X + 46 * S, Y - 75 * S, 400 * z, 1.0 * a.get("alpha", 1), (1.0, 0.75, 0.45)))
        if who == "fahmy" and a.get("held") == "phone":
            if arms == "shush": lights.append((X + 4 * S, Y - 165 * S, 260 * max(0.6, z * s / 2.4), 1.2, (0.6, 0.8, 1.1)))
            else: lights.append((X + 34 * S, Y - 70 * S, 300 * z, 0.9, (0.6, 0.8, 1.1)))
        if who == "tota" and a.get("held") == "torch":
            hand = (X + (84 if arms == "point" else 46) * S, Y - (140 if arms == "point" else 104) * S)
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
    if sh.get("patch") or sh.get("wallk2") or sh.get("wallk"): wx, wy = 945, 260
    else: wx, wy = 900 + math.sin(tt * 0.8) * 240, 420 + math.sin(tt * 1.3) * 60
    return (wx - x0) * z, (wy - y0) * z, 300 * z

def light_map(set_, sh, tt, cam, lights, hand):
    x0, y0, z = cam; W3 = lambda px, py: ((px - x0) * z, (py - y0) * z)
    if set_ == "door7":
        m = np.full((LH, LW, 3), 0.36, np.float32) * np.array([0.8, 0.9, 1.05], np.float32)
        X, Y = W3(150, 860); m += 0.55 * glow(X, Y, 520 * z)[..., None] * np.array([0.8, 0.9, 1.0], np.float32)
    elif set_ == "window":
        m = np.full((LH, LW, 3), 0.62, np.float32) * np.array([0.8, 0.9, 1.1], np.float32)
        X, Y = W3(750, 585); m += 0.6 * glow(X, Y, 160 * z)[..., None] * np.array([1.0, 0.7, 0.4], np.float32)
        X, Y = W3(280, 60); m += 0.5 * glow(X, Y, 500 * z)[..., None] * np.array([0.8, 0.9, 1.1], np.float32)
    elif set_ == "well":
        m = np.full((LH, LW, 3), 0.5, np.float32) * np.array([0.8, 0.9, 1.08], np.float32)
        X, Y = W3(990, 760); m += 0.8 * glow(X, Y, 140 * z)[..., None] * np.array([1.0, 0.8, 0.5], np.float32)
    elif set_ == "stairs":
        m = np.full((LH, LW, 3), 0.42, np.float32) * np.array([0.75, 0.85, 1.1], np.float32)
    else:
        dark_ = 0.24 if tt >= TORCH_OFF else 0.3
        m = np.full((LH, LW, 3), dark_, np.float32) * np.array([0.75, 0.85, 1.1], np.float32)
        X, Y = W3(1650, 300); m += 0.85 * glow(X, Y, 520 * z)[..., None] * np.array([0.75, 0.85, 1.1], np.float32)
        if tt >= DOOR_OPEN:
            fl = kk(tt, DOOR_OPEN, DOOR_OPEN + 0.8) * (0.9 + 0.1 * math.sin(tt * 23))
            X, Y = W3(-60, 640); m += 1.3 * fl * glow(X, Y, 520 * z)[..., None] * np.array([1.0, 0.72, 0.42], np.float32)
        if sh.get("wrap"):
            X, Y = W3(WRAP[0] - 200, WRAP[1] - 60); m += 1.1 * glow(X, Y, 320 * z)[..., None] * np.array([1.0, 0.75, 0.45], np.float32)
    for X, Y, R, inten, col in lights:
        m += inten * glow(X, Y, R)[..., None] * np.array(col, np.float32)
    spot = None
    tl = torch_level(tt)
    if hand and set_ == "apt" and tl > 0:
        tx, ty, R = torch_target(sh, tt, cam); spot = glow(tx, ty, R) * tl
        m += 1.8 * spot[..., None] * np.array([1.0, 0.97, 0.85], np.float32)
        m += 0.35 * tl * glow(hand[0], hand[1], 240 * z)[..., None] * np.array([1.0, 0.95, 0.85], np.float32)
    elif set_ == "apt" and (sh.get("patch") or sh.get("ghost")) and tt < TORCH_OFF:   # insert: torch from off-screen
        tx, ty, R = torch_target(sh, tt, cam); spot = glow(tx, ty, R)
        m += 1.6 * spot[..., None] * np.array([1.0, 0.97, 0.85], np.float32)
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

def door_beam(fr, tt, cam):
    if tt < DOOR_OPEN: return
    x0, y0, z = cam; k = kk(tt, DOOR_OPEN, DOOR_OPEN + 0.8)
    ov = Image.new("L", (W // 2, H // 2), 0); d = ImageDraw.Draw(ov)
    P_ = lambda wx, wy: ((wx - x0) * z / 2, (wy - y0) * z / 2)
    d.polygon([P_(-40, 380), P_(60, 330), P_(900, 1090), P_(-40, 1090)], fill=int(60 * k))
    ov = ov.filter(ImageFilter.GaussianBlur(16)).resize((W, H), Image.BILINEAR)
    fr.paste(Image.new("RGB", (W, H), (255, 200, 130)), (0, 0), ov)

def draw_beam(fr, sh, tt, cam, hand):
    tl = torch_level(tt)
    if not hand or tl <= 0: return
    tx, ty, R = torch_target(sh, tt, cam)
    ov = Image.new("L", (W // 2, H // 2), 0); d = ImageDraw.Draw(ov)
    hx, hy = hand[0] / 2, hand[1] / 2; ang = math.atan2(ty - hand[1], tx - hand[0]); w_ = R * 0.6 / 2
    px, py = -math.sin(ang) * w_, math.cos(ang) * w_
    d.polygon([(hx, hy), (tx / 2 + px, ty / 2 + py), (tx / 2 - px, ty / 2 - py)], fill=int(44 * tl))
    ov = ov.filter(ImageFilter.GaussianBlur(14)).resize((W, H), Image.BILINEAR)
    fr.paste(Image.new("RGB", (W, H), (255, 248, 220)), (0, 0), ov)

def wrapper(d, X, Y, S, tt):
    d.ellipse([X - 22 * S, Y - 13 * S, X + 22 * S, Y + 13 * S], fill=(226, 160, 70, 255), outline=(120, 70, 20, 255), width=max(1, int(2 * S)))
    for sx in (-1, 1):
        d.polygon([(X + sx * 20 * S, Y), (X + sx * 44 * S, Y - 16 * S), (X + sx * 38 * S, Y), (X + sx * 46 * S, Y + 14 * S)],
                  fill=(236, 180, 90, 255), outline=(120, 70, 20, 255))
    for i in range(3):
        d.line([(X - 12 * S + i * 10 * S, Y - 9 * S), (X - 6 * S + i * 10 * S, Y + 9 * S)], fill=(160, 100, 30, 255), width=max(1, int(1.5 * S)))
    d.line([(X - 14 * S, Y - 6 * S), (X - 2 * S, Y - 9 * S)], fill=(255, 240, 200, 220), width=max(1, int(2 * S)))
    if int(tt * 4) % 2:
        gx_, gy_ = X + 10 * S, Y - 16 * S
        d.line([(gx_ - 10 * S, gy_), (gx_ + 10 * S, gy_)], fill=(255, 255, 230, 230), width=max(1, int(2 * S)))
        d.line([(gx_, gy_ - 10 * S), (gx_, gy_ + 10 * S)], fill=(255, 255, 230, 230), width=max(1, int(2 * S)))

def apt_props(img, tt, cam, sh):
    x0, y0, z = cam; S = SS * z; d = ImageDraw.Draw(img, "RGBA")
    if sh.get("patch"):
        a_ = int(150 + 100 * math.sin(tt * 6))
        d.rectangle([(825 - x0) * S, (144 - y0) * S, (1065 - x0) * S, (336 - y0) * S], outline=(255, 214, 90, a_), width=max(2, int(6 * S)))
    if sh.get("ghost"):   # ghost of the missing family photo
        k = kk(tt, GHOST[0] + 0.2, GHOST[0] + 1.2) * (0.85 + 0.15 * math.sin(tt * 9))
        g = Image.new("RGBA", img.size, (0, 0, 0, 0)); gd = ImageDraw.Draw(g)
        X0, Y0, X1, Y1 = (835 - x0) * S, (154 - y0) * S, (1055 - x0) * S, (326 - y0) * S
        gd.rectangle([X0, Y0, X1, Y1], fill=(196, 170, 120, int(150 * k)), outline=(90, 60, 30, int(220 * k)), width=max(2, int(8 * S)))
        for i, (fx_, hr) in enumerate(((0.32, 26), (0.62, 22))):
            cx_ = X0 + (X1 - X0) * fx_; cy_ = Y0 + (Y1 - Y0) * 0.38
            gd.ellipse([cx_ - hr * S, cy_ - hr * S, cx_ + hr * S, cy_ + hr * S], fill=(250, 240, 220, int(200 * k)), outline=(60, 40, 20, int(220 * k)), width=max(1, int(2 * S)))
            gd.line([(cx_, cy_ + hr * S), (cx_, cy_ + 70 * S)], fill=(60, 40, 20, int(220 * k)), width=max(1, int(3 * S)))
        g = g.filter(ImageFilter.GaussianBlur(1.5 * S))
        img.paste(g, (0, 0), g)
    if sh.get("wallk") or sh.get("wallk2"):
        for k_ in (WALLK if sh.get("wallk") else K2):
            u = tt - k_
            if 0 <= u < 0.6:
                for i in range(10):
                    px = (845 + i * 22 - x0) * S; py = (336 + u * 300 + (i % 3) * 10 - y0) * S
                    d.ellipse([px - 3 * S, py - 3 * S, px + 3 * S, py + 3 * S], fill=(200, 190, 170, int(220 * (1 - u / 0.6))))
    if tt >= DOOR_OPEN and not sh.get("wrap"):
        k = kk(tt, DOOR_OPEN, DOOR_OPEN + 0.7)
        g = Image.new("RGBA", img.size, (0, 0, 0, 0)); gd = ImageDraw.Draw(g)
        gd.polygon([((40 - x0) * S, (300 - y0) * S), ((330 - x0) * S, (330 - y0) * S), ((330 - x0) * S, (1010 - y0) * S), ((40 - x0) * S, (1040 - y0) * S)],
                   fill=(240, 170, 95, int((200 if tt < BW[0] else 120) * k)))
        g = g.filter(ImageFilter.GaussianBlur(6 * S)); img.paste(g, (0, 0), g)
    if tt < PICK:
        wrapper(d, (WRAP[0] - x0) * S, (WRAP[1] - y0) * S, S * (0.8 if not sh.get("wrap") else 1.0), tt)

def window_props(img, tt, cam):   # the swinging rope + wind streaks
    x0, y0, z = cam; S = SS * z; d = ImageDraw.Draw(img, "RGBA")
    sw = math.sin(tt * 2.1) * 40
    pts = [((1320 + (1140 - 1320) * u + sw * u * u - x0) * S, (195 + 870 * u - y0) * S) for u in np.linspace(0, 1, 14)]
    d.line(pts, fill=(200, 185, 150, 255), width=max(2, int(5 * S)))
    for i in range(14):
        u = (tt * 1.6 + i * 0.13) % 1
        wx = lerp(-200, 2100, u); wy = 120 + (i * 71) % 900
        d.line([((wx - x0) * S, (wy - y0) * S), ((wx + 160 - x0) * S, (wy - 12 - y0) * S)], fill=(210, 225, 255, 60), width=max(1, int(2 * S)))

def bg_frame(set_, cam):
    x0, y0, z = cam; src = SRCBG[set_]; sw, sh = src.size; f = sw / W
    box = (x0 * f, y0 * f, (x0 + W / z) * f, (y0 + H / z) * f)
    if z > 1.6:
        b = tuple(int(v) for v in box); b = (max(0, b[0] - 20), max(0, b[1] - 20), min(sw, b[2] + 20), min(sh, b[3] + 20))
        part = src.crop(b).filter(ImageFilter.GaussianBlur(min(3, (z - 1.5) * 1.3)))
        box = (box[0] - b[0], box[1] - b[1], box[2] - b[0], box[3] - b[1]); src = part
    return src.resize((SSW, SSH), Image.BICUBIC, box=box)

def card(name, tt, sh):
    k = (tt - sh["start"]) / (sh["end"] - sh["start"])
    fr = Image.new("RGB", (W, H), (8, 8, 12))
    g = lambda c: tuple(int(v * min(1, k * 4)) for v in c)
    if name == "title":
        text(fr, W / 2, H / 2 - 80, "عمارة نعناعة", 110, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 + 50, "سر الدور السابع", 64, g((230, 230, 230)))
        text(fr, W / 2, H / 2 + 145, EPT, 48, g((210, 210, 210)))
    elif name == "endcard":
        text(fr, W / 2, H / 2 - 60, "الحلقة الأخيرة بكرة", 104, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 + 70, "مين اللي قفل الباب؟ اكتب في الكومنتات", 48, g((230, 230, 230)))
    return fr

def hud(fr, tt, v=False):
    sc = 0.85 if v else 1.0; cx = 540 if v else W / 2
    if Q02_T + 1.6 <= tt < GHOST[1]:
        d = ImageDraw.Draw(fr, "RGBA"); y = 1700 if v else 120
        d.rounded_rectangle([cx - 470 * sc, y - 50 * sc, cx + 470 * sc, y + 50 * sc], int(22 * sc), fill=(20, 60, 30, 220), outline=(120, 230, 120, 255), width=4)
        text(fr, cx, y, "إجابة امبارح: الصورة اللي كانت على الحيطة ✓", int(40 * sc), (200, 255, 200))

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
    text(bgv, 540, 420, EPT, 52, (235, 235, 235))
    k, _ = line_at(tt)
    if k:
        ls_ = wrap(SUB[k])
        if len(ls_) <= 4:
            for i, l in enumerate(ls_): text(bgv, 540, 1290 + i * 80, l, 60, sw=6)
        else:
            ls_ = wrap(SUB[k], 30)
            for i, l in enumerate(ls_[:6]): text(bgv, 540, 1270 + i * 64, l, 50, sw=5)
    hud(bgv, tt, True)
    if PUZ <= tt < PUZ_END:
        d.rounded_rectangle([40, 1640, 1040, 1800], 26, fill=(20, 20, 30), outline=(255, 214, 90), width=5)
        text(bgv, 540, 1695, "لغز الحلقة: مين اللي قفل الباب؟", 50, (255, 214, 90))
        text(bgv, 540, 1758, "اكتب حلّك في الكومنتات", 42)
    return bgv

def finish(fr, tt, dark=False):
    fr = ImageChops.multiply(fr, VIG_DARK if dark else VIG)
    a = np.asarray(fr, np.float32)
    g = GRAIN[int(tt * FPS) % len(GRAIN)]
    g = np.repeat(np.repeat(g, 2, 0), 2, 1)[..., None]
    return Image.fromarray(np.clip(a + g, 0, 255).astype(np.uint8))

def sepia(fr, tt):
    g = np.asarray(fr.convert("L"), np.float32) / 255
    fl = 0.93 + 0.07 * math.sin(tt * 37) * math.sin(tt * 11)
    out = np.stack([g * 255 * 1.05, g * 220, g * 170], -1) * fl + np.array([18, 10, 0])
    im = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(im, "RGBA"); r = np.random.default_rng(int(tt * FPS))
    for _ in range(3):
        x = r.uniform(0, W); d.line([(x, 0), (x + r.uniform(-20, 20), H)], fill=(40, 30, 20, int(r.uniform(30, 90))), width=2)
    for _ in range(14):
        x, y = r.uniform(0, W), r.uniform(0, H); rr = r.uniform(1, 3.5)
        d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=(30, 22, 12, 140))
    return ImageChops.multiply(im, VIG)

def eyes_only(tt, sh):
    fr = Image.new("RGB", (W, H), (0, 0, 0)); d = ImageDraw.Draw(fr)
    x0, y0, z = cam_at(sh, tt)
    for who, (x, y, s) in APT.items():
        S = s * CH[who]["scale"] * z
        hx = (x - x0) * z + math.sin(tt * 50 + x) * 2; hy = (y - y0) * z - 190 * S
        if ((tt + (hash(who) % 5) * 0.4) % 2.2) < 0.12:
            for sx in (-1, 1): d.line([(hx + sx * 15 * S - 8 * S, hy), (hx + sx * 15 * S + 8 * S, hy)], fill=(160, 160, 160), width=3)
            continue
        look = -1 if tt > BLACK[0] + 1.6 else math.sin(tt * 3 + x)
        for sx in (-1, 1):
            ex = hx + sx * 15 * S; er = 12 * S
            d.ellipse([ex - er * 0.82, hy - er, ex + er * 0.82, hy + er], fill=(235, 235, 240))
            pr = 2.8 * S; px = ex + look * 4 * S
            d.ellipse([px - pr, hy - pr, px + pr, hy + pr], fill=(0, 0, 0))
    return fr

def frame(tt):
    sh = shot_at(tt); set_ = sh["set"]
    if set_ in ("title", "endcard"): return finish(card(set_, tt, sh), tt)
    if set_ == "black": return Image.new("RGB", (W, H), (0, 0, 0))
    if sh.get("blackout"): return finish(eyes_only(tt, sh), tt, True)
    cam = cam_at(sh, tt)
    img = bg_frame(set_, cam)
    if set_ == "apt": apt_props(img, tt, cam, sh)
    if set_ == "window": window_props(img, tt, cam)
    layer, lights, hand = draw_scene_chars(set_, tt, cam, sh)
    if set_ != "flash": layer = tint_layer(layer, TINT[set_], 0.95)
    img.paste(layer, (0, 0), layer)
    fr = img.resize((W, H), Image.LANCZOS)
    if set_ == "flash":
        if tt - FLASH[0] < 0.25: fr = Image.blend(fr, Image.new("RGB", (W, H), (255, 250, 235)), 1 - (tt - FLASH[0]) / 0.25)
        return finish(sepia(fr, tt), tt)
    lm, spot = light_map(set_, sh, tt, cam, lights, hand)
    fr = ImageChops.multiply(fr, lm); fr = ImageEnhance.Brightness(fr).enhance(1.65)
    if spot is not None:
        sp = Image.fromarray((np.clip(spot, 0, 1) * 255).astype(np.uint8)).resize((W, H), Image.BILINEAR)
        fr = Image.composite(ImageChops.screen(fr, Image.new("RGB", (W, H), (100, 96, 80))), fr, sp)
    if set_ == "apt":
        moonbeams(fr, tt, cam); draw_beam(fr, sh, tt, cam, hand); door_beam(fr, tt, cam)
    if set_ == "stairs" and tt >= LOOKUP:   # eye + bow-tie glint
        x0, y0, z = cam; x, y, s = FAHMY_CU; S = s * CH["fahmy"]["scale"] * z
        k = kk(tt, LOOKUP, LOOKUP + 0.25) * (1 - kk(tt, LOOKUP + 0.6, LOOKUP + 1.2))
        if k > 0:
            dd = ImageDraw.Draw(fr, "RGBA"); hx = (x - x0) * z; hy = (y - y0) * z - 190 * S
            for sx in (-1, 1):
                ex, ey = hx + sx * 15 * S + 3 * S, hy - 2 * S
                dd.line([(ex - 16 * S * k, ey), (ex + 16 * S * k, ey)], fill=(255, 255, 255, 230), width=3)
                dd.line([(ex, ey - 16 * S * k), (ex, ey + 16 * S * k)], fill=(255, 255, 255, 230), width=3)
    if tt - FLASH[1] < 0.2 and tt >= FLASH[1]:
        fr = Image.blend(fr, Image.new("RGB", (W, H), (255, 250, 235)), 1 - (tt - FLASH[1]) / 0.2)
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
            text(h, W / 2, 117, "لغز الحلقة: مين اللي قفل الباب؟ اكتب في الكومنتات", 38, (255, 214, 90))
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
        if s_["set"] == "flash": env[int(s_["start"] * SR):int(s_["end"] * SR)] = 0.3
    env = np.convolve(env, np.ones(4410) / 4410, mode="same")
    mix_into(buf, dr * env, 0, 1.1)
    r = np.random.default_rng(9); ts = np.arange(int(SR * 1.6)) / SR
    k_ = sfx_knock()
    S = {"boom": sfx_boom(), "tick": sfx_tick() * 3, **SFXF}
    S["mknock"] = np.convolve(k_, np.ones(30) / 30, mode="same") * 1.4
    S["sting"] = (np.sin(2 * np.pi * (1200 + 80 * np.sin(ts * 40)) * ts) * 0.08 + np.sin(2 * np.pi * 1263 * ts) * 0.06
                  + np.sin(2 * np.pi * 55 * ts) * 0.4) * np.exp(-ts * 1.8)
    for t0, n, g in sfx:
        if n in S: mix_into(buf, S[n], t0, g)
    # torch buzz while flickering
    n_ = int((TORCH_OFF - Q07_T) * SR); tz = np.arange(n_) / SR
    bz = np.sign(np.sin(2 * np.pi * 100 * tz)) * 0.03 * (np.sin(tz * 47) > 0.2)
    mix_into(buf, bz.astype(np.float32), Q07_T, 1.0)
    # music box for the flashback (soft, nostalgic)
    notes = [523.25, 659.25, 783.99, 659.25, 587.33, 698.46, 880.0, 698.46, 523.25, 659.25, 783.99, 1046.5]
    for i, f in enumerate(notes * 2):
        tn = FLASH[0] + 0.4 + i * 0.42
        if tn > FLASH[1] - 0.4: break
        tt_ = np.arange(int(SR * 1.2)) / SR
        mix_into(buf, (np.sin(2 * np.pi * f * tt_) + 0.3 * np.sin(4 * np.pi * f * tt_)) * np.exp(-tt_ * 3.5) * 0.06, tn, 1.0)
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
    elif sys.argv[1:2] == ["times"]:
        for s_ in shots: print(s_["set"], round(s_["start"], 2), round(s_["end"], 2), {k: v for k, v in s_.items() if v is True})
    else:
        build_audio()
        render("h.mp4", "v.mp4")
        mux("h.mp4", "sirr_eldor_elsabe3_ep9.mp4"); mux("v.mp4", "sirr_eldor_elsabe3_ep9_vertical.mp4")
        print("done")
