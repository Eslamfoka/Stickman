import sys, os, math, subprocess, wave
sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter, ImageFont
from engine import *

os.chdir(ROOT + "/s2e3")
SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(303)
SEASON = "سر البدروم"
EPT = "الحلقة 3: الباشا"

SUB = {
 "E01": "الموبايل سجل طول الليل... تعالوا اسمعوا!",
 "E02": "الساعة ستة الصبح يا توتة... حتى العفاريت نايمين!",
 "E03": "الساعة اتناشر... نفس المزيكا، ونفس الخطوات الحديد.",
 "E04": "استنوا... الساعة تلاتة... فيه عربية وقفت!",
 "E05": "(تسجيل) حاضر يا باشا... بس فين النور؟",
 "E06": "(تسجيل) بكرة الصبح... هتشوف النور.",
 "E07": "باشا؟!... باشا مين؟!",
 "E08": "الجوابات!... لغز امبارح: السبعة اللي بتستنى الجوابات... هي صندوق البوسطة رقم سبعة!",
 "E09": "شقة سبعة... دي شقة عم رشدي.",
 "E10": "ده عم رشدي وهو صغير!... وفي إيده ميكروفون؟",
 "E11": "ومكتوب ورا الصورة: 1958",
 "E12": "الصوت ده... نفس صوت العربية اللي في التسجيل!",
 "E13": "افتح إنت يا زلطة... إنت الكبير.",
 "E14": "أنا أكبر منك بيومين بس!",
 "E15": "جاي جاي!... مين بيخبط على الصبح كده؟",
 "E16": "صباح الخير... الحاجة نعناعة موجودة؟",
 "E17": "آه!... راسي يا باشا!",
 "E18": "يا حاجة نعناعة!... فيه ضيوف عايزينك!",
 "E19": "جاية أهه... خير يا أستاذ؟",
 "E20": "أنا عايز أأجر البدروم... مخزن. وهدفع اللي تطلبيه.",
 "E21": "البدروم ده مش للإيجار... ولا للبيع.",
 "E22": "كل حاجة ليها تمن يا حاجة.",
 "E23": "خد فلوسك... واتفضل.",
 "E24": "إنت... اللي كنت في الشباك امبارح.",
 "E25": "أنا؟!... لا لا، ده كان أخويا التوأم!",
 "E26": "يا باشا... السلم ضلمة أوي هنا.",
 "E27": "صورت نمرة العربية!",
 "E28": "وكلمة «أيوا يا باشا»... أنا سمعتها قبل كده.",
 "E29": "لغز النهارده: مين في الموسم الأول كان بيقول «أيوا يا باشا» في التليفون؟ اكتبوا في الكومنتات!",
 "E30": "المفتاح... ضاع... ضاع خلاص...",
 "E31": "لقيته يا باشا!... المفتاح كان في جيبه طول الوقت!",
 "E32": "يا ماما... إيه النور الأحمر ده؟!",
}
WHO = {"E01": "tota", "E02": "shatta", "E03": "zalata", "E04": "tota", "E05": "rec", "E06": "rec", "E07": "shatta", "E08": "tota",
       "E09": "zalata", "E10": "shatta", "E11": "zalata", "E12": "zalata", "E13": "shatta", "E14": "zalata", "E15": "bondo2",
       "E16": "pasha", "E17": "abdo", "E18": "bondo2", "E19": "nana", "E20": "pasha", "E21": "nana", "E22": "pasha", "E23": "nana",
       "E24": "pasha", "E25": "shatta", "E26": "abdo", "E27": "tota", "E28": "zalata", "E29": "tota", "E30": "bondo2", "E31": "abdo", "E32": "abdo"}
EXPR = {"E01": "happy", "E02": "sleepy", "E03": "flat", "E04": "shock", "E07": "scared", "E08": [(0, "shock"), (0.25, "happy")],
        "E09": "flat", "E10": "shock", "E11": "flat", "E12": "shock", "E13": "scared", "E14": "angry", "E15": [(0, "sleepy"), (0.4, "angry")],
        "E16": "smug", "E17": "shock", "E18": "shout", "E19": "flat", "E20": "smug", "E21": "angry", "E22": "smug", "E23": "angry",
        "E24": "flat", "E25": "scared", "E26": "scared", "E27": "happy", "E28": "flat", "E29": [(0, "neutral"), (0.6, "smug")],
        "E30": "sleepy", "E31": "happy", "E32": "shock"}
ARMS = {"E01": "point", "E02": "down", "E03": "hold", "E04": "point", "E07": "scared", "E08": "point", "E09": "hold", "E10": "point",
        "E11": "hold", "E12": "point", "E13": "point", "E14": "hips", "E15": "up", "E16": "down", "E17": "up", "E18": "up", "E19": "hips",
        "E20": "talk", "E21": "hips", "E23": "point", "E24": "point", "E25": "scared", "E26": "scared", "E28": "hold", "E29": "point",
        "E31": "up", "E32": "scared"}

def _aud(k):
    f = f"audio/{k}_fx.mp3"
    return load_audio(f if os.path.exists(f) else f"audio/{k}.mp3")
AUD = {k: _aud(k) for k in SUB}
ENV = {k: envelope(v) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}
SFXF = {n: load_audio(f"sfx/{n}.mp3") for n in ("whoosh", "creak", "slam", "switch", "steps_metal", "snore", "car", "clang",
                                                 "mail", "keys", "bonk", "knocks", "car_arrive", "stinger")}

lines, sfx, shots, jumps, shakes = [], [], [], {}, []
def say(t, k): lines.append((t, k)); return t + DUR[k]
def fx(t, n, g=1.0): sfx.append((t, n, g))
def jump(w, t): jumps.setdefault(w, []).append(t)
def shot(set_, s, e, c0, c1=None, **kw): shots.append(dict(set=set_, start=s, end=e, c0=c0, c1=c1 or c0, **kw))
def cut(t, g=0.4): fx(t - 0.12, "whoosh", g)
def T(k): return [st for st, kk_ in lines if kk_ == k][0]
KIDS = ("shatta", "zalata", "tota")

# ---------------- world (lobby = morning.png, 1920x1080 coords) ----------------
DOORO = (754, 180, 864, 600)      # street-door opening
ENTR = (809, 600)                 # feet in the street doorway (far)
VENT = (1402, 812, 1512, 872)
VC = ((VENT[0] + VENT[2]) / 2, (VENT[1] + VENT[3]) / 2)
MAIL7 = (205, 300)
BENCH = (170, 1000, 1.85)
STB = (1330, 905, 1.65)           # bottom of the staircase (kids / Nana come from here)
VS = {"tota": (1420, 1040, 1.95), "shatta": (1130, 1040, 1.95), "zalata": (940, 1040, 1.95)}
MB = {"zalata": (430, 1040, 1.95), "tota": (610, 1040, 1.95), "shatta": (790, 1040, 1.95)}
DR = {"zalata": (700, 860, 1.45), "shatta": (860, 860, 1.45), "tota": (1000, 860, 1.45)}     # peeking at the door
BK = {"shatta": (1400, 1040, 1.95), "zalata": (1550, 1040, 1.95), "tota": (1690, 1040, 1.95)}  # watching the visit
PASHA_P = (800, 1040, 2.05); ABDO_P = (540, 1030, 2.0); NANA_P = (1130, 1040, 1.95)
BONDO_D = (690, 640, 0.95); BONDO_C = (300, 1010, 1.85)
PASHA_TURN = (800, 820, 1.5)
TOTA_DOOR = (900, 760, 1.25)

def CU(who, pos, z=2.2, dx=0):
    x, y, s = pos; S = s * CH[who]["scale"]
    if who == "tota": z *= 1.3; dx -= 50
    hy = y - 190 * S
    return (x + dx, hy + H / (2 * z) - 1.45 * 46 * S - 25, z)

t = 0.0
# ===== 0. HOOK — dawn, the phone still recording in the grate =====
shot("lobby", 0, 1.7, (VC[0] - 8, VC[1] - 30, 3.8), (VC[0] - 8, VC[1] - 20, 4.4), tod=0.42, ventcu=True)
t = 1.7; cut(t, 0.35)
DESC = (t, t + 3.0)
shot("stairs", t, DESC[1], (1150, 560, 1.05), (1150, 620, 1.2), mood="dawn"); t = DESC[1]
KIN = (t, t + 2.6)
shot("lobby", t, KIN[1], (1150, 700, 1.25), (1250, 740, 1.5), tod=0.42); t = KIN[1]
PICK = t + 0.2
s = t; t = say(t + 0.3, "E01") + 0.1
shot("lobby", s, t, CU("tota", VS["tota"], 1.55), CU("tota", VS["tota"], 1.8), tod=0.42)
s = t; t = say(t, "E02") + 0.15
shot("lobby", s, t, CU("shatta", VS["shatta"], 1.8), CU("shatta", VS["shatta"], 2.0), tod=0.42)
PH1 = (t, t + 3.2); fx(t + 0.2, "switch", 0.6)
shot("phone", t, PH1[1], None, stamp=("12:00", "AM")); t = PH1[1]
s = t; t = say(t, "E03") + 0.1
shot("lobby", s, t, CU("zalata", VS["zalata"], 1.7), CU("zalata", VS["zalata"], 1.9), tod=0.42)
PH2 = (t, t + 2.2)
shot("phone", t, PH2[1], None, stamp=("03:12", "AM"), scrub=True); t = PH2[1]
s = t; t = say(t, "E04") + 0.1
shot("lobby", s, t, CU("tota", VS["tota"], 1.7), CU("tota", VS["tota"], 2.0), ease="crash", tod=0.42)
s = t; t = say(t + 0.2, "E05") + 0.2
shot("phone", s, t, None, stamp=("03:14", "AM"))
s = t; t = say(t + 0.1, "E06") + 0.5
shot("lobby", s, t, (1140, 650, 1.35), (1150, 660, 1.75), tod=0.42)
s = t; t = say(t, "E07") + 0.3
shot("lobby", s, t, CU("shatta", VS["shatta"], 1.8), CU("shatta", VS["shatta"], 2.6), ease="crash", tod=0.42)
fx(t - 0.3, "whoosh", 0.6); shot("title", t, t + 2.0, None); TITLE = t; t += 2.0
# ===== 1. MAIL — the sun is up; letters fall through the slot =====
SUNUP = (t, t + 2.4)
shot("lobby", t, SUNUP[1], (1000, 600, 1.1), (1000, 600, 1.15), tl=(0.42, 1, SUNUP)); t = SUNUP[1]
MAIL = t; fx(t - 0.3, "mail", 1.0)
shot("lobby", t, t + 1.5, (1150, 640, 1.3), (809, 470, 2.4), ease="crash", tod=1); t += 1.5
s = t; t = say(t + 0.05, "E08") + 0.15
shot("lobby", s, t, CU("tota", VS["tota"], 1.6), CU("tota", VS["tota"], 1.75), tod=1)
WMB = (t, t + 2.6)
shot("lobby", t, WMB[1], (1050, 650, 1.25), (600, 600, 1.3), tod=1); t = WMB[1]
BOXOPEN = t + 0.5; fx(BOXOPEN, "creak", 0.7)
shot("lobby", t, t + 1.8, (MAIL7[0] + 20, MAIL7[1] + 20, 3.4), (MAIL7[0] + 20, MAIL7[1] + 40, 3.9), tod=1, boxcu=True); t += 1.8
s = t; t = say(t, "E09") + 0.15
shot("lobby", s, t, (560, 640, 1.5), (560, 650, 1.6), tod=1)
PHOTO = (t, None)
s = t; t = say(t + 0.4, "E10") + 0.2
FLIP = t; fx(FLIP, "whoosh", 0.3)
s2 = t; t = say(t + 0.5, "E11") + 0.4
shot("photo", s, t, None); PHOTO = (s, t)
# ===== 2. THE CAR (J-cut: engine before the cut) =====
CAR1 = t - 1.0; fx(CAR1, "car_arrive", 1.0)
s = t; t = say(t + 0.3, "E12") + 0.1
shot("lobby", s, t, CU("zalata", MB["zalata"], 1.8), CU("zalata", MB["zalata"], 2.3), ease="crash", tod=1)
RUN = (t, t + 1.6)
shot("lobby", t, RUN[1], (700, 700, 1.25), (809, 560, 1.7), tod=1); t = RUN[1]
POV = (t, t + 5.2)
shot("street", t, POV[1], (960, 560, 1.12), (1050, 600, 1.3), glass=True); t = POV[1]
KNOCK = t + 0.5; fx(KNOCK, "knocks", 1.2)
BACKOFF = (t + 0.3, t + 1.6)
shot("lobby", t, t + 2.4, (809, 420, 2.4), (809, 470, 2.0), tod=1, lowdoor=True); t += 2.4
s = t; t = say(t, "E13") + 0.05
shot("lobby", s, t, (900, 700, 1.6), (900, 700, 1.7), tod=1)
s = t; t = say(t, "E14") + 0.2
shot("lobby", s, t, CU("zalata", DR["zalata"], 2.0), CU("zalata", DR["zalata"], 2.2), tod=1)
WAKE = t
s = t; t = say(t + 0.1, "E15") + 0.1
shot("lobby", s, t, CU("bondo2", BENCH, 1.7), CU("bondo2", BENCH, 1.9), tod=1)
BWALK = (t, t + 2.6); fx(t + 0.2, "slam", 0)  # placeholder
shot("lobby", t, BWALK[1], (500, 700, 1.15), (760, 560, 1.6), tod=1); t = BWALK[1]
DOOROPEN = t + 0.2; fx(DOOROPEN, "creak", 0.9)
PIN = (t + 0.8, t + 3.6); STING = t + 0.9; fx(STING, "stinger", 0.9)
shot("lobby", t, PIN[1], (809, 470, 2.4), (820, 640, 1.35), tod=1, backlit=True); t = PIN[1]
s = t; t = say(t + 0.1, "E16") + 0.1
shot("lobby", s, t, CU("pasha", PASHA_P, 1.6), CU("pasha", PASHA_P, 1.8), tod=1, low=True)
BUMP = t + 0.6; fx(BUMP, "bonk", 1.0); shakes.append((BUMP, 10)); jump("abdo", BUMP)
AIN = (t - 0.2, t + 1.8)
s = t; t = say(t + 0.75, "E17") + 0.15
shot("lobby", s, t, (700, 640, 1.6), (680, 680, 1.4), tod=1)
s = t; t = say(t + 0.1, "E18") + 0.15
shot("lobby", s, t, CU("bondo2", BONDO_C, 1.7), CU("bondo2", BONDO_C, 1.9), tod=1)
cut(t, 0.3); NDESC = (t, t + 3.2)
s = t; say(t + 1.6, "E19"); t = NDESC[1]
shot("stairs", s, t, (1150, 560, 1.05), (1150, 640, 1.25), mood="day")
NIN = (t, t + 1.6)
shot("lobby", t, NIN[1], (1100, 640, 1.2), (1050, 640, 1.25), tod=1); t = NIN[1]
s = t; t = say(t + 0.1, "E20") + 0.1
shot("lobby", s, t, (960, 600, 1.55), (940, 600, 1.7), tod=1)
s = t; t = say(t, "E21") + 0.15
shot("lobby", s, t, CU("nana", NANA_P, 1.8), CU("nana", NANA_P, 2.0), tod=1)
ENV0 = t + 0.2; fx(t + 0.3, "stinger", 0.6)
s = t; t = say(t + 0.2, "E22") + 0.2
shot("lobby", s, t, CU("pasha", PASHA_P, 1.7), CU("pasha", PASHA_P, 2.1), tod=1, low=True)
s = t; t = say(t, "E23") + 0.2; PUSHBACK = s + 0.6
shot("lobby", s, t, (1010, 640, 1.5), (1010, 640, 1.55), tod=1)
PEXIT = (t, t + 2.0)
shot("lobby", t, PEXIT[1], (900, 640, 1.2), (850, 620, 1.3), tod=1); t = PEXIT[1]
s = t; t = say(t + 0.3, "E24") + 0.3
shot("lobby", s, t, CU("pasha", PASHA_TURN, 1.3), CU("pasha", PASHA_TURN, 2.0), tod=1)
s = t; t = say(t, "E25") + 0.2
shot("lobby", s, t, CU("shatta", BK["shatta"], 1.8), CU("shatta", BK["shatta"], 2.5), ease="crash", tod=1)
POUT = (t, t + 2.4)
s = t; t = say(t + 0.6, "E26") + 0.3; t = max(t, POUT[1])
shot("lobby", s, t, (820, 600, 1.5), (809, 560, 1.8), tod=1)
TRUN = (t, t + 1.2)
shot("lobby", t, TRUN[1], (1000, 640, 1.2), (850, 560, 1.5), tod=1); t = TRUN[1]
CAR2 = t + 0.6; fx(t, "car", 0.8)
s = t; t = say(t + 0.6, "E27") + 0.6
shot("street", s, t, (1430, 600, 2.2), (1480, 610, 2.8), phonepov=True)
# ===== plant: the doorman goes back to sleep — the key in his pocket =====
BBACK = (t, t + 2.4)
shot("lobby", t, BBACK[1], (600, 700, 1.25), (400, 720, 1.35), tod=1); t = BBACK[1]
SNORE1 = t - 0.3; fx(SNORE1, "snore", 0.8)
KEYCU = (t, t + 1.8)
shot("lobby", t, KEYCU[1], (BENCH[0] + 48, 880, 3.0), (BENCH[0] + 48, 890, 3.5), tod=1); t = KEYCU[1]
# ===== 3. CLUE + PUZZLE =====
s = t; t = say(t + 0.1, "E28") + 0.2
shot("lobby", s, t, CU("zalata", BK["zalata"], 1.7), CU("zalata", BK["zalata"], 2.0), tod=1)
PUZ = t; s = t; t = say(t + 0.1, "E29") + 0.8; PUZ_END = t
shot("lobby", s, t, CU("tota", BK["tota"], 1.6), CU("tota", BK["tota"], 1.85), tod=1)
# ===== 4. NIGHT — the theft =====
cut(t, 0.4); TL = (t, t + 3.6)
shot("lobby", t, TL[1], (700, 620, 1.12), (600, 640, 1.2), tl=(1, 0, TL)); t = TL[1]
SNORE2 = TL[0] + 1.2; fx(SNORE2, "snore", 0.9)
CAR3 = t; fx(CAR3, "car", 0.7)
SWEEP = (t + 0.8, t + 3.0)
shot("lobby", t, SWEEP[1] + 0.2, (809, 520, 1.6), (809, 520, 1.75), tod=0); t = SWEEP[1] + 0.2
NDOOR = t + 0.1; fx(NDOOR, "creak", 1.0)
AIN2 = (t + 0.9, t + 5.2)
shot("lobby", t, AIN2[1], (809, 520, 2.0), (420, 720, 1.3), tod=0); t = AIN2[1]
HAND = (t, t + 2.2); fx(t + 0.8, "keys", 1.2)
shot("lobby", t, HAND[1], (BENCH[0] + 120, 870, 2.6), (BENCH[0] + 110, 880, 2.9), tod=0); t = HAND[1]
s = t; t = say(t + 0.2, "E30") + 0.3; FREEZE = s + 0.2
shot("lobby", s, t, (300, 700, 1.7), (300, 700, 1.9), tod=0)
SNORE3 = t - 0.1; fx(SNORE3, "snore", 0.7)
s = t; t = say(t + 0.4, "E31") + 0.3
shot("lobby", s, t, CU("abdo", (420, 1010, 1.9), 1.7), CU("abdo", (420, 1010, 1.9), 1.9), tod=0)
RED_ON = t + 0.3; fx(RED_ON, "steps_metal", 0.9); fx(RED_ON + 0.05, "switch", 0.6)
shot("lobby", t, t + 2.2, (1690, 900, 2.6), (1690, 930, 3.0), tod=0, dutch=True); t += 2.2
s = t; t = say(t + 0.1, "E32") + 0.4
shot("lobby", s, t, CU("abdo", (420, 1010, 1.9), 1.5), CU("abdo", (420, 1010, 1.9), 2.8), ease="crash", tod=0, dutch=True)
fx(t, "clang", 1.2); fx(t, "boom", 0.9); shakes.append((t, 14))
shot("black", t, t + 0.6, None); t += 0.6
shot("endcard", t, t + 4.0, None); t += 4.0
TOTAL = t

STEPS = []
def contacts(t0, t1, rate, g=0.5):
    n = math.ceil(t0 * rate / math.pi)
    while True:
        tc = n * math.pi / rate
        if tc >= t1: break
        if tc >= t0: STEPS.append((tc, g))
        n += 1
for a_, b_, r_, g_ in ((DESC[0], DESC[1], 8, 0.4), (KIN[0], KIN[1], 8, 0.45), (WMB[0], WMB[1], 8, 0.45), (RUN[0], RUN[1], 11, 0.5),
                       (BWALK[0], BWALK[1], 6, 0.45), (PIN[0] + 0.6, PIN[1], 6, 0.55), (NDESC[0], NDESC[1], 6, 0.45), (NIN[0], NIN[1], 6, 0.45),
                       (PEXIT[0], PEXIT[1], 6, 0.5), (POUT[0], POUT[1], 6, 0.5), (TRUN[0], TRUN[1], 11, 0.45), (BBACK[0], BBACK[1], 6, 0.4),
                       (AIN2[0], AIN2[1], 4, 0.25)):
    contacts(a_, b_, r_, g_)

# ---------------- helpers ----------------
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

def tod(sh, tt):
    if "tl" in sh:
        a, b, (t0, t1) = sh["tl"]; return lerp(a, b, ease(kk(tt, t0, t1)))
    return sh.get("tod", 1)

def tinted(img, lvl=1.0, tint=(255, 255, 255)):
    return ImageChops.multiply(ImageEnhance.Brightness(img).enhance(lvl), Image.new("RGB", img.size, tint))
_mor = Image.open(ROOT + "/s1e10/bg/morning.png").convert("RGB")
_st = Image.open(ROOT + "/s1e1/bg/stairs_1080.png").convert("RGB")
_street = Image.open("bg/street_day.png").convert("RGB")
SRC = {"lobby_day": _mor, "lobby_night": tinted(_mor, 0.9, (150, 165, 230)),
       "stairs_dawn": tinted(ImageEnhance.Brightness(_st).enhance(1.15), 1.0, (190, 200, 240)),
       "stairs_day": tinted(ImageEnhance.Brightness(_st).enhance(1.55), 1.0, (255, 225, 175)),
       "street": _street}
yy, xx = np.mgrid[0:H, 0:W]
vg = 1 - 0.55 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) ** 1.2
VIG = Image.fromarray((np.clip(vg, 0.25, 1) * 255).astype(np.uint8)).convert("RGB")
vg2 = np.clip(1 - 0.85 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2), 0.15, 1)
VIG_DARK = Image.fromarray((vg2 * 255).astype(np.uint8)).convert("RGB")
GRAIN = [np.random.default_rng(i).normal(0, 4.5, (H // 2, W // 2)).astype(np.float32) for i in range(6)]

def cam_at(sh, tt):
    k = ease((tt - sh["start"]) / max(0.01, sh["end"] - sh["start"]), sh.get("ease"))
    cx, cy, z = [a + (b - a) * k for a, b in zip(sh["c0"], sh["c1"])]
    shake = 0
    for st, amp in shakes:
        if 0 <= tt - st < 0.45: shake = max(shake, amp * (1 - (tt - st) / 0.45))
    cw, ch = W / z, H / z
    hand = 2.0 if sh.get("phonepov") else 1.0
    cx += (math.sin(tt * 0.9) * 5 + math.sin(tt * 2.3) * 2) * hand; cy += math.sin(tt * 1.3 + 1) * 3.5 * hand
    x0 = min(max(cx - cw / 2, 0), W - cw); y0 = min(max(cy - ch / 2, 0), H - ch)
    if shake:
        x0 = min(max(x0 + rng.normal(0, shake / z), 0), W - cw); y0 = min(max(y0 + rng.normal(0, shake / z), 0), H - ch)
    return x0, y0, z

def bg_crop(src, cam, blur_on=True):
    x0, y0, z = cam; sw, sh = src.size; f = sw / W
    box = (x0 * f, y0 * f, (x0 + W / z) * f, (y0 + H / z) * f)
    if z > 1.6 and blur_on:
        b = tuple(int(v) for v in box); b = (max(0, b[0] - 20), max(0, b[1] - 20), min(sw, b[2] + 20), min(sh, b[3] + 20))
        part = src.crop(b).filter(ImageFilter.GaussianBlur(min(3, (z - 1.5) * 1.3)))
        box = (box[0] - b[0], box[1] - b[1], box[2] - b[0], box[3] - b[1]); src = part
    return src.resize((SSW, SSH), Image.BICUBIC, box=box)

def bg_frame(set_, cam, d, sh):
    if set_ == "lobby":
        bl = not (sh.get("boxcu") or sh.get("dutch"))
        if d >= 0.999: return bg_crop(SRC["lobby_day"], cam, bl)
        if d <= 0.001: return bg_crop(SRC["lobby_night"], cam, bl)
        return Image.blend(bg_crop(SRC["lobby_night"], cam, bl), bg_crop(SRC["lobby_day"], cam, bl), d)
    if set_ == "stairs": return bg_crop(SRC["stairs_" + sh.get("mood", "day")], cam, False)
    return bg_crop(SRC[set_], cam, not sh.get("phonepov"))

def A_(who, pos, **kw):
    x, y, s = pos; d = dict(who=who, x=x, y=y, s=s, look=0, expr="neutral", arms="down"); d.update(kw); return d
def walk_to(a, p0, p1, win, tt, rate=8):
    k = kk(tt, *win); e = ease(k)
    a["x"], a["y"], a["s"] = lerp(p0[0], p1[0], e), lerp(p0[1], p1[1], e), lerp(p0[2], p1[2], e)
    if 0 < k < 1: a["walk"] = tt * rate
    return k

def kid_pos(who, tt):
    """Where each kid is (lobby) and how they behave."""
    a = A_(who, VS[who], look=1, expr="neutral")
    if who == "zalata": a["held"] = "nbpen"; a["arms"] = "hold"; a["expr"] = "flat"
    off = {"tota": 0.0, "shatta": 0.35, "zalata": 0.7}[who]
    if tt < KIN[1] + 0.1:
        st0 = KIN[0] + off * 0.9
        if tt < st0: a["hide"] = True
        k = walk_to(a, (STB[0] + 40, STB[1], STB[2]), VS[who], (st0, KIN[1] - 0.2 + off * 0.2), tt, 8)
        a["look"] = -1
        if who == "shatta": a["expr"] = "sleepy"
    if who == "tota" and tt >= KIN[1] - 0.3 and tt < TITLE:
        a["lean"] = 0.9 * ease(kk(tt, KIN[1] - 0.3, PICK)) if tt < PICK + 0.3 else 0.9 * (1 - ease(kk(tt, PICK + 0.3, PICK + 0.7)))
        a["held"] = "phone" if tt >= PICK + 0.3 else None; a["arms"] = "hold" if tt >= PICK + 0.3 else "down"; a["look"] = 1
    if KIN[1] <= tt < TITLE:
        a["look"] = 1 if who != "tota" else -1
        if who == "tota": a["held"] = "phone"; a["arms"] = "hold"
        if who == "shatta": a["expr"] = "sleepy" if tt < PH1[0] else "scared"
        if tt >= T("E04"): a["expr"] = "shock" if who != "zalata" else "flat"
        if tt >= T("E06"): a["expr"] = "scared"
    if tt >= TITLE:
        a["expr"] = "neutral" if who != "zalata" else "flat"
        if who == "tota": a["held"] = "phone"; a["arms"] = "hold"
        if tt >= MAIL: a["look"] = -1; a["expr"] = "shock" if tt < MAIL + 0.6 else a["expr"]
        if tt >= WMB[0]:
            k = walk_to(a, VS[who], MB[who], (WMB[0] + off * 0.3, WMB[1] - 0.2), tt, 8); a["look"] = -1
            if k >= 1: a["look"] = -1; a["lean"] = -0.35   # looking up at the mailboxes
        if tt >= T("E09"):
            a["lean"] = 0; a["look"] = 1 if who != "zalata" else -1
            if who == "zalata": a["held"] = "photo"; a["arms"] = "hold"
        if tt >= T("E12") - 0.2:
            a["expr"] = "shock"; a["look"] = 1
        if tt >= RUN[0]:
            k = walk_to(a, MB[who], DR[who], (RUN[0] + off * 0.2, RUN[1]), tt, 11); a["look"] = 1
            if who == "zalata": a["held"] = "nbpen"
        if tt >= BACKOFF[0]:
            k = walk_to(a, DR[who], BK[who] if tt >= BACKOFF[1] + 0.01 and False else (DR[who][0] + 180, 1040, 1.95), BACKOFF, tt, 10)
            a["look"] = -1; a["expr"] = "scared"
            if who == "zalata" and tt >= T("E14"): a["expr"] = "angry"
        if tt >= WAKE + 0.5:
            mid = (DR[who][0] + 180, 1040, 1.95)
            walk_to(a, mid, BK[who], (WAKE + 0.5 + off * 0.3, WAKE + 2.4 + off * 0.3), tt, 9); a["look"] = -1; a["expr"] = "scared"
        if tt >= PIN[0]: a["expr"] = "scared"; a["arms"] = "scared" if who == "shatta" else a["arms"]
        if tt >= T("E17") + 0.3 and tt < NDESC[0]: a["expr"] = "smug"  # Abdo bumping his head is funny
        if tt >= T("E20"): a["expr"] = "neutral" if who != "zalata" else "flat"; a["arms"] = "down" if who != "zalata" else "hold"
        if tt >= T("E24"):
            a["expr"] = "scared"
            if who == "shatta": a["expr"] = "shock"; a["arms"] = "scared"
        if tt >= POUT[0] + 1.0: a["expr"] = "neutral" if who != "zalata" else "flat"; a["arms"] = "down" if who != "zalata" else "hold"
        if who == "tota" and tt >= TRUN[0]:
            k = walk_to(a, BK["tota"], TOTA_DOOR, TRUN, tt, 11); a["look"] = -1; a["held"] = "phone"; a["arms"] = "hold"
            if tt >= BBACK[0]:
                walk_to(a, TOTA_DOOR, BK["tota"], (BBACK[0], BBACK[0] + 1.6), tt, 9); a["look"] = 1 if tt < BBACK[0] + 1.6 else -1; a["expr"] = "happy"
        if tt >= T("E28"): a["look"] = -1 if who != "zalata" else -1
    return a

def actors(set_, tt, sh):
    A = []
    if sh.get("ventcu") or sh.get("boxcu") or sh.get("dutch") and tt < T("E32"): return A
    if set_ == "stairs":
        if sh.get("mood") == "dawn":
            for who, d0 in (("tota", 0.0), ("shatta", 0.55), ("zalata", 0.95)):
                a = A_(who, (1150, 330, 0.6), look=0, expr="sleepy" if who != "tota" else "happy")
                xo = {"tota": 0, "shatta": -70, "zalata": 70}[who]
                k = walk_to(a, (1170 + xo * 0.3, 330, 0.55), (1150 + xo, 1020, 1.9), (DESC[0] + d0, DESC[0] + d0 + 2.6), tt, 7)
                if who == "zalata": a["held"] = "nbpen"; a["arms"] = "hold"; a["expr"] = "flat"
                if k >= 1: continue
                if tt >= DESC[0] + d0: A.append(a)
        else:
            n = A_("nana", (1170, 330, 0.55), look=0, expr="flat")
            walk_to(n, (1170, 330, 0.55), (1150, 1030, 1.95), (NDESC[0] + 0.2, NDESC[1] - 0.1), tt, 6)
            A.append(n)
        return A
    if set_ == "street":
        if sh.get("phonepov"): return A
        u = tt - POV[0]
        ab = A_("abdo", (880, 800, 2.0), look=1, expr="neutral")
        ab["alpha"] = kk(u, 0.4, 0.9)
        if u >= 1.0:
            walk_to(ab, (880, 800, 2.0), (1180, 805, 2.0), (POV[0] + 1.0, POV[0] + 2.0), tt, 7)
        if u >= 3.0:
            walk_to(ab, (1180, 805, 2.0), (1000, 1120, 3.1), (POV[0] + 3.0, POV[1] + 0.4), tt, 6); ab["look"] = -1
        A.append(ab)
        if u >= 1.9:
            pa = A_("pasha", (1250, 790, 2.0), look=-1, expr="flat")
            pa["alpha"] = kk(u, 1.9, 2.4)
            if u >= 2.6:
                walk_to(pa, (1250, 790, 2.0), (880, 1130, 3.3), (POV[0] + 2.6, POV[1] + 0.2), tt, 6); pa["look"] = -1
            A.append(pa)
        return A
    if set_ != "lobby": return A
    for who in KIDS:
        if tt < KIN[0]: break
        a = kid_pos(who, tt)
        if not a.get("hide"): A.append(a)
    # Nana
    if NIN[0] <= tt < TL[0]:
        n = A_("nana", NANA_P, look=-1, expr="flat")
        walk_to(n, STB, NANA_P, NIN, tt, 6)
        if tt >= T("E21"): n["expr"] = "angry"
        if tt >= T("E23"): n["expr"] = "angry"
        if PEXIT[0] <= tt < T("E24"): n["expr"] = "angry"; n["arms"] = "hips"
        if tt >= POUT[1]: n["expr"] = "sad"
        if tt >= POUT[1] + 0.5:
            k = walk_to(n, NANA_P, STB, (POUT[1] + 0.5, POUT[1] + 2.5), tt, 6); n["look"] = 1
            if k >= 1: n = None
        if n: A.append(n)
    # Pasha (lobby)
    if PIN[0] <= tt < POUT[1]:
        pa = A_("pasha", PASHA_P, look=1, expr="smug")
        walk_to(pa, (ENTR[0], ENTR[1], 0.75), PASHA_P, (PIN[0], PIN[1] - 0.2), tt, 5)
        if T("E22") - 0.1 <= tt < PEXIT[0] + 0.5:
            pa["held"] = "paper"; pa["arms"] = "hold"
            if tt >= PUSHBACK: pa["expr"] = "flat"
        if tt >= PEXIT[0]:
            pa["look"] = -1
            k = walk_to(pa, PASHA_P, PASHA_TURN, PEXIT, tt, 5)
            if tt >= T("E24") - 0.2: pa["look"] = 1; pa["expr"] = "flat"
            if tt >= POUT[0]:
                walk_to(pa, PASHA_TURN, (ENTR[0], ENTR[1], 0.75), (POUT[0] + 0.2, POUT[1]), tt, 5); pa["look"] = -1
        if tt >= PIN[0] and tt < PIN[0] + 1.2: pa["sil"] = 1 - kk(tt, PIN[0] + 0.4, PIN[0] + 1.2)
        A.append(pa)
    # Abdo (day)
    if AIN[0] <= tt < POUT[1] + 0.3:
        ab = A_("abdo", ABDO_P, look=1, expr="neutral")
        walk_to(ab, (ENTR[0], ENTR[1], 0.75), ABDO_P, (AIN[0], AIN[1]), tt, 5)
        if BUMP <= tt < BUMP + 2.0: ab["expr"] = "shock"; ab["stars"] = True
        if tt >= POUT[0] + 0.3:
            walk_to(ab, ABDO_P, (ENTR[0], ENTR[1], 0.75), (POUT[0] + 0.3, POUT[1] + 0.3), tt, 5); ab["look"] = -1; ab["expr"] = "scared"
        A.append(ab)
    # Abdo (night)
    if tt >= AIN2[0]:
        ab = A_("abdo", (420, 1010, 1.9), look=-1, expr="scared", held="phone", arms="hold")
        walk_to(ab, (ENTR[0], ENTR[1], 0.75), (420, 1010, 1.9), AIN2, tt, 4)
        if tt >= HAND[0]: ab["lean"] = -0.4; ab["look"] = -1
        if tt >= FREEZE: ab["expr"] = "shock"; ab["lean"] = 0
        if tt >= T("E31"): ab["expr"] = "happy"; ab["held"] = "keys"; ab["arms"] = "up"
        if tt >= RED_ON: ab["look"] = 1; ab["expr"] = "scared"; ab["arms"] = "hold"
        if tt >= T("E32"): ab["expr"] = "shock"
        A.append(ab)
    # doorman
    b = A_("bondo2", BENCH, look=1, expr="sleepy", lean=-0.25)
    if tt >= WAKE:
        b["lean"] = 0; b["expr"] = "sleepy"
        if tt >= T("E15") + 0.8: b["expr"] = "angry"
        if tt >= BWALK[0]:
            k = walk_to(b, BENCH, BONDO_D, BWALK, tt, 6); b["look"] = 1
        if tt >= PIN[0]:
            walk_to(b, BONDO_D, BONDO_C, (PIN[0] + 0.2, PIN[1] + 0.6), tt, 6); b["look"] = 1; b["expr"] = "neutral"
        if tt >= T("E18"): b["look"] = 1
        if tt >= T("E20"): b["look"] = -1; b["expr"] = "neutral"
        if tt >= BBACK[0]:
            k = walk_to(b, BONDO_C, BENCH, (BBACK[0], BBACK[1] - 0.2), tt, 6); b["look"] = -1; b["expr"] = "sleepy"
            if k >= 1: b["lean"] = -0.25; b["look"] = 1
    A.append(b)
    return A

def jump_off(who, tt):
    for j in jumps.get(who, []):
        if 0 <= tt - j < 0.4: return math.sin((tt - j) / 0.4 * math.pi) * 45
    return 0
def expr_of(k, lt):
    e = EXPR.get(k, "neutral")
    if isinstance(e, str): return e
    cur = e[0][1]
    for f, ex in e:
        if lt / DUR[k] >= f: cur = ex
    return cur

HANDS = {"hold": (46, 104), "up": (72, 186), "point": (84, 140), "talk": (60, 126), "hips": (48, 94), "down": (34, 62), "scared": (40, 150)}
def draw_scene_chars(set_, tt, cam, sh):
    x0, y0, z = cam
    layer = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0))
    k, lt = line_at(tt); lights = []
    for a in sorted(actors(set_, tt, sh), key=lambda a: (a["s"], a["y"])):
        who = a["who"]; talking = k is not None and WHO[k] == who
        expr = a.get("expr", "neutral")
        if talking: expr = expr_of(k, lt)
        mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
        if who == "abdo" and k in ("E05",) or who == "pasha" and k == "E06": mouth = 0
        arms = a.get("arms", "down")
        if talking and not a.get("held") and k in ARMS: arms = ARMS[k]
        bob = abs(math.sin(a["walk"])) * 5 * a["s"] if a.get("walk") is not None else 0
        wy = a["y"] - jump_off(who, tt) - bob
        shiver = math.sin(tt * 60) * 2.5 if expr in ("scared", "shock") and who in KIDS + ("abdo",) else 0
        blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11 and expr != "sleepy"
        X = (a["x"] + shiver - x0) * z; Y = (wy - y0) * z; s = a["s"] * z
        al = a.get("alpha", 1.0)
        tgt = layer if al >= 0.999 else Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0))
        p = P(tgt)
        p.ell(X, (a["y"] - y0) * z + 4 * s, 46 * s, 9 * s, (0, 0, 0, 110), None)
        draw_char(p, who, X, Y, s, expr, mouth, a.get("look", 0), blink, arms, tt, a.get("held"), a.get("lean", 0), a.get("walk"))
        S = s * CH[who]["scale"]
        if who == "pasha":   # fedora + cigar (brand look from Ep2)
            hy = Y - 190 * S + math.sin(tt * 2.2 + X) * 1.6 * S; hx = X + a.get("lean", 0) * 18 * S
            p.rect(hx - 30 * S, hy - 70 * S, hx + 30 * S, hy - 34 * S, (22, 22, 28, 255), INK, 2.5 * S, 14 * S)
            p.line([(hx - 10 * S, hy - 68 * S), (hx + 10 * S, hy - 66 * S)], (60, 60, 70, 255), 3 * S)
            p.rect(hx - 29 * S, hy - 46 * S, hx + 29 * S, hy - 38 * S, (140, 25, 30, 255), None)
            p.ell(hx, hy - 36 * S, 60 * S, 10 * S, (22, 22, 28, 255), INK, 2.5 * S)
            lk = a.get("look", 0); cxg = hx + (30 if lk >= 0 else -30) * S
            p.line([(cxg - 2 * S, hy + 30 * S), (cxg + (16 if lk >= 0 else -16) * S, hy + 27 * S)], (110, 70, 40, 255), 5 * S)
            ex = cxg + (17 if lk >= 0 else -17) * S
            gl = 0.6 + 0.4 * math.sin(tt * 3.1) ** 2
            p.ell(ex, hy + 27 * S, 3.5 * S, 3.5 * S, (255, int(120 + 80 * gl), 40, 255), None)
            for i in range(3):
                u = ((tt * 0.5 + i / 3) % 1)
                p.ell(ex + 6 * S * math.sin(u * 6 + i), hy + 20 * S - 60 * S * u, (4 + 8 * u) * S, (4 + 8 * u) * S, (220, 220, 225, int(90 * (1 - u))), None)
        if a.get("stars"):
            hy = Y - 190 * S
            for i in range(4):
                ang = tt * 5 + i * math.pi / 2
                sx_, sy_ = X + math.cos(ang) * 55 * S, hy - 60 * S + math.sin(ang) * 14 * S
                p.poly([(sx_, sy_ - 9 * S), (sx_ + 3 * S, sy_ - 3 * S), (sx_ + 9 * S, sy_), (sx_ + 3 * S, sy_ + 3 * S), (sx_, sy_ + 9 * S),
                        (sx_ - 3 * S, sy_ + 3 * S), (sx_ - 9 * S, sy_), (sx_ - 3 * S, sy_ - 3 * S)], (255, 220, 60, 255), INK, 1.5 * S)
        if who == "bondo2" and a.get("lean", 0) < 0 and tt > 0:   # Zzz
            for i in range(3):
                u = ((tt * 0.6) + i / 3) % 1
                text(tgt, (X + (40 + 30 * u + i * 6) * S) * SS, (Y - (220 + 140 * u) * S) * SS, "Z", int((26 + 18 * i) * S * SS), (255, 255, 255, int(255 * (1 - u))), sw=2)
        if a.get("sil"):   # backlit silhouette in the doorway
            sil = a["sil"]; al_ = tgt.getchannel("A")
            dark = Image.new("RGBA", tgt.size, (10, 10, 14, 255)); dark.putalpha(al_.point(lambda v: int(v * sil)))
            tgt.alpha_composite(dark)
        if tgt is not layer:
            tgt.putalpha(tgt.getchannel("A").point(lambda v: int(v * al)))
            layer.alpha_composite(tgt)
        hx_, hy_ = HANDS.get(arms, (46, 104))
        hand = (X + hx_ * S, Y - hy_ * S)
        if who == "abdo" and a.get("held") == "phone" and set_ == "lobby" and tod(sh, tt) < 0.5:
            lights.append((hand[0] + 40 * S, hand[1] - 10 * S, 300 * z, 1.1, (0.95, 0.97, 1.0)))
    return layer, lights

def tint_layer(layer, tint, lvl):
    rgb = layer.convert("RGB"); al = layer.getchannel("A")
    c = tuple(int((v * 0.55 + 255 * 0.45) * min(1.0, lvl)) for v in tint)
    rgb = ImageChops.multiply(rgb, Image.new("RGB", rgb.size, c))
    out = rgb.convert("RGBA"); out.putalpha(al); return out

LW, LH = W // 8, H // 8
gy, gx = np.mgrid[0:LH, 0:LW] * 8.0
def glow(X, Y, R): return np.exp(-((gx - X) ** 2 + (gy - Y) ** 2) / (R * R))
def band(Xc, R): return np.exp(-((gx - Xc) ** 2) / (R * R))
RED = np.array([1.3, 0.12, 0.08], np.float32)

def light_map(set_, sh, tt, cam, lights, d):
    x0, y0, z = cam; W3 = lambda px, py: ((px - x0) * z, (py - y0) * z)
    cool = np.array([0.75, 0.85, 1.1], np.float32)
    m = np.full((LH, LW, 3), 0.44, np.float32) * cool
    X, Y = W3(809, 380); m += 0.35 * glow(X, Y, 380 * z)[..., None] * cool
    if tt < TITLE:   # phone REC dot in the grate / phone screen glow
        X, Y = W3(VC[0] - 8, VC[1] + 8); m += (0.5 if int(tt * 2) % 2 else 0.25) * glow(X, Y, 70 * z)[..., None] * np.array([1.0, 0.3, 0.3], np.float32)
    if SWEEP[0] <= tt < NDOOR + 2:   # car headlights through the street door
        k = kk(tt, SWEEP[0], SWEEP[1]); al = math.sin(min(1, k) * math.pi * 0.5) if tt < SWEEP[1] else max(0, 1 - (tt - SWEEP[1]) / 2.5)
        X, Y = W3(809, 420); m += 1.6 * al * glow(X, Y, 260 * z)[..., None] * np.array([1.2, 1.15, 1.0], np.float32)
        Xc = W3(lerp(1500, 300, ease(k)), 0)[0]
        m += 1.2 * al * (band(Xc, 160 * z) * np.clip((gy - W3(0, 650)[1]) / (300 * z), 0, 1))[..., None] * np.array([1.2, 1.15, 1.0], np.float32)
    if tt >= RED_ON:
        r = 0.75 + 0.25 * math.sin(tt * 6) ** 2
        X, Y = W3(1690, 965); m += 1.2 * r * glow(X, Y, 260 * z)[..., None] * RED
    for X, Y, R, inten, col in lights:
        m += inten * glow(X, Y, R)[..., None] * np.array(col, np.float32)
    lm = np.clip(m / 1.4, 0, 1)
    lm = lm * (1 - d) + d
    return Image.fromarray((lm * 255).astype(np.uint8), "RGB").resize((W, H), Image.BILINEAR)

def sparkle(d, X, Y, r, a):
    col = (255, 250, 220, a)
    d.polygon([(X, Y - r), (X + r * 0.22, Y - r * 0.22), (X + r, Y), (X + r * 0.22, Y + r * 0.22), (X, Y + r),
               (X - r * 0.22, Y + r * 0.22), (X - r, Y), (X - r * 0.22, Y - r * 0.22)], fill=col)

LET = rng.uniform(0, 1, (5, 3))
def props(img, set_, tt, cam, sh, d_):
    x0, y0, z = cam; S = SS * z; d = ImageDraw.Draw(img, "RGBA")
    W2 = lambda wx, wy: ((wx - x0) * S, (wy - y0) * S)
    lw = lambda v: max(1, int(v * S))
    if set_ == "lobby":
        # the basement padlock
        lx, ly = W2(1624, 702); S0 = S; S = S * 1.35
        d.arc([lx - 14 * S, ly - 34 * S, lx + 14 * S, ly - 6 * S], 180, 360, fill=(200, 200, 210, 255), width=lw(5 / 1.35 * 1.35))
        d.rounded_rectangle([lx - 22 * S, ly - 8 * S, lx + 22 * S, ly + 28 * S], int(5 * S), fill=(235, 185, 50, 255), outline=(110, 75, 10, 255), width=max(1, int(2.5 * S)))
        S = S0
        # the floor vent
        a0 = W2(VENT[0], VENT[1]); a1 = W2(VENT[2], VENT[3])
        d.rectangle([a0[0], a0[1], a1[0], a1[1]], fill=(25, 22, 20, 255), outline=(95, 88, 78, 255), width=lw(4))
        for i in range(1, 7):
            xx_ = a0[0] + (a1[0] - a0[0]) * i / 7
            d.line([(xx_, a0[1] + 3 * S), (xx_, a1[1] - 3 * S)], fill=(110, 102, 90, 255), width=lw(3))
        if tt < PICK + 0.3:     # Tota's phone, still recording
            px, py = W2(VC[0] - 8, VC[1] + 6)
            d.rounded_rectangle([px - 13 * S, py - 22 * S, px + 13 * S, py + 22 * S], int(4 * S), fill=(20, 20, 24, 255), outline=(70, 70, 80, 255), width=lw(2))
            d.rectangle([px - 10 * S, py - 18 * S, px + 10 * S, py + 16 * S], fill=(30, 40, 60, 255))
            if int(tt * 2) % 2: d.ellipse([px - 4 * S, py - 4 * S, px + 4 * S, py + 4 * S], fill=(255, 40, 40, 255))
            ImageDraw.Draw(img).text((px, py + 12 * S), "REC", font=ImageFont.truetype(FONT, max(6, int(6 * S))), fill=(255, 90, 90), anchor="mm")
        # street-door leaf (closed except when someone uses it)
        op = 0.0
        for a_, b_ in ((DOOROPEN, POUT[1] + 0.6), (NDOOR, NDOOR + 6.5)):
            if a_ <= tt < b_ + 0.6: op = max(op, ease(kk(tt, a_, a_ + 0.7)) * (1 - ease(kk(tt, b_, b_ + 0.6))))
        if not (TITLE <= tt < DOOROPEN) or True:
            l0 = W2(DOORO[0], DOORO[1]); l1 = W2(DOORO[2], DOORO[3])
            wdt = (l1[0] - l0[0]) * (1 - op)
            if wdt > 1:
                d.rectangle([l0[0], l0[1], l0[0] + wdt, l1[1]], fill=(48, 36, 26, 255), outline=(20, 14, 10, 255), width=lw(3))
                for i in range(1, 4):
                    yy_ = l0[1] + (l1[1] - l0[1]) * i / 4
                    d.line([(l0[0], yy_), (l0[0] + wdt, yy_)], fill=(90, 70, 45, 255), width=lw(3))
                gx0 = l0[0] + wdt * 0.2; gx1 = l0[0] + wdt * 0.8
                d.rectangle([gx0, l0[1] + 20 * S, gx1, l0[1] + (l1[1] - l0[1]) * 0.45], fill=(255, 225, 160, int(150 * max(0.2, d_))) if d_ > 0.3 else (60, 70, 110, 160))
        # letters through the slot
        if MAIL <= tt < TL[0]:
            for i, (a, b, c) in enumerate(LET):
                u = ease(kk(tt, MAIL - 0.2 + i * 0.07, MAIL + 0.3 + i * 0.07))
                px = 790 + a * 60 + (b - 0.5) * 70 * u; py = 520 + 75 * u
                X, Y = W2(px, py); w_ = 14 * S; h_ = 9 * S
                d.polygon([(X - w_, Y - h_), (X + w_, Y - h_ + c * 4 * S), (X + w_, Y + h_), (X - w_, Y + h_ - c * 4 * S)], fill=(245, 240, 225, 255), outline=(120, 110, 90, 255))
        # mailbox 7: the little door opens, a hand takes the photo
        if sh.get("boxcu"):
            mx, my = W2(*MAIL7); k = ease(kk(tt, BOXOPEN, BOXOPEN + 0.5))
            bw, bh = 58 * S, 60 * S
            d.rectangle([mx - bw / 2, my - bh / 2, mx + bw / 2, my + bh / 2], fill=(18, 12, 8, 255))
            dw = bw * (1 - 0.85 * k)
            d.rectangle([mx - bw / 2, my - bh / 2, mx - bw / 2 + dw, my + bh / 2], fill=(110, 70, 35, 255), outline=(40, 25, 10, 255), width=lw(2))
            ImageDraw.Draw(img).text((mx - bw / 2 + dw / 2, my - 8 * S), "7", font=ImageFont.truetype(FONT, max(8, int(22 * S * (1 - 0.6 * k)))), fill=(230, 190, 90), anchor="mm")
            for i in range(14):   # dust
                u = kk(tt, BOXOPEN + 0.2, BOXOPEN + 1.6)
                if 0 < u < 1:
                    px = mx + (rng.uniform(-1, 1)) * bw * 0.6 * (0.3 + u); py = my + (i / 14 - 0.5) * bh + 30 * S * u
                    d.ellipse([px - 3 * S, py - 3 * S, px + 3 * S, py + 3 * S], fill=(200, 190, 160, int(150 * (1 - u))))
            if tt >= BOXOPEN + 0.6:   # Zalata's arm reaching in from below
                u = ease(kk(tt, BOXOPEN + 0.6, BOXOPEN + 1.0)) - ease(kk(tt, BOXOPEN + 1.3, BOXOPEN + 1.7))
                hx, hy = mx + 10 * S, lerp(img.size[1] + 40 * S, my + 4 * S, u)
                d.line([(hx + 90 * S, img.size[1] + 60 * S), (hx, hy)], fill=(22, 22, 22, 255), width=lw(9))
                d.ellipse([hx - 14 * S, hy - 14 * S, hx + 14 * S, hy + 14 * S], fill=(255, 255, 255, 255), outline=(22, 22, 22, 255), width=lw(3))
                if tt >= BOXOPEN + 1.25:
                    d.rectangle([hx - 22 * S, hy - 34 * S, hx + 20 * S, hy - 4 * S], fill=(215, 190, 145, 255), outline=(90, 60, 30, 255), width=lw(2))
    elif set_ == "street" and sh.get("phonepov"):
        # fictional plate on the rear of the car
        px, py = W2(1500, 640)
        d.rounded_rectangle([px - 60 * S, py - 18 * S, px + 60 * S, py + 18 * S], int(4 * S), fill=(245, 245, 240, 255), outline=(30, 30, 30, 255), width=lw(2))
        d.rectangle([px - 60 * S, py - 18 * S, px + 60 * S, py - 8 * S], fill=(60, 110, 190, 255))
        ImageDraw.Draw(img).text((px, py + 5 * S), "7 7 7  ب ش", font=ImageFont.truetype(FONT, max(8, int(15 * S))), fill=(20, 20, 20), anchor="mm")

def post_props(img, set_, tt, cam, sh):
    x0, y0, z = cam; S = SS * z; d = ImageDraw.Draw(img, "RGBA")
    W2 = lambda wx, wy: ((wx - x0) * S, (wy - y0) * S)
    lw = lambda v: max(1, int(v * S))
    if set_ == "lobby":
        # the key ring in the sleeping doorman's pocket (plant) / stolen at night
        if (BBACK[1] - 0.2 <= tt < HAND[0] + 1.0):
            kx, ky = W2(BENCH[0] + 48, BENCH[1] - 100)
            if tt >= HAND[0]: ky -= 40 * S * ease(kk(tt, HAND[0] + 0.6, HAND[0] + 1.0))
            d.ellipse([kx - 9 * S, ky - 9 * S, kx + 9 * S, ky + 9 * S], outline=(225, 185, 60, 255), width=lw(3))
            for j, ang in enumerate((-0.6, 0.0, 0.7)):
                ex_, ey_ = kx + math.sin(ang) * 24 * S, ky + math.cos(ang) * 24 * S
                d.line([(kx + math.sin(ang) * 8 * S, ky + math.cos(ang) * 8 * S), (ex_, ey_)], fill=(225, 185, 60, 255), width=lw(3))
            if KEYCU[0] + 0.5 <= tt < KEYCU[0] + 1.1:
                sparkle(d, kx + 10 * S, ky - 6 * S, (6 + 16 * math.sin(kk(tt, KEYCU[0] + 0.5, KEYCU[0] + 1.1) * math.pi)) * S, 240)
        if HAND[0] <= tt < HAND[1]:   # Abdo's big hand sneaking into the pocket
            u = ease(kk(tt, HAND[0], HAND[0] + 0.7)) - ease(kk(tt, HAND[0] + 1.2, HAND[1]))
            kx, ky = W2(BENCH[0] + 48, BENCH[1] - 100)
            hx, hy = lerp(kx + 420 * S, kx + 12 * S, u), lerp(ky - 60 * S, ky - 10 * S, u)
            d.line([(hx + 500 * S, hy - 120 * S), (hx, hy)], fill=(22, 22, 22, 255), width=lw(11))
            d.ellipse([hx - 17 * S, hy - 17 * S, hx + 17 * S, hy + 17 * S], fill=(255, 255, 255, 255), outline=(22, 22, 22, 255), width=lw(3))

def glass_frame(fr, tt):
    """Looking out through the iron-grilled glass of the street door."""
    ov = Image.new("RGBA", fr.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    d.rectangle([0, 0, W, H], outline=(28, 20, 14, 255), width=150)
    for x in (W * 0.33, W * 0.66):
        d.line([(x, 0), (x, H)], fill=(28, 20, 14, 230), width=16)
    d.line([(0, H * 0.5), (W, H * 0.5)], fill=(28, 20, 14, 230), width=14)
    for cx in (W * 0.33, W * 0.66):
        d.ellipse([cx - 90, H * 0.5 - 90, cx + 90, H * 0.5 + 90], outline=(28, 20, 14, 220), width=10)
    fr = fr.convert("RGBA"); fr.alpha_composite(ov)
    fr = Image.blend(fr.convert("RGB"), Image.new("RGB", fr.size, (255, 230, 190)), 0.06)
    return fr

def phone_ui(fr, tt):
    d = ImageDraw.Draw(fr, "RGBA")
    d.rectangle([40, 40, W - 40, H - 40], outline=(255, 255, 255, 200), width=3)
    for (x, y, sx, sy) in ((80, 80, 1, 1), (W - 80, 80, -1, 1), (80, H - 80, 1, -1), (W - 80, H - 80, -1, -1)):
        d.line([(x, y), (x + 60 * sx, y)], fill=(255, 255, 255, 230), width=6); d.line([(x, y), (x, y + 60 * sy)], fill=(255, 255, 255, 230), width=6)
    if int(tt * 2) % 2: d.ellipse([90, 90, 120, 120], fill=(255, 40, 40, 255))
    ltr(fr, 200, 106, "REC", 34, (255, 255, 255))
    ltr(fr, W - 200, 106, f"00:0{int(tt - T('E27') + 3) % 10}", 34, (255, 255, 255))
    d.rectangle([W / 2 - 160, H / 2 - 100, W / 2 + 160, H / 2 + 100], outline=(255, 214, 90, 230), width=4)

def phone_card(tt, sh):
    """Close-up of Tota's phone playing the night recording."""
    bgc = bg_crop(SRC["lobby_night"], (500, 260, 1.6)).resize((W, H)).filter(ImageFilter.GaussianBlur(14))
    fr = ImageEnhance.Brightness(Image.blend(bgc, bg_crop(SRC["lobby_day"], (500, 260, 1.6)).resize((W, H)).filter(ImageFilter.GaussianBlur(14)), 0.3)).enhance(0.55)
    d = ImageDraw.Draw(fr, "RGBA")
    u = tt - sh["start"]; k = ease(kk(tt, sh["start"], sh["end"]))
    sc = 1.0 + 0.06 * k; cx, cy = W / 2 + math.sin(tt * 1.3) * 6, H / 2 + 20 + math.sin(tt * 0.9) * 5
    pw, ph = 470 * sc, 900 * sc
    d.rounded_rectangle([cx - pw / 2, cy - ph / 2, cx + pw / 2, cy + ph / 2], int(60 * sc), fill=(18, 18, 22), outline=(22, 22, 22), width=8)
    sx0, sy0, sx1, sy1 = cx - pw / 2 + 22 * sc, cy - ph / 2 + 60 * sc, cx + pw / 2 - 22 * sc, cy + ph / 2 - 60 * sc
    d.rounded_rectangle([sx0, sy0, sx1, sy1], int(30 * sc), fill=(14, 20, 36))
    text(fr, cx, sy0 + 70 * sc, "تسجيل صوتي", int(40 * sc), (220, 225, 240), sw=0)
    hh, mm = sh["stamp"]
    if sh.get("scrub"):
        v = int(lerp(0, 192, ease(kk(tt, sh["start"], sh["start"] + 1.2))))
        hh, mm = f"{v // 60:02d}:{v % 60:02d}", "AM"
        hh = f"{(v // 60):02d}:{(v % 60):02d}"
    ltr(fr, cx, sy0 + 190 * sc, f"{hh} {mm}", int(76 * sc), (255, 214, 90), sw=0)
    # waveform
    kln, lt = line_at(tt)
    lvl = 0.25 + 0.15 * math.sin(tt * 7) ** 2
    if kln: lvl = 0.3 + 0.9 * float(ENV[kln][min(int(lt * FPS), len(ENV[kln]) - 1)])
    if sh["stamp"][0] == "12:00":
        if (u % 0.8) < 0.15: lvl += 0.6       # metal steps
    if sh.get("scrub") and u > 1.2: lvl += 0.5 * (1 - abs(math.sin(u * 2)))  # car engine
    n = 34; bw = (sx1 - sx0 - 60 * sc) / n
    for i in range(n):
        hgt = (20 + 220 * lvl * abs(math.sin(i * 1.7 + tt * 11) * 0.6 + math.sin(i * 0.6 - tt * 7) * 0.4)) * sc
        x = sx0 + 30 * sc + i * bw
        col = (255, 90, 90) if i < n * ((u * 0.15) % 1) else (120, 170, 255)
        d.rounded_rectangle([x + 2, cy + 40 * sc - hgt / 2, x + bw - 3, cy + 40 * sc + hgt / 2], 4, fill=col)
    d.ellipse([cx - 45 * sc, sy1 - 150 * sc, cx + 45 * sc, sy1 - 60 * sc], fill=(255, 60, 60))
    d.polygon([(cx - 12 * sc, sy1 - 125 * sc), (cx - 12 * sc, sy1 - 85 * sc), (cx + 20 * sc, sy1 - 105 * sc)], fill=(255, 255, 255))
    # Tota's stickman hands holding it
    for sx in (-1, 1):
        hx = cx + sx * (pw / 2 + 4); hy = cy + 180 * sc
        d.line([(hx + sx * 140, H + 40), (hx, hy)], fill=(22, 22, 22), width=int(16 * sc))
        d.ellipse([hx - 30 * sc, hy - 30 * sc, hx + 30 * sc, hy + 30 * sc], fill=(255, 255, 255), outline=(22, 22, 22), width=6)
    # REC glow on the screen
    return fr

def photo_card(tt, sh):
    """Old photo of young Roshdy at a studio microphone, then flipped: 1958."""
    fr = ImageEnhance.Brightness(bg_crop(SRC["lobby_day"], (0, 120, 1.8)).resize((W, H)).filter(ImageFilter.GaussianBlur(16))).enhance(0.6)
    k = ease(kk(tt, sh["start"], sh["start"] + 0.6))
    fl = kk(tt, FLIP + 0.15, FLIP + 0.75); ang = fl * math.pi
    side = "front" if ang < math.pi / 2 else "back"
    wscale = abs(math.cos(ang))
    pw, ph = 760, 560
    card_ = Image.new("RGBA", (pw, ph), (0, 0, 0, 0)); d = ImageDraw.Draw(card_)
    if side == "front":
        d.rectangle([0, 0, pw, ph], fill=(236, 226, 200, 255))
        inner = Image.new("RGBA", (pw - 60, ph - 90), (150, 125, 90, 255)); pd = P(inner)
        di = ImageDraw.Draw(inner)
        for i in range(0, ph, 18): di.line([(0, i), (pw, i - 40)], fill=(140, 115, 80, 255), width=6)   # studio wall panels
        # microphone on a stand
        mx, my = 450 / SS, 120 / SS
        pd.line([(mx, my + 20), (mx, 330 / SS)], (40, 35, 30, 255), 4); pd.line([(mx - 40, 330 / SS), (mx + 40, 330 / SS)], (40, 35, 30, 255), 4)
        pd.ell(mx, my, 20, 30, (70, 65, 60, 255), INK, 3)
        for j in range(5): pd.line([(mx - 16, my - 18 + j * 9), (mx + 16, my - 18 + j * 9)], (120, 115, 110, 255), 1.5)
        draw_char(pd, "roshdy", 230 / SS, 450 / SS, 1.25, "happy", 0.4, 1, False, "point", 0.0, None, 0, None)
        g = inner.convert("L"); inner = Image.merge("RGBA", (g.point(lambda v: min(255, int(v * 1.05 + 25))), g.point(lambda v: int(v * 0.92 + 15)), g.point(lambda v: int(v * 0.72)), Image.new("L", g.size, 255)))
        card_.paste(inner, (30, 30))
        d.text((pw / 2, ph - 30), "", fill=(0, 0, 0))
    else:
        d.rectangle([0, 0, pw, ph], fill=(228, 216, 186, 255))
        for i in range(6): d.line([(40, 120 + i * 70), (pw - 40, 120 + i * 70)], fill=(200, 188, 160, 255), width=2)
        ImageDraw.Draw(card_).text((pw / 2, ph / 2), "1958", font=ImageFont.truetype(FONT, 150), fill=(60, 40, 110), anchor="mm")
        text(card_, pw / 2, ph / 2 + 150, "استوديو العمارة", 46, (70, 50, 110), (228, 216, 186), 0)
    for _ in range(40):   # age spots
        x_, y_ = rng.uniform(0, pw), rng.uniform(0, ph)
    cw_ = max(2, int(pw * wscale))
    card_ = card_.resize((cw_, ph))
    sc = lerp(0.6, 1.0, k)
    card_ = card_.resize((max(2, int(cw_ * sc)), int(ph * sc))).rotate(-4 + 4 * k, expand=True, resample=Image.BICUBIC)
    fr = fr.convert("RGBA")
    sh_ = Image.new("RGBA", card_.size, (0, 0, 0, 0)); sh_.putalpha(card_.getchannel("A").point(lambda v: int(v * 0.5)))
    fr.alpha_composite(sh_.filter(ImageFilter.GaussianBlur(10)), (int(W / 2 - card_.width / 2 + 14), int(H / 2 - card_.height / 2 + 20)))
    fr.alpha_composite(card_, (int(W / 2 - card_.width / 2), int(H / 2 - card_.height / 2)))
    return fr.convert("RGB")

def ltr(img, x, y, s, size, fill, stroke=(10, 10, 10), sw=3):
    ImageDraw.Draw(img).text((x, y), s, font=ImageFont.truetype(FONT, size), fill=fill, anchor="mm", direction="ltr", stroke_width=sw, stroke_fill=stroke)

def card(name, tt, sh):
    k = (tt - sh["start"]) / (sh["end"] - sh["start"])
    fr = Image.new("RGB", (W, H), (8, 8, 12))
    g = lambda c: tuple(int(v * min(1, k * 4)) for v in c)
    if name == "title":
        text(fr, W / 2, H / 2 - 110, "عمارة نعناعة", 110, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 + 20, "الموسم التاني: " + SEASON, 70, g((255, 120, 90)), (30, 5, 5), 5)
        text(fr, W / 2, H / 2 + 125, EPT, 52, g((225, 225, 225)))
    elif name == "endcard":
        text(fr, W / 2, H / 2 - 130, "الحلقة 4 بكرة: النزول", 100, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 + 10, "عبده هيفتح البدروم؟ اكتبوا توقعكم", 58, g((235, 235, 235)))
        text(fr, W / 2, H / 2 + 110, "اعمل اشتراك عشان ما يفوتكش", 46, g((200, 200, 200)))
    return fr

def hud(fr, tt, v=False):
    sc = 0.85 if v else 1.0; cx = 540 if v else W / 2
    a0 = T("E08") + 1.6
    if a0 <= tt < T("E08") + DUR["E08"] + 1.0:
        d = ImageDraw.Draw(fr, "RGBA"); y = 1700 if v else 120
        d.rounded_rectangle([cx - 470 * sc, y - 50 * sc, cx + 470 * sc, y + 50 * sc], int(22 * sc), fill=(20, 60, 30, 220), outline=(120, 230, 120, 255), width=4)
        text(fr, cx, y, "إجابة امبارح: صندوق البوسطة رقم 7 ✓", int(42 * sc), (200, 255, 200))

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
    text(bgv, 540, 300, SEASON, 96, (255, 120, 90), (40, 10, 10), 6)
    text(bgv, 540, 425, EPT, 52, (235, 235, 235))
    k, _ = line_at(tt)
    if k:
        ls_ = wrap(SUB[k])
        if len(ls_) <= 4:
            for i, l in enumerate(ls_): text(bgv, 540, 1290 + i * 80, l, 60, sw=6)
        else:
            for i, l in enumerate(wrap(SUB[k], 30)[:6]): text(bgv, 540, 1270 + i * 64, l, 50, sw=5)
    hud(bgv, tt, True)
    if PUZ <= tt < PUZ_END:
        d.rounded_rectangle([40, 1640, 1040, 1800], 26, fill=(20, 20, 30), outline=(255, 214, 90), width=5)
        text(bgv, 540, 1695, "لغز النهارده: مين كان بيقول «أيوا يا باشا»؟", 44, (255, 214, 90))
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
    if set_ in ("title", "endcard"): return finish(card(set_, tt, sh), tt)
    if set_ == "black": return Image.new("RGB", (W, H), (0, 0, 0))
    if set_ == "phone": return finish(phone_card(tt, sh), tt, True)
    if set_ == "photo": return finish(photo_card(tt, sh), tt)
    cam = cam_at(sh, tt)
    d = tod(sh, tt) if set_ == "lobby" else 1
    img = bg_frame(set_, cam, d, sh)
    props(img, set_, tt, cam, sh, d)
    layer, lights = draw_scene_chars(set_, tt, cam, sh)
    if set_ == "lobby":
        tint = tuple(int(lerp(a, b, d)) for a, b in zip((165, 180, 235), (255, 246, 228)))
    elif set_ == "stairs": tint = (200, 210, 245) if sh.get("mood") == "dawn" else (255, 240, 215)
    else: tint = (255, 244, 225)
    layer = tint_layer(layer, tint, 0.97)
    img.paste(layer, (0, 0), layer)
    post_props(img, set_, tt, cam, sh)
    fr = img.resize((W, H), Image.LANCZOS)
    if sh.get("dutch"):
        fr = fr.rotate(7, resample=Image.BICUBIC).crop((80, 45, W - 80, H - 45)).resize((W, H), Image.LANCZOS)
    dark = set_ == "lobby" and d < 0.5
    if set_ == "lobby" and d < 0.999:
        lm = light_map(set_, sh, tt, cam, lights, d)
        fr = ImageChops.multiply(fr, lm); fr = ImageEnhance.Brightness(fr).enhance(lerp(1.7, 1.0, d))
    if sh.get("backlit") and tt < PIN[0] + 1.4:
        fr = Image.blend(fr, Image.new("RGB", fr.size, (255, 236, 200)), 0.12 * (1 - kk(tt, PIN[0] + 0.6, PIN[0] + 1.4)))
    if sh.get("glass"): fr = glass_frame(fr, tt)
    if sh.get("phonepov"): phone_ui(fr, tt)
    return finish(fr, tt, dark)

def render(out_h, out_v, stills=None, t0=0.0, t1=None):
    fh = fv = None
    if not stills:
        mk = lambda w, h, o: subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}",
                                   "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
                                   "-pix_fmt", "yuv420p", o], stdin=subprocess.PIPE)
        fh = mk(W, H, out_h); fv = mk(1080, 1920, out_v)
    t1 = TOTAL if t1 is None else t1
    times = stills or [i / FPS for i in range(int(round(t0 * FPS)), int(round(t1 * FPS)))]
    for i, tt in enumerate(times):
        base = frame(tt)
        h = base.copy(); hud(h, tt)
        if PUZ <= tt < PUZ_END:
            d = ImageDraw.Draw(h, "RGBA")
            d.rounded_rectangle([W / 2 - 700, 60, W / 2 + 700, 175], 24, fill=(20, 20, 30, 215), outline=(255, 214, 90, 255), width=4)
            text(h, W / 2, 117, "لغز النهارده: مين في الموسم الأول كان بيقول «أيوا يا باشا»؟", 38, (255, 214, 90))
        subtitle(h, tt)
        if stills:
            h.save(f"still_h_{tt:.1f}.png"); vertical(base, tt).save(f"still_v_{tt:.1f}.png")
        else:
            fh.stdin.write(h.tobytes()); fv.stdin.write(vertical(base, tt).tobytes())
        if i % 240 == 0: print("frame", i, round(tt, 1), flush=True)
    if fh:
        fh.stdin.close(); fv.stdin.close(); fh.wait(); fv.wait()

def lowpass(x, fc):
    from numpy.fft import rfft, irfft
    X = rfft(x); fq = np.fft.rfftfreq(len(x), 1 / SR); X[fq > fc] *= 0.12; return irfft(X, len(x)).astype(np.float32)

def build_audio(path="mix.wav"):
    buf = np.zeros(int(TOTAL * SR) + SR * 3, dtype=np.float32)
    dr = drone(TOTAL + 1); env = np.zeros(len(dr), np.float32)
    for s_ in shots:
        tense = s_["set"] in ("phone", "black") or (s_["set"] == "lobby" and s_.get("tod", 1) < 0.5 and "tl" not in s_) or s_.get("low") or s_.get("glass")
        if tense: env[int(s_["start"] * SR):int(s_["end"] * SR)] = 1.0
    env[int(PIN[0] * SR):int(POUT[1] * SR)] = np.maximum(env[int(PIN[0] * SR):int(POUT[1] * SR)], 0.55)
    env[int(TL[0] * SR):] = 1.0
    env = np.convolve(env, np.ones(4410) / 4410, mode="same")
    mix_into(buf, dr * env, 0, 1.2)
    r = np.random.default_rng(9)
    S = {"boom": sfx_boom(), **SFXF}
    for t0, nme, g in sfx:
        if nme in S and g > 0: mix_into(buf, S[nme], t0, g)
    # phone playback: tape hiss + muffled old music + metal steps (12:00), engine (03:12)
    n = int((PH1[1] - PH1[0]) * SR); mus = lowpass(np.resize(load_audio("sfx/music_old.mp3"), n).astype(np.float32), 900)
    e = np.ones(n, np.float32); fi = int(0.3 * SR); e[:fi] = np.linspace(0, 1, fi); e[-fi:] = np.linspace(1, 0, fi)
    mix_into(buf, mus * e, PH1[0], 0.5)
    for i in range(4): mix_into(buf, lowpass(SFXF["clang"][:int(0.6 * SR)].copy(), 1500), PH1[0] + 0.3 + i * 0.8, 0.45)
    car = lowpass(SFXF["car"].copy(), 1200); mix_into(buf, car[:int(2.0 * SR)], PH2[0] + 1.1, 0.6)
    for a_, b_ in ((PH1[0], PH2[1]), (T("E05") - 0.2, T("E06") + DUR["E06"])):
        n = int((b_ - a_) * SR); hiss = np.convolve(r.normal(0, 1, n), np.ones(6) / 6, mode="same").astype(np.float32) * 0.04
        mix_into(buf, hiss, a_, 1.0)
    # comic pizzicato: «you're the oldest» + «my twin brother» + the head bump
    for t_, notes in ((T("E14") + 0.1, [392, 330, 262]), (T("E25") + 0.9, [523, 494, 440, 392]), (BUMP + 0.4, [330, 392, 523])):
        for i, f in enumerate(notes):
            tt_ = np.arange(int(SR * 0.4)) / SR
            mix_into(buf, np.sin(2 * np.pi * f * tt_) * np.exp(-tt_ * 12) * 0.09, t_ + i * 0.22, 1.0)
    # low tension string under the Pasha scenes and the final theft
    for a_, b_ in ((PIN[0], T("E24") + DUR["E24"]), (AIN2[0], T("E32") + DUR["E32"])):
        ts = np.arange(int((b_ - a_) * SR)) / SR
        rise = (np.sin(2 * np.pi * (98 + 30 * ts / ts[-1]) * ts) + 0.5 * np.sin(2 * np.pi * (147 + 45 * ts / ts[-1]) * ts)) * 0.04 * np.minimum(1, ts / 2)
        mix_into(buf, rise, a_, 1.0)
    # outdoor ambience while the street door is open
    amb = lowpass(r.normal(0, 1, int((POUT[1] - DOOROPEN) * SR)).astype(np.float32), 500) * 0.02
    mix_into(buf, amb, DOOROPEN, 1.0)
    tsx = np.arange(int(SR * 0.25)) / SR
    for st, g in STEPS:
        nz = np.convolve(r.normal(0, 1, len(tsx)), np.ones(12) / 12, mode="same")
        mix_into(buf, (np.sin(2 * np.pi * 80 * tsx) * np.exp(-tsx * 30) * 0.9 + nz * np.exp(-tsx * 25) * 0.9) * 0.6, st, g)
    for st, k in lines: mix_into(buf, AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8, st, 1.0)
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
        for st, k in lines: print(k, round(st, 2))
    elif sys.argv[1:2] == ["part"]:
        i, n = int(sys.argv[2]), int(sys.argv[3]); a = round(TOTAL * i / n * FPS) / FPS; b = round(TOTAL * (i + 1) / n * FPS) / FPS
        render(f"h_{i}.mp4", f"v_{i}.mp4", None, a, b)
    elif sys.argv[1:2] == ["audio"]:
        build_audio()
    else:
        build_audio(); render("h.mp4", "v.mp4")
        mux("h.mp4", "sirr_elbadroom_ep3.mp4"); mux("v.mp4", "sirr_elbadroom_ep3_vertical.mp4")
