import sys, os, math, subprocess, wave
sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter, ImageFont
from engine import *
from locations import loc

# م2 ح8 «ليلة البدروم» — built from s2e7/ep7.py, Episode checklist (docs/directing.md) + fixed locations (docs/locations.md).
# New vs Ep7: new set (the dug tunnel), Shatta's solo crawl in the dark (mouse + Abdo's torch sweep = 2 freezes),
# antenna-plug insert + robot power-on, the «رشدي؟! / أنا عبده!» gag, the first chase of the season, a night→dawn
# time-lapse inside the basement with a moving sun beam that IS the puzzle, tiles insert, the Pasha's ringed hand + reveal.
os.chdir(ROOT + "/s2e8")
SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(808)
SEASON = "سر البدروم"
EPT = "الحلقة 8: ليلة البدروم"

SUB = {
 "K01": "العلامات دي... داخلة جوه الحيطة!",
 "K02": "وفيه صوت حفر... جاي من جوه!",
 "K03": "نتيجة التصويت: أغلبكم قالوا فهمي صادق... وعندكم حق! فهمي ما كانش بيكدب!",
 "K04": "يا معلم... الروبوت ده لو صحي هياكلنا!",
 "K05": "احفروا بسرعة... الباشا عايز الصندوق قبل الفجر!",
 "K06": "صفيح فاصل خالص... من غير الهوائي بتاعه!",
 "K07": "الهوائي معايا!... بس لازم حد يحطه في مكانه.",
 "K08": "أنا؟!... في العتمة؟!... ماشي. أنا هروح.",
 "K09": "مين هناك؟!... أنا مش خايف... أنا بس بسأل.",
 "K10": "تمام... يا رشدي.",
 "K11": "لا يا عم صفيح... أنا شطة. وأنا مش خايف!",
 "K12": "رشدي؟!",
 "K13": "أنا عبده يا عم!... عبده!",
 "K14": "دخلاء!... وضع الحراسة!",
 "K15": "يا ماما!... فين النور؟!",
 "K16": "احتمال عبده يرجع تاني: صفر في المية.",
 "K17": "رسالة رشدي: الكنز تحت البلاطة... اللي شعاع الشمس بييجي عليها الصبح.",
 "K18": "بس إحنا بالليل!... ومافيش شمس!",
 "K19": "الشباك العالي!... الشمس بتدخل منه على بلاطة واحدة بس.",
 "K20": "لغز النهارده: أنهي بلاطة؟ النجمة، الوردة، الهلال، ولا السادة؟ ركزوا في الشعاع... واكتبوا في الكومنتات!",
 "K21": "اعملوا فولو... ده أمر من صفيح!",
 "K22": "صندوق!... لقيناه!",
 "K23": "شكرًا يا ولاد... وفرتوا عليا التعب.",
}
WHO = {"K01": "zalata", "K02": "shatta", "K03": "tota", "K04": "abdo", "K05": "abdo", "K06": "zalata", "K07": "tota", "K08": "shatta",
       "K09": "abdo", "K10": "safeeh", "K11": "shatta", "K12": "safeeh", "K13": "abdo", "K14": "safeeh", "K15": "abdo", "K16": "zalata",
       "K17": "safeeh", "K18": "tota", "K19": "zalata", "K20": "tota", "K21": "safeeh", "K22": "shatta", "K23": "pasha"}
EXPR = {"K01": "scared", "K02": "scared", "K03": [(0, "neutral"), (0.5, "smug")], "K04": "scared", "K05": "angry", "K06": "flat",
        "K07": "neutral", "K08": [(0, "shock"), (0.55, "angry")], "K09": "scared", "K11": [(0, "happy"), (0.5, "smug")], "K13": "scared",
        "K15": "scared", "K16": "flat", "K18": "sad", "K19": "happy", "K20": [(0, "neutral"), (0.6, "smug")], "K22": "happy", "K23": "smug"}
ARMS = {"K03": "point", "K04": "talk", "K05": "point", "K08": "hips", "K09": "hold", "K11": "hips", "K13": "up", "K15": "up",
        "K18": "talk", "K19": "point", "K20": "point", "K22": "up", "K23": "hold"}

def _aud(k): return load_audio(f"audio/{k}.mp3")
AUD = {k: _aud(k) for k in SUB}
ENV = {k: envelope(v) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}
SFXF = {n: load_audio(ROOT + f"/s2e4/sfx/{n}.mp3") for n in ("whoosh", "creak", "slam", "switch", "clang", "stinger", "servo",
                                                             "steps_metal", "mouse", "unlock", "bonk")}

lines, sfx, shots, jumps, shakes = [], [], [], {}, []
def say(t, k): lines.append((t, k)); return t + DUR[k]
def fx(t, n, g=1.0): sfx.append((t, n, g))
def jump(w, t): jumps.setdefault(w, []).append(t)
def shot(set_, s, e, c0, c1=None, **kw): shots.append(dict(set=set_, start=s, end=e, c0=c0, c1=c1 or c0, **kw))
def cut(t, g=0.4): fx(t - 0.12, "whoosh", g)
def T(k): return [st for st, kk_ in lines if kk_ == k][0]
KIDS = ("shatta", "zalata", "tota")

# ---------------- world ----------------
# studio (s2e5 studio_nosheet, lights off) — the drag marks run from Safeeh's spot to a hole in the left wall
ST = {"tota": (620, 1000, 1.95), "shatta": (860, 1010, 1.95), "zalata": (1100, 1000, 1.95)}
SAFE = (1600, 770); HOLE_S = (150, 760)
# tunnel (s2e8/bg/tunnel.png → 1920 coords)
PK = {"zalata": (70, 690, 1.1), "tota": (165, 695, 1.1), "shatta": (255, 700, 1.1)}
TK = {"tota": (560, 1005, 1.9), "shatta": (780, 1012, 1.9), "zalata": (1000, 1005, 1.9)}
ABD = (1500, 985, 1.9); WORKER = (935, 470, 0.42); SAFT = (1110, 880, 1.3)
LANT = [(455, 430, 260), (735, 175, 170)]
CR0, CR1, CR2 = (300, 760, 1.25), (520, 930, 1.5), (960, 905, 1.48)
# basement (s2/bg/basement_day.png): high window top-left, iron door right-centre
BK = {"tota": (600, 1010, 1.9), "shatta": (800, 1015, 1.9), "zalata": (1170, 1005, 1.9)}
SAFB = (1660, 985, 1.5); BEAM = (1040, 905); WIN = (350, 120); PDOOR = (1365, 712, 1.45)

def CU(who, pos, z=2.2, dx=0, dy=0):
    x, y, s = pos
    if who == "safeeh":
        return (x + dx, y - 250 * s + H / (2 * (z + 0.45)) - 110 * s - dy - 130 * s, z + 0.45)
    S = s * CH[who]["scale"]
    z += 0.45
    if who == "tota": z *= 1.3; dx -= 50
    hy = y - 190 * S
    return (x + dx, hy + H / (2 * z) - 1.45 * 46 * S - 25 - dy, z)

t = 0.0
# ===== 0. HOOK — same second as Ep7: torch on the drag marks, digging from inside the wall =====
DIG0 = 0.0
shot("studio", 0, 3.7, (1450, 820, 1.9), (430, 760, 1.85), follow=True)
say(0.3, "K01"); t = 3.7
s = t; t = say(t + 0.1, "K02") + 0.2; jump("shatta", s)
shot("studio", s, t, CU("shatta", ST["shatta"], 1.5), CU("shatta", ST["shatta"], 1.75))
cut(t, 0.3); TITLE = t; shot("title", t, t + 2.0, None); t += 2.0
# ===== 1. Answer of the Ep7 vote =====
s = t; t = say(t + 0.1, "K03") + 0.2; ANS = s
shot("studio", s, t, CU("tota", ST["tota"], 1.5), CU("tota", ST["tota"], 1.65))
# ===== 2. THE TUNNEL =====
cut(t, 0.3); TW = (t, t + 3.2)
shot("tunnel", t, TW[1], (980, 560, 1.0), (1000, 580, 1.08)); t = TW[1]
s = t; t = say(t, "K04") + 0.1
shot("tunnel", s, t, CU("abdo", ABD, 1.5, -40), CU("abdo", ABD, 1.65, -40))
s = t; t = say(t, "K05") + 0.2
shot("tunnel", s, t, (1250, 640, 1.35), (1300, 640, 1.45))
s = t; t = say(t, "K06") + 0.1
shot("tunnel", s, t, CU("zalata", PK["zalata"], 2.0, 60), CU("zalata", PK["zalata"], 2.15, 60))
s = t; t = say(t, "K07") + 0.1
shot("tunnel", s, t, CU("tota", PK["tota"], 2.0, 50), CU("tota", PK["tota"], 2.15, 50))
s = t; t = say(t, "K08") + 0.2
shot("tunnel", s, t, CU("shatta", PK["shatta"], 1.9), CU("shatta", PK["shatta"], 2.2))
# ===== 3. Shatta crawls alone (mouse freeze, torch freeze) =====
CRAWL = (t, t + 5.2); MOUSE = t + 1.8; ABTURN = t + 3.8
fx(MOUSE, "mouse", 0.9); fx(ABTURN, "stinger", 0.7)
shot("tunnel", t, t + 3.6, (520, 760, 1.5), (760, 780, 1.6), low=True)
shot("tunnel", t + 3.6, CRAWL[1], (1000, 640, 1.2), (1000, 640, 1.25)); t = CRAWL[1]
s = t; t = say(t, "K09") + 0.2; K09T = s
shot("tunnel", s, t, CU("abdo", ABD, 1.6, -40), CU("abdo", ABD, 1.8, -40))
CRAWL2 = (t, t + 1.8)
shot("tunnel", t, CRAWL2[1], (900, 700, 1.45), (1000, 700, 1.55)); t = CRAWL2[1]
ANT = (t, t + 2.0); PLUG = t + 1.0; fx(PLUG, "switch", 1.0); fx(PLUG + 0.1, "servo", 0.9); shakes.append((PLUG, 5))
shot("tunnel", t, ANT[1], None, antins=True); t = ANT[1]
s = t; t = say(t + 0.1, "K10") + 0.1
shot("tunnel", s, t, CU("safeeh", (SAFT[0], SAFT[1], SAFT[2]), 1.4), CU("safeeh", SAFT, 1.6), low=True)
s = t; t = say(t, "K11") + 0.2; jump("shatta", s + DUR["K11"] * 0.5)
shot("tunnel", s, t, CU("shatta", CR2, 1.5, -60), CU("shatta", CR2, 1.7, -60))
# ===== 4. The gag + the chase =====
TURN = (t, t + 1.3); fx(t + 0.1, "servo", 0.8)
shot("tunnel", t, TURN[1], (1300, 640, 1.3), (1300, 640, 1.35)); t = TURN[1]
s = t; t = say(t, "K12") + 0.2
shot("tunnel", s, t, CU("safeeh", SAFT, 1.6, 30), CU("safeeh", SAFT, 1.75, 30))
s = t; t = say(t, "K13") + 0.1; jump("abdo", s)
shot("tunnel", s, t, CU("abdo", ABD, 1.6, -40), CU("abdo", ABD, 1.75, -40))
s = t; t = say(t, "K14") + 0.1; RED = s + 0.15; SNAP = s + 0.9; fx(RED, "stinger", 1.0); fx(SNAP, "clang", 0.8); shakes.append((SNAP, 9))
shot("tunnel", s, t, CU("safeeh", SAFT, 1.2), CU("safeeh", SAFT, 2.0), ease="crash", low=True)
s = t; t = say(t, "K15"); CHASE = (s, s + 4.2)
for i in range(7): fx(s + 0.4 + i * 0.5, "steps_metal", 0.5)
shot("tunnel", s, CHASE[1], (980, 620, 1.05), (960, 560, 1.15)); t = CHASE[1]
KIN = (t, t + 1.8)
shot("tunnel", t, KIN[1], (700, 640, 1.15), (760, 660, 1.2)); t = KIN[1]
s = t; t = say(t, "K16") + 0.3; Z0 = s
shot("tunnel", s, t, CU("zalata", TK["zalata"], 1.7), CU("zalata", TK["zalata"], 1.85))
SBACK = (t, t + 2.4)
for i in range(4): fx(t + 0.3 + i * 0.5, "steps_metal", 0.45)
shot("tunnel", t, SBACK[1], (1000, 600, 1.1), (1050, 620, 1.2)); t = SBACK[1]
s = t; t = say(t, "K17") + 0.3; MSG = s; fx(s - 0.3, "servo", 0.6)
shot("tunnel", s, t, CU("safeeh", (1250, 905, 1.42), 1.3), CU("safeeh", (1250, 905, 1.42), 1.6))
s = t; t = say(t, "K18") + 0.1
shot("tunnel", s, t, CU("tota", TK["tota"], 1.5), CU("tota", TK["tota"], 1.62))
s = t; t = say(t, "K19") + 0.3
shot("tunnel", s, t, CU("zalata", TK["zalata"], 1.7), CU("zalata", TK["zalata"], 1.9))
# ===== 5. BASEMENT: night → dawn, the sun beam =====
cut(t, 0.3); TL = (t, t + 5.0); BEAMON = t + 3.6
shot("basement", t, TL[1], (960, 540, 1.0), (960, 540, 1.04), tl=TL); t = TL[1]
WAKE = (t, t + 2.0)
shot("basement", t, WAKE[1], (1000, 700, 1.25), (BEAM[0], BEAM[1] - 120, 1.7)); t = WAKE[1]
PUZ = t; s = t; t = say(t + 0.1, "K20") + 0.4; PUZ_END = t
shot("basement", s, s + 3.6, CU("tota", BK["tota"], 1.5), CU("tota", BK["tota"], 1.6))
shot("basement", s + 3.6, t, None, tilesins=True)
s = t; t = say(t, "K21") + 0.4; CTA = (s, t)
shot("basement", s, s + 1.3, CU("safeeh", SAFB, 1.4), CU("safeeh", SAFB, 1.5))
shot("phone", s + 1.3, t + 0.4, None); TAP = s + 1.3 + 1.4; fx(TAP, "switch", 0.9); t += 0.4
LIFT = (t, t + 3.0); LUP = t + 1.6; fx(t + 0.3, "steps_metal", 0.0); fx(LUP - 0.2, "unlock", 0.9); fx(LUP, "slam", 0.5)
shot("basement", t, t + 1.4, (900, 700, 1.3), (1000, 720, 1.45))
shot("basement", t + 1.4, LIFT[1], None, liftins=True); t = LIFT[1]
s = t; t = say(t, "K22") + 0.1; jump("shatta", s)
shot("basement", s, t, CU("shatta", (BEAM[0] - 60, 1000, 1.9), 1.6), CU("shatta", (BEAM[0] - 60, 1000, 1.9), 1.8))
HAND = (t, t + 2.4); GRAB = t + 1.0; fx(t + 0.2, "stinger", 1.0); fx(GRAB, "clang", 0.5)
shot("basement", t, HAND[1], None, handins=True); t = HAND[1]
s = t; t = say(t + 0.2, "K23") + 0.5; PREV = s
shot("basement", s, s + 2.2, (PDOOR[0], 560, 1.6), (PDOOR[0], 560, 1.9), low=True)
shot("basement", s + 2.2, t, CU("pasha", PDOOR, 1.5), CU("pasha", PDOOR, 2.6), ease="crash", low=True)
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
for a_, b_, r_, g_ in ((CHASE[0], CHASE[1], 12, 0.5), (KIN[0], KIN[1], 7, 0.35), (WAKE[0] + 0.6, WAKE[1], 6, 0.3)):
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

SRC = {"studio": loc("studio", "day"), "tunnel": loc("tunnel", "day"),
       "basement": loc("basement", "day"), "basement_n": loc("basement", "dark")}
SRC["tunnel"] = ImageEnhance.Brightness(SRC["tunnel"]).enhance(1.15)
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
    if CHASE[0] <= tt < CHASE[1] - 1.0: shake = max(shake, 4)
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

def dawn(tt):
    if tt < TL[0]: return 0.0
    return ease(kk(tt, TL[0] + 0.6, TL[1] - 0.6))

def bg_frame(set_, cam, sh, tt):
    if set_ == "basement":
        d = dawn(tt)
        if d >= 0.999: return bg_crop(SRC["basement"], cam)
        if d <= 0.001: return bg_crop(SRC["basement_n"], cam)
        return Image.blend(bg_crop(SRC["basement_n"], cam), bg_crop(SRC["basement"], cam), d)
    return bg_crop(SRC[set_], cam)

def A_(who, pos, **kw):
    x, y, s = pos; d = dict(who=who, x=x, y=y, s=s, look=0, expr="neutral", arms="down"); d.update(kw); return d
def walk_to(a, p0, p1, win, tt, rate=8):
    k = kk(tt, *win); e = ease(k)
    a["x"], a["y"], a["s"] = lerp(p0[0], p1[0], e), lerp(p0[1], p1[1], e), lerp(p0[2], p1[2], e)
    if 0 < k < 1: a["walk"] = tt * rate
    return k
def SF(pos, **kw):
    d = dict(who="safeeh", x=pos[0], y=pos[1], s=pos[2], eye="off", eye_on=0.0, arms="down", drawer=0.0, sad=True, look=0, lean=0.0, antenna=False)
    d.update(kw); return d

def safeeh_tunnel(tt):
    sf = SF(SAFT)
    if tt >= PLUG: sf["antenna"] = True
    if tt >= PLUG:   # flicker on → green
        u = tt - PLUG; sf["eye"] = "green"; sf["sad"] = False
        sf["eye_on"] = [1, 0, 1, 0.3, 1][min(4, int(u / 0.08))] if u < 0.4 else 1.0
    if tt >= TURN[0]: sf["look"] = 1
    if tt >= RED: sf["eye"] = "red"; sf["arms"] = "up" if tt < CHASE[0] + 0.3 else "down"
    if tt >= CHASE[0]:
        k = walk_to(sf, SAFT, (930, 560, 0.62), (CHASE[0] + 0.5, CHASE[1]), tt, 7)
        if k >= 1 and tt < SBACK[0]: return None
    if tt >= SBACK[0]:
        sf.update(eye="green", eye_on=1.0, sad=False, look=-1, arms="down")
        walk_to(sf, (930, 560, 0.62), (1250, 905, 1.42), SBACK, tt, 6)
    if tt >= MSG: sf["drawer"] = min(1.0, (tt - MSG) * 2); sf["look"] = -1
    return sf

def kid(who, set_, tt):
    a = A_(who, (0, 0, 1), look=1)
    off = {"tota": 0.0, "shatta": 0.35, "zalata": 0.7}[who]
    torch = "torch"
    if set_ == "studio":
        if shot_at(tt).get("follow"): return None
        a["x"], a["y"], a["s"] = ST[who]; a["held"] = torch; a["arms"] = "hold"; a["expr"] = "scared"; a["look"] = -1
        if tt >= ANS: a["expr"] = "neutral" if who != "zalata" else "flat"
        return a
    if set_ == "tunnel":
        if tt < KIN[0]:
            if who == "shatta" and tt >= CRAWL[0]:
                a.update(arms="down", held=None, expr="scared", look=1, lean=0.7)
                if tt < CRAWL[1]:
                    u = kk(tt, CRAWL[0], CRAWL[1])
                    frz = (MOUSE <= tt < MOUSE + 0.9) or (ABTURN <= tt)
                    if u < 0.35: p0, p1, v = CR0, CR1, u / 0.35
                    else:
                        v = (u - 0.35) / 0.65
                        v = min(v, kk(MOUSE, CRAWL[0], CRAWL[1]) * 0 + v)
                        p0, p1 = CR1, (lerp(CR1[0], CR2[0], 0.55), lerp(CR1[1], CR2[1], 0.55), lerp(CR1[2], CR2[2], 0.55))
                    if frz and tt >= ABTURN: v = kk(ABTURN, CRAWL[0], CRAWL[1]); v = (v - 0.35) / 0.65
                    a["x"], a["y"], a["s"] = lerp(p0[0], p1[0], v), lerp(p0[1], p1[1], v), lerp(p0[2], p1[2], v)
                    a["y"] += 40; a["walk"] = None if frz else tt * 4
                    if frz: a["expr"] = "shock"; a["lean"] = 0.9
                    return a
                if tt < CRAWL2[1] or tt < ANT[0]:
                    mid = (lerp(CR1[0], CR2[0], 0.55), lerp(CR1[1], CR2[1], 0.55) + 40, lerp(CR1[2], CR2[2], 0.55))
                    walk_to(a, mid, CR2, CRAWL2, tt, 4); a["held"] = "antenna"; a["arms"] = "hold"
                    a["y"] += 40 * (1 - kk(tt, CRAWL2[0], CRAWL2[1]))
                    return a
                a.update(x=CR2[0], y=CR2[1], s=CR2[2], lean=0, expr="happy", arms="down", held=None, look=1)
                if tt >= T("K11"): a["expr"] = "smug"
                if tt >= TURN[0]: a["expr"] = "shock"
                if tt >= CHASE[0]: a["expr"] = "happy"; a["arms"] = "up"
                return a
            a["x"], a["y"], a["s"] = PK[who]; a["look"] = 1; a["expr"] = "scared" if who != "zalata" else "flat"
            a["held"] = torch if who != "tota" else "antenna"; a["arms"] = "hold"
            if who == "shatta" and T("K08") <= tt: a["held"] = "antenna"
            if who == "tota" and tt >= T("K08") + 0.6: a["held"] = torch
            if T("K08") <= tt < CRAWL[0] and who != "shatta": a["look"] = 1
            if tt >= CHASE[0]: a["expr"] = "shock"
            return a
        if who == "shatta" and tt < KIN[1]:
            a.update(x=CR2[0], y=CR2[1], s=CR2[2], expr="happy", look=-1, arms="hips")
            walk_to(a, CR2, TK["shatta"], (KIN[0] + 0.4, KIN[1]), tt, 7)
            return a
        st0 = KIN[0] + off * 0.5
        walk_to(a, (PK[who][0] + 150, 760, 1.2), TK[who], (st0, KIN[1] + 0.2), tt, 7)
        a["look"] = 1; a["held"] = torch; a["arms"] = "hold"; a["expr"] = "happy" if who != "zalata" else "smug"
        if tt >= SBACK[0]: a["expr"] = "neutral" if who != "zalata" else "flat"; a["look"] = 1
        if who == "zalata" and tt >= T("K19"): a["held"] = None
        return a
    if set_ == "basement":
        a["x"], a["y"], a["s"] = BK[who]; a["look"] = 1
        if tt < WAKE[0] + 0.4:
            a.update(expr="sleepy", lean=-0.3 if who != "zalata" else 0.3, arms="down")
            return a
        a["expr"] = "shock"; a["look"] = 1 if BK[who][0] < BEAM[0] else -1
        if tt >= PUZ: a["expr"] = "happy" if who != "zalata" else "smug"
        if who == "shatta" and tt >= LIFT[0]:
            walk_to(a, BK["shatta"], (BEAM[0] - 60, 1000, 1.9), (LIFT[0], LIFT[0] + 1.2), tt, 7)
            a["expr"] = "happy"
        if tt >= HAND[0]: a["expr"] = "shock"; a["look"] = 1
        if tt >= PREV: a["expr"] = "scared" if who != "zalata" else "shock"; a["look"] = 1
        return a
    return None

def actors(set_, tt, sh):
    A = []
    if any(sh.get(k) for k in ("antins", "tilesins", "liftins", "handins")): return A
    if set_ == "tunnel":
        if tt < CHASE[1]:
            ab = A_("abdo", ABD, look=1, expr="neutral", arms="up" if int(tt * 2.2) % 2 else "hold", held=None)
            if T("K04") <= tt < T("K04") + DUR["K04"]: ab.update(look=-1, arms="talk", expr="scared")
            if ABTURN - 0.3 <= tt < K09T + DUR["K09"]: ab.update(look=-1, held="torch", arms="hold", expr="scared")
            if tt >= TURN[0]: ab.update(look=-1, held="torch", arms="hold", expr="shock")
            if tt >= T("K13"): ab.update(held=None, arms="up", expr="scared")
            if tt >= CHASE[0]:
                k = walk_to(ab, ABD, (935, 470, 0.4), (CHASE[0] + 0.1, CHASE[0] + 2.4), tt, 14)
                ab["back"] = True; ab["arms"] = "up"
                if k >= 1: ab = None
            if ab: A.append(ab)
            w = A_("abdo", WORKER, look=1, arms="up" if int(tt * 2.5) % 2 else "hold", sil=1.0)
            if tt >= CHASE[0]:
                if walk_to(w, WORKER, (940, 430, 0.25), (CHASE[0] + 0.3, CHASE[0] + 1.4), tt, 14) >= 1: w = None
                elif w: w["back"] = True
            if w: A.append(w)
        sf = safeeh_tunnel(tt)
        if sf: A.append(sf)
    if set_ == "basement":
        A.append(SF(SAFB, eye="green", eye_on=1.0, sad=False, antenna=True, look=-1))
        if tt >= PREV:
            p = A_("pasha", PDOOR, look=-1, expr="smug", held="box", arms="hold", sil=1.0 - 0.75 * ease(kk(tt, PREV + 0.6, PREV + 2.0)))
            A.append(p)
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
            if a["who"] == WHO[k] and not a.get("sil"): spk = a
    for a in sorted(acts, key=lambda a: (a["s"], a["y"])):
        who = a["who"]; talking = k is not None and WHO[k] == who and not (who == "abdo" and a.get("sil"))
        mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
        bob = abs(math.sin(a["walk"])) * 5 * a["s"] if a.get("walk") is not None else 0
        wy = a["y"] - jump_off(who, tt) - bob
        X = (a["x"] - x0) * z; Y = (wy - y0) * z; s = a["s"] * z
        tgt = layer if not a.get("sil") else Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0))
        p = P(tgt)
        p.ell(X, (a["y"] - y0) * z + 4 * s, (70 if who == "safeeh" else 46) * s, 9 * s, (0, 0, 0, 110), None)
        if who == "safeeh":
            draw_safeeh(p, X, Y, s, tt, a["eye"], a["eye_on"], mouth, a.get("look", 0), a.get("walk"), a["arms"], a["drawer"],
                        a.get("lean", 0), a["sad"], antenna=a.get("antenna", True))
            if a["eye_on"] > 0.3:
                ec = (1.4, 0.2, 0.15) if a["eye"] == "red" else (0.3, 1.4, 0.5)
                lights.append((X, Y - 230 * s, 80 * s, 0.4, ec)); lights.append((X, Y - 120 * s, 160 * s, 0.25, (1.0, 0.9, 0.8)))
            if set_ == "tunnel" and tt < SNAP:   # ropes
                for i, dy in enumerate((150, 120, 85)):
                    p.line([(X - 62 * s, Y - dy * s), (X + 62 * s, Y - (dy - 10) * s)], (150, 115, 70, 255), 5 * s)
            if set_ == "tunnel" and SNAP <= tt < SNAP + 0.6:
                u = kk(tt, SNAP, SNAP + 0.6)
                for i in range(6):
                    ang = i * 1.05; L = 60 + 120 * u
                    p.line([(X + math.cos(ang) * 40 * s, Y - 120 * s), (X + math.cos(ang) * L * s, Y - 120 * s + math.sin(ang) * L * s + 80 * u * s)], (150, 115, 70, int(255 * (1 - u))), 4 * s)
            continue
        if a.get("back"):
            draw_back(p, who, X, Y, s, tt, a.get("walk"), a.get("arms", "down"), a.get("held"))
            if tgt is not layer:
                al_ = tgt.getchannel("A"); dark = Image.new("RGBA", tgt.size, (8, 8, 10, 255)); dark.putalpha(al_); layer.alpha_composite(dark)
            continue
        expr = a.get("expr", "neutral")
        if talking: expr = expr_of(k, lt)
        arms = a.get("arms", "down")
        if talking and not a.get("held") and k in ARMS: arms = ARMS[k]
        look = a.get("look", 0)
        if spk is not None and not talking and a.get("walk") is None and who in KIDS and set_ != "studio":
            look = 1 if spk["x"] > a["x"] else -1
        shiver = math.sin(tt * 60) * 2.5 if expr in ("scared", "shock") and who in KIDS + ("abdo",) else 0
        blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11 and expr != "sleepy"
        held = a.get("held"); held_e = held if held != "box" else None
        draw_char(p, who, X + shiver * z, Y, s, expr, mouth, look, blink, arms, tt, held_e, a.get("lean", 0), a.get("walk"))
        S = s * CH[who]["scale"]
        if who == "pasha":
            hy = Y - 190 * S + math.sin(tt * 2.2 + X) * 1.6 * S; hx = X + a.get("lean", 0) * 18 * S
            p.rect(hx - 30 * S, hy - 70 * S, hx + 30 * S, hy - 34 * S, (22, 22, 28, 255), INK, 2.5 * S, 14 * S)
            p.rect(hx - 29 * S, hy - 46 * S, hx + 29 * S, hy - 38 * S, (140, 25, 30, 255), None)
            p.ell(hx, hy - 36 * S, 60 * S, 10 * S, (22, 22, 28, 255), INK, 2.5 * S)
        if held == "box":
            hx_, hy_ = HANDS["hold"]; bx, by = X + hx_ * S, Y - hy_ * S
            p.rect(bx - 34 * S, by - 26 * S, bx + 34 * S, by + 22 * S, (120, 126, 134, 255), INK, 2.5 * S, 3 * S)
            p.line([(bx - 34 * S, by - 12 * S), (bx + 34 * S, by - 12 * S)], INK, 2 * S)
        if expr == "sleepy" and a.get("lean", 0):
            for i in range(3):
                u = ((tt * 0.6) + i / 3 + hash(who) % 3 * 0.2) % 1
                text(layer, (X + (40 + 30 * u + i * 6) * S) * SS, (Y - (220 + 140 * u) * S) * SS, "Z", int((22 + 14 * i) * S * SS), (255, 255, 255, int(255 * (1 - u))), sw=2)
        hx_, hy_ = HANDS.get(arms, (46, 104)); hand = (X + hx_ * S, Y - hy_ * S)
        if held == "torch": lights.append((hand[0], hand[1], 120 * s, 1.0, (1.0, 0.95, 0.75), "torch", who))
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
WARM = np.array([1.05, 0.95, 0.78], np.float32); COOL = np.array([0.75, 0.85, 1.1], np.float32)

def scan_pt(tt, sh):
    if sh.get("follow"):
        u = kk(tt, sh["start"], sh["end"])
        return lerp(SAFE[0] - 80, HOLE_S[0] + 40, ease(u)), lerp(860, HOLE_S[1] + 20, ease(u))
    return 900 + math.sin(tt * 1.7) * 200, 700

def light_map(set_, sh, tt, cam, lights):
    x0, y0, z = cam; W3 = lambda px, py: ((px - x0) * z, (py - y0) * z)
    torches = [l for l in lights if len(l) > 5]
    if set_ == "studio":
        m = np.full((LH, LW, 3), 0.1, np.float32) * COOL
        px, py = scan_pt(tt, sh); X, Y = W3(px, py)
        m += 2.0 * glow(X, Y, 300 * z)[..., None] * WARM
        for l in torches: m += 0.7 * glow(l[0], l[1], l[2] * 0.6)[..., None] * WARM
    elif set_ == "tunnel":
        m = np.full((LH, LW, 3), 0.42, np.float32) * WARM
        for lx, ly, R in LANT:
            X, Y = W3(lx, ly); m += (0.85 + 0.08 * math.sin(tt * 9 + lx)) * glow(X, Y, R * z)[..., None] * np.array([1.2, 0.9, 0.6], np.float32)
        for l in torches:
            m += 0.6 * glow(l[0], l[1], l[2] * 0.6)[..., None] * WARM
            if l[6] == "abdo":   # Abdo's torch sweeps toward the hole side
                u = kk(tt, ABTURN - 0.3, ABTURN + 0.5); tx = lerp(1300, 760, ease(u)); X, Y = W3(tx, 900)
                m += 1.3 * glow(X, Y, 200 * z)[..., None] * WARM
    elif set_ == "basement":
        d = dawn(tt)
        m = np.full((LH, LW, 3), lerp(0.55, 1.0, d), np.float32) * (COOL * (1 - d) + d)
        if tt >= BEAMON:
            b = ease(kk(tt, BEAMON, BEAMON + 1.0)); X, Y = W3(*BEAM)
            m += 0.9 * b * glow(X, Y, 170 * z)[..., None] * np.array([1.15, 1.0, 0.75], np.float32)
    else:
        return None
    for l in lights:
        if len(l) == 5:
            X, Y, R, inten, col = l; m += inten * glow(X, Y, R)[..., None] * np.array(col, np.float32)
    lm = np.clip(m / 1.3, 0, 1)
    return Image.fromarray((lm * 255).astype(np.uint8), "RGB").resize((W, H), Image.BILINEAR)

def props(img, set_, tt, cam, sh):
    x0, y0, z = cam; S = SS * z; d = ImageDraw.Draw(img, "RGBA")
    W2 = lambda wx, wy: ((wx - x0) * S, (wy - y0) * S)
    lw = lambda v: max(1, int(v * S))
    if set_ == "studio":
        cx_, cy_ = W2(SAFE[0], SAFE[1] + 12)
        d.ellipse([cx_ - 95 * S, cy_ - 24 * S, cx_ + 95 * S, cy_ + 24 * S], fill=(150, 125, 95, 150))
        for off in (-26, 26):   # drag marks: down toward the camera, then along the floor to the hole in the left wall
            pts = [W2(SAFE[0] + off + i * -40, SAFE[1] + 20 + i * 18 + math.sin(i) * 6) for i in range(10)]
            pts += [W2(lerp(SAFE[0] - 400, HOLE_S[0] + 60, i / 12) + off * 0.3, lerp(SAFE[1] + 200, HOLE_S[1] + 120, i / 12) + off) for i in range(13)]
            d.line(pts, fill=(20, 14, 10, 235), width=lw(7))
            d.line([(x_ + 3 * S, y_ - 3 * S) for x_, y_ in pts], fill=(210, 180, 140, 170), width=lw(2))
        hx, hy = W2(*HOLE_S)   # broken hole in the left wall
        pts = [(hx + math.cos(a) * (140 + 25 * math.sin(a * 5)) * S, hy + math.sin(a) * (170 + 20 * math.cos(a * 7)) * S) for a in np.linspace(0, 2 * math.pi, 24)]
        d.polygon(pts, fill=(6, 5, 4, 255), outline=(90, 60, 40, 255))
        for i in range(10):
            a = i * 0.63; bx, by = hx + math.cos(a) * 175 * S, hy + math.sin(a) * 200 * S
            d.rectangle([bx - 18 * S, by - 9 * S, bx + 18 * S, by + 9 * S], fill=(130, 70, 45, 255), outline=(50, 30, 20, 255))
    if set_ == "tunnel":
        if MOUSE - 0.2 <= tt < MOUSE + 1.4:
            u = kk(tt, MOUSE - 0.2, MOUSE + 1.4); X, Y = W2(lerp(1200, 250, u), 990); s_ = 1.1 * S
            d.ellipse([X - 22 * s_, Y - 12 * s_, X + 22 * s_, Y + 12 * s_], fill=(110, 105, 100, 255), outline=(30, 30, 30, 255), width=lw(2))
            d.ellipse([X - 34 * s_, Y - 10 * s_, X - 16 * s_, Y + 6 * s_], fill=(110, 105, 100, 255), outline=(30, 30, 30, 255), width=lw(2))
            d.line([(X + 22 * s_, Y), (X + 50 * s_, Y - 8 * s_ * math.sin(tt * 30))], fill=(60, 50, 50, 255), width=lw(2))
        if tt < CHASE[0] + 0.5:   # dirt flying from Abdo's pick
            ph = (tt * 2.2) % 1
            if ph < 0.35:
                r_ = np.random.default_rng(int(tt * 2.2))
                for i in range(8):
                    X, Y = W2(1640 + r_.uniform(-40, 40) + ph * 200, 900 - ph * 300 * r_.uniform(0.3, 1) + ph * ph * 600)
                    d.ellipse([X - 4 * S, Y - 4 * S, X + 4 * S, Y + 4 * S], fill=(80, 55, 35, 255))
        if CHASE[0] <= tt < CHASE[1] + 2:   # dust after the chase
            u = kk(tt, CHASE[0], CHASE[1] + 2); dl = Image.new("RGBA", img.size, (0, 0, 0, 0)); dd = ImageDraw.Draw(dl)
            for i in range(12):
                X, Y = W2(940 + math.sin(i * 2.3) * 220 * u, 560 + i * 25); r = (60 + 80 * u) * S
                dd.ellipse([X - r, Y - r * 0.5, X + r, Y + r * 0.5], fill=(150, 120, 90, int(40 * (1 - u))))
            dl = dl.filter(ImageFilter.GaussianBlur(int(16 * S))); img.paste(dl, (0, 0), dl)
    if set_ == "basement" and tt >= BEAMON:
        b = ease(kk(tt, BEAMON, BEAMON + 1.0)); bl = Image.new("RGBA", img.size, (0, 0, 0, 0)); bd = ImageDraw.Draw(bl)
        a1, a2 = W2(WIN[0] - 80, WIN[1]), W2(WIN[0] + 90, WIN[1])
        c1, c2 = W2(BEAM[0] - 110, BEAM[1] - 10), W2(BEAM[0] + 110, BEAM[1] + 10)
        bd.polygon([a1, a2, c2, c1], fill=(255, 240, 190, int(70 * b)))
        r_ = np.random.default_rng(int(tt * 4))
        for i in range(30):   # dust in the beam
            v = r_.uniform(0, 1); X = lerp(lerp(a1[0], a2[0], 0.5), lerp(c1[0], c2[0], 0.5), v) + r_.uniform(-60, 60) * S
            Y = lerp(a1[1], c1[1], v); bd.ellipse([X - 2 * S, Y - 2 * S, X + 2 * S, Y + 2 * S], fill=(255, 250, 220, int(160 * b)))
        bl = bl.filter(ImageFilter.GaussianBlur(int(8 * S))); img.paste(bl, (0, 0), bl)
        X, Y = W2(*BEAM)   # the lit tile: a crescent shows only inside the sun spot
        if tt < HAND[0]:
            d.ellipse([X - 26 * S, Y - 12 * S, X + 26 * S, Y + 12 * S], fill=(120, 80, 40, int(150 * b)))
            d.ellipse([X - 16 * S, Y - 14 * S, X + 30 * S, Y + 10 * S], fill=(225, 200, 150, int(150 * b)))
        else:
            d.rectangle([X - 60 * S, Y - 26 * S, X + 60 * S, Y + 26 * S], fill=(8, 6, 5, 255))

def ltr(img, x, y, s, size, fill, stroke=(10, 10, 10), sw=3):
    ImageDraw.Draw(img).text((x, y), s, font=ImageFont.truetype(FONT, size), fill=fill, anchor="mm", direction="ltr", stroke_width=sw, stroke_fill=stroke)

# ---------- inserts ----------
def ins_bg(col=(30, 24, 18)):
    fr = Image.new("RGB", (W, H), col); return fr, ImageDraw.Draw(fr, "RGBA")
def ant_card(tt, sh):
    """antenna plug: Safeeh's head, Shatta's hand slots the antenna in, spark, eyes on"""
    fr = ImageEnhance.Brightness(bg_crop(SRC["tunnel"], (700, 300, 1.6), True).resize((W, H)).filter(ImageFilter.GaussianBlur(9))).enhance(0.45)
    tmp = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(tmp)
    on = tt >= PLUG
    draw_safeeh(p, W * 0.47, H * 1.95, 3.2, tt, "green" if on else "off", (1.0 if tt > PLUG + 0.35 else [1, 0, 1, 0.3, 1][min(4, int((tt - PLUG) / 0.08))]) if on else 0.0,
                0.0, 0, None, "down", 0.0, 0.0, not on, antenna=on)
    fr.paste(tmp.resize((W, H), Image.LANCZOS), (0, 0), tmp.resize((W, H), Image.LANCZOS))
    d = ImageDraw.Draw(fr, "RGBA")
    sx, sy = W * 0.47 + 26 * 3.2, H * 1.95 - 300 * 3.2 + 30   # socket
    if not on:
        u = ease(kk(tt, sh["start"], PLUG)); ax, ay = lerp(sx + 260, sx + 10, u), lerp(sy - 260, sy - 70, u)
        d.line([(ax + 300, ay - 80), (ax + 20, ay + 20)], fill=(22, 22, 22, 255), width=26)   # Shatta's arm
        d.line([(ax, ay), (ax + 18, ay - 120)], fill=(150, 156, 162, 255), width=12)
        d.ellipse([ax + 2, ay - 150, ax + 36, ay - 116], fill=(255, 70, 50, 255), outline=(30, 20, 20, 255), width=3)
    elif tt < PLUG + 0.5:
        u = kk(tt, PLUG, PLUG + 0.5)
        for i in range(10):
            a = i * 0.63; L = 40 + 120 * u
            d.line([(sx, sy - 60), (sx + math.cos(a) * L, sy - 60 + math.sin(a) * L)], fill=(255, 240, 150, int(255 * (1 - u))), width=5)
    return fr
TILE_N = [("النجمة", "star"), ("الوردة", "flower"), ("الهلال", "moon"), ("السادة", "plain")]
def tiles_card(tt, sh):
    fr, d = ins_bg((26, 22, 18))
    k = ease(kk(tt, sh["start"], sh["start"] + 0.5))
    for i, (nm, kind) in enumerate(TILE_N):
        cx = W / 2 + (i - 1.5) * 420; cy = H / 2 - 40 + (1 - k) * 300 * (1 + i * 0.2); R = 170
        d.rectangle([cx - R, cy - R, cx + R, cy + R], fill=(206, 190, 160, 255), outline=(70, 55, 40, 255), width=8)
        col = (60, 70, 110, 255)
        if kind == "star":
            pts = [(cx + math.cos(a) * (110 if j % 2 == 0 else 50), cy + math.sin(a) * (110 if j % 2 == 0 else 50)) for j, a in enumerate(np.linspace(-math.pi / 2, 1.5 * math.pi, 17)[:-1])]
            d.polygon(pts, fill=col)
        elif kind == "flower":
            for j in range(6):
                a = j * math.pi / 3; d.ellipse([cx + math.cos(a) * 60 - 42, cy + math.sin(a) * 60 - 42, cx + math.cos(a) * 60 + 42, cy + math.sin(a) * 60 + 42], fill=col)
            d.ellipse([cx - 30, cy - 30, cx + 30, cy + 30], fill=(170, 60, 50, 255))
        elif kind == "moon":
            d.ellipse([cx - 100, cy - 100, cx + 100, cy + 100], fill=col); d.ellipse([cx - 55, cy - 115, cx + 125, cy + 75], fill=(206, 190, 160, 255))
        for c in ((-R + 22, -R + 22), (R - 22, -R + 22), (-R + 22, R - 22), (R - 22, R - 22)): d.ellipse([cx + c[0] - 6, cy + c[1] - 6, cx + c[0] + 6, cy + c[1] + 6], fill=(70, 55, 40, 255))
        d.ellipse([cx - R - 30, cy - R - 30, cx - R + 50, cy - R + 50], fill=(255, 214, 90, 255), outline=(30, 10, 5, 255), width=5)
        ltr(fr, cx - R + 10, cy - R + 10, str(i + 1), 50, (30, 10, 5), (255, 214, 90), 1)
        text(fr, cx, cy + R + 60, nm, 60, (255, 214, 90), (30, 10, 5), 4)
    return fr
def lift_card(tt, sh):
    fr, d = ins_bg((40, 32, 24))
    u = ease(kk(tt, sh["start"] + 0.1, sh["start"] + 0.9)); cx, cy = W / 2, H / 2 + 60
    for i in range(-3, 4):
        for j in range(-2, 3):
            if i == 0 and j == 0: continue
            d.rectangle([cx + i * 300 - 145, cy + j * 300 - 145, cx + i * 300 + 145, cy + j * 300 + 145], fill=(150, 130, 100, 255), outline=(60, 48, 36, 255), width=6)
    d.rectangle([cx - 145, cy - 145, cx + 145, cy + 145], fill=(10, 8, 6, 255))
    d.rounded_rectangle([cx - 110, cy - 80, cx + 110, cy + 90], 10, fill=(120, 126, 134, 255), outline=(40, 40, 44, 255), width=6)   # the box
    for x_ in (-80, 80): d.ellipse([cx + x_ - 8, cy - 60, cx + x_ + 8, cy - 44], fill=(70, 70, 76, 255))
    tile_y = cy - 400 * u
    d.rectangle([cx - 150 + 60 * u, tile_y - 150, cx + 150 + 60 * u, tile_y + 150 - 120 * u], fill=(225, 210, 175, 255), outline=(60, 48, 36, 255), width=6)
    d.line([(cx + 600, cy + 700), (cx + 120 + 60 * u, tile_y + 40)], fill=(22, 22, 22, 255), width=28)   # Shatta's arm lifting
    gl = Image.new("RGBA", fr.size, (0, 0, 0, 0)); gd = ImageDraw.Draw(gl)
    gd.ellipse([cx - 600, cy - 500, cx + 400, cy + 300], fill=(255, 240, 190, 90)); gl = gl.filter(ImageFilter.GaussianBlur(60)); fr.paste(gl, (0, 0), gl)
    return fr
def hand_card(tt, sh):
    fr = lift_card(sh["start"] + 2.0, sh); d = ImageDraw.Draw(fr, "RGBA"); cx, cy = W / 2, H / 2 + 60
    u = ease(kk(tt, sh["start"], GRAB)); v = ease(kk(tt, GRAB + 0.2, sh["end"]))
    hy = lerp(-300, cy - 40, u) - 700 * v
    if v > 0:   # the box goes up with the hand
        d.rectangle([cx - 145, cy - 145, cx + 145, cy + 145], fill=(10, 8, 6, 255))
        d.rounded_rectangle([cx - 110, hy - 40, cx + 110, hy + 130], 10, fill=(120, 126, 134, 255), outline=(40, 40, 44, 255), width=6)
    d.polygon([(cx - 70, -20), (cx + 70, -20), (cx + 60, hy - 60), (cx - 60, hy - 60)], fill=(22, 22, 28, 255))   # black sleeve
    d.rectangle([cx - 64, hy - 90, cx + 64, hy - 55], fill=(240, 240, 240, 255))   # white cuff
    d.ellipse([cx - 60, hy - 70, cx + 60, hy + 40], fill=(22, 22, 22, 255))
    rx, ry = cx + 30, hy - 10   # gold ring + glint
    d.ellipse([rx - 26, ry - 14, rx + 26, ry + 14], outline=(235, 190, 60, 255), width=10)
    if int(tt * 6) % 2: d.polygon([(rx + 30, ry - 40), (rx + 36, ry - 20), (rx + 56, ry - 14), (rx + 36, ry - 8), (rx + 30, ry + 12), (rx + 24, ry - 8), (rx + 4, ry - 14), (rx + 24, ry - 20)], fill=(255, 250, 200, 255))
    return fr
FOLLOW = {k: Image.open(ROOT + f"/brand/follow/{k}.png").convert("RGB") for k in ("yt", "tt", "ig", "fb")}
BTN = {"yt": ((25, 414, 551, 477), "Subscribed", (230, 230, 230), (20, 20, 20)),
       "tt": ((18, 269, 244, 336), "Following", (235, 235, 235), (30, 30, 30)),
       "ig": ((19, 351, 252, 403), "Following", (239, 239, 239), (20, 20, 20)),
       "fb": ((19, 659, 281, 716), "متابَع ✓", (228, 230, 235), (20, 20, 20))}
def phone_card(tt, sh, plat="yt", CW_=W, CH_=H):
    fr = Image.new("RGB", (CW_, CH_), (0, 0, 0))
    bgc = bg_crop(SRC["basement"], (600, 100, 1.6), True).resize((W, H))
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
        text(fr, W / 2, H / 2 - 230, "الحلقة 9 بكرة: الصندوق", 96, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 - 100, "أنهي بلاطة؟ اكتبوها في الكومنتات", 52, g((235, 235, 235)))
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
    if ANS + 1.0 <= tt < ANS + DUR["K03"] + 0.6:
        d.rounded_rectangle([cx - 430 * sc, y - 50 * sc, cx + 430 * sc, y + 50 * sc], int(22 * sc), fill=(20, 60, 30, 220), outline=(120, 230, 120, 255), width=4)
        text(fr, cx, y, "التصويت: فهمي صادق ✓", int(42 * sc), (200, 255, 200))
    if Z0 + DUR["K16"] * 0.5 <= tt < Z0 + DUR["K16"] + 0.3:
        d.rounded_rectangle([cx - 150 * sc, y - 50 * sc, cx + 150 * sc, y + 50 * sc], int(22 * sc), fill=(60, 20, 20, 220), outline=(255, 120, 90, 255), width=4)
        ltr(fr, cx, y, "0%", int(56 * sc), (255, 160, 120))
    if TL[0] + 0.4 <= tt < TL[1]:
        hrs = ["2:00", "3:00", "4:00", "5:00", "6:00"][min(4, int(kk(tt, TL[0] + 0.4, TL[1]) * 5))]
        d.rounded_rectangle([cx - 150 * sc, y - 46 * sc, cx + 150 * sc, y + 46 * sc], int(20 * sc), fill=(10, 10, 14, 200), outline=(230, 200, 120, 255), width=3)
        ltr(fr, cx, y, hrs, int(50 * sc), (255, 230, 170))

PUZ_TXT = "أنهي بلاطة؟ النجمة، الوردة، الهلال، ولا السادة؟"
def puzzle_box(fr, tt, cx, y, sc=1.0):
    d = ImageDraw.Draw(fr, "RGBA"); k = ease(kk(tt, PUZ + 0.2, PUZ + 0.7))
    d.rounded_rectangle([cx - 640 * sc, y - 70 * sc, cx + 640 * sc, y + 90 * sc], int(26 * sc), fill=(20, 20, 30, int(225 * k)), outline=(255, 214, 90, int(255 * k)), width=5)
    text(fr, cx, y - 15 * sc, "لغز النهارده: " + PUZ_TXT, int(40 * sc), (255, 214, 90))
    text(fr, cx, y + 45 * sc, "ركزوا في شعاع الشمس... اكتبوا في الكومنتات", int(34 * sc), (235, 235, 235))

TINT = {"studio": (200, 190, 200), "tunnel": (255, 215, 170), "basement": (255, 236, 210)}
def frame(tt, plat="yt"):
    sh = shot_at(tt); set_ = sh["set"]
    if set_ in ("title", "endcard"): return finish(card(set_, tt, sh), tt)
    if set_ == "black": return Image.new("RGB", (W, H), (0, 0, 0))
    if set_ == "phone": return finish(phone_card(tt, sh, plat), tt)
    for k_, fn in (("antins", ant_card), ("tilesins", tiles_card), ("liftins", lift_card), ("handins", hand_card)):
        if sh.get(k_): return finish(fn(tt, sh), tt, True)
    cam = cam_at(sh, tt)
    img = bg_frame(set_, cam, sh, tt)
    layer, lights = draw_scene_chars(set_, tt, cam, sh)
    tint = TINT.get(set_, (255, 244, 225))
    if set_ == "basement": tint = tuple(int(lerp(a, b, dawn(tt))) for a, b in zip((150, 165, 225), tint))
    layer = tint_layer(layer, tint, 0.97)
    img.paste(layer, (0, 0), layer)
    props(img, set_, tt, cam, sh)
    fr = img.resize((W, H), Image.LANCZOS)
    lm = light_map(set_, sh, tt, cam, lights)
    if lm is not None:
        fr = ImageChops.multiply(fr, lm)
        fr = ImageEnhance.Brightness(fr).enhance({"studio": 1.35, "tunnel": 1.3, "basement": 1.2}.get(set_, 1.0))
    dark = set_ in ("studio", "tunnel") or (set_ == "basement" and dawn(tt) < 0.5)
    return finish(fr, tt, dark)

def lowpass(x, fc):
    from numpy.fft import rfft, irfft
    X = rfft(x); fq = np.fft.rfftfreq(len(x), 1 / SR); X[fq > fc] *= 0.08; return irfft(X, len(x)).astype(np.float32)

def build_audio(path="mix.wav"):
    buf = np.zeros(int(TOTAL * SR) + SR * 3, dtype=np.float32)
    dr = drone(TOTAL + 1); env = np.zeros(len(dr), np.float32)
    for a_, b_ in ((0, TITLE), (TW[0], CHASE[0]), (HAND[0], TOTAL - 4.9)):
        env[int(a_ * SR):int(b_ * SR)] = 1.0
    env = np.convolve(env, np.ones(4410) / 4410, mode="same")
    mix_into(buf, dr * env, 0, 1.2)
    r = np.random.default_rng(9)
    S = {"boom": sfx_boom(), **SFXF}
    for t0, nme, g in sfx:
        if nme in S and g > 0: mix_into(buf, S[nme], t0, g)
    # digging: pick hits (muffled through the wall in the studio, clear in the tunnel)
    tb = np.arange(int(SR * 0.3)) / SR
    hit = (np.sin(2 * np.pi * 180 * tb) * np.exp(-tb * 30) + np.convolve(r.normal(0, 1, len(tb)), np.ones(8) / 8, mode="same") * np.exp(-tb * 22) * 0.8).astype(np.float32)
    tk = 0.2
    while tk < CHASE[0]:
        st = shot_at(tk)["set"]
        h = lowpass(hit, 900) * 0.6 if st == "studio" or tk < TW[0] else hit
        if not (CRAWL[0] <= tk < ANT[1]) or st != "tunnel" or tk < ABTURN - 0.3 or tk > K09T + DUR["K09"]:
            mix_into(buf, h, tk, 0.35)
        tk += 1 / 1.1
    # sneaky pizzicato under the crawl
    for i in range(int((CRAWL[1] - CRAWL[0]) / 0.4)):
        f = [196, 0, 233, 0, 196, 0, 175, 0][i % 8]
        if f: tp = np.arange(int(SR * 0.2)) / SR; mix_into(buf, np.sin(2 * np.pi * f * tp) * np.exp(-tp * 25) * 0.12, CRAWL[0] + i * 0.4, 1.0)
    # chase: fast comic tuba-ish bass + robot servo steps
    for i in range(int((CHASE[1] - CHASE[0]) / 0.25)):
        f = [110, 131, 147, 131][i % 4]; tp = np.arange(int(SR * 0.2)) / SR
        mix_into(buf, np.sign(np.sin(2 * np.pi * f * tp)) * np.exp(-tp * 14) * 0.05, CHASE[0] + i * 0.25, 1.0)
    # comic stings: the gag, the 0%
    for t_, notes in ((T("K13") + 0.3, [392, 370, 349, 330]), (Z0 + DUR["K16"] * 0.5, [523, 494, 440, 392])):
        for i, f in enumerate(notes):
            tt_ = np.arange(int(SR * 0.4)) / SR
            mix_into(buf, np.sin(2 * np.pi * f * tt_) * np.exp(-tt_ * 12) * 0.09, t_ + i * 0.18, 1.0)
    # dawn: birds + a warm pad when the beam appears
    for i in range(14):
        t0 = BEAMON - 1.2 + i * 0.45 + r.uniform(0, 0.2); tp = np.arange(int(SR * 0.12)) / SR
        mix_into(buf, np.sin(2 * np.pi * (2600 + 900 * np.sin(tp * 60)) * tp) * np.exp(-tp * 20) * 0.04, t0, 1.0)
    tp = np.arange(int(SR * 4.0)) / SR
    pad = (np.sin(2 * np.pi * 262 * tp) + np.sin(2 * np.pi * 330 * tp) + np.sin(2 * np.pi * 392 * tp)) * 0.02 * np.minimum(1, tp) * np.minimum(1, (4 - tp))
    mix_into(buf, pad.astype(np.float32), BEAMON, 1.0)
    # tension rise: hand → Pasha
    a_, b_ = HAND[0], TOTAL - 4.9
    ts = np.arange(int((b_ - a_) * SR)) / SR
    mix_into(buf, ((np.sin(2 * np.pi * (98 + 50 * ts / ts[-1]) * ts) + 0.5 * np.sin(2 * np.pi * (147 + 70 * ts / ts[-1]) * ts)) * 0.05).astype(np.float32), a_, 1.0)
    tsx = np.arange(int(SR * 0.25)) / SR
    for st, g in STEPS:
        nz = np.convolve(r.normal(0, 1, len(tsx)), np.ones(12) / 12, mode="same")
        mix_into(buf, (np.sin(2 * np.pi * 80 * tsx) * np.exp(-tsx * 30) * 0.9 + nz * np.exp(-tsx * 25) * 0.9) * 0.6, st, g)
    for st, k in lines:
        a = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8
        mix_into(buf, a, st, 1.0)
    buf = buf[:int(TOTAL * SR)]
    buf = np.clip(buf / max(1e-6, np.abs(buf).max()) * 0.95, -1, 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((buf * 32767).astype(np.int16).tobytes())
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
    if PUZ <= tt < PUZ_END: puzzle_box(bgv, tt, 540, 1640, 0.8)
    return bgv

def finish(fr, tt, dark=False):
    fr = ImageChops.multiply(fr, VIG_DARK if dark else VIG)
    a = np.asarray(fr, np.float32)
    g = GRAIN[int(tt * 6) % len(GRAIN)]
    g = np.repeat(np.repeat(g, 4, 0), 4, 1)[..., None]
    return Image.fromarray(np.clip(a + g, 0, 255).astype(np.uint8))

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
        if PUZ <= tt < PUZ_END: puzzle_box(h, tt, W / 2, 130)
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
