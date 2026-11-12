import sys, os, math, subprocess, wave
sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter, ImageFont
from engine import *
from locations import loc

# م2 ح9 «الصندوق» — built from s2e8/ep8.py, Episode checklist (docs/directing.md) + fixed locations (docs/locations.md).
# New vs Ep8: a planned heist with 4 roles (whole building), the plan told over a drawn "plan board" insert, Sawsan's live
# phone-UI POV, the speaker under the car seat (red LED + robot voice) that makes Abdo flee, the box insert (old photo of
# young Roshdy + a covered pharaoh figure + a «الدور الأخير» key = Season 3 tease), Roshdy's letter voice-over, and the
# biggest cliff of the season: a loader's headlights at the end of the street.
os.chdir(ROOT + "/s2e9")
SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(909)
SEASON = "سر البدروم"
EPT = "الحلقة 9: الصندوق"

SUB = {
 "M01": "الصندوق معايا... واللعبة خلصت.", "M02": "افتحه يا باشا!... بلاش نستنى!", "M03": "مش هنا يا عبده... بالليل، في المكتب.",
 "M04": "إجابة لغز امبارح: بلاطة الهلال!... كانت باينة في شعاع الشمس.", "M05": "لقيناه... وراح منّا.",
 "M06": "احتمال نرجعه: خمسة في المية بس.", "M07": "أنا عندي خطة!", "M08": "خطة تانية يا فهمي؟!",
 "M09": "السماعات بتاعتي... اللي كنت بخوفكم بيها زمان.", "M10": "هنحط سماعة صغيرة في عربية الباشا... وصفيح يتكلم فيها.",
 "M11": "وأنا أعمل معاه لايف... عشان ينزل من العربية!", "M12": "وأنا... هفضل صاحي.", "M13": "تمام... يا رشدي.", "M14": "رشدي مين؟!",
 "M15": "أهلاً يا جماعة!... معانا لايف... الباشا بنفسه!", "M16": "عبده!... أنا جوه العربية!", "M17": "الروبوت!... يا ماما!",
 "M18": "الصندوق معايا!... اجروا!", "M19": "فاضي!... مافيهوش أسطوانة!", "M20": "فيه صورة لعم رشدي... ومفتاح غريب!",
 "M21": "لو لقيتوا الصندوق ده فاضي... ما تزعلوش. السر الأكبر... لسه ما ابتداش.",
 "M22": "رشدي نقل الأسطوانة... للمكان اللي بيغني لوحده.",
 "M23": "لغز النهارده: إيه اللي بيغني لوحده في العمارة؟ افتكروا الموسم الأول... واكتبوا في الكومنتات!",
 "M24": "اعملوا فولو... وإلا الشبشب جاهز!", "M25": "يا عبده... هات اللودر. العمارة دي... هتتهد الصبح.",
}
WHO = {"M01": "pasha", "M02": "abdo", "M03": "pasha", "M04": "tota", "M05": "shatta", "M06": "zalata", "M07": "fahmy", "M08": "nana",
       "M09": "fahmy", "M10": "fahmy", "M11": "sawsan", "M12": "bondo2", "M13": "safeeh", "M14": "fahmy", "M15": "sawsan", "M16": "safeeh",
       "M17": "abdo", "M18": "shatta", "M19": "tota", "M20": "zalata", "M21": "roshdy", "M22": "safeeh", "M23": "tota", "M24": "nana", "M25": "pasha"}
EXPR = {"M01": "smug", "M02": "happy", "M03": "smug", "M04": [(0, "neutral"), (0.6, "smug")], "M05": "sad", "M06": "flat", "M07": "happy",
        "M08": "angry", "M09": "sad", "M10": "smug", "M11": "happy", "M12": "sleepy", "M14": "shock", "M15": "happy", "M17": "scared",
        "M18": "happy", "M19": "shock", "M20": "neutral", "M23": [(0, "neutral"), (0.6, "smug")], "M24": "angry", "M25": "angry"}
ARMS = {"M02": "talk", "M04": "point", "M05": "down", "M06": "hold", "M08": "hips", "M09": "talk", "M10": "point", "M11": "up",
        "M12": "hips", "M14": "talk", "M17": "up", "M19": "up", "M23": "point", "M24": "point"}

def _aud(k): return load_audio(f"audio/{k}.mp3")
AUD = {k: _aud(k) for k in SUB}
ENV = {k: envelope(v) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}
SFXF = {n: load_audio(ROOT + f"/s2e4/sfx/{n}.mp3") for n in ("whoosh", "creak", "slam", "switch", "clang", "stinger", "servo",
                                                             "steps_metal", "unlock", "knocks", "car", "snore")}

lines, sfx, shots, jumps, shakes = [], [], [], {}, []
def say(t, k): lines.append((t, k)); return t + DUR[k]
def fx(t, n, g=1.0): sfx.append((t, n, g))
def jump(w, t): jumps.setdefault(w, []).append(t)
def shot(set_, s, e, c0, c1=None, **kw): shots.append(dict(set=set_, start=s, end=e, c0=c0, c1=c1 or c0, **kw))
def cut(t, g=0.4): fx(t - 0.12, "whoosh", g)
def T(k): return [st for st, kk_ in lines if kk_ == k][0]
KIDS = ("shatta", "zalata", "tota")
CHASE = (-9, -8); SNAP = -1   # (helpers shared with ep8)

# ---------------- world ----------------
CAR_P = (1380, 880, 2.3); CAR_A = (560, 900, 2.4); SPK = (980, 905)            # car interior (carday / carin)
LV = {"tota": (820, 1010, 1.9), "shatta": (1020, 1015, 1.9), "zalata": (1220, 1010, 1.9)}
NANA_L = (560, 1000, 1.9); FAH_L = (1500, 1000, 1.95); BON_L = (1730, 1000, 1.85); SAW_L = (170, 1000, 1.9); SAF_L = (360, 930, 1.4)
SAW_S = (620, 880, 1.45); PAS_S0 = (1340, 800, 1.25); PAS_S = (900, 865, 1.45); SDOOR = (330, 800, 1.05); CARDOOR = (1240, 805, 1.22)
LK = {"tota": (620, 1000, 1.9), "shatta": (840, 1010, 1.9), "zalata": (1060, 1000, 1.9)}; SAF_K = (1330, 985, 1.5); NANA_K = (380, 1000, 1.9)
PAS_C = (1240, 820, 1.35)

def CU(who, pos, z=2.2, dx=0, dy=0):
    x, y, s = pos
    if who == "safeeh":
        return (x + dx, y - 250 * s + H / (2 * (z + 0.45)) - 110 * s - dy - 130 * s, z + 0.45)
    S = s * CH[who]["scale"]
    z += 0.45
    if who == "tota": z *= 1.3; dx -= 50
    if who == "fahmy": z += 0.4
    hy = y - 190 * S
    return (x + dx, hy + H / (2 * z) - 1.45 * 46 * S - 25 - dy, z)

t = 0.0
# ===== 0. HOOK — the Pasha's car, the box on his lap =====
shot("car", 0, 1.2, (1480, 700, 2.5), (1470, 690, 2.8), boxglint=True); fx(0.0, "stinger", 0.6)
s = 0.2; t = say(s, "M01") + 0.1
shot("car", 1.2, t, CU("pasha", CAR_P, 1.6), CU("pasha", CAR_P, 1.75))
s = t; t = say(t, "M02") + 0.1
shot("car", s, t, CU("abdo", CAR_A, 1.4), CU("abdo", CAR_A, 1.55))
s = t; t = say(t, "M03") + 0.3; CLOSE = s + 1.2; fx(CLOSE, "slam", 0.5)
shot("car", s, t, (960, 560, 1.05), (960, 560, 1.12))
cut(t, 0.3); TITLE = t; shot("title", t, t + 2.0, None); t += 2.0
# ===== 1. LIVING ROOM (day): answer + low spirits =====
s = t; t = say(t + 0.1, "M04") + 0.2; ANS = s
shot("living", s, s + 3.0, CU("tota", LV["tota"], 1.5), CU("tota", LV["tota"], 1.62))
shot("living", s + 3.0, t, None, tileins=True)
s = t; t = say(t, "M05") + 0.2
shot("living", s, t, CU("shatta", LV["shatta"], 1.6), CU("shatta", LV["shatta"], 1.8))
s = t; t = say(t, "M06") + 0.2; P5 = s
shot("living", s, t, CU("zalata", LV["zalata"], 1.7), CU("zalata", LV["zalata"], 1.85))
KNOCK = t + 0.1; fx(KNOCK, "knocks", 1.0)
shot("living", t, t + 1.2, (1000, 580, 1.05), (1000, 580, 1.08)); t += 1.2
s = t; t = say(t, "M07") + 0.1
FIN = (t, t + 2.4); fx(t + 0.1, "creak", 0.8)
shot("living", s, FIN[1], (1250, 600, 1.2), (1300, 600, 1.25)); t = FIN[1]
s = t; t = say(t, "M08") + 0.2
shot("living", s, t, CU("nana", NANA_L, 1.6), CU("nana", NANA_L, 1.75))
s = t; t = say(t, "M09") + 0.2
shot("living", s, t, CU("fahmy", FAH_L, 1.6), CU("fahmy", FAH_L, 1.75))
s = t; t = say(t, "M10") + 0.2; PLAN = (s, t)
shot("living", s, t, None, planins=True)
SWIN = (t, t + 1.4)
s = t; t = say(t + 0.6, "M11") + 0.2
shot("living", s, t, CU("sawsan", SAW_L, 1.6, 60), CU("sawsan", SAW_L, 1.75, 60))
s = t; t = say(t, "M12") + 0.2
shot("living", s, t, CU("bondo2", BON_L, 1.6, -40), CU("bondo2", BON_L, 1.75, -40))
s = t; t = say(t, "M13") + 0.1; fx(s - 0.2, "servo", 0.6)
shot("living", s, t, CU("safeeh", SAF_L, 1.5), CU("safeeh", SAF_L, 1.6))
s = t; t = say(t, "M14") + 0.4; jump("fahmy", s)
shot("living", s, t, CU("fahmy", FAH_L, 1.6), CU("fahmy", FAH_L, 1.9), ease="crash")
# ===== 2. THE HEIST (night street) =====
cut(t, 0.3); NIGHT = (t, t + 2.6); fx(t + 0.3, "car", 0.5)
shot("street", t, NIGHT[1], (1100, 600, 1.1), (1050, 620, 1.18)); t = NIGHT[1]
s = t; t = say(t, "M15") + 0.2; LIVE = s
shot("street", s, s + 1.6, None, liveins=True)
PWALK = (s + 1.0, t + 1.0)
shot("street", s + 1.6, t + 1.2, (1000, 640, 1.3), (900, 660, 1.4)); t += 1.2
SPKON = t; fx(t + 0.1, "switch", 0.8)
shot("carin", t, t + 1.2, (SPK[0], SPK[1] - 80, 2.6), (SPK[0], SPK[1] - 80, 2.9)); t += 1.2
s = t; t = say(t, "M16") + 0.1; shakes.append((s, 6))
shot("carin", s, t, (900, 620, 1.3), (900, 620, 1.4))
s = t; t = say(t, "M17"); RUN = (s + 0.4, s + 3.0); fx(s + 0.3, "slam", 0.9); jump("abdo", s)
shot("carin", s, s + 0.9, CU("abdo", CAR_P, 1.4), CU("abdo", CAR_P, 1.6), ease="crash")
shot("street", s + 0.9, RUN[1] + 0.3, (1350, 640, 1.2), (1450, 640, 1.25)); t = RUN[1] + 0.3
GRAB = (t, t + 3.2)
shot("street", t, GRAB[1], (1050, 650, 1.25), (1050, 650, 1.3)); t = GRAB[1]
s = t; t = say(t, "M18") + 0.2; jump("shatta", s)
shot("street", s, t, CU("shatta", (430, 850, 1.4), 1.4), CU("shatta", (430, 850, 1.4), 1.55))
# ===== 3. LOBBY (night): the box is empty =====
cut(t, 0.3); OPEN = (t, t + 2.4); fx(t + 1.3, "unlock", 1.0); fx(t + 1.6, "creak", 0.6)
shot("lobby", t, t + 1.2, (850, 640, 1.2), (850, 660, 1.3))
shot("lobby", t + 1.2, OPEN[1], None, boxins=True, empty=True); t = OPEN[1]
s = t; t = say(t, "M19") + 0.1; jump("tota", s)
shot("lobby", s, t, CU("tota", LK["tota"], 1.5), CU("tota", LK["tota"], 1.7), ease="crash")
s = t; t = say(t, "M20") + 0.2
shot("lobby", s, t, None, boxins=True, empty=False)
s = t; t = say(t + 0.2, "M21") + 0.5; LET = s
shot("lobby", s, s + 2.8, None, photoins=True)
shot("lobby", s + 2.8, t, None, keyins=True)
s = t; t = say(t, "M22") + 0.3; fx(s - 0.2, "servo", 0.6)
shot("lobby", s, t, CU("safeeh", SAF_K, 1.4), CU("safeeh", SAF_K, 1.65), low=True)
PUZ = t; s = t; t = say(t + 0.1, "M23") + 0.4; PUZ_END = t
shot("lobby", s, s + 3.4, CU("tota", LK["tota"], 1.5), CU("tota", LK["tota"], 1.62))
shot("lobby", s + 3.4, t, None, radioins=True)
s = t; t = say(t, "M24") + 0.4; CTA = (s, t)
shot("lobby", s, s + 1.5, CU("nana", NANA_K, 1.6), CU("nana", NANA_K, 1.7))
shot("phone", s + 1.5, t + 0.4, None); TAP = s + 1.5 + 1.6; fx(TAP, "switch", 0.9); t += 0.4
# ===== 4. CLIFF: the Pasha on the phone + the loader =====
cut(t, 0.3); s = t; t = say(t + 0.4, "M25") + 0.3; PCALL = s
shot("street", s, s + 3.2, (PAS_C[0], 600, 1.5), (PAS_C[0], 620, 1.7), low=True)
shot("street", s + 3.2, t, CU("pasha", PAS_C, 1.4), CU("pasha", PAS_C, 1.8))
LOAD = (t, t + 3.2); fx(t + 0.2, "car", 1.0); fx(t + 0.3, "clang", 0.4)
shot("street", t, LOAD[1], (1500, 600, 1.4), (1700, 610, 2.2), ease="crash"); t = LOAD[1]
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
for a_, b_, r_, g_ in ((FIN[0], FIN[1], 6, 0.35), (SWIN[0], SWIN[1], 7, 0.3), (PWALK[0], PWALK[1], 5, 0.35), (RUN[0], RUN[1], 13, 0.5),
                       (GRAB[0], GRAB[1], 9, 0.35)):
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

def ltr(img, x, y, s, size, fill, stroke=(10, 10, 10), sw=3):
    ImageDraw.Draw(img).text((x, y), s, font=ImageFont.truetype(FONT, size), fill=fill, anchor="mm", direction="ltr", stroke_width=sw, stroke_fill=stroke)


SRC = {"car": loc("car", "day"), "carin": loc("car", "night"), "living": ImageEnhance.Brightness(loc("living", "day")).enhance(1.35),
       "street": loc("street", "night"), "lobby": ImageEnhance.Brightness(loc("lobby", "night")).enhance(1.45)}
def bg_frame(set_, cam, sh, tt): return bg_crop(SRC[set_], cam)

def kid(who, set_, tt):
    a = A_(who, (0, 0, 1), look=1)
    off = {"tota": 0.0, "shatta": 0.35, "zalata": 0.7}[who]
    if set_ == "living":
        a["x"], a["y"], a["s"] = LV[who]; a["expr"] = "sad" if who != "zalata" else "flat"
        if who == "zalata": a["held"] = "nbpen"; a["arms"] = "hold"
        if tt >= KNOCK: a["expr"] = "shock" if who != "zalata" else "flat"
        if tt >= FIN[1]: a["expr"] = "neutral" if who != "zalata" else "flat"
        if tt >= T("M10") + 2: a["expr"] = "happy" if who != "zalata" else "smug"
        if tt >= T("M14"): a["expr"] = "happy"
        return a
    if set_ == "street":
        if tt < LIVE or tt >= PCALL: return None
        if who != "shatta":   # the others peek from the building door
            a.update(x=SDOOR[0] - 70 - 90 * off, y=SDOOR[1], s=SDOOR[2], look=1, expr="scared" if who != "zalata" else "flat")
            if tt >= GRAB[1]: a["expr"] = "happy"
            return a
        a.update(x=SDOOR[0], y=SDOOR[1] + 10, s=SDOOR[2], look=1, expr="scared", lean=0.4)
        if tt >= GRAB[0]:
            u = kk(tt, GRAB[0], GRAB[1])
            if u < 0.45: walk_to(a, (SDOOR[0], SDOOR[1] + 10, SDOOR[2]), CARDOOR, (GRAB[0], GRAB[0] + 1.4), tt, 9)
            elif u < 0.6: a.update(x=CARDOOR[0], y=CARDOOR[1], s=CARDOOR[2], arms="hold", held="box", expr="happy")
            else:
                walk_to(a, CARDOOR, (430, 850, 1.4), (GRAB[0] + 1.9, GRAB[1]), tt, 11); a.update(held="box", arms="hold", expr="happy", look=-1)
        if tt >= GRAB[1]: a.update(x=430, y=850, s=1.4, held="box", arms="hold", expr="happy", look=-1, lean=0)
        return a
    if set_ == "lobby":
        a["x"], a["y"], a["s"] = LK[who]; a["look"] = 1 if who == "tota" else -1
        a["expr"] = "happy"
        if who == "shatta" and tt < OPEN[0] + 1.3: a["held"] = "box"; a["arms"] = "hold"
        if tt >= T("M19"): a["expr"] = "shock" if who != "zalata" else "flat"
        if tt >= LET: a["expr"] = "neutral" if who != "zalata" else "flat"
        if tt >= T("M22"): a["look"] = 1; a["expr"] = "shock" if who == "shatta" else a["expr"]
        if tt >= PUZ: a["expr"] = "smug" if who == "tota" else "neutral"
        return a
    return None

def actors(set_, tt, sh):
    A = []
    if any(sh.get(k) for k in ("tileins", "planins", "liveins", "boxins", "photoins", "keyins", "radioins")): return A
    if set_ == "car":
        p = A_("pasha", CAR_P, look=-1, expr="smug", arms="hold", held="box")
        if tt < 1.2: p["look"] = 0
        a = A_("abdo", CAR_A, look=1, expr="happy", arms="down")
        A += [a, p]
    if set_ == "carin":
        a = A_("abdo", CAR_P, look=-1, expr="neutral", arms="hold", held="box")
        if tt >= SPKON: a["look"] = 0; a["expr"] = "shock"
        if tt >= T("M16") + 1.0: a["expr"] = "scared"; a["arms"] = "up"; a["held"] = None
        if tt >= T("M17") + 0.4: return A
        A.append(a)
    if set_ == "living":
        n = A_("nana", NANA_L, look=1, expr="sad", held="slipper", arms="hold")
        if tt >= KNOCK: n["expr"] = "angry"
        if tt >= T("M10"): n["expr"] = "flat"
        if tt >= T("M14"): n["expr"] = "happy"
        A.append(n)
        if tt >= FIN[0]:
            f = A_("fahmy", FAH_L, look=-1, expr="happy", arms="down")
            walk_to(f, (2100, 1000, 1.95), FAH_L, FIN, tt, 6)
            if tt >= T("M08"): f["expr"] = "sad"
            if tt >= T("M10"): f["expr"] = "smug"
            A.append(f)
            b = A_("bondo2", BON_L, look=-1, expr="flat", arms="down")
            walk_to(b, (2250, 1000, 1.85), BON_L, (FIN[0] + 0.8, FIN[1] + 0.6), tt, 5)
            A.append(b)
        if tt >= SWIN[0]:
            sw = A_("sawsan", SAW_L, look=1, expr="happy", held="phone", arms="hold")
            walk_to(sw, (-200, 1000, 1.9), SAW_L, SWIN, tt, 7); A.append(sw)
        sf = SF(SAF_L, eye="green", eye_on=1.0, sad=False, antenna=True, look=1)
        if T("M13") <= tt < T("M14") + 1.2: sf["look"] = 1
        A.append(sf)
    if set_ == "street":
        if tt < PCALL:
            if tt >= LIVE:
                sw = A_("sawsan", SAW_S, look=1, expr="happy", held="phone", arms="hold"); A.append(sw)
                p = A_("pasha", PAS_S0, look=-1, expr="smug", arms="down")
                walk_to(p, PAS_S0, PAS_S, PWALK, tt, 5)
                if tt >= PWALK[1]: p["arms"] = "hold"
                A.append(p)
            if RUN[0] <= tt < RUN[1]:
                ab = A_("abdo", (1320, 810, 1.3), look=1, expr="scared", arms="up")
                walk_to(ab, (1320, 810, 1.3), (2000, 840, 1.42), RUN, tt, 14); A.append(ab)
        else:
            p = A_("pasha", PAS_C, look=1, expr="angry", arms="talk", held="phone")
            A.append(p)
    if set_ == "lobby":
        A.append(SF(SAF_K, eye="green", eye_on=1.0, sad=False, antenna=True, look=-1))
        A.append(A_("nana", NANA_K, look=1, expr="sad", held="slipper", arms="hold"))
        if tt >= T("M24"): A[-1]["expr"] = "angry"; A[-1]["arms"] = "up"
    for who in KIDS:
        a = kid(who, set_, tt)
        if a: A.append(a)
    return A

def light_map(set_, sh, tt, cam, lights):
    x0, y0, z = cam; W3 = lambda px, py: ((px - x0) * z, (py - y0) * z)
    if set_ == "carin":
        m = np.full((LH, LW, 3), 0.75, np.float32) * COOL
        if tt >= SPKON:
            X, Y = W3(*SPK); m += (0.7 + 0.3 * math.sin(tt * 12)) * glow(X, Y, 160 * z)[..., None] * np.array([1.4, 0.2, 0.15], np.float32)
    elif set_ == "lobby":
        m = np.full((LH, LW, 3), 0.7, np.float32) * COOL
        X, Y = W3(775, 60); m += 0.6 * glow(X, Y, 400 * z)[..., None] * WARM
    elif set_ == "street":
        if tt < LOAD[0]: return None
        m = np.full((LH, LW, 3), 0.9, np.float32)
        u = kk(tt, LOAD[0], LOAD[1])
        for dx in (-40, 40):
            X, Y = W3(1760 + dx * (0.6 + u), 690 - 10 * u); m += 2.0 * u * glow(X, Y, (60 + 160 * u) * z)[..., None] * np.array([1.2, 1.15, 0.9], np.float32)
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
    if set_ == "carin":   # the little speaker under the seat
        X, Y = W2(*SPK)
        d.rounded_rectangle([X - 30 * S, Y - 22 * S, X + 30 * S, Y + 22 * S], int(6 * S), fill=(30, 30, 34, 255), outline=(10, 10, 10, 255), width=lw(3))
        for i in range(3): d.ellipse([X - 18 * S + i * 13 * S, Y - 5 * S, X - 10 * S + i * 13 * S, Y + 3 * S], fill=(60, 60, 66, 255))
        if tt >= SPKON and int(tt * 6) % 2: d.ellipse([X + 18 * S, Y - 18 * S, X + 26 * S, Y - 10 * S], fill=(255, 40, 30, 255))
    if set_ == "street" and tt >= LOAD[0]:   # the loader at the end of the street
        u = ease(kk(tt, LOAD[0], LOAD[1])); X, Y = W2(1760, 700); s_ = (0.5 + 0.5 * u) * S
        d.rectangle([X - 90 * s_, Y - 110 * s_, X + 90 * s_, Y], fill=(150, 120, 20, 255))
        d.rectangle([X - 60 * s_, Y - 170 * s_, X + 40 * s_, Y - 110 * s_], fill=(120, 95, 15, 255))
        d.polygon([(X - 150 * s_, Y - 20 * s_), (X - 90 * s_, Y - 60 * s_), (X - 90 * s_, Y), (X - 160 * s_, Y + 10 * s_)], fill=(90, 90, 95, 255))
        for wx in (-55, 55): d.ellipse([X + (wx - 32) * s_, Y - 30 * s_, X + (wx + 32) * s_, Y + 34 * s_], fill=(15, 15, 15, 255))
        gl = Image.new("RGBA", img.size, (0, 0, 0, 0)); gd = ImageDraw.Draw(gl)
        for hx in (-60, 60): gd.ellipse([X + (hx - 26) * s_, Y - 80 * s_, X + (hx + 26) * s_, Y - 40 * s_], fill=(255, 250, 210, 255))
        gd.polygon([(X - 90 * s_, Y - 60 * s_), (X + 90 * s_, Y - 60 * s_), (X + 400 * s_, Y + 260 * s_), (X - 500 * s_, Y + 260 * s_)], fill=(255, 245, 200, 60))
        if int(tt * 4) % 2: gd.ellipse([X - 16 * s_, Y - 200 * s_, X + 16 * s_, Y - 170 * s_], fill=(255, 150, 20, 255))   # beacon
        gl = gl.filter(ImageFilter.GaussianBlur(int(6 * S))); img.paste(gl, (0, 0), gl)

# ---------- inserts ----------
def ins_bg(col=(30, 24, 18)):
    fr = Image.new("RGB", (W, H), col); return fr, ImageDraw.Draw(fr, "RGBA")
def tile_card(tt, sh):
    fr, d = ins_bg((40, 32, 24)); cx, cy, R = W / 2, H / 2 - 20, 260
    gl = Image.new("RGBA", fr.size, (0, 0, 0, 0)); gd = ImageDraw.Draw(gl); gd.ellipse([cx - 500, cy - 400, cx + 500, cy + 400], fill=(255, 240, 190, 110))
    fr.paste(gl.filter(ImageFilter.GaussianBlur(60)), (0, 0), gl.filter(ImageFilter.GaussianBlur(60)))
    d.rectangle([cx - R, cy - R, cx + R, cy + R], fill=(206, 190, 160, 255), outline=(70, 55, 40, 255), width=10)
    d.ellipse([cx - 160, cy - 160, cx + 160, cy + 160], fill=(60, 70, 110, 255)); d.ellipse([cx - 90, cy - 185, cx + 200, cy + 120], fill=(206, 190, 160, 255))
    text(fr, cx, cy + R + 70, "بلاطة الهلال ✓", 70, (200, 255, 200), (10, 40, 10), 5)
    return fr
def plan_card(tt, sh):
    """the plan, drawn on a sheet of paper: 4 roles appear one by one"""
    fr, d = ins_bg((60, 44, 30)); u = kk(tt, sh["start"], sh["end"])
    d.rectangle([180, 90, W - 180, H - 160], fill=(240, 232, 210, 255), outline=(120, 100, 70, 255), width=8)
    text(fr, W / 2, 170, "الخطة", 80, (150, 30, 30), (240, 232, 210), 1)
    items = [("1", "سوسن: لايف", 1420, 420), ("2", "الباشا ينزل", 1420, 640), ("3", "سماعة + صفيح", 700, 420), ("4", "شطة: الصندوق", 700, 640)]
    for i, (n, lab, x, y) in enumerate(items):
        if u > i * 0.2:
            d.ellipse([x + 170, y - 45, x + 260, y + 45], outline=(150, 30, 30, 255), width=6)
            ltr(fr, x + 215, y, n, 56, (150, 30, 30), (240, 232, 210), 1)
            text(fr, x - 140, y, lab, 60, (40, 30, 20), (240, 232, 210), 1)
    if u > 0.85: d.line([(980, 420), (980, 700)], fill=(150, 30, 30, 255), width=6)
    return fr
def live_card(tt, sh):
    """Sawsan's phone: live UI on the Pasha"""
    fr = ImageEnhance.Brightness(bg_crop(SRC["street"], (600, 200, 1.5), True).resize((W, H))).enhance(0.9)
    d = ImageDraw.Draw(fr, "RGBA")
    d.rounded_rectangle([40, 40, 300, 120], 20, fill=(220, 30, 40, 255)); ltr(fr, 170, 80, "LIVE", 52, (255, 255, 255), (120, 0, 0), 2)
    d.rounded_rectangle([330, 40, 640, 120], 20, fill=(0, 0, 0, 150)); ltr(fr, 485, 80, f"{1200 + int((tt - sh['start']) * 900)}", 46, (255, 255, 255), (0, 0, 0), 2)
    for i in range(6):   # hearts floating
        v = ((tt - sh["start"]) * 0.8 + i / 6) % 1; x, y = W - 160 + math.sin(i * 2 + tt * 3) * 40, H - 120 - v * 600
        d.ellipse([x - 22, y - 22, x + 22, y + 22], fill=(255, 60, 90, int(255 * (1 - v))))
    d.rectangle([0, 0, W, H], outline=(255, 255, 255, 120), width=6)
    return fr
def box_card(tt, sh):
    fr, d = ins_bg((24, 20, 16)); cx, cy = W / 2, H / 2 + 60
    u = ease(kk(tt, sh["start"], sh["start"] + 0.8)) if sh.get("empty") else 1.0
    d.rounded_rectangle([cx - 420, cy - 200, cx + 420, cy + 240], 20, fill=(120, 126, 134, 255), outline=(40, 40, 44, 255), width=10)
    d.rectangle([cx - 390, cy - 170, cx + 390, cy + 210], fill=(40, 38, 36, 255))
    d.polygon([(cx - 430, cy - 200), (cx + 430, cy - 200), (cx + 430, cy - 200 - 360 * u), (cx - 430, cy - 200 - 360 * u)], fill=(140, 146, 154, 255), outline=(40, 40, 44, 255))
    if not sh.get("empty") or tt > sh["start"] + 1.2:
        k = 1.0 if not sh.get("empty") else 0.0
        if k:   # photo + key inside
            d.rectangle([cx - 330, cy - 130, cx - 30, cy + 150], fill=(225, 210, 175, 255), outline=(90, 70, 40, 255), width=6)
            d.rectangle([cx - 305, cy - 105, cx - 55, cy + 100], fill=(150, 120, 80, 255))
            keyart(d, fr, cx + 60, cy + 20, 1.0)
    return fr
def keyart(d, fr, x, y, s):
    d.ellipse([x - 50 * s, y - 50 * s, x + 50 * s, y + 50 * s], outline=(200, 160, 60, 255), width=int(14 * s))
    d.rectangle([x + 45 * s, y - 9 * s, x + 280 * s, y + 9 * s], fill=(200, 160, 60, 255))
    for bx in (220, 255): d.rectangle([x + bx * s, y + 9 * s, x + (bx + 20) * s, y + 44 * s], fill=(200, 160, 60, 255))
    d.rounded_rectangle([x - 20 * s, y + 80 * s, x + 230 * s, y + 160 * s], int(10 * s), fill=(176, 170, 160, 255), outline=(90, 80, 70, 255), width=4)
    d.line([(x, y + 45 * s), (x + 30 * s, y + 80 * s)], fill=(80, 70, 60, 255), width=4)
    text(fr, x + 105 * s, y + 120 * s, "الدور الأخير", int(40 * s), (60, 40, 20), (176, 170, 160), 1)
def photo_card(tt, sh):
    """old sepia photo: young Roshdy in a hidden workshop, a sheet-covered figure with a pharaoh crown peeking out"""
    fr, d = ins_bg((30, 24, 18)); k = ease(kk(tt, sh["start"], sh["start"] + 0.5)); cx, cy = W / 2, H / 2 + (1 - k) * 200
    d.rectangle([cx - 520, cy - 380, cx + 520, cy + 380], fill=(230, 215, 180, 255))
    ph = Image.new("RGB", (960, 680), (170, 140, 100)); pd = ImageDraw.Draw(ph, "RGBA")
    pd.rectangle([0, 520, 960, 680], fill=(120, 95, 65))
    for i in range(6): pd.rectangle([60 + i * 150, 120, 120 + i * 150, 520], fill=(140, 112, 80))   # shelves/pillars
    pd.polygon([(600, 520), (640, 240), (780, 240), (820, 520)], fill=(225, 215, 195))   # sheet-covered figure
    pd.polygon([(650, 250), (710, 120), (770, 250)], fill=(60, 60, 110)); pd.rectangle([680, 200, 740, 250], fill=(200, 160, 60))   # crown peeks out
    tmp = Image.new("RGBA", (960, 680), (0, 0, 0, 0)); draw_char(P(tmp), "roshdy", 330 / SS, 640 / SS, 1.5 / SS * 1.55, "happy", 0, 1, False, "hold", tt, "key")
    ph.paste(tmp, (0, 0), tmp)
    g = np.asarray(ph.convert("L"), np.float32) / 255; ph = Image.fromarray(np.clip(np.stack([g * 255, g * 220, g * 170], -1), 0, 255).astype(np.uint8))
    fr.paste(ph, (int(cx - 480), int(cy - 340)))
    text(fr, cx, cy + 420, "عم رشدي... وتمثال متغطي؟!", 52, (255, 214, 90), (30, 10, 5), 4)
    return fr
def key_card(tt, sh):
    fr, d = ins_bg((26, 22, 18)); u = kk(tt, sh["start"], sh["end"])
    keyart(d, fr, W / 2 - 300 + u * 40, H / 2 - 80, 2.0)
    if int(tt * 5) % 2: d.polygon([(W / 2 + 200, H / 2 - 160), (W / 2 + 212, H / 2 - 128), (W / 2 + 244, H / 2 - 116), (W / 2 + 212, H / 2 - 104), (W / 2 + 200, H / 2 - 72), (W / 2 + 188, H / 2 - 104), (W / 2 + 156, H / 2 - 116), (W / 2 + 188, H / 2 - 128)], fill=(255, 250, 200, 255))
    return fr
def radio_card(tt, sh):
    """hint: a silhouette of an old radio with music notes — blurred, «?»"""
    fr, d = ins_bg((20, 18, 26)); cx, cy = W / 2, H / 2 - 40
    d.rounded_rectangle([cx - 300, cy - 180, cx + 300, cy + 180], 40, fill=(70, 50, 35, 255))
    d.ellipse([cx - 250, cy - 130, cx - 10, cy + 110], fill=(40, 30, 22, 255))
    for i in range(5): d.line([(cx + 40, cy - 100 + i * 45), (cx + 250, cy - 100 + i * 45)], fill=(40, 30, 22, 255), width=10)
    fr = fr.filter(ImageFilter.GaussianBlur(14)); d = ImageDraw.Draw(fr, "RGBA")
    for i in range(4):
        v = ((tt - sh["start"]) * 0.6 + i / 4) % 1; x = cx + 260 + math.sin(i * 2 + tt * 2) * 60; y = cy - 120 - v * 300
        text(fr, x, y, "♪", 90, (255, 214, 90, int(255 * (1 - v))), (30, 10, 5), 2)
    text(fr, cx, cy + 300, "؟", 160, (255, 214, 90), (30, 10, 5), 6)
    return fr

def hud(fr, tt, v=False):
    sc = 0.85 if v else 1.0; cx = 540 if v else W / 2; y = 1700 if v else 120
    d = ImageDraw.Draw(fr, "RGBA")
    if P5 + DUR["M06"] * 0.5 <= tt < P5 + DUR["M06"] + 0.3:
        d.rounded_rectangle([cx - 150 * sc, y - 50 * sc, cx + 150 * sc, y + 50 * sc], int(22 * sc), fill=(60, 20, 20, 220), outline=(255, 120, 90, 255), width=4)
        ltr(fr, cx, y, "5%", int(56 * sc), (255, 160, 120))

PUZ_TXT = "إيه اللي بيغني لوحده في العمارة؟"
def puzzle_box(fr, tt, cx, y, sc=1.0):
    d = ImageDraw.Draw(fr, "RGBA"); k = ease(kk(tt, PUZ + 0.2, PUZ + 0.7))
    d.rounded_rectangle([cx - 600 * sc, y - 70 * sc, cx + 600 * sc, y + 90 * sc], int(26 * sc), fill=(20, 20, 30, int(225 * k)), outline=(255, 214, 90, int(255 * k)), width=5)
    text(fr, cx, y - 15 * sc, "لغز النهارده: " + PUZ_TXT, int(42 * sc), (255, 214, 90))
    text(fr, cx, y + 45 * sc, "افتكروا الموسم الأول... اكتبوا في الكومنتات", int(34 * sc), (235, 235, 235))

TINT = {"car": (255, 240, 220), "carin": (150, 160, 200), "living": (255, 228, 190), "street": (150, 160, 210), "lobby": (150, 165, 225)}
INS = (("tileins", tile_card), ("planins", plan_card), ("liveins", live_card), ("boxins", box_card), ("photoins", photo_card),
       ("keyins", key_card), ("radioins", radio_card))
def frame(tt, plat="yt"):
    sh = shot_at(tt); set_ = sh["set"]
    if set_ in ("title", "endcard"): return finish(card(set_, tt, sh), tt)
    if set_ == "black": return Image.new("RGB", (W, H), (0, 0, 0))
    if set_ == "phone": return finish(phone_card(tt, sh, plat), tt)
    for k_, fn in INS:
        if sh.get(k_):
            out = fn(tt, sh)
            if k_ == "photoins": out = ImageChops.multiply(out, VIG_DARK)
            return finish(out, tt, True)
    cam = cam_at(sh, tt)
    img = bg_frame(set_, cam, sh, tt)
    layer, lights = draw_scene_chars(set_, tt, cam, sh)
    layer = tint_layer(layer, TINT.get(set_, (255, 244, 225)), 0.97)
    img.paste(layer, (0, 0), layer)
    props(img, set_, tt, cam, sh)
    if set_ in ("car", "carin"):   # seat cushion in front of the sitters
        x0, y0, z = cam; ys = int((870 - y0) * z * SS)
        if ys < SSH: bgc = bg_crop(SRC[set_], cam, True); img.paste(bgc.crop((0, ys, SSW, SSH)), (0, ys))
        if set_ == "carin": props(img, set_, tt, cam, sh)
    fr = img.resize((W, H), Image.LANCZOS)
    lm = light_map(set_, sh, tt, cam, lights)
    if lm is not None:
        fr = ImageChops.multiply(fr, lm); fr = ImageEnhance.Brightness(fr).enhance({"carin": 1.4, "lobby": 1.5, "street": 1.15}.get(set_, 1.0))
    return finish(fr, tt, set_ in ("carin", "street", "lobby"))

def lowpass(x, fc):
    from numpy.fft import rfft, irfft
    X = rfft(x); fq = np.fft.rfftfreq(len(x), 1 / SR); X[fq > fc] *= 0.08; return irfft(X, len(x)).astype(np.float32)

def build_audio(path="mix.wav"):
    buf = np.zeros(int(TOTAL * SR) + SR * 3, dtype=np.float32)
    dr = drone(TOTAL + 1); env = np.zeros(len(dr), np.float32)
    for a_, b_ in ((0, TITLE), (NIGHT[0], OPEN[1]), (PCALL, TOTAL - 4.9)):
        env[int(a_ * SR):int(b_ * SR)] = 1.0
    env = np.convolve(env, np.ones(4410) / 4410, mode="same")
    mix_into(buf, dr * env, 0, 1.2)
    r = np.random.default_rng(9)
    S = {"boom": sfx_boom(), **SFXF}
    for t0, nme, g in sfx:
        if nme in S and g > 0: mix_into(buf, S[nme], t0, g)
    # heist music: sneaky pizzicato from the plan to the grab
    for i in range(int((GRAB[1] - PLAN[0]) / 0.35)):
        f = [196, 0, 233, 0, 262, 0, 233, 196][i % 8]; tp = np.arange(int(SR * 0.2)) / SR
        if f: mix_into(buf, np.sin(2 * np.pi * f * tp) * np.exp(-tp * 25) * (0.06 if PLAN[0] + i * 0.35 < NIGHT[0] else 0.1), PLAN[0] + i * 0.35, 1.0)
    # comic stings: 5%, «رشدي مين؟!», Abdo flees, the slipper
    for t_, notes in ((P5 + DUR["M06"] * 0.5, [523, 494, 440, 392]), (T("M14") + 0.6, [392, 370, 349, 330]), (RUN[0] + 0.3, [660, 440, 330]),
                      (T("M24") + DUR["M24"] - 0.3, [784, 659, 523])):
        for i, f in enumerate(notes):
            tt_ = np.arange(int(SR * 0.4)) / SR
            mix_into(buf, np.sin(2 * np.pi * f * tt_) * np.exp(-tt_ * 12) * 0.09, t_ + i * 0.18, 1.0)
    # Roshdy's letter: a soft music box under it
    for i in range(int(DUR["M21"] / 0.5) + 2):
        f = [523, 659, 784, 659][i % 4]; tb = np.arange(int(SR * 0.45)) / SR
        mix_into(buf, np.sin(2 * np.pi * f * tb) * np.exp(-tb * 6) * 0.03, LET + i * 0.5, 1.0)
    # crowd hum on the live
    n = int(2.5 * SR); mix_into(buf, (np.convolve(r.normal(0, 1, n), np.ones(60) / 60, mode="same") * 0.04).astype(np.float32), LIVE, 1.0)
    # loader: low diesel rumble + beeps
    tp = np.arange(int(SR * 4.0)) / SR
    mix_into(buf, ((np.sign(np.sin(2 * np.pi * 38 * tp)) * 0.05 + np.sin(2 * np.pi * 76 * tp) * 0.05) * np.minimum(1, tp)).astype(np.float32), LOAD[0], 1.0)
    for i in range(5):
        tb = np.arange(int(SR * 0.25)) / SR; mix_into(buf, np.sin(2 * np.pi * 1000 * tb) * 0.05, LOAD[0] + 0.5 + i * 0.5, 1.0)
    tsx = np.arange(int(SR * 0.25)) / SR
    for st, g in STEPS:
        nz = np.convolve(r.normal(0, 1, len(tsx)), np.ones(12) / 12, mode="same")
        mix_into(buf, (np.sin(2 * np.pi * 80 * tsx) * np.exp(-tsx * 30) * 0.9 + nz * np.exp(-tsx * 25) * 0.9) * 0.6, st, g)
    for st, k in lines:
        a = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8
        if k == "M07": a = lowpass(a, 2500) * 0.9                 # behind the door
        if k == "M16": a = lowpass(a, 3000) * 0.9                 # through the small speaker
        if k == "M25": a = lowpass(a, 3500)
        mix_into(buf, a, st, 1.0)
    buf = buf[:int(TOTAL * SR)]
    buf = np.clip(buf / max(1e-6, np.abs(buf).max()) * 0.95, -1, 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((buf * 32767).astype(np.int16).tobytes())
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
        text(fr, W / 2, H / 2 - 230, "الحلقة 10 والأخيرة بكرة: أغنية العمارة", 96, g((255, 214, 90)), (40, 10, 10), 6)
        text(fr, W / 2, H / 2 - 100, "إيه اللي بيغني لوحده في العمارة؟ اكتبوها في الكومنتات", 52, g((235, 235, 235)))
        xs = [W / 2 - 660, W / 2 - 220, W / 2 + 220, W / 2 + 660]
        for x_, kk_ in zip(xs, ("yt", "fb", "ig", "tt")):
            im = FOLLOW[kk_]; sc = 380 / im.size[0]; th = im.resize((380, int(im.size[1] * sc)), Image.LANCZOS)
            th = th.crop((0, 0, 380, min(th.size[1], 300)))
            if k > 0.15: fr.paste(th, (int(x_ - 190), int(H / 2 + 20)))
        text(fr, W / 2 + 230, H - 70, "تابعونا:", 50, g((255, 214, 90)), (40, 10, 10), 4)
        ltr(fr, W / 2 - 110, H - 70, "@shattawzalata", 50, g((255, 214, 90)), (40, 10, 10), 4)
    return fr


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
