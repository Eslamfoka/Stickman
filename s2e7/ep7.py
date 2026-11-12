import sys, os, math, subprocess, wave
sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter, ImageFont
from engine import *
from locations import loc

# م2 ح7 «فهمي التايب» — built from s2e6/ep6.py, Episode checklist (docs/directing.md) + fixed locations (docs/locations.md).
# New vs Ep6: found-footage phone video insert, thumps under the floor (chandelier shake + dust + a crack that runs across
# the wall + dutch tilt), the first audience VOTE, a whole-building blackout lit only by eyes, then by torch beams,
# villain heard but not seen (muffled voice behind the basement door), torch-POV corridor, empty robot spot + drag marks,
# a van leaving + the Pasha's cigar ember in the parked car.
os.chdir(ROOT + "/s2e7")
SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(707)
SEASON = "سر البدروم"
EPT = "الحلقة 7: فهمي التايب"

SUB = {
 "J01": "فهمي؟!... بعد اللي عملته فينا؟!",
 "J02": "اسمعيني بس... دقيقة واحدة!",
 "J03": "إجابة لغز امبارح: سجلوا الأغنية سنة 1958... كانت على النتيجة!",
 "J04": "بصوا الفيديو ده... اتصور امبارح بالليل.",
 "J05": "دول بيحفروا... تحت أساسات العمارة!",
 "J06": "الباشا عايز يثبت إن العمارة آيلة للسقوط... ويهدها.",
 "J07": "سامعين؟!... الحيطة بتتشرخ!",
 "J08": "العمارة دي... عمري كله.",
 "J09": "أنا مصدقه!",
 "J10": "احتمال إنه بيكدب: 70%",
 "J11": "عارف إنكم شاكين فيا... وعندكم حق.",
 "J12": "لغز النهارده: أستاذ فهمي صادق ولا كداب؟ اكتبوا: صادق... أو كداب!",
 "J13": "واسمعوا كلام توتة... اعملوا فولو، عشان تعرفوا مين كان عنده حق!",
 "J14": "ده عايز لايف!",
 "J15": "الشبشب جاهز يا سوسن.",
 "J16": "الباشا جاي النهارده... الساعة 12... عشان صفيح.",
 "J17": "الساعة 12 إلا دقيقة.",
 "J18": "أنا صاحي أهو!",
 "J19": "آآآه!... يا عم البواب خضتنا!",
 "J20": "حاضر يا باشا... بس فين النور؟",
 "J21": "ده صوت عبده!... تحت في البدروم!",
 "J22": "شغلوا الكشافات... بسرعة!",
 "J23": "باب البدروم... مفتوح!",
 "J24": "صفيح!... رد علينا!",
 "J25": "صفيح... مش موجود!",
}
WHO = {"J01": "nana", "J02": "fahmy", "J03": "tota", "J04": "fahmy", "J05": "zalata", "J06": "fahmy", "J07": "shatta",
       "J08": "nana", "J09": "shatta", "J10": "zalata", "J11": "fahmy", "J12": "tota", "J13": "tota", "J14": "sawsan",
       "J15": "nana", "J16": "fahmy", "J17": "zalata", "J18": "bondo2", "J19": "shatta", "J20": "abdo", "J21": "tota",
       "J22": "zalata", "J23": "shatta", "J24": "tota", "J25": "shatta"}
EXPR = {"J01": "angry", "J02": "scared", "J03": [(0, "neutral"), (0.6, "smug")], "J04": "flat", "J05": "shock", "J06": "flat",
        "J07": "scared", "J08": "sad", "J09": "smug", "J10": "flat", "J11": "sad", "J12": [(0, "neutral"), (0.55, "smug")],
        "J13": "smug", "J14": "happy", "J15": "angry", "J16": "flat", "J17": "scared", "J18": "flat", "J19": [(0, "shock"), (0.35, "angry")],
        "J21": "scared", "J22": "flat", "J23": "scared", "J24": "scared", "J25": "sad"}
ARMS = {"J02": "up", "J03": "point", "J06": "talk", "J07": "scared", "J09": "hips", "J11": "talk", "J12": "point", "J13": "point",
        "J16": "talk", "J17": "hold", "J19": "scared", "J21": "scared", "J23": "scared", "J25": "down"}

def _aud(k): return load_audio(f"audio/{k}.mp3")
AUD = {k: _aud(k) for k in SUB}
ENV = {k: envelope(v) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}
SFXF = {n: load_audio(ROOT + f"/s2e4/sfx/{n}.mp3") for n in ("whoosh", "creak", "slam", "switch", "clang", "stinger", "car",
                                                             "snore", "lights", "knocks", "steps_metal")}

lines, sfx, shots, jumps, shakes = [], [], [], {}, []
def say(t, k): lines.append((t, k)); return t + DUR[k]
def fx(t, n, g=1.0): sfx.append((t, n, g))
def jump(w, t): jumps.setdefault(w, []).append(t)
def shot(set_, s, e, c0, c1=None, **kw): shots.append(dict(set=set_, start=s, end=e, c0=c0, c1=c1 or c0, **kw))
def cut(t, g=0.4): fx(t - 0.12, "whoosh", g)
def T(k): return [st for st, kk_ in lines if kk_ == k][0]
KIDS = ("shatta", "zalata", "tota")

# ---------------- world ----------------
# lobby (s1e10/bg/morning.png, night grade)
ENTR = (809, 600); FDOOR = (809, 640, 0.95); BENCH = (170, 1000, 1.85); LAMP = (775, 60)
PEEK = {"tota": (1290, 905, 1.5), "shatta": (1380, 900, 1.5), "zalata": (1470, 905, 1.5)}
NSTAIR0 = (1180, 640, 1.05); NANA_H = (990, 940, 1.7)
BDOOR = (1550, 480, 1840, 960); BDC = (1695, 720)
# living room (s1e1/bg/living_1080.png)
LV = {"tota": (820, 1010, 1.9), "shatta": (1020, 1015, 1.9), "zalata": (1220, 1010, 1.9)}
NANA_L = (560, 1000, 1.9); FAH_L = (1520, 1000, 1.95); SAW_IN = (-160, 1000, 1.9); SAW_P = (150, 1000, 1.9)
CHAND = (980, 40); CRACK = (1115, 80, 1115, 380); CANDLE = (790, 480)
# studio (s2e5/bg/studio_nosheet.png, lights off)
ST = {"tota": (620, 1000, 1.95), "shatta": (860, 1010, 1.95), "zalata": (1100, 1000, 1.95)}
SAFE = (1600, 770); BULB = (1430, 905)
VAULT = (994, 506)
CAL = (1590, 340)
# street night (s2/bg/street_car.png)
EMBER = (1505, 655)

def CU(who, pos, z=2.2, dx=0, dy=0):
    x, y, s = pos
    S = s * CH[who]["scale"]
    z += 0.45
    if who == "tota": z *= 1.3; dx -= 50
    if who == "fahmy": z += 0.6
    hy = y - 190 * S
    return (x + dx, hy + H / (2 * z) - 1.45 * 46 * S - 25 - dy, z)

t = 0.0
# ===== 0. HOOK — same second as Ep6: Fahmy in the street door; Nana heard first, then comes down with the slipper =====
fx(0.0, "stinger", 0.5)
shot("lobby", 0, 1.5, (ENTR[0], ENTR[1] - 150, 2.5), (ENTR[0], ENTR[1] - 150, 2.75))
say(0.3, "J01")
NWALK = (1.2, 3.0); fx(1.25, "steps_metal", 0.0)
shot("lobby", 1.5, 3.2, (1080, 700, 1.45), (1070, 740, 1.6), low=True); t = 3.2
s = t; t = say(t + 0.1, "J02") + 0.2
shot("lobby", s, t, CU("fahmy", FDOOR, 1.7), CU("fahmy", FDOOR, 1.95))
REACT = (t, t + 1.3)
shot("lobby", t, REACT[1], (1250, 730, 1.55), (1270, 730, 1.65)); t = REACT[1]
cut(t, 0.3); TITLE = t; shot("title", t, t + 2.0, None); t += 2.0
# ===== 1. Answer of Ep6 (to camera) + the calendar =====
s = t; t = say(t + 0.1, "J03") + 0.1; ANS = s
shot("lobby", s, s + 3.4, CU("tota", PEEK["tota"], 1.9, 70), CU("tota", PEEK["tota"], 2.05, 70))
shot("flash", s + 3.4, t + 0.3, (CAL[0], CAL[1] + 20, 3.2), (CAL[0], CAL[1] + 10, 3.6), calins=True); t += 0.3
# Nana lowers the slipper, turns and goes up — Fahmy follows (backs to camera)
UP = (t, t + 3.4); fx(t + 0.4, "steps_metal", 0.4)
shot("lobby", t, UP[1], (1000, 600, 1.15), (1080, 560, 1.25)); t = UP[1]
# ===== 2. LIVING ROOM — the video =====
cut(t, 0.25); LIN = (t, t + 3.4); fx(t + 0.1, "creak", 0.7)
shot("living", t, LIN[1], (1000, 560, 1.0), (1000, 580, 1.08)); t = LIN[1]
s = t; t = say(t, "J04") + 0.2
shot("living", s, t, CU("fahmy", FAH_L, 1.6), CU("fahmy", FAH_L, 1.8))
VID = (t, t + 4.0); fx(t, "switch", 0.5)
shot("living", t, VID[1], None, vidins=True); t = VID[1]
s = t; t = say(t, "J05") + 0.2
shot("living", s, t, CU("zalata", LV["zalata"], 1.7), CU("zalata", LV["zalata"], 1.95))
s = t; t = say(t, "J06") + 0.3
shot("living", s, t, CU("fahmy", FAH_L, 1.6), CU("fahmy", FAH_L, 2.1))
# ===== 2b. THUMPS under the floor =====
TH = [t + 0.3, t + 1.15, t + 2.0]
for th in TH: fx(th, "boom", 1.0); shakes.append((th, 9))
shot("living", t, t + 1.0, (CHAND[0], CHAND[1] + 120, 2.6), (CHAND[0], CHAND[1] + 120, 2.8)); t += 1.0
shot("living", t, t + 0.9, (1000, 560, 1.05), (1000, 560, 1.05)); t += 0.9
CRK = (TH[2] + 0.05, TH[2] + 1.6); fx(CRK[0], "creak", 0.6)
shot("living", t, t + 2.0, (1115, 260, 2.2), (1115, 250, 2.5)); t += 2.0
s = t; t = say(t, "J07") + 0.2; jump("shatta", s)
shot("living", s, t, CU("shatta", LV["shatta"], 1.6), CU("shatta", LV["shatta"], 1.75), ease="crash")
s = t; t = say(t + 0.2, "J08") + 0.4
shot("living", s, t, CU("nana", NANA_L, 1.6), CU("nana", NANA_L, 2.05), dutch=-5)
# ===== 3. SPLIT — believe him or not + the VOTE + CTA =====
s = t; t = say(t, "J09") + 0.15; jump("shatta", s)
shot("living", s, t, CU("shatta", LV["shatta"], 1.7), CU("shatta", LV["shatta"], 1.8))
s = t; t = say(t, "J10") + 0.3; P70 = s
shot("living", s, t, CU("zalata", LV["zalata"], 1.7), CU("zalata", LV["zalata"], 1.85))
s = t; t = say(t, "J11") + 0.3
shot("living", s, t, CU("fahmy", FAH_L, 1.7), CU("fahmy", FAH_L, 1.95))
PUZ = t; s = t; t = say(t + 0.1, "J12") + 0.4; PUZ_END = t
shot("living", s, t, CU("tota", LV["tota"], 1.5, 0, 90), CU("tota", LV["tota"], 1.62, 0, 90))
s = t; t = say(t, "J13") + 0.4; CTA = (s, t)
shot("living", s, s + 1.6, CU("tota", LV["tota"], 1.55), CU("tota", LV["tota"], 1.65))
shot("phone", s + 1.6, t + 0.5, None); TAP = s + 1.6 + 1.8; fx(TAP, "switch", 0.9); t += 0.5
# ===== 3b. SAWSAN was listening (creak → peek, filming) =====
SWIN = (t, t + 1.8); fx(t + 0.1, "creak", 1.0)
shot("living", t, SWIN[1], (760, 600, 1.3), (620, 620, 1.4)); t = SWIN[1]
s = t; t = say(t, "J14") + 0.2
shot("living", s, t, CU("sawsan", SAW_P, 1.6), CU("sawsan", SAW_P, 1.75))
s = t; t = say(t + 0.1, "J15") + 0.2; SLIP = s
shot("living", s, t, CU("nana", NANA_L, 1.6, -40), CU("nana", NANA_L, 1.9, -40), low=True)
SOUT = (t, t + 1.7)
shot("living", t, SOUT[1], (760, 600, 1.25), (660, 600, 1.3)); t = SOUT[1]
# ===== 4. THE WARNING — Fahmy leaves (turns only his head), back to camera =====
FWALK = (t, t + 1.4)
shot("living", t, FWALK[1], (1300, 600, 1.25), (1450, 620, 1.35)); t = FWALK[1]
s = t; t = say(t + 0.1, "J16") + 0.3
shot("living", s, t, CU("fahmy", (1760, 990, 1.85), 1.6, -60), CU("fahmy", (1760, 990, 1.85), 1.95, -60))
FOUT = (t, t + 2.4); fx(t + 2.1, "slam", 0.6)
shot("living", t, FOUT[1], (1250, 580, 1.15), (1300, 580, 1.2)); t = FOUT[1]
# ===== 5. NIGHT WATCH in the lobby =====
cut(t, 0.25); LOBW = (t, t + 2.6)
shot("lobby", t, LOBW[1], (1000, 600, 1.08), (1150, 640, 1.18)); t = LOBW[1]
s = t; t = say(t, "J17") + 0.2
shot("lobby", s, t, CU("zalata", PEEK["zalata"], 1.7), CU("zalata", PEEK["zalata"], 1.85))
CLK = (t, t + 3.2); C12 = t + 2.6
shot("lobby", t, CLK[1], None, clockins=True); t = CLK[1]
# ===== 6. BLACKOUT =====
SPARK = t + 0.3; BLACK = t + 0.75; fx(SPARK, "lights", 0.9); fx(SPARK + 0.05, "clang", 0.4); fx(BLACK, "boom", 0.7)
shot("lobby", t, t + 3.0, (950, 520, 1.05), (950, 540, 1.1)); t += 3.0
s = t; t = say(t + 0.1, "J18") + 0.1; BEYES = s
fx(s, "stinger", 1.0); shakes.append((s, 10))
shot("lobby", s, t, (BENCH[0] + 60, 640, 2.4), (BENCH[0] + 60, 640, 2.8), ease="crash")
s = t; t = say(t, "J19") + 0.5; shakes.append((s, 8))
shot("lobby", s, t, (1380, 680, 1.9), (1380, 680, 2.05))
s = t; t = say(t + 0.5, "J20") + 0.4; ABDO = s
shot("lobby", s, t, (1600, 660, 1.35), (BDC[0], BDC[1], 1.85))
s = t; t = say(t, "J21") + 0.1
shot("lobby", s, t, (1290, 640, 2.4), (1290, 640, 2.55))
s = t; t = say(t, "J22") + 0.1
shot("lobby", s, t, (1470, 640, 2.4), (1470, 640, 2.5))
TORCH = [t + 0.1, t + 0.35, t + 0.6]
for tc in TORCH: fx(tc, "switch", 0.9)
shot("lobby", t, t + 1.6, (1350, 600, 1.3), (1450, 620, 1.4)); t += 1.6
DAJAR = t + 0.5; fx(DAJAR, "creak", 1.1); fx(DAJAR + 0.1, "stinger", 0.8)
shot("lobby", t, t + 2.0, (BDC[0], BDC[1], 1.6), (BDC[0], BDC[1], 1.9)); t += 2.0
s = t; t = say(t, "J23") + 0.2; jump("shatta", s)
shot("lobby", s, t, CU("shatta", PEEK["shatta"], 1.7), CU("shatta", PEEK["shatta"], 2.0))
# ===== 7. DOWN — corridor POV → studio dark → Safeeh gone =====
cut(t, 0.35); POV = (t, t + 3.0); fx(t + 0.1, "steps_metal", 0.6)
shot("corridor", t, POV[1], (VAULT[0], 560, 1.05), (VAULT[0], VAULT[1] + 10, 1.9), pov=True); t = POV[1]
SIN = (t, t + 2.4)
shot("studio", t, SIN[1], (900, 600, 1.05), (950, 600, 1.12)); t = SIN[1]
SCAN = (t, t + 2.6)
shot("studio", t, SCAN[1], (1250, 640, 1.5), (1600, 640, 1.75), scan=True); t = SCAN[1]
EMPTY = t; fx(t, "stinger", 0.9)
shot("studio", t, t + 1.8, (1600, 760, 2.3), (1600, 760, 2.6), scan=True, fixed=SAFE); t += 1.8
BULBI = (t, t + 1.6)
shot("studio", t, BULBI[1], (BULB[0], BULB[1] - 30, 3.4), (BULB[0], BULB[1] - 30, 3.8), scan=True, fixed=BULB); t = BULBI[1]
s = t; t = say(t, "J24") + 0.5
shot("studio", s, t, CU("tota", ST["tota"], 1.5), CU("tota", ST["tota"], 1.65))
s = t; t = say(t, "J25") + 0.1; VANSND = t - 0.9; fx(VANSND, "car", 1.0)
shot("studio", s, t, CU("shatta", ST["shatta"], 1.5), CU("shatta", ST["shatta"], 2.1))
VAN = (t, t + 3.0)
shot("street", t, VAN[1], (900, 600, 1.1), (1150, 620, 1.2)); t = VAN[1]
shot("street", t, t + 1.4, (EMBER[0], EMBER[1], 1.6), (EMBER[0], EMBER[1], 3.4), ease="crash"); fx(t + 0.2, "stinger", 1.0); t += 1.4
fx(t, "boom", 0.9); shakes.append((t - 0.2, 10))
shot("black", t, t + 0.5, None); t += 0.5
shot("endcard", t, t + 4.4, None); t += 4.4
TOTAL = t

STEPS = []
def contacts(t0, t1, rate, g=0.5):
    n = math.ceil(t0 * rate / math.pi)
    while True:
        tc = n * math.pi / rate
        if tc >= t1: break
        if tc >= t0: STEPS.append((tc, g))
        n += 1
for a_, b_, r_, g_ in ((NWALK[0], NWALK[1], 7, 0.5), (UP[0], UP[1], 6, 0.35), (LIN[0], LIN[1], 7, 0.35), (FWALK[0], FWALK[1], 6, 0.4),
                       (FOUT[0], FOUT[1] - 0.4, 6, 0.4), (SOUT[0], SOUT[1], 11, 0.45), (SIN[0], SIN[1], 6, 0.35)):
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

SRC = {"lobby": loc("lobby", "night"),
       "living": ImageEnhance.Brightness(loc("living", "day")).enhance(1.35),
       "corridor": loc("corridor", "day"),
       "studio": loc("studio", "day"),
       "street": loc("street", "night"),
       "flash": ImageEnhance.Brightness(loc("studio", "day")).enhance(1.7),
       "wall_n": loc("wall", "night")}
SRC["lobby"] = ImageEnhance.Brightness(SRC["lobby"]).enhance(1.45)
yy, xx = np.mgrid[0:H, 0:W]
vg = 1 - 0.55 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) ** 1.2
VIG = Image.fromarray((np.clip(vg, 0.25, 1) * 255).astype(np.uint8)).convert("RGB")
vg2 = np.clip(1 - 0.85 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2), 0.15, 1)
VIG_DARK = Image.fromarray((vg2 * 255).astype(np.uint8)).convert("RGB")
GRAIN = [np.random.default_rng(i).normal(0, 3.0, (H // 4, W // 4)).astype(np.float32) for i in range(4)]

def cam_at(sh, tt):
    k = ease((tt - sh["start"]) / max(0.01, sh["end"] - sh["start"]), sh.get("ease"))
    cx, cy, z = [a + (b - a) * k for a, b in zip(sh["c0"], sh["c1"])]
    shake = 0
    for st, amp in shakes:
        if 0 <= tt - st < 0.45: shake = max(shake, amp * (1 - (tt - st) / 0.45))
    cw, ch = W / z, H / z
    hand = 2.2 if sh.get("pov") else 1.0
    cx += (math.sin(tt * 0.9) * 5 + math.sin(tt * 2.3) * 2) * hand; cy += math.sin(tt * 1.3 + 1) * 3.5 * hand
    if sh.get("pov"): cy += abs(math.sin(tt * 6.5)) * 8   # walking bob
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

def A_(who, pos, **kw):
    x, y, s = pos; d = dict(who=who, x=x, y=y, s=s, look=0, expr="neutral", arms="down"); d.update(kw); return d
def walk_to(a, p0, p1, win, tt, rate=8):
    k = kk(tt, *win); e = ease(k)
    a["x"], a["y"], a["s"] = lerp(p0[0], p1[0], e), lerp(p0[1], p1[1], e), lerp(p0[2], p1[2], e)
    if 0 < k < 1: a["walk"] = tt * rate
    return k

OFF = {"tota": 0.0, "shatta": 0.35, "zalata": 0.7}
def lit(tt): return tt >= TORCH[0]
def dark_lobby(tt): return BLACK <= tt < TOTAL and shot_at(tt)["set"] == "lobby"

def kid(who, set_, tt):
    a = A_(who, (0, 0, 1), look=-1)
    off = OFF[who]
    if set_ == "lobby":
        if UP[0] <= tt < LIN[0]:
            # kids follow Nana up the stairs (backs)
            p0 = PEEK[who]; p1 = (1180 + 40 * off, 600, 0.95)
            k = walk_to(a, p0, p1, (UP[0] + 1.0 + off * 0.6, UP[1] + 0.3), tt, 7)
            a["back"] = k > 0.02; a["arms"] = "down"
            if who == "zalata": a["held"] = "nbpen"; a["arms"] = "hold"
            return a
        a["x"], a["y"], a["s"] = PEEK[who]
        if tt < TITLE + 0.5:
            a["look"] = -1; a["expr"] = "shock" if who != "zalata" else "flat"
            a["arms"] = "scared" if who == "shatta" else "down"
            if who == "zalata": a["held"] = "nbpen"; a["arms"] = "hold"
            return a
        if tt < UP[0]:
            a["look"] = -1; a["expr"] = "neutral" if who != "zalata" else "flat"
            if who == "zalata": a["held"] = "nbpen"; a["arms"] = "hold"
            return a
        # night watch: sitting on the stairs, looking at the basement door
        a["look"] = 1; a["expr"] = "scared" if who != "zalata" else "flat"
        if who == "zalata": a["held"] = "nbpen"; a["arms"] = "hold"
        if lit(tt):
            on = tt >= TORCH[{"tota": 0, "shatta": 1, "zalata": 2}[who]]
            a["held"] = "torch" if on else None; a["arms"] = "hold"
            if tt >= DAJAR: a["expr"] = "shock" if who != "zalata" else "scared"
        return a
    if set_ == "living":
        a["x"], a["y"], a["s"] = LV[who]
        if who == "zalata": a["held"] = "nbpen"; a["arms"] = "hold"; a["expr"] = "flat"
        if tt < LIN[1] + 0.5:
            st0 = LIN[0] + 0.6 + off * 0.7
            if tt < st0: return None
            walk_to(a, (2050, 1000, 1.95), LV[who], (st0, LIN[1] + 0.3), tt, 7)
            a["look"] = -1
            return a
        a["look"] = 1
        if VID[0] <= tt < TH[0]: a["expr"] = "shock" if who != "zalata" else "flat"
        if TH[0] <= tt < T("J09"):
            a["expr"] = "scared" if who != "zalata" else "shock"
            if who != "zalata": a["arms"] = "scared"
        if T("J09") <= tt < SWIN[0]: a["expr"] = "neutral" if who != "zalata" else "flat"
        if SWIN[0] <= tt < SLIP: a["look"] = -1; a["expr"] = "shock"
        if SLIP + DUR["J15"] * 0.5 <= tt < FWALK[0]: a["look"] = -1; a["expr"] = "happy" if who != "zalata" else "smug"
        if tt >= FWALK[0]: a["look"] = 1; a["expr"] = "neutral" if who != "zalata" else "flat"
        if tt >= T("J16"): a["expr"] = "scared" if who != "zalata" else "flat"
        return a
    if set_ == "studio":
        st0 = SIN[0] + off * 0.5
        if tt < st0: return None
        walk_to(a, (-200, 1060, 2.1), ST[who], (st0, SIN[1] + 0.3), tt, 6)
        a["look"] = 1; a["expr"] = "scared"; a["held"] = "torch"; a["arms"] = "hold"
        if tt >= EMPTY: a["expr"] = "shock"
        if tt >= T("J25"): a["expr"] = "sad"
        return a
    return None

def actors(set_, tt, sh):
    A = []
    if sh.get("calins") or sh.get("vidins") or sh.get("clockins"): return A
    if set_ == "lobby":
        # Fahmy (only until he follows Nana up)
        if tt < LIN[0]:
            f = A_("fahmy", FDOOR, look=1, expr="flat", arms="down")
            if tt < 0.4: f["look"] = -1
            if tt >= 1.0: f["arms"] = "up"; f["expr"] = "scared"
            if tt >= ANS: f["arms"] = "down"; f["expr"] = "sad"
            if tt >= UP[0] + 0.6:
                k = walk_to(f, FDOOR, (1170, 600, 0.95), (UP[0] + 0.6, UP[1] + 0.2), tt, 6)
                f["back"] = k > 0.35; f["look"] = 1
            A.append(f)
            # Nana comes down with the slipper raised
            if tt >= NWALK[0] - 0.1:
                n = A_("nana", NANA_H, look=-1, expr="angry", held="slipper", arms="up")
                walk_to(n, NSTAIR0, NANA_H, NWALK, tt, 7)
                if REACT[0] <= tt: n["swing"] = math.sin(tt * 14) * 6 if tt < REACT[1] else 0
                if tt >= ANS: n["arms"] = "hold"; n["expr"] = "flat"
                if tt >= UP[0]:
                    k = walk_to(n, NANA_H, (1180, 600, 0.95), (UP[0] + 0.2, UP[1] - 0.2), tt, 6)
                    n["back"] = k > 0.05; n["arms"] = "down"; n["held"] = "slipper"
                A.append(n)
            # doorman (holds the lantern by the door)
            b = A_("bondo2", (ENTR[0] + 110, 690, 1.05), look=-1, expr="shock", held="lantern", arms="hold")
            if tt >= ANS: b["expr"] = "flat"
            A.append(b)
        else:
            b = A_("bondo2", BENCH, look=1, expr="sleepy", lean=-0.25)
            if tt >= BEYES: b["expr"] = "flat"; b["lean"] = 0
            A.append(b)
    if set_ == "living":
        n = A_("nana", NANA_L, look=1, expr="sad", held="slipper", arms="hold")
        if tt < LIN[1] + 0.4:
            k = walk_to(n, (2050, 1000, 1.95), NANA_L, (LIN[0], LIN[1] - 0.4), tt, 7); n["look"] = -1
        if TH[0] <= tt < T("J09"): n["expr"] = "scared"
        if SWIN[0] <= tt: n["look"] = -1
        if SLIP <= tt < SOUT[1]: n["expr"] = "angry"; n["arms"] = "up"
        if tt >= SOUT[1]: n["look"] = 1; n["expr"] = "sad"; n["arms"] = "hold"
        A.append(n)
        if tt < FOUT[1]:
            f = A_("fahmy", FAH_L, look=-1, expr="flat", held="phone", arms="hold")
            if tt < LIN[1] + 0.4:
                walk_to(f, (2100, 1000, 1.95), FAH_L, (LIN[0] + 1.4, LIN[1] + 0.4), tt, 7)
            if tt >= VID[1]: f["held"] = None; f["arms"] = "down"
            if tt >= T("J11"): f["expr"] = "sad"
            if SWIN[0] <= tt < FWALK[0]: f["expr"] = "flat"
            if tt >= FWALK[0]:
                k = walk_to(f, FAH_L, (1760, 990, 1.85), FWALK, tt, 6); f["back"] = 0 < k < 1; f["look"] = 1
                if k >= 1: f["back"] = False; f["look"] = -1      # turns his head back to them
            if tt >= FOUT[0]:
                k = walk_to(f, (1760, 990, 1.85), (2150, 880, 1.45), (FOUT[0] + 0.2, FOUT[1] - 0.3), tt, 6)
                f["back"] = True; f["arms"] = "down"
            A.append(f)
        if SWIN[0] <= tt < SOUT[1]:
            sw = A_("sawsan", SAW_P, look=1, expr="happy", held="phone", arms="hold")
            walk_to(sw, SAW_IN, SAW_P, (SWIN[0] + 0.2, SWIN[0] + 1.1), tt, 6)
            if SLIP <= tt: sw["expr"] = "shock"
            if tt >= SOUT[0]:
                k = walk_to(sw, SAW_P, (-260, 980, 1.8), (SOUT[0] + 0.15, SOUT[1] - 0.2), tt, 12)
                sw["back"] = True
            A.append(sw)
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
EYES = []      # filled per frame: (X, Y, S, who) for the blackout eyes-only pass
def draw_scene_chars(set_, tt, cam, sh):
    x0, y0, z = cam
    layer = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0))
    k, lt = line_at(tt); lights = []; EYES.clear()
    acts = actors(set_, tt, sh)
    spk = None
    if k:
        for a in acts:
            if a["who"] == WHO[k]: spk = a
    for a in sorted(acts, key=lambda a: (a["s"], a["y"])):
        who = a["who"]; talking = k is not None and WHO[k] == who
        mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
        bob = abs(math.sin(a["walk"])) * 5 * a["s"] if a.get("walk") is not None else 0
        wy = a["y"] - jump_off(who, tt) - bob
        X = (a["x"] + a.get("swing", 0) - x0) * z; Y = (wy - y0) * z; s = a["s"] * z
        S = s * CH[who]["scale"]
        EYES.append((X, Y - 190 * S, S, who, a.get("expr", "neutral"), a.get("back", False)))
        p = P(layer)
        p.ell(X, (a["y"] - y0) * z + 4 * s, 46 * s, 9 * s, (0, 0, 0, 110), None)
        if a.get("back"):
            draw_back(p, who, X, Y, s, tt, a.get("walk"), a.get("arms", "down"), a.get("held"))
            if a.get("held") == "lantern": lights.append((X + 30 * s, Y - 110 * s, 150 * s, 1.2, (1.0, 0.85, 0.5)))
            continue
        expr = a.get("expr", "neutral")
        if talking: expr = expr_of(k, lt)
        arms = a.get("arms", "down")
        if talking and not a.get("held") and k in ARMS: arms = ARMS[k]
        if talking and who == "fahmy" and k == "J02": arms = "up"
        look = a.get("look", 0)
        if spk is not None and not talking and a.get("walk") is None and who not in ("bondo2",) and set_ != "studio":
            look = 1 if spk["x"] > a["x"] else -1             # listeners react: look at whoever talks
        shiver = math.sin(tt * 60) * 2.5 if expr in ("scared", "shock") and who in KIDS else 0
        blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11 and expr != "sleepy"
        draw_char(p, who, X + shiver * z, Y, s, expr, mouth, look, blink, arms, tt, a.get("held"), a.get("lean", 0), a.get("walk"))
        if who == "bondo2" and a.get("lean", 0) < 0:   # Zzz
            for i in range(3):
                u = ((tt * 0.6) + i / 3) % 1
                text(layer, (X + (40 + 30 * u + i * 6) * S) * SS, (Y - (220 + 140 * u) * S) * SS, "Z", int((26 + 18 * i) * S * SS), (255, 255, 255, int(255 * (1 - u))), sw=2)
        if who == "sawsan" and a.get("held") == "phone" and int(tt * 3) % 2:   # REC light on her phone
            hx_, hy_ = HANDS["hold"]; p.ell(X + hx_ * S + 5 * S, Y - hy_ * S - 18 * S, 3 * S, 3 * S, (255, 40, 40, 255), None)
        hx_, hy_ = HANDS.get(arms, (46, 104)); hand = (X + hx_ * S, Y - hy_ * S)
        if a.get("held") == "torch": lights.append((hand[0], hand[1], 120 * s, 1.0, (1.0, 0.95, 0.75), "torch"))
        if a.get("held") == "lantern": lights.append((hand[0], hand[1] + 30 * S, 170 * s, 1.3, (1.0, 0.85, 0.5)))
    return layer, lights

def tint_layer(layer, tint, lvl):
    rgb = layer.convert("RGB"); al = layer.getchannel("A")
    c = tuple(int((v * 0.55 + 255 * 0.45) * min(1.0, lvl)) for v in tint)
    rgb = ImageChops.multiply(rgb, Image.new("RGB", rgb.size, c))
    out = rgb.convert("RGBA"); out.putalpha(al); return out

LW, LH = W // 8, H // 8
gy, gx = np.mgrid[0:LH, 0:LW] * 8.0
def glow(X, Y, R): return np.exp(-((gx - X) ** 2 + (gy - Y) ** 2) / (R * R))
WARM = np.array([1.05, 0.95, 0.78], np.float32); COOL = np.array([0.75, 0.85, 1.1], np.float32)

def scan_pt(tt, sh):
    """where the torches point in the studio"""
    if sh.get("fixed"): return sh["fixed"][0] + math.sin(tt * 3) * 15, sh["fixed"][1] - 20 + math.sin(tt * 2.3) * 10
    if tt < SCAN[0]: return 900 + math.sin(tt * 1.7) * 250, 640
    u = ease(kk(tt, SCAN[0], SCAN[1]))
    return lerp(700, 1600, u) + math.sin(tt * 4) * 30, lerp(560, 740, u)

def light_map(set_, sh, tt, cam, lights):
    x0, y0, z = cam; W3 = lambda px, py: ((px - x0) * z, (py - y0) * z)
    torches = [l for l in lights if len(l) > 5]
    if set_ == "lobby":
        if tt < BLACK:
            m = np.full((LH, LW, 3), 0.62, np.float32) * COOL
            X, Y = W3(*LAMP); m += 0.55 * glow(X, Y, 360 * z)[..., None] * WARM
            if tt < LIN[0]:   # backlight through the open street door (continuity with Ep6)
                X, Y = W3(ENTR[0], ENTR[1] - 120); m += 1.4 * glow(X, Y, 260 * z)[..., None] * np.array([1.0, 0.95, 0.85], np.float32)
            if SPARK <= tt < BLACK:
                f = 1.6 * abs(math.sin((tt - SPARK) * 40))
                X, Y = W3(*LAMP); m += f * glow(X, Y, 300 * z)[..., None] * np.array([1.2, 1.1, 0.9], np.float32)
        else:
            m = np.full((LH, LW, 3), 0.05, np.float32) * COOL
            X, Y = W3(ENTR[0], ENTR[1] - 200); m += 0.12 * glow(X, Y, 300 * z)[..., None] * COOL   # moonlight in the door glass
            if ABDO - 0.2 <= tt < TORCH[0] + 2:   # thin light line under the basement door
                X, Y = W3(BDC[0], 955); m += (0.5 + 0.2 * math.sin(tt * 13)) * glow(X, Y, 120 * z)[..., None] * WARM
            for X, Y, R, inten, col, _ in torches:
                m += 0.9 * glow(X, Y, R * 0.6)[..., None] * WARM
                TX, TY = W3(*BDC); m += 0.9 * glow(TX + math.sin(tt * 2 + X) * 30 * z, TY + 40 * z, 230 * z)[..., None] * WARM
    elif set_ == "corridor":
        m = np.full((LH, LW, 3), 0.08, np.float32) * COOL
        u = kk(tt, POV[0], POV[1])
        m += 1.6 * glow(W / 2 + math.sin(tt * 2.1) * 120, H / 2 + 60 + math.sin(tt * 1.4) * 40, 420)[..., None] * WARM
        m += 0.5 * glow(W / 2 - 300, H / 2 + 120, 300)[..., None] * WARM
    elif set_ == "studio":
        m = np.full((LH, LW, 3), 0.09, np.float32) * COOL
        px, py = scan_pt(tt, sh); X, Y = W3(px, py)
        m += 1.7 * glow(X, Y, 260 * z)[..., None] * WARM
        for X, Y, R, inten, col, _ in torches: m += 0.7 * glow(X, Y, R * 0.6)[..., None] * WARM
        if tt >= SIN[0]:   # the robot's antenna bulb on the floor (red pulse)
            on = 1.0 if int(tt * 2.5) % 2 else 0.15
            X, Y = W3(*BULB); m += 0.9 * on * glow(X, Y, 90 * z)[..., None] * np.array([1.4, 0.2, 0.15], np.float32)
    elif set_ == "living":
        if not lights and not (TH[0] <= tt < TH[2] + 1.0): return None
        m = np.full((LH, LW, 3), 1.0, np.float32)
        for th in TH:   # the candle flame ducks with every thump
            if 0 <= tt - th < 0.5: m *= 0.8 + 0.2 * kk(tt, th, th + 0.5)
        return Image.fromarray((np.clip(m, 0, 1) * 255).astype(np.uint8), "RGB").resize((W, H), Image.BILINEAR)
    else:
        return None
    for l in lights:
        if len(l) == 5:
            X, Y, R, inten, col = l; m += inten * glow(X, Y, R)[..., None] * np.array(col, np.float32)
    lm = np.clip(m / 1.3, 0, 1)
    return Image.fromarray((lm * 255).astype(np.uint8), "RGB").resize((W, H), Image.BILINEAR)

def beams(img, set_, tt, cam, sh, lights):
    """visible torch cones (additive haze)"""
    x0, y0, z = cam; S = z; W2 = lambda wx, wy: ((wx - x0) * S, (wy - y0) * S)
    torches = [l for l in lights if len(l) > 5]
    if not torches and set_ != "corridor": return img
    hz = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(hz)
    if set_ == "corridor":
        a = (img.size[0] * 0.62, img.size[1] * 1.05); tx, ty = img.size[0] / 2 + math.sin(tt * 2.1) * 120 , img.size[1] / 2 + 60 
        d.polygon([(a[0] - 30 , a[1]), (tx - 260 , ty - 140 ), (tx + 260 , ty + 140 ), (a[0] + 30 , a[1])], fill=(255, 240, 200, 30))
    for X, Y, R, inten, col, _ in torches:
        hx, hy = X, Y
        if set_ == "lobby": tx, ty = W2(BDC[0] + math.sin(tt * 2 + X) * 30, BDC[1] + 80)
        else: tx, ty = W2(*scan_pt(tt, sh))
        dx, dy = tx - hx, ty - hy; L = max(1, math.hypot(dx, dy)); nx, ny = -dy / L, dx / L; w = 150 * S
        d.polygon([(hx + nx * 6 * S, hy + ny * 6 * S), (tx + nx * w, ty + ny * w), (tx - nx * w, ty - ny * w), (hx - nx * 6 * S, hy - ny * 6 * S)], fill=(255, 240, 200, 40))
    hz = hz.filter(ImageFilter.GaussianBlur(int(14 )))
    base = img.convert("RGBA"); base.alpha_composite(hz); return base.convert("RGB")

def props(img, set_, tt, cam, sh):
    x0, y0, z = cam; S = SS * z; d = ImageDraw.Draw(img, "RGBA")
    W2 = lambda wx, wy: ((wx - x0) * S, (wy - y0) * S)
    lw = lambda v: max(1, int(v * S))
    if set_ == "lobby":
        if tt < LIN[0]:   # open street door: fog in the doorway (continuity with Ep6)
            fog = Image.new("RGBA", img.size, (0, 0, 0, 0)); fd = ImageDraw.Draw(fog)
            for i in range(14):
                u = ((tt + 9) * 0.25 + i / 14) % 1
                X, Y = W2(ENTR[0] + math.sin(i * 2.1 + tt * 0.5) * 140, 600 - i * 18 + u * 40)
                r = (70 + 50 * u) * S
                fd.ellipse([X - r, Y - r * 0.45, X + r, Y + r * 0.45], fill=(220, 225, 235, int(28 * (1 - u))))
            fog = fog.filter(ImageFilter.GaussianBlur(int(18 * S))); img.paste(fog, (0, 0), fog)
        else:   # street door closed for the night
            l0 = W2(754, 180); l1 = W2(864, 600)
            d.rectangle([l0[0], l0[1], l1[0], l1[1]], fill=(40, 30, 22, 255), outline=(15, 10, 8, 255), width=lw(3))
        if SPARK <= tt < BLACK + 0.4:   # lamp sparks
            r_ = np.random.default_rng(int(tt * FPS))
            X, Y = W2(*LAMP)
            for _ in range(10):
                a = r_.uniform(0, math.pi); L = r_.uniform(20, 90) * S
                d.line([(X, Y + 20 * S), (X + math.cos(a) * L, Y + 20 * S + math.sin(a) * L)], fill=(255, 230, 140, 255), width=lw(3))
        if tt >= DAJAR - 2.5:   # the basement door is ajar: dark gap that widens with the creak
            g = 18 + 50 * ease(kk(tt, DAJAR, DAJAR + 0.8))
            a_ = W2(BDOOR[0] + 12, BDOOR[1] + 30); b_ = W2(BDOOR[0] + 12 + g, BDOOR[3] - 10)
            d.rectangle([a_[0], a_[1], b_[0], b_[1]], fill=(5, 4, 4, 255))
    if set_ == "living":
        # the crack runs down the wall
        u = ease(kk(tt, *CRK))
        if u > 0:
            pts = []; r_ = np.random.default_rng(77)
            for i in range(13):
                v = i / 12; pts.append((CRACK[0] + r_.uniform(-26, 26) * (0 < i < 12), lerp(CRACK[1], CRACK[3], v)))
            n = max(2, int(u * len(pts)) + 1); pts = pts[:n]
            d.line([W2(p_[0] + 3, p_[1] + 2) for p_ in pts], fill=(225, 200, 160, 200), width=lw(3))
            d.line([W2(*p_) for p_ in pts], fill=(18, 10, 6, 255), width=lw(7))
            for j in (3, 7, 10):   # side branches
                if j < n - 1:
                    p_ = pts[j]; d.line([W2(*p_), W2(p_[0] + (30 if j % 2 else -34), p_[1] + 30)], fill=(25, 15, 10, 255), width=lw(2))
        # dust falling from the ceiling after each thump
        for th in TH:
            v = tt - th
            if 0 <= v < 1.6:
                r_ = np.random.default_rng(int(th * 10))
                for _ in range(40):
                    x_ = r_.uniform(700, 1500); y_ = 20 + v * r_.uniform(250, 520); a_ = int(200 * (1 - v / 1.6))
                    X, Y = W2(x_, y_); d.ellipse([X - 2 * S, Y - 2 * S, X + 2 * S, Y + 2 * S], fill=(200, 180, 150, a_))
        # chandelier sway overlay (crystal drops swinging under the lamp)
        sw = 0
        for th in TH:
            if 0 <= tt - th < 1.5: sw = max(sw, math.sin((tt - th) * 12) * 14 * (1 - (tt - th) / 1.5))
        if sw:
            X, Y = W2(*CHAND)
            for i in range(7):
                ox = (i - 3) * 22; L = 70 + (i % 2) * 20
                d.line([(X + ox * S, Y + 40 * S), (X + (ox + sw) * S, Y + (40 + L) * S)], fill=(230, 210, 160, 200), width=lw(2))
                d.ellipse([X + (ox + sw - 5) * S, Y + (40 + L - 5) * S, X + (ox + sw + 5) * S, Y + (40 + L + 7) * S], fill=(255, 235, 180, 230))
    if set_ == "corridor":
        vx, vy = W2(*VAULT); RR = 190 * S
        d.ellipse([vx - RR, vy - RR, vx + RR, vy + RR], fill=(8, 6, 5, 255))   # the vault door stands wide open
    if set_ == "studio":
        cx_, cy_ = W2(SAFE[0], SAFE[1] + 12)   # dust-free patch: something big stood here for years
        d.ellipse([cx_ - 95 * S, cy_ - 24 * S, cx_ + 95 * S, cy_ + 24 * S], fill=(150, 125, 95, 150))
        d.ellipse([cx_ - 95 * S, cy_ - 24 * S, cx_ + 95 * S, cy_ + 24 * S], outline=(60, 45, 30, 200), width=lw(3))
        # drag marks from where Safeeh stood toward the exit
        for off in (-26, 26):
            pts = [W2(SAFE[0] + off + i * -40, SAFE[1] + 20 + i * 28 + math.sin(i) * 6) for i in range(12)]
            d.line(pts, fill=(25, 18, 12, 220), width=lw(5))
        # Safeeh's antenna lying on the floor
        bx, by = W2(*BULB)
        d.line([(bx - 60 * S, by + 8 * S), (bx, by)], fill=(150, 156, 162, 255), width=lw(5))
        on = int(tt * 2.5) % 2
        d.ellipse([bx - 11 * S, by - 11 * S, bx + 11 * S, by + 11 * S], fill=(255, 50, 40, 255) if on else (90, 30, 30, 255), outline=(30, 20, 20, 255), width=lw(2))
    if set_ == "street":
        # the van pulls away from the building door, front lane (own layer + motion blur)
        u = kk(tt, VAN[0], VAN[1]); vx = lerp(520, 2500, u ** 1.7); spd = 1.7 * u ** 0.7
        vl = Image.new("RGBA", img.size, (0, 0, 0, 0)); vd = ImageDraw.Draw(vl)
        X, Y = W2(vx, 880); s_ = 1.15 * S
        body = (19, 20, 25, 255); edge = (4, 4, 6, 255)
        vd.rounded_rectangle([X - 300 * s_, Y - 250 * s_, X + 170 * s_, Y - 30 * s_], int(22 * s_), fill=body, outline=edge, width=lw(4))
        vd.polygon([(X + 170 * s_, Y - 170 * s_), (X + 260 * s_, Y - 140 * s_), (X + 290 * s_, Y - 80 * s_), (X + 290 * s_, Y - 30 * s_), (X + 170 * s_, Y - 30 * s_)], fill=body, outline=edge)
        vd.polygon([(X + 180 * s_, Y - 160 * s_), (X + 252 * s_, Y - 134 * s_), (X + 270 * s_, Y - 96 * s_), (X + 180 * s_, Y - 96 * s_)], fill=(40, 60, 90, 255))
        vd.line([(X - 60 * s_, Y - 240 * s_), (X - 60 * s_, Y - 40 * s_)], fill=(18, 18, 22, 255), width=lw(3))   # sliding door seam
        vd.line([(X - 290 * s_, Y - 246 * s_), (X + 160 * s_, Y - 246 * s_), (X + 250 * s_, Y - 142 * s_)], fill=(95, 115, 160, 200), width=lw(3))   # street-light rim
        vd.rectangle([X - 300 * s_, Y - 128 * s_, X + 170 * s_, Y - 118 * s_], fill=(60, 64, 74, 255))
        vd.rectangle([X - 40 * s_, Y - 150 * s_, X - 14 * s_, Y - 142 * s_], fill=(80, 84, 92, 255))
        vd.rectangle([X - 300 * s_, Y - 60 * s_, X + 290 * s_, Y - 30 * s_], fill=(20, 20, 24, 255))
        for wx_ in (-190, 190):
            vd.ellipse([X + (wx_ - 46) * s_, Y - 76 * s_, X + (wx_ + 46) * s_, Y + 16 * s_], fill=(10, 10, 12, 255), outline=(70, 70, 76, 255), width=lw(5))
        vd.rectangle([X - 306 * s_, Y - 150 * s_, X - 292 * s_, Y - 100 * s_], fill=(255, 50, 30, 255))
        vl = vl.filter(ImageFilter.GaussianBlur(1 + 3 * spd))
        img.paste(vl, (0, 0), vl)
        tl = Image.new("RGBA", img.size, (0, 0, 0, 0)); td = ImageDraw.Draw(tl)
        td.ellipse([X - 360 * s_, Y - 180 * s_, X - 240 * s_, Y - 70 * s_], fill=(255, 30, 20, 150))
        tl = tl.filter(ImageFilter.GaussianBlur(int(16 * S))); img.paste(tl, (0, 0), tl)
        # cigar ember in the parked car's window (the Pasha is watching)
        if tt >= VAN[0] + 1.6:
            e = 0.6 + 0.4 * math.sin(tt * 5)
            X, Y = W2(*EMBER)
            em = Image.new("RGBA", img.size, (0, 0, 0, 0)); ed = ImageDraw.Draw(em)
            ed.ellipse([X - 22 * S, Y - 22 * S, X + 22 * S, Y + 22 * S], fill=(255, 120, 30, int(160 * e)))
            em = em.filter(ImageFilter.GaussianBlur(int(8 * S))); img.paste(em, (0, 0), em)
            d.ellipse([X - 5 * S, Y - 5 * S, X + 5 * S, Y + 5 * S], fill=(255, 210, 120, 255))

def ltr(img, x, y, s, size, fill, stroke=(10, 10, 10), sw=3):
    ImageDraw.Draw(img).text((x, y), s, font=ImageFont.truetype(FONT, size), fill=fill, anchor="mm", direction="ltr", stroke_width=sw, stroke_fill=stroke)

def sepia(fr, tt):
    g = np.asarray(fr.convert("L"), np.float32) / 255
    fl = 0.93 + 0.07 * math.sin(tt * 37) * math.sin(tt * 11)
    out = np.stack([g * 255 * 1.05, g * 220, g * 170], -1) * fl + np.array([18, 10, 0])
    im = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))
    return ImageChops.multiply(im, VIG_DARK)

def calendar(img, cam):
    x0, y0, z = cam; S = SS * z; d = ImageDraw.Draw(img, "RGBA"); X, Y = (CAL[0] - x0) * S, (CAL[1] - y0) * S
    lw = lambda v: max(1, int(v * S))
    d.rectangle([X - 70 * S, Y - 90 * S, X + 70 * S, Y + 90 * S], fill=(240, 232, 210, 255), outline=(60, 40, 20, 255), width=lw(3))
    d.rectangle([X - 70 * S, Y - 90 * S, X + 70 * S, Y - 50 * S], fill=(170, 40, 40, 255))
    text(img, X, Y - 70 * S, "يناير", int(22 * S), (255, 255, 255), (120, 20, 20), 1)
    ltr(img, X, Y + 10 * S, "1958", int(46 * S), (40, 30, 20), (240, 232, 210), 1)
    for i in range(3): d.line([(X - 50 * S, Y + (50 + i * 12) * S), (X + 50 * S, Y + (50 + i * 12) * S)], fill=(120, 110, 90, 255), width=lw(2))

# ---------- inserts ----------
def vid_card(tt, sh):
    """Fahmy's phone: night footage of men digging at the building's foundations (found-footage look)"""
    fr = ImageEnhance.Brightness(bg_crop(SRC["living"], (500, 150, 1.4), True).resize((W, H)).filter(ImageFilter.GaussianBlur(10))).enhance(0.45)
    k = ease(kk(tt, sh["start"], sh["start"] + 0.4))
    cx, cy = W / 2, H / 2 + (1 - k) * 500 + math.sin(tt * 2.2) * 5
    sw, shh = 1240, 698
    d = ImageDraw.Draw(fr, "RGBA")
    d.rounded_rectangle([cx - sw / 2 - 60, cy - shh / 2 - 34, cx + sw / 2 + 60, cy + shh / 2 + 34], 60, fill=(20, 20, 24, 255), outline=(5, 5, 5, 255), width=6)
    # the footage
    jit = (math.sin(tt * 9) * 6, math.sin(tt * 7 + 1) * 5)
    src = SRC["wall_n"].crop((200 + jit[0], 380 + jit[1], 1640 + jit[0], 1190 + jit[1])).resize((sw, shh))
    g = np.asarray(src.convert("L"), np.float32) / 255
    vid = Image.fromarray(np.clip(np.stack([g * 150, g * 215, g * 150], -1) * 1.3 + 12, 0, 255).astype(np.uint8))
    vd = ImageDraw.Draw(vid, "RGBA")
    # two diggers (silhouettes) at the foundation + a torch on the ground + dirt flying
    for i, (mx, ph) in enumerate(((430, 0.0), (780, 1.7))):
        u = (math.sin(tt * 4 + ph) + 1) / 2; by = 600
        vd.ellipse([mx - 26, by - 250, mx + 26, by - 198], fill=(8, 12, 8, 255))
        vd.polygon([(mx - 34, by - 196), (mx + 34, by - 196), (mx + 44, by - 80), (mx - 44, by - 80)], fill=(8, 12, 8, 255))
        vd.line([(mx - 18, by - 80), (mx - 26, by)], fill=(8, 12, 8, 255), width=14); vd.line([(mx + 18, by - 80), (mx + 26, by)], fill=(8, 12, 8, 255), width=14)
        sx, sy = mx + 70, by - 40 - u * 110
        vd.line([(mx + 20, by - 170), (sx, sy)], fill=(8, 12, 8, 255), width=12)
        vd.line([(sx, sy), (sx + 30, sy + 120 - u * 40)], fill=(8, 12, 8, 255), width=8)
        vd.polygon([(sx + 18, sy + 110 - u * 40), (sx + 52, sy + 104 - u * 40), (sx + 46, sy + 150 - u * 40), (sx + 14, sy + 150 - u * 40)], fill=(8, 12, 8, 255))
        if u > 0.75:
            for j in range(6): vd.ellipse([sx + 40 + j * 14, sy - 20 - j * 9, sx + 48 + j * 14, sy - 12 - j * 9], fill=(30, 40, 28, 255))
    vd.polygon([(1000, 640), (600, 520), (620, 690)], fill=(230, 255, 200, 50))
    vd.rectangle([990, 628, 1030, 652], fill=(20, 20, 20, 255))
    vd.rectangle([0, 600, sw, shh], fill=(10, 14, 10, 120))   # the trench
    r_ = np.random.default_rng(int(tt * FPS))
    for _ in range(300):
        x_, y_ = r_.uniform(0, sw), r_.uniform(0, shh); vd.point((x_, y_), fill=(220, 255, 220, int(r_.uniform(40, 140))))
    for y_ in range(0, shh, 4): vd.line([(0, y_), (sw, y_)], fill=(0, 0, 0, 28))
    fr.paste(vid, (int(cx - sw / 2), int(cy - shh / 2)))
    if int(tt * 2) % 2: d.ellipse([cx - sw / 2 + 30, cy - shh / 2 + 30, cx - sw / 2 + 58, cy - shh / 2 + 58], fill=(255, 40, 40, 255))
    ltr(fr, cx - sw / 2 + 120, cy - shh / 2 + 44, "REC", 36, (255, 255, 255), (0, 0, 0), 3)
    secs = 13 + int(tt - sh["start"])
    ltr(fr, cx + sw / 2 - 160, cy - shh / 2 + 44, f"02:{secs:02d} AM", 36, (255, 255, 255), (0, 0, 0), 3)
    return fr

def clock_card(tt, sh):
    """the lobby clock ticks to 12:00"""
    fr = ImageEnhance.Brightness(bg_crop(SRC["lobby"], (700, 300, 1.6), True).resize((W, H)).filter(ImageFilter.GaussianBlur(6))).enhance(0.5)
    d = ImageDraw.Draw(fr, "RGBA"); cx, cy, R = W / 2, H / 2, 380
    z = 1 + 0.08 * kk(tt, sh["start"], sh["end"])
    R *= z
    d.ellipse([cx - R - 30, cy - R - 30, cx + R + 30, cy + R + 30], fill=(90, 60, 30, 255), outline=(30, 18, 8, 255), width=8)
    d.ellipse([cx - R, cy - R, cx + R, cy + R], fill=(236, 226, 196, 255), outline=(40, 30, 20, 255), width=6)
    for i in range(60):
        a = i * math.pi / 30; L = 40 if i % 5 == 0 else 16
        d.line([(cx + math.sin(a) * (R - 12), cy - math.cos(a) * (R - 12)), (cx + math.sin(a) * (R - 12 - L), cy - math.cos(a) * (R - 12 - L))], fill=(40, 30, 20, 255), width=8 if i % 5 == 0 else 3)
    for i in range(1, 13):
        a = i * math.pi / 6; ltr(fr, cx + math.sin(a) * (R - 90), cy - math.cos(a) * (R - 90), str(i), int(60 * z), (40, 30, 20), (236, 226, 196), 1)
    secs = 57 + min(3, int((tt - sh["start"]) / ((C12 - sh["start"]) / 3)))   # 11:59:57 → 12:00:00
    if tt >= C12: secs = 60
    mins = 59 + secs / 60 if secs < 60 else 60
    ah = (11 + mins / 60) * math.pi / 6; am = mins * math.pi / 30; as_ = (secs % 60) * math.pi / 30
    d.line([(cx, cy), (cx + math.sin(ah) * R * 0.5, cy - math.cos(ah) * R * 0.5)], fill=(20, 14, 8, 255), width=22)
    d.line([(cx, cy), (cx + math.sin(am) * R * 0.78, cy - math.cos(am) * R * 0.78)], fill=(20, 14, 8, 255), width=14)
    d.line([(cx, cy), (cx + math.sin(as_) * R * 0.85, cy - math.cos(as_) * R * 0.85)], fill=(190, 30, 30, 255), width=5)
    d.ellipse([cx - 20, cy - 20, cx + 20, cy + 20], fill=(20, 14, 8, 255))
    if tt >= C12:   # flash on twelve
        u = kk(tt, C12, C12 + 0.5); d.rectangle([0, 0, W, H], fill=(255, 240, 200, int(90 * (1 - u))))
    return fr

FOLLOW = {k: Image.open(ROOT + f"/brand/follow/{k}.png").convert("RGB") for k in ("yt", "tt", "ig", "fb")}
BTN = {"yt": ((25, 414, 551, 477), "Subscribed", (230, 230, 230), (20, 20, 20)),
       "tt": ((18, 269, 244, 336), "Following", (235, 235, 235), (30, 30, 30)),
       "ig": ((19, 351, 252, 403), "Following", (239, 239, 239), (20, 20, 20)),
       "fb": ((19, 659, 281, 716), "متابَع ✓", (228, 230, 235), (20, 20, 20))}
def phone_card(tt, sh, plat="yt", CW_=W, CH_=H):
    fr = Image.new("RGB", (CW_, CH_), (0, 0, 0))
    bgc = bg_crop(SRC["living"], (600, 100, 1.6), True).resize((W, H))
    if CW_ != W: bgc = bgc.crop((W / 2 - 304, 0, W / 2 + 304, H)).resize((CW_, CH_))
    fr.paste(ImageEnhance.Brightness(bgc.filter(ImageFilter.GaussianBlur(8))).enhance(0.55))
    shot_im = FOLLOW[plat]; sw_, sh_ = shot_im.size
    vert = CW_ != W
    maxw, maxh = (960, 1150) if vert else (820, 820)
    scale = min(maxw / sw_, maxh / sh_); iw, ih = int(sw_ * scale), int(sh_ * scale)
    k = ease(kk(tt, sh["start"], sh["start"] + 0.35))
    cx = CW_ / 2; cy = CH_ / 2 - (60 if vert else 0) + (1 - k) * CH_ * 0.5 + math.sin(tt * 2) * 4
    pw, phh = iw + 50, ih + 150
    d = ImageDraw.Draw(fr, "RGBA")
    d.rounded_rectangle([cx - pw / 2 + 12, cy - phh / 2 + 16, cx + pw / 2 + 12, cy + phh / 2 + 16], 54, fill=(0, 0, 0, 120))
    d.rounded_rectangle([cx - pw / 2, cy - phh / 2, cx + pw / 2, cy + phh / 2], 54, fill=(22, 22, 26, 255), outline=(10, 10, 10, 255), width=6)
    scr = (int(cx - iw / 2), int(cy - phh / 2 + 70))
    d.rounded_rectangle([scr[0] - 4, scr[1] - 50, scr[0] + iw + 4, cy + phh / 2 - 22], 30, fill=(255, 255, 255, 255))
    fr.paste(shot_im.resize((iw, ih), Image.LANCZOS), scr)
    (bx0, by0, bx1, by1), new_txt, ncol, tcol = BTN[plat]
    B = [scr[0] + bx0 * scale, scr[1] + by0 * scale, scr[0] + bx1 * scale, scr[1] + by1 * scale]
    bcx, bcy = (B[0] + B[2]) / 2, (B[1] + B[3]) / 2
    if tt >= TAP:
        d.rounded_rectangle(B, int((B[3] - B[1]) / 2), fill=ncol + (255,))
        f = ImageFont.truetype(FONT, int((B[3] - B[1]) * 0.45))
        d.text((bcx, bcy), new_txt, font=f, fill=tcol, anchor="mm", direction="rtl" if plat == "fb" else "ltr")
        u = kk(tt, TAP, TAP + 0.9)
        if u < 1:
            r = 40 + 160 * u; d.ellipse([bcx - r, bcy - r, bcx + r, bcy + r], outline=(255, 214, 90, int(255 * (1 - u))), width=8)
            hy = bcy - 60 - 220 * u; hs = 50 * (0.6 + 0.6 * math.sin(min(1, u * 2) * math.pi / 2))
            d.polygon([(bcx, hy + hs * 0.9), (bcx - hs, hy), (bcx - hs * 0.5, hy - hs * 0.6), (bcx, hy - hs * 0.2), (bcx + hs * 0.5, hy - hs * 0.6), (bcx + hs, hy)], fill=(255, 60, 90, int(255 * (1 - u * 0.7))))
    else:
        g = 0.5 + 0.5 * math.sin(tt * 10)
        d.rounded_rectangle([B[0] - 8, B[1] - 8, B[2] + 8, B[3] + 8], int((B[3] - B[1]) / 2 + 8), outline=(255, 214, 90, int(150 + 100 * g)), width=6)
    v = kk(tt, TAP - 0.8, TAP); w_ = kk(tt, TAP, TAP + 0.5)
    fx_ = bcx + 40; fy = lerp(CH_ + 120, bcy + 18, ease(v)) + (ease(w_) * 260 if tt >= TAP + 0.15 else 0)
    press = 6 if abs(tt - TAP) < 0.1 else 0
    d.line([(fx_ + 220, fy + 420), (fx_, fy + press)], fill=(22, 22, 22, 255), width=22)
    d.ellipse([fx_ - 22, fy - 22 + press, fx_ + 22, fy + 22 + press], fill=(22, 22, 22, 255))
    ltr(fr, CW_ / 2, 90 if vert else 70, "@shattawzalata", 60 if vert else 50, (255, 214, 90), (40, 10, 10), 4)
    return fr

def card(name, tt, sh):
    k = (tt - sh["start"]) / (sh["end"] - sh["start"])
    fr = Image.new("RGB", (W, H), (8, 8, 12))
    g = lambda c: tuple(int(v * min(1, k * 4)) for v in c)
    if name == "title":
        text(fr, W / 2, H / 2 - 110, "عمارة نعناعة", 110, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 + 20, "الموسم التاني: " + SEASON, 70, g((255, 120, 90)), (30, 5, 5), 5)
        text(fr, W / 2, H / 2 + 125, EPT, 52, g((225, 225, 225)))
    elif name == "endcard":
        text(fr, W / 2, H / 2 - 230, "الحلقة 8 بكرة: ليلة البدروم", 96, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 - 100, "أستاذ فهمي صادق ولا كداب؟ اكتبوا في الكومنتات", 52, g((235, 235, 235)))
        xs = [W / 2 - 660, W / 2 - 220, W / 2 + 220, W / 2 + 660]
        for x_, kk_ in zip(xs, ("yt", "fb", "ig", "tt")):
            im = FOLLOW[kk_]; sc = 380 / im.size[0]; th = im.resize((380, int(im.size[1] * sc)), Image.LANCZOS)
            th = th.crop((0, 0, 380, min(th.size[1], 300)))
            if k > 0.15: fr.paste(th, (int(x_ - 190), int(H / 2 + 20)))
        text(fr, W / 2 + 230, H - 70, "تابعونا:", 50, g((255, 214, 90)), (40, 10, 10), 4)
        ltr(fr, W / 2 - 110, H - 70, "@shattawzalata", 50, g((255, 214, 90)), (40, 10, 10), 4)
    return fr

def hud(fr, tt, v=False):
    sc = 0.85 if v else 1.0; cx = 540 if v else W / 2
    y = 1700 if v else 120
    d = ImageDraw.Draw(fr, "RGBA")
    if T("J03") + 1.0 <= tt < T("J03") + DUR["J03"] + 0.6:
        d.rounded_rectangle([cx - 430 * sc, y - 50 * sc, cx + 430 * sc, y + 50 * sc], int(22 * sc), fill=(20, 60, 30, 220), outline=(120, 230, 120, 255), width=4)
        text(fr, cx, y, "إجابة امبارح: سنة 1958 ✓", int(42 * sc), (200, 255, 200))
    if P70 + DUR["J10"] * 0.5 <= tt < P70 + DUR["J10"] + 0.3:
        d.rounded_rectangle([cx - 160 * sc, y - 50 * sc, cx + 160 * sc, y + 50 * sc], int(22 * sc), fill=(60, 20, 20, 220), outline=(255, 120, 90, 255), width=4)
        ltr(fr, cx, y, "70%", int(56 * sc), (255, 160, 120))
    if BLACK <= tt < BLACK + 2.0 and shot_at(tt)["set"] == "lobby":
        d.rounded_rectangle([cx - 150 * sc, y - 44 * sc, cx + 150 * sc, y + 44 * sc], int(20 * sc), fill=(10, 10, 14, 200), outline=(120, 120, 140, 255), width=3)
        ltr(fr, cx, y, "12:00", int(50 * sc), (230, 230, 240))

def vote_box(fr, tt, cx, y, sc=1.0):
    """the first audience VOTE: صادق / كداب"""
    d = ImageDraw.Draw(fr, "RGBA"); k = ease(kk(tt, PUZ + 0.2, PUZ + 0.7))
    d.rounded_rectangle([cx - 600 * sc, y - 90 * sc, cx + 600 * sc, y + 150 * sc], int(26 * sc), fill=(20, 20, 30, int(225 * k)), outline=(255, 214, 90, int(255 * k)), width=5)
    text(fr, cx, y - 30 * sc, "أستاذ فهمي... صادق ولا كداب؟", int(48 * sc), (255, 214, 90))
    for i, (lab, col) in enumerate((("صادق", (60, 170, 90)), ("كداب", (200, 55, 50)))):
        bx = cx + (230 if i == 0 else -230) * sc; pul = 1 + 0.06 * math.sin(tt * 6 + i * 3)
        w_, h_ = 190 * sc * pul, 50 * sc * pul
        d.rounded_rectangle([bx - w_, y + 75 * sc - h_, bx + w_, y + 75 * sc + h_], int(24 * sc), fill=col + (int(255 * k),), outline=(255, 255, 255, int(255 * k)), width=4)
        text(fr, bx, y + 75 * sc, lab, int(52 * sc), (255, 255, 255))

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

def vertical(fr, tt, plat="tt"):
    sh = shot_at(tt)
    if sh["set"] == "phone":
        bgv = phone_card(tt, sh, plat, 1080, 1920)
        k, _ = line_at(tt)
        if k:
            for i, l in enumerate(wrap(SUB[k], 30)[:3]): text(bgv, 540, 1730 + i * 62, l, 50, sw=5)
        return bgv
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
    if PUZ <= tt < PUZ_END: vote_box(bgv, tt, 540, 1640, 0.82)
    return bgv

def finish(fr, tt, dark=False):
    fr = ImageChops.multiply(fr, VIG_DARK if dark else VIG)
    a = np.asarray(fr, np.float32)
    g = GRAIN[int(tt * 6) % len(GRAIN)]
    g = np.repeat(np.repeat(g, 4, 0), 4, 1)[..., None]
    return Image.fromarray(np.clip(a + g, 0, 255).astype(np.uint8))

def emissive(fr, set_, tt, cam):
    """self-lit things drawn after the light map: sparks, the line of light under the basement door"""
    x0, y0, z = cam; W2 = lambda wx, wy: ((wx - x0) * z, (wy - y0) * z)
    if set_ != "lobby": return
    gl = Image.new("RGBA", fr.size, (0, 0, 0, 0)); d = ImageDraw.Draw(gl)
    if SPARK <= tt < BLACK + 0.3:
        r_ = np.random.default_rng(int(tt * FPS)); X, Y = W2(*LAMP)
        for _ in range(12):
            a = r_.uniform(0, math.pi); L = r_.uniform(20, 110) * z
            d.line([(X, Y + 20 * z), (X + math.cos(a) * L, Y + 20 * z + math.sin(a) * L)], fill=(255, 235, 150, 255), width=max(1, int(3 * z)))
    if ABDO - 0.3 <= tt < DAJAR + 2.5 and tt >= BLACK:
        f = 0.75 + 0.25 * math.sin(tt * 13) * math.sin(tt * 5)
        a_ = W2(BDOOR[0] + 20, 952); b_ = W2(BDOOR[2] - 20, 962)
        d.rectangle([a_[0], a_[1] - 10 * z, b_[0], b_[1] + 10 * z], fill=(255, 170, 70, int(70 * f)))
        d.rectangle([a_[0], a_[1], b_[0], b_[1]], fill=(255, 200, 110, int(230 * f)))
    fr.paste(gl.filter(ImageFilter.GaussianBlur(2)), (0, 0), gl.filter(ImageFilter.GaussianBlur(2)))

def eyes_pass(fr, tt):
    """blackout: only the eyes glow in the dark"""
    d = ImageDraw.Draw(fr, "RGBA")
    for X, Y, S, who, expr, back in EYES:
        if back: continue
        if who == "bondo2" and tt < BEYES: continue        # asleep
        if who == "fahmy": continue
        blink = ((tt + (hash(who) % 7) * 0.37) % 2.8) < 0.12
        sh_ = math.sin(tt * 60) * 2 * S if who == "shatta" else 0
        big = 1.35 if (who == "bondo2" and tt < BEYES + 0.5) or (who == "shatta" and T("J19") <= tt < T("J19") + 1.0) else 1.0
        for ex in (-15, 15):
            x_, y_ = X + ex * S + sh_, Y + 2 * S
            rx, ry = 9 * S * big, (2 if blink else 12) * S * big
            d.ellipse([x_ - rx, y_ - ry, x_ + rx, y_ + ry], fill=(250, 250, 245, 255))
            if not blink: d.ellipse([x_ - 4 * S, y_ - 4 * S, x_ + 4 * S, y_ + 4 * S], fill=(10, 10, 10, 255))

TINT = {"living": (255, 228, 190), "studio": (200, 190, 200), "corridor": (130, 145, 185), "street": (150, 160, 210), "flash": (255, 240, 215)}
def frame(tt, plat="yt"):
    sh = shot_at(tt); set_ = sh["set"]
    if set_ in ("title", "endcard"): return finish(card(set_, tt, sh), tt)
    if set_ == "black": return Image.new("RGB", (W, H), (0, 0, 0))
    if set_ == "phone": return finish(phone_card(tt, sh, plat), tt)
    if sh.get("vidins"): return finish(vid_card(tt, sh), tt, True)
    if sh.get("clockins"): return finish(clock_card(tt, sh), tt, True)
    cam = cam_at(sh, tt)
    img = bg_crop(SRC[set_], cam, not sh.get("calins"))
    if sh.get("calins"):
        calendar(img, cam); return finish(sepia(img.resize((W, H), Image.LANCZOS), tt), tt)
    layer, lights = draw_scene_chars(set_, tt, cam, sh)
    tint = (150, 165, 225) if set_ == "lobby" else TINT.get(set_, (255, 244, 225))
    layer = tint_layer(layer, tint, 0.97)
    img.paste(layer, (0, 0), layer)
    props(img, set_, tt, cam, sh)
    fr = img.resize((W, H), Image.LANCZOS)
    lm = light_map(set_, sh, tt, cam, lights)
    dark = set_ in ("corridor", "studio", "street") or (set_ == "lobby" and tt >= BLACK)
    if lm is not None:
        fr = ImageChops.multiply(fr, lm)
        if set_ == "lobby" and tt < BLACK: fr = ImageEnhance.Brightness(fr).enhance(1.6)
        if set_ in ("studio", "corridor"): fr = ImageEnhance.Brightness(fr).enhance(1.35)
        if set_ == "lobby" and tt >= BLACK: fr = ImageEnhance.Brightness(fr).enhance(1.25)
    if set_ in ("lobby", "studio", "corridor"): fr = beams(fr, set_, tt, (cam[0], cam[1], cam[2]), sh, lights)
    emissive(fr, set_, tt, cam)
    if set_ == "lobby" and BLACK <= tt and not lit(tt): eyes_pass(fr, tt)
    if sh.get("dutch"):
        a = sh["dutch"] * ease(kk(tt, sh["start"], sh["start"] + 0.8))
        fr = fr.rotate(a, resample=Image.BICUBIC).crop((96, 54, W - 96, H - 54)).resize((W, H), Image.BICUBIC)
    return finish(fr, tt, dark)

def lowpass(x, fc):
    from numpy.fft import rfft, irfft
    X = rfft(x); fq = np.fft.rfftfreq(len(x), 1 / SR); X[fq > fc] *= 0.08; return irfft(X, len(x)).astype(np.float32)
def echo(x, delays=((0.17, 0.42), (0.34, 0.22), (0.52, 0.1))):
    out = np.zeros(len(x) + int(SR * 0.6), np.float32); out[:len(x)] += x
    for dl, g in delays: i = int(dl * SR); out[i:i + len(x)] += x * g
    return out

def build_audio(path="mix.wav"):
    buf = np.zeros(int(TOTAL * SR) + SR * 3, dtype=np.float32)
    dr = drone(TOTAL + 1); env = np.zeros(len(dr), np.float32)
    for a_, b_ in ((0, TITLE), (TH[0] - 0.5, T("J09")), (LOBW[0], TOTAL - 4.9)):
        env[int(a_ * SR):int(b_ * SR)] = 1.0
    env = np.convolve(env, np.ones(4410) / 4410, mode="same")
    mix_into(buf, dr * env, 0, 1.2)
    r = np.random.default_rng(9)
    S = {"boom": sfx_boom(), "tick": sfx_tick(), **SFXF}
    for t0, nme, g in sfx:
        if nme in S and g > 0: mix_into(buf, S[nme], t0, g)
    # clock ticks from Zalata's line to 12:00, then the big bell-like hit
    tk = T("J17")
    while tk < C12: mix_into(buf, S["tick"], tk, 0.9); tk += 1.0
    # comic stings: 70%, the slipper, the scream
    for t_, notes in ((P70 + 0.5, [523, 494, 440, 392]), (SLIP + DUR["J15"] - 0.2, [784, 659, 523]), (SOUT[0] + 0.2, [392, 523, 659, 784])):
        for i, f in enumerate(notes):
            tt_ = np.arange(int(SR * 0.4)) / SR
            mix_into(buf, np.sin(2 * np.pi * f * tt_) * np.exp(-tt_ * 12) * 0.09, t_ + i * 0.16, 1.0)
    # tension string: the night watch → blackout → basement → van
    a_, b_ = LOBW[0], TOTAL - 4.9
    ts = np.arange(int((b_ - a_) * SR)) / SR
    rise = (np.sin(2 * np.pi * (98 + 40 * ts / ts[-1]) * ts) + 0.5 * np.sin(2 * np.pi * (147 + 60 * ts / ts[-1]) * ts)) * 0.04 * np.minimum(1, ts / 2)
    rise[int((BLACK - a_) * SR):int((BEYES - a_) * SR)] *= 0.25       # near-silence in the dark before the false scare
    mix_into(buf, rise, a_, 1.0)
    # heartbeat in the blackout
    hb = BLACK + 0.4
    while hb < BEYES - 0.2:
        for o in (0, 0.22):
            tb = np.arange(int(SR * 0.18)) / SR; mix_into(buf, np.sin(2 * np.pi * 55 * tb) * np.exp(-tb * 25) * 0.5, hb + o, 1.0)
        hb += 0.85
    # night crickets under the lobby night (before the blackout)
    n = int((LOBW[0] - 0) * SR)
    tsx = np.arange(int(SR * 0.25)) / SR
    for st, g in STEPS:
        nz = np.convolve(r.normal(0, 1, len(tsx)), np.ones(12) / 12, mode="same")
        mix_into(buf, (np.sin(2 * np.pi * 80 * tsx) * np.exp(-tsx * 30) * 0.9 + nz * np.exp(-tsx * 25) * 0.9) * 0.6, st, g)
    for st, k in lines:
        a = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8
        if k == "J20": a = echo(lowpass(a, 1100)) * 0.75             # behind the basement door
        if k == "J24": a = echo(a, ((0.21, 0.3), (0.42, 0.14)))       # the empty studio answers
        if k == "J01" : a = a * 0.85                                   # heard first, off-screen
        mix_into(buf, a, st, 1.0)
    buf = buf[:int(TOTAL * SR)]
    buf = np.clip(buf / max(1e-6, np.abs(buf).max()) * 0.95, -1, 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((buf * 32767).astype(np.int16).tobytes())

def render(out_h, out_v, stills=None, t0=0.0, t1=None):
    fh = fv = None
    if not stills:
        mk = lambda w, h, o: subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}",
                                   "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                                   "-pix_fmt", "yuv420p", o], stdin=subprocess.PIPE)
        fh = mk(W, H, out_h); fv = mk(1080, 1920, out_v)
    t1 = TOTAL if t1 is None else t1
    times = stills or [i / FPS for i in range(int(round(t0 * FPS)), int(round(t1 * FPS)))]
    for i, tt in enumerate(times):
        base = frame(tt, "yt")
        h = base.copy(); hud(h, tt)
        if PUZ <= tt < PUZ_END: vote_box(h, tt, W / 2, 150)
        subtitle(h, tt)
        if stills:
            h.save(f"still_h_{tt:.1f}.png"); vertical(base, tt, "tt").save(f"still_v_{tt:.1f}.png")
        else:
            fh.stdin.write(h.tobytes()); fv.stdin.write(vertical(base, tt, "tt").tobytes())
        if i % 240 == 0: print("frame", i, round(tt, 1), flush=True)
    if fh:
        fh.stdin.close(); fv.stdin.close(); fh.wait(); fv.wait()

def render_phone_variants():
    sh = [s_ for s_ in shots if s_["set"] == "phone"][0]
    for plat in ("ig", "yt"):
        p_ = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "1080x1920", "-r", str(FPS), "-i", "-",
                               "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", f"phone_{plat}.mp4"], stdin=subprocess.PIPE)
        for i in range(int(round(sh["start"] * FPS)), int(round(sh["end"] * FPS))):
            tt = i / FPS; p_.stdin.write(vertical(frame(tt, plat), tt, plat).tobytes())
        p_.stdin.close(); p_.wait()
    print("phone window", round(round(sh["start"] * FPS) / FPS, 3), round(round(sh["end"] * FPS) / FPS, 3))

if __name__ == "__main__":
    print("TOTAL", round(TOTAL, 1))
    if sys.argv[1:2] == ["stills"]:
        render(None, None, [float(v) for v in sys.argv[2:]])
    elif sys.argv[1:2] == ["times"]:
        for s_ in shots: print(s_["set"], round(s_["start"], 2), round(s_["end"], 2), {k: v for k, v in s_.items() if k not in ("set", "start", "end", "c0", "c1")})
        for st, k in lines: print(k, round(st, 2))
    elif sys.argv[1:2] == ["part"]:
        i, n = int(sys.argv[2]), int(sys.argv[3]); a = round(TOTAL * i / n * FPS) / FPS; b = round(TOTAL * (i + 1) / n * FPS) / FPS
        render(f"h_{i}.mp4", f"v_{i}.mp4", None, a, b)
    elif sys.argv[1:2] == ["audio"]:
        build_audio()
    elif sys.argv[1:2] == ["phones"]:
        render_phone_variants()
