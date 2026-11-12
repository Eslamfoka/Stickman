import sys, os, math, subprocess, wave
sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter, ImageFont
from engine import *

# م2 ح6 «الأسطوانة» — built from s2e5/ep5.py, follows the Episode checklist in docs/directing.md.
# New vs Ep5: night hook with a torch beam, the stairs montage (backs to camera, floor numbers), the sunny roof + ladder climb
# with a slip, Nana heard first then walking in, a sepia 1958 flashback with the singer's silhouette + the original song,
# backlit silhouette reveal in the street door.
os.chdir(ROOT + "/s2e6")
SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(606)
SEASON = "سر البدروم"
EPT = "الحلقة 6: الأسطوانة"
SONG = ROOT + "/s2/music/أغنية العمارة - نسخة 2أ.mp3"

SUB = {
 "H01": "يا باشا!... الروبوت صاحي... وعينه حمرا!",
 "H02": "اصبر يا عبده... كل حاجة ليها تمن.",
 "H03": "صباح الخير يا صفيح!... قلتلك هاجي لك.",
 "H04": "صباح الخير... يا رشدي.",
 "H05": "خلاص يا شطة... بقيت رشدي رسمي.",
 "H06": "إجابة لغز امبارح: فوق الكل ومليان مية... خزان المية اللي على السطوح!",
 "H07": "سبع أدوار... من غير أسانسير... أنا خلصت.",
 "H08": "احتمال شطة يطلع فوق الخزان: 10%",
 "H09": "ثقوا فيا المرة دي!",
 "H10": "لقيت حاجة!... علبة!... علبة حديد!",
 "H11": "مكتوب على المفتاح: تسجيلات عمارة نعناعة... والسنة ممسوحة!",
 "H12": "إنتو بتعملوا إيه فوق السطوح؟!",
 "H13": "المفتاح ده... مفتاح رشدي.",
 "H14": "زمان... البدروم ده كان أحلى استوديو في مصر.",
 "H15": "يا نعناعة... هاتي المفك!... صفيح هيبقى أحسن حارس في الدنيا!",
 "H16": "رشدي بنى صفيح... عشان يحرس الأسطوانة.",
 "H17": "أسطوانة إيه يا تيتا؟",
 "H18": "أغنية العمارة... بصوت الست بهية.",
 "H19": "لغز النهارده: الأغنية دي اتسجلت سنة كام؟... ركزوا في الفلاش باك! اكتبوا في الكومنتات!",
 "H20": "ثقوا فيا... اعملوا فولو، عشان تعرفوا الإجابة بكرة!",
 "H21": "مين اللي بيخبط بالليل؟... أنا صاحي أهو.",
 "H22": "أنا مش جاي أأذي حد... أنا جاي أحذركم.",
 "H23": "أستاذ فهمي؟!",
}
WHO = {"H01": "abdo", "H02": "pasha", "H03": "shatta", "H04": "safeeh", "H05": "zalata", "H06": "tota", "H07": "shatta",
       "H08": "zalata", "H09": "shatta", "H10": "shatta", "H11": "tota", "H12": "nana", "H13": "nana", "H14": "nana",
       "H15": "roshdy", "H16": "nana", "H17": "zalata", "H18": "nana", "H19": "tota", "H20": "shatta", "H21": "bondo2",
       "H22": "fahmy", "H23": "shatta"}
EXPR = {"H01": "scared", "H02": "smug", "H03": "happy", "H05": "flat", "H06": [(0, "neutral"), (0.6, "smug")], "H07": "sad",
        "H08": "flat", "H09": "smug", "H10": [(0, "shock"), (0.3, "happy")], "H11": "neutral", "H12": "angry", "H13": "sad",
        "H14": "happy", "H15": "happy", "H16": "sad", "H17": "neutral", "H18": "happy", "H19": [(0, "neutral"), (0.6, "smug")],
        "H20": "smug", "H21": "sleepy", "H22": "flat", "H23": "shock"}
ARMS = {"H03": "up", "H05": "hold", "H06": "point", "H07": "hips", "H08": "hold", "H09": "hips", "H11": "hold", "H12": "point",
        "H13": "hold", "H14": "talk", "H15": "talk", "H16": "talk", "H17": "talk", "H18": "talk", "H19": "point", "H20": "point",
        "H22": "talk", "H23": "scared"}

def _aud(k): return load_audio(f"audio/{k}.mp3")
AUD = {k: _aud(k) for k in SUB}
ENV = {k: envelope(v) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}
SFXF = {n: load_audio(ROOT + f"/s2e4/sfx/{n}.mp3") for n in ("whoosh", "creak", "slam", "switch", "steps_metal", "clang",
                                                             "stinger", "servo", "car", "keys", "snore", "unlock")}
SFXF["knocks"] = load_audio(ROOT + "/s2e4/sfx/knocks.mp3")
SONGA = load_audio(SONG)

lines, sfx, shots, jumps, shakes = [], [], [], {}, []
def say(t, k): lines.append((t, k)); return t + DUR[k]
def fx(t, n, g=1.0): sfx.append((t, n, g))
def jump(w, t): jumps.setdefault(w, []).append(t)
def shot(set_, s, e, c0, c1=None, **kw): shots.append(dict(set=set_, start=s, end=e, c0=c0, c1=c1 or c0, **kw))
def cut(t, g=0.4): fx(t - 0.12, "whoosh", g)
def T(k): return [st for st, kk_ in lines if kk_ == k][0]
KIDS = ("shatta", "zalata", "tota")

# ---------------- world ----------------
WWIN = (512, 487, 937, 787)                         # wall.png basement window
AB0, AB1 = (1500, 985, 1.7), (1035, 985, 1.7)       # Abdo walks in to the window
CAR_P = (1380, 880, 2.3)                            # night car (s2e4 carin)
SAFE = (1600, 770, 1.6)                            # studio (Safeeh stands where the sheet was)
SK = {"tota": (620, 1000, 1.95), "shatta": (860, 1010, 1.95), "zalata": (1100, 1000, 1.95)}
# roof_day.png → 1920 coords
RDOOR = (205, 690, 1.0); TANK = (1725, 170); LAD_B = (1840, 712, 1.25); LAD_T = (1840, 330, 1.2)
RK = {"tota": (700, 1000, 1.95), "shatta": (980, 1010, 1.95), "zalata": (1240, 1000, 1.95)}
RKN = (420, 990, 1.9)                               # Nana on the roof
# lobby (morning.png)
ENTR = (809, 600); BENCH = (170, 1000, 1.85); STB = (1330, 905, 1.65)
PEEK = {"tota": (1290, 905, 1.5), "shatta": (1380, 900, 1.5), "zalata": (1470, 905, 1.5)}
FDOOR = (809, 640, 0.95)
# flashback (studio, 1958)
SINGER = (1000, 760, 1.25); RYOUNG = (1450, 960, 1.85); NYOUNG = (1680, 980, 1.7); SMALLS = (1300, 950, 0.95)
CAL = (1590, 340)

def CU(who, pos, z=2.2, dx=0):
    x, y, s = pos
    if who == "safeeh":
        return (x + dx, y - 250 * s + H / (2 * z) - 110 * s, z)
    S = s * CH[who]["scale"]
    z += 0.45
    if who == "tota": z *= 1.3; dx -= 50
    hy = y - 190 * S
    return (x + dx, hy + H / (2 * z) - 1.45 * 46 * S - 25, z)

t = 0.0
# ===== 0. HOOK — night, Abdo comes back to the basement window =====
AWALK = (0.0, 2.2); fx(0.2, "steps_metal", 0.0)
shot("wall_n", 0, 2.2, (1100, 560, 1.15), (900, 600, 1.35))
EYES = 2.6; fx(EYES - 0.05, "switch", 1.0); fx(EYES, "stinger", 1.0); shakes.append((EYES, 8))
shot("wall_n", 2.2, 3.4, (725, 640, 2.4), (725, 640, 3.0), ease="crash")
FALL = 3.4; fx(FALL + 0.15, "clang", 0.6); shakes.append((FALL + 0.15, 10))
shot("wall_n", 3.4, 4.6, (950, 640, 1.4), (950, 660, 1.5)); t = 4.6
RUN = (t, t + DUR["H01"] + 0.4)
s = t; t = say(t, "H01") + 0.1
shot("wall_n", s, t, (1100, 600, 1.25), (1350, 600, 1.3))
cut(t, 0.3)
s = t; t = say(t + 0.3, "H02") + 0.4
shot("carin", s, t, CU("pasha", CAR_P, 1.4), CU("pasha", CAR_P, 1.7), low=True)
TITLE = t; shot("title", t, t + 2.0, None); t += 2.0
# ===== 1. MORNING — promise kept =====
TLM = (t, t + 2.4)
shot("lobby", t, TLM[1], (760, 620, 1.12), (700, 640, 1.18), tl=(0, 1, TLM)); t = TLM[1]
LWALK = (t, t + 3.0); fx(t + 2.6, "creak", 0.8)
shot("lobby", t, LWALK[1], (1100, 640, 1.2), (1400, 640, 1.3), tod=1); t = LWALK[1]
cut(t, 0.25); SIN = (t, t + 2.4)
shot("studio", t, SIN[1], (1200, 560, 1.1), (1300, 560, 1.15)); t = SIN[1]
s = t; t = say(t, "H03") + 0.1; jump("shatta", s)
shot("studio", s, t, CU("shatta", SK["shatta"], 1.6), CU("shatta", SK["shatta"], 1.75))
s = t; t = say(t + 0.2, "H04") + 0.2
shot("studio", s, t, CU("safeeh", SAFE, 1.8), CU("safeeh", SAFE, 2.0), low=True)
s = t; t = say(t, "H05") + 0.3
shot("studio", s, t, CU("zalata", SK["zalata"], 1.8), CU("zalata", SK["zalata"], 1.95))
s = t; t = say(t, "H06") + 0.2
shot("studio", s, t, CU("tota", SK["tota"], 1.5), CU("tota", SK["tota"], 1.62))
# ===== 1b. Seven floors, no lift (backs to camera, floor numbers) =====
cut(t, 0.25); MONT = (t, t + 4.8)
for i in range(4):
    shot("stairs", t + i * 1.2, t + (i + 1) * 1.2, (1150, 560, 1.05 + i * 0.03), (1150, 600, 1.12 + i * 0.03), floor=i)
t = MONT[1]
s = t; t = say(t, "H07") + 0.3
shot("roof", s, t, CU("shatta", (330, 1000, 1.95), 1.6), CU("shatta", (330, 1000, 1.95), 1.75))
# ===== 2. THE ROOF =====
RIN = (t, t + 2.6)
shot("roof", t, RIN[1], (900, 560, 1.05), (1000, 560, 1.12)); t = RIN[1]
s = t; t = say(t, "H08") + 0.2
shot("roof", s, t, CU("zalata", RK["zalata"], 1.8), CU("zalata", RK["zalata"], 1.95))
s = t; t = say(t, "H09") + 0.1
shot("roof", s, t, CU("shatta", RK["shatta"], 1.6), CU("shatta", RK["shatta"], 1.75))
CLIMB = (t, t + 4.6); SLIP = t + 2.3; fx(SLIP, "clang", 0.7); fx(SLIP + 0.05, "whoosh", 0.6); shakes.append((SLIP, 6))
shot("roof", t, t + 2.0, (1500, 560, 1.4), (1700, 470, 1.8), low=True)
shot("roof", t + 2.0, CLIMB[1], (1820, 420, 2.4), (1820, 380, 2.6), low=True); t = CLIMB[1]
s = t; t = say(t, "H10") + 0.2
shot("roof", s, t, (1760, 250, 2.5), (1760, 240, 2.8))
DOWN = (t, t + 1.6)
shot("roof", t, DOWN[1], (1400, 600, 1.3), (1200, 620, 1.35)); t = DOWN[1]
BOX = t; fx(t + 0.5, "unlock", 0.8); fx(t + 0.9, "keys", 0.8)
shot("roof", t, t + 2.2, None, boxins=True); t += 2.2
s = t; t = say(t, "H11") + 0.2
shot("roof", s, s + 2.4, None, boxins=True, keyzoom=True)
shot("roof", s + 2.4, t, CU("tota", RK["tota"], 1.5), CU("tota", RK["tota"], 1.65))
# ===== 3. NANA (heard first, then walks in) =====
s = t; t = say(t + 0.2, "H12") + 0.1; FREEZE = s
shot("roof", s, t, (1000, 600, 1.2), (1000, 600, 1.25))
NIN = (t, t + 2.2); fx(t + 0.1, "creak", 0.9)
shot("roof", t, NIN[1], (420, 640, 1.4), (460, 640, 1.55)); t = NIN[1]
shot("roof", t, t + 1.6, None, keyins2=True); KEYSEE = t; t += 1.6
s = t; t = say(t, "H13") + 0.3
shot("roof", s, t, CU("nana", RKN, 1.7), CU("nana", RKN, 1.9))
s = t; t = say(t, "H14") + 0.3
shot("roof", s, t, CU("nana", RKN, 1.8), CU("nana", RKN, 2.3))
# ===== 4. FLASHBACK 1958 =====
FB = (t, None); fx(t, "whoosh", 0.6)
SONG_T = (t, t + 7.0)
shot("flash", t, t + 3.6, (1000, 520, 1.0), (1000, 560, 1.15)); t += 3.6
shot("flash", t, t + 1.8, (SINGER[0], SINGER[1] - 300, 2.0), (SINGER[0], SINGER[1] - 300, 2.3)); t += 1.8
shot("flash", t, t + 1.6, (CAL[0], CAL[1] + 20, 3.2), (CAL[0], CAL[1] + 10, 3.6), calins=True); t += 1.6
s = t; t = say(t + 0.1, "H15") + 0.2
shot("flash", s, t, CU("roshdy", RYOUNG, 1.6), CU("roshdy", RYOUNG, 1.75))
s = t; t = say(t, "H16") + 0.6; SPARK = s + 1.2; fx(SPARK, "switch", 0.6)
shot("flash", s, t, (1450, 640, 1.4), (1420, 640, 1.6))
FB = (FB[0], t); fx(t - 0.1, "whoosh", 0.6)
# ===== 5. BACK ON THE ROOF — puzzle + CTA =====
s = t; t = say(t + 0.2, "H17") + 0.2
shot("roof", s, t, CU("zalata", RK["zalata"], 1.8), CU("zalata", RK["zalata"], 1.95))
s = t; t = say(t, "H18") + 0.4
shot("roof", s, t, CU("nana", RKN, 1.7), CU("nana", RKN, 1.9))
PUZ = t; s = t; t = say(t + 0.1, "H19") + 0.5; PUZ_END = t
shot("roof", s, t, CU("tota", RK["tota"], 1.5), CU("tota", RK["tota"], 1.68))
s = t; t = say(t, "H20") + 0.4; CTA = (s, t)
shot("roof", s, s + 1.4, CU("shatta", RK["shatta"], 1.6), CU("shatta", RK["shatta"], 1.7))
shot("phone", s + 1.4, t + 0.6, None); TAP = s + 1.4 + 1.6; fx(TAP, "switch", 0.9); t += 0.6
# ===== 6. NIGHT — knocks =====
TLN = (t, t + 2.4)
shot("lobby", t, TLN[1], (760, 620, 1.12), (760, 640, 1.18), tl=(1, 0, TLN)); t = TLN[1]
KNOCK = t + 0.2; fx(KNOCK, "knocks", 1.1)
shot("lobby", t, t + 1.6, (ENTR[0], ENTR[1] - 120, 2.4), (ENTR[0], ENTR[1] - 120, 2.6)); t += 1.6
WAKE = t; fx(t, "snore", 0.0)
shot("lobby", t, t + 1.0, CU("bondo2", BENCH, 1.8), CU("bondo2", BENCH, 1.9)); t += 1.0
s = t; t = say(t, "H21") + 0.2
shot("lobby", s, t, CU("bondo2", BENCH, 1.8), CU("bondo2", BENCH, 2.0))
BWALK = (t, t + 3.2); fx(t + 2.8, "knocks", 0.7)
shot("lobby", t, BWALK[1], (900, 640, 1.2), (850, 600, 1.3)); t = BWALK[1]
PEEKS = t
shot("lobby", t, t + 1.4, (1380, 560, 1.9), (1380, 560, 2.0)); t += 1.4
DOPEN = t + 0.2; fx(DOPEN, "creak", 1.1); fx(DOPEN + 0.3, "stinger", 0.9)
shot("lobby", t, t + 2.6, (ENTR[0], ENTR[1] - 60, 1.4), (ENTR[0], ENTR[1] - 90, 2.0)); t += 2.6
s = t; t = say(t, "H22") + 0.3; REVEAL = s + 1.0
shot("lobby", s, t, (ENTR[0], ENTR[1] - 140, 2.2), (ENTR[0], ENTR[1] - 150, 2.8))
s = t; t = say(t, "H23") + 0.3; jump("shatta", s)
shot("lobby", s, t, CU("shatta", PEEK["shatta"], 1.7), CU("shatta", PEEK["shatta"], 2.4), ease="crash")
fx(t, "clang", 1.2); fx(t, "boom", 0.9); shakes.append((t - 0.2, 12))
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
for a_, b_, r_, g_ in ((AWALK[0], AWALK[1], 7, 0.45), (RUN[0], RUN[1], 12, 0.5), (LWALK[0], LWALK[1], 8, 0.4), (SIN[0], SIN[1], 7, 0.35),
                       (MONT[0], MONT[1], 9, 0.35), (RIN[0], RIN[1], 7, 0.35), (NIN[0], NIN[1], 6, 0.4), (BWALK[0], BWALK[1], 5, 0.4)):
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
    return sh.get("tod", 0 if tt >= TLN[0] else 1)
def tinted(img, lvl=1.0, tint=(255, 255, 255)):
    return ImageChops.multiply(ImageEnhance.Brightness(img).enhance(lvl), Image.new("RGB", img.size, tint))
def _ld(p): return Image.open(p).convert("RGB").resize((1920, 1080), Image.LANCZOS)
_mor = _ld(ROOT + "/s1e10/bg/morning.png")
_st = _ld(ROOT + "/s1e1/bg/stairs_1080.png")
SRC = {"wall_n": tinted(_ld(ROOT + "/s2e5/bg/wall.png"), 0.42, (120, 140, 210)),
       "carin": _ld(ROOT + "/s2e4/bg/carin.png"),
       "lobby_day": _mor, "lobby_night": tinted(_mor, 0.72, (140, 158, 225)),
       "stairs": tinted(ImageEnhance.Brightness(_st).enhance(1.5), 1.0, (255, 228, 185)),
       "studio": ImageEnhance.Brightness(_ld(ROOT + "/s2e5/bg/studio_nosheet.png")).enhance(1.25),
       "roof": _ld("bg/roof_day.png"),
       "flash": ImageEnhance.Brightness(_ld(ROOT + "/s2e5/bg/studio_nosheet.png")).enhance(1.7)}
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

def bg_frame(set_, cam, sh, tt):
    ins = sh.get("calins")
    if set_ == "lobby":
        d = tod(sh, tt)
        if d >= 0.999: return bg_crop(SRC["lobby_day"], cam)
        if d <= 0.001: return bg_crop(SRC["lobby_night"], cam)
        return Image.blend(bg_crop(SRC["lobby_night"], cam), bg_crop(SRC["lobby_day"], cam), d)
    return bg_crop(SRC[set_], cam, not ins)

def A_(who, pos, **kw):
    x, y, s = pos; d = dict(who=who, x=x, y=y, s=s, look=0, expr="neutral", arms="down"); d.update(kw); return d
def walk_to(a, p0, p1, win, tt, rate=8):
    k = kk(tt, *win); e = ease(k)
    a["x"], a["y"], a["s"] = lerp(p0[0], p1[0], e), lerp(p0[1], p1[1], e), lerp(p0[2], p1[2], e)
    if 0 < k < 1: a["walk"] = tt * rate
    return k

OFF = {"tota": 0.0, "shatta": 0.35, "zalata": 0.7}
def kid(who, set_, tt):
    a = A_(who, SK[who], look=1)
    if who == "zalata": a["held"] = "nbpen"; a["arms"] = "hold"; a["expr"] = "flat"
    off = OFF[who]
    if set_ == "lobby":
        if tt < TLN[0]:
            if not (LWALK[0] <= tt < LWALK[1]): return None
            p0 = (STB[0] - 60 + 60 * off, STB[1] + 60, 1.7); p1 = (1560 + 80 * off, 935, 1.55)
            k = walk_to(a, p0, p1, (LWALK[0] + off * 0.5, LWALK[1] - 0.2), tt, 8)
            a["look"] = 1; a["back"] = k > 0.55
            if k >= 1: return None
            return a
        if tt < PEEKS - 1.5: return None
        a["x"], a["y"], a["s"] = PEEK[who]; a["look"] = -1; a["expr"] = "scared" if who != "zalata" else "flat"
        a["held"] = None; a["arms"] = "scared" if who == "shatta" else "down"
        if tt >= DOPEN: a["expr"] = "shock" if who != "zalata" else "shock"
        return a
    if set_ == "studio":
        st0 = SIN[0] + off * 0.5
        if tt < st0: return None
        walk_to(a, (-200, 1020, 2.0), SK[who], (st0, SIN[1] + 0.3), tt, 7)
        a["look"] = 1; a["expr"] = "happy" if who != "zalata" else "flat"
        return a
    if set_ == "stairs":
        sh = shot_at(tt); i = sh.get("floor", 0)
        u = kk(tt, sh["start"], sh["end"])
        xo = {"tota": 0, "shatta": -70, "zalata": 70}[who]
        k0 = max(0, min(1, u * 1.25 - off * 0.25))
        a.update(x=1150 + xo * lerp(1, 0.4, k0), y=lerp(1050, 380, k0), s=lerp(1.9, 0.7, k0), walk=tt * (8 - i), back=True,
                 arms="down", held=None)
        return a
    if set_ == "roof":
        a["held"] = "nbpen" if who == "zalata" else None
        if tt < RIN[0]:
            if who == "shatta": a.update(x=330, y=1000, s=1.95, look=1, expr="sad", arms="hips", lean=0.3); return a
            return None
        st0 = RIN[0] + off * 0.5
        if tt < st0: return None
        walk_to(a, (RDOOR[0] + 60, RDOOR[1] + 280, 1.8), RK[who], (st0, RIN[1] + 0.2), tt, 7)
        a["look"] = 1; a["expr"] = "neutral" if who != "zalata" else "flat"
        if who == "shatta" and tt >= CLIMB[0]:
            if tt < DOWN[1]:
                # walk to the ladder, climb (back to camera), slip, hang, climb on
                k1 = walk_to(a, RK["shatta"], LAD_B, (CLIMB[0], CLIMB[0] + 1.0), tt, 8)
                if k1 >= 1:
                    u = kk(tt, CLIMB[0] + 1.0, CLIMB[1])
                    if tt < SLIP: v = kk(tt, CLIMB[0] + 1.0, SLIP) * 0.55
                    elif tt < SLIP + 1.0: v = 0.55 - 0.18 * ease(kk(tt, SLIP, SLIP + 0.2))
                    else: v = lerp(0.37, 1.0, ease(kk(tt, SLIP + 1.0, CLIMB[1])))
                    a.update(x=LAD_B[0], y=lerp(LAD_B[1], LAD_T[1], v), s=lerp(LAD_B[2], LAD_T[2], v), back=True, arms="up",
                             walk=(tt * 6 if tt < SLIP or tt > SLIP + 1.0 else None))
                    if SLIP <= tt < SLIP + 1.0:
                        a["swing"] = math.sin((tt - SLIP) * 9) * 18
                    if tt >= CLIMB[1]:
                        a.update(back=False, x=LAD_T[0] - 40, y=LAD_T[1], s=LAD_T[2], expr="happy", arms="up", held=None, walk=None)
                        if tt >= T("H10") + DUR["H10"] * 0.3: a["held"] = "paper"; a["arms"] = "hold"
                    if tt >= DOWN[0]:   # he's already down the ladder: walks back to the others with the box
                        walk_to(a, (LAD_B[0] - 60, LAD_B[1] + 150, 1.6), RK["shatta"], DOWN, tt, 8); a["back"] = False
                        a["held"] = "paper"; a["arms"] = "hold"; a["expr"] = "happy"
            else:
                a["x"], a["y"], a["s"] = RK["shatta"]
        if SLIP <= tt < SLIP + 1.4 and who != "shatta": a["expr"] = "shock"; a["arms"] = "scared" if who == "tota" else a["arms"]
        if tt >= FREEZE:
            a["expr"] = "shock" if tt < NIN[1] else ("sad" if who != "zalata" else "flat"); a["look"] = -1
            if tt < NIN[1]: a["arms"] = "up" if who == "shatta" else a["arms"]
        if who == "tota" and tt >= BOX: a["held"] = "key"; a["arms"] = "hold"
        if tt >= FB[1]: a["expr"] = "neutral" if who != "zalata" else "flat"; a["look"] = -1
        return a
    return None

def nana_roof(tt):
    if tt < NIN[0] - 0.2: return None
    a = A_("nana", RKN, look=1, expr="angry", held="basket", arms="hold")
    k = walk_to(a, (RDOOR[0], RDOOR[1] + 40, 1.1), RKN, NIN, tt, 6)
    if tt >= KEYSEE: a["expr"] = "sad"
    if tt >= T("H14"): a["expr"] = "happy"
    if tt >= FB[1]: a["expr"] = "happy"
    return a

def actors(set_, tt, sh):
    A = []
    if sh.get("boxins") or sh.get("keyins2") or sh.get("calins"): return A
    if set_ == "wall_n":
        ab = A_("abdo", AB1, look=-1, expr="neutral", held="torch", arms="hold", lean=-0.6)
        walk_to(ab, AB0, AB1, AWALK, tt, 7)
        if tt >= EYES: ab["expr"] = "shock"
        if tt >= FALL:
            ab["arms"] = "up"; ab["held"] = None
            u = kk(tt, FALL, FALL + 0.3); ab["y"] = AB1[1] + 60 * ease(u); ab["lean"] = 0.8 * ease(u)
            ab["stars"] = tt < RUN[0] + 0.6
        if tt >= RUN[0]:
            k = walk_to(ab, (AB1[0], AB1[1] + 60, AB1[2]), (2300, 985, 1.7), RUN, tt, 12)
            ab.update(expr="scared", held="phone", arms="shush", look=1, lean=0)
            if k >= 1: return A
        A.append(ab)
        return A
    if set_ == "carin":
        A.append(A_("pasha", CAR_P, look=-1, expr="smug", held="phone", arms="shush")); return A
    if set_ == "studio":
        sf = dict(who="safeeh", x=SAFE[0], y=SAFE[1], s=SAFE[2], eye="green", eye_on=1.0, arms="down", drawer=0.0, sad=False, look=-1, lean=0.0)
        if T("H04") <= tt < T("H04") + 1.6: sf["arms"] = "point"     # waves
        if tt < SIN[0] + 0.8: sf["sad"] = True; sf["eye_on"] = 0.6
        A.append(sf)
    if set_ == "lobby":
        if tt >= TLN[0]:
            b = A_("bondo2", BENCH, look=1, expr="sleepy", lean=-0.25)
            if tt >= WAKE: b["expr"] = "flat"; b["lean"] = 0
            if tt >= BWALK[0]:
                k = walk_to(b, BENCH, (ENTR[0] + 110, 690, 1.05), BWALK, tt, 5); b["back"] = k > 0.3; b["held"] = "lantern"; b["arms"] = "hold"
                if tt >= DOPEN: b["back"] = False; b["look"] = -1; b["expr"] = "shock"
            A.append(b)
            if tt >= DOPEN + 0.3:
                f = A_("fahmy", FDOOR, look=1, expr="flat", sil=1.0 - ease(kk(tt, REVEAL, REVEAL + 1.2)) * 0.85)
                walk_to(f, (ENTR[0], 600, 0.8), FDOOR, (DOPEN + 0.3, DOPEN + 1.6), tt, 4)
                A.append(f)
    if set_ == "roof":
        n = nana_roof(tt)
        if n: A.append(n)
    if set_ == "flash":
        A.append(A_("roshdy", RYOUNG, look=-1, expr="happy", arms="hold", held="key"))
        A.append(A_("youngnana", NYOUNG, look=-1, expr="happy", arms="hold", held="paper"))
        sf = dict(who="safeeh", x=SMALLS[0], y=SMALLS[1], s=SMALLS[2], eye="green", eye_on=0.0, arms="down", drawer=0.0, sad=False, look=1, lean=0.0)
        if tt >= SPARK: sf["eye_on"] = [1, 0, 1, 0.4, 1][min(4, int((tt - SPARK) / 0.07))] if tt < SPARK + 0.35 else 1.0
        A.append(sf)
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
        tgt = layer if not a.get("sil") else Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0))
        p = P(tgt)
        if set_ not in ("stairs",) and not (who == "shatta" and set_ == "roof" and CLIMB[0] + 1.0 <= tt < DOWN[1]):
            p.ell(X, (a["y"] - y0) * z + 4 * s, (70 if who == "safeeh" else 46) * s, 9 * s, (0, 0, 0, 110), None)
        if who == "safeeh":
            draw_safeeh(p, X, Y, s, tt, a["eye"], a["eye_on"], mouth, a.get("look", 0), a.get("walk"), a["arms"], a["drawer"], a.get("lean", 0), a["sad"])
            continue
        if a.get("back"):
            draw_back(p, who, X, Y, s, tt, a.get("walk"), a.get("arms", "down"), a.get("held"))
            if who == "bondo2" and a.get("held") == "lantern":
                lights.append((X + 30 * s, Y - 110 * s, 150 * s, 1.2, (1.0, 0.85, 0.5)))
            continue
        expr = a.get("expr", "neutral")
        if talking: expr = expr_of(k, lt)
        arms = a.get("arms", "down")
        if talking and not a.get("held") and k in ARMS: arms = ARMS[k]
        look = a.get("look", 0)
        if spk is not None and not talking and a.get("walk") is None and who != "fahmy":
            look = 1 if spk["x"] > a["x"] else -1             # listeners react: look at whoever talks
        shiver = math.sin(tt * 60) * 2.5 if expr in ("scared", "shock") and who in KIDS + ("abdo",) else 0
        blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11 and expr != "sleepy"
        draw_char(p, who, X + shiver * z, Y, s, expr, mouth, look, blink, arms, tt, a.get("held"), a.get("lean", 0), a.get("walk"))
        S = s * CH[who]["scale"]
        if who == "pasha":
            hy = Y - 190 * S + math.sin(tt * 2.2 + X) * 1.6 * S; hx = X + a.get("lean", 0) * 18 * S
            p.rect(hx - 30 * S, hy - 70 * S, hx + 30 * S, hy - 34 * S, (22, 22, 28, 255), INK, 2.5 * S, 14 * S)
            p.rect(hx - 29 * S, hy - 46 * S, hx + 29 * S, hy - 38 * S, (140, 25, 30, 255), None)
            p.ell(hx, hy - 36 * S, 60 * S, 10 * S, (22, 22, 28, 255), INK, 2.5 * S)
        if a.get("stars"):
            hy = Y - 190 * S
            for i in range(4):
                ang = tt * 5 + i * math.pi / 2
                sx_, sy_ = X + math.cos(ang) * 55 * S, hy - 60 * S + math.sin(ang) * 14 * S
                p.poly([(sx_, sy_ - 9 * S), (sx_ + 3 * S, sy_ - 3 * S), (sx_ + 9 * S, sy_), (sx_ + 3 * S, sy_ + 3 * S), (sx_, sy_ + 9 * S),
                        (sx_ - 3 * S, sy_ + 3 * S), (sx_ - 9 * S, sy_), (sx_ - 3 * S, sy_ - 3 * S)], (255, 220, 60, 255), INK, 1.5 * S)
        if who == "bondo2" and a.get("lean", 0) < 0:   # Zzz
            for i in range(3):
                u = ((tt * 0.6) + i / 3) % 1
                text(tgt, (X + (40 + 30 * u + i * 6) * S) * SS, (Y - (220 + 140 * u) * S) * SS, "Z", int((26 + 18 * i) * S * SS), (255, 255, 255, int(255 * (1 - u))), sw=2)
        hx_, hy_ = HANDS.get(arms, (46, 104)); hand = (X + hx_ * S, Y - hy_ * S)
        if a.get("held") == "torch":
            lights.append((hand[0] - 60 * S, hand[1], 200 * s, 1.6, (1.0, 0.95, 0.75)))
        if a.get("held") == "lantern":
            lights.append((hand[0], hand[1] + 30 * S, 170 * s, 1.3, (1.0, 0.85, 0.5)))
        if a.get("sil"):
            sil = a["sil"]; al_ = tgt.getchannel("A")
            dark = Image.new("RGBA", tgt.size, (10, 10, 14, 255)); dark.putalpha(al_.point(lambda v: int(v * sil)))
            tgt.alpha_composite(dark); layer.alpha_composite(tgt)
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
    cool = np.array([0.75, 0.85, 1.1], np.float32); warm = np.array([1.05, 0.95, 0.8], np.float32)
    if set_ == "wall_n":
        m = np.full((LH, LW, 3), 0.55, np.float32) * cool
        X, Y = W3(1500, 0); m += 0.25 * glow(X, Y, 600 * z)[..., None] * cool
        if tt >= EYES and tt < RUN[1] + 0.5:
            r = 0.8 + 0.2 * math.sin(tt * 9)
            X, Y = W3(725, 640); m += 1.1 * r * glow(X, Y, 200 * z)[..., None] * np.array([1.3, 0.15, 0.1], np.float32)
    elif set_ == "lobby":
        d = tod(sh, tt)
        if d >= 0.99 and not lights: return None
        m = np.full((LH, LW, 3), 0.62 + 0.38 * d, np.float32) * (cool * (1 - d) + d)
        if tt >= DOPEN:   # backlight + fog through the open street door
            k = ease(kk(tt, DOPEN, DOPEN + 0.8))
            X, Y = W3(ENTR[0], ENTR[1] - 120); m += 1.6 * k * glow(X, Y, 260 * z)[..., None] * np.array([1.0, 0.95, 0.85], np.float32)
    else:
        if not lights: return None
        m = np.full((LH, LW, 3), 1.0, np.float32)
        for X, Y, R, inten, col in lights: m += inten * 0.35 * glow(X, Y, R)[..., None] * np.array(col, np.float32)
        return Image.fromarray((np.clip(m / 1.15, 0, 1) * 255).astype(np.uint8), "RGB").resize((W, H), Image.BILINEAR)
    for X, Y, R, inten, col in lights:
        m += inten * glow(X, Y, R)[..., None] * np.array(col, np.float32)
    lm = np.clip(m / 1.4, 0, 1)
    return Image.fromarray((lm * 255).astype(np.uint8), "RGB").resize((W, H), Image.BILINEAR)

def keytag(d, X, Y, S, label_img, img):
    """big old key with a tin tag; the year is rusted away"""
    d.ellipse([X - 60 * S, Y - 60 * S, X + 60 * S, Y + 60 * S], outline=(200, 160, 60, 255), width=max(2, int(16 * S)))
    d.rectangle([X + 50 * S, Y - 10 * S, X + 330 * S, Y + 10 * S], fill=(200, 160, 60, 255))
    for bx in (260, 300): d.rectangle([X + bx * S, Y + 10 * S, X + (bx + 22) * S, Y + 48 * S], fill=(200, 160, 60, 255))
    tx, ty = X - 40 * S, Y + 120 * S
    d.line([(X, Y + 50 * S), (tx + 120 * S, ty)], fill=(80, 70, 60, 255), width=max(1, int(4 * S)))
    d.rounded_rectangle([tx - 30 * S, ty, tx + 330 * S, ty + 150 * S], int(12 * S), fill=(176, 170, 160, 255), outline=(90, 80, 70, 255), width=max(1, int(4 * S)))
    text(img, tx + 150 * S, ty + 48 * S, "تسجيلات عمارة نعناعة", int(30 * S), (60, 40, 20), (176, 170, 160), 1)
    text(img, tx + 150 * S, ty + 108 * S, "19", int(40 * S), (60, 40, 20), (176, 170, 160), 1)
    for i in range(10):   # rust blotch over the last two digits
        rx, ry = tx + (176 + (i % 4) * 20) * S, ty + (92 + (i // 4) * 14) * S
        d.ellipse([rx - 18 * S, ry - 12 * S, rx + 18 * S, ry + 12 * S], fill=(140, 80, 40, 235))

def props(img, set_, tt, cam, sh):
    x0, y0, z = cam; S = SS * z; d = ImageDraw.Draw(img, "RGBA")
    W2 = lambda wx, wy: ((wx - x0) * S, (wy - y0) * S)
    lw = lambda v: max(1, int(v * S))
    if set_ == "wall_n":
        if tt < FALL + 0.2:   # torch beam on the wall
            ax, ay = W2(AB1[0] - 80, 760) if tt >= AWALK[1] else W2(lerp(AB0[0], AB1[0], ease(kk(tt, *AWALK))) - 80, 760)
            tx_, ty_ = W2(725 + math.sin(tt * 2) * 40, 640)
            beam = Image.new("RGBA", img.size, (0, 0, 0, 0)); bd = ImageDraw.Draw(beam)
            bd.polygon([(ax, ay - 8 * S), (tx_ - 60 * S, ty_ - 45 * S), (tx_ + 60 * S, ty_ + 45 * S), (ax, ay + 8 * S)], fill=(255, 245, 200, 35))
            bd.ellipse([tx_ - 70 * S, ty_ - 52 * S, tx_ + 70 * S, ty_ + 52 * S], fill=(255, 245, 210, 45))
            beam = beam.filter(ImageFilter.GaussianBlur(int(6 * S))); img.paste(beam, (0, 0), beam)
        if tt >= EYES and tt < RUN[1] + 0.5:   # red eyes behind the bars
            on = ease(kk(tt, EYES, EYES + 0.15)) * (0.85 + 0.15 * math.sin(tt * 9))
            for ex in (690, 760):
                X, Y = W2(ex, 650)
                for r_, a_ in ((26, 60), (14, 130), (7, 255)): d.ellipse([X - r_ * S, Y - r_ * 0.7 * S, X + r_ * S, Y + r_ * 0.7 * S], fill=(255, 40, 30, int(a_ * on)))
    if set_ == "stairs":
        sh_ = shot_at(tt); n = 2 + sh_.get("floor", 0) + (1 if sh_.get("floor", 0) >= 2 else 0) + (1 if sh_.get("floor", 0) >= 3 else 0)
        n = [2, 4, 6, 7][sh_.get("floor", 0)]
        X, Y = W2(1700, 160); r = 80 * S
        d.ellipse([X - r, Y - r, X + r, Y + r], fill=(255, 214, 90, 230), outline=(40, 20, 10, 255), width=lw(5))
        text(img, X, Y - 10 * S, str(n), int(90 * S), (40, 20, 10), (255, 214, 90), 2)
        text(img, X, Y + 52 * S, "الدور", int(26 * S), (40, 20, 10), (255, 214, 90), 1)
    if set_ == "roof":
        if sh.get("boxins"):
            img.paste((40, 34, 28), [0, 0, img.size[0], img.size[1]])
            u = ease(kk(tt, sh["start"], sh["start"] + 0.6))
            cx, cy = img.size[0] / 2, img.size[1] / 2 + 60 * SS
            if sh.get("keyzoom"):
                keytag(d, cx - 160 * SS, cy - 160 * SS, 1.7 * SS, None, img)
            else:
                d.rounded_rectangle([cx - 420 * SS, cy - 160 * SS, cx + 420 * SS, cy + 260 * SS], int(20 * SS), fill=(150, 156, 162, 255), outline=(60, 60, 64, 255), width=int(8 * SS))
                lid = 1 - u
                d.polygon([(cx - 430 * SS, cy - 160 * SS), (cx + 430 * SS, cy - 160 * SS), (cx + 430 * SS, cy - 160 * SS - 300 * SS * u), (cx - 430 * SS, cy - 160 * SS - 300 * SS * u)], fill=(170, 176, 182, 255), outline=(60, 60, 64, 255))
                if u > 0.5:
                    keytag(d, cx - 250 * SS, cy - 20 * SS, 0.9 * SS, None, img)
                    d.rectangle([cx + 120 * SS, cy - 100 * SS, cx + 360 * SS, cy + 200 * SS], fill=(230, 220, 190, 255), outline=(90, 70, 40, 255), width=int(5 * SS))
                    d.rectangle([cx + 140 * SS, cy - 80 * SS, cx + 340 * SS, cy + 120 * SS], fill=(150, 120, 80, 255))
                    for i, (px, py) in enumerate(((190, 40), (290, 40))):   # two silhouettes in the old photo (Roshdy + Nana)
                        d.ellipse([cx + (px - 26) * SS, cy + (py - 50) * SS, cx + (px + 26) * SS, cy + (py + 2) * SS], fill=(90, 60, 35, 255))
                        d.rectangle([cx + (px - 22) * SS, cy + (py + 4) * SS, cx + (px + 22) * SS, cy + 115 * SS], fill=(90, 60, 35, 255))
            return
        if sh.get("keyins2"):   # Nana's POV: the key in Tota's hand
            img.paste((70, 60, 50), [0, 0, img.size[0], img.size[1]])
            cx, cy = img.size[0] / 2, img.size[1] / 2
            d.line([(cx + 600 * SS, cy + 700 * SS), (cx - 60 * SS, cy - 60 * SS)], fill=(22, 22, 22, 255), width=int(22 * SS))
            d.ellipse([cx - 90 * SS, cy - 90 * SS, cx - 30 * SS, cy - 30 * SS], fill=(22, 22, 22, 255))
            keytag(d, cx - 120 * SS, cy - 80 * SS, 1.3 * SS, None, img)
            return
        # the tin box sits on the tank top until Shatta grabs it
        if tt < T("H10") + DUR["H10"] * 0.3:
            X, Y = W2(TANK[0] + 60, 300)
            d.rectangle([X - 30 * S, Y - 20 * S, X + 30 * S, Y + 6 * S], fill=(150, 156, 162, 255), outline=(50, 50, 55, 255), width=lw(3))
            d.line([(X - 30 * S, Y - 20 * S), (X - 70 * S, Y - 120 * S)], fill=(150, 120, 80, 255), width=lw(3))
    if set_ == "flash":
        if sh.get("calins") or True:   # wall calendar (the clue)
            X, Y = W2(*CAL)
            d.rectangle([X - 70 * S, Y - 90 * S, X + 70 * S, Y + 90 * S], fill=(240, 232, 210, 255), outline=(60, 40, 20, 255), width=lw(3))
            d.rectangle([X - 70 * S, Y - 90 * S, X + 70 * S, Y - 50 * S], fill=(170, 40, 40, 255))
            text(img, X, Y - 70 * S, "يناير", int(22 * S), (255, 255, 255), (120, 20, 20), 1)
            ltr(img, X, Y + 10 * S, "1958", int(46 * S), (40, 30, 20), (240, 232, 210), 1)
            for i in range(3): d.line([(X - 50 * S, Y + (50 + i * 12) * S), (X + 50 * S, Y + (50 + i * 12) * S)], fill=(120, 110, 90, 255), width=lw(2))
        # the singer at the microphone: dark silhouette in a spotlight
        X, Y = W2(SINGER[0], SINGER[1])
        spot = Image.new("RGBA", img.size, (0, 0, 0, 0)); sd = ImageDraw.Draw(spot)
        sd.polygon([(X - 40 * S, -10), (X + 40 * S, -10), (X + 260 * S, Y + 20 * S), (X - 260 * S, Y + 20 * S)], fill=(255, 245, 210, 70))
        spot = spot.filter(ImageFilter.GaussianBlur(int(10 * S))); img.paste(spot, (0, 0), spot)
        s_ = SINGER[2] * S / SS
        tmp = Image.new("RGBA", img.size, (0, 0, 0, 0)); tp = P(tmp)
        draw_char(tp, "youngnana", X / SS, Y / SS, SINGER[2] * 1.15 * z, "happy", 0.4 + 0.3 * math.sin(tt * 6), 0, False, "talk", tt)
        gs = SINGER[2] * 1.15 * z * CH["youngnana"]["scale"]; gx, gy = X / SS, Y / SS
        tp.poly([(gx - 30 * gs, gy - 130 * gs), (gx + 30 * gs, gy - 130 * gs), (gx + 70 * gs, gy + 4 * gs), (gx - 70 * gs, gy + 4 * gs)], (0, 0, 0, 255), None)
        tp.ell(gx - 34 * gs, gy - 228 * gs, 12 * gs, 12 * gs, (0, 0, 0, 255), None)   # flower in the hair
        al = tmp.getchannel("A"); dark = Image.new("RGBA", img.size, (25, 18, 14, 255)); dark.putalpha(al)
        img.paste(dark, (0, 0), dark)
        d.line([W2(SINGER[0] + 70, SINGER[1] - 250), W2(SINGER[0] + 70, SINGER[1])], fill=(30, 30, 30, 255), width=lw(5))
        mx, my = W2(SINGER[0] + 70, SINGER[1] - 260); d.ellipse([mx - 16 * S, my - 24 * S, mx + 16 * S, my + 24 * S], fill=(120, 120, 125, 255), outline=(30, 30, 30, 255), width=lw(3))
        # workbench in front of young Roshdy
        bx, by = W2(1300, 960)
        d.rectangle([bx - 150 * S, by - 10 * S, bx + 150 * S, by + 10 * S], fill=(110, 70, 40, 255))
    if set_ == "lobby" and tt >= TLN[0]:
        # street door: closed leaf until it opens; fog in the doorway
        l0 = W2(754, 180); l1 = W2(864, 600)
        op = ease(kk(tt, DOPEN, DOPEN + 0.9)) if tt >= DOPEN else 0
        wdt = (l1[0] - l0[0]) * (1 - op)
        if wdt > 1:
            d.rectangle([l0[0], l0[1], l0[0] + wdt, l1[1]], fill=(40, 30, 22, 255), outline=(15, 10, 8, 255), width=lw(3))
        if tt >= DOPEN:
            fog = Image.new("RGBA", img.size, (0, 0, 0, 0)); fd = ImageDraw.Draw(fog)
            for i in range(14):
                u = ((tt - DOPEN) * 0.25 + i / 14) % 1
                X, Y = W2(ENTR[0] + math.sin(i * 2.1 + tt * 0.5) * 140, 600 - i * 18 + u * 40)
                r = (70 + 50 * u) * S
                fd.ellipse([X - r, Y - r * 0.45, X + r, Y + r * 0.45], fill=(220, 225, 235, int(28 * (1 - u))))
            fog = fog.filter(ImageFilter.GaussianBlur(int(18 * S))); img.paste(fog, (0, 0), fog)
        if KNOCK <= tt < KNOCK + 1.2 or BWALK[1] - 0.4 <= tt < BWALK[1] + 0.6:   # the door shakes with each knock
            pass

def ltr(img, x, y, s, size, fill, stroke=(10, 10, 10), sw=3):
    ImageDraw.Draw(img).text((x, y), s, font=ImageFont.truetype(FONT, size), fill=fill, anchor="mm", direction="ltr", stroke_width=sw, stroke_fill=stroke)

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
    return ImageChops.multiply(im, VIG_DARK)

FOLLOW = {k: Image.open(ROOT + f"/brand/follow/{k}.png").convert("RGB") for k in ("yt", "tt", "ig", "fb")}
BTN = {"yt": ((25, 414, 551, 477), "Subscribed", (230, 230, 230), (20, 20, 20)),
       "tt": ((18, 269, 244, 336), "Following", (235, 235, 235), (30, 30, 30)),
       "ig": ((19, 351, 252, 403), "Following", (239, 239, 239), (20, 20, 20)),
       "fb": ((19, 659, 281, 716), "متابَع ✓", (228, 230, 235), (20, 20, 20))}
def phone_card(tt, sh, plat="yt", CW_=W, CH_=H):
    fr = Image.new("RGB", (CW_, CH_), (0, 0, 0))
    bgc = bg_crop(SRC["roof"], (500, 63, 1.6), True).resize((W, H))
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
        text(fr, W / 2, H / 2 - 230, "الحلقة 7 بكرة: فهمي التايب", 96, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 - 100, "الأغنية اتسجلت سنة كام؟ اكتبوها في الكومنتات", 52, g((235, 235, 235)))
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
    if T("H06") + 1.4 <= tt < T("H06") + DUR["H06"] + 1.0:
        d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([cx - 470 * sc, y - 50 * sc, cx + 470 * sc, y + 50 * sc], int(22 * sc), fill=(20, 60, 30, 220), outline=(120, 230, 120, 255), width=4)
        text(fr, cx, y, "إجابة امبارح: خزان المية ✓", int(42 * sc), (200, 255, 200))
    if T("H08") + DUR["H08"] * 0.4 <= tt < T("H08") + DUR["H08"] + 0.3:
        d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([cx - 160 * sc, y - 50 * sc, cx + 160 * sc, y + 50 * sc], int(22 * sc), fill=(60, 20, 20, 220), outline=(255, 120, 90, 255), width=4)
        ltr(fr, cx, y, "10%", int(56 * sc), (255, 160, 120))
    if FB[0] + 0.3 <= tt < FB[0] + 2.8:
        d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([cx - 220 * sc, y - 46 * sc, cx + 220 * sc, y + 46 * sc], int(20 * sc), fill=(40, 28, 16, 210), outline=(230, 200, 140, 255), width=3)
        text(fr, cx, y, "زمان...", int(44 * sc), (240, 220, 180))

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

PUZ_TXT = "لغز النهارده: «أغنية العمارة» اتسجلت سنة كام؟ ركزوا في الفلاش باك!"
def finish_v(fr, tt):
    a = np.asarray(fr, np.float32); return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
def vertical(fr, tt, plat="tt"):
    sh = shot_at(tt)
    if sh["set"] == "phone":
        bgv = finish_v(phone_card(tt, sh, plat, 1080, 1920), tt)
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
    if PUZ <= tt < PUZ_END:
        d.rounded_rectangle([30, 1630, 1050, 1830], 26, fill=(20, 20, 30), outline=(255, 214, 90), width=5)
        for i, l in enumerate(wrap(PUZ_TXT, 34)[:2]): text(bgv, 540, 1680 + i * 56, l, 42, (255, 214, 90))
        text(bgv, 540, 1795, "اكتب في الكومنتات", 40)
    return bgv

def finish(fr, tt, dark=False):
    fr = ImageChops.multiply(fr, VIG_DARK if dark else VIG)
    a = np.asarray(fr, np.float32)
    g = GRAIN[int(tt * 6) % len(GRAIN)]
    g = np.repeat(np.repeat(g, 4, 0), 4, 1)[..., None]
    return Image.fromarray(np.clip(a + g, 0, 255).astype(np.uint8))

TINT = {"studio": (255, 232, 205), "wall_n": (140, 155, 210), "carin": (150, 160, 200), "stairs": (255, 238, 210),
        "roof": (255, 246, 228), "flash": (255, 240, 215)}
def frame(tt, plat="yt"):
    sh = shot_at(tt); set_ = sh["set"]
    if set_ in ("title", "endcard"): return finish(card(set_, tt, sh), tt)
    if set_ == "black": return Image.new("RGB", (W, H), (0, 0, 0))
    if set_ == "phone": return finish(phone_card(tt, sh, plat), tt)
    if sh.get("boxins") or sh.get("keyins2"):
        img = Image.new("RGB", (SSW, SSH), (0, 0, 0)); props(img, set_, tt, (0, 0, 1), sh)
        return finish(img.resize((W, H), Image.LANCZOS), tt, True)
    cam = cam_at(sh, tt)
    img = bg_frame(set_, cam, sh, tt)
    layer, lights = draw_scene_chars(set_, tt, cam, sh)
    if set_ == "lobby":
        d = tod(sh, tt); tint = tuple(int(lerp(a, b, d)) for a, b in zip((150, 165, 225), (255, 246, 228)))
    else: tint = TINT.get(set_, (255, 244, 225))
    layer = tint_layer(layer, tint, 0.97)
    if set_ == "flash": props(img, set_, tt, cam, sh)
    img.paste(layer, (0, 0), layer)
    if set_ != "flash": props(img, set_, tt, cam, sh)
    if set_ == "carin":
        x0, y0, z = cam; ys = int((870 - y0) * z * SS)
        if ys < SSH:
            bgc = bg_crop(SRC["carin"], cam, True); img.paste(bgc.crop((0, ys, SSW, SSH)), (0, ys))
    if set_ == "wall_n":
        x0, y0, z = cam; ys = int((905 - y0) * z * SS)
        if ys < SSH:
            bgc = bg_crop(SRC["wall_n"], cam, False); img.paste(bgc.crop((0, ys, SSW, SSH)), (0, ys))
    fr = img.resize((W, H), Image.LANCZOS)
    if sh.get("low") and set_ == "roof": pass
    lm = light_map(set_, sh, tt, cam, lights)
    dark = set_ in ("wall_n", "carin") or (set_ == "lobby" and tod(sh, tt) < 0.5)
    if lm is not None:
        fr = ImageChops.multiply(fr, lm)
        if set_ == "wall_n": fr = ImageEnhance.Brightness(fr).enhance(1.6)
        if set_ == "lobby": fr = ImageEnhance.Brightness(fr).enhance(lerp(1.7, 1.0, tod(sh, tt)))
    if set_ == "flash": return finish(sepia(fr, tt), tt)
    return finish(fr, tt, dark)

def lowpass(x, fc):
    from numpy.fft import rfft, irfft
    X = rfft(x); fq = np.fft.rfftfreq(len(x), 1 / SR); X[fq > fc] *= 0.12; return irfft(X, len(x)).astype(np.float32)

def build_audio(path="mix.wav"):
    buf = np.zeros(int(TOTAL * SR) + SR * 3, dtype=np.float32)
    dr = drone(TOTAL + 1); env = np.zeros(len(dr), np.float32)
    for a_, b_ in ((0, TITLE), (TLN[0], TOTAL - 4.4)):
        env[int(a_ * SR):int(b_ * SR)] = 1.0
    env = np.convolve(env, np.ones(4410) / 4410, mode="same")
    mix_into(buf, dr * env, 0, 1.2)
    r = np.random.default_rng(9)
    S = {"boom": sfx_boom(), **SFXF}
    for t0, nme, g in sfx:
        if nme in S and g > 0: mix_into(buf, S[nme], t0, g)
    # the song: soft from the flashback start, under the lines, out at the end of the flashback
    a_, b_ = FB[0] + 0.2, FB[1] + 0.3
    n = int((b_ - a_) * SR); song = SONGA[int(8.0 * SR): int(8.0 * SR) + n]
    if len(song) < n: song = np.pad(song, (0, n - len(song)))
    e = np.ones(n, np.float32); fi = int(0.6 * SR); e[:fi] = np.linspace(0, 1, fi); e[-fi:] = np.linspace(1, 0, fi)
    duck = np.ones(n, np.float32)
    for st, k in lines:
        if a_ <= st < b_:
            i0 = int((st - a_) * SR); i1 = min(n, int((st + DUR[k] - a_) * SR))
            duck[max(0, i0 - 4000):i1 + 4000] = 0.35
    duck = np.convolve(duck, np.ones(4410) / 4410, mode="same")
    mix_into(buf, lowpass(song.astype(np.float32), 5000) * e * duck, a_, 0.55)
    # comic stings: the stairs gag, the slip, the 10%
    for t_, notes in ((T("H07") + DUR["H07"] - 0.3, [392, 370, 349, 330]), (SLIP + 0.1, [660, 440, 330]), (T("H05") + 0.4, [523, 494, 440, 392])):
        for i, f in enumerate(notes):
            tt_ = np.arange(int(SR * 0.4)) / SR
            mix_into(buf, np.sin(2 * np.pi * f * tt_) * np.exp(-tt_ * 12) * 0.09, t_ + i * 0.2, 1.0)
    # light morning music box on the roof
    for i in range(int((T("H11") - RIN[0]) / 0.5)):
        f = [523, 659, 784, 659][i % 4]; tb = np.arange(int(SR * 0.45)) / SR
        mix_into(buf, np.sin(2 * np.pi * f * tb) * np.exp(-tb * 6) * 0.03, RIN[0] + i * 0.5, 1.0)
    # tension string under the night knocks → reveal
    a_, b_ = TLN[1], TOTAL - 4.4
    ts = np.arange(int((b_ - a_) * SR)) / SR
    rise = (np.sin(2 * np.pi * (98 + 30 * ts / ts[-1]) * ts) + 0.5 * np.sin(2 * np.pi * (147 + 45 * ts / ts[-1]) * ts)) * 0.04 * np.minimum(1, ts / 2)
    mix_into(buf, rise, a_, 1.0)
    # wind on the roof (day)
    n = int((FB[0] - RIN[0]) * SR); wind = np.convolve(r.normal(0, 1, n), np.ones(200) / 200, mode="same").astype(np.float32) * 0.05
    mix_into(buf, wind, RIN[0], 1.0)
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

def puzzle_h(h, tt):
    if PUZ <= tt < PUZ_END:
        d = ImageDraw.Draw(h, "RGBA")
        d.rounded_rectangle([W / 2 - 760, 50, W / 2 + 760, 185], 24, fill=(20, 20, 30, 215), outline=(255, 214, 90, 255), width=4)
        text(h, W / 2, 117, PUZ_TXT, 38, (255, 214, 90))

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
        h = base.copy(); hud(h, tt); puzzle_h(h, tt); subtitle(h, tt)
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
        for s_ in shots: print(s_["set"], round(s_["start"], 2), round(s_["end"], 2))
        for st, k in lines: print(k, round(st, 2))
    elif sys.argv[1:2] == ["part"]:
        i, n = int(sys.argv[2]), int(sys.argv[3]); a = round(TOTAL * i / n * FPS) / FPS; b = round(TOTAL * (i + 1) / n * FPS) / FPS
        render(f"h_{i}.mp4", f"v_{i}.mp4", None, a, b)
    elif sys.argv[1:2] == ["audio"]:
        build_audio()
    elif sys.argv[1:2] == ["phones"]:
        render_phone_variants()
