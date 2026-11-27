import sys, os, math, subprocess, wave
sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter, ImageFont
from engine import *

os.chdir(ROOT + "/s2e4")
SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(404)
SEASON = "سر البدروم"
EPT = "الحلقة 4: النزول"

SUB = {
 "F01": "عفريت!... عفريت عينه حمرا!",
 "F02": "فين المفتاح يا عبده؟",
 "F03": "وقع مني يا باشا... ورجلي ما رضيتش تستنى!",
 "F04": "مفيش حاجة اسمها عفاريت... بكرة بالليل، هننزل إحنا.",
 "F05": "آي!... إيه اللي تحت رجلي ده؟!",
 "F06": "مفتاح البدروم!... بيعمل إيه هنا؟!",
 "F07": "حد كان هنا بالليل... وهرب بسرعة.",
 "F08": "لغز امبارح: مين كان بيقول «أيوا يا باشا»؟... أستاذ فهمي!",
 "F09": "يعني أستاذ فهمي عارف الباشا... من زمان.",
 "F10": "عم رشدي قال ما تفتحوهوش بالليل... واحنا في عز الصبح!",
 "F11": "احتمال إننا نندم: 94%",
 "F12": "الحاجة نعناعة راحت السوق... قدامنا ساعة بس.",
 "F13": "البدروم... بارد كده ليه؟",
 "F14": "شغلوا الكشافات.",
 "F15": "فار!!!",
 "F16": "شطة... انزل من على إيدي.",
 "F17": "باب حديد... بعجلة زي الخزنة!",
 "F18": "مش راضية تلف!... ساعدوني!",
 "F19": "ده... استوديو!",
 "F20": "ميكروفونات... أجهزة تسجيل... ده استوديو كامل تحت العمارة!",
 "F21": "أنا كنت عارف!... أنا اللي قلت!",
 "F22": "إنت قلت فار.",
 "F23": "الساعة دي... واقفة.",
 "F24": "لغز النهارده: الساعة واقفة على كام؟... وليه؟ اكتبوا في الكومنتات!",
 "F25": "(شريط) لو وصلتوا هنا... يبقى اللعبة بدأت بجد.",
 "F26": "يا جماعة... الملاية... بتتحرك!",
}
WHO = {"F01": "abdo", "F02": "pasha", "F03": "abdo", "F04": "pasha", "F05": "shatta", "F06": "tota", "F07": "zalata", "F08": "tota",
       "F09": "zalata", "F10": "shatta", "F11": "zalata", "F12": "tota", "F13": "shatta", "F14": "zalata", "F15": "shatta", "F16": "zalata",
       "F17": "tota", "F18": "zalata", "F19": "tota", "F20": "zalata", "F21": "shatta", "F22": "zalata", "F23": "shatta", "F24": "tota",
       "F25": "rec", "F26": "shatta"}
EXPR = {"F01": "shock", "F02": "flat", "F03": "scared", "F04": "smug", "F05": [(0, "shock"), (0.4, "neutral")], "F06": "shock",
        "F07": "flat", "F08": [(0, "neutral"), (0.6, "happy")], "F09": "flat", "F10": "smug", "F11": "flat", "F12": "neutral",
        "F13": "scared", "F14": "flat", "F15": "shock", "F16": "flat", "F17": "shock", "F18": "angry", "F19": "shock", "F20": "happy",
        "F21": "smug", "F22": "flat", "F23": "neutral", "F24": [(0, "neutral"), (0.6, "smug")], "F26": "shock"}
ARMS = {"F01": "scared", "F03": "up", "F04": "talk", "F05": "up", "F06": "point", "F07": "hold", "F08": "point", "F09": "hold",
        "F10": "hips", "F11": "hold", "F12": "point", "F13": "scared", "F14": "hold", "F15": "up", "F16": "hold", "F17": "point",
        "F18": "up", "F19": "point", "F20": "hold", "F21": "hips", "F22": "hold", "F23": "point", "F24": "point", "F26": "scared"}

def _aud(k):
    f = f"audio/{k}_fx.mp3"
    return load_audio(f if os.path.exists(f) else f"audio/{k}.mp3")
AUD = {k: _aud(k) for k in SUB}
ENV = {k: envelope(v) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}
SFXF = {n: load_audio(f"sfx/{n}.mp3") for n in ("whoosh", "creak", "slam", "switch", "steps_metal", "snore", "car", "clang",
                                                 "keys", "car_arrive", "stinger", "music_old", "mouse", "servo", "vault", "unlock",
                                                 "lights", "tape")}

lines, sfx, shots, jumps, shakes = [], [], [], {}, []
def say(t, k): lines.append((t, k)); return t + DUR[k]
def fx(t, n, g=1.0): sfx.append((t, n, g))
def jump(w, t): jumps.setdefault(w, []).append(t)
def shot(set_, s, e, c0, c1=None, **kw): shots.append(dict(set=set_, start=s, end=e, c0=c0, c1=c1 or c0, **kw))
def cut(t, g=0.4): fx(t - 0.12, "whoosh", g)
def T(k): return [st for st, kk_ in lines if kk_ == k][0]
KIDS = ("shatta", "zalata", "tota")

# ---------------- world ----------------
# lobby (morning.png coords)
ENTR = (809, 600); BENCH = (170, 1000, 1.85); STB = (1330, 905, 1.65)
DOOR = (1545, 495, 1830, 938); LOCK = (1624, 702)
KEYSPOT = (540, 1036)
AB_N = (420, 1010, 1.9)
LB = {"tota": (760, 1040, 1.95), "zalata": (940, 1040, 1.95), "shatta": (560, 1040, 1.95)}
BD = {"zalata": (1120, 1040, 1.95), "shatta": (1290, 1040, 1.95), "tota": (1450, 1040, 1.95)}
# car interior (carin.png → 1920 coords)
CAR_P = (1380, 880, 2.3); CAR_A = (560, 900, 2.4)
# corridor
VAULT = (994, 506)
CSTAIR = (330, 760, 1.25)
CW = {"zalata": (620, 900, 1.6), "shatta": (780, 905, 1.6), "tota": (940, 900, 1.6)}
CV = {"zalata": (900, 760, 1.15), "shatta": (1060, 765, 1.15), "tota": (1200, 760, 1.15)}
# studio
SWITCH = (190, 560)
ST = {"tota": (700, 1000, 1.95), "shatta": (900, 1010, 1.95), "zalata": (1100, 1000, 1.95)}
REELS = ((572, 394), (647, 394)); CLOCK = (979, 128); SHEET = (1762, 300)

def CU(who, pos, z=2.2, dx=0):
    x, y, s = pos; S = s * CH[who]["scale"]
    if who == "tota": z *= 1.3; dx -= 50
    hy = y - 190 * S
    return (x + dx, hy + H / (2 * z) - 1.45 * 46 * S - 25, z)

t = 0.0
# ===== 0. COLD OPEN — same second Ep3 ended =====
STEP1 = 0.35; fx(STEP1, "steps_metal", 1.0); shakes.append((STEP1, 6))
shot("lobby", 0, 0.9, (1690, 860, 2.2), (1690, 880, 2.6), tod=0)
shot("lobby", 0.9, 1.3, CU("abdo", AB_N, 2.0), CU("abdo", AB_N, 2.2), tod=0)
t = 1.3
s = t; t = say(t, "F01")
RUNA = (s + 0.25, s + 2.0); KEYFLY = s + 0.45
shot("lobby", s, t + 0.4, (700, 640, 1.2), (760, 600, 1.35), tod=0); t += 0.4
KINS = (t, t + 1.7); fx(t + 0.2, "keys", 1.2); fx(t + 0.75, "keys", 0.6)
shot("lobby", t, KINS[1], (KEYSPOT[0] - 20, KEYSPOT[1] - 70, 3.4), (KEYSPOT[0], KEYSPOT[1] - 60, 3.8), tod=0, keyins=True); t = KINS[1]
fx(t - 0.3, "slam", 0.9); fx(t - 0.2, "car", 0.8)
CARIN = (t, None); ADIVE = (t + 0.1, t + 0.8)
shot("carin", t, t + 1.4, (960, 540, 1.0), (960, 540, 1.06)); t += 1.4
s = t; t = say(t, "F02") + 0.1
shot("carin", s, t, CU("pasha", CAR_P, 1.7), CU("pasha", CAR_P, 1.85))
s = t; t = say(t, "F03") + 0.15
shot("carin", s, t, CU("abdo", CAR_A, 1.6), CU("abdo", CAR_A, 1.75))
s = t; t = say(t + 0.1, "F04") + 0.5
shot("carin", s, t, (1200, 470, 1.4), CU("pasha", CAR_P, 2.3), low=True)
DRIVE = t - 0.4; fx(t - 0.6, "car_arrive", 0.6)
shot("title", t, t + 2.0, None); TITLE = t; t += 2.0
# ===== 1. MORNING =====
TLM = (t, t + 2.8)
shot("lobby", t, TLM[1], (760, 620, 1.12), (700, 640, 1.18), tl=(0, 1, TLM)); t = TLM[1]
fx(TLM[0] + 0.4, "snore", 0.6)
DESC = (t, t + 2.8)
shot("stairs", t, DESC[1], (1150, 560, 1.05), (1150, 620, 1.2), mood="day"); t = DESC[1]
KIN = (t, t + 3.2); STEPON = KIN[1] - 0.1
shot("lobby", t, KIN[1], (1100, 640, 1.2), (800, 660, 1.3), tod=1); t = KIN[1]
s = t; t = say(t, "F05") + 0.1; jump("shatta", s)
shot("lobby", s, t, CU("shatta", LB["shatta"], 1.8), (KEYSPOT[0], KEYSPOT[1] - 80, 3.0), tod=1, ease="crash")
PICKUP = t + 0.3
s = t; t = say(t + 0.2, "F06") + 0.1
shot("lobby", s, t, CU("tota", LB["tota"], 1.6), CU("tota", LB["tota"], 1.8), tod=1)
s = t; t = say(t, "F07") + 0.1
shot("lobby", s, t, CU("zalata", LB["zalata"], 1.7), CU("zalata", LB["zalata"], 1.9), tod=1)
s = t; t = say(t, "F08") + 0.1
shot("lobby", s, t, CU("tota", LB["tota"], 1.6), CU("tota", LB["tota"], 1.75), tod=1)
s = t; t = say(t, "F09") + 0.2
shot("lobby", s, t, CU("zalata", LB["zalata"], 1.8), CU("zalata", LB["zalata"], 2.0), tod=1)
s = t; t = say(t, "F10") + 0.1
shot("lobby", s, t, (760, 650, 1.35), (760, 650, 1.45), tod=1)
s = t; t = say(t, "F11") + 0.2
shot("lobby", s, t, CU("zalata", LB["zalata"], 1.8), CU("zalata", LB["zalata"], 2.0), tod=1)
SNZ = t; fx(t + 0.1, "snore", 1.0)
shot("lobby", t, t + 1.3, CU("bondo2", BENCH, 1.8), CU("bondo2", BENCH, 1.9), tod=1); t += 1.3
s = t; t = say(t, "F12") + 0.1
shot("lobby", s, t, CU("tota", LB["tota"], 1.6), CU("tota", LB["tota"], 1.8), tod=1)
WBD = (t, t + 2.4)
shot("lobby", t, WBD[1], (900, 640, 1.2), (1300, 640, 1.3), tod=1); t = WBD[1]
UNLOCK = t + 0.4; fx(UNLOCK, "unlock", 1.1)
shot("lobby", t, t + 2.2, (LOCK[0], LOCK[1] + 20, 4.0), (LOCK[0], LOCK[1] + 40, 4.4), tod=1, lockins=True); t += 2.2
DOPEN = t + 0.1; fx(DOPEN, "creak", 1.0)
shot("lobby", t, t + 1.9, (1500, 640, 1.35), (1560, 660, 1.6), tod=1, low=True); t += 1.9
s = t; t = say(t, "F13") + 0.2
shot("lobby", s, t, CU("shatta", BD["shatta"], 1.8), CU("shatta", BD["shatta"], 2.0), tod=1)
# ===== 3. DESCENT =====
cut(t, 0.3); CDESC = (t, t + 2.4)
shot("corridor", t, CDESC[1], (600, 560, 1.15), (650, 600, 1.25)); t = CDESC[1]
s = t; t = say(t, "F14") + 0.1; FLASH = t - 0.1
for i in range(3): fx(FLASH + i * 0.18, "switch", 0.6)
shot("corridor", s, t + 0.5, CU("zalata", CW["zalata"], 1.6), CU("zalata", CW["zalata"], 1.8)); t += 0.5
CWALK = (t, t + 3.6); MOUSE = t + 1.4; fx(MOUSE - 0.1, "mouse", 1.1)
shot("corridor", t, MOUSE + 0.3, (800, 600, 1.15), (900, 580, 1.3)); t = MOUSE + 0.3
s = t; t = say(t, "F15") + 0.2; JUMPIN = s
shot("corridor", s, t, (900, 640, 1.5), (900, 640, 1.65), ease="crash")
s = t; t = say(t + 0.1, "F16") + 0.3
shot("corridor", s, t, (900, 620, 1.8), (900, 620, 1.9))
BEHIND = t; fx(t + 0.4, "steps_metal", 0.6); fx(t + 1.1, "steps_metal", 0.4)
shot("corridor", t, t + 2.8, (760, 640, 1.3), (380, 560, 1.7)); t += 2.8
CW2 = (t, t + 2.4)
shot("corridor", t, CW2[1], (950, 600, 1.2), (994, 540, 1.6)); t = CW2[1]
s = t; t = say(t, "F17") + 0.1
shot("corridor", s, t, (994, 520, 1.7), (994, 520, 1.9), low=True)
WHEEL = (t, t + 4.2); fx(t + 0.2, "vault", 1.1)
shot("corridor", t, t + 1.6, (VAULT[0], VAULT[1], 3.3), (VAULT[0], VAULT[1], 3.6), wheelins=True); t += 1.6
s = t; t = say(t, "F18") + 0.2
shot("corridor", s, t, CU("zalata", CV["zalata"], 1.7), CU("zalata", CV["zalata"], 1.9))
VOPEN = t; shakes.append((t, 10))
shot("corridor", t, t + 2.0, (994, 560, 1.5), (994, 506, 2.4)); t += 2.0
# ===== 4. THE STUDIO =====
SIN = (t, t + 2.8)
shot("studio", t, SIN[1], (960, 600, 1.12), (900, 620, 1.18)); t = SIN[1]
SCAN = t
for c0_, c1_ in (((1500, 250, 2.6), (1560, 270, 2.9)), ((870, 380, 3.0), (900, 390, 3.3)), ((1400, 520, 2.4), (1300, 520, 2.6))):
    shot("studio", t, t + 1.7, c0_, c1_, scan=True); t += 1.7
LIGHTS = t + 0.5; fx(LIGHTS - 0.05, "lights", 1.1); fx(LIGHTS + 0.9, "stinger", 0.9)
shot("studio", t, t + 3.2, (600, 560, 1.3), (960, 540, 1.0)); t += 3.2
s = t; t = say(t, "F19") + 0.2
shot("studio", s, t, CU("tota", (300, 1000, 1.95), 1.5), CU("tota", (300, 1000, 1.95), 1.65))
s = t; t = say(t, "F20") + 0.2
shot("studio", s, s + DUR["F20"] * 0.45, (330, 430, 2.4), (380, 430, 2.6))
shot("studio", s + DUR["F20"] * 0.45, t, (610, 400, 2.8), (610, 400, 3.1))
s = t; t = say(t, "F21") + 0.05
shot("studio", s, t, CU("shatta", ST["shatta"], 1.7), CU("shatta", ST["shatta"], 1.9))
s = t; t = say(t + 0.1, "F22") + 0.4
shot("studio", s, t, CU("zalata", ST["zalata"], 1.8), CU("zalata", ST["zalata"], 2.0))
s = t; t = say(t + 0.2, "F23") + 0.2
shot("studio", s, s + 0.9, CU("shatta", ST["shatta"], 1.7), CU("shatta", ST["shatta"], 1.8))
shot("studio", s + 0.9, t + 0.6, (CLOCK[0], CLOCK[1] + 30, 3.6), (CLOCK[0], CLOCK[1] + 20, 4.4), clockins=True); t += 0.6
PUZ = t; s = t; t = say(t + 0.1, "F24") + 0.8; PUZ_END = t
shot("studio", s, t, CU("tota", (300, 1000, 1.95), 1.5), CU("tota", (300, 1000, 1.95), 1.7))
# ===== 5. CLIFF =====
TAPE = t + 0.3; fx(TAPE, "tape", 1.1); shakes.append((TAPE, 5))
shot("studio", t, t + 1.4, (610, 400, 3.0), (610, 400, 3.3)); t += 1.4
s = t; t = say(t, "F25") + 0.3
shot("studio", s, t, (900, 560, 1.25), (900, 560, 1.4))
SHEETMOVE = t; fx(t, "servo", 1.1)
shot("studio", t, t + 1.8, (1700, 420, 2.0), (1730, 380, 2.4)); t += 1.8
s = t; t = say(t, "F26") + 0.2
shot("studio", s, t, CU("shatta", ST["shatta"], 1.7), CU("shatta", ST["shatta"], 2.3), ease="crash")
EYES = t + 0.2; fx(EYES, "switch", 0.8)
shot("studio", t, t + 2.4, (SHEET[0], SHEET[1] + 40, 2.2), (SHEET[0], SHEET[1] + 10, 4.0), ease="crash", dutch=True); t += 2.4
fx(t, "clang", 1.2); fx(t, "boom", 0.9); shakes.append((t - 0.3, 14))
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
for a_, b_, r_, g_ in ((RUNA[0], RUNA[1], 12, 0.6), (DESC[0], DESC[1], 8, 0.4), (KIN[0], KIN[1], 8, 0.45), (WBD[0], WBD[1], 8, 0.45),
                       (CDESC[0], CDESC[1], 7, 0.35), (CWALK[0], MOUSE, 6, 0.35), (CW2[0], CW2[1], 6, 0.35), (SIN[0], SIN[1], 6, 0.35)):
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
def _ld(p): return Image.open(p).convert("RGB").resize((1920, 1080), Image.LANCZOS)
_mor = Image.open(ROOT + "/s1e10/bg/morning.png").convert("RGB")
_st = Image.open(ROOT + "/s1e1/bg/stairs_1080.png").convert("RGB")
_studio = _ld("bg/studio.png")
SRC = {"lobby_day": _mor, "lobby_night": tinted(_mor, 0.9, (150, 165, 230)),
       "stairs_day": tinted(ImageEnhance.Brightness(_st).enhance(1.55), 1.0, (255, 225, 175)),
       "carin": _ld("bg/carin.png"), "corridor": ImageEnhance.Brightness(_ld("bg/corridor.png")).enhance(1.0),
       "studio_dark": tinted(_studio, 0.32, (150, 160, 200)), "studio": ImageEnhance.Brightness(_studio).enhance(1.15)}
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
    cx += math.sin(tt * 0.9) * 5 + math.sin(tt * 2.3) * 2; cy += math.sin(tt * 1.3 + 1) * 3.5
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

def studio_light(tt):
    if tt < LIGHTS: return 0.0
    u = tt - LIGHTS
    if u > 1.6: return 1.0
    fl = [0, 0.4, 0, 0.55, 0.2, 0.8, 0.5, 1.0]
    return fl[min(len(fl) - 1, int(u / 0.2))]

def bg_frame(set_, cam, d, sh, tt):
    ins = sh.get("keyins") or sh.get("lockins") or sh.get("wheelins") or sh.get("clockins")
    if set_ == "lobby":
        if d >= 0.999: return bg_crop(SRC["lobby_day"], cam, not ins)
        if d <= 0.001: return bg_crop(SRC["lobby_night"], cam, not ins)
        return Image.blend(bg_crop(SRC["lobby_night"], cam), bg_crop(SRC["lobby_day"], cam), d)
    if set_ == "stairs": return bg_crop(SRC["stairs_day"], cam, False)
    if set_ == "studio":
        L = studio_light(tt)
        if L <= 0: return bg_crop(SRC["studio_dark"], cam, not ins)
        if L >= 1: return bg_crop(SRC["studio"], cam, not ins and not sh.get("dutch"))
        return Image.blend(bg_crop(SRC["studio_dark"], cam), bg_crop(SRC["studio"], cam), L)
    return bg_crop(SRC[set_], cam, not ins)

def A_(who, pos, **kw):
    x, y, s = pos; d = dict(who=who, x=x, y=y, s=s, look=0, expr="neutral", arms="down"); d.update(kw); return d
def walk_to(a, p0, p1, win, tt, rate=8):
    k = kk(tt, *win); e = ease(k)
    a["x"], a["y"], a["s"] = lerp(p0[0], p1[0], e), lerp(p0[1], p1[1], e), lerp(p0[2], p1[2], e)
    if 0 < k < 1: a["walk"] = tt * rate
    return k

OFF = {"tota": 0.0, "shatta": 0.4, "zalata": 0.8}
def kid(who, set_, tt):
    a = A_(who, LB[who], look=-1)
    if who == "zalata": a["held"] = "nbpen"; a["arms"] = "hold"; a["expr"] = "flat"
    off = OFF[who]
    if set_ == "lobby":
        if tt < KIN[0]: return None
        st0 = KIN[0] + off * 0.8
        if tt < st0: return None
        walk_to(a, (STB[0] + 40, STB[1], STB[2]), LB[who], (st0, KIN[1] - (0.1 if who == "shatta" else 0.4)), tt, 8)
        a["look"] = -1
        if tt >= T("F05"): a["look"] = -1 if who == "shatta" else -1
        if who == "shatta" and T("F05") <= tt < T("F05") + 1.0: a["expr"] = "shock"; a["arms"] = "up"
        if who == "tota" and tt >= PICKUP: a["held"] = "keys"; a["arms"] = "hold"
        if tt >= T("F06"): a["look"] = 1 if who == "shatta" else (-1 if who == "zalata" else 1)
        if tt >= T("F10"):
            a["look"] = 1 if who == "shatta" else -1
            if who == "shatta": a["expr"] = "smug"
        if tt >= SNZ: a["expr"] = "flat" if who == "zalata" else "neutral"
        if tt >= WBD[0]:
            p0 = LB[who]; walk_to(a, p0, BD[who], (WBD[0] + off * 0.2, WBD[1] - 0.2), tt, 8); a["look"] = 1
        if tt >= DOPEN: a["expr"] = "scared" if who != "zalata" else "flat"
        return a
    if set_ == "corridor":
        a["held"] = "phone" if who != "zalata" else "nbpen"
        if who == "zalata": a["held"] = "phone"
        a["arms"] = "hold"; a["look"] = 1; a["expr"] = "scared" if who == "shatta" else "flat"
        st0 = CDESC[0] + off * 0.5
        if tt < st0: return None
        walk_to(a, CSTAIR, CW[who], (st0, CDESC[1] + 0.2), tt, 7)
        if tt >= CWALK[0]:
            mid = (lerp(CW[who][0], CV[who][0], 0.45), lerp(CW[who][1], CV[who][1], 0.45), lerp(CW[who][2], CV[who][2], 0.45))
            walk_to(a, CW[who], mid, (CWALK[0], MOUSE), tt, 6)
            if tt >= CW2[0]:
                walk_to(a, mid, CV[who], CW2, tt, 6)
        if BEHIND <= tt < CW2[0]: a["look"] = -1; a["expr"] = "scared" if who != "zalata" else "shock"
        if JUMPIN <= tt < BEHIND:
            if who == "shatta":
                z_ = kid("zalata", set_, tt)
                a["x"] = z_["x"] + 25; a["y"] = z_["y"] - 120 * ease(kk(tt, JUMPIN, JUMPIN + 0.25)); a["s"] = z_["s"]
                a["arms"] = "up"; a["expr"] = "scared"; a["held"] = None
            if who == "zalata": a["expr"] = "flat"; a["arms"] = "up"; a["held"] = None
        if tt >= T("F17"): a["expr"] = "shock" if who == "tota" else a["expr"]
        if WHEEL[0] <= tt < VOPEN and who != "tota":
            a["arms"] = "up"; a["held"] = None; a["expr"] = "angry" if who == "zalata" else "scared"
        if tt >= VOPEN + 0.6:
            vt = (VAULT[0] + {"tota": 40, "shatta": 0, "zalata": -40}[who], 700, 0.8)
            k = walk_to(a, CV[who], vt, (VOPEN + 0.6 + off * 0.2, VOPEN + 2.0), tt, 6)
            if k >= 1: return None
        return a
    if set_ == "studio":
        a["held"] = "phone"; a["arms"] = "hold"; a["look"] = 1; a["expr"] = "scared" if who == "shatta" else "flat"
        st0 = SIN[0] + off * 0.5
        if tt < st0: return None
        p0 = (-150, 1030, 2.0)
        if who == "tota":
            k = walk_to(a, p0, (300, 1000, 1.95), (st0, SIN[1] + 0.2), tt, 6)
            if tt >= LIGHTS - 0.4: a["arms"] = "point"; a["held"] = None; a["look"] = -1
            if tt >= LIGHTS + 0.4: a["look"] = 1; a["arms"] = "down"; a["expr"] = "shock"
        else:
            walk_to(a, p0, ST[who], (st0, SIN[1] + 0.4), tt, 6)
        if tt >= LIGHTS + 0.3:
            a["held"] = None if who != "zalata" else "nbpen"; a["arms"] = "down" if who != "zalata" else "hold"
            a["expr"] = "shock" if who != "zalata" else "happy"
        if tt >= T("F21"): a["expr"] = "neutral" if who != "zalata" else "flat"
        if tt >= T("F23"): a["look"] = 1; a["expr"] = "neutral"
        if tt >= TAPE: a["look"] = -1; a["expr"] = "scared" if who != "zalata" else "shock"
        if tt >= SHEETMOVE: a["look"] = 1; a["expr"] = "scared"; a["arms"] = "scared" if who == "shatta" else a["arms"]
        return a
    return None

def actors(set_, tt, sh):
    A = []
    if sh.get("keyins") or sh.get("lockins") or sh.get("wheelins") or sh.get("clockins") or sh.get("scan"): return A
    if set_ == "stairs":
        for who in KIDS:
            d0 = OFF[who] * 0.8
            a = A_(who, (1150, 330, 0.6), look=0, expr="neutral" if who != "zalata" else "flat")
            xo = {"tota": 0, "shatta": -70, "zalata": 70}[who]
            k = walk_to(a, (1170 + xo * 0.3, 330, 0.55), (1150 + xo, 1020, 1.9), (DESC[0] + d0, DESC[0] + d0 + 2.4), tt, 7)
            if who == "zalata": a["held"] = "nbpen"; a["arms"] = "hold"
            if tt >= DESC[0] + d0 and k < 1: A.append(a)
        return A
    if set_ == "carin":
        pa = A_("pasha", CAR_P, look=-1, expr="smug" if tt >= T("F04") else "flat")
        A.append(pa)
        ab = A_("abdo", CAR_A, look=1, expr="scared")
        walk_to(ab, (-250, 900, 2.4), CAR_A, ADIVE, tt, 9)
        A.append(ab)
        return A
    if set_ == "lobby":
        if tt < TITLE:
            ab = A_("abdo", AB_N, look=1, expr="scared", held="keys", arms="hold")
            if tt >= STEP1: ab["expr"] = "shock"
            if tt >= RUNA[0]:
                ab["held"] = None if tt >= KEYFLY else "keys"; ab["arms"] = "scared"; ab["look"] = -1
                k = walk_to(ab, AB_N, (ENTR[0], ENTR[1], 0.75), RUNA, tt, 12)
                if k >= 1: ab = None
            if ab and tt < KINS[0]: A.append(ab)
            return A
        for who in KIDS:
            a = kid(who, set_, tt)
            if a: A.append(a)
        b = A_("bondo2", BENCH, look=1, expr="sleepy", lean=-0.25)
        A.append(b)
        return A
    for who in KIDS:
        a = kid(who, set_, tt)
        if a: A.append(a)
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
        if a.get("held") == "phone" and (set_ == "corridor" and tt >= FLASH or set_ == "studio" and studio_light(tt) < 1):
            lk = 1 if a.get("look", 0) >= 0 else -1
            lights.append((hand[0] + lk * 40 * S, hand[1] - 10 * S, 170 * z * a["s"] / 1.6, 1.7, (1.0, 0.98, 0.9)))
            lights.append((hand[0] + lk * 260 * S, hand[1] + 40 * S, 360 * z * a["s"] / 1.6, 1.2, (1.0, 0.97, 0.88)))
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
    warm = np.array([1.05, 0.95, 0.8], np.float32); cool = np.array([0.75, 0.85, 1.1], np.float32)
    if set_ == "lobby":
        m = np.full((LH, LW, 3), 0.44, np.float32) * cool
        X, Y = W3(809, 380); m += 0.35 * glow(X, Y, 380 * z)[..., None] * cool
        if tt < TITLE:
            r = 0.85 + 0.25 * math.sin(tt * 6) ** 2 + (0.6 if 0 <= tt - STEP1 < 0.5 else 0)
            X, Y = W3(1690, 965); m += 1.2 * r * glow(X, Y, 280 * z)[..., None] * RED
    elif set_ == "corridor":
        m = np.full((LH, LW, 3), 0.3 if tt < FLASH else 0.4, np.float32) * cool
        X, Y = W3(120, 120); m += 0.5 * glow(X, Y, 420 * z)[..., None] * cool
        if tt >= VOPEN:
            X, Y = W3(*VAULT); m += 1.1 * kk(tt, VOPEN, VOPEN + 1.5) * glow(X, Y, 260 * z)[..., None] * warm
    elif set_ == "studio":
        L = studio_light(tt)
        m = np.full((LH, LW, 3), 0.38 + 0.62 * L, np.float32)
        if sh.get("scan"):
            u = kk(tt, sh["start"], sh["end"])
            m += 1.6 * glow(W / 2 + math.sin(u * 3) * 260, H / 2 + 40, 380)[..., None] * warm
        if L >= 1: return None
    else:
        return None
    for X, Y, R, inten, col in lights:
        m += inten * glow(X, Y, R)[..., None] * np.array(col, np.float32)
    lm = np.clip(m / 1.4, 0, 1)
    if set_ == "lobby": lm = lm * (1 - d) + d
    return Image.fromarray((lm * 255).astype(np.uint8), "RGB").resize((W, H), Image.BILINEAR)

def sparkle(d, X, Y, r, a):
    col = (255, 250, 220, a)
    d.polygon([(X, Y - r), (X + r * 0.22, Y - r * 0.22), (X + r, Y), (X + r * 0.22, Y + r * 0.22), (X, Y + r),
               (X - r * 0.22, Y + r * 0.22), (X - r, Y), (X - r * 0.22, Y - r * 0.22)], fill=col)

def keyring(d, X, Y, S, rot=0.0, lw=None):
    lw = lw or max(1, int(3 * S))
    d.ellipse([X - 9 * S, Y - 9 * S, X + 9 * S, Y + 9 * S], outline=(225, 185, 60, 255), width=lw)
    for ang in (-0.6, 0.0, 0.7):
        a = ang + rot
        d.line([(X + math.sin(a) * 8 * S, Y + math.cos(a) * 8 * S), (X + math.sin(a) * 26 * S, Y + math.cos(a) * 26 * S)], fill=(225, 185, 60, 255), width=lw)
        ex, ey = X + math.sin(a) * 26 * S, Y + math.cos(a) * 26 * S
        d.rectangle([ex - 3 * S, ey - 3 * S, ex + 3 * S, ey + 3 * S], fill=(225, 185, 60, 255))

def key_pos(tt):
    """flying keys after Abdo drops them → land and slide to KEYSPOT"""
    u = kk(tt, KEYFLY, KEYFLY + 0.6)
    ab = (lerp(AB_N[0], 600, 0.3), AB_N[1] - 160)
    if u < 1:
        x = lerp(ab[0], KEYSPOT[0] - 40, u); y = lerp(ab[1], KEYSPOT[1], u) - math.sin(u * math.pi) * 120
        return x, y, u * 9
    v = kk(tt, KEYFLY + 0.6, KEYFLY + 1.0)
    return lerp(KEYSPOT[0] - 40, KEYSPOT[0], ease(v)), KEYSPOT[1] - abs(math.sin(v * math.pi * 2)) * 20 * (1 - v), 9 + v * 2

def props(img, set_, tt, cam, sh, d_):
    x0, y0, z = cam; S = SS * z; d = ImageDraw.Draw(img, "RGBA")
    W2 = lambda wx, wy: ((wx - x0) * S, (wy - y0) * S)
    lw = lambda v: max(1, int(v * S))
    if set_ == "lobby":
        # basement door opening
        if tt >= DOPEN:
            k = ease(kk(tt, DOPEN, DOPEN + 1.2))
            a0 = W2(DOOR[0], DOOR[1]); a1 = W2(DOOR[2], DOOR[3])
            d.rectangle([a0[0], a0[1], lerp(a0[0], a1[0], k * 0.85), a1[1]], fill=(6, 6, 8, 255))
            for i in range(22):
                u = ((tt - DOPEN) * 0.6 + i / 22) % 1
                if tt - DOPEN > 0.3:
                    px = lerp(DOOR[0] + 60, DOOR[0] - 260, u) + math.sin(i * 3.1) * 40; py = DOOR[1] + 60 + (i * 37) % 380
                    X, Y = W2(px, py); d.ellipse([X - 3 * S, Y - 3 * S, X + 3 * S, Y + 3 * S], fill=(210, 200, 180, int(120 * (1 - u))))
        # padlock (until unlocked → falls)
        if tt < UNLOCK + 1.6:
            lx, ly = W2(*LOCK); S1 = S * 1.35
            fall = 0
            if tt >= UNLOCK + 0.5: fall = (ease(kk(tt, UNLOCK + 0.5, UNLOCK + 0.9))) * 230 * S
            if tt < DOPEN:
                op = 10 * S1 if tt >= UNLOCK + 0.25 else 0
                d.arc([lx - 14 * S1, ly - 34 * S1 - op + fall, lx + 14 * S1, ly - 6 * S1 - op + fall], 180, 360, fill=(200, 200, 210, 255), width=max(1, int(5 * S1)))
                d.rounded_rectangle([lx - 22 * S1, ly - 8 * S1 + fall, lx + 22 * S1, ly + 28 * S1 + fall], int(5 * S1), fill=(235, 185, 50, 255), outline=(110, 75, 10, 255), width=max(1, int(2.5 * S1)))
                d.ellipse([lx - 4 * S1, ly + 4 * S1 + fall, lx + 4 * S1, ly + 12 * S1 + fall], fill=(60, 40, 10, 255))
        # key in the lock (insert)
        if sh.get("lockins") and tt < UNLOCK + 0.5:
            lx, ly = W2(*LOCK); S1 = S * 1.35
            u = ease(kk(tt, sh["start"], UNLOCK - 0.05)); rot = ease(kk(tt, UNLOCK, UNLOCK + 0.25)) * 1.4
            kx = lx + lerp(-160, 0, u) * S1 / 1.35 * 1.35; ky = ly + 8 * S1
            d.line([(kx - 120 * S1, ky + 90 * S1), (kx - 30 * S1, ky + 10 * S1)], fill=(22, 22, 22, 255), width=max(1, int(8 * S1)))
            d.ellipse([kx - 44 * S1, ky - 6 * S1, kx - 16 * S1, ky + 22 * S1], fill=(255, 255, 255, 255), outline=(22, 22, 22, 255), width=max(1, int(3 * S1)))
            keyring(d, kx - 10 * S1, ky + 4 * S1, S1 * 0.9, 1.57 + rot)
        # vent
        V = (1402, 812, 1512, 872); a0 = W2(V[0], V[1]); a1 = W2(V[2], V[3])
        d.rectangle([a0[0], a0[1], a1[0], a1[1]], fill=(25, 22, 20, 255), outline=(95, 88, 78, 255), width=lw(4))
        for i in range(1, 7):
            xx_ = a0[0] + (a1[0] - a0[0]) * i / 7
            d.line([(xx_, a0[1] + 3 * S), (xx_, a1[1] - 3 * S)], fill=(110, 102, 90, 255), width=lw(3))
        # the street-door leaf (closed during the day / after Abdo leaves)
        l0 = W2(754, 180); l1 = W2(864, 600)
        op = 1 - ease(kk(tt, RUNA[1] - 0.4, RUNA[1] + 0.3)) if tt < TITLE and tt >= RUNA[1] - 1.2 else (0 if tt >= TITLE or tt < 0 else 0)
        if tt < TITLE and RUNA[0] <= tt < RUNA[1] + 0.3: op = 1 - ease(kk(tt, RUNA[1] - 0.2, RUNA[1] + 0.3))
        wdt = (l1[0] - l0[0]) * (1 - op)
        if wdt > 1:
            d.rectangle([l0[0], l0[1], l0[0] + wdt, l1[1]], fill=(48, 36, 26, 255), outline=(20, 14, 10, 255), width=lw(3))
            gx0 = l0[0] + wdt * 0.2; gx1 = l0[0] + wdt * 0.8
            d.rectangle([gx0, l0[1] + 20 * S, gx1, l0[1] + (l1[1] - l0[1]) * 0.45], fill=(255, 225, 160, 150) if d_ > 0.3 else (60, 70, 110, 160))
        # keys: flying / on the floor until Tota picks them up
        if KEYFLY <= tt < TITLE or TITLE <= tt < PICKUP:
            if tt < TITLE:
                if sh.get("keyins"):
                    v = kk(tt, KINS[0], KINS[1]) ; kx_ = lerp(KEYSPOT[0] - 70, KEYSPOT[0], ease(v)); ky_ = KEYSPOT[1] - abs(math.sin(v * math.pi * 3)) * 45 * (1 - v)
                    X, Y = W2(kx_, ky_); keyring(d, X, Y, S, v * 7)
                elif tt < KINS[0]:
                    kx_, ky_, r_ = key_pos(tt); X, Y = W2(kx_, ky_); keyring(d, X, Y, S, r_)
            else:
                X, Y = W2(*KEYSPOT); keyring(d, X, Y, S, 1.57)
                if TLM[1] - 1.0 <= tt < TLM[1] + 0.2 or T("F05") + 0.4 <= tt < T("F05") + 1.2:
                    sparkle(d, X + 10 * S, Y - 10 * S, (8 + 14 * abs(math.sin(tt * 5))) * S, 230)
    elif set_ == "corridor":
        vx, vy = W2(*VAULT)
        R = 84 * S
        if tt < VOPEN:
            rot = 0.0
            if WHEEL[0] <= tt: rot = (tt - WHEEL[0]) * 1.6 * (0.3 if tt < WHEEL[0] + 0.8 else 1)
            for i in range(8):
                a = rot + i * math.pi / 4
                d.line([(vx, vy), (vx + math.cos(a) * R, vy + math.sin(a) * R)], fill=(70, 66, 62, 255), width=lw(9))
            d.ellipse([vx - R, vy - R, vx + R, vy + R], outline=(80, 74, 68, 255), width=lw(10))
            d.ellipse([vx - 16 * S, vy - 16 * S, vx + 16 * S, vy + 16 * S], fill=(60, 56, 52, 255))
        else:
            k = ease(kk(tt, VOPEN, VOPEN + 1.2)); RR = 190 * S
            d.ellipse([vx - RR * k, vy - RR, vx + RR * k, vy + RR], fill=(60, 40, 22, 255))
        if MOUSE - 0.2 <= tt < MOUSE + 1.2:
            u = kk(tt, MOUSE - 0.2, MOUSE + 1.2); mx = lerp(1500, 150, u); my = 930
            X, Y = W2(mx, my); s_ = 1.0 * S
            d.ellipse([X - 22 * s_, Y - 12 * s_, X + 22 * s_, Y + 12 * s_], fill=(110, 105, 100, 255), outline=(30, 30, 30, 255), width=lw(2))
            d.ellipse([X - 34 * s_, Y - 10 * s_, X - 16 * s_, Y + 6 * s_], fill=(110, 105, 100, 255), outline=(30, 30, 30, 255), width=lw(2))
            d.line([(X + 22 * s_, Y), (X + 50 * s_, Y - 8 * s_ * math.sin(tt * 30))], fill=(60, 50, 50, 255), width=lw(2))
            d.ellipse([X - 30 * s_, Y - 6 * s_, X - 26 * s_, Y - 2 * s_], fill=(0, 0, 0, 255))
    elif set_ == "studio":
        if tt >= TAPE:
            for (rx, ry) in REELS:
                X, Y = W2(rx, ry); R = 30 * S; rot = (tt - TAPE) * 6
                for i in range(3):
                    a = rot + i * 2 * math.pi / 3
                    d.line([(X, Y), (X + math.cos(a) * R * 0.85, Y + math.sin(a) * R * 0.85)], fill=(30, 30, 30, 230), width=lw(4))
                d.ellipse([X - 5 * S, Y - 5 * S, X + 5 * S, Y + 5 * S], fill=(200, 200, 200, 255))
            X, Y = W2(610, 435)
            if int(tt * 3) % 2: d.ellipse([X - 4 * S, Y - 4 * S, X + 4 * S, Y + 4 * S], fill=(255, 60, 40, 255))
        if tt >= EYES:
            on = ease(kk(tt, EYES, EYES + 0.3)) * (0.8 + 0.2 * math.sin(tt * 9))
            for ex in (SHEET[0] - 26, SHEET[0] + 26):
                X, Y = W2(ex, SHEET[1])
                for r_, a_ in ((34, 50), (20, 110), (9, 255)):
                    d.ellipse([X - r_ * S, Y - r_ * 0.7 * S, X + r_ * S, Y + r_ * 0.7 * S], fill=(255, 40, 30, int(a_ * on)))

def sheet_wobble(img, tt, cam):
    if tt < SHEETMOVE: return
    x0, y0, z = cam; S = SS * z
    box = [int((1600 - x0) * S), int((170 - y0) * S), int((1900 - x0) * S), int((740 - y0) * S)]
    box = [max(0, box[0]), max(0, box[1]), min(img.size[0], box[2]), min(img.size[1], box[3])]
    if box[2] - box[0] < 4 or box[3] - box[1] < 4: return
    u = tt - SHEETMOVE
    dx = int(math.sin(u * 13) * 6 * S * min(1, u)); dy = int(abs(math.sin(u * 7)) * -4 * S)
    part = img.crop(box); img.paste(part, (box[0] + dx, box[1] + dy))

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
        text(fr, W / 2, H / 2 - 130, "الحلقة 5 بكرة: صفيح", 100, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 + 10, "مين اللي تحت الملاية؟ اكتبوا توقعكم", 58, g((235, 235, 235)))
        text(fr, W / 2, H / 2 + 110, "اعمل اشتراك عشان ما يفوتكش", 46, g((200, 200, 200)))
    return fr

def hud(fr, tt, v=False):
    sc = 0.85 if v else 1.0; cx = 540 if v else W / 2
    if T("F08") + 2.2 <= tt < T("F08") + DUR["F08"] + 1.2:
        d = ImageDraw.Draw(fr, "RGBA"); y = 1700 if v else 120
        d.rounded_rectangle([cx - 430 * sc, y - 50 * sc, cx + 430 * sc, y + 50 * sc], int(22 * sc), fill=(20, 60, 30, 220), outline=(120, 230, 120, 255), width=4)
        text(fr, cx, y, "إجابة امبارح: أستاذ فهمي ✓", int(42 * sc), (200, 255, 200))
    if T("F11") <= tt < T("F11") + DUR["F11"] + 0.3:
        d = ImageDraw.Draw(fr, "RGBA"); y = 1700 if v else 120
        d.rounded_rectangle([cx - 160 * sc, y - 50 * sc, cx + 160 * sc, y + 50 * sc], int(22 * sc), fill=(60, 20, 20, 220), outline=(255, 120, 90, 255), width=4)
        ltr(fr, cx, y, "94%", int(56 * sc), (255, 160, 120))
def ltr(img, x, y, s, size, fill, stroke=(10, 10, 10), sw=3):
    ImageDraw.Draw(img).text((x, y), s, font=ImageFont.truetype(FONT, size), fill=fill, anchor="mm", direction="ltr", stroke_width=sw, stroke_fill=stroke)

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
        text(bgv, 540, 1695, "لغز النهارده: الساعة واقفة على كام... وليه؟", 44, (255, 214, 90))
        text(bgv, 540, 1758, "اكتب في الكومنتات", 42)
    return bgv

def finish(fr, tt, dark=False):
    fr = ImageChops.multiply(fr, VIG_DARK if dark else VIG)
    a = np.asarray(fr, np.float32)
    g = GRAIN[int(tt * FPS) % len(GRAIN)]
    g = np.repeat(np.repeat(g, 2, 0), 2, 1)[..., None]
    return Image.fromarray(np.clip(a + g, 0, 255).astype(np.uint8))

TINT = {"carin": (150, 160, 200), "corridor": (120, 135, 175), "stairs": (255, 240, 215)}
def frame(tt):
    sh = shot_at(tt); set_ = sh["set"]
    if set_ in ("title", "endcard"): return finish(card(set_, tt, sh), tt)
    if set_ == "black": return Image.new("RGB", (W, H), (0, 0, 0))
    cam = cam_at(sh, tt)
    d = tod(sh, tt) if set_ == "lobby" else 1
    img = bg_frame(set_, cam, d, sh, tt)
    if set_ == "studio": sheet_wobble(img, tt, cam)
    props(img, set_, tt, cam, sh, d)
    layer, lights = draw_scene_chars(set_, tt, cam, sh)
    if set_ == "lobby":
        tint = tuple(int(lerp(a, b, d)) for a, b in zip((165, 180, 235), (255, 246, 228)))
    elif set_ == "studio":
        L = studio_light(tt); tint = tuple(int(lerp(a, b, L)) for a, b in zip((95, 100, 130), (255, 232, 200)))
    else: tint = TINT.get(set_, (255, 244, 225))
    layer = tint_layer(layer, tint, 0.97)
    img.paste(layer, (0, 0), layer)
    if set_ == "carin":   # the seat cushion hides the hips/legs → they sit
        x0, y0, z = cam; ys = int((870 - y0) * z * SS)
        if ys < SSH:
            bgc = bg_crop(SRC["carin"], cam, True)
            img.paste(bgc.crop((0, ys, SSW, SSH)), (0, ys))
        if tt >= DRIVE:   # street lights passing over the car
            u = ((tt - DRIVE) * 0.9) % 1
            ov = Image.new("RGBA", img.size, (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
            xs = lerp(-0.3, 1.3, u) * SSW
            od.polygon([(xs, 0), (xs + 300 * SS, 0), (xs + 100 * SS, SSH), (xs - 200 * SS, SSH)], fill=(255, 170, 80, 50))
            img.paste(ov, (0, 0), ov)
    fr = img.resize((W, H), Image.LANCZOS)
    if sh.get("dutch"):
        fr = fr.rotate(7, resample=Image.BICUBIC).crop((80, 45, W - 80, H - 45)).resize((W, H), Image.LANCZOS)
    if set_ == "studio" and studio_light(tt) < 1:
        m = np.zeros((LH, LW), np.float32)
        for X, Y, R, inten, col in lights: m += inten * 0.6 * glow(X, Y, R)
        if sh.get("scan"):
            u = kk(tt, sh["start"], sh["end"]); m += 1.0 * glow(W / 2 + math.sin(u * 3) * 260, H / 2 + 40, 420)
        mask = Image.fromarray((np.clip(m, 0, 1) * 255).astype(np.uint8), "L").resize((W, H), Image.BILINEAR)
        L = studio_light(tt)
        fr = Image.composite(ImageEnhance.Brightness(fr).enhance(3.0), fr, mask)
        if L > 0: fr = ImageEnhance.Brightness(fr).enhance(1 + 0.0 * L)
        return finish(fr, tt, True)
    lm = light_map(set_, sh, tt, cam, lights, d)
    dark = False
    if lm is not None:
        fr = ImageChops.multiply(fr, lm)
        if set_ == "lobby": fr = ImageEnhance.Brightness(fr).enhance(lerp(1.7, 1.0, d)); dark = d < 0.5
        else: fr = ImageEnhance.Brightness(fr).enhance(1.6); dark = True
    if set_ == "carin": dark = True
    return finish(fr, tt, dark)

def build_audio(path="mix.wav"):
    buf = np.zeros(int(TOTAL * SR) + SR * 3, dtype=np.float32)
    dr = drone(TOTAL + 1); env = np.zeros(len(dr), np.float32)
    for a_, b_ in ((0, TITLE), (T("F13"), LIGHTS), (TAPE, TOTAL)):
        env[int(a_ * SR):int(b_ * SR)] = 1.0
    env = np.convolve(env, np.ones(4410) / 4410, mode="same")
    mix_into(buf, dr * env, 0, 1.2)
    r = np.random.default_rng(9)
    S = {"boom": sfx_boom(), **SFXF}
    for t0, nme, g in sfx:
        if nme in S and g > 0: mix_into(buf, S[nme], t0, g)
    # rain on the car roof
    n = int((TITLE - CARIN[0]) * SR); rain = np.convolve(r.normal(0, 1, n), np.ones(3) / 3, mode="same").astype(np.float32) * 0.035
    mix_into(buf, rain, CARIN[0], 1.0)
    # old music faint from the tape machine after Roshdy's line
    a_ = T("F25") + DUR["F25"]; n = int((TOTAL - 4.6 - a_) * SR)
    if n > 0:
        mus = lowpass(np.resize(SFXF["music_old"], n).astype(np.float32), 1200)
        e = np.ones(n, np.float32); fi = int(0.4 * SR); e[:fi] = np.linspace(0, 1, fi); e[-fi:] = np.linspace(1, 0, fi)
        mix_into(buf, mus * e, a_, 0.35)
    # comic pizzicato: the mouse jump + «you said mouse»
    for t_, notes in ((T("F16") + 0.1, [392, 330, 262]), (T("F22") + 0.5, [523, 494, 440, 392])):
        for i, f in enumerate(notes):
            tt_ = np.arange(int(SR * 0.4)) / SR
            mix_into(buf, np.sin(2 * np.pi * f * tt_) * np.exp(-tt_ * 12) * 0.09, t_ + i * 0.22, 1.0)
    # tension string rising from the door to the vault, and under the cliff
    for a_, b_ in ((DOPEN, VOPEN), (TAPE, TOTAL - 4.6)):
        ts = np.arange(int((b_ - a_) * SR)) / SR
        rise = (np.sin(2 * np.pi * (98 + 30 * ts / ts[-1]) * ts) + 0.5 * np.sin(2 * np.pi * (147 + 45 * ts / ts[-1]) * ts)) * 0.04 * np.minimum(1, ts / 2)
        mix_into(buf, rise, a_, 1.0)
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
            text(h, W / 2, 117, "لغز النهارده: الساعة الواقفة في الاستوديو على كام... وليه؟", 38, (255, 214, 90))
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

def mux(v, out):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", v, "-i", "mix.wav", "-c:v", "copy", "-af",
                    "loudnorm=I=-15:TP=-1.5", "-c:a", "aac", "-b:a", "192k", "-shortest", out], check=True)


if __name__ == "__main__":
    print("TOTAL", round(TOTAL, 1))
    if sys.argv[1:2] == ["stills"]:
        render(None, None, [float(v) for v in sys.argv[2:]])
    elif sys.argv[1:2] == ["times"]:
        for s_ in shots: print(s_["set"], round(s_["start"], 2), round(s_["end"], 2))
        for st, k in lines: print(k, round(st, 2))
    elif sys.argv[1:2] == ["part"]:
        i, n = int(sys.argv[2]), int(sys.argv[3]); a = round(TOTAL * i / n * FPS) / FPS; b = round(TOTAL * (i + 1) / n * FPS) / FPS
        render(f"h_{i}.mp4", f"v_{i}.mp4", None, a, b)
    elif sys.argv[1:2] == ["audio"]:
        build_audio()
