import sys, os, math, subprocess, wave
sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter, ImageFont
from engine import *

os.chdir(ROOT + "/s1e10")
SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(101)
E1 = ROOT + "/s1e1/"
EPT = "الحلقة 10: الحقيقة"

SUB = {
 "R01": "الليلة... هنمسكه.",
 "R02": "لغز امبارح: مين اللي قفل علينا الباب؟... أستاذ فهمي! البونبوني بتاعه هو اللي فضحه!",
 "R03": "الخطة: شطة في البدروم عند مفتاح النور. أنا وتوتة فوق عند فتحة التهوية. والبواب على السلم.",
 "R04": "البدروم؟! لوحدي؟... في العتمة؟",
 "R05": "إيه يا شطة... خايف من العتمة؟",
 "R06": "أنا؟! أبداً... ثقوا فيا!",
 "R07": "وأنا معاكو! طنط سوسن هتصور كل حاجة... لايف!",
 "R08": "رشدي أخويا... ساب سر في العمارة دي؟... يبقى أنا جاية معاكو. والشبشب جاي معايا!",
 "R09": "خلاص... كله في مكانه.",
 "R10": "النور راح... وأنا لوحدي.",
 "R11": "ده... أستاذ فهمي!",
 "R12": "نخوفهم شوية كمان... وبكرة يمضوا على البيع.",
 "R13": "مش الليلة يا أستاذ فهمي!",
 "R14": "إنت؟!",
 "R15": "بص يا زلطة! سلك نازل من فتحة التهوية... لحد شباك الدور الخامس!",
 "R16": "سماعة. يعني العفريت... بيشتغل بالكهربا.",
 "R17": "أهلاً يا متابعين! إحنا لايف... وده يا جماعة أستاذ فهمي، اللي بيخوف العمارة كلها!",
 "R18": "ما تشغلوش بالكم يا حلوين... العمارة هتتباع بكرة، والسر اللي بتدوروا عليه ضاع من تلاتين سنة!",
 "R19": "لا... ما ضاعش. أنا عارفة هو فين.",
 "R20": "البكرة! عم رشدي خباه في البكرة!",
 "R21": "ده خط رشدي... العمارة دي بتاعة السكان كلهم... ومش هتتباع!",
 "R22": "رشدي... يا حبيبي. لسه بيحافظ علينا من بعيد.",
 "R23": "رايح فين يا فهمي؟!... الشبشب جايلك!",
 "R24": "أنا صاحي أهو.",
 "R25": "مليون مشاهدة يا جماعة!",
 "R26": "شفتوا؟ قلتلكو ثقوا فيا!",
 "R27": "أنا كنت حاسبها بالقلم من الأول.",
 "R28": "لغز النهارده: إنتو خمنتوا من الأول إن فهمي هو اللي ورا الخبط؟ اكتبوا في الكومنتات!",
 "R29": "جواب... من برا مصر!",
 "R30": "ده خط رشدي!... افتحوا البدروم.",
 "R31": "البدروم؟!... تاني؟!",
}
WHO = {"R01": "shatta", "R02": "tota", "R03": "zalata", "R04": "shatta", "R05": "tota", "R06": "shatta", "R07": "sawsan",
       "R08": "nana", "R09": "zalata", "R10": "shatta", "R11": "shatta", "R12": "fahmy", "R13": "shatta", "R14": "fahmy",
       "R15": "tota", "R16": "zalata", "R17": "sawsan", "R18": "fahmy", "R19": "tota", "R20": "tota", "R21": "bondo2",
       "R22": "nana", "R23": "nana", "R24": "bondo2", "R25": "sawsan", "R26": "shatta", "R27": "zalata", "R28": "tota",
       "R29": "bondo2", "R30": "nana", "R31": "shatta"}
EXPR = {"R01": "angry", "R02": [(0, "neutral"), (0.45, "happy")], "R03": "neutral", "R04": "scared", "R05": "smug",
        "R06": [(0, "shock"), (0.35, "happy")], "R07": "happy", "R08": [(0, "sad"), (0.55, "angry")], "R09": "flat",
        "R10": "scared", "R11": "shock", "R12": "smug", "R13": "angry", "R14": "shock", "R15": "happy", "R16": "flat",
        "R17": "happy", "R18": [(0, "scared"), (0.4, "smug")], "R19": "smug", "R20": "happy", "R21": "sad", "R22": "sad",
        "R23": "angry", "R24": "sleepy", "R25": "happy", "R26": "happy", "R27": "smug", "R28": [(0, "neutral"), (0.6, "smug")],
        "R29": "shock", "R30": "shock", "R31": "shock"}
ARMS = {"R01": "hips", "R02": "point", "R03": "hold", "R04": "scared", "R05": "hips", "R06": "hips", "R07": "up", "R08": "up",
        "R09": "shush", "R10": "hold", "R11": "hold", "R12": "up", "R13": "up", "R14": "scared", "R15": "point", "R16": "down",
        "R17": "hold", "R18": "talk", "R19": "hips", "R20": "up", "R21": "hold", "R22": "talk", "R23": "up", "R24": "hips",
        "R25": "up", "R26": "up", "R27": "hold", "R28": "point", "R29": "hold", "R30": "hold", "R31": "up"}

AUD = {k: load_audio(f"audio/{k}.mp3") for k in SUB}
ENV = {k: envelope(v) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}
SFXF = {n: load_audio(f"sfx/{n}.mp3") for n in ("whoosh", "creak", "slam", "lock", "wind", "crinkle", "radio", "slipper", "switch", "cheer")}

lines, sfx, shots, jumps, shakes = [], [], [], {}, []
def say(t, k): lines.append((t, k)); return t + DUR[k]
def fx(t, n, g=1.0): sfx.append((t, n, g))
def jump(w, t): jumps.setdefault(w, []).append(t)
def shot(set_, s, e, c0, c1=None, **kw):
    shots.append(dict(set=set_, start=s, end=e, c0=c0, c1=c1 or c0, **kw))
def cut(t, g=0.45): fx(t - 0.12, "whoosh", g)
KIDS = ("shatta", "zalata", "tota")

BED = {"shatta": (620, 1030, 2.4), "zalata": (960, 1030, 2.4), "tota": (1300, 1030, 2.4)}
LIV = {"tota": (380, 1030, 2.0), "shatta": (560, 1030, 2.0), "nana": (850, 1030, 2.1), "zalata": (1110, 1030, 2.0), "sawsan": (1430, 1030, 2.1)}
ROOF = {"tota": (800, 830, 1.5), "zalata": (1200, 830, 1.5)}
SH_B = (820, 1050, 2.3); FA_BOX = (1560, 1060, 2.6)
FAPT = {"fahmy": (1300, 1045, 2.4), "sawsan": (600, 1045, 2.3), "tota": (380, 1045, 2.2), "shatta": (200, 1045, 2.2), "zalata": (40, 1045, 2.2)}
GRP = {"sawsan": (400, 1000, 1.9), "bondo2": (660, 1000, 1.9), "nana": (900, 1000, 1.9), "tota": (1120, 1000, 1.9), "shatta": (1300, 1000, 1.9), "zalata": (1480, 1000, 1.9)}
LOB = {"fahmy": (240, 1020, 1.85), "bondo2": (420, 1020, 1.85), "nana": (640, 1020, 1.85), "tota": (840, 1020, 1.85), "shatta": (1010, 1020, 1.85),
       "zalata": (1180, 1020, 1.85), "sawsan": (1400, 1020, 1.85)}
MOR = {"bondo2": (520, 1030, 2.2), "nana": (780, 1030, 2.2), "tota": (1000, 1030, 2.1), "shatta": (1160, 1030, 2.1), "zalata": (1320, 1030, 2.1)}
D7N = (1000, 1030, 2.2)
def CU(who, pos, z=2.2, dx=0):
    x, y, s = pos; S = s * CH[who]["scale"]
    if who == "tota": z *= 1.3; dx -= 50
    hy = y - 190 * S
    return (x + dx, hy + H / (2 * z) - 1.45 * 46 * S - 25, z)

t = 0.0
# ===== 0. HOOK =====
fx(0.1, "sting", 0.9)
HOOK = (0, 3.0)
shot("stairs", 0, 3.0, (1300, 560, 1.15), (1200, 640, 1.45), dark=True, hookfahmy=True)
t = 3.0; cut(t, 0.5); s = t; t = say(t + 0.1, "R01") + 0.3
shot("bedroom", s, t, CU("shatta", BED["shatta"], 1.6), CU("shatta", BED["shatta"], 2.5), ease="crash", dark=True, torchface=True)
cut(t, 0.6); fx(t, "boom", 0.8); shot("title", t, t + 1.7, None); t += 1.7
# ===== 1. answer + plan =====
cut(t, 0.4); s = t; R02_T = t + 0.1; t = say(R02_T, "R02") + 0.1
shot("bedroom", s, t, CU("tota", BED["tota"], 1.5), CU("tota", BED["tota"], 1.7))
s = t; R03_T = t; t = say(t, "R03") + 0.15
d3 = DUR["R03"]
PLAN = [(s, s + d3 * 0.12), (s + d3 * 0.12, s + d3 * 0.42), (s + d3 * 0.42, s + d3 * 0.76), (s + d3 * 0.76, t)]
shot("bedroom", PLAN[0][0], PLAN[0][1], CU("zalata", BED["zalata"], 2.0))
shot("basement", PLAN[1][0], PLAN[1][1], (1650, 420, 1.6), (1690, 400, 2.1), insert=True)
shot("roof", PLAN[2][0], PLAN[2][1], (990, 600, 1.8), (990, 610, 2.4), insert=True)
shot("stairs", PLAN[3][0], PLAN[3][1], (1200, 600, 1.2), (1250, 560, 1.4), insert=True)
for a_, b_ in PLAN[1:]: fx(a_ - 0.08, "whoosh", 0.5)
cut(t, 0.4); s = t; t = say(t, "R04") + 0.1
shot("bedroom", s, t, CU("shatta", BED["shatta"], 1.7), CU("shatta", BED["shatta"], 2.6), ease="crash")
s = t; t = say(t, "R05") + 0.05
shot("bedroom", s, t, CU("tota", BED["tota"], 1.55), CU("tota", BED["tota"], 1.75))
s = t; t = say(t, "R06") + 0.3
shot("bedroom", s, t, CU("shatta", BED["shatta"], 2.2), CU("shatta", BED["shatta"], 2.0))
# ===== 2. Sawsan + Nana join =====
cut(t, 0.5); SAW_IN = (t, t + 1.0); fx(t + 0.1, "creak", 0.6)
s = t; t = say(t + 0.7, "R07") + 0.1
shot("living", s, t, (1150, 600, 1.15), (1250, 580, 1.3))
s = t; R08_T = t; t = say(t, "R08") + 0.3
shot("living", s, t, CU("nana", LIV["nana"], 1.8), CU("nana", LIV["nana"], 2.3))
SLIPPER_UP = R08_T + DUR["R08"] * 0.62
# ===== 3. hide and wait =====
cut(t, 0.5); s = t; t = say(t + 0.4, "R09") + 0.3
shot("roof", s, t, (1000, 640, 1.3), (1000, 660, 1.6))
CLOCK = (t, t + 2.6); TICK12 = t + 1.6
for i in range(4): fx(t + 0.3 + i * 0.4, "tock", 1.0)
fx(TICK12, "boom", 0.9)
shot("clock", t, CLOCK[1], None); t = CLOCK[1]
# 12:00 — knocking + power cut
KN = [t + 0.1 + d for d in (0, .25, .5, 1.1, 1.35, 1.6)]
for k_ in KN: fx(k_, "knock", 1.2)
shot("roof", t, t + 2.0, (990, 600, 1.9), (990, 600, 2.6), vent=True); t += 2.0
POWER_OFF = t; fx(t, "powercut", 1.3); shakes.append((t, 10))
shot("basement", t, t + 0.6, (900, 600, 1.2), blackout=True); t += 0.6
TORCH_ON = t; fx(t, "tick", 1.5)
s = t; t = say(t + 0.3, "R10") + 0.2
shot("basement", s, t, CU("shatta", SH_B, 1.9), CU("shatta", SH_B, 2.3), dark=True)
FWALK = (t, t + 2.6); fx(t, "creak", 0.9)
shot("basement", t, FWALK[1], (900, 560, 1.0), (1150, 600, 1.12)); t = FWALK[1]
s = t; t = say(t, "R11") + 0.1
shot("basement", s, t, CU("shatta", SH_B, 2.2), CU("shatta", SH_B, 2.6), dark=True)
s = t; t = say(t, "R12") + 0.2
shot("basement", s, t, CU("fahmy", FA_BOX, 1.6), CU("fahmy", FA_BOX, 2.1), ease="crash")
SH_RUN = (t, t + 0.7)
s = t; R13_T = t + 0.25; t = say(R13_T, "R13")
POWER_ON = t + 0.15; fx(POWER_ON - 0.05, "switch", 1.4); shakes.append((POWER_ON, 12))
t = POWER_ON + 0.5
shot("basement", s, t, (1250, 560, 1.15), (1300, 560, 1.25))
for w_ in ("fahmy",): jump(w_, POWER_ON)
s = t; t = say(t, "R14") + 0.2
shot("basement", s, t, CU("fahmy", FA_BOX, 2.2), CU("fahmy", FA_BOX, 2.5), ease="crash")
FLEE = (t, t + 1.3); fx(t, "whoosh", 0.8)
shot("basement", t, FLEE[1], (1100, 600, 1.0)); t = FLEE[1]
# ===== 4. roof: the cable =====
cut(t, 0.5); s = t; t = say(t + 0.2, "R15") + 0.1
shot("roof", s, t, (1150, 600, 1.2), (1300, 580, 1.35), cable=True)
s = t; t = say(t, "R16") + 0.3
shot("roof", s, t, CU("zalata", ROOF["zalata"], 2.4), CU("zalata", ROOF["zalata"], 2.7), cable=True)
# ===== 5. Fahmy's apartment, live =====
cut(t, 0.6); FIN = t; fx(t, "slam", 1.0); shakes.append((t, 10))
LIVE0 = t + 0.6
s = t; t = say(t + 0.9, "R17") + 0.1
shot("fahmy", s, t, (900, 580, 1.05), (950, 560, 1.15), live=True)
s = t; t = say(t, "R18") + 0.1
shot("fahmy", s, t, CU("fahmy", FAPT["fahmy"], 1.7), CU("fahmy", FAPT["fahmy"], 2.3), live=True)
s = t; t = say(t, "R19") + 0.3
shot("fahmy", s, t, CU("tota", FAPT["tota"], 2.0), CU("tota", FAPT["tota"], 2.3), live=True)
LIVE1 = t
# ===== 6. the pulley =====
cut(t, 0.6); PUL = (t, t + 3.2)
for i in range(5): fx(t + 0.3 + i * 0.55, "creak", 0.7)
fx(t, "wind", 1.0)
shot("window", t, PUL[1], (1050, 560, 1.05), (1150, 520, 1.3), pulley=True); t = PUL[1]
s = t; t = say(t, "R20") + 0.2
shot("window", s, t, (1170, 560, 1.6), (1170, 540, 2.0), pulley=True); fx(s, "sting", 0.8)
cut(t, 0.5); s = t; t = say(t + 0.2, "R21") + 0.2
shot("apt", s, t, CU("bondo2", GRP["bondo2"], 1.9), CU("bondo2", GRP["bondo2"], 2.3))
s = t; R22_T = t; t = say(t, "R22") + 0.3
SNEAK = (R22_T, t + 0.4)
shot("apt", s, t, (900, 560, 1.1), (900, 580, 1.2))
# ===== 7. slipper climax =====
cut(t, 0.6); s = t; t = say(t + 0.1, "R23") + 0.05
THROW = t - 0.3
shot("door7", s, t, CU("nana", D7N, 1.8), CU("nana", D7N, 2.2), ease="crash")
RUN = (t, t + 2.4); HIT = t + 1.6
fx(t + 0.6, "slipper", 1.6); fx(HIT, "boom", 0.5); shakes.append((HIT, 14))
shot("stairs", t, RUN[1], (1250, 600, 1.05), (1150, 680, 1.25), escape=True); t = RUN[1]
s = t; t = say(t + 0.1, "R24") + 0.4
shot("stairs", s, t, CU("bondo2", (620, 1010, 2.3), 1.9), CU("bondo2", (620, 1010, 2.3), 2.2), escape=True)
# ===== 8. celebration =====
cut(t, 0.5); CHEER = t; fx(t, "cheer", 1.4); fx(t + 0.9, "cheer", 1.0)
for w_ in ("tota", "shatta", "zalata", "nana", "sawsan"): jump(w_, t + 0.2); jump(w_, t + 0.9)
s = t; R25_T = t + 0.8; t = say(R25_T, "R25") + 0.1
shot("lobby", s, t, (900, 600, 1.05), (920, 590, 1.12), live=True)
s = t; t = say(t, "R26") + 0.1
shot("lobby", s, t, CU("shatta", LOB["shatta"], 2.2), CU("shatta", LOB["shatta"], 2.5))
s = t; t = say(t, "R27") + 0.2
shot("lobby", s, t, CU("zalata", LOB["zalata"], 2.2), CU("zalata", LOB["zalata"], 2.4))
PUZ = t; s = t; t = say(t, "R28") + 0.7; PUZ_END = t
shot("lobby", s, t, CU("tota", LOB["tota"], 2.2), CU("tota", LOB["tota"], 2.5))
# ===== 9. next morning: the letter =====
cut(t, 0.6); shot("caption", t, t + 1.6, None); t += 1.6
s = t; t = say(t + 0.5, "R29") + 0.2
shot("morning", s, t, (800, 600, 1.05), (760, 600, 1.15))
s = t; t = say(t, "R30") + 0.15
LETTER = (s, t)
shot("letter", s, t, None)
DOOR_K = [t + 0.4 + d for d in (0, 0.45, 0.9)]
for k_ in DOOR_K: fx(k_, "knock", 1.5); shakes.append((k_, 9))
for w_ in KIDS + ("nana", "bondo2"): jump(w_, DOOR_K[0] + 0.05)
shot("morning", t, DOOR_K[-1] + 0.9, (1300, 640, 1.2), (1660, 700, 2.3), doorknock=True); t = DOOR_K[-1] + 0.9
s = t; t = say(t, "R31") + 0.4
shot("morning", s, t, CU("shatta", MOR["shatta"], 1.8), CU("shatta", MOR["shatta"], 2.6), ease="crash")
fx(t, "boom", 1.0); fx(t, "sting", 1.0); shot("black", t, t + 0.5, None); t += 0.5
shot("endcard", t, t + 4.0, None); t += 4.0
TOTAL = t

STEPS = []
def contacts(t0, t1, rate, g0=0.7, g1=0.7, jingle=False):
    n = math.ceil(t0 * rate / math.pi)
    while True:
        tc = n * math.pi / rate
        if tc >= t1: break
        if tc >= t0: STEPS.append((tc, g0 + (g1 - g0) * (tc - t0) / max(1e-3, t1 - t0), jingle))
        n += 1
contacts(HOOK[0] + 0.2, HOOK[1], 7, 0.4, 0.6)
contacts(SAW_IN[0], SAW_IN[1], 8, 0.5, 0.5)
contacts(FWALK[0], FWALK[1], 7, 0.5, 0.9)
contacts(SH_RUN[0], SH_RUN[1] + 0.3, 10, 0.7, 0.7)
contacts(FLEE[0], FLEE[1], 10, 0.8, 0.4)
contacts(FIN, FIN + 0.9, 8, 0.6, 0.6)
contacts(RUN[0], HIT, 10, 0.6, 0.9)

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

def tinted(img, lvl=1.0, tint=(255, 255, 255)):
    return ImageChops.multiply(ImageEnhance.Brightness(img).enhance(lvl), Image.new("RGB", img.size, tint))
_bed = Image.open(E1 + "bg/bedroom_clean.png").convert("RGB")
SRCBG = {"bedroom": tinted(_bed, 1.05, (255, 225, 190)),
         "living": tinted(Image.open(E1 + "bg/living.png").convert("RGB"), 1.35, (255, 240, 225)),
         "roof": Image.open(ROOT + "/s1e6/bg/roof_raw.png").convert("RGB"),
         "basement": Image.open("bg/basement.png").convert("RGB"),
         "fahmy": tinted(Image.open(ROOT + "/s1e5/bg/fahmy_raw.png").convert("RGB"), 1.1, (255, 240, 225)),
         "window": Image.open(ROOT + "/s1e9/bg/window.png").convert("RGB"),
         "apt": tinted(Image.open(ROOT + "/s1e8/bg/apt7_raw.png").convert("RGB"), 1.3, (255, 235, 210)),
         "stairs": Image.open(E1 + "bg/stairs.png").convert("RGB"),
         "door7": tinted(Image.open(ROOT + "/s1e2/bg/door7.png").convert("RGB"), 1.25, (255, 235, 210)),
         "lobby": tinted(Image.open(E1 + "bg/lobby.png").convert("RGB"), 1.3, (255, 240, 220)),
         "morning": Image.open("bg/morning.png").convert("RGB")}
TINT = {"bedroom": (255, 235, 210), "living": (255, 238, 215), "roof": (165, 180, 240), "basement": (165, 180, 235),
        "fahmy": (255, 240, 220), "window": (165, 180, 240), "apt": (250, 230, 205), "stairs": (255, 235, 210),
        "door7": (250, 232, 210), "lobby": (255, 240, 220), "morning": (255, 248, 230)}
LIT = {"living", "fahmy", "lobby", "morning", "door7"}
yy, xx = np.mgrid[0:H, 0:W]
vg = 1 - 0.55 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) ** 1.2
VIG = Image.fromarray((np.clip(vg, 0.25, 1) * 255).astype(np.uint8)).convert("RGB")
vg2 = np.clip(1 - 0.9 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2), 0.12, 1)
VIG_DARK = Image.fromarray((vg2 * 255).astype(np.uint8)).convert("RGB")
GRAIN = [np.random.default_rng(i).normal(0, 4.5, (H // 2, W // 2)).astype(np.float32) for i in range(6)]

def cam_at(sh, tt):
    k = ease((tt - sh["start"]) / max(0.01, sh["end"] - sh["start"]), sh.get("ease"))
    cx, cy, z = [a + (b - a) * k for a, b in zip(sh["c0"], sh["c1"])]
    shake = 0
    for st, amp in shakes:
        if 0 <= tt - st < 0.4: shake = max(shake, amp * (1 - (tt - st) / 0.4))
    if sh.get("vent") and any(0 <= tt - k_ < 0.1 for k_ in KN): shake = max(shake, 6)
    if sh["set"] == "window": shake = max(shake, 2.0)
    cw, ch = W / z, H / z
    cx += math.sin(tt * 0.9) * 6 + math.sin(tt * 2.3) * 2.5; cy += math.sin(tt * 1.3 + 1) * 4
    x0 = min(max(cx - cw / 2, 0), W - cw); y0 = min(max(cy - ch / 2, 0), H - ch)
    if shake:
        x0 = min(max(x0 + rng.normal(0, shake / z), 0), W - cw); y0 = min(max(y0 + rng.normal(0, shake / z), 0), H - ch)
    return x0, y0, z

def A_(who, pos, **kw):
    x, y, s = pos; d = dict(who=who, x=x, y=y, s=s, look=0, expr="neutral", arms="down"); d.update(kw); return d

def actors(set_, tt, sh):
    A = []
    if sh.get("insert"): return A
    if set_ == "bedroom":
        for who, p_ in BED.items():
            a = A_(who, p_, look={"shatta": 1, "zalata": 0, "tota": -1}[who])
            if who == "zalata": a["held"] = "nbpen"; a["arms"] = "hold"
            if who == "shatta" and sh.get("torchface"): a["held"] = "torch"; a["arms"] = "hold"
            if who == "shatta" and R04_T <= tt < R06_T: a["expr"] = "scared"
            if who == "tota" and R05_T <= tt: a["expr"] = "smug"
            A.append(a)
    elif set_ == "living":
        for who, p_ in LIV.items():
            a = A_(who, p_, look=1 if p_[0] < 1000 else -1, expr="happy" if who in KIDS else "neutral")
            if who == "sawsan":
                k = kk(tt, SAW_IN[0], SAW_IN[1]); a["x"] = lerp(2150, p_[0], ease(k)); a["walk"] = tt * 8 if k < 1 else None
                a["held"] = "phone"; a["arms"] = "hold"; a["look"] = -1; a["expr"] = "happy"
            if who == "nana":
                a["look"] = 0; a["expr"] = "sad" if tt < SLIPPER_UP else "angry"
                if tt >= SLIPPER_UP: a["held"] = "slipper"; a["arms"] = "up"
            A.append(a)
    elif set_ == "roof":
        for who, p_ in ROOF.items():
            a = A_(who, p_, look=1 if who == "tota" else -1, expr="scared")
            if sh.get("cable"): a["expr"] = "happy" if who == "tota" else "flat"; a["look"] = 1
            if sh.get("vent"): a["expr"] = "shock"; a["arms"] = "scared"
            A.append(a)
    elif set_ == "basement":
        a = A_("shatta", SH_B, expr="scared", look=1, held="torch", arms="hold")
        if tt < TORCH_ON: a["held"] = None
        if tt >= SH_RUN[0]:
            k = kk(tt, SH_RUN[0], SH_RUN[1]); a["x"] = lerp(SH_B[0], 1330, ease(k)); a["walk"] = tt * 10 if k < 1 else None
            a["expr"] = "angry"; a["arms"] = "up"; a["held"] = None
        if tt >= POWER_ON + 0.3: a["expr"] = "happy"; a["arms"] = "hips"
        A.append(a)
        if tt >= FWALK[0]:
            k = kk(tt, FWALK[0], FWALK[1])
            f = A_("fahmy", FA_BOX, x=lerp(260, FA_BOX[0], ease(k)), y=lerp(780, FA_BOX[1], ease(k)), s=lerp(1.4, FA_BOX[2], ease(k)),
                   look=1, held="torch", arms="hold", expr="smug", walk=tt * 7 if k < 1 else None)
            if k >= 1: f["arms"] = "up"; f["held"] = None
            if tt >= POWER_ON: f["expr"] = "shock"; f["arms"] = "scared"; f["look"] = -1
            if tt >= FLEE[0]:
                k2 = kk(tt, FLEE[0], FLEE[1]); f["x"] = lerp(FA_BOX[0], -300, ease(k2)); f["walk"] = tt * 11; f["look"] = -1
            A.append(f)
    elif set_ == "fahmy":
        for who, p_ in FAPT.items():
            a = A_(who, p_, look=-1 if who == "fahmy" else 1, expr="smug" if who in KIDS else "happy")
            if who == "fahmy":
                a["expr"] = "shock" if tt < LIVE0 + 1.5 else "scared"; a["arms"] = "scared" if tt < LIVE0 + 2 else "down"
            if who == "sawsan":
                k = kk(tt, FIN, FIN + 0.9); a["x"] = lerp(-200, p_[0], ease(k)); a["walk"] = tt * 8 if k < 1 else None
                a["held"] = "phone"; a["arms"] = "hold"
            if who in KIDS:
                k = kk(tt, FIN + 0.5, FIN + 1.6); a["x"] = lerp(-260, p_[0], ease(k)); a["walk"] = tt * 8 if k < 1 else None
            A.append(a)
    elif set_ == "window":
        A.append(A_("tota", (905, 1180, 3.0), arms="up", look=1, expr="happy" if tt > PUL[0] + 2.0 else "neutral",
                    lean=math.sin(tt * 5) * 0.3))
    elif set_ == "apt":
        for who, p_ in GRP.items():
            a = A_(who, p_, look=-1 if p_[0] > 700 else 1, expr="happy")
            if who == "bondo2": a["held"] = "paper"; a["arms"] = "hold"; a["expr"] = "sad"; a["look"] = 1
            if who == "nana": a["expr"] = "sad"; a["look"] = -1
            if who == "sawsan": a["held"] = "phone"; a["arms"] = "hold"
            A.append(a)
        if SNEAK[0] <= tt < SNEAK[1]:
            k = kk(tt, SNEAK[0], SNEAK[1])
            A.append(A_("fahmy", (lerp(200, -150, k), 1000, 1.9), look=-1, expr="scared", walk=tt * 5, arms="scared"))
    elif set_ == "door7":
        a = A_("nana", D7N, look=-1, expr="angry", arms="up", held="slipper")
        if tt >= THROW: a["arms"] = "point"; a["held"] = None
        A.append(a)
    elif set_ == "stairs":
        if sh.get("hookfahmy"):
            k = kk(tt, 0, 3.0)
            A.append(A_("fahmy", (lerp(1500, 1200, k), lerp(380, 900, k), lerp(1.0, 2.0, k)), look=-1, expr="smug", held="phone",
                        arms="shush", walk=tt * 7, sil=True))
        if sh.get("escape"):
            k = kk(tt, RUN[0], HIT)
            if tt < HIT:
                f = A_("fahmy", (lerp(1500, 1200, ease(k)), lerp(340, 990, ease(k)), lerp(1.0, 2.2, ease(k))), look=-1, expr="scared",
                       arms="scared", walk=tt * 12)
            else:
                kf = kk(tt, HIT, HIT + 0.35)
                f = A_("fahmy", (1200 - 40 * kf, 990, 2.2), look=0, expr="shock", arms="up", lean=-1.6 * kf)
            A.append(f)
            A.append(A_("bondo2", (620, 1010, 2.3), look=1, expr="sleepy" if tt < HIT + 0.6 else "flat", arms="hips"))
    elif set_ == "lobby":
        for who, p_ in LOB.items():
            a = A_(who, p_, look=0, expr="happy", arms="up" if tt < CHEER + 1.6 and who not in ("fahmy", "bondo2") else "down")
            if who == "fahmy": a["expr"] = "sad"; a["look"] = 1
            if who == "bondo2": a["arms"] = "hips"; a["expr"] = "smug"; a["look"] = -1
            if who == "sawsan": a["held"] = "phone"; a["arms"] = "hold" if tt >= CHEER + 1.6 else "up"
            A.append(a)
    elif set_ == "morning":
        for who, p_ in MOR.items():
            a = A_(who, p_, look=1, expr="neutral")
            if who == "bondo2": a["held"] = "paper"; a["arms"] = "hold"
            if tt >= DOOR_K[0]: a["expr"] = "shock"; a["look"] = 1; a["arms"] = "scared" if who in KIDS else a["arms"]
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

HANDS = {"hold": (46, 104), "up": (72, 186), "point": (84, 140), "shush": (4, 164), "talk": (60, 126), "hips": (48, 94), "down": (34, 62)}
def draw_scene_chars(set_, tt, cam, sh):
    x0, y0, z = cam
    layer = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(layer)
    k, lt = line_at(tt); lights = []
    for a in sorted(actors(set_, tt, sh), key=lambda a: a["s"]):
        who = a["who"]; talking = k is not None and WHO[k] == who
        expr = a.get("expr", "neutral")
        if talking: expr = expr_of(k, lt)
        mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
        arms = a.get("arms", "down")
        if talking and not a.get("held") and set_ not in ("window",): arms = ARMS.get(k, arms)
        if talking and who == "nana" and set_ == "living": arms = a["arms"]
        bob = abs(math.sin(a["walk"])) * 5 * a["s"] if a.get("walk") is not None else 0
        wy = a["y"] - jump_off(who, tt) - bob
        shiver = math.sin(tt * 60) * 2.5 if expr in ("scared", "shock") and who in KIDS else 0
        blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11 and expr != "sleepy"
        X = (a["x"] + shiver - x0) * z; Y = (wy - y0) * z; s = a["s"] * z
        target = p; L = None
        if a.get("sil"): L = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); target = P(L)
        target.ell(X, (a["y"] - y0) * z + 4 * s, 46 * s, 9 * s, (0, 0, 0, 110), None)
        draw_char(target, who, X, Y, s, expr, mouth, a.get("look", 0), blink, arms, tt, a.get("held"), a.get("lean", 0), a.get("walk"))
        S = s * CH[who]["scale"]; hx_, hy_ = HANDS.get(arms, (46, 104)); hand = (X + hx_ * S, Y - hy_ * S)
        if L is not None:
            rgb = Image.new("RGB", L.size, (10, 9, 12)); al = L.getchannel("A"); L = rgb.convert("RGBA"); L.putalpha(al)
            layer = Image.alpha_composite(layer, L); p = P(layer)
        h = a.get("held")
        if h == "torch": lights.append((hand[0], hand[1], 300 * z, 1.1, (1.0, 0.96, 0.85)))
        if h == "lantern": lights.append((hand[0], hand[1] + 30 * S, 380 * z, 1.0, (1.0, 0.75, 0.45)))
        if h == "phone": lights.append((hand[0], hand[1] - 10 * S, 230 * max(0.5, s / 2.2), 0.9, (0.6, 0.8, 1.1)))
        if sh.get("torchface") and who == "shatta":
            lights.append((X, Y - 150 * S, 420 * z, 1.4, (1.0, 0.9, 0.7)))
    return layer, lights

def tint_layer(layer, tint, lvl):
    rgb = layer.convert("RGB"); al = layer.getchannel("A")
    c = tuple(int((v * 0.55 + 255 * 0.45) * min(1.0, lvl)) for v in tint)
    rgb = ImageChops.multiply(rgb, Image.new("RGB", rgb.size, c))
    out = rgb.convert("RGBA"); out.putalpha(al); return out

LW, LH = W // 8, H // 8
gy, gx = np.mgrid[0:LH, 0:LW] * 8.0
def glow(X, Y, R): return np.exp(-((gx - X) ** 2 + (gy - Y) ** 2) / (R * R))

def light_map(set_, sh, tt, cam, lights):
    x0, y0, z = cam; W3 = lambda px, py: ((px - x0) * z, (py - y0) * z)
    cool = np.array([0.75, 0.85, 1.1], np.float32); warm = np.array([1.0, 0.8, 0.55], np.float32)
    if set_ == "bedroom":
        m = np.full((LH, LW, 3), 0.75 if not sh.get("dark") else 0.3, np.float32) * warm
    elif set_ == "roof":
        m = np.full((LH, LW, 3), 0.55, np.float32) * cool
        X, Y = W3(1650, 80); m += 0.5 * glow(X, Y, 600 * z)[..., None] * cool
    elif set_ == "basement":
        if sh.get("insert"): base = 0.75
        elif tt >= POWER_ON: base = 0.95 * (0.85 + 0.15 * (int(tt * 20) % 2 if tt < POWER_ON + 0.5 else 1))
        else: base = 0.22
        m = np.full((LH, LW, 3), base, np.float32) * (warm if tt >= POWER_ON else cool)
        X, Y = W3(160, 200); m += 0.35 * glow(X, Y, 300 * z)[..., None] * cool
        if FWALK[1] <= tt < POWER_ON and not sh.get("insert"):
            X, Y = W3(1640, 560); m += 1.3 * glow(X, Y, 420 * z)[..., None] * np.array([1.0, 0.96, 0.85], np.float32)
    elif set_ == "window":
        m = np.full((LH, LW, 3), 0.62, np.float32) * cool
        X, Y = W3(750, 585); m += 0.6 * glow(X, Y, 160 * z)[..., None] * np.array([1.0, 0.7, 0.4], np.float32)
        X, Y = W3(280, 60); m += 0.5 * glow(X, Y, 500 * z)[..., None] * cool
    elif set_ == "apt":
        m = np.full((LH, LW, 3), 0.7, np.float32) * warm
    elif set_ == "stairs":
        m = np.full((LH, LW, 3), 0.42 if sh.get("dark") else 0.85, np.float32) * (cool if sh.get("dark") else warm)
        if sh.get("hookfahmy"): X, Y = W3(1330, 170); m += 0.9 * glow(X, Y, 420 * z)[..., None] * warm
        if sh.get("escape"): m = np.full((LH, LW, 3), 0.85, np.float32) * warm
    else:
        m = np.full((LH, LW, 3), 1.0, np.float32)
    for X, Y, R, inten, col in lights:
        m += inten * glow(X, Y, R)[..., None] * np.array(col, np.float32)
    return Image.fromarray((np.clip(m / 1.4, 0, 1) * 255).astype(np.uint8), "RGB").resize((W, H), Image.BILINEAR)

def star(d, cx, cy, r, col):
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5; rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + math.cos(ang) * rr, cy + math.sin(ang) * rr))
    d.polygon(pts, fill=col, outline=(80, 60, 0, 255))

def slipper_img(d, X, Y, S, ang):
    pts = []
    for i in range(16):
        a = i / 16 * 2 * math.pi; rx, ry = 12 * S, 26 * S
        px, py = math.cos(a) * rx, math.sin(a) * ry
        pts.append((X + px * math.cos(ang) - py * math.sin(ang), Y + px * math.sin(ang) + py * math.cos(ang)))
    d.polygon(pts, fill=(60, 140, 200, 255), outline=(20, 20, 20, 255))
    sx, sy = 10 * S * math.cos(ang), 10 * S * math.sin(ang)
    d.line([(X - sx + 6 * S * math.sin(ang), Y - sy - 6 * S * math.cos(ang)), (X + sx + 6 * S * math.sin(ang), Y + sy - 6 * S * math.cos(ang))],
           fill=(240, 240, 240, 255), width=max(2, int(4 * S)))

def props(img, set_, tt, cam, sh):
    x0, y0, z = cam; S = SS * z; d = ImageDraw.Draw(img, "RGBA")
    W2 = lambda wx, wy: ((wx - x0) * S, (wy - y0) * S)
    if set_ == "basement":   # main lever on the fuse box
        X, Y = W2(1700, 400); up = tt >= POWER_ON or tt < POWER_OFF
        ang = -0.9 if up else 0.9
        d.rectangle([X - 18 * S, Y - 8 * S, X + 18 * S, Y + 8 * S], fill=(60, 60, 60, 255), outline=(20, 20, 20, 255))
        ex, ey = X + math.sin(ang) * 0 , Y + (-1 if up else 1) * 70 * S
        d.line([(X, Y), (X + 10 * S, ey)], fill=(170, 30, 30, 255), width=max(3, int(10 * S)))
        d.ellipse([X + 10 * S - 12 * S, ey - 12 * S, X + 10 * S + 12 * S, ey + 12 * S], fill=(30, 30, 30, 255))
        if POWER_ON <= tt < POWER_ON + 0.4:
            for i in range(8):
                a = rng.uniform(0, 6.28); r_ = rng.uniform(20, 90) * S
                d.line([(X, Y), (X + math.cos(a) * r_, Y + math.sin(a) * r_)], fill=(255, 240, 150, 230), width=max(1, int(3 * S)))
    if set_ == "roof" and (sh.get("cable") or sh.get("insert")):
        pts = [W2(1000, 600), W2(1200, 560), W2(1450, 545), W2(1700, 560), W2(1760, 600), W2(1770, 1100)]
        d.line(pts, fill=(15, 15, 18, 255), width=max(2, int(5 * S)), joint="curve")
        if sh.get("cable") and int(tt * 3) % 2:
            for px, py in pts[1:4]:
                d.ellipse([px - 14 * S, py - 14 * S, px + 14 * S, py + 14 * S], outline=(255, 214, 90, 220), width=max(2, int(3 * S)))
    if set_ == "roof" and sh.get("vent") and int(tt * 6) % 2 == 0:
        X, Y = W2(1040, 600)
        d.ellipse([X - 10 * S, Y - 10 * S, X + 10 * S, Y + 10 * S], fill=(255, 50, 40, 255))
    if set_ == "fahmy":   # blinking speaker LEDs
        for i, (lx, ly) in enumerate(((1060, 300), (1060, 520), (1440, 330), (1500, 520), (760, 560), (1120, 600))):
            if (int(tt * 4) + i) % 3:
                X, Y = W2(lx, ly); d.ellipse([X - 6 * S, Y - 6 * S, X + 6 * S, Y + 6 * S], fill=(255, 40, 30, 255))
    if set_ == "window" and sh.get("pulley"):
        k = kk(tt, PUL[0] + 0.3, PUL[1] - 0.4)
        bx = 1170 + math.sin(tt * 2.1) * 12; by = lerp(1250, 640, ease(k))
        X, Y = W2(bx, by)
        d.line([W2(1320, 195), (X, Y - 40 * S)], fill=(200, 185, 150, 255), width=max(2, int(5 * S)))
        d.arc([X - 34 * S, Y - 70 * S, X + 34 * S, Y + 0], 180, 360, fill=(80, 55, 25, 255), width=max(2, int(5 * S)))
        d.polygon([(X - 48 * S, Y - 30 * S), (X + 48 * S, Y - 30 * S), (X + 38 * S, Y + 40 * S), (X - 38 * S, Y + 40 * S)],
                  fill=(176, 130, 70, 255), outline=(60, 40, 15, 255))
        for i in range(3):
            d.line([(X - 44 * S, Y - 14 * S + i * 18 * S), (X + 44 * S, Y - 14 * S + i * 18 * S)], fill=(130, 90, 45, 255), width=max(1, int(3 * S)))
        d.rounded_rectangle([X - 10 * S, Y - 64 * S, X + 10 * S, Y - 22 * S], int(8 * S), fill=(236, 226, 196, 255), outline=(60, 50, 30, 255),
                            width=max(1, int(2 * S)))
        d.line([(X - 10 * S, Y - 44 * S), (X + 10 * S, Y - 44 * S)], fill=(180, 30, 30, 255), width=max(2, int(4 * S)))
        if tt > PUL[1] - 0.6:
            g = int(160 + 90 * math.sin(tt * 10))
            for r_ in (40, 60):
                d.ellipse([X - r_ * S, Y - 43 * S - r_ * S, X + r_ * S, Y - 43 * S + r_ * S], outline=(255, 230, 120, g // (r_ // 20)), width=max(2, int(3 * S)))
    if set_ == "stairs" and sh.get("escape"):
        if tt < HIT:
            k = kk(tt, RUN[0] + 0.5, HIT)
            sx = lerp(1950, 1200 - 20, k); sy = lerp(120, 990 - 2.2 * 0.82 * 190 - 20, k) - math.sin(k * math.pi) * 120
            if k > 0:
                X, Y = W2(sx, sy); slipper_img(d, X, Y, S * 1.6, tt * 14)
                for j in range(1, 5):
                    kj = max(0, k - j * 0.04); px_ = lerp(1950, 1180, kj); py_ = lerp(120, 990 - 2.2 * 0.82 * 190 - 20, kj) - math.sin(kj * math.pi) * 120
                    Xj, Yj = W2(px_, py_); d.ellipse([Xj - 6 * S, Yj - 6 * S, Xj + 6 * S, Yj + 6 * S], fill=(255, 255, 255, 120 - j * 25))
        else:
            hx_, hy_ = W2(1160, 990 - 2.2 * 0.82 * 200)
            for i in range(4):
                a = tt * 5 + i * math.pi / 2
                star(d, hx_ + math.cos(a) * 70 * S, hy_ - 60 * S + math.sin(a) * 22 * S, 14 * S, (255, 220, 60, 255))
            X, Y = W2(1290, 1000); slipper_img(d, X, Y, S * 1.6, 1.4)
    if set_ == "morning" and sh.get("doorknock"):
        for k_ in DOOR_K:
            u = tt - k_
            if 0 <= u < 0.8:
                for i in range(14):
                    px = 1600 + (i * 37) % 170; py = 560 + u * 380 + (i % 4) * 20
                    X, Y = W2(px, py); d.ellipse([X - 3 * S, Y - 3 * S, X + 3 * S, Y + 3 * S], fill=(230, 210, 170, int(230 * (1 - u / 0.8))))

def bg_frame(set_, cam):
    x0, y0, z = cam; src = SRCBG[set_]; sw, sh = src.size; f = sw / W
    box = (x0 * f, y0 * f, (x0 + W / z) * f, (y0 + H / z) * f)
    if z > 1.6:
        b = tuple(int(v) for v in box); b = (max(0, b[0] - 20), max(0, b[1] - 20), min(sw, b[2] + 20), min(sh, b[3] + 20))
        part = src.crop(b).filter(ImageFilter.GaussianBlur(min(3, (z - 1.5) * 1.3)))
        box = (box[0] - b[0], box[1] - b[1], box[2] - b[0], box[3] - b[1]); src = part
    return src.resize((SSW, SSH), Image.BICUBIC, box=box)

def ltr(img, x, y, s, size, fill, stroke=(10, 10, 10), sw=3):
    ImageDraw.Draw(img).text((x, y), s, font=ImageFont.truetype(FONT, size), fill=fill, anchor="mm", direction="ltr", stroke_width=sw, stroke_fill=stroke)

def clock_card(tt, sh):
    fr = Image.new("RGB", (W, H), (10, 10, 16)); d = ImageDraw.Draw(fr)
    cx, cy, R = W / 2, H / 2, 330
    z_ = 1 + 0.08 * kk(tt, sh["start"], sh["end"])
    R *= z_
    g = Image.new("L", (W, H), 0); ImageDraw.Draw(g).ellipse([cx - R - 60, cy - R - 60, cx + R + 60, cy + R + 60], fill=90)
    fr.paste(Image.new("RGB", (W, H), (255, 214, 120) if tt >= TICK12 else (120, 140, 200)), (0, 0), g.filter(ImageFilter.GaussianBlur(40)))
    d.ellipse([cx - R, cy - R, cx + R, cy + R], fill=(235, 228, 205), outline=(60, 45, 25), width=14)
    for i in range(12):
        a = i * math.pi / 6; d.line([(cx + math.sin(a) * R * 0.82, cy - math.cos(a) * R * 0.82), (cx + math.sin(a) * R * 0.93, cy - math.cos(a) * R * 0.93)], fill=(40, 30, 20), width=10)
    mins = 59 if tt < TICK12 else 60
    am = mins / 60 * 2 * math.pi; ah = (11 + mins / 60) / 12 * 2 * math.pi
    if tt < TICK12: am += 0.02 * math.sin(tt * 30)
    d.line([(cx, cy), (cx + math.sin(ah) * R * 0.5, cy - math.cos(ah) * R * 0.5)], fill=(20, 20, 20), width=22)
    d.line([(cx, cy), (cx + math.sin(am) * R * 0.78, cy - math.cos(am) * R * 0.78)], fill=(20, 20, 20), width=12)
    d.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=(150, 30, 30))
    ltr(fr, cx, cy + R + 70, "12:00" if tt >= TICK12 else "11:59", 80, (255, 214, 90) if tt >= TICK12 else (220, 220, 230), sw=5)
    if TICK12 <= tt < TICK12 + 0.15: fr = ImageEnhance.Brightness(fr).enhance(1.8)
    return fr

def letter_card(tt, sh):
    k = kk(tt, sh["start"], sh["end"])
    fr = Image.new("RGB", (W, H), (70, 45, 25)); d = ImageDraw.Draw(fr)
    for i in range(0, W, 9): d.line([(i, 0), (i + math.sin(i * 0.03) * 25, H)], fill=(78 + (i * 7) % 12, 50, 28), width=4)
    z_ = 1 + 0.12 * k; cx, cy = W / 2, H / 2 + 10
    pw, ph = 620 * z_, 420 * z_
    d.polygon([(cx - pw, cy - ph), (cx + pw, cy - ph + 14), (cx + pw - 10, cy + ph), (cx - pw + 8, cy + ph - 12)], fill=(240, 228, 196), outline=(120, 95, 60))
    d.rectangle([cx + pw - 190 * z_, cy - ph + 40 * z_, cx + pw - 50 * z_, cy - ph + 200 * z_], fill=(190, 60, 50), outline=(120, 30, 20), width=4)
    d.ellipse([cx + pw - 260 * z_, cy - ph + 60 * z_, cx + pw - 110 * z_, cy - ph + 210 * z_], outline=(60, 60, 120), width=5)
    text(fr, cx - 40 * z_, cy - 180 * z_, "يا نعناعة يا أختي...", int(54 * z_), (40, 40, 90), (240, 228, 196), 0)
    a_ = int(255 * kk(tt, sh["start"] + 0.8, sh["start"] + 1.6))
    if a_ > 0:
        tl = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        text(tl, cx, cy + 10 * z_, "افتحوا البدروم", int(110 * z_), (150, 20, 20), (240, 228, 196), 0)
        tl.putalpha(tl.getchannel("A").point(lambda v: min(v, a_))); fr.paste(tl, (0, 0), tl)
    text(fr, cx + 260 * z_, cy + 260 * z_, "رشدي", int(58 * z_), (40, 40, 90), (240, 228, 196), 0)
    return fr

def card(name, tt, sh):
    k = (tt - sh["start"]) / (sh["end"] - sh["start"])
    fr = Image.new("RGB", (W, H), (8, 8, 12))
    g = lambda c: tuple(int(v * min(1, k * 4)) for v in c)
    if name == "title":
        text(fr, W / 2, H / 2 - 80, "عمارة نعناعة", 110, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 + 50, "سر الدور السابع", 64, g((230, 230, 230)))
        text(fr, W / 2, H / 2 + 145, EPT + " (الحلقة الأخيرة)", 48, g((210, 210, 210)))
    elif name == "caption":
        fr = Image.new("RGB", (W, H), (30, 22, 10))
        text(fr, W / 2, H / 2, "تاني يوم الصبح...", 90, g((255, 225, 150)), (40, 20, 5), 5)
    elif name == "endcard":
        text(fr, W / 2, H / 2 - 120, "نهاية الموسم الأول", 104, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 + 20, "الموسم التاني قريب... إيه اللي في البدروم؟", 56, g((235, 235, 235)))
        text(fr, W / 2, H / 2 + 120, "اعمل اشتراك عشان ما يفوتكش", 46, g((200, 200, 200)))
    elif name == "clock": return clock_card(tt, sh)
    elif name == "letter": return letter_card(tt, sh)
    return fr

HEARTS = rng.uniform(0, 1, (18, 3))
def live_overlay(fr, tt, v=False):
    d = ImageDraw.Draw(fr, "RGBA")
    if R25_T - 0.8 <= tt: views = 1000000
    else:
        k = kk(tt, LIVE0, LIVE1); views = int(1200 + (k ** 2.2) * 480000)
    d.rounded_rectangle([40, 40, 200, 100], 14, fill=(220, 30, 40, 235))
    ltr(fr, 120, 70, "● LIVE", 34, (255, 255, 255), sw=0)
    d.rounded_rectangle([215, 40, 470, 100], 14, fill=(0, 0, 0, 160))
    ltr(fr, 342, 70, f"👁 {views:,}".replace("👁 ", ""), 34, (255, 255, 255), sw=0)
    for i, (a, b, c) in enumerate(HEARTS):
        u = (tt * (0.35 + 0.3 * c) + a) % 1
        x = W - 140 + math.sin(u * 8 + i) * 40 + b * 60; y = H - 80 - u * 620
        r_ = 16 + 10 * c; al = int(255 * (1 - u))
        col = (255, 60, 90, al) if i % 3 else (255, 200, 60, al)
        d.ellipse([x - r_, y - r_, x, y], fill=col); d.ellipse([x, y - r_, x + r_, y], fill=col)
        d.polygon([(x - r_, y - r_ / 2), (x + r_, y - r_ / 2), (x, y + r_)], fill=col)
    comments = ["هههههه مسكناه!", "برافو يا ولاد", "العمارة بتاعتنا!", "طنط سوسن أسطورة", "فهمي اتقفش!"]
    n = int((tt - LIVE0) / 1.3) if tt >= LIVE0 else 0
    for j in range(min(3, n)):
        cmt = comments[(n - 1 - j) % len(comments)]; y = H - 300 - j * 70
        d.rounded_rectangle([40, y - 28, 520, y + 28], 18, fill=(0, 0, 0, 150 - j * 30))
        text(fr, 280, y, cmt, 30, (255, 255, 255), sw=0)

def hud(fr, tt, v=False):
    sc = 0.85 if v else 1.0; cx = 540 if v else W / 2
    if R02_T + 2.6 <= tt < R03_T:
        d = ImageDraw.Draw(fr, "RGBA"); y = 1700 if v else 120
        d.rounded_rectangle([cx - 420 * sc, y - 50 * sc, cx + 420 * sc, y + 50 * sc], int(22 * sc), fill=(20, 60, 30, 220), outline=(120, 230, 120, 255), width=4)
        text(fr, cx, y, "إجابة امبارح: أستاذ فهمي ✓", int(42 * sc), (200, 255, 200))

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
        text(bgv, 540, 1695, "لغز الحلقة: خمّنت من الأول؟", 50, (255, 214, 90))
        text(bgv, 540, 1758, "اكتب في الكومنتات", 42)
    return bgv

def finish(fr, tt, dark=False):
    fr = ImageChops.multiply(fr, VIG_DARK if dark else VIG)
    a = np.asarray(fr, np.float32)
    g = GRAIN[int(tt * FPS) % len(GRAIN)]
    g = np.repeat(np.repeat(g, 2, 0), 2, 1)[..., None]
    return Image.fromarray(np.clip(a + g, 0, 255).astype(np.uint8))

def frame(tt):
    sh = shot_at(tt); set_ = sh["set"]
    if set_ in ("title", "endcard", "caption", "clock", "letter"): return finish(card(set_, tt, sh), tt)
    if set_ == "black" or sh.get("blackout"):
        fr = Image.new("RGB", (W, H), (0, 0, 0))
        if sh.get("blackout") and int(tt * 12) % 3 == 0: fr = Image.new("RGB", (W, H), (14, 14, 22))
        return fr
    cam = cam_at(sh, tt)
    img = bg_frame(set_, cam)
    props(img, set_, tt, cam, sh)
    layer, lights = draw_scene_chars(set_, tt, cam, sh)
    layer = tint_layer(layer, TINT[set_], 0.97)
    img.paste(layer, (0, 0), layer)
    fr = img.resize((W, H), Image.LANCZOS)
    if set_ in LIT and not sh.get("dark"):
        if set_ == "lobby" and CHEER <= tt < CHEER + 0.15: fr = ImageEnhance.Brightness(fr).enhance(1.4)
    else:
        lm = light_map(set_, sh, tt, cam, lights)
        fr = ImageChops.multiply(fr, lm); fr = ImageEnhance.Brightness(fr).enhance(1.6)
    if set_ == "basement" and POWER_ON <= tt < POWER_ON + 0.2: fr = ImageEnhance.Brightness(fr).enhance(2.0)
    if set_ == "roof" and sh.get("vent") and any(0 <= tt - k_ < 0.12 for k_ in KN): fr = ImageEnhance.Brightness(fr).enhance(0.6)
    if sh.get("live") and tt >= LIVE0: live_overlay(fr, tt)
    return finish(fr, tt, sh.get("dark"))

def render(out_h, out_v, stills=None):
    fh = fv = None
    if not stills:
        mk = lambda w, h, o: subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}",
                                   "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "21",
                                   "-pix_fmt", "yuv420p", o], stdin=subprocess.PIPE)
        fh = mk(W, H, out_h); fv = mk(1080, 1920, out_v)
    times = stills or [i / FPS for i in range(int(TOTAL * FPS))]
    for i, tt in enumerate(times):
        base = frame(tt)
        h = base.copy(); hud(h, tt)
        if PUZ <= tt < PUZ_END:
            d = ImageDraw.Draw(h, "RGBA")
            d.rounded_rectangle([W / 2 - 600, 60, W / 2 + 600, 175], 24, fill=(20, 20, 30, 215), outline=(255, 214, 90, 255), width=4)
            text(h, W / 2, 117, "لغز الحلقة: خمّنت من الأول إن فهمي ورا الخبط؟ اكتب في الكومنتات", 34, (255, 214, 90))
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
        if s_["set"] in ("lobby", "morning", "living", "caption") or (s_["set"] == "basement" and s_["start"] >= POWER_ON - 0.01):
            env[int(s_["start"] * SR):int(s_["end"] * SR)] = 0.25
    env = np.convolve(env, np.ones(4410) / 4410, mode="same")
    mix_into(buf, dr * env, 0, 1.1)
    r = np.random.default_rng(9); ts = np.arange(int(SR * 1.6)) / SR
    tk = np.arange(int(SR * 0.15)) / SR
    S = {"boom": sfx_boom(), "tick": sfx_tick() * 3, "knock": sfx_knock() * 1.3, "powercut": sfx_powercut() * 1.5, **SFXF}
    S["tock"] = (np.sin(2 * np.pi * 900 * tk) * np.exp(-tk * 60) * 0.5 + r.normal(0, 1, len(tk)) * np.exp(-tk * 150) * 0.3)
    S["sting"] = (np.sin(2 * np.pi * (1200 + 80 * np.sin(ts * 40)) * ts) * 0.08 + np.sin(2 * np.pi * 1263 * ts) * 0.06
                  + np.sin(2 * np.pi * 55 * ts) * 0.4) * np.exp(-ts * 1.8)
    for t0, n, g in sfx:
        if n in S: mix_into(buf, S[n], t0, g)
    # happy victory jingle in the celebration
    notes = [523.25, 659.25, 783.99, 1046.5, 783.99, 1046.5]
    for i, f in enumerate(notes):
        tt_ = np.arange(int(SR * 0.6)) / SR
        mix_into(buf, (np.sin(2 * np.pi * f * tt_) + 0.4 * np.sin(4 * np.pi * f * tt_)) * np.exp(-tt_ * 4) * 0.09, CHEER + 0.1 + i * 0.16, 1.0)
    # emotional music box under the contract reveal
    mb = [659.25, 587.33, 523.25, 587.33, 659.25, 659.25, 659.25, 587.33, 587.33, 587.33, 659.25, 783.99]
    for i, f in enumerate(mb):
        tn = PUL[1] + 0.3 + i * 0.5
        tt_ = np.arange(int(SR * 1.2)) / SR
        mix_into(buf, (np.sin(2 * np.pi * f * tt_) + 0.3 * np.sin(4 * np.pi * f * tt_)) * np.exp(-tt_ * 3.5) * 0.05, tn, 1.0)
    tsx = np.arange(int(SR * 0.25)) / SR; jt = np.arange(int(SR * 0.3)) / SR
    for i, (st, g, jing) in enumerate(STEPS):
        nz = np.convolve(r.normal(0, 1, len(tsx)), np.ones(12) / 12, mode="same")
        mix_into(buf, (np.sin(2 * np.pi * 80 * tsx) * np.exp(-tsx * 30) * 0.9 + nz * np.exp(-tsx * 25) * 0.9) * 0.6, st, g)
    for st, k in lines: mix_into(buf, AUD[k], st, 1.0)
    buf = buf[:int(TOTAL * SR)]
    buf = np.clip(buf / max(1e-6, np.abs(buf).max()) * 0.95, -1, 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((buf * 32767).astype(np.int16).tobytes())

def mux(v, out):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", v, "-i", "mix.wav", "-c:v", "copy", "-af",
                    "loudnorm=I=-15:TP=-1.5", "-c:a", "aac", "-b:a", "192k", "-shortest", out], check=True)

R04_T = [st for st, k in lines if k == "R04"][0]; R05_T = [st for st, k in lines if k == "R05"][0]; R06_T = [st for st, k in lines if k == "R06"][0]

if __name__ == "__main__":
    print("TOTAL", round(TOTAL, 1))
    if sys.argv[1:2] == ["stills"]:
        render(None, None, [float(v) for v in sys.argv[2:]])
    elif sys.argv[1:2] == ["times"]:
        for s_ in shots: print(s_["set"], round(s_["start"], 2), round(s_["end"], 2), {k: v for k, v in s_.items() if v is True})
    else:
        build_audio()
        render("h.mp4", "v.mp4")
        mux("h.mp4", "sirr_eldor_elsabe3_ep10.mp4"); mux("v.mp4", "sirr_eldor_elsabe3_ep10_vertical.mp4")
        print("done")
