import sys, os, math, subprocess, wave
sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter, ImageFont
from engine import *

# م2 ح5 «صفيح» — built from s2e4/ep4.py. New: draw_safeeh (robot), draw_back (walking away from camera),
# listener auto-reactions (everyone looks at whoever talks), follow-CTA phone insert with the real profile screenshot.
os.chdir(ROOT + "/s2e5")
SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(505)
SEASON = "سر البدروم"
EPT = "الحلقة 5: صفيح"

SUB = {
 "G01": "مين... هنا؟",
 "G02": "عفريت حديد!!!",
 "G03": "احتمال نطلع من هنا عايشين: 3%!",
 "G04": "توتة!... استخبي ورايا... لا لا، أنا اللي هستخبى وراكي!",
 "G05": "مش إنت صاحب «ثقوا فيا»؟!",
 "G06": "ممنوع... الدخول... بالليل.",
 "G07": "يا عم... إحنا الضهر!",
 "G08": "الساعة!... واقفة على اتناشر... فهو فاكر إننا بالليل!",
 "G09": "ودي إجابة لغز امبارح: اتناشر... الساعة اللي الشريط بيشتغل فيها كل ليلة!",
 "G10": "عينه... بقت خضرا.",
 "G11": "رشدي؟... رجعت يا رشدي؟",
 "G12": "رشدي مين؟... أنا شطة!",
 "G13": "تمام يا رشدي.",
 "G14": "مبروك يا عم رشدي.",
 "G15": "عم رشدي هو اللي عامله!... ده روبوت حارس!",
 "G16": "رسالة... ليك... يا رشدي.",
 "G17": "(شريط) أول لغز يا ولاد: أنا فوق الكل... ومليان مية... بس عمري ما شربت.",
 "G18": "سهلة!... دي... دي... لا، صعبة.",
 "G19": "لغز النهارده: فزورة عم رشدي... إجابتها إيه؟ اكتبوا في الكومنتات!",
 "G20": "واحتمال تعرف الإجابة بكرة لو ما عملتش فولو: صفر في المية.",
 "G21": "الساعة خلصت!... تيتا نعناعة راجعة!",
 "G22": "رشدي... ما تمشيش تاني.",
 "G23": "هاجي لك... بكرة الصبح. وعد.",
 "G24": "آآآه!... إيده الحديد على كتفي!",
 "G25": "ده بيودعك.",
 "G26": "يا باشا... العفريت طلع روبوت!... وبينادي الواد يا رشدي!",
 "G27": "روبوت رشدي؟... يبقى هو المفتاح. هاته.",
}
WHO = {"G01": "safeeh", "G02": "shatta", "G03": "zalata", "G04": "shatta", "G05": "tota", "G06": "safeeh", "G07": "zalata",
       "G08": "tota", "G09": "tota", "G10": "shatta", "G11": "safeeh", "G12": "shatta", "G13": "safeeh", "G14": "zalata",
       "G15": "tota", "G16": "safeeh", "G17": "rec", "G18": "shatta", "G19": "tota", "G20": "zalata", "G21": "tota",
       "G22": "safeeh", "G23": "shatta", "G24": "shatta", "G25": "zalata", "G26": "abdo", "G27": "pasha"}
EXPR = {"G02": "shock", "G03": "scared", "G04": [(0, "scared"), (0.45, "shock")], "G05": "angry", "G07": "flat",
        "G08": [(0, "shock"), (0.35, "happy")], "G09": [(0, "neutral"), (0.55, "smug")], "G10": "scared", "G12": "shock",
        "G14": "flat", "G15": "happy", "G18": [(0, "smug"), (0.5, "sad")], "G19": [(0, "neutral"), (0.6, "smug")],
        "G20": "flat", "G21": "shock", "G23": "sad", "G24": "shock", "G25": "flat", "G26": "scared", "G27": "smug"}
ARMS = {"G02": "up", "G03": "scared", "G05": "hips", "G07": "talk", "G08": "point", "G09": "point", "G10": "point",
        "G12": "talk", "G14": "hold", "G15": "point", "G18": "talk", "G19": "point", "G20": "hold", "G21": "up",
        "G23": "talk", "G24": "up", "G25": "hold", "G27": "talk"}

def _aud(k): return load_audio(f"audio/{k}.mp3")
AUD = {k: _aud(k) for k in SUB}
ENV = {k: envelope(v) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}
SFXF = {n: load_audio(ROOT + f"/s2e4/sfx/{n}.mp3") for n in ("whoosh", "creak", "slam", "switch", "steps_metal", "clang",
                                                             "stinger", "music_old", "servo", "unlock", "tape", "car")}

lines, sfx, shots, jumps, shakes = [], [], [], {}, []
def say(t, k): lines.append((t, k)); return t + DUR[k]
def fx(t, n, g=1.0): sfx.append((t, n, g))
def jump(w, t): jumps.setdefault(w, []).append(t)
def shot(set_, s, e, c0, c1=None, **kw): shots.append(dict(set=set_, start=s, end=e, c0=c0, c1=c1 or c0, **kw))
def cut(t, g=0.4): fx(t - 0.12, "whoosh", g)
def T(k): return [st for st, kk_ in lines if kk_ == k][0]
KIDS = ("shatta", "zalata", "tota")

# ---------------- world ----------------
# studio (studio_nosheet.png → 1920 coords)
SAFE0 = (1745, 735, 1.55)                     # where the sheet stood
CLOCK = (980, 128); REELS = ((572, 394), (647, 394))
EXITB = (430, 1000, 1.95)                     # Safeeh blocks the way out (exit is off-left)
SAFE2 = (960, 955, 1.8)                     # Safeeh comes close to "Roshdy"
STOOL = (980, 760, 1.35)
ST = {"tota": (700, 1000, 1.95), "shatta": (900, 1010, 1.95), "zalata": (1100, 1000, 1.95)}
HIDE = {"tota": (1240, 1000, 1.95), "shatta": (1345, 995, 1.95), "zalata": (1580, 1000, 1.95)}
TALK = {"tota": (640, 1000, 1.95), "shatta": (860, 1010, 1.95), "zalata": (1450, 1000, 1.95)}
# corridor (s2e4 corridor.png)
VAULT = (994, 506); CSTAIR = (330, 760, 1.25); CTOP = (430, 170, 0.5)
CW = {"zalata": (560, 900, 1.6), "shatta": (720, 905, 1.6), "tota": (880, 900, 1.6)}
VX = (994, 690, 0.9)
# basement outer room (s2/bg/basement_day.png): high window top-left, vault door right
WIN = (255, 45, 435, 150); BDOOR = (1355, 720, 1.05); BSPOT = (760, 960, 1.65)
# outside wall (s2e5/bg/wall.png): basement window
WWIN = (512, 487, 937, 787)
CARP = (960, 905, 2.45)

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
# ===== 0. HOOK — the second Ep4 ended: the sheet moves, red eyes =====
fx(0.0, "servo", 0.9); shakes.append((0.2, 4))
shot("studio", 0, 1.3, (1745, 460, 2.6), (1745, 430, 2.9), dutch=True)
SDROP = 1.3; fx(SDROP, "whoosh", 0.8); fx(SDROP + 0.55, "clang", 0.5)
shot("studio", 1.3, 2.4, (1600, 520, 1.6), (1650, 500, 1.7), low=True)
EYEON = 2.25; fx(EYEON - 0.05, "switch", 1.0); fx(EYEON, "stinger", 0.8); shakes.append((EYEON, 8))
t = 2.4
s = t; t = say(t, "G01") + 0.1
shot("studio", s, t, CU("safeeh", SAFE0, 2.0), CU("safeeh", SAFE0, 3.1), ease="crash", low=True)
s = t; t = say(t, "G02") + 0.1; jump("shatta", s)
shot("studio", s, t, CU("shatta", ST["shatta"], 1.6), CU("shatta", ST["shatta"], 2.2), ease="crash")
TITLE = t; shot("title", t, t + 2.0, None); t += 2.0
# ===== 1. CHASE (comic circle) — Safeeh walks to guard the way out =====
STEP0 = t; fx(t + 0.1, "steps_metal", 1.1); shakes.append((t + 0.1, 7))
CHASE = (t, t + 6.4); SAFEWALK = (t + 0.2, t + 6.0)
shot("studio", t, t + 1.4, (1300, 620, 1.25), (1250, 600, 1.3))
s = t + 1.4; t = say(t + 1.4, "G03") + 0.1
shot("studio", s, t, (1000, 640, 1.4), (900, 640, 1.45))
shot("studio", t, CHASE[1], (960, 560, 1.05), (1000, 560, 1.08)); t = CHASE[1]
s = t; t = say(t, "G04") + 0.1
shot("studio", s, t, (1310, 720, 1.9), (1310, 720, 2.05))
s = t; t = say(t, "G05") + 0.2
shot("studio", s, t, CU("tota", HIDE["tota"], 1.6), CU("tota", HIDE["tota"], 1.75))
s = t; t = say(t, "G06") + 0.15
shot("studio", s, t, CU("safeeh", EXITB, 1.5), CU("safeeh", EXITB, 1.7), low=True)
s = t; t = say(t, "G07") + 0.3
shot("studio", s, t, CU("zalata", HIDE["zalata"], 1.8), CU("zalata", HIDE["zalata"], 1.95))
# ===== 2. THE CLOCK — answer of Ep4's puzzle =====
LOOKUP = t
shot("studio", t, t + 1.3, CU("tota", HIDE["tota"], 1.6), CU("tota", HIDE["tota"], 1.7)); t += 1.3
s = t; t = say(t, "G08") + 0.1
shot("studio", s, s + 1.4, (CLOCK[0], CLOCK[1] + 40, 3.4), (CLOCK[0], CLOCK[1] + 30, 4.0), clockins=True)
shot("studio", s + 1.4, t, CU("tota", HIDE["tota"], 1.55), CU("tota", HIDE["tota"], 1.7))
s = t; t = say(t + 0.1, "G09") + 0.2
shot("studio", s, t, CU("tota", HIDE["tota"], 1.5), CU("tota", HIDE["tota"], 1.62))
CLIMB = (t, t + 3.0)
shot("studio", t, CLIMB[1], (1150, 600, 1.2), (1000, 520, 1.45)); t = CLIMB[1]
TURN = (t + 0.3, t + 2.0)
for i in range(4): fx(TURN[0] + i * 0.4, "switch", 0.35)
shot("studio", t, t + 2.3, (CLOCK[0], CLOCK[1] + 40, 3.6), (CLOCK[0], CLOCK[1] + 40, 3.9), clockins=True, hand=True); t += 2.3
GREEN = t + 0.35; fx(GREEN, "servo", 0.8)
shot("studio", t, t + 1.8, CU("safeeh", EXITB, 1.8), CU("safeeh", EXITB, 2.3)); t += 1.8
s = t; t = say(t, "G10") + 0.2
shot("studio", s, t, CU("shatta", HIDE["shatta"], 1.7), CU("shatta", HIDE["shatta"], 1.9))
# ===== 3. «Roshdy?» — scan, approach =====
SCAN = (t, t + 2.6); fx(t + 0.1, "servo", 0.6)
shot("studio", t, SCAN[1], (1350, 700, 1.5), (1350, 700, 1.5), scanpov=True); t = SCAN[1]
s = t; t = say(t + 0.1, "G11") + 0.2
shot("studio", s, t, CU("safeeh", EXITB, 1.7), CU("safeeh", EXITB, 1.95))
s = t; t = say(t, "G12") + 0.1
shot("studio", s, t, CU("shatta", HIDE["shatta"], 1.7), CU("shatta", HIDE["shatta"], 1.85))
APPR = (t, t + 3.2); fx(t + 0.3, "steps_metal", 0.8); fx(t + 1.4, "steps_metal", 0.6); fx(t + 2.4, "steps_metal", 0.5)
shot("studio", t, APPR[1], (900, 600, 1.15), (1150, 620, 1.3)); t = APPR[1]
s = t; t = say(t, "G13") + 0.3
shot("studio", s, t, (1260, 520, 1.6), (1260, 520, 1.75))
s = t; t = say(t, "G14") + 0.3
shot("studio", s, t, CU("zalata", HIDE["zalata"], 1.8), CU("zalata", HIDE["zalata"], 1.95))
s = t; t = say(t, "G15") + 0.2
shot("studio", s, t, (1300, 600, 1.25), (1300, 600, 1.35))
# ===== 3b. The message =====
s = t; t = say(t, "G16") + 0.1
shot("studio", s, t, CU("safeeh", SAFE2, 1.8), CU("safeeh", SAFE2, 2.0))
DRAWER = t; fx(t + 0.1, "servo", 0.7); fx(t + 0.9, "tape", 1.0)
shot("studio", t, t + 1.8, (SAFE2[0], SAFE2[1] - 330, 3.4), (SAFE2[0], SAFE2[1] - 320, 3.8), drawerins=True); t += 1.8
s = t; t = say(t + 0.1, "G17") + 0.4
shot("studio", s, s + DUR["G17"] * 0.55, (1250, 600, 1.2), (1300, 640, 1.45))
shot("studio", s + DUR["G17"] * 0.55, t, (SAFE2[0], SAFE2[1] - 330, 2.6), (SAFE2[0], SAFE2[1] - 330, 3.0))
s = t; t = say(t, "G18") + 0.2
shot("studio", s, t, CU("shatta", HIDE["shatta"], 1.7), CU("shatta", HIDE["shatta"], 1.85))
PUZ = t; s = t; t = say(t + 0.1, "G19") + 0.5; PUZ_END = t
shot("studio", s, t, CU("tota", HIDE["tota"], 1.5), CU("tota", HIDE["tota"], 1.68))
s = t; t = say(t, "G20") + 0.4; CTA = (s, t)
shot("studio", s, s + 1.3, CU("zalata", HIDE["zalata"], 1.8), CU("zalata", HIDE["zalata"], 1.9))
shot("phone", s + 1.3, t + 0.6, None); TAP = s + 1.3 + 1.7; fx(TAP, "switch", 0.9); t += 0.6
# ===== 4. ALARM → goodbye =====
ALARM = t
shot("studio", t, t + 1.4, (HIDE["tota"][0] + 40, HIDE["tota"][1] - 150, 3.2), (HIDE["tota"][0] + 40, HIDE["tota"][1] - 150, 3.4), alarmins=True); t += 1.4
s = t; t = say(t, "G21") + 0.2; jump("tota", s)
shot("studio", s, t, CU("tota", HIDE["tota"], 1.55), CU("tota", HIDE["tota"], 1.7), ease="crash")
s = t; t = say(t + 0.2, "G22") + 0.4
shot("studio", s, t, CU("safeeh", SAFE2, 1.8), CU("safeeh", SAFE2, 2.1))
s = t; t = say(t, "G23") + 0.4
shot("studio", s, t, (1265, 560, 1.7), (1265, 560, 1.85))
LEAVE = (t, t + 3.4)
shot("studio", t, LEAVE[1], (1100, 560, 1.1), (900, 560, 1.15)); t = LEAVE[1]
# ===== 5. CORRIDOR — false scare, walking away (backs to camera) =====
cut(t, 0.3); CWALK = (t, t + 3.4); SAFEFOLLOW = (t + 1.2, t + 4.2)
fx(t + 2.2, "steps_metal", 0.35)
shot("corridor", t, CWALK[1], (900, 600, 1.15), (800, 640, 1.3)); t = CWALK[1]
HANDON = t + 0.8; fx(HANDON, "clang", 0.6)
shot("corridor", t, HANDON + 0.4, CU("shatta", CW["shatta"], 2.0, 60), CU("shatta", CW["shatta"], 2.3, 60), handcu=True); t = HANDON + 0.4
s = t; t = say(t, "G24") + 0.1; jump("shatta", s); shakes.append((s, 10))
shot("corridor", s, t, (760, 600, 1.4), (760, 600, 1.55), ease="crash")
s = t; t = say(t, "G25") + 0.4
shot("corridor", s, t, CU("zalata", CW["zalata"], 1.7), CU("zalata", CW["zalata"], 1.85))
CLIMBUP = (t, t + 5.2); WAVE = t + 2.6
shot("corridor", t, CLIMBUP[1], (700, 600, 1.15), (560, 520, 1.25)); t = CLIMBUP[1]
# ===== 6. THE WINDOW =====
cut(t, 0.25); BWALK = (t, t + 3.4)
for i in range(4): fx(t + 0.4 + i * 0.75, "steps_metal", 0.5)
shot("basement", t, BWALK[1], (1000, 560, 1.05), (850, 560, 1.12)); t = BWALK[1]
LOOKW = t
shot("basement", t, t + 1.8, CU("safeeh", BSPOT, 1.8), CU("safeeh", BSPOT, 2.0)); t += 1.8
SHADOW = t + 0.6; fx(SHADOW, "stinger", 1.0); shakes.append((SHADOW, 6))
shot("basement", t, t + 2.4, (345, 160, 2.6), (345, 110, 3.6), ease="crash"); t += 2.4
cut(t, 0.3); fx(t + 0.6, "car", 0.3)
shot("wall", t, t + 1.4, (860, 560, 1.15), (900, 600, 1.6)); t += 1.4
s = t; t = say(t, "G26") + 0.2
shot("wall", s, t, (960, 640, 2.0), (960, 640, 2.2))
s = t; t = say(t + 0.1, "G27") + 0.5
shot("carday", s, t, CU("pasha", CARP, 1.4), CU("pasha", CARP, 1.8), low=True)
# ===== 7. CLIFF — Safeeh's eyes flip back to RED =====
RED2 = t + 0.9; fx(RED2, "switch", 1.0); fx(RED2 + 0.05, "servo", 0.9)
shot("basement", t, t + 2.6, CU("safeeh", BSPOT, 1.6), CU("safeeh", BSPOT, 3.4), ease="crash", dutch=True); t += 2.6
fx(t, "clang", 1.2); fx(t, "boom", 0.9); shakes.append((t - 0.3, 14))
shot("black", t, t + 0.6, None); t += 0.6
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
for a_, b_, r_, g_ in ((CHASE[0], CHASE[1], 13, 0.45), (CLIMB[0], CLIMB[1] - 0.8, 8, 0.35), (LEAVE[0], LEAVE[1], 8, 0.4),
                       (CWALK[0], CWALK[1], 7, 0.35), (CLIMBUP[0], CLIMBUP[1], 6, 0.3)):
    contacts(a_, b_, r_, g_)
METAL = []
for a_, b_, per in ((SAFEWALK[0], SAFEWALK[1], 0.8), (APPR[0] + 0.3, APPR[1], 0.55)):
    tt_ = a_
    while tt_ < b_: METAL.append(tt_); tt_ += per

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
def tinted(img, lvl=1.0, tint=(255, 255, 255)):
    return ImageChops.multiply(ImageEnhance.Brightness(img).enhance(lvl), Image.new("RGB", img.size, tint))
def _ld(p): return Image.open(p).convert("RGB").resize((1920, 1080), Image.LANCZOS)
SRC = {"studio": ImageEnhance.Brightness(_ld("bg/studio_nosheet.png")).enhance(1.25),
       "corridor": _ld(ROOT + "/s2e4/bg/corridor.png"),
       "basement": ImageEnhance.Brightness(_ld(ROOT + "/s2/bg/basement_day.png")).enhance(1.08),
       "wall": _ld("bg/wall.png"), "carday": _ld("bg/carday.png")}
yy, xx = np.mgrid[0:H, 0:W]
vg = 1 - 0.55 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) ** 1.2
VIG = Image.fromarray((np.clip(vg, 0.25, 1) * 255).astype(np.uint8)).convert("RGB")
vg2 = np.clip(1 - 0.85 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2), 0.15, 1)
VIG_DARK = Image.fromarray((vg2 * 255).astype(np.uint8)).convert("RGB")
# softer, slowly-changing grain (smaller files — see docs/status.md)
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

INS = ("clockins", "drawerins", "alarmins")
def bg_frame(set_, cam, sh, tt):
    ins = any(sh.get(k) for k in INS)
    return bg_crop(SRC[set_], cam, not ins and not sh.get("dutch"))

def A_(who, pos, **kw):
    x, y, s = pos; d = dict(who=who, x=x, y=y, s=s, look=0, expr="neutral", arms="down"); d.update(kw); return d
def walk_to(a, p0, p1, win, tt, rate=8):
    k = kk(tt, *win); e = ease(k)
    a["x"], a["y"], a["s"] = lerp(p0[0], p1[0], e), lerp(p0[1], p1[1], e), lerp(p0[2], p1[2], e)
    if 0 < k < 1: a["walk"] = tt * rate
    return k

# ---- Safeeh state ----
def safeeh_state(set_, tt):
    d = dict(who="safeeh", eye="red", eye_on=1.0, arms="down", drawer=0.0, sad=False, look=0, lean=0.0)
    if set_ == "studio":
        x, y, s = SAFE0
        if tt < EYEON: d["eye_on"] = 0.0 if tt < 0.5 else 0.35 + 0.25 * math.sin(tt * 9)
        elif tt < EYEON + 0.3: d["eye_on"] = [1, 0, 1, 0.3, 1][min(4, int((tt - EYEON) / 0.06))]
        if tt >= SAFEWALK[0]:
            k = kk(tt, *SAFEWALK); e = ease(k)
            x, y, s = lerp(SAFE0[0], EXITB[0], e), lerp(SAFE0[1], EXITB[1], e), lerp(SAFE0[2], EXITB[2] * 0.9, e)
            if 0 < k < 1: d["walk"] = tt * 4.0; d["look"] = -1
            d["arms"] = "down" if k < 1 else "block"
        if tt >= T("G06") + DUR["G06"] + 0.3: d["arms"] = "down"
        if tt >= LOOKUP: d["look"] = 1
        if tt >= GREEN:
            u = kk(tt, GREEN, GREEN + 0.6)
            d["eye"] = "red" if u < 0.5 and int(u * 12) % 2 == 0 else "green"
        if SCAN[0] <= tt < SCAN[1]: d["look"] = math.sin(kk(tt, *SCAN) * math.pi * 1.5) * 1.0 + 0.5
        if tt >= SCAN[1]: d["look"] = 1
        if tt >= APPR[0]:
            k = kk(tt, APPR[0] + 0.2, APPR[1] - 0.1); e = ease(k)
            x, y, s = lerp(EXITB[0], SAFE2[0], e), lerp(EXITB[1], SAFE2[1], e), lerp(EXITB[2] * 0.9, SAFE2[2], e)
            if 0 < k < 1: d["walk"] = tt * 5.0
            d["look"] = 1
        if tt >= T("G13"): d["look"] = 1
        if tt >= T("G16"): d["arms"] = "chest" if tt < DRAWER + 1.6 else "down"
        if tt >= DRAWER: d["drawer"] = ease(kk(tt, DRAWER + 0.1, DRAWER + 0.8))
        if tt >= ALARM: d["drawer"] = 1 - ease(kk(tt, ALARM, ALARM + 0.6))
        if tt >= T("G22") - 0.3: d["sad"] = True; d["eye_on"] = 0.7
        if tt >= LEAVE[0]:
            d["look"] = -1; d["sad"] = True
            d["arms"] = "point" if LEAVE[0] + 1.2 <= tt < LEAVE[0] + 2.6 else "down"   # a little wave
        d.update(x=x, y=y, s=s)
        return d
    if set_ == "corridor":
        d["eye"] = "green"
        if tt < SAFEFOLLOW[0]: return None
        k = kk(tt, *SAFEFOLLOW); e = ease(k)
        x, y, s = lerp(VX[0], 940, e), lerp(VX[1], 870, e), lerp(VX[2], 1.4, e)
        if 0 < k < 1: d["walk"] = tt * 4.0
        d["look"] = -1
        if tt >= HANDON - 0.5: d["arms"] = "point"
        if tt >= T("G25"): d["arms"] = "down"; d["sad"] = True; d["eye_on"] = 0.75
        if tt >= WAVE: d["arms"] = "point" if tt < WAVE + 1.6 else "down"
        d.update(x=x, y=y, s=s)
        return d
    if set_ == "basement":
        d["eye"] = "green"; d["sad"] = True; d["eye_on"] = 0.75
        k = kk(tt, BWALK[0] + 0.3, BWALK[1] - 0.2); e = ease(k)
        x, y, s = lerp(BDOOR[0], BSPOT[0], e), lerp(BDOOR[1], BSPOT[1], e), lerp(BDOOR[2], BSPOT[2], e)
        if 0 < k < 1: d["walk"] = tt * 4.0
        d["look"] = -1
        if tt >= LOOKW: d["look"] = -1; d["lean"] = -0.4
        if tt >= RED2:
            u = kk(tt, RED2, RED2 + 0.5); d["sad"] = False; d["eye_on"] = 1.0
            d["eye"] = "green" if u < 0.6 and int(u * 14) % 2 == 0 else "red"
            d["arms"] = "block" if u >= 1 else "down"
        d.update(x=x, y=y, s=s)
        return d
    return None

# ---- kids ----
def circle_pos(who, tt):
    ph0 = {"tota": 0.0, "shatta": 0.75, "zalata": 1.5}[who]
    u = kk(tt, CHASE[0] + 0.4, CHASE[1] - 1.0)
    ang = ph0 + u * 2 * math.pi * 1.1
    x = 960 + math.cos(ang) * 470; depth = math.sin(ang)       # depth<0 → further back
    y = 960 + depth * 70; s = 1.95 * (1 + depth * 0.12)
    return x, y, s, (-1 if math.sin(ang) > 0 else 1)
def kid(who, set_, tt):
    a = A_(who, ST[who], look=1)
    if who == "zalata": a["held"] = "nbpen"; a["arms"] = "hold"; a["expr"] = "flat"
    if set_ == "studio":
        a["expr"] = "scared" if who != "zalata" else "shock"
        if tt < TITLE: a["look"] = 1; return a
        if tt < CHASE[1]:
            if tt >= CHASE[0] + 0.4:
                x, y, s, lk = circle_pos(who, tt)
                k = kk(tt, CHASE[1] - 1.0, CHASE[1])
                if k > 0:
                    x0_, y0_, s0_, _ = circle_pos(who, CHASE[1] - 1.0)
                    x, y, s = lerp(x0_, HIDE[who][0], ease(k)), lerp(y0_, HIDE[who][1], ease(k)), lerp(s0_, HIDE[who][2], ease(k))
                a.update(x=x, y=y, s=s, look=lk, walk=tt * 13, arms="up" if who != "zalata" else "scared")
                a["held"] = None
            return a
        a["x"], a["y"], a["s"] = HIDE[who]; a["look"] = -1
        if who == "shatta":                     # crouched behind tiny Tota
            hide = 1 - ease(kk(tt, LOOKUP, LOOKUP + 0.6)) if tt < GREEN + 1.0 else 0
            a["crouch"] = 120 * hide; a["lean"] = 0.35 * hide; a["expr"] = "scared"
        if tt >= T("G04") and who == "tota": a["look"] = 1 if tt < T("G05") + DUR["G05"] else -1
        if tt >= LOOKUP: a["look"] = -1 if who != "tota" else -1; a["expr"] = "neutral" if who != "zalata" else "flat"
        if tt >= T("G08"): a["look"] = -1
        if who == "tota" and tt >= CLIMB[0]:
            k = walk_to(a, HIDE["tota"], STOOL, (CLIMB[0], CLIMB[1] - 0.8), tt, 8)
            if tt >= CLIMB[1] - 0.8:
                a["y"] = STOOL[1] - 62 * ease(kk(tt, CLIMB[1] - 0.8, CLIMB[1] - 0.3)); a["arms"] = "up"; a["look"] = 0
            a["held"] = None
            if tt >= TURN[1] + 0.3:
                k = walk_to(a, (STOOL[0], STOOL[1] - 62, STOOL[2]), HIDE["tota"], (TURN[1] + 0.3, GREEN + 1.6), tt, 8)
                a["arms"] = "down"; a["look"] = 1 if k < 1 else -1
        if tt >= GREEN: a["expr"] = "shock" if who != "zalata" else "flat"
        if tt >= T("G13"): a["expr"] = "neutral" if who != "zalata" else "flat"
        if tt >= T("G15"): a["expr"] = "happy" if who == "tota" else a["expr"]
        if tt >= T("G17"): a["expr"] = "neutral"; a["lean"] = -0.25
        if tt >= T("G18"): a["lean"] = 0
        if who == "tota" and ALARM <= tt < T("G21") + DUR["G21"]: a["held"] = "phone"; a["arms"] = "hold"
        if tt >= T("G22"): a["expr"] = "sad" if who != "zalata" else "flat"
        if tt >= LEAVE[0]:
            off = {"tota": 0.0, "shatta": 0.6, "zalata": 0.3}[who]
            k = walk_to(a, HIDE[who], (-260, 1020, 2.0), (LEAVE[0] + off, LEAVE[1] - 0.2), tt, 8)
            a["look"] = -1
            if who == "shatta" and LEAVE[0] + 1.6 <= tt < LEAVE[0] + 2.3: a["look"] = 1   # one look back
            if k >= 1: return None
        return a
    if set_ == "corridor":
        a["held"] = "phone"; a["arms"] = "hold"; a["expr"] = "neutral" if who != "zalata" else "flat"
        off = {"tota": 0.0, "shatta": 0.35, "zalata": 0.7}[who]
        st0 = CWALK[0] + off * 0.6
        if tt < st0: return None
        walk_to(a, (VAULT[0] + 40 * (off - 0.35), 700, 0.85), CW[who], (st0, CWALK[1] - 0.1), tt, 7)
        a["look"] = -1
        if tt >= T("G24"):
            a["look"] = 1; a["expr"] = "shock" if who == "shatta" else ("flat" if who == "zalata" else "scared")
        if tt >= CLIMBUP[0]:
            o2 = {"tota": 0.0, "zalata": 0.5, "shatta": 1.0}[who]
            mid = (CSTAIR[0] + 30 * o2, CSTAIR[1], CSTAIR[2])
            k1 = walk_to(a, CW[who], mid, (CLIMBUP[0] + o2 * 0.5, CLIMBUP[0] + o2 * 0.5 + 1.2), tt, 7)
            if k1 >= 1:
                k2 = walk_to(a, mid, CTOP, (CLIMBUP[0] + o2 * 0.5 + 1.2, CLIMBUP[1] - 0.6 + o2 * 0.3), tt, 6)
                a["back"] = True
                if who == "shatta" and WAVE <= tt < WAVE + 1.4:
                    a["walk"] = None; a["arms"] = "wave"
                    a["x"], a["y"], a["s"] = lerp(mid[0], CTOP[0], 0.15), lerp(mid[1], CTOP[1], 0.15), lerp(mid[2], CTOP[2], 0.15)
                if k2 >= 1: return None
            else:
                a["back"] = k1 > 0.15
        return a
    return None

def actors(set_, tt, sh):
    A = []
    if any(sh.get(k) for k in INS) or sh.get("scanpov"):
        if sh.get("scanpov"): return [kid(w, set_, tt) for w in KIDS if kid(w, set_, tt)]
        return A
    if set_ in ("studio", "corridor"):
        for who in KIDS:
            a = kid(who, set_, tt)
            if a: A.append(a)
    if set_ in ("studio", "corridor", "basement"):
        sf = safeeh_state(set_, tt)
        if sf: A.append(sf)
    if set_ == "wall":
        ab = A_("abdo", (1035, 985, 1.7), look=-1, expr="shock" if tt < T("G26") else "scared", lean=-0.9)
        if tt >= T("G26") - 0.4: ab["held"] = "phone"; ab["arms"] = "shush"; ab["look"] = 1; ab["lean"] = -0.2
        A.append(ab)
    if set_ == "carday":
        A.append(A_("pasha", CARP, look=-1, expr="smug", held="phone", arms="shush"))
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
            if a["who"] == WHO[k] or (WHO[k] == "rec" and a["who"] == "safeeh"): spk = a
    reaching = set_ == "corridor" and HANDON - 0.6 <= tt < T("G25")
    for a in sorted(acts, key=lambda a: (1 if (reaching and a["who"] == "safeeh") else 0, a["s"], a["y"])):
        who = a["who"]; talking = k is not None and (WHO[k] == who or (WHO[k] == "rec" and who == "safeeh"))
        mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
        bob = abs(math.sin(a["walk"])) * 5 * a["s"] if a.get("walk") is not None else 0
        wy = a["y"] - jump_off(who, tt) - bob + a.get("crouch", 0)
        X = (a["x"] - x0) * z; Y = (wy - y0) * z; s = a["s"] * z
        p = P(layer)
        p.ell(X, (a["y"] - y0) * z + 4 * s, (70 if who == "safeeh" else 46) * s, 9 * s, (0, 0, 0, 110), None)
        if who == "safeeh":
            reach = None
            if set_ == "corridor" and HANDON - 0.6 <= tt < T("G25"):
                sk = kid("shatta", set_, tt)
                if sk:
                    SS_ = sk["s"] * CH["shatta"]["scale"]
                    tgt = ((sk["x"] + 20 * SS_ - x0) * z, (sk["y"] - 128 * SS_ - y0) * z)
                    u_ = ease(kk(tt, HANDON - 0.6, HANDON))
                    rest = (X + 76 * s, Y - 110 * s)
                    reach = (lerp(rest[0], tgt[0], u_), lerp(rest[1], tgt[1], u_))
            draw_safeeh(p, X, Y, s, tt, a["eye"], a["eye_on"], mouth, a.get("look", 0), a.get("walk"), a["arms"],
                        a["drawer"], a.get("lean", 0), a["sad"], reach)
            col = EYE_COL[a["eye"]]
            hx = X + a.get("look", 0) * 6 * s; ey = Y - (90 + 154 + 96 - 34) * s
            if a["eye_on"] > 0.2:
                lights.append((hx, ey, 120 * s, 0.9 * a["eye_on"], tuple(c / 255 for c in col)))
            continue
        if a.get("back"):
            draw_back(p, who, X, Y, s, tt, a.get("walk"), a.get("arms", "down"), a.get("held"))
            continue
        expr = a.get("expr", "neutral")
        if talking: expr = expr_of(k, lt)
        arms = a.get("arms", "down")
        if talking and not a.get("held") and k in ARMS: arms = ARMS[k]
        look = a.get("look", 0)
        if spk is not None and not talking and a.get("walk") is None and set_ in ("studio", "corridor"):
            look = 1 if spk["x"] > a["x"] else -1             # listeners react: look at whoever talks
        shiver = math.sin(tt * 60) * 2.5 if expr in ("scared", "shock") and who in KIDS + ("abdo",) else 0
        blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11 and expr != "sleepy"
        draw_char(p, who, X + shiver * z, Y, s, expr, mouth, look, blink, arms, tt, a.get("held"), a.get("lean", 0), a.get("walk"))
        S = s * CH[who]["scale"]
        if who == "pasha":   # fedora + cigar (brand look from Ep2)
            hy = Y - 190 * S + math.sin(tt * 2.2 + X) * 1.6 * S; hx = X + a.get("lean", 0) * 18 * S
            p.rect(hx - 30 * S, hy - 70 * S, hx + 30 * S, hy - 34 * S, (22, 22, 28, 255), INK, 2.5 * S, 14 * S)
            p.line([(hx - 10 * S, hy - 68 * S), (hx + 10 * S, hy - 66 * S)], (60, 60, 70, 255), 3 * S)
            p.rect(hx - 29 * S, hy - 46 * S, hx + 29 * S, hy - 38 * S, (140, 25, 30, 255), None)
            p.ell(hx, hy - 36 * S, 60 * S, 10 * S, (22, 22, 28, 255), INK, 2.5 * S)
        hx_, hy_ = HANDS.get(arms, (46, 104))
        hand = (X + hx_ * S, Y - hy_ * S)
        if a.get("held") == "phone" and set_ == "corridor":
            lk = 1 if look >= 0 else -1
            lights.append((hand[0] + lk * 40 * S, hand[1] - 10 * S, 170 * z * a["s"] / 1.6, 1.4, (1.0, 0.98, 0.9)))
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
    if set_ == "corridor":
        m = np.full((LH, LW, 3), 0.62, np.float32) * cool
        X, Y = W3(420, 120); m += 0.9 * glow(X, Y, 380 * z)[..., None] * warm
        X, Y = W3(330, 700); m += 0.45 * glow(X, Y, 360 * z)[..., None] * warm
        X, Y = W3(*VAULT); m += 0.9 * glow(X, Y, 260 * z)[..., None] * warm
    elif set_ == "basement":
        m = np.full((LH, LW, 3), 0.62, np.float32)
        sun = 1.0
        if tt >= SHADOW: sun = 0.35 + 0.65 * (1 - ease(kk(tt, SHADOW, SHADOW + 0.25)))
        X, Y = W3(560, 700); m += 0.55 * sun * glow(X, Y, 420 * z)[..., None] * warm
        X, Y = W3(345, 100); m += 0.6 * sun * glow(X, Y, 200 * z)[..., None] * warm
    else:
        if not lights: return None
        m = np.full((LH, LW, 3), 1.0, np.float32)
        for X, Y, R, inten, col in lights: m += inten * 0.35 * glow(X, Y, R)[..., None] * np.array(col, np.float32)
        return Image.fromarray((np.clip(m / 1.15, 0, 1) * 255).astype(np.uint8), "RGB").resize((W, H), Image.BILINEAR)
    for X, Y, R, inten, col in lights:
        m += inten * glow(X, Y, R)[..., None] * np.array(col, np.float32)
    lm = np.clip(m / 1.4, 0, 1)
    return Image.fromarray((lm * 255).astype(np.uint8), "RGB").resize((W, H), Image.BILINEAR)

def props(img, set_, tt, cam, sh):
    x0, y0, z = cam; S = SS * z; d = ImageDraw.Draw(img, "RGBA")
    W2 = lambda wx, wy: ((wx - x0) * S, (wy - y0) * S)
    lw = lambda v: max(1, int(v * S))
    if set_ == "studio":
        # clock hands: 12:00 until Tota turns them → 3:00
        cx, cy = W2(*CLOCK); R = 34 * S
        d.ellipse([cx - 50 * S, cy - 50 * S, cx + 50 * S, cy + 50 * S], fill=(214, 200, 168, 255))   # repaint the face (hides the painted 12:00 hands)
        for i in range(12):
            a_ = i * math.pi / 6; r0 = 42 * S if i % 3 else 36 * S
            d.line([(cx + math.cos(a_) * r0, cy + math.sin(a_) * r0), (cx + math.cos(a_) * 47 * S, cy + math.sin(a_) * 47 * S)], fill=(40, 30, 20, 255), width=lw(3 if i % 3 == 0 else 1.5))
        u = ease(kk(tt, TURN[0], TURN[1])) if tt >= TURN[0] else 0
        ha = -math.pi / 2 + u * math.pi / 2; ma = -math.pi / 2 + u * 2 * math.pi * 3
        d.line([(cx, cy), (cx + math.cos(ha) * R * 0.55, cy + math.sin(ha) * R * 0.55)], fill=(25, 20, 15, 255), width=lw(4))
        d.line([(cx, cy), (cx + math.cos(ma) * R * 0.85, cy + math.sin(ma) * R * 0.85)], fill=(25, 20, 15, 255), width=lw(2.5))
        d.ellipse([cx - 3 * S, cy - 3 * S, cx + 3 * S, cy + 3 * S], fill=(25, 20, 15, 255))
        if sh.get("hand") and TURN[0] - 0.3 <= tt < TURN[1] + 0.2:   # Tota's hand turning the hands
            hx, hy = cx + math.cos(ma) * R * 0.8, cy + math.sin(ma) * R * 0.8 + 4 * S
            d.line([(hx, hy), (hx + 30 * S, hy + 140 * S)], fill=(22, 22, 22, 255), width=lw(5))
            d.ellipse([hx - 6 * S, hy - 6 * S, hx + 6 * S, hy + 6 * S], fill=(22, 22, 22, 255))
        # stool under the clock (brought by Tota)
        if CLIMB[0] + 1.0 <= tt < GREEN + 2.0:
            sx, sy = W2(STOOL[0], STOOL[1])
            d.rectangle([sx - 46 * S, sy - 66 * S, sx + 46 * S, sy - 54 * S], fill=(110, 70, 40, 255), outline=(30, 20, 10, 255), width=lw(2))
            for ox in (-38, 38): d.line([(sx + ox * S, sy - 56 * S), (sx + ox * 1.15 * S, sy)], fill=(80, 50, 30, 255), width=lw(5))
        # the sheet: covers Safeeh until it slides off (falls to the floor → the crumpled sheet of the bg)
        if tt < SDROP + 0.7:
            u = ease(kk(tt, SDROP, SDROP + 0.7))
            bx, by = SAFE0[0], SAFE0[1]; top = by - 570 + u * 520
            wob = math.sin(tt * 13) * 6 * (1 if tt > 0.2 else 0)
            pts = [(bx - 150 - u * 40, by + 6), (bx - 120 + wob, top + 120), (bx - 60, top + 10), (bx + wob, top - 5),
                   (bx + 60, top + 12), (bx + 125 + wob, top + 130), (bx + 160 + u * 50, by + 6)]
            d.polygon([W2(*p_) for p_ in pts], fill=(176, 166, 146, 255), outline=(90, 80, 66, 255))
            for i in range(5):   # folds: dark grooves + light ridges
                fx_ = bx - 110 + i * 55
                d.line([W2(fx_, top + 70), W2(fx_ + 14 + wob, by)], fill=(120, 110, 92, 255), width=lw(6))
                d.line([W2(fx_ + 14, top + 80), W2(fx_ + 30 + wob, by)], fill=(205, 196, 176, 255), width=lw(3))
            if tt < SDROP:   # red glow through the cloth
                on = 0.4 + 0.3 * math.sin(tt * 9)
                for ex in (bx - 34, bx + 34):
                    X, Y = W2(ex, top + 70)
                    for r_, a_ in ((30, 50), (16, 110)): d.ellipse([X - r_ * S, Y - r_ * 0.7 * S, X + r_ * S, Y + r_ * 0.7 * S], fill=(255, 40, 30, int(a_ * on)))
        # scanning beam (Safeeh's POV)
        if sh.get("scanpov"):
            u = kk(tt, *SCAN); sxp = lerp(500, 1450, min(1, u * 1.25))
            if u > 0.8: sxp = 1350
            X, Y = W2(sxp, 780)
            d.rectangle([0, 0, img.size[0], img.size[1]], fill=(40, 255, 110, 28))
            for yl in range(0, img.size[1], int(6 * SS)): d.line([(0, yl), (img.size[0], yl)], fill=(0, 0, 0, 40), width=1)
            r_ = 120 * S
            d.ellipse([X - r_, Y - r_, X + r_, Y + r_], outline=(80, 255, 140, 230), width=lw(3))
            d.line([(X - r_ * 1.3, Y), (X - r_ * 0.6, Y)], fill=(80, 255, 140, 230), width=lw(3)); d.line([(X + r_ * 0.6, Y), (X + r_ * 1.3, Y)], fill=(80, 255, 140, 230), width=lw(3))
            d.line([(X, Y - r_ * 1.3), (X, Y - r_ * 0.6)], fill=(80, 255, 140, 230), width=lw(3)); d.line([(X, Y + r_ * 0.6), (X, Y + r_ * 1.3)], fill=(80, 255, 140, 230), width=lw(3))
            if u > 0.8 and int(tt * 6) % 2: text(img, X, Y - r_ * 1.5, "رُشْدِي؟", int(46 * S), (120, 255, 160), (0, 40, 10), 4)
        # alarm insert: Tota's phone screen ringing
        if sh.get("alarmins"):
            X, Y = W2(HIDE["tota"][0] + 40, HIDE["tota"][1] - 150)
            sh_ = math.sin(tt * 70) * 3 * S
            d.rounded_rectangle([X - 60 * S + sh_, Y - 110 * S, X + 60 * S + sh_, Y + 110 * S], int(14 * S), fill=(25, 25, 30, 255), outline=(10, 10, 10, 255), width=lw(3))
            d.rounded_rectangle([X - 52 * S + sh_, Y - 98 * S, X + 52 * S + sh_, Y + 98 * S], int(10 * S), fill=(255, 90, 70, 255))
            ax, ay = X + sh_, Y - 30 * S
            d.ellipse([ax - 30 * S, ay - 30 * S, ax + 30 * S, ay + 30 * S], fill=(255, 255, 255, 255), outline=(120, 20, 10, 255), width=lw(4))
            for sx in (-1, 1): d.ellipse([ax + sx * 30 * S - 10 * S, ay - 40 * S, ax + sx * 30 * S + 10 * S, ay - 22 * S], fill=(255, 255, 255, 255), outline=(120, 20, 10, 255), width=lw(3))
            d.line([(ax, ay), (ax, ay - 20 * S)], fill=(120, 20, 10, 255), width=lw(4)); d.line([(ax, ay), (ax + 14 * S, ay + 6 * S)], fill=(120, 20, 10, 255), width=lw(4))
            text(img, X + sh_, Y + 50 * S, "ساعة!", int(34 * S), (255, 255, 255), (120, 20, 10), 3)
    if set_ == "corridor" and sh.get("handins"):
        # Safeeh's claw lands on Shatta's shoulder
        sx, sy = W2(CW["shatta"][0] + 30, CW["shatta"][1] - 260)
        u = ease(kk(tt, sh["start"], HANDON))
        hx, hy = sx + lerp(260, 0, u) * S, sy - lerp(120, 0, u) * S
        d.rectangle([sx - 120 * S, sy - 10 * S, sx + 40 * S, sy + 200 * S], fill=(216, 90, 48, 255), outline=(22, 22, 22, 255), width=lw(4))
        d.line([(hx + 400 * S, hy - 160 * S), (hx, hy)], fill=(22, 22, 22, 255), width=lw(30)); d.line([(hx + 400 * S, hy - 160 * S), (hx, hy)], fill=(120, 126, 134, 255), width=lw(22))
        for dx_ in (-22, 4):
            d.line([(hx, hy), (hx + dx_ * S, hy + 36 * S)], fill=(22, 22, 22, 255), width=lw(10))
        d.ellipse([hx - 20 * S, hy - 20 * S, hx + 20 * S, hy + 20 * S], fill=(168, 174, 180, 255), outline=(22, 22, 22, 255), width=lw(3))
    if set_ == "basement" and tt >= SHADOW:
        # Abdo's face pressed against the high window (outside, backlit), bars in front
        u = ease(kk(tt, SHADOW, SHADOW + 0.25))
        cx, cy = W2(345, 112 + (1 - u) * 50); r = 38 * S
        tmp = Image.new("RGBA", img.size, (0, 0, 0, 0)); tp = P(tmp)
        draw_char(tp, "abdo", cx / SS, cy / SS + 190 * 0.8 * z * 1.1, 0.8 * z, "shock", 0, -1, False, "down", tt)
        a0 = W2(WIN[0], WIN[1]); a1 = W2(WIN[2], WIN[3])
        mask = Image.new("L", img.size, 0); ImageDraw.Draw(mask).rectangle([a0[0], a0[1], a1[0], a1[1]], fill=255)
        tmp.putalpha(ImageChops.multiply(tmp.getchannel("A"), mask))
        img.paste(tmp, (0, 0), tmp)
        for i in range(1, 6):
            bx = a0[0] + (a1[0] - a0[0]) * i / 6
            d.line([(bx, a0[1]), (bx, a1[1])], fill=(30, 26, 22, 255), width=lw(5))

def ltr(img, x, y, s, size, fill, stroke=(10, 10, 10), sw=3):
    ImageDraw.Draw(img).text((x, y), s, font=ImageFont.truetype(FONT, size), fill=fill, anchor="mm", direction="ltr", stroke_width=sw, stroke_fill=stroke)

FOLLOW = {k: Image.open(ROOT + f"/brand/follow/{k}.png").convert("RGB") for k in ("yt", "tt", "ig", "fb")}
# where the Follow/Subscribe button is in each cropped screenshot (x0,y0,x1,y1) and what it turns into
BTN = {"yt": ((25, 414, 551, 477), "Subscribed", (230, 230, 230), (20, 20, 20)),
       "tt": ((18, 269, 244, 336), "Following", (235, 235, 235), (30, 30, 30)),
       "ig": ((19, 351, 252, 403), "Following", (239, 239, 239), (20, 20, 20)),
       "fb": ((19, 659, 281, 716), "متابَع ✓", (228, 230, 235), (20, 20, 20))}
def phone_card(tt, sh, plat="yt", CW_=W, CH_=H):
    """Zalata's phone held up: the real profile screenshot, a finger taps Follow/Subscribe, it flips, a heart pops."""
    fr = Image.new("RGB", (CW_, CH_), (0, 0, 0))
    bgc = bg_crop(SRC["studio"], (500, 63, 1.6), True).resize((W, H))
    if CW_ != W:   # vertical canvas: fill with a centre crop of the blurred studio
        bgc = bgc.crop((W / 2 - 304, 0, W / 2 + 304, H)).resize((CW_, CH_))
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
        u = kk(tt, TAP, TAP + 0.9)   # heart pop + ring
        if u < 1:
            r = 40 + 160 * u; d.ellipse([bcx - r, bcy - r, bcx + r, bcy + r], outline=(255, 214, 90, int(255 * (1 - u))), width=8)
            hy = bcy - 60 - 220 * u; hs = 50 * (0.6 + 0.6 * math.sin(min(1, u * 2) * math.pi / 2))
            d.polygon([(bcx, hy + hs * 0.9), (bcx - hs, hy), (bcx - hs * 0.5, hy - hs * 0.6), (bcx, hy - hs * 0.2), (bcx + hs * 0.5, hy - hs * 0.6), (bcx + hs, hy)], fill=(255, 60, 90, int(255 * (1 - u * 0.7))))
    else:
        g = 0.5 + 0.5 * math.sin(tt * 10)
        d.rounded_rectangle([B[0] - 8, B[1] - 8, B[2] + 8, B[3] + 8], int((B[3] - B[1]) / 2 + 8), outline=(255, 214, 90, int(150 + 100 * g)), width=6)
    # the finger (stick-figure hand) comes in and taps
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
        text(fr, W / 2, H / 2 - 230, "الحلقة 6 بكرة: الأسطوانة", 96, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 - 100, "فزورة عم رشدي إجابتها إيه؟ اكتبوها في الكومنتات", 52, g((235, 235, 235)))
        # follow strip: the real profile screenshots
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
    if T("G09") + 1.2 <= tt < T("G09") + DUR["G09"] + 1.0:
        d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([cx - 430 * sc, y - 50 * sc, cx + 430 * sc, y + 50 * sc], int(22 * sc), fill=(20, 60, 30, 220), outline=(120, 230, 120, 255), width=4)
        text(fr, cx, y, "إجابة امبارح: الساعة 12 ✓", int(42 * sc), (200, 255, 200))
    for key, val in (("G03", "3%"), ("G20", "0%")):
        if T(key) + DUR[key] * 0.4 <= tt < T(key) + DUR[key] + 0.3 and not (key == "G20" and shot_at(tt)["set"] == "phone"):
            d = ImageDraw.Draw(fr, "RGBA")
            d.rounded_rectangle([cx - 160 * sc, y - 50 * sc, cx + 160 * sc, y + 50 * sc], int(22 * sc), fill=(60, 20, 20, 220), outline=(255, 120, 90, 255), width=4)
            ltr(fr, cx, y, val, int(56 * sc), (255, 160, 120))

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

PUZ_TXT = "لغز النهارده: أنا فوق الكل ومليان مية... بس عمري ما شربت. أنا مين؟"
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

def finish_v(fr, tt):
    a = np.asarray(fr, np.float32); return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))

def finish(fr, tt, dark=False):
    fr = ImageChops.multiply(fr, VIG_DARK if dark else VIG)
    a = np.asarray(fr, np.float32)
    g = GRAIN[int(tt * 6) % len(GRAIN)]
    g = np.repeat(np.repeat(g, 4, 0), 4, 1)[..., None]
    return Image.fromarray(np.clip(a + g, 0, 255).astype(np.uint8))

TINT = {"studio": (255, 232, 205), "corridor": (130, 145, 185), "basement": (255, 236, 210), "wall": (255, 236, 200), "carday": (235, 215, 190)}
def frame(tt, plat="yt"):
    sh = shot_at(tt); set_ = sh["set"]
    if set_ in ("title", "endcard"): return finish(card(set_, tt, sh), tt)
    if set_ == "black": return Image.new("RGB", (W, H), (0, 0, 0))
    if set_ == "phone": return finish(phone_card(tt, sh, plat), tt)
    cam = cam_at(sh, tt)
    img = bg_frame(set_, cam, sh, tt)
    layer, lights = draw_scene_chars(set_, tt, cam, sh)
    layer = tint_layer(layer, TINT.get(set_, (255, 244, 225)), 0.97)
    img.paste(layer, (0, 0), layer)
    props(img, set_, tt, cam, sh)
    if set_ == "carday":   # the seat cushion hides the hips/legs → he sits
        x0, y0, z = cam; ys = int((880 - y0) * z * SS)
        if ys < SSH:
            bgc = bg_crop(SRC["carday"], cam, True); img.paste(bgc.crop((0, ys, SSW, SSH)), (0, ys))
    if set_ == "wall":     # Abdo is outside, low: the sidewalk edge stays in front of his body
        x0, y0, z = cam; ys = int((905 - y0) * z * SS)
        if ys < SSH:
            bgc = bg_crop(SRC["wall"], cam, False); img.paste(bgc.crop((0, ys, SSW, SSH)), (0, ys))
    fr = img.resize((W, H), Image.LANCZOS)
    if sh.get("dutch"):
        fr = fr.rotate(7, resample=Image.BICUBIC).crop((80, 45, W - 80, H - 45)).resize((W, H), Image.LANCZOS)
    lm = light_map(set_, sh, tt, cam, lights)
    dark = set_ in ("corridor",) or sh.get("dutch", False)
    if lm is not None:
        fr = ImageChops.multiply(fr, lm)
        if set_ in ("corridor", "basement"): fr = ImageEnhance.Brightness(fr).enhance(1.5 if set_ == "corridor" else 1.25)
    return finish(fr, tt, dark)

def build_audio(path="mix.wav"):
    buf = np.zeros(int(TOTAL * SR) + SR * 3, dtype=np.float32)
    dr = drone(TOTAL + 1); env = np.zeros(len(dr), np.float32)
    for a_, b_ in ((0, TITLE), (T("G06"), GREEN), (SHADOW - 1.5, TOTAL - 4.4)):
        env[int(a_ * SR):int(b_ * SR)] = 1.0
    env = np.convolve(env, np.ones(4410) / 4410, mode="same")
    mix_into(buf, dr * env, 0, 1.2)
    r = np.random.default_rng(9)
    S = {"boom": sfx_boom(), **SFXF}
    for t0, nme, g in sfx:
        if nme in S and g > 0: mix_into(buf, S[nme], t0, g)
    # Safeeh's metal steps + servo creak on each step
    for st in METAL:
        mix_into(buf, SFXF["steps_metal"][:int(0.5 * SR)], st, 0.55)
    # power-up whine under the hook
    ts = np.arange(int(1.6 * SR)) / SR
    mix_into(buf, np.sin(2 * np.pi * (180 + 500 * ts / ts[-1]) * ts) * 0.05 * np.minimum(1, ts * 3), EYEON - 1.2, 1.0)
    # phone alarm (two-tone beeps)
    for i in range(6):
        tb = np.arange(int(0.12 * SR)) / SR
        mix_into(buf, np.sin(2 * np.pi * (1320 if i % 2 else 990) * tb) * 0.12, ALARM + 0.1 + i * 0.18, 1.0)
    # chase: comic running pizzicato loop
    for i in range(int((CHASE[1] - CHASE[0]) / 0.25)):
        f = [392, 440, 494, 440][i % 4]; tb = np.arange(int(SR * 0.2)) / SR
        mix_into(buf, np.sin(2 * np.pi * f * tb) * np.exp(-tb * 18) * 0.07, CHASE[0] + 0.3 + i * 0.25, 1.0)
    # comic stings: hiding behind Tota, «congrats uncle Roshdy», «easy... no, hard», «he's saying bye»
    for t_, notes in ((T("G04") + DUR["G04"] - 0.2, [523, 392, 262]), (T("G14") + 0.6, [523, 494, 440, 392]),
                      (T("G18") + DUR["G18"] - 0.2, [392, 370, 349]), (T("G25") + 0.5, [523, 494, 440, 392])):
        for i, f in enumerate(notes):
            tt_ = np.arange(int(SR * 0.4)) / SR
            mix_into(buf, np.sin(2 * np.pi * f * tt_) * np.exp(-tt_ * 12) * 0.09, t_ + i * 0.2, 1.0)
    # warm music box when the eyes turn green and on the goodbye
    for a_, dur_ in ((GREEN + 0.4, 5.0), (T("G22"), 6.0)):
        for i in range(int(dur_ / 0.45)):
            f = [659, 784, 880, 784, 659, 587][i % 6]; tb = np.arange(int(SR * 0.5)) / SR
            mix_into(buf, np.sin(2 * np.pi * f * tb) * np.exp(-tb * 5) * 0.045, a_ + i * 0.45, 1.0)
    # old music faint from the tape in Safeeh's chest
    a_ = DRAWER + 0.9; n = int((T("G17") + DUR["G17"] + 1.0 - a_) * SR)
    mus = lowpass(np.resize(SFXF["music_old"], n).astype(np.float32), 1200)
    e = np.ones(n, np.float32); fi = int(0.4 * SR); e[:fi] = np.linspace(0, 1, fi); e[-fi:] = np.linspace(1, 0, fi)
    mix_into(buf, mus * e, a_, 0.25)
    # tension string under the window / cliff
    a_, b_ = SHADOW - 1.0, TOTAL - 4.4
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
    """Vertical phone-insert clips for Reels (ig) and Shorts (yt) — spliced over the TikTok vertical by publish step."""
    sh = [s_ for s_ in shots if s_["set"] == "phone"][0]
    for plat in ("ig", "yt"):
        p_ = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "1080x1920", "-r", str(FPS), "-i", "-",
                               "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", f"phone_{plat}.mp4"], stdin=subprocess.PIPE)
        for i in range(int(round(sh["start"] * FPS)), int(round(sh["end"] * FPS))):
            tt = i / FPS; p_.stdin.write(vertical(None, tt, plat).tobytes())
        p_.stdin.close(); p_.wait()
    print("phone window", round(round(sh["start"] * FPS) / FPS, 3), round(round(sh["end"] * FPS) / FPS, 3))

def lowpass(x, fc):
    from numpy.fft import rfft, irfft
    X = rfft(x); fq = np.fft.rfftfreq(len(x), 1 / SR); X[fq > fc] *= 0.12; return irfft(X, len(x)).astype(np.float32)

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
