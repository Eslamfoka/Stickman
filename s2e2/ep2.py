import sys, os, math, subprocess, wave
sys.path.insert(0, "/home/claude/s1e1")
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter, ImageFont
from engine import *

os.chdir("/home/claude/s2e2")
SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(202)
SEASON = "سر البدروم"
EPT = "الحلقة 2: الصوت اللي تحت الأرض"

SUB = {
 "C01": "لو سامعين صوتي... يبقى اللعبة ابتدت.",
 "C02": "الصوت جاي من الفتحة دي!",
 "C03": "أول رقم: سبعة. دوروا على السبعة اللي بتستنى الجوابات.",
 "C04": "ده... صوت عم رشدي تاني!",
 "C05": "كل واحد يطلع على شقته... حالاً!",
 "C06": "لغز امبارح: مين اللي غير القفل؟... الإجابة هتصدمكو!",
 "C07": "صباح الفل يا ولاد!... إيه، مالكو بتبصولي كده؟",
 "C08": "يا عم... إنت اللي غيرت القفل بتاع البدروم؟",
 "C09": "أيوه أنا! القديم كان مصدي... بس المفتاح الجديد... ضاع برضه.",
 "C10": "يعني مفيش حد معاه مفتاح... طب مين اللي جوه؟!",
 "C11": "الاحتمالات بتقل... والخوف بيزيد.",
 "C12": "الفتحة دي... بتودي على البدروم على طول.",
 "C13": "مفيش صوت... ولا حاجة.",
 "C14": "يا ماما!",
 "C15": "فيه حد تحت... حتى بالنهار!",
 "C16": "أنا هسيب الموبايل هنا... يسجل طول الليل.",
 "C17": "لغز النهارده: إيه هي السبعة اللي بتستنى الجوابات؟ اكتبوا في الكومنتات!",
 "C18": "(لاسلكي) شطة... سامعني؟ حول.",
 "C19": "سامعك... مش عارف أنام. حول.",
 "C20": "(لاسلكي) الساعة قربت على اتناشر... والموبايل لسه بيسجل. حول.",
 "C21": "استنى... فيه عربية واقفة تحت!",
 "C22": "(لاسلكي) شطة؟... رد عليا! حول!",
 "C23": "العمارة دي... هاخدها... ولو بالعافية.",
 "C24": "هو... شافني!",
 "D01": "سبعة... ممكن تكون رقم شقة... أو رقم دور.",
 "D02": "أو سبع عفاريت ساكنين تحت!",
 "D03": "يا شطة! مفيش حاجة اسمها عفاريت.",
 "D04": "(لاسلكي) شطة... إنت سامع المزيكا؟ رجعت تاني! حول.",
 "D05": "أيوه يا عبده... الولاد ابتدوا يدوروا. لازم نسبقهم.",
}
WHO = {"C01": "tape", "C02": "tota", "C03": "tape", "C04": "shatta", "C05": "nana", "C06": "tota", "C07": "bondo2", "C08": "zalata",
       "C09": "bondo2", "C10": "shatta", "C11": "zalata", "C12": "tota", "C13": "shatta", "C14": "shatta", "C15": "zalata", "C16": "tota",
       "C17": "tota", "C18": "radio", "C19": "shatta", "C20": "radio", "C21": "shatta", "C22": "radio", "C23": "pasha", "C24": "shatta", "D01": "zalata", "D02": "shatta", "D03": "tota", "D04": "radio", "D05": "pasha"}
EXPR = {"D01": "flat", "D02": "scared", "D03": "angry", "C02": "shock", "C04": "scared", "C05": "angry", "C06": [(0, "smug"), (0.6, "happy")], "C07": [(0, "happy"), (0.55, "neutral")],
        "C08": "flat", "C09": [(0, "smug"), (0.45, "sad")], "C10": "scared", "C11": "flat", "C12": "neutral", "C13": "neutral",
        "C14": "shock", "C15": "scared", "C16": "smug", "C17": [(0, "neutral"), (0.6, "smug")], "C19": "sad", "C21": "shock", "C24": "shock"}
ARMS = {"D01": "hold", "D02": "scared", "D03": "hips", "C02": "point", "C04": "scared", "C05": "up", "C06": "point", "C07": "hold", "C08": "point", "C09": "hips", "C10": "scared",
        "C11": "hold", "C12": "point", "C13": "down", "C14": "scared", "C15": "scared", "C16": "point", "C17": "point", "C19": "hold",
        "C21": "hold", "C24": "scared"}

def _aud(k):
    f = f"audio/{k}_fx.mp3"
    return load_audio(f if os.path.exists(f) else f"audio/{k}.mp3")
AUD = {k: _aud(k) for k in SUB}
ENV = {k: envelope(v) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}
SFXF = {n: load_audio(f"sfx/{n}.mp3") for n in ("whoosh", "creak", "slam", "switch", "steps_metal", "wind", "morning", "snore", "walkie", "car", "clang")}

lines, sfx, shots, jumps, shakes = [], [], [], {}, []
def say(t, k): lines.append((t, k)); return t + DUR[k]
def fx(t, n, g=1.0): sfx.append((t, n, g))
def jump(w, t): jumps.setdefault(w, []).append(t)
def shot(set_, s, e, c0, c1=None, **kw): shots.append(dict(set=set_, start=s, end=e, c0=c0, c1=c1 or c0, **kw))
def cut(t, g=0.4): fx(t - 0.12, "whoosh", g)
def T(k): return [st for st, kk_ in lines if kk_ == k][0]
KIDS = ("shatta", "zalata", "tota")

# ---------------- world (lobby = morning.png, 1920x1080 coords) ----------------
DOOR = (1545, 495, 1830, 938)
VENT = (1402, 812, 1512, 872)
VC = ((VENT[0] + VENT[2]) / 2, (VENT[1] + VENT[3]) / 2)
MAIL7 = (205, 300)
ENTR = (745, 600)          # feet position in the street doorway (far)
NIT = {"zalata": (980, 1040, 2.0), "tota": (1140, 1040, 2.0), "shatta": (1480, 1040, 2.0)}
NANA_N = (760, 1040, 2.1)
DAY = {"tota": (980, 1040, 1.95), "shatta": (1180, 1040, 1.95), "zalata": (1380, 1040, 1.95)}
VSPOT = {"zalata": (880, 1040, 1.95), "shatta": (1090, 1040, 1.95), "tota": (1290, 1040, 1.95)}
BONDO_IN = (620, 1040, 1.95)
BENCH = (300, 1000, 1.85)
BED = {"shatta": (1050, 1010, 1.9)}
WIN_SH = (430, 560, 1.15)

def CU(who, pos, z=2.2, dx=0):
    x, y, s = pos; S = s * CH[who]["scale"]
    if who == "tota": z *= 1.3; dx -= 50
    hy = y - 190 * S
    return (x + dx, hy + H / (2 * z) - 1.45 * 46 * S - 25, z)

t = 0.0
# ===== 0. COLD OPEN — same second Ep1 ended =====
RED_OFF = 0.7; fx(RED_OFF, "switch", 1.0)
for w_ in KIDS + ("nana",): jump(w_, RED_OFF + 0.05)
shot("lobby", 0, 1.8, (1300, 660, 1.3), (1330, 670, 1.38), tod=0)
STATIC0 = 1.5
cut(1.8, 0.5); s = 1.8; t = say(2.1, "C01") + 0.2
shot("lobby", s, t, (VC[0], VC[1] - 60, 2.6), (VC[0], VC[1] - 40, 3.4), ease="crash", tod=0, ventcu=True)
s = t; t = say(t + 0.05, "C02") + 0.1
shot("lobby", s, t, CU("tota", NIT["tota"], 1.6), CU("tota", NIT["tota"], 1.85), tod=0)
s = t; t = say(t + 0.1, "C03") + 0.2
shot("lobby", s, t, (VC[0], VC[1] - 40, 3.0), (VC[0], VC[1] - 30, 3.6), tod=0, ventcu=True)
TAPE_STOP = t; fx(t, "switch", 0.7); STATIC1 = t
s = t; t = say(t + 0.5, "C04") + 0.1
shot("lobby", s, t, CU("shatta", NIT["shatta"], 1.8), CU("shatta", NIT["shatta"], 2.3), ease="crash", tod=0)
s = t; t = say(t, "C05") + 0.1
shot("lobby", s, t, CU("nana", NANA_N, 1.7), CU("nana", NANA_N, 2.0), tod=0)
EXIT = (t, t + 3.4)
shot("lobby", t, EXIT[1], (900, 640, 1.15), (860, 640, 1.18), tod=0, exitnight=True); t = EXIT[1]
fx(t - 0.3, "whoosh", 0.6); shot("title", t, t + 2.0, None); TITLE = t; t += 2.0
# ===== 1. MORNING (time-lapse in the same lobby) =====
TL1 = (t, t + 3.4); fx(t + 0.2, "morning", 0.9)
shot("lobby", t, TL1[1], (820, 560, 1.12), (760, 540, 1.2), tl=(0, 1, TL1)); t = TL1[1]
GLINT = TL1[1] - 0.8
KIN = (t, t + 1.9)
shot("lobby", t, KIN[1], (820, 600, 1.15), (900, 620, 1.2), tod=1); t = KIN[1]
s = t; t = say(t + 0.1, "C06") + 0.15
shot("lobby", s, t, CU("tota", DAY["tota"], 1.55), CU("tota", DAY["tota"], 1.75), tod=1)
s = t; t = say(t + 0.1, "D01") + 0.1
shot("lobby", s, t, CU("zalata", DAY["zalata"], 1.8), CU("zalata", DAY["zalata"], 2.0), tod=1)
s = t; t = say(t, "D02") + 0.1
shot("lobby", s, t, CU("shatta", DAY["shatta"], 1.8), CU("shatta", DAY["shatta"], 2.4), ease="crash", tod=1)
s = t; t = say(t, "D03") + 0.2
shot("lobby", s, t, (1080, 640, 1.4), (1080, 650, 1.5), tod=1)
BIN = (t, t + 3.0); fx(t + 0.1, "creak", 0.8)
shot("lobby", t, BIN[1], (760, 560, 1.55), (700, 640, 1.25), tod=1); t = BIN[1]
s = t; t = say(t, "C07") + 0.1
shot("lobby", s, t, CU("bondo2", BONDO_IN, 1.8), CU("bondo2", BONDO_IN, 2.1), tod=1)
s = t; t = say(t, "C08") + 0.1
shot("lobby", s, t, CU("zalata", DAY["zalata"], 1.8), CU("zalata", DAY["zalata"], 2.1), tod=1)
s = t; C09_T = t; t = say(t, "C09") + 0.15
shot("lobby", s, t, CU("bondo2", BONDO_IN, 2.0), CU("bondo2", BONDO_IN, 2.3), tod=1)
s = t; t = say(t, "C10") + 0.1
shot("lobby", s, t, CU("shatta", DAY["shatta"], 1.8), CU("shatta", DAY["shatta"], 2.4), ease="crash", tod=1)
BTB = (t, t + 2.2)
s = t; t = say(t + 0.4, "C11") + 0.4; SNORE = BTB[1] + 0.1; fx(SNORE, "snore", 1.0)
t = max(t, SNORE + 1.2)
shot("lobby", s, t, (900, 620, 1.2), (820, 640, 1.25), tod=1)
# ===== 2. THE VENT — follow the kids with a pan =====
KV = (t, t + 1.7)
shot("lobby", t, KV[1], (1050, 640, 1.25), (1300, 700, 1.55), tod=1); t = KV[1]
s = t; t = say(t + 0.1, "C12") + 0.1
shot("lobby", s, t, (VSPOT["tota"][0] + 20, 760, 2.2), (VSPOT["tota"][0] + 40, 770, 2.4), tod=1)
LISTEN = (t, t + 0.8)
s = t; t = say(t + 0.7, "C13") + 0.1
shot("lobby", s, t, (VSPOT["shatta"][0] + 80, 760, 2.2), (VSPOT["shatta"][0] + 100, 780, 2.6), tod=1)
SILENT = (t, t + 2.2)
shot("lobby", t, SILENT[1], (VSPOT["shatta"][0] + 100, 780, 2.6), (VSPOT["shatta"][0] + 120, 790, 3.0), tod=1); t = SILENT[1]
CLANG = t; fx(t, "clang", 1.6); fx(t, "boom", 0.6); shakes.append((t, 16))
for w_ in KIDS: jump(w_, t + 0.05)
s = t; t = say(t + 0.15, "C14") + 0.1
shot("lobby", s, t, (1300, 700, 1.6), (1250, 690, 1.35), ease="crash", tod=1, dust=True)
s = t; t = say(t + 0.1, "C15") + 0.1
shot("lobby", s, t, CU("zalata", VSPOT["zalata"], 1.8), CU("zalata", VSPOT["zalata"], 2.1), tod=1)
s = t; t = say(t + 0.1, "C16") + 0.1; PHONE_IN = s + 0.4 + DUR["C16"] * 0.6
shot("lobby", s, t, (VSPOT["tota"][0] + 40, 790, 2.2), (VSPOT["tota"][0] + 60, 800, 2.5), tod=1)
PUZ = t; s = t; t = say(t + 0.1, "C17") + 0.8; PUZ_END = t
shot("lobby", s, t, CU("tota", VSPOT["tota"], 1.6), CU("tota", VSPOT["tota"], 1.9), tod=1)
# ===== 3. NIGHT =====
cut(t, 0.4); TL2 = (t, t + 3.4)
shot("lobby", t, TL2[1], (VC[0] - 10, VC[1] - 50, 2.4), (VC[0], VC[1] - 40, 3.0), tl=(1, 0, TL2), ventcu=True); t = TL2[1]
fx(t - 0.6, "steps_metal", 0.35)
cut(t, 0.4); BED0 = t
shot("bed", t, t + 3.0, (330, 260, 1.7), CU("shatta", BED["shatta"], 1.5)); t += 3.0
fx(t - 0.25, "walkie", 0.8)
s = t; t = say(t + 0.1, "C18") + 0.2; fx(t - 0.15, "walkie", 0.5)
shot("bed", s, t, CU("shatta", BED["shatta"], 1.6), CU("shatta", BED["shatta"], 1.8))
s = t; t = say(t, "C19") + 0.2
shot("bed", s, t, CU("shatta", BED["shatta"], 1.9), CU("shatta", BED["shatta"], 2.1))
fx(t - 0.2, "walkie", 0.8); s = t; MUSIC2 = t + 0.3; t = say(t + 0.1, "D04") + 0.2; fx(t - 0.15, "walkie", 0.5)
shot("bed", s, t, CU("shatta", BED["shatta"], 1.8), CU("shatta", BED["shatta"], 2.0))
FLOOR = (t, t + 2.4)       # Shatta looks down at the floor, the old music rising faintly from below
shot("bed", t, FLOOR[1], (1050, 820, 1.6), (1050, 860, 1.9)); t = FLOOR[1]
fx(t - 0.2, "walkie", 0.8); s = t; t = say(t + 0.1, "C20") + 0.2; fx(t - 0.15, "walkie", 0.5)
shot("bed", s, t, CU("shatta", BED["shatta"], 1.8), CU("shatta", BED["shatta"], 1.9))
CAR0 = t; fx(t, "car", 1.0)
SWEEP = (t + 0.6, t + 3.2)
shot("bed", t, SWEEP[1], (960, 520, 1.05), (960, 520, 1.1)); t = SWEEP[1]
s = t; t = say(t, "C21") + 0.2
shot("bed", s, t, CU("shatta", BED["shatta"], 1.9), CU("shatta", BED["shatta"], 2.5), ease="crash")
TOWIN = (t, t + 1.4)
shot("bed", t, TOWIN[1], (900, 560, 1.25), (820, 560, 1.3)); t = TOWIN[1]
cut(t, 0.35); shot("bed", t, t + 1.5, (360, 330, 2.3), (350, 320, 2.5), atwin=True); t += 1.5
POV = (t, t + 2.6); shot("win", t, POV[1], (960, 300, 1.12), (770, 620, 1.7)); t = POV[1]
STREET = t; DOOR_OPEN = t + 0.4; FIG_IN = (t + 0.8, t + 1.9)
s = t; t = say(t + 2.6, "C22") + 0.2; fx(s + 2.4, "walkie", 0.8)
shot("street", s, t, (1300, 600, 1.25), (1360, 630, 1.5))
PHONE = (t, t + DUR["D05"] + 0.8)
s = t; t = say(t + 0.3, "D05") + 0.4
shot("street", s, t, (1400, 600, 1.7), (1410, 580, 2.0))
LOOKUP = (t + 0.4, t + 1.8)
s = t; t = say(t + 0.3, "C23") + 0.4
shot("street", s, t, (1420, 560, 2.0), (1430, 500, 3.0))
cut(t, 0.4); DUCK = t + 0.35; s = t; t = say(t + 0.15, "C24") + 0.4
shot("bed", s, t, (360, 330, 2.5), (360, 360, 2.9), atwin=True, ease="crash")
FLASH = [t + 0.2, t + 0.55]
shot("street", t, t + 1.1, (1300, 640, 1.3), (1300, 640, 1.32)); fx(t + 0.2, "boom", 1.0); shakes.append((t + 0.2, 10)); t += 1.1
shot("black", t, t + 0.5, None); t += 0.5
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
for a_, b_, r_, g_ in ((EXIT[0], EXIT[1], 9, 0.5), (KIN[0], KIN[1], 8, 0.45), (BIN[0], BIN[1], 6, 0.5), (BTB[0], BTB[1], 6, 0.45),
                       (KV[0], KV[1], 8, 0.45), (TOWIN[0], TOWIN[1], 7, 0.4)):
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
_mor = Image.open("/home/claude/s1e10/bg/morning.png").convert("RGB")
SRC = {"lobby_day": _mor, "lobby_night": tinted(_mor, 0.9, (150, 165, 230)),
       "bed": Image.open("bg_bedroom.png").convert("RGB"),
       "win": Image.open("/home/claude/s1e9/bg/window.png").convert("RGB"),
       "street": Image.open("/home/claude/s2/bg/street_car.png").convert("RGB")}
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

def bg_crop(src, cam):
    x0, y0, z = cam; sw, sh = src.size; f = sw / W
    box = (x0 * f, y0 * f, (x0 + W / z) * f, (y0 + H / z) * f)
    if z > 1.6:
        b = tuple(int(v) for v in box); b = (max(0, b[0] - 20), max(0, b[1] - 20), min(sw, b[2] + 20), min(sh, b[3] + 20))
        part = src.crop(b).filter(ImageFilter.GaussianBlur(min(3, (z - 1.5) * 1.3)))
        box = (box[0] - b[0], box[1] - b[1], box[2] - b[0], box[3] - b[1]); src = part
    return src.resize((SSW, SSH), Image.BICUBIC, box=box)

def bg_frame(set_, cam, d):
    if set_ == "lobby":
        if d >= 0.999: return bg_crop(SRC["lobby_day"], cam)
        if d <= 0.001: return bg_crop(SRC["lobby_night"], cam)
        return Image.blend(bg_crop(SRC["lobby_night"], cam), bg_crop(SRC["lobby_day"], cam), d)
    return bg_crop(SRC[set_], cam)

def A_(who, pos, **kw):
    x, y, s = pos; d = dict(who=who, x=x, y=y, s=s, look=0, expr="neutral", arms="down"); d.update(kw); return d
def walk_to(a, p0, p1, win, tt, rate=8):
    k = kk(tt, *win); e = ease(k)
    a["x"], a["y"], a["s"] = lerp(p0[0], p1[0], e), lerp(p0[1], p1[1], e), lerp(p0[2], p1[2], e)
    if 0 < k < 1: a["walk"] = tt * rate
    return k

def actors(set_, tt, sh):
    A = []
    if sh.get("ventcu") or set_ in ("win",): return A
    if set_ == "lobby":
        if tt < TITLE:      # night, continuing Ep1
            for who, p_ in NIT.items():
                a = A_(who, p_, look=1, expr="shock" if tt < STATIC0 + 0.5 else "scared")
                if who == "zalata": a["held"] = "torch"; a["arms"] = "hold"
                if who == "shatta": a["look"] = -1 if tt > T("C02") else 1
                if tt >= TAPE_STOP: a["look"] = -1
                if tt >= EXIT[0]:
                    d0 = {"zalata": 0.0, "tota": 0.35, "shatta": 0.7}[who]
                    k = walk_to(a, p_, (-260, p_[1], p_[2]), (EXIT[0] + d0, EXIT[0] + d0 + 2.2), tt, 9)
                    a["look"] = -1; a["expr"] = "scared"
                    if k >= 1: continue
                A.append(a)
            n = A_("nana", NANA_N, look=1, expr="angry", held="lantern", arms="hold")
            if tt >= EXIT[0]:
                n["look"] = 1 if tt < EXIT[0] + 1.2 else -1
                k = walk_to(n, NANA_N, (-260, 1040, 2.1), (EXIT[0] + 1.3, EXIT[1] - 0.1), tt, 8)
                n["expr"] = "sad"
                if k >= 1: n = None
            if n: A.append(n)
            return A
        # ---- day ----
        for who, p_ in DAY.items():
            a = A_(who, p_, look=-1, expr="happy")
            if who == "zalata": a["held"] = "nbpen"; a["arms"] = "hold"; a["expr"] = "flat"
            if tt < KIN[0]: continue
            off = {"tota": 0.0, "shatta": 0.25, "zalata": 0.5}[who]
            walk_to(a, (-240, p_[1], p_[2]), p_, (KIN[0] + off * 0.6, KIN[1] - 0.1 + off * 0.2), tt, 8)
            if tt < KIN[1]: a["look"] = 1
            if tt >= BIN[0]: a["look"] = -1; a["expr"] = "neutral" if who != "zalata" else "flat"
            if tt >= T("C08") and who in ("tota", "shatta"): a["expr"] = "smug"
            if tt >= T("C10"): a["expr"] = "scared"
            if tt >= KV[0]:
                k = walk_to(a, p_, VSPOT[who], KV, tt, 8); a["look"] = 1; a["expr"] = "neutral" if who != "zalata" else "flat"
            if who == "tota" and tt >= KV[1]:
                a["lean"] = 0.9; a["y"] = VSPOT["tota"][1] + 30; a["look"] = 1
                if tt >= T("C17"): a["lean"] = 0.0; a["y"] = VSPOT["tota"][1]; a["look"] = -1
            if who == "tota" and LISTEN[0] <= tt < T("C16"):
                k = kk(tt, *LISTEN); a["x"] = lerp(VSPOT["tota"][0], 1060, ease(k)); a["lean"] = 0.9 * (1 - k); a["y"] = VSPOT["tota"][1] + 30 * (1 - k)
                a["walk"] = tt * 8 if 0 < k < 1 else None
            if who == "tota" and tt >= T("C16") and tt < PUZ:
                k = kk(tt, T("C16"), T("C16") + 0.6); a["x"] = lerp(1060, VSPOT["tota"][0], ease(k)); a["lean"] = 0.9 * k; a["look"] = 1
                a["walk"] = tt * 8 if 0 < k < 1 else None
            if who == "shatta" and tt >= LISTEN[0]:
                k = kk(tt, *LISTEN); a["lean"] = 1.1 * ease(k); a["x"] = lerp(VSPOT["shatta"][0], 1300, ease(k)); a["look"] = 1
                a["walk"] = tt * 8 if 0 < k < 1 else None
                if tt >= CLANG + 0.35: a["x"] = 1180
            if tt >= CLANG:
                kc = kk(tt, CLANG, CLANG + 0.35)
                a["lean"] = lerp(a.get("lean", 0), -0.5, kc) if tt < CLANG + 1.2 else 0
                a["x"] = a["x"] - 60 * ease(kc) if who == "shatta" and tt < CLANG + 0.35 else a["x"]
                a["expr"] = "shock"; a["arms"] = "scared"
                if tt >= T("C16"):
                    if who == "tota": a["expr"] = "smug"; a["arms"] = "down"; a["look"] = 1 if tt < PUZ else -1
                    else: a["expr"] = "scared"; a["arms"] = "down"
                if who == "tota" and tt >= PUZ: a["y"] = VSPOT["tota"][1]; a["lean"] = 0; a["x"] = VSPOT["tota"][0]
            A.append(a)
        # doorman
        if tt >= BIN[0]:
            b = A_("bondo2", BONDO_IN, look=1, expr="happy", held="basket", arms="hold")
            far = (ENTR[0], ENTR[1], 0.72)
            k = walk_to(b, far, BONDO_IN, BIN, tt, 6)
            if k < 1: b["look"] = 0
            if tt >= BTB[0]:
                b["held"] = None; b["arms"] = "down"
                k2 = walk_to(b, BONDO_IN, BENCH, BTB, tt, 6); b["look"] = -1; b["expr"] = "sleepy"
                if k2 >= 1: b["look"] = 1; b["lean"] = -0.25
            A.append(b)
    elif set_ == "bed":
        a = A_("shatta", BED["shatta"], look=-1, expr="sad", arms="hold")
        if FLOOR[0] <= tt < CAR0: a["expr"] = "scared"; a["look"] = 1
        if tt >= CAR0: a["expr"] = "neutral"
        if tt >= SWEEP[0]: a["look"] = 1; a["expr"] = "shock"
        if tt >= T("C21"): a["look"] = -1; a["expr"] = "shock"
        if sh.get("atwin"):
            a = A_("shatta", WIN_SH, look=-1, expr="scared", arms="hold")
            if tt >= DUCK:
                kd = kk(tt, DUCK, DUCK + 0.25); a["y"] = WIN_SH[1] + 170 * ease(kd); a["expr"] = "shock"; a["arms"] = "scared"
            A.append(a); return A
        if tt >= TOWIN[0]:
            k = walk_to(a, BED["shatta"], (-200, 1010, 1.9), TOWIN, tt, 8); a["look"] = -1
            if k >= 1: return A
        A.append(a)
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
def draw_walkie(p, x, y, s, lit):
    p.rect(x - 9 * s, y - 34 * s, x + 9 * s, y + 6 * s, (35, 35, 40, 255), INK, 2 * s, 3 * s)
    p.line([(x + 5 * s, y - 34 * s), (x + 5 * s, y - 56 * s)], INK, 3 * s)
    p.ell(x, y - 26 * s, 3.5 * s, 3.5 * s, (90, 255, 120, 255) if lit else (200, 40, 40, 255), None)
    for i in range(3): p.line([(x - 5 * s, y - 16 * s + i * 5 * s), (x + 5 * s, y - 16 * s + i * 5 * s)], (90, 90, 95, 255), 1.5 * s)

def draw_scene_chars(set_, tt, cam, sh):
    x0, y0, z = cam
    layer = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(layer)
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
        shiver = math.sin(tt * 60) * 2.5 if expr in ("scared", "shock") and who in KIDS else 0
        blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11 and expr != "sleepy"
        X = (a["x"] + shiver - x0) * z; Y = (wy - y0) * z; s = a["s"] * z
        p.ell(X, (a["y"] - y0) * z + 4 * s, 46 * s, 9 * s, (0, 0, 0, 110), None)
        draw_char(p, who, X, Y, s, expr, mouth, a.get("look", 0), blink, arms, tt, a.get("held"), a.get("lean", 0), a.get("walk"))
        S = s * CH[who]["scale"]; hx_, hy_ = HANDS.get(arms, (46, 104))
        hand = (X + hx_ * S * (1 if a.get("look", 0) >= 0 else 1), Y - hy_ * S)
        if set_ == "bed" and who == "shatta" and arms == "hold":
            kk_, _ = line_at(tt); draw_walkie(p, hand[0], hand[1], S, kk_ is not None and WHO[kk_] == "radio")
            lights.append((hand[0], hand[1] - 20 * S, 60 * z, 0.5, (0.5, 1.0, 0.6) if (kk_ and WHO[kk_] == "radio") else (1.0, 0.3, 0.3)))
        h = a.get("held")
        if h == "torch": lights.append((hand[0], hand[1], 320 * z, 1.0, (1.0, 0.96, 0.85)))
        if h == "lantern": lights.append((hand[0], hand[1] + 30 * S, 420 * z, 1.3, (1.0, 0.8, 0.45)))
        if who == "bondo2" and a.get("lean", 0) < 0 and tt > SNORE - 0.2:   # Zzz
            for i in range(3):
                u = ((tt - SNORE) * 0.6 + i / 3) % 1
                text(layer, (X + (40 + 30 * u + i * 6) * S) * SS, (Y - (220 + 140 * u) * S) * SS, "Z", int((26 + 18 * i) * S * SS), (255, 255, 255, int(255 * (1 - u))), sw=2)
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
    if set_ == "lobby":
        m = np.full((LH, LW, 3), 0.44, np.float32) * cool
        X, Y = W3(745, 300); m += 0.3 * glow(X, Y, 380 * z)[..., None] * cool
        if tt < RED_OFF:
            r = 0.75 + 0.25 * math.sin(tt * 6) ** 2
            X, Y = W3(1690, 965); m += 1.1 * r * glow(X, Y, 260 * z)[..., None] * RED
        if sh.get("ventcu") and tt < TITLE:  # Zalata's torch pointed at the vent
            X, Y = W3(VC[0], VC[1] - 10); m += 1.2 * glow(X, Y, 230 * z)[..., None] * np.array([1.0, 0.96, 0.85], np.float32)
        if STATIC0 <= tt < STATIC1:      # faint flicker from the vent while the tape talks
            X, Y = W3(*VC); m += (0.25 + 0.15 * math.sin(tt * 40)) * glow(X, Y, 160 * z)[..., None] * np.array([0.6, 0.7, 1.0], np.float32)
        if tt >= PHONE_IN:
            X, Y = W3(VC[0] - 8, VC[1] + 8); m += (0.5 if int(tt * 2) % 2 else 0.25) * glow(X, Y, 70 * z)[..., None] * np.array([1.0, 0.3, 0.3], np.float32)
    elif set_ == "bed":
        m = np.full((LH, LW, 3), 0.6, np.float32) * cool
        X, Y = W3(300, 200); m += 0.5 * glow(X, Y, 420 * z)[..., None] * np.array([0.7, 0.8, 1.2], np.float32)
        X, Y = W3(1100, 330); m += 0.35 * glow(X, Y, 200 * z)[..., None] * np.array([1.2, 0.9, 0.6], np.float32)   # desk lamp
        if SWEEP[0] <= tt < SWEEP[1]:
            k = ease(kk(tt, *SWEEP)); Xc = W3(lerp(1900, 100, k), 0)[0]
            m += 3.2 * (band(Xc, 170 * z) * np.clip(1 - np.abs(gy - W3(0, 380)[1]) / (380 * z), 0, 1))[..., None] * np.array([1.2, 1.15, 1.0], np.float32)
        if sh.get("atwin"):
            X, Y = W3(330, 380); m += 0.5 * glow(X, Y, 260 * z)[..., None] * np.array([1.2, 0.85, 0.5], np.float32)   # street glow from below
            if tt >= STREET: m += 0.3 * glow(*W3(330, 360), 300 * z)[..., None]
    else:
        m = np.full((LH, LW, 3), 1.0, np.float32)
    for X, Y, R, inten, col in lights:
        m += inten * glow(X, Y, R)[..., None] * np.array(col, np.float32)
    lm = np.clip(m / 1.4, 0, 1)
    if set_ == "lobby": lm = lm * (1 - d) + d       # daylight washes the light map out
    return Image.fromarray((lm * 255).astype(np.uint8), "RGB").resize((W, H), Image.BILINEAR)

def sparkle(d, X, Y, r, a):
    col = (255, 250, 220, a)
    d.polygon([(X, Y - r), (X + r * 0.22, Y - r * 0.22), (X + r, Y), (X + r * 0.22, Y + r * 0.22), (X, Y + r),
               (X - r * 0.22, Y + r * 0.22), (X - r, Y), (X - r * 0.22, Y - r * 0.22)], fill=col)

DUST = rng.uniform(0, 1, (26, 3))
def props(img, set_, tt, cam, sh, d_):
    x0, y0, z = cam; S = SS * z; d = ImageDraw.Draw(img, "RGBA")
    W2 = lambda wx, wy: ((wx - x0) * S, (wy - y0) * S)
    if set_ == "lobby":
        # the new padlock from Ep1 (covers the old one)
        lx, ly = W2(1624, 702); S0 = S; S = S * 1.35
        d.arc([lx - 14 * S, ly - 34 * S, lx + 14 * S, ly - 6 * S], 180, 360, fill=(200, 200, 210, 255), width=max(2, int(5 * S)))
        for sx_ in (-14, 14): d.line([(lx + sx_ * S, ly - 20 * S), (lx + sx_ * S, ly - 6 * S)], fill=(200, 200, 210, 255), width=max(2, int(5 * S)))
        d.rounded_rectangle([lx - 22 * S, ly - 8 * S, lx + 22 * S, ly + 28 * S], int(5 * S), fill=(235, 185, 50, 255), outline=(110, 75, 10, 255), width=max(1, int(2.5 * S)))
        d.ellipse([lx - 4 * S, ly + 4 * S, lx + 4 * S, ly + 12 * S], fill=(60, 40, 5, 255)); S = S0
        # the floor vent (grate)
        a0 = W2(VENT[0], VENT[1]); a1 = W2(VENT[2], VENT[3])
        d.rectangle([a0[0], a0[1], a1[0], a1[1]], fill=(25, 22, 20, 255), outline=(95, 88, 78, 255), width=max(2, int(4 * S)))
        n = 7
        for i in range(1, n):
            xx_ = a0[0] + (a1[0] - a0[0]) * i / n
            d.line([(xx_, a0[1] + 3 * S), (xx_, a1[1] - 3 * S)], fill=(110, 102, 90, 255), width=max(1, int(3 * S)))
        for (bx, by) in ((a0[0] + 5 * S, a0[1] + 5 * S), (a1[0] - 5 * S, a0[1] + 5 * S), (a0[0] + 5 * S, a1[1] - 5 * S), (a1[0] - 5 * S, a1[1] - 5 * S)):
            d.ellipse([bx - 2.5 * S, by - 2.5 * S, bx + 2.5 * S, by + 2.5 * S], fill=(150, 140, 120, 255))
        # tape crackle — tiny sparks of light behind the grate
        if STATIC0 <= tt < STATIC1 and int(tt * 18) % 3 == 0:
            for i in range(3):
                u = (tt * 7 + i * 0.37) % 1; px = a0[0] + (a1[0] - a0[0]) * u
                d.ellipse([px - 2 * S, a0[1] + 20 * S, px + 2 * S, a0[1] + 24 * S], fill=(200, 220, 255, 160))
        # Tota's phone inside the grate
        if tt >= PHONE_IN:
            k = ease(kk(tt, PHONE_IN, PHONE_IN + 0.4)); px, py = W2(VC[0] - 8, VC[1] + 6)
            py += (1 - k) * 40 * S
            d.rounded_rectangle([px - 13 * S, py - 22 * S, px + 13 * S, py + 22 * S], int(4 * S), fill=(20, 20, 24, 255), outline=(70, 70, 80, 255), width=max(1, int(2 * S)))
            d.rectangle([px - 10 * S, py - 18 * S, px + 10 * S, py + 16 * S], fill=(30, 40, 60, 255))
            if int(tt * 2) % 2: d.ellipse([px - 4 * S, py - 4 * S, px + 4 * S, py + 4 * S], fill=(255, 40, 40, 255))
            ImageDraw.Draw(img).text((px, py + 12 * S), "REC", font=ImageFont.truetype(FONT, max(6, int(6 * S))), fill=(255, 90, 90), anchor="mm")
        # dust puff from the vent at the clang
        if sh.get("dust") or (CLANG <= tt < CLANG + 1.6 and set_ == "lobby"):
            u0 = tt - CLANG
            if 0 <= u0 < 1.6:
                for i, (a, b, c) in enumerate(DUST):
                    u = u0 / 1.6
                    px = VC[0] - 60 + a * 120 + (a - 0.5) * 160 * u; py = VC[1] - 10 - b * 40 - 140 * u * (0.6 + c)
                    X, Y = W2(px, py); r_ = (6 + 14 * u + 8 * c) * S
                    d.ellipse([X - r_, Y - r_, X + r_, Y + r_], fill=(190, 180, 160, int(170 * (1 - u))))
        # mailbox 7 easter egg — a single glint at the end of the morning time-lapse
        if GLINT <= tt < GLINT + 0.45:
            mx, my = W2(*MAIL7); u = kk(tt, GLINT, GLINT + 0.45)
            sparkle(d, mx, my, (8 + 22 * math.sin(u * math.pi)) * S, 240)
    elif set_ == "bed":
        if SWEEP[0] <= tt < SWEEP[1]:   # car lights projected through the window bars, sliding across the wall
            k = ease(kk(tt, *SWEEP)); cx_ = lerp(1950, 50, k); al = math.sin(k * math.pi)
            for wdt, aa in ((260, 22), (190, 30), (130, 40)):
                pts = [W2(cx_ - wdt / 2, 60), W2(cx_ + wdt / 2 - 60, 60), W2(cx_ + wdt / 2, 660), W2(cx_ - wdt / 2 + 60, 660)]
                d.polygon(pts, fill=(255, 248, 215, int(aa * al)))
            for i in range(4):     # bar shadows
                bx = cx_ - 90 + i * 60
                d.line([W2(bx, 60), W2(bx + 30, 660)], fill=(0, 0, 0, int(60 * al)), width=max(2, int(10 * S)))
    elif set_ == "win":
        if tt >= POV[0] + 1.0:   # headlights appear down in the alley
            a = int(220 * kk(tt, POV[0] + 1.0, POV[0] + 1.6))
            for ox in (-14, 14):
                X, Y = W2(752 + ox, 650)
                for r_, aa in ((60, a // 6), (26, a // 3), (8, a)):
                    d.ellipse([X - r_ * S, Y - r_ * S, X + r_ * S, Y + r_ * S], fill=(255, 250, 220, aa))
    elif set_ == "street":
        # high beams: flicker and the final double flash
        for fl in FLASH:
            if 0 <= tt - fl < 0.18:
                for (hx, hy) in ((1190, 700), (1352, 702)):
                    X, Y = W2(hx, hy)
                    for r_, aa in ((40, 90), (16, 255)):
                        d.ellipse([X - r_ * S, Y - r_ * S, X + r_ * S, Y + r_ * S], fill=(255, 255, 240, aa))
        if tt >= DOOR_OPEN:   # car door swings open
            k = ease(kk(tt, DOOR_OPEN, DOOR_OPEN + 0.5))
            hx, hy = W2(1455, 650); w_ = 95 * S; dx = -w_ * 0.55 * k
            d.polygon([(hx, hy), (hx + dx, hy + 10 * S * k), (hx + dx, hy + 120 * S), (hx, hy + 115 * S)], fill=(10, 10, 14, 255), outline=(60, 70, 90, 255))
        if tt >= FIG_IN[0]: draw_pasha(d, W2, S, tt)

def draw_pasha(d, W2, S, tt):
    k = ease(kk(tt, *FIG_IN)); a = int(255 * k)
    fx_, fy_ = 1405 - 25 * (1 - k), 800          # feet
    up = ease(kk(tt, *LOOKUP)) if tt >= LOOKUP[0] else 0
    look_left = ease(kk(tt, T("C22"), T("C22") + 0.8)) if tt >= T("C22") else 0
    H_ = 380; top = fy_ - H_
    col = (8, 8, 12, a); rim = (70, 85, 120, a)
    P_ = lambda x, y: W2(fx_ + x, top + y)
    # legs + coat
    for lx in (-22, 22):
        x1, y1 = P_(lx - 11, 270); x2, y2 = P_(lx + 11, H_); d.rectangle([x1, y1, x2, y2], fill=col)
    coat = [P_(-52, 88), P_(52, 88), P_(72, 300), P_(-72, 300)]
    d.polygon(coat, fill=col); d.line([coat[1], coat[2]], fill=rim, width=max(1, int(3 * S)))
    # head (tilts up at LOOKUP)
    hx, hy = 0 - 8 * look_left, 50 - 10 * up
    cx, cy = P_(hx, hy); r = 36 * S
    d.ellipse([cx - r, cy - r * 1.05, cx + r, cy + r * 1.05], fill=col)
    # fedora
    bx1, by1 = P_(hx - 64, hy - 30 - 4 * up); bx2, by2 = P_(hx + 64, hy - 18 - 4 * up)
    d.ellipse([bx1, by1, bx2, by2], fill=col)
    cx1, cy1 = P_(hx - 36, hy - 72 - 4 * up); cx2, cy2 = P_(hx + 36, hy - 22 - 4 * up)
    d.rounded_rectangle([cx1, cy1, cx2, cy2], int(10 * S), fill=col)
    d.line([P_(hx - 34, hy - 30), P_(hx + 34, hy - 30)], fill=(90, 20, 20, a), width=max(1, int(4 * S)))   # hat band
    # arm with the cigar
    sx_, sy_ = P_(-40, 105); ex, ey = P_(hx - 38, hy + 20)
    d.line([(sx_, sy_), P_(-62, 170), (ex, ey)], fill=col, width=max(2, int(16 * S)), joint="curve")
    glow_ = 0.6 + 0.4 * math.sin(tt * 3.1) ** 2
    for r_, aa in ((22, int(60 * glow_ * k)), (10, int(140 * glow_ * k)), (4, int(255 * k))):
        d.ellipse([ex - 6 * S - r_ * S, ey - r_ * S, ex - 6 * S + r_ * S, ey + r_ * S], fill=(255, 120, 30, aa))
    if PHONE[0] <= tt < PHONE[1]:
        px, py = P_(hx + 40, hy + 5)
        d.line([P_(40, 105), P_(58, 170), (px, py + 10 * S)], fill=col, width=max(2, int(16 * S)), joint="curve")
        d.rounded_rectangle([px - 6 * S, py - 14 * S, px + 6 * S, py + 14 * S], int(2 * S), fill=(40, 60, 90, a))
        d.ellipse([px - 26 * S, py - 26 * S, px + 26 * S, py + 26 * S], fill=(120, 160, 255, int(40 * k)))
    # eyes catch the street light once he looks up
    if up > 0.5:
        ea = int(255 * (up - 0.5) * 2)
        for ox in (-12, 12):
            X, Y = P_(hx + ox, hy - 4); d.ellipse([X - 4 * S, Y - 2.5 * S, X + 4 * S, Y + 2.5 * S], fill=(255, 235, 170, ea))

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
        text(fr, W / 2, H / 2 - 130, "الحلقة 3 بكرة", 110, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 + 10, "مين صاحب العربية السودا؟ اكتبوا توقعكم", 58, g((235, 235, 235)))
        text(fr, W / 2, H / 2 + 110, "اعمل اشتراك عشان ما يفوتكش", 46, g((200, 200, 200)))
    return fr

def hud(fr, tt, v=False):
    sc = 0.85 if v else 1.0; cx = 540 if v else W / 2
    if C09_T + 2.0 <= tt < C09_T + DUR["C09"] + 1.2:
        d = ImageDraw.Draw(fr, "RGBA"); y = 1700 if v else 120
        d.rounded_rectangle([cx - 430 * sc, y - 50 * sc, cx + 430 * sc, y + 50 * sc], int(22 * sc), fill=(20, 60, 30, 220), outline=(120, 230, 120, 255), width=4)
        text(fr, cx, y, "إجابة امبارح: البواب نفسه! ✓", int(42 * sc), (200, 255, 200))

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
    text(bgv, 540, 425, "الحلقة 2: الصوت اللي تحت الأرض", 48, (235, 235, 235))
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
        text(bgv, 540, 1695, "لغز النهارده: إيه هي السبعة؟", 50, (255, 214, 90))
        text(bgv, 540, 1758, "اكتب في الكومنتات", 42)
    return bgv

def finish(fr, tt, dark=False):
    fr = ImageChops.multiply(fr, VIG_DARK if dark else VIG)
    a = np.asarray(fr, np.float32)
    g = GRAIN[int(tt * FPS) % len(GRAIN)]
    g = np.repeat(np.repeat(g, 2, 0), 2, 1)[..., None]
    return Image.fromarray(np.clip(a + g, 0, 255).astype(np.uint8))

TINT = {"bed": (160, 175, 235), "win": (255, 255, 255), "street": (200, 210, 255)}
def frame(tt):
    sh = shot_at(tt); set_ = sh["set"]
    if set_ in ("title", "endcard"): return finish(card(set_, tt, sh), tt)
    if set_ == "black": return Image.new("RGB", (W, H), (0, 0, 0))
    cam = cam_at(sh, tt)
    d = tod(sh, tt) if set_ == "lobby" else 0
    img = bg_frame(set_, cam, d)
    props(img, set_, tt, cam, sh, d)
    layer, lights = draw_scene_chars(set_, tt, cam, sh)
    if set_ == "lobby":
        tint = tuple(int(lerp(a, b, d)) for a, b in zip((165, 180, 235), (255, 246, 228)))
    else: tint = TINT[set_]
    layer = tint_layer(layer, tint, 0.97)
    img.paste(layer, (0, 0), layer)
    fr = img.resize((W, H), Image.LANCZOS)
    dark = set_ in ("bed",) or (set_ == "lobby" and d < 0.5)
    if set_ in ("lobby", "bed") and not (set_ == "lobby" and d >= 0.999):
        lm = light_map(set_, sh, tt, cam, lights, d)
        fr = ImageChops.multiply(fr, lm); fr = ImageEnhance.Brightness(fr).enhance(lerp(1.7, 1.0, d) if set_ == "lobby" else 1.85)
    if set_ == "street" and any(0 <= tt - fl < 0.14 for fl in FLASH): fr = Image.blend(ImageEnhance.Brightness(fr).enhance(1.8), Image.new("RGB", fr.size, (255, 252, 235)), 0.45)
    if set_ == "win": fr = ImageEnhance.Brightness(fr).enhance(1.15)
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
            d.rounded_rectangle([W / 2 - 620, 60, W / 2 + 620, 175], 24, fill=(20, 20, 30, 215), outline=(255, 214, 90, 255), width=4)
            text(h, W / 2, 117, "لغز النهارده: إيه هي السبعة اللي بتستنى الجوابات؟", 38, (255, 214, 90))
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
        night = (s_["set"] == "lobby" and s_.get("tod", 1) == 0) or s_["set"] in ("bed", "win", "street", "black")
        if night: env[int(s_["start"] * SR):int(s_["end"] * SR)] = 1.0
    env[int(SILENT[0] * SR):int(CLANG * SR)] = 0.8
    env = np.convolve(env, np.ones(4410) / 4410, mode="same")
    mix_into(buf, dr * env, 0, 1.2)
    r = np.random.default_rng(9)
    S = {"boom": sfx_boom(), **SFXF}
    # tape hiss/crackle while Roshdy's tape plays from the vent
    n = int((STATIC1 - STATIC0) * SR); hiss = r.normal(0, 1, n).astype(np.float32)
    hiss = np.convolve(hiss, np.ones(6) / 6, mode="same") * 0.05
    cr = (r.uniform(0, 1, n) > 0.9992).astype(np.float32) * r.uniform(0.2, 0.6, n); hiss += np.convolve(cr, np.exp(-np.arange(200) / 30), mode="same")[:n] * 0.4
    e = np.ones(n, np.float32); fi = int(0.3 * SR); e[:fi] = np.linspace(0, 1, fi); e[-fi:] = np.linspace(1, 0, fi)
    mix_into(buf, hiss * e, STATIC0, 1.0)
    for t0, nme, g in sfx:
        if nme in S: mix_into(buf, S[nme], t0, g)
    mus = load_audio("sfx/music_old.mp3"); n = int((CAR0 + 1.0 - MUSIC2) * SR); x = np.resize(mus, n).astype(np.float32)
    e = np.ones(n, np.float32); fi = int(1.5 * SR); e[:fi] = np.linspace(0, 1, fi); e[-fi:] = np.linspace(1, 0, fi)
    from numpy.fft import rfft, irfft
    X = rfft(x); fq = np.fft.rfftfreq(n, 1 / SR); X[fq > 700] *= 0.15; x = irfft(X, n).astype(np.float32)   # through the floor
    mix_into(buf, x * e, MUSIC2, 0.6)
    # comic pizzicato under the doorman confession
    for i, f in enumerate([392, 440, 392, 330, 392, 523]):
        tt_ = np.arange(int(SR * 0.4)) / SR
        mix_into(buf, np.sin(2 * np.pi * f * tt_) * np.exp(-tt_ * 12) * 0.08, T("C09") + 1.0 + i * 0.35, 1.0)
    # rising tension string under the car / silhouette
    ts = np.arange(int((T("C23") + DUR["C23"] - STREET) * SR)) / SR
    rise = (np.sin(2 * np.pi * (110 + 40 * ts / ts[-1]) * ts) + 0.5 * np.sin(2 * np.pi * (165 + 60 * ts / ts[-1]) * ts)) * 0.05 * (ts / ts[-1])
    mix_into(buf, rise, STREET, 1.0)
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
        mux("h.mp4", "sirr_elbadroom_ep2.mp4"); mux("v.mp4", "sirr_elbadroom_ep2_vertical.mp4")
