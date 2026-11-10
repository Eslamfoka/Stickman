import sys, os, math, subprocess, wave
sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter, ImageFont
from engine import *

os.chdir(ROOT + "/s2e1")
SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(201)
E1 = ROOT + "/s1e1/"
SEASON = "سر البدروم"
EPT = "الحلقة 1: باب البدروم"

SUB = {
 "A01": "سامعين؟... فيه حاجة ماشية تحت الأرض!",
 "B01": "صباح الخير يا متابعين! بعد ما مسكنا أستاذ فهمي... عمارة نعناعة بقت ترند!",
 "B02": "والنهارده... فيه سر جديد. لايف!",
 "A02": "لغز امبارح: اللي خمنوا إن فهمي هو اللي ورا الخبط... برافو عليكو!",
 "A03": "بس الجواب مكتوب فيه: افتحوا البدروم... يعني اللعبة لسه ما خلصتش.",
 "A04": "يلا ننزل حالاً! ثقوا فيا المرة دي!",
 "A05": "محدش هينزل البدروم! البدروم ده مقفول من قبل ما تتولدوا.",
 "B03": "رشدي أخويا ساب العمارة من تلاتين سنة... ومن ساعتها محدش دخل البدروم.",
 "A06": "المفتاح؟ ضاع من زمان يا ولاد...",
 "B04": "يا عم... إنت كنت نايم!",
 "B05": "نايم؟! أنا واخد بالي كويس... بس عيني مغمضة.",
 "A07": "أنا صاحي أهو.",
 "A08": "بصوا... القفل ده جديد ولامع! يعني حد غيره.",
 "A09": "القفل ده جديد... على باب مقفول تلاتين سنة؟ احتمال إنه صدفة: صفر في المية.",
 "A10": "ودي علامة رجلين مين؟... دي قد الحلة!",
 "B06": "المقاس: أربعين سنتي. دي مش جزمة... دي حاجة تانية خالص.",
 "B07": "خليني أبص من خرم الباب...",
 "B08": "آآآآه!",
 "B09": "إيه يا شطة... خايف؟",
 "B10": "أنا؟! أبداً... ده النور بس اللي خضني.",
 "A11": "لغز النهارده: مين اللي غير القفل بتاع البدروم؟ اكتبوا في الكومنتات!",
 "B11": "الخطة: الساعة اتناشر، نستخبى على السلم... ونسمع بس. محدش ينزل.",
 "B12": "نسمع بس... أكيد. ثقوا فيا.",
 "A12": "الساعة اتناشر بالظبط.",
 "A13": "المزيكا دي قديمة أوي... زي بتاعة تيتا.",
 "A14": "سامعين؟... فيه خطوات... بتخوف.",
 "A15": "دي خطوات حديد!",
 "B13": "الباب... بيتحرك لوحده!",
 "A16": "إنتو بتعملوا إيه هنا؟!... الشبشب جايلكو!",
 "A17": "نعناعة... يا أختي.",
 "A18": "ده... صوت رشدي!",
 "B14": "يعني عم رشدي... جوه البدروم؟!",
}
WHO = {"A01": "shatta", "B01": "sawsan", "B02": "sawsan", "A02": "tota", "A03": "zalata", "A04": "shatta", "A05": "nana", "B03": "nana",
       "A06": "bondo2", "B04": "shatta", "B05": "bondo2", "A07": "bondo2", "A08": "tota", "A09": "zalata", "A10": "shatta", "B06": "zalata",
       "B07": "shatta", "B08": "shatta", "B09": "tota", "B10": "shatta", "A11": "tota", "B11": "zalata", "B12": "shatta", "A12": "zalata",
       "A13": "zalata", "A14": "tota", "A15": "shatta", "B13": "tota", "A16": "nana", "A17": "roshdy", "A18": "nana", "B14": "shatta"}
EXPR = {"A01": "scared", "B01": "happy", "B02": [(0, "smug"), (0.6, "happy")], "A02": [(0, "smug"), (0.6, "happy")], "A03": "flat",
        "A04": "happy", "A05": "angry", "B03": "sad", "A06": "sleepy", "B04": "smug", "B05": [(0, "angry"), (0.5, "sleepy")], "A07": "shock",
        "A08": "happy", "A09": "flat", "A10": "scared", "B06": "flat", "B07": "neutral", "B08": "shock", "B09": "smug",
        "B10": [(0, "shock"), (0.4, "smug")], "A11": [(0, "neutral"), (0.6, "smug")], "B11": "flat", "B12": "smug", "A12": "flat",
        "A13": "flat", "A14": "scared", "A15": "shock", "B13": "shock", "A16": "angry", "A17": "neutral", "A18": "shock", "B14": "shock"}
ARMS = {"A01": "hold", "B01": "hold", "B02": "hold", "A02": "point", "A03": "hold", "A04": "up", "A05": "up", "B03": "talk",
        "A06": "hips", "B04": "point", "B05": "hips", "A07": "hips", "A08": "point", "A09": "hold", "A10": "scared", "B06": "hold",
        "B07": "down", "B08": "scared", "B09": "hips", "B10": "hips", "A11": "point", "B11": "talk", "B12": "hips", "A12": "hold",
        "A13": "hold", "A14": "scared", "A15": "scared", "B13": "point", "A16": "up", "A17": "down", "A18": "scared", "B14": "scared"}

def _aud(k): return load_audio("audio/A17_fx.mp3" if k == "A17" else f"audio/{k}.mp3")
AUD = {k: _aud(k) for k in SUB}
ENV = {k: envelope(v) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}
SFXF = {n: load_audio(f"sfx/{n}.mp3") for n in ("whoosh", "creak", "slam", "lock", "wind", "slipper", "switch", "steps_metal", "music_old")}

lines, sfx, shots, jumps, shakes = [], [], [], {}, []
def say(t, k): lines.append((t, k)); return t + DUR[k]
def fx(t, n, g=1.0): sfx.append((t, n, g))
def jump(w, t): jumps.setdefault(w, []).append(t)
def shot(set_, s, e, c0, c1=None, **kw):
    shots.append(dict(set=set_, start=s, end=e, c0=c0, c1=c1 or c0, **kw))
def cut(t, g=0.45): fx(t - 0.12, "whoosh", g)
def T(k): return [st for st, kk_ in lines if kk_ == k][0]
KIDS = ("shatta", "zalata", "tota")

# ---- world positions (lobby image with the basement door under the stairs) ----
DOOR = (1545, 495, 1830, 938)          # basement door box
LOCK = (1624, 702)                     # new shiny padlock
KEYH = (1722, 712)                     # keyhole
FOOT = (1450, 985)                    # metal footprint on the floor
MOR = {"bondo2": (240, 1040, 2.0), "sawsan": (470, 1040, 2.0), "nana": (700, 1040, 2.1), "tota": (950, 1040, 2.0),
       "shatta": (1160, 1040, 2.0), "zalata": (1380, 1040, 2.0)}
NANA_DOOR = (1560, 1040, 2.1)
NIT = {"zalata": (980, 1040, 2.0), "tota": (1140, 1040, 2.0), "shatta": (1300, 1040, 2.0)}
NANA_N = (760, 1040, 2.1)
ROOF = {"tota": (660, 920, 1.95), "shatta": (950, 920, 1.95), "zalata": (1250, 920, 1.95)}

def CU(who, pos, z=2.2, dx=0):
    x, y, s = pos; S = s * CH[who]["scale"]
    if who == "tota": z *= 1.3; dx -= 50
    hy = y - 190 * S
    return (x + dx, hy + H / (2 * z) - 1.45 * 46 * S - 25, z)

t = 0.0
# ===== 0. HOOK (night, the basement door) =====
HOOK = (0, 3.4)
fx(0.0, "music_old", 0.55); fx(0.2, "steps_metal", 1.0)
shot("night", 0, 3.4, (1690, 700, 1.25), (1690, 760, 1.9), hookdoor=True)
t = 3.4; cut(t, 0.5); s = t; t = say(t + 0.1, "A01") + 0.35
shot("night", s, t, CU("shatta", NIT["shatta"], 1.7), CU("shatta", NIT["shatta"], 2.5), ease="crash", hookshatta=True)
cut(t, 0.6); fx(t, "boom", 0.8); shot("title", t, t + 2.0, None); t += 2.0
HOOK_END = t
# ===== 1. morning: Sawsan live + yesterday's answer =====
shot("caption", t, t + 1.3, None, text="الصبح..."); t += 1.3
cut(t, 0.4); LIVE0 = t; s = t; t = say(t + 0.3, "B01") + 0.1
shot("door", s, t, (700, 640, 1.25), (760, 620, 1.4), live=True)
s = t; t = say(t, "B02") + 0.15
shot("door", s, t, CU("sawsan", MOR["sawsan"], 1.9), CU("sawsan", MOR["sawsan"], 2.3), live=True)
LIVE1 = t
cut(t, 0.4); s = t; A02_T = t + 0.1; t = say(A02_T, "A02") + 0.1
shot("door", s, t, CU("tota", MOR["tota"], 1.55), CU("tota", MOR["tota"], 1.75))
s = t; t = say(t, "A03") + 0.1
shot("door", s, t, CU("zalata", MOR["zalata"], 1.9), CU("zalata", MOR["zalata"], 2.2))
s = t; t = say(t, "A04") + 0.05
shot("door", s, t, CU("shatta", MOR["shatta"], 1.8), CU("shatta", MOR["shatta"], 2.2))
SH_RUN = (t, t + 0.9); NANA_IN = (t + 0.2, t + 1.0); fx(t + 0.25, "whoosh", 0.6)
shot("door", t, t + 1.2, (1250, 640, 1.2), (1400, 640, 1.3)); t += 1.2
s = t; t = say(t, "A05") + 0.1
shot("door", s, t, CU("nana", NANA_DOOR, 1.7), CU("nana", NANA_DOOR, 2.4), ease="crash")
s = t; t = say(t + 0.2, "B03") + 0.4
shot("door", s, t, CU("nana", NANA_DOOR, 2.1), CU("nana", NANA_DOOR, 2.3), sadmusic=True)
SADMUSIC = (s, t)
NANA_OUT = (t, t + 1.6)
# ===== 2. the doorman =====
cut(t, 0.45); s = t; KIDS_WALK = (t, t + 1.4); t = say(t + 0.9, "A06") + 0.1
shot("door", s, t, (560, 640, 1.3), (430, 680, 1.6))
s = t; t = say(t, "B04") + 0.05
shot("door", s, t, CU("shatta", (700, 1040, 2.0), 1.9), CU("shatta", (700, 1040, 2.0), 2.1))
s = t; t = say(t, "B05") + 0.05
shot("door", s, t, CU("bondo2", MOR["bondo2"], 1.9), CU("bondo2", MOR["bondo2"], 2.2))
s = t; A07_T = t + 0.15; t = say(A07_T, "A07") + 0.4; jump("bondo2", A07_T)
shot("door", s, t, CU("bondo2", MOR["bondo2"], 2.3), CU("bondo2", MOR["bondo2"], 2.0), ease="crash")
# ===== 3. investigation at the door =====
cut(t, 0.45); KIDS_BACK = (t, t + 1.0); s = t; t = say(t + 0.6, "A08") + 0.1
shot("door", s, s + 0.9, (1400, 640, 1.2), (1450, 640, 1.25))
shot("door", s + 0.9, t, (LOCK[0], LOCK[1] + 30, 3.6), (LOCK[0], LOCK[1] + 20, 4.4), lockcu=True); fx(s + 0.95, "sting", 0.6)
s = t; t = say(t, "A09") + 0.1
shot("door", s, t, CU("zalata", MOR["zalata"], 1.9), CU("zalata", MOR["zalata"], 2.2))
FOOT_T = t; fx(t + 0.1, "sting", 0.7)
s = t; t = say(t + 0.4, "A10") + 0.1
shot("door", s, s + 1.3, (FOOT[0], 900, 2.8), (FOOT[0], 920, 3.3), footcu=True)
shot("door", s + 1.3, t, CU("shatta", MOR["shatta"], 1.8), CU("shatta", MOR["shatta"], 2.4), ease="crash")
s = t; t = say(t, "B06") + 0.15
shot("door", s, t, (FOOT[0], 900, 3.0), (FOOT[0] + 20, 910, 3.2), footcu=True, ruler=True)
s = t; PEEK = (t, t + 0.8); t = say(t + 0.7, "B07") + 0.5
shot("door", s, t, (1640, 720, 1.6), (1690, 760, 2.4))
FLASH = t; fx(t, "sting", 1.2); fx(t, "boom", 0.6); shakes.append((t, 14))
s = t; t = say(t + 0.05, "B08") + 0.1; jump("shatta", FLASH + 0.05)
FALL = (FLASH + 0.1, FLASH + 0.6)
shot("door", s, t, (1600, 760, 1.9), (1550, 760, 1.6), ease="crash", keyflash=True)
s = t; t = say(t + 0.1, "B09") + 0.05
shot("door", s, t, CU("tota", MOR["tota"], 1.55), CU("tota", MOR["tota"], 1.7))
s = t; t = say(t, "B10") + 0.3
shot("door", s, t, (1500, 760, 1.6), (1480, 760, 1.8))
PUZ = t; s = t; t = say(t, "A11") + 0.8; PUZ_END = t
shot("door", s, t, CU("tota", MOR["tota"], 1.6), CU("tota", MOR["tota"], 1.9))
# ===== 4. roof at sunset: the plan =====
cut(t, 0.5); shot("caption", t, t + 1.3, None, text="بعد الضهر..."); t += 1.3
fx(t, "wind", 0.7); s = t; t = say(t + 0.5, "B11") + 0.2
shot("roof", s, t, (950, 640, 1.15), CU("zalata", ROOF["zalata"], 1.9))
s = t; t = say(t, "B12") + 0.5
shot("roof", s, t, CU("shatta", ROOF["shatta"], 1.9), CU("shatta", ROOF["shatta"], 2.3))
# ===== 5. midnight =====
cut(t, 0.5); CLOCK = (t, t + 2.6); TICK12 = t + 1.6
for i in range(4): fx(t + 0.3 + i * 0.4, "tock", 1.0)
fx(TICK12, "boom", 0.8)
shot("clock", t, CLOCK[1], None); t = CLOCK[1]
NIGHT0 = t; s = t; t = say(t + 0.4, "A12") + 0.3
shot("night", s, t, (1150, 640, 1.2), (1180, 650, 1.35))
MUSIC0 = t; fx(t, "music_old", 0.9)
s = t; t = say(t + 1.4, "A13") + 0.2
shot("night", s, t, CU("zalata", NIT["zalata"], 1.7), CU("zalata", NIT["zalata"], 2.1))
STEP0 = t; fx(t, "steps_metal", 1.2)
s = t; t = say(t + 1.0, "A14") + 0.1
shot("night", s, t, (1690, 720, 1.4), CU("tota", NIT["tota"], 1.7))
s = t; t = say(t, "A15") + 0.2
shot("night", s, t, CU("shatta", NIT["shatta"], 1.8), CU("shatta", NIT["shatta"], 2.5), ease="crash")
RATTLE = (t, t + 2.2); fx(t, "creak", 1.0); fx(t + 0.6, "lock", 1.0); shakes.append((t, 6))
s = t; t = say(t + 0.4, "B13") + 0.2
shot("night", s, s + 1.3, (1690, 720, 1.5), (1690, 730, 1.8), rattle=True)
shot("night", s + 1.3, t, CU("tota", NIT["tota"], 1.7), CU("tota", NIT["tota"], 1.9))
SH_GO = (t, t + 1.6); fx(t, "steps_metal", 0.5)
shot("night", t, t + 1.6, (1300, 660, 1.2), (1420, 660, 1.35)); t += 1.6
NANA_POP = t; fx(t, "slipper", 1.0); shakes.append((t, 10))
for w_ in KIDS: jump(w_, t + 0.05)
s = t; t = say(t + 0.25, "A16") + 0.3
shot("night", s, t, CU("nana", NANA_N, 1.6), CU("nana", NANA_N, 2.3), ease="crash")
KN = [t + 0.3 + d for d in (0, 0.45, 0.9)]
for k_ in KN: fx(k_, "knock", 1.5); shakes.append((k_, 9))
for w_ in KIDS + ("nana",): jump(w_, KN[0] + 0.05)
shot("night", t, KN[-1] + 0.8, (1300, 650, 1.1), (1600, 700, 1.4), knock=True); t = KN[-1] + 0.8
s = t; t = say(t + 0.3, "A17") + 0.5
shot("night", s, t, (1690, 820, 2.0), (1690, 880, 3.0), roshdy=True)
s = t; t = say(t, "A18") + 0.3
shot("night", s, t, CU("nana", NANA_N, 2.0), CU("nana", NANA_N, 2.6), ease="crash")
s = t; t = say(t, "B14") + 0.4
shot("night", s, t, CU("shatta", (1480, 1040, 2.0), 1.8), CU("shatta", (1480, 1040, 2.0), 2.7), ease="crash")
fx(t, "boom", 1.0); fx(t, "sting", 1.0); shot("black", t, t + 0.5, None); t += 0.5
NIGHT1 = t
shot("endcard", t, t + 4.0, None); t += 4.0
TOTAL = t

STEPS = []
def contacts(t0, t1, rate, g0=0.7, g1=0.7):
    n = math.ceil(t0 * rate / math.pi)
    while True:
        tc = n * math.pi / rate
        if tc >= t1: break
        if tc >= t0: STEPS.append((tc, g0 + (g1 - g0) * (tc - t0) / max(1e-3, t1 - t0)))
        n += 1
contacts(SH_RUN[0], SH_RUN[1], 10, 0.6, 0.6)
contacts(NANA_IN[0], NANA_IN[1], 8, 0.5, 0.5)
contacts(KIDS_WALK[0], KIDS_WALK[1], 8, 0.4, 0.4)
contacts(KIDS_BACK[0], KIDS_BACK[1], 8, 0.4, 0.4)
contacts(PEEK[0], PEEK[1], 6, 0.3, 0.3)
contacts(SH_GO[0], SH_GO[1], 4, 0.3, 0.45)

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
_mor = Image.open(ROOT + "/s1e10/bg/morning.png").convert("RGB")
SRCBG = {"door": _mor,
         "night": tinted(_mor, 0.9, (150, 165, 230)),
         "roof": tinted(Image.open(ROOT + "/s1e6/bg/roof_raw.png").convert("RGB"), 1.5, (255, 175, 120))}
TINT = {"door": (255, 246, 228), "night": (165, 180, 235), "roof": (255, 200, 160)}
LIT = {"door", "roof"}
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
    if sh.get("rattle"): shake = max(shake, 3)
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
    if sh.get("lockcu") or sh.get("footcu") or sh.get("hookdoor") or sh.get("roshdy"): return A
    if set_ == "door":
        for who, p_ in MOR.items():
            a = A_(who, p_, look=1 if p_[0] < 1000 else -1, expr="happy" if who in KIDS else "neutral")
            if who == "sawsan": a["held"] = "phone"; a["arms"] = "hold"; a["expr"] = "happy"
            if who == "zalata": a["held"] = "paper" if tt < KIDS_BACK[0] else "nbpen"; a["arms"] = "hold"; a["expr"] = "flat"
            if who == "bondo2":
                a["expr"] = "sleepy" if tt < A07_T else "smug"; a["look"] = 1; a["arms"] = "hips"
            if who == "nana":
                a["expr"] = "neutral"
                if tt >= NANA_IN[0]:
                    k = kk(tt, *NANA_IN); a["x"] = lerp(p_[0], NANA_DOOR[0], ease(k)); a["walk"] = tt * 9 if k < 1 else None
                    a["look"] = 1 if k < 1 else -1; a["expr"] = "angry"; a["arms"] = "up" if k >= 1 else "down"
                if tt >= T("B03"): a["expr"] = "sad"; a["arms"] = "down"
                if tt >= NANA_OUT[0]:
                    k = kk(tt, *NANA_OUT); a["x"] = lerp(NANA_DOOR[0], -250, ease(k)); a["walk"] = tt * 8 if k < 1 else None; a["look"] = -1
                if tt >= NANA_OUT[1]: continue
            if who == "shatta":
                if tt >= SH_RUN[0]:
                    k = kk(tt, *SH_RUN); a["x"] = lerp(p_[0], 1400, ease(k)); a["walk"] = tt * 11 if k < 1 else None; a["look"] = 1
                    if tt >= NANA_IN[1] - 0.2: a["expr"] = "shock"; a["arms"] = "scared"
                if tt >= T("A05"): a["x"] = 1400; a["expr"] = "scared"
            if who in KIDS and tt >= KIDS_WALK[0]:
                tgt = {"tota": 880, "shatta": 700, "zalata": 1060}[who]
                src = 1400 if who == "shatta" else p_[0]
                k = kk(tt, *KIDS_WALK); a["x"] = lerp(src, tgt, ease(k)); a["walk"] = tt * 8 if k < 1 else None; a["look"] = -1
                a["expr"] = "smug" if who == "shatta" else "happy"
                if tt >= KIDS_BACK[0]:
                    tgt2 = {"tota": 950, "shatta": 1160, "zalata": 1380}[who]
                    k = kk(tt, *KIDS_BACK); a["x"] = lerp(tgt, tgt2, ease(k)); a["walk"] = tt * 8 if k < 1 else None; a["look"] = 1
                    a["expr"] = "neutral"
            if who == "shatta" and tt >= T("A10"): a["expr"] = "scared"
            if who == "shatta" and tt >= PEEK[0]:
                k = kk(tt, *PEEK); a["x"] = lerp(1160, 1630, ease(k)); a["walk"] = tt * 6 if k < 1 else None
                a["lean"] = 0.8 * k; a["look"] = 1; a["expr"] = "neutral"
                if tt >= FLASH:
                    kf = kk(tt, *FALL); a["x"] = lerp(1630, 1480, kf); a["lean"] = lerp(0.8, -1.5, kf) if tt < FALL[1] + 0.8 else -0.2 * 0
                    a["expr"] = "shock"; a["arms"] = "scared"
                    if tt >= FALL[1] + 0.8: a["lean"] = 0; a["x"] = 1480
                if tt >= T("B10"): a["expr"] = "smug"; a["arms"] = "hips"
            if who == "tota" and tt >= T("B09"): a["look"] = 1
            pass
            A.append(a)
    elif set_ == "roof":
        for who, p_ in ROOF.items():
            a = A_(who, p_, look=1 if who != "zalata" else -1, expr="neutral")
            if who == "zalata": a["held"] = "nbpen"; a["arms"] = "hold"; a["expr"] = "flat"
            if who == "shatta" and tt >= T("B12"): a["look"] = -1; a["expr"] = "smug"
            A.append(a)
    elif set_ == "night":
        if sh.get("hookshatta"):
            A.append(A_("shatta", NIT["shatta"], look=1, expr="scared", held="torch", arms="hold"))
            return A
        for who, p_ in NIT.items():
            a = A_(who, p_, look=1, expr="scared")
            if who == "zalata": a["held"] = "torch"; a["arms"] = "hold"; a["expr"] = "flat" if tt < STEP0 else "scared"
            if who == "shatta" and tt >= SH_GO[0]:
                k = kk(tt, *SH_GO); a["x"] = lerp(p_[0], 1480, ease(k)); a["walk"] = tt * 5 if k < 1 else None; a["expr"] = "neutral"
                if tt >= NANA_POP: a["x"] = 1480; a["look"] = -1; a["expr"] = "shock"; a["arms"] = "scared"; a["walk"] = None
            if tt >= NANA_POP: a["look"] = -1; a["expr"] = "shock"
            if tt >= KN[0]: a["look"] = 1; a["expr"] = "shock"; a["arms"] = "scared"
            A.append(a)
        if tt >= NANA_POP:
            n = A_("nana", NANA_N, look=1, expr="angry", held="slipper", arms="up")
            if tt >= KN[0]: n["expr"] = "shock"; n["arms"] = "scared"; n["held"] = None
            if tt >= T("A18"): n["expr"] = "sad"
            A.append(n)
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
        if talking and not a.get("held"): arms = ARMS.get(k, arms)
        bob = abs(math.sin(a["walk"])) * 5 * a["s"] if a.get("walk") is not None else 0
        wy = a["y"] - jump_off(who, tt) - bob
        shiver = math.sin(tt * 60) * 2.5 if expr in ("scared", "shock") and who in KIDS else 0
        blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11 and expr != "sleepy"
        X = (a["x"] + shiver - x0) * z; Y = (wy - y0) * z; s = a["s"] * z
        p.ell(X, (a["y"] - y0) * z + 4 * s, 46 * s, 9 * s, (0, 0, 0, 110), None)
        draw_char(p, who, X, Y, s, expr, mouth, a.get("look", 0), blink, arms, tt, a.get("held"), a.get("lean", 0), a.get("walk"))
        S = s * CH[who]["scale"]; hx_, hy_ = HANDS.get(arms, (46, 104)); hand = (X + hx_ * S, Y - hy_ * S)
        h = a.get("held")
        if h == "torch": lights.append((hand[0], hand[1], 320 * z, 1.1, (1.0, 0.96, 0.85)))
        if h == "phone": lights.append((hand[0], hand[1] - 10 * S, 230 * max(0.5, s / 2.2), 0.9, (0.6, 0.8, 1.1)))
        if sh.get("hookshatta") and who == "shatta": lights.append((X, Y - 150 * S, 420 * z, 1.4, (1.0, 0.9, 0.7)))
    return layer, lights

def tint_layer(layer, tint, lvl):
    rgb = layer.convert("RGB"); al = layer.getchannel("A")
    c = tuple(int((v * 0.55 + 255 * 0.45) * min(1.0, lvl)) for v in tint)
    rgb = ImageChops.multiply(rgb, Image.new("RGB", rgb.size, c))
    out = rgb.convert("RGBA"); out.putalpha(al); return out

LW, LH = W // 8, H // 8
gy, gx = np.mgrid[0:LH, 0:LW] * 8.0
def glow(X, Y, R): return np.exp(-((gx - X) ** 2 + (gy - Y) ** 2) / (R * R))
RED = np.array([1.3, 0.12, 0.08], np.float32)

def red_level(tt):
    """How strong the red light under the basement door is at time tt (night only)."""
    if tt < HOOK_END: return 0.6 + 0.4 * math.sin(tt * 7) ** 2
    if tt < STEP0: return 0.0
    base = 0.25 + 0.75 * kk(tt, STEP0, STEP0 + 3)
    if RATTLE[0] <= tt < RATTLE[1]: base = 0.6 + 0.4 * (int(tt * 14) % 2)
    if tt >= KN[0]: base = 1.0
    return base * (0.75 + 0.25 * math.sin(tt * 6) ** 2)

def light_map(set_, sh, tt, cam, lights):
    x0, y0, z = cam; W3 = lambda px, py: ((px - x0) * z, (py - y0) * z)
    cool = np.array([0.75, 0.85, 1.1], np.float32)
    m = np.full((LH, LW, 3), 0.44, np.float32) * cool
    X, Y = W3(420, 120); m += 0.25 * glow(X, Y, 380 * z)[..., None] * cool       # moonlight through the entrance
    if sh.get("hookdoor"): X, Y = W3(1690, 700); m += 0.55 * glow(X, Y, 380 * z)[..., None] * cool
    r = red_level(tt)
    if r > 0:
        X, Y = W3(1690, 965); m += 1.1 * r * glow(X, Y, 260 * z)[..., None] * RED
        X, Y = W3(1690, 1040); m += 0.6 * r * glow(X, Y, 420 * z)[..., None] * RED
        if sh.get("roshdy"): X, Y = W3(1690, 940); m += 0.8 * glow(X, Y, 500 * z)[..., None] * RED
    for X, Y, R, inten, col in lights:
        m += inten * glow(X, Y, R)[..., None] * np.array(col, np.float32)
    return Image.fromarray((np.clip(m / 1.4, 0, 1) * 255).astype(np.uint8), "RGB").resize((W, H), Image.BILINEAR)

def sparkle(d, X, Y, r, a):
    col = (255, 250, 220, a)
    d.polygon([(X, Y - r), (X + r * 0.22, Y - r * 0.22), (X + r, Y), (X + r * 0.22, Y + r * 0.22), (X, Y + r),
               (X - r * 0.22, Y + r * 0.22), (X - r, Y), (X - r * 0.22, Y - r * 0.22)], fill=col)

def props(img, set_, tt, cam, sh):
    x0, y0, z = cam; S = SS * z; d = ImageDraw.Draw(img, "RGBA")
    W2 = lambda wx, wy: ((wx - x0) * S, (wy - y0) * S)
    if set_ not in ("door", "night"): return
    # door rattle: re-paste the door region with a small jitter
    if sh.get("rattle") or (RATTLE[0] <= tt < RATTLE[1]):
        a0 = W2(DOOR[0], DOOR[1]); a1 = W2(DOOR[2], DOOR[3])
        box = tuple(int(v) for v in (max(0, a0[0]), max(0, a0[1]), min(img.width, a1[0]), min(img.height, a1[1])))
        if box[2] > box[0] and box[3] > box[1]:
            reg = img.crop(box); dx = int(math.sin(tt * 55) * 5 * S); dy = int(math.sin(tt * 37) * 2 * S)
            img.paste(reg, (box[0] + dx, box[1] + dy))
    # footprint in the dust (big, square, with bolts)
    fx_, fy_ = W2(*FOOT)
    for (ox, oy) in ((-70, 0), (90, -24)):
        cx, cy = fx_ + ox * S, fy_ + oy * S
        d.rounded_rectangle([cx - 46 * S, cy - 17 * S, cx + 46 * S, cy + 17 * S], int(10 * S), fill=(48, 40, 32, 160), outline=(25, 20, 15, 220), width=max(1, int(4 * S)))
        d.rounded_rectangle([cx - 58 * S, cy - 26 * S, cx + 58 * S, cy + 26 * S], int(16 * S), outline=(230, 215, 180, 40), width=max(1, int(3 * S)))
        for bx in (-28, 0, 28):
            d.ellipse([cx + bx * S - 5 * S, cy - 5 * S, cx + bx * S + 5 * S, cy + 5 * S], fill=(30, 26, 22, 170))
    if sh.get("ruler"):
        k = kk(tt, sh["start"] + 0.2, sh["start"] + 1.2)
        L = 92 * k; cx, cy = fx_ - 70 * S, fy_ + 28 * S
        d.rectangle([cx - 46 * S, cy - 7 * S, cx - 46 * S + L * S, cy + 7 * S], fill=(240, 200, 60, 240), outline=(90, 70, 10, 255))
        for i in range(int(L // 8) + 1):
            xx_ = cx - 46 * S + i * 8 * S; d.line([(xx_, cy - 7 * S), (xx_, cy - (1 if i % 5 else -2) * S)], fill=(60, 40, 0, 255), width=max(1, int(1.5 * S)))
        if k >= 1: ImageDraw.Draw(img).text((cx, cy - 26 * S), "40cm", font=ImageFont.truetype(FONT, int(16 * S)), fill=(255, 240, 160), anchor="mm", stroke_width=max(1, int(2 * S)), stroke_fill=(20, 20, 20))
    # the new shiny padlock
    lx, ly = W2(*LOCK); S0 = S; S = S * 1.35
    d.arc([lx - 14 * S, ly - 34 * S, lx + 14 * S, ly - 6 * S], 180, 360, fill=(200, 200, 210, 255), width=max(2, int(5 * S)))
    d.line([(lx - 14 * S, ly - 20 * S), (lx - 14 * S, ly - 6 * S)], fill=(200, 200, 210, 255), width=max(2, int(5 * S)))
    d.line([(lx + 14 * S, ly - 20 * S), (lx + 14 * S, ly - 6 * S)], fill=(200, 200, 210, 255), width=max(2, int(5 * S)))
    d.rounded_rectangle([lx - 22 * S, ly - 8 * S, lx + 22 * S, ly + 28 * S], int(5 * S), fill=(235, 185, 50, 255), outline=(110, 75, 10, 255), width=max(1, int(2.5 * S)))
    d.ellipse([lx - 4 * S, ly + 4 * S, lx + 4 * S, ly + 12 * S], fill=(60, 40, 5, 255)); d.rectangle([lx - 1.5 * S, ly + 10 * S, lx + 1.5 * S, ly + 20 * S], fill=(60, 40, 5, 255))
    d.line([(lx - 16 * S, ly - 2 * S), (lx - 8 * S, ly + 20 * S)], fill=(255, 245, 200, 200), width=max(1, int(3 * S)))
    if set_ == "door":
        ph = (tt * 0.8) % 1
        if ph < 0.35 or sh.get("lockcu"): sparkle(d, lx + 14 * S, ly - 2 * S, (10 + 14 * math.sin(ph / 0.35 * math.pi)) * S, 235)
    S = S0
    # keyhole
    kx, ky = W2(*KEYH)
    d.ellipse([kx - 6 * S, ky - 6 * S, kx + 6 * S, ky + 6 * S], fill=(15, 10, 8, 255)); d.polygon([(kx - 4 * S, ky), (kx + 4 * S, ky), (kx + 6 * S, ky + 16 * S), (kx - 6 * S, ky + 16 * S)], fill=(15, 10, 8, 255))
    if set_ == "door" and FLASH <= tt < FLASH + 0.7:
        a = int(255 * (1 - kk(tt, FLASH, FLASH + 0.7)))
        for r_, aa in ((60, a // 4), (30, a // 2), (10, a)):
            d.ellipse([kx - r_ * S, ky + 6 * S - r_ * S, kx + r_ * S, ky + 6 * S + r_ * S], fill=(255, 30, 20, aa))
    # red light under the door (night)
    if set_ == "night":
        r = red_level(tt)
        if r > 0:
            a0 = W2(DOOR[0] + 20, DOOR[3] - 6); a1 = W2(DOOR[2] - 20, DOOR[3] + 4)
            d.rectangle([a0[0], a0[1], a1[0], a1[1]], fill=(255, 40, 30, int(220 * r)))
        if sh.get("roshdy") or sh.get("hookdoor"):   # the red eye seen through the keyhole
            if int(tt * 2.5) % 3 != 0:
                d.ellipse([kx - 4 * S, ky + 2 * S, kx + 4 * S, ky + 10 * S], fill=(255, 60, 40, 255))
        if sh.get("knock"):
            for k_ in KN:
                u = tt - k_
                if 0 <= u < 0.8:
                    for i in range(14):
                        px = 1580 + (i * 37) % 220; py = 520 + u * 380 + (i % 4) * 20
                        X, Y = W2(px, py); d.ellipse([X - 3 * S, Y - 3 * S, X + 3 * S, Y + 3 * S], fill=(200, 190, 170, int(220 * (1 - u / 0.8))))

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
    cx, cy, R = W / 2, H / 2 - 30, 330
    R *= 1 + 0.08 * kk(tt, sh["start"], sh["end"])
    g = Image.new("L", (W, H), 0); ImageDraw.Draw(g).ellipse([cx - R - 60, cy - R - 60, cx + R + 60, cy + R + 60], fill=90)
    fr.paste(Image.new("RGB", (W, H), (255, 80, 60) if tt >= TICK12 else (120, 140, 200)), (0, 0), g.filter(ImageFilter.GaussianBlur(40)))
    d.ellipse([cx - R, cy - R, cx + R, cy + R], fill=(235, 228, 205), outline=(60, 45, 25), width=14)
    for i in range(12):
        a = i * math.pi / 6; d.line([(cx + math.sin(a) * R * 0.82, cy - math.cos(a) * R * 0.82), (cx + math.sin(a) * R * 0.93, cy - math.cos(a) * R * 0.93)], fill=(40, 30, 20), width=10)
    mins = 59 if tt < TICK12 else 60
    am = mins / 60 * 2 * math.pi; ah = (11 + mins / 60) / 12 * 2 * math.pi
    if tt < TICK12: am += 0.02 * math.sin(tt * 30)
    d.line([(cx, cy), (cx + math.sin(ah) * R * 0.5, cy - math.cos(ah) * R * 0.5)], fill=(20, 20, 20), width=22)
    d.line([(cx, cy), (cx + math.sin(am) * R * 0.78, cy - math.cos(am) * R * 0.78)], fill=(20, 20, 20), width=12)
    d.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=(150, 30, 30))
    ltr(fr, cx, cy + R + 70, "12:00" if tt >= TICK12 else "11:59", 80, (255, 120, 90) if tt >= TICK12 else (220, 220, 230), sw=5)
    if TICK12 <= tt < TICK12 + 0.15: fr = ImageEnhance.Brightness(fr).enhance(1.8)
    return fr

def card(name, tt, sh):
    k = (tt - sh["start"]) / (sh["end"] - sh["start"])
    fr = Image.new("RGB", (W, H), (8, 8, 12))
    g = lambda c: tuple(int(v * min(1, k * 4)) for v in c)
    if name == "title":
        text(fr, W / 2, H / 2 - 110, "عمارة نعناعة", 110, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 + 20, "الموسم التاني: " + SEASON, 70, g((255, 120, 90)), (30, 5, 5), 5)
        text(fr, W / 2, H / 2 + 125, EPT, 52, g((225, 225, 225)))
    elif name == "caption":
        fr = Image.new("RGB", (W, H), (30, 22, 10))
        text(fr, W / 2, H / 2, sh["text"], 92, g((255, 225, 150)), (40, 20, 5), 5)
    elif name == "endcard":
        text(fr, W / 2, H / 2 - 130, "الحلقة 2 بكرة", 110, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 + 10, "مين اللي ماشي في البدروم؟ اكتبوا توقعكم", 58, g((235, 235, 235)))
        text(fr, W / 2, H / 2 + 110, "اعمل اشتراك عشان ما يفوتكش", 46, g((200, 200, 200)))
    elif name == "clock": return clock_card(tt, sh)
    return fr

HEARTS = rng.uniform(0, 1, (18, 3))
def live_overlay(fr, tt):
    d = ImageDraw.Draw(fr, "RGBA")
    k = kk(tt, LIVE0, LIVE1); views = int(12000 + (k ** 1.8) * 250000)
    d.rounded_rectangle([40, 40, 200, 100], 14, fill=(220, 30, 40, 235))
    ltr(fr, 120, 70, "● LIVE", 34, (255, 255, 255), sw=0)
    d.rounded_rectangle([215, 40, 470, 100], 14, fill=(0, 0, 0, 160))
    ltr(fr, 342, 70, f"{views:,}", 34, (255, 255, 255), sw=0)
    for i, (a, b, c) in enumerate(HEARTS):
        u = (tt * (0.35 + 0.3 * c) + a) % 1
        x = W - 140 + math.sin(u * 8 + i) * 40 + b * 60; y = H - 80 - u * 620
        r_ = 16 + 10 * c; al = int(255 * (1 - u))
        col = (255, 60, 90, al) if i % 3 else (255, 200, 60, al)
        d.ellipse([x - r_, y - r_, x, y], fill=col); d.ellipse([x, y - r_, x + r_, y], fill=col)
        d.polygon([(x - r_, y - r_ / 2), (x + r_, y - r_ / 2), (x, y + r_)], fill=col)
    comments = ["العمارة رجعت!", "إيه اللي في البدروم؟", "طنط سوسن ترند", "مستنيين الموسم التاني", "أنا خايف بجد"]
    n = int((tt - LIVE0) / 1.2) + 1
    for j in range(min(3, n)):
        cmt = comments[(n - 1 - j) % len(comments)]; y = H - 300 - j * 70
        d.rounded_rectangle([40, y - 28, 520, y + 28], 18, fill=(0, 0, 0, 150 - j * 30))
        text(fr, 280, y, cmt, 30, (255, 255, 255), sw=0)

def hud(fr, tt, v=False):
    sc = 0.85 if v else 1.0; cx = 540 if v else W / 2
    if A02_T + 2.2 <= tt < A02_T + DUR["A02"] + 0.6:
        d = ImageDraw.Draw(fr, "RGBA"); y = 1700 if v else 120
        d.rounded_rectangle([cx - 430 * sc, y - 50 * sc, cx + 430 * sc, y + 50 * sc], int(22 * sc), fill=(20, 60, 30, 220), outline=(120, 230, 120, 255), width=4)
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
    text(bgv, 540, 300, SEASON, 96, (255, 120, 90), (40, 10, 10), 6)
    text(bgv, 540, 425, EPT, 52, (235, 235, 235))
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
        text(bgv, 540, 1695, "لغز النهارده: مين غيّر القفل؟", 50, (255, 214, 90))
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
    if set_ in ("title", "endcard", "caption", "clock"): return finish(card(set_, tt, sh), tt)
    if set_ == "black": return Image.new("RGB", (W, H), (0, 0, 0))
    cam = cam_at(sh, tt)
    img = bg_frame(set_, cam)
    props(img, set_, tt, cam, sh)
    layer, lights = draw_scene_chars(set_, tt, cam, sh)
    layer = tint_layer(layer, TINT[set_], 0.97)
    img.paste(layer, (0, 0), layer)
    fr = img.resize((W, H), Image.LANCZOS)
    dark = set_ == "night"
    if dark:
        lm = light_map(set_, sh, tt, cam, lights)
        fr = ImageChops.multiply(fr, lm); fr = ImageEnhance.Brightness(fr).enhance(1.7)
    if set_ == "door" and FLASH <= tt < FLASH + 0.12: fr = ImageChops.multiply(fr, Image.new("RGB", fr.size, (255, 120, 110)))
    if set_ == "night" and any(0 <= tt - k_ < 0.1 for k_ in KN): fr = ImageEnhance.Brightness(fr).enhance(1.35)
    if sh.get("live") and tt >= LIVE0: live_overlay(fr, tt)
    return finish(fr, tt, dark)

def render(out_h, out_v, stills=None, t0=0.0, t1=None):
    fh = fv = None
    if not stills:
        mk = lambda w, h, o: subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}",
                                   "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "21",
                                   "-pix_fmt", "yuv420p", o], stdin=subprocess.PIPE)
        fh = mk(W, H, out_h); fv = mk(1080, 1920, out_v)
    t1 = TOTAL if t1 is None else t1
    times = stills or [i / FPS for i in range(int(t0 * FPS), int(t1 * FPS))]
    for i, tt in enumerate(times):
        base = frame(tt)
        h = base.copy(); hud(h, tt)
        if PUZ <= tt < PUZ_END:
            d = ImageDraw.Draw(h, "RGBA")
            d.rounded_rectangle([W / 2 - 600, 60, W / 2 + 600, 175], 24, fill=(20, 20, 30, 215), outline=(255, 214, 90, 255), width=4)
            text(h, W / 2, 117, "لغز النهارده: مين اللي غيّر قفل البدروم؟ اكتب في الكومنتات", 36, (255, 214, 90))
        subtitle(h, tt)
        if stills:
            h.save(f"still_h_{tt:.1f}.png"); vertical(base, tt).save(f"still_v_{tt:.1f}.png")
        else:
            fh.stdin.write(h.tobytes()); fv.stdin.write(vertical(base, tt).tobytes())
        if i % 240 == 0: print("frame", i, round(tt, 1), flush=True)
    if fh:
        fh.stdin.close(); fv.stdin.close(); fh.wait(); fv.wait()

def build_audio(path="mix.wav"):
    buf = np.zeros(int(TOTAL * SR) + SR * 3, dtype=np.float32)
    dr = drone(TOTAL + 1); env = np.zeros(len(dr), np.float32)
    for s_ in shots:
        if s_["set"] in ("night", "clock") or (s_["set"] == "black"): env[int(s_["start"] * SR):int(s_["end"] * SR)] = 1.0
        if s_["set"] == "door" and s_["start"] >= PUZ - 0.01: env[int(s_["start"] * SR):int(s_["end"] * SR)] = 0.4
    env = np.convolve(env, np.ones(4410) / 4410, mode="same")
    mix_into(buf, dr * env, 0, 1.2)
    r = np.random.default_rng(9); ts = np.arange(int(SR * 1.6)) / SR
    tk = np.arange(int(SR * 0.15)) / SR
    S = {"boom": sfx_boom(), "tick": sfx_tick() * 3, "knock": sfx_knock() * 1.3, **SFXF}
    S["tock"] = (np.sin(2 * np.pi * 900 * tk) * np.exp(-tk * 60) * 0.5 + r.normal(0, 1, len(tk)) * np.exp(-tk * 150) * 0.3)
    S["sting"] = (np.sin(2 * np.pi * (1200 + 80 * np.sin(ts * 40)) * ts) * 0.08 + np.sin(2 * np.pi * 1263 * ts) * 0.06
                  + np.sin(2 * np.pi * 55 * ts) * 0.4) * np.exp(-ts * 1.8)
    # old music: hook (short, fades) and from MUSIC0 to the end of the night (looped, fading at the knocks)
    mus = SFXF["music_old"]
    def music_bed(t0, t1, g, fade_out=0.8):
        n = int((t1 - t0) * SR); x = np.resize(mus, n).astype(np.float32)
        e = np.ones(n, np.float32); fi = int(1.2 * SR); fo = int(fade_out * SR)
        e[:fi] = np.linspace(0, 1, fi); e[-fo:] *= np.linspace(1, 0, fo)
        mix_into(buf, x * e, t0, g)
    sfx_ = [(a, b, c) for a, b, c in sfx if b != "music_old"]
    music_bed(0.0, HOOK_END - 1.6, 0.5, 1.0)
    music_bed(MUSIC0, KN[0], 0.45, 0.5)
    # metal footsteps: hook, after STEP0 (a few times), and while the door rattles
    for t0, n, g in sfx_:
        if n in S: mix_into(buf, S[n], t0, g)
    stm = SFXF["steps_metal"]
    for tt_ in (STEP0 + len(stm) / SR + 0.3,):
        if tt_ < RATTLE[0]: mix_into(buf, stm, tt_, 1.3)
    # red light hum under the night
    hum_t = np.arange(int((NIGHT1 - STEP0) * SR)) / SR
    hum = (np.sin(2 * np.pi * 60 * hum_t) + 0.5 * np.sin(2 * np.pi * 120 * hum_t)) * 0.025 * np.clip(hum_t / 3, 0, 1)
    mix_into(buf, hum, STEP0, 1.0)
    # sad music box under Nana's memory of Roshdy
    mb = [659.25, 587.33, 523.25, 493.88, 523.25, 587.33, 523.25]
    for i, f in enumerate(mb):
        tn = SADMUSIC[0] + 0.2 + i * 0.55
        tt_ = np.arange(int(SR * 1.2)) / SR
        mix_into(buf, (np.sin(2 * np.pi * f * tt_) + 0.3 * np.sin(4 * np.pi * f * tt_)) * np.exp(-tt_ * 3.5) * 0.05, tn, 1.0)
    # playful pizzicato under the comic doorman bit
    pz = [392, 440, 392, 330, 392, 523]
    for i, f in enumerate(pz):
        tt_ = np.arange(int(SR * 0.4)) / SR
        mix_into(buf, np.sin(2 * np.pi * f * tt_) * np.exp(-tt_ * 12) * 0.08, T("B05") + i * 0.35, 1.0)
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
    elif sys.argv[1:2] == ["part"]:          # render a slice: part i n  -> h_i.mp4 / v_i.mp4
        i, n = int(sys.argv[2]), int(sys.argv[3]); a = TOTAL * i / n; b = TOTAL * (i + 1) / n
        a = round(a * FPS) / FPS; b = round(b * FPS) / FPS
        render(f"h_{i}.mp4", f"v_{i}.mp4", None, a, b)
    elif sys.argv[1:2] == ["audio"]:
        build_audio()
    else:
        build_audio()
        render("h.mp4", "v.mp4")
        mux("h.mp4", "sirr_elbadroom_ep1.mp4"); mux("v.mp4", "sirr_elbadroom_ep1_vertical.mp4")
        print("done")
