import sys, os, math, subprocess, wave
sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter, ImageFont
from engine import *
from locations import loc

# م2 ح10 «أغنية العمارة» — SEASON FINALE. Built from s2e9/ep9.py, Episode checklist + fixed locations.
# New vs Ep9: dawn street with the loader (machine vs robot), the 7-floor stairs race with floor badges, the S1E8 radio in
# apt 7 (back opens → the record), the record-spin insert, the ORIGINAL SONG out loud over the whole street with neighbours
# lighting up their windows, the Pasha's catchphrase turned on him + exit with his back to camera, the key plant for S3,
# and the night cliff: Safeeh's chest screen «أنا راجع» + the pharaoh's shadow in the top-floor window.
os.chdir(ROOT + "/s2e10")
SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(1010)
SEASON = "سر البدروم"
EPT = "الحلقة 10: أغنية العمارة"
SONG = ROOT + "/s2/music/أغنية العمارة - نسخة 2أ.mp3"

SUB = {
 "N01": "الساعة سبعة... العمارة دي هتتهد.", "N02": "أنا صاحي أهو!... مين عايز يوقّع العمارة؟!",
 "N03": "إجابة لغز امبارح: الراديو اللي في الدور السابع!... اشتغل لوحده في الموسم الأول!",
 "N04": "يبقى الأسطوانة جوه الراديو!... اطلعوا بسرعة!", "N05": "سبع أدوار تاني؟!... احتمال أوصل: تلاتين في المية.",
 "N06": "لقيتها!... الأسطوانة!", "N07": "ابدأ يا عبده!", "N08": "يا باشا... فيه عيال جوه.", "N09": "اسمع الكلام وابدأ!",
 "N10": "وضع الحراسة!... محدش هيلمس العمارة!", "N11": "اللايف شغال!... كل الناس بتتفرج!",
 "N12": "شغّلوا الأسطوانة!... خلي الشارع كله يسمع!", "N13": "دي... الست بهية.", "N14": "الأغاني دي اتغنت هنا... العمارة دي تراث!",
 "N15": "والباشا... ممسوك ومعاه العدة!", "N16": "كل حاجة ليها تمن... وأنا دفعته.", "N17": "أنا آسف يا ست نعناعة...",
 "N18": "الشبشب... هيستناك المرة الجاية.", "N19": "لغز آخر الموسم: المفتاح ده بيفتح إيه؟... اكتبوا توقعاتكم!",
 "N20": "اعملوا فولو... أنا صاحي أهو!", "N21": "وحشتوني يا ولاد... أنا راجع.",
}
WHO = {"N01": "pasha", "N02": "bondo2", "N03": "tota", "N04": "shatta", "N05": "zalata", "N06": "tota", "N07": "pasha", "N08": "abdo",
       "N09": "pasha", "N10": "safeeh", "N11": "sawsan", "N12": "shatta", "N13": "nana", "N14": "nana", "N15": "zalata", "N16": "pasha",
       "N17": "abdo", "N18": "nana", "N19": "tota", "N20": "bondo2", "N21": "roshdy"}
EXPR = {"N01": "smug", "N02": "angry", "N03": [(0, "neutral"), (0.6, "smug")], "N04": "happy", "N05": "sad", "N06": "happy", "N07": "smug",
        "N08": "sad", "N09": "angry", "N11": "happy", "N12": "happy", "N13": "sad", "N14": "happy", "N15": "smug", "N16": "sad", "N17": "sad",
        "N18": "angry", "N19": [(0, "neutral"), (0.6, "smug")], "N20": "happy"}
ARMS = {"N02": "point", "N03": "point", "N04": "point", "N05": "hold", "N07": "point", "N08": "talk", "N09": "point", "N11": "up",
        "N12": "up", "N14": "talk", "N15": "point", "N16": "down", "N17": "hold", "N18": "up", "N19": "hold", "N20": "up"}

def _aud(k): return load_audio(f"audio/{k}.mp3")
AUD = {k: _aud(k) for k in SUB}
ENV = {k: envelope(v) for k, v in AUD.items()}
DUR = {k: len(v) / SR for k, v in AUD.items()}
SFXF = {n: load_audio(ROOT + f"/s2e4/sfx/{n}.mp3") for n in ("whoosh", "creak", "slam", "switch", "clang", "stinger", "servo",
                                                             "steps_metal", "unlock", "car", "tape")}
SONGA = load_audio(SONG)

lines, sfx, shots, jumps, shakes = [], [], [], {}, []
def say(t, k): lines.append((t, k)); return t + DUR[k]
def fx(t, n, g=1.0): sfx.append((t, n, g))
def jump(w, t): jumps.setdefault(w, []).append(t)
def shot(set_, s, e, c0, c1=None, **kw): shots.append(dict(set=set_, start=s, end=e, c0=c0, c1=c1 or c0, **kw))
def cut(t, g=0.4): fx(t - 0.12, "whoosh", g)
def T(k): return [st for st, kk_ in lines if kk_ == k][0]
KIDS = ("shatta", "zalata", "tota")
CHASE = (-9, -8); SNAP = -1

# ---------------- world ----------------
PAS = (1180, 905, 1.55); BON0 = (120, 960, 1.85); BON = (420, 975, 1.85); ABD = (1480, 880, 1.45); LOADER = (1640, 610)
SAF0 = (-150, 960, 1.5); SAF = (1330, 950, 1.5); SAW = (150, 995, 1.85); NANA_S = (330, 1000, 1.9)
KS = {"tota": (560, 1010, 1.9), "shatta": (760, 1015, 1.9), "zalata": (950, 1010, 1.9)}
PEEK = {"tota": (1290, 905, 1.5), "shatta": (1380, 900, 1.5), "zalata": (1470, 905, 1.5)}
A7 = {"tota": (760, 1000, 1.9), "shatta": (980, 1010, 1.9), "zalata": (1200, 1000, 1.9)}; RADIO = (590, 500)
WINS = [(480, 150), (770, 80), (1110, 175), (1330, 235), (1520, 120), (1720, 180)]; TOPWIN = (770, 80)
SAF_N = (960, 980, 1.6)

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
# ===== 0. HOOK — dawn, the loader rolls in behind the Pasha's car =====
fx(0.0, "car", 0.9); fx(0.2, "clang", 0.3)
shot("street", 0, 2.0, (1650, 560, 1.6), (1550, 600, 1.4))
s = 2.0; t = say(s, "N01") + 0.1
shot("street", s, t, CU("pasha", PAS, 1.5), CU("pasha", PAS, 1.65), low=True)
BWALK = (t, t + 1.3)
s = t; t = say(t + 0.6, "N02") + 0.2; jump("bondo2", s + 0.6)
shot("street", s, t, (420, 640, 1.3), (440, 660, 1.45))
cut(t, 0.3); TITLE = t; shot("title", t, t + 2.0, None); t += 2.0
# ===== 1. LOBBY (day): the answer → up the stairs =====
s = t; t = say(t + 0.1, "N03") + 0.2; ANS = s
shot("lobby", s, s + 3.0, CU("tota", PEEK["tota"], 1.9, 70), CU("tota", PEEK["tota"], 2.0, 70))
shot("lobby", s + 3.0, t, None, radioins=True, front=True)
s = t; t = say(t, "N04") + 0.1; jump("shatta", s)
shot("lobby", s, t, CU("shatta", PEEK["shatta"], 1.8), CU("shatta", PEEK["shatta"], 2.0))
cut(t, 0.25); MONT = (t, t + 4.8)
for i in range(4): shot("stairs", t + i * 1.2, t + (i + 1) * 1.2, (1150, 560, 1.05 + i * 0.03), (1150, 600, 1.12 + i * 0.03), floor=i)
t = MONT[1]
s = t; t = say(t, "N05") + 0.2
shot("stairs", s, t, CU("zalata", (1150, 1000, 1.9), 1.4), CU("zalata", (1150, 1000, 1.9), 1.55), floor=4, still=True)
# ===== 2. APT 7 — the radio =====
cut(t, 0.3); A7IN = (t, t + 2.4); fx(t + 0.1, "creak", 1.0)
shot("apt7", t, A7IN[1], (1000, 560, 1.05), (900, 580, 1.15)); t = A7IN[1]
OPEN = (t, t + 2.2); fx(t + 0.6, "unlock", 0.8); fx(t + 1.2, "creak", 0.5)
shot("apt7", t, OPEN[1], None, radioins=True, front=False); t = OPEN[1]
s = t; t = say(t, "N06") + 0.2; jump("tota", s)
shot("apt7", s, t, CU("tota", A7["tota"], 1.5), CU("tota", A7["tota"], 1.7), ease="crash")
# ===== 3. STREET — machine vs robot =====
cut(t, 0.3)
s = t; t = say(t + 0.2, "N07") + 0.1
shot("street", s, t, CU("pasha", PAS, 1.5), CU("pasha", PAS, 1.6))
s = t; t = say(t, "N08") + 0.1
shot("street", s, t, CU("abdo", ABD, 1.5, -30), CU("abdo", ABD, 1.6, -30))
s = t; t = say(t, "N09") + 0.1; shakes.append((s + 0.3, 5))
shot("street", s, t, CU("pasha", PAS, 1.7), CU("pasha", PAS, 2.1), ease="crash")
ROLL = (t, t + 2.4); fx(t, "car", 1.0)
for i in range(4): fx(t + 0.5 + i * 0.45, "steps_metal", 0.6)
shot("street", t, ROLL[1], (1300, 600, 1.15), (1350, 620, 1.2)); t = ROLL[1]
s = t; t = say(t, "N10") + 0.2; RED = s; fx(s, "stinger", 1.0); shakes.append((s, 8))
shot("street", s, t, CU("safeeh", SAF, 1.3), CU("safeeh", SAF, 1.6), low=True)
s = t; t = say(t, "N11") + 0.2
shot("street", s, s + 1.4, CU("sawsan", SAW, 1.6, 60), CU("sawsan", SAW, 1.7, 60))
shot("street", s + 1.4, t, None, liveins=True)
KOUT = (t, t + 1.8); fx(t + 0.1, "slam", 0.6)
shot("street", t, KOUT[1], (700, 640, 1.2), (720, 660, 1.25)); t = KOUT[1]
s = t; t = say(t, "N12") + 0.2; jump("shatta", s)
shot("street", s, t, CU("shatta", KS["shatta"], 1.6), CU("shatta", KS["shatta"], 1.8))
# ===== 4. THE SONG =====
SONG_T = (t, None); fx(t, "tape", 0.6)
shot("street", t, t + 2.4, None, recins=True); t += 2.4
shot("facade", t, t + 4.0, (1000, 500, 1.05), (1000, 420, 1.2)); FAC = (t - 4.0 + 4.0, t + 4.0); t += 4.0
shot("street", t, t + 2.6, (900, 600, 1.05), (900, 600, 1.1)); NIN = (t, t + 2.4); t += 2.6
s = t; t = say(t, "N13") + 0.3
shot("street", s, t, CU("nana", NANA_S, 1.6), CU("nana", NANA_S, 1.9))
s = t; t = say(t, "N14") + 0.4
shot("street", s, t, CU("nana", NANA_S, 1.7), CU("nana", NANA_S, 1.85))
SONG_T = (SONG_T[0], t)
s = t; t = say(t, "N15") + 0.2
shot("street", s, t, CU("zalata", KS["zalata"], 1.6), CU("zalata", KS["zalata"], 1.75))
s = t; t = say(t, "N16") + 0.2
shot("street", s, t, CU("pasha", PAS, 1.6), CU("pasha", PAS, 1.75))
PEXIT = (t, t + 2.6)
shot("street", t, PEXIT[1], (1250, 600, 1.15), (1300, 600, 1.2)); t = PEXIT[1]
s = t; t = say(t, "N17") + 0.1
shot("street", s, t, CU("abdo", ABD, 1.5, -30), CU("abdo", ABD, 1.6, -30))
s = t; t = say(t, "N18") + 0.3
shot("street", s, t, CU("nana", NANA_S, 1.6, 40), CU("nana", NANA_S, 1.7, 40))
PUZ = t; s = t; t = say(t + 0.1, "N19") + 0.3; PUZ_END = t
shot("street", s, t, CU("tota", KS["tota"], 1.5), CU("tota", KS["tota"], 1.62))
KEYT = (t, t + 2.4)
shot("street", t, KEYT[1], None, keyins=True); t = KEYT[1]
s = t; t = say(t, "N20") + 0.4; CTA = (s, t)
shot("street", s, s + 1.4, CU("bondo2", BON, 1.6, 30), CU("bondo2", BON, 1.7, 30))
shot("phone", s + 1.4, t + 0.4, None); TAP = s + 1.4 + 1.4; fx(TAP, "switch", 0.9); t += 0.4
# ===== 5. NIGHT CLIFF =====
cut(t, 0.4); NIGHT = (t, t + 2.4); SCREEN = t + 1.2; fx(SCREEN, "servo", 0.6)
shot("lobbyn", t, NIGHT[1], (SAF_N[0], 560, 1.4), CU("safeeh", SAF_N, 1.2)); t = NIGHT[1]
s = t; t = say(t + 0.2, "N21") + 0.4
shot("lobbyn", s, t, CU("safeeh", SAF_N, 1.3), CU("safeeh", SAF_N, 1.7))
TILT = (t, t + 3.6); SHADOW = t + 2.2; fx(SHADOW, "stinger", 1.0)
shot("facaden", t, TILT[1], (1000, 600, 1.05), (TOPWIN[0], TOPWIN[1] + 120, 2.6)); t = TILT[1]
fx(t, "boom", 0.9); shakes.append((t - 0.2, 10))
shot("black", t, t + 0.5, None); t += 0.5
shot("endcard", t, t + 5.0, None); t += 5.0
TOTAL = t

STEPS = []
def contacts(t0, t1, rate, g=0.5):
    n = math.ceil(t0 * rate / math.pi)
    while True:
        tc = n * math.pi / rate
        if tc >= t1: break
        if tc >= t0: STEPS.append((tc, g))
        n += 1
for a_, b_, r_, g_ in ((BWALK[0], BWALK[1], 6, 0.4), (MONT[0], MONT[1], 9, 0.35), (A7IN[0], A7IN[1], 6, 0.3), (KOUT[0], KOUT[1], 10, 0.4),
                       (NIN[0], NIN[1], 6, 0.35), (PEXIT[0], PEXIT[1], 5, 0.35)):
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
        held = a.get("held"); held_e = held if held not in ("box", "radio") else None
        draw_char(p, who, X + shiver * z, Y, s, expr, mouth, look, blink, arms, tt, held_e, a.get("lean", 0), a.get("walk"))
        S = s * CH[who]["scale"]
        if who == "pasha":
            hy = Y - 190 * S + math.sin(tt * 2.2 + X) * 1.6 * S; hx = X + a.get("lean", 0) * 18 * S
            p.rect(hx - 30 * S, hy - 70 * S, hx + 30 * S, hy - 34 * S, (22, 22, 28, 255), INK, 2.5 * S, 14 * S)
            p.rect(hx - 29 * S, hy - 46 * S, hx + 29 * S, hy - 38 * S, (140, 25, 30, 255), None)
            p.ell(hx, hy - 36 * S, 60 * S, 10 * S, (22, 22, 28, 255), INK, 2.5 * S)
        if held == "radio":
            hx_, hy_ = HANDS["hold"]; bx, by = X + hx_ * S - 20 * S, Y - hy_ * S
            p.rect(bx - 44 * S, by - 34 * S, bx + 44 * S, by + 26 * S, (120, 76, 42, 255), INK, 2.5 * S, 8 * S)
            p.ell(bx - 18 * S, by - 4 * S, 16 * S, 16 * S, (60, 40, 25, 255), None)
            for k_ in range(3): p.line([(bx + 8 * S, by - 18 * S + k_ * 12 * S), (bx + 36 * S, by - 18 * S + k_ * 12 * S)], (60, 40, 25, 255), 2.5 * S)
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


_st = loc("stairs", "day")
SRC = {"street": loc("street", "day"), "lobby": loc("lobby", "day"), "stairs": ImageEnhance.Brightness(_st).enhance(1.5),
       "apt7": ImageEnhance.Brightness(loc("apt7", "day")).enhance(1.5),
       "facade": ImageChops.multiply(ImageEnhance.Brightness(loc("street", "night")).enhance(1.9), Image.new("RGB", (W, H), (255, 225, 190))),
       "facaden": loc("street", "night"), "lobbyn": ImageEnhance.Brightness(loc("lobby", "night")).enhance(0.9)}
def bg_frame(set_, cam, sh, tt): return bg_crop(SRC[set_], cam)

def kid(who, set_, tt):
    a = A_(who, (0, 0, 1), look=1)
    off = {"tota": 0.0, "shatta": 0.35, "zalata": 0.7}[who]
    if set_ == "lobby":
        a["x"], a["y"], a["s"] = PEEK[who]; a["look"] = -1; a["expr"] = "happy" if who != "zalata" else "flat"
        if who == "zalata": a["held"] = "nbpen"; a["arms"] = "hold"
        return a
    if set_ == "stairs":
        sh = shot_at(tt); i = sh.get("floor", 0)
        if sh.get("still"):
            a.update(x=1150 + {"tota": -60, "shatta": 60, "zalata": 0}[who], y=1000 if who == "zalata" else 760, s=1.9 if who == "zalata" else 1.0,
                     back=who != "zalata", expr="sad", lean=0.5 if who == "zalata" else 0, look=1)
            if who != "zalata": a["walk"] = tt * 7
            return a
        u = kk(tt, sh["start"], sh["end"]); xo = {"tota": 0, "shatta": -70, "zalata": 70}[who]
        k0 = max(0, min(1, u * 1.25 - off * 0.25))
        a.update(x=1150 + xo * lerp(1, 0.4, k0), y=lerp(1050, 380, k0), s=lerp(1.9, 0.7, k0), walk=tt * (9 - i), back=True, arms="down")
        return a
    if set_ == "apt7":
        st0 = A7IN[0] + 0.4 + off * 0.5
        if tt < st0: return None
        walk_to(a, (2100, 1010, 1.95), A7[who], (st0, A7IN[1] + 0.3), tt, 7)
        a["look"] = -1; a["expr"] = "shock" if who != "zalata" else "flat"
        if tt >= OPEN[1]: a["expr"] = "happy"
        if who == "tota" and tt >= OPEN[1]: a["held"] = "paper"; a["arms"] = "up"
        return a
    if set_ == "street":
        if tt < KOUT[0] or tt >= NIGHT[0]: return None
        walk_to(a, (100 + 40 * off, 980, 1.8), KS[who], (KOUT[0] + off * 0.4, KOUT[1] + 0.2), tt, 9)
        a["look"] = 1; a["expr"] = "happy"
        if who == "shatta": a["held"] = "radio"; a["arms"] = "hold"
        if who == "zalata": a["held"] = "nbpen"; a["arms"] = "hold"
        if who == "tota" and tt >= PUZ: a["held"] = "key"; a["arms"] = "hold"
        if who == "tota" and tt >= KEYT[1]: a["held"] = None; a["arms"] = "down"
        if tt >= T("N16"): a["look"] = 1
        if PEXIT[0] <= tt < PEXIT[1]: a["expr"] = "smug" if who == "zalata" else "happy"
        return a
    return None

def actors(set_, tt, sh):
    A = []
    if any(sh.get(k) for k in ("radioins", "liveins", "recins", "keyins")): return A
    if set_ == "street":
        if tt < PEXIT[1]:
            p = A_("pasha", PAS, look=-1, expr="smug", arms="down")
            if T("N07") <= tt: p["look"] = 1
            if tt >= RED: p["look"] = 1; p["expr"] = "shock"
            if tt >= SONG_T[0]: p["expr"] = "sad"
            if tt >= PEXIT[0]:
                walk_to(p, PAS, (2150, 880, 1.45), (PEXIT[0] + 0.2, PEXIT[1]), tt, 5); p["back"] = True
            A.append(p)
        ab = A_("abdo", ABD, look=-1, expr="neutral", arms="hold")
        if tt >= RED: ab["expr"] = "scared"; ab["arms"] = "up"
        if tt >= SONG_T[0]: ab["expr"] = "sad"; ab["arms"] = "down"
        if tt >= T("N17"): ab["look"] = -1
        A.append(ab)
        b = A_("bondo2", BON, look=1, expr="angry", arms="hips")
        if tt < BWALK[1]: walk_to(b, BON0, BON, BWALK, tt, 6)
        if tt >= T("N02") + DUR["N02"]: b["expr"] = "flat"
        if tt >= SONG_T[0]: b["expr"] = "happy"
        A.append(b)
        if tt >= ROLL[0]:
            sf = SF(SAF, eye="green", eye_on=1.0, sad=False, antenna=True, look=1, arms="up")
            walk_to(sf, SAF0, SAF, (ROLL[0], ROLL[1] - 0.2), tt, 6)
            if tt >= RED: sf["eye"] = "red"
            if tt >= SONG_T[0]: sf["eye"] = "green"; sf["arms"] = "down"
            A.append(sf)
        if tt >= T("N11") - 0.5:
            A.append(A_("sawsan", SAW, look=1, expr="happy", held="phone", arms="hold"))
        if tt >= NIN[0]:
            n = A_("nana", NANA_S, look=1, expr="sad", held="slipper", arms="hold")
            walk_to(n, (-150, 1000, 1.9), NANA_S, NIN, tt, 6)
            if tt >= T("N14"): n["expr"] = "happy"
            if tt >= T("N18"): n["expr"] = "angry"
            if KEYT[0] <= tt: n["expr"] = "smug"
            A.append(n)
    if set_ == "apt7":
        pass
    if set_ == "lobbyn":
        A.append(SF(SAF_N, eye="green", eye_on=0.35, sad=True, antenna=True, look=0))
    for who in KIDS:
        a = kid(who, set_, tt)
        if a: A.append(a)
    return A

def light_map(set_, sh, tt, cam, lights):
    x0, y0, z = cam; W3 = lambda px, py: ((px - x0) * z, (py - y0) * z)
    if set_ != "lobbyn": return None
    m = np.full((LH, LW, 3), 0.45, np.float32) * COOL
    if tt >= SCREEN:
        X, Y = W3(SAF_N[0], SAF_N[1] - 150 * SAF_N[2]); m += 1.1 * glow(X, Y, 260 * z)[..., None] * np.array([0.5, 1.2, 0.7], np.float32)
    lm = np.clip(m / 1.3, 0, 1)
    return Image.fromarray((lm * 255).astype(np.uint8), "RGB").resize((W, H), Image.BILINEAR)

def props(img, set_, tt, cam, sh):
    x0, y0, z = cam; S = SS * z; d = ImageDraw.Draw(img, "RGBA")
    W2 = lambda wx, wy: ((wx - x0) * S, (wy - y0) * S)
    lw = lambda v: max(1, int(v * S))
    if set_ == "street":
        # the loader behind the car (rolls forward a little, stops in front of Safeeh)
        u = ease(kk(tt, 0, 2.0)) * 0.3 + (ease(kk(tt, ROLL[0], RED)) * 0.25 if tt >= ROLL[0] else 0)
        X, Y = W2(LOADER[0] + 60 - 120 * u, LOADER[1]); s_ = 1.0 * S
        d.rectangle([X - 90 * s_, Y - 110 * s_, X + 90 * s_, Y], fill=(205, 160, 30, 255), outline=(40, 30, 10, 255), width=lw(4))
        d.rectangle([X - 60 * s_, Y - 180 * s_, X + 40 * s_, Y - 110 * s_], fill=(60, 80, 100, 255), outline=(40, 30, 10, 255), width=lw(4))
        d.line([(X - 90 * s_, Y - 60 * s_), (X - 170 * s_, Y - 40 * s_)], fill=(80, 80, 85, 255), width=lw(10))
        d.polygon([(X - 150 * s_, Y - 60 * s_), (X - 230 * s_, Y - 40 * s_), (X - 220 * s_, Y + 20 * s_), (X - 150 * s_, Y + 10 * s_)], fill=(90, 90, 95, 255), outline=(30, 30, 30, 255))
        for wx in (-55, 55): d.ellipse([X + (wx - 34) * s_, Y - 30 * s_, X + (wx + 34) * s_, Y + 38 * s_], fill=(20, 20, 20, 255))
        if tt < SONG_T[0] and int(tt * 4) % 2: d.ellipse([X - 14 * s_, Y - 200 * s_, X + 14 * s_, Y - 176 * s_], fill=(255, 150, 20, 255))
        if tt >= T("N15") - 0.5:   # the digging tools at the Pasha's feet
            bx, by = W2(PAS[0] + 70, PAS[1])
            d.line([(bx, by), (bx + 40 * S, by - 160 * S)], fill=(120, 80, 40, 255), width=lw(6))
            d.polygon([(bx - 20 * S, by), (bx + 20 * S, by), (bx + 10 * S, by + 30 * S), (bx - 10 * S, by + 30 * S)], fill=(150, 150, 155, 255))
            d.line([(bx + 60 * S, by), (bx + 110 * S, by - 150 * S)], fill=(120, 80, 40, 255), width=lw(6))
            d.polygon([(bx + 70 * S, by - 150 * S), (bx + 150 * S, by - 160 * S), (bx + 100 * S, by - 130 * S)], fill=(150, 150, 155, 255))
        if SONG_T[0] <= tt < SONG_T[1] + 1.0:   # notes floating over the street
            for i in range(8):
                v = ((tt - SONG_T[0]) * 0.35 + i / 8) % 1; X = (200 + i * 220 + math.sin(tt + i) * 40 - x0) * S; Y = (900 - v * 800 - y0) * S
                text(img, X, Y, "♪", int(70 * S), (255, 214, 90, int(255 * (1 - v))), (30, 10, 5), 2)
    if set_ == "stairs":
        sh_ = shot_at(tt); n = [2, 4, 5, 6, 7][min(4, sh_.get("floor", 0))]
        X, Y = W2(1700, 160); r = 80 * S
        d.ellipse([X - r, Y - r, X + r, Y + r], fill=(255, 214, 90, 230), outline=(40, 20, 10, 255), width=lw(5))
        text(img, X, Y - 10 * S, str(n), int(90 * S), (40, 20, 10), (255, 214, 90), 2)
        text(img, X, Y + 52 * S, "الدور", int(26 * S), (40, 20, 10), (255, 214, 90), 1)
    if set_ in ("facade", "facaden"):
        night = set_ == "facaden"
        for i, (wx, wy) in enumerate(WINS):
            if night and (wx, wy) != TOPWIN: continue
            on = 1.0 if night else ease(kk(tt, FAC[0] + i * 0.4, FAC[0] + i * 0.4 + 0.5))
            X, Y = W2(wx, wy); ww, wh = 50 * S, 70 * S
            d.rectangle([X - ww, Y - wh, X + ww, Y + wh], fill=(255, 210, 120, int(230 * on)))
            if not night and on > 0.5:   # a neighbour leans out
                d.ellipse([X - 22 * S, Y - 40 * S, X + 22 * S, Y + 4 * S], fill=(30, 20, 15, 255)); d.rectangle([X - 30 * S, Y + 4 * S, X + 30 * S, Y + wh], fill=(30, 20, 15, 255))
            if night and tt >= SHADOW - 0.6:   # the pharaoh's shadow slides across
                u = kk(tt, SHADOW - 0.6, SHADOW + 0.8); sx = X - ww + 2 * ww * u
                d.polygon([(sx - 26 * S, Y + wh), (sx - 26 * S, Y - 10 * S), (sx - 34 * S, Y - 40 * S), (sx, Y - 62 * S), (sx + 34 * S, Y - 40 * S),
                           (sx + 26 * S, Y - 10 * S), (sx + 26 * S, Y + wh)], fill=(10, 8, 6, 255))
                d.rectangle([sx - 6 * S, Y - 12 * S, sx + 6 * S, Y + 6 * S], fill=(10, 8, 6, 255))
        if not night:
            for i in range(8):
                v = ((tt - FAC[0]) * 0.3 + i / 8) % 1; X, Y = W2(300 + i * 200, 700 - v * 600)
                text(img, X, Y, "♪", int(60 * S), (255, 214, 90, int(255 * (1 - v))), (30, 10, 5), 2)
    if set_ == "lobbyn" and tt >= SCREEN:   # «أنا راجع» on Safeeh's chest screen
        X, Y = W2(SAF_N[0], SAF_N[1] - 175 * SAF_N[2])
        fl = 1.0 if tt > SCREEN + 0.4 else [1, 0, 1, 0, 1][min(4, int((tt - SCREEN) / 0.08))]
        if fl:
            d.rectangle([X - 70 * S, Y - 40 * S, X + 70 * S, Y + 40 * S], fill=(10, 30, 15, 255), outline=(120, 255, 150, 255), width=lw(3))
            text(img, X, Y, "أنا راجع", int(34 * S), (120, 255, 150), (0, 20, 0), 1)

# ---------- inserts ----------
def ins_bg(col=(30, 24, 18)):
    fr = Image.new("RGB", (W, H), col); return fr, ImageDraw.Draw(fr, "RGBA")
def radio_card(tt, sh):
    """S1E8 radio: front (memory flash) / the back opens → the record inside"""
    fr, d = ins_bg((26, 22, 18)); cx, cy = W / 2, H / 2
    d.rounded_rectangle([cx - 420, cy - 260, cx + 420, cy + 260], 50, fill=(110, 70, 40, 255), outline=(40, 25, 15, 255), width=10)
    if sh.get("front"):
        d.ellipse([cx - 360, cy - 200, cx - 20, cy + 140], fill=(60, 40, 25, 255))
        for i in range(6): d.line([(cx + 60, cy - 170 + i * 50), (cx + 360, cy - 170 + i * 50)], fill=(60, 40, 25, 255), width=12)
        d.rectangle([cx - 340, cy + 170, cx + 340, cy + 220], fill=(230, 200, 140, 255))
        for i in range(4):
            v = ((tt - sh["start"]) * 0.6 + i / 4) % 1
            text(fr, cx + 380 + math.sin(i * 2 + tt * 2) * 40, cy - 200 - v * 260, "♪", 90, (255, 214, 90, int(255 * (1 - v))), (30, 10, 5), 2)
        g = np.asarray(fr.convert("L"), np.float32) / 255
        fr = Image.fromarray(np.clip(np.stack([g * 255, g * 220, g * 170], -1), 0, 255).astype(np.uint8))
        text(fr, cx, cy + 330, "الموسم الأول...", 56, (255, 214, 90), (30, 10, 5), 4)
        return fr
    u = ease(kk(tt, sh["start"] + 0.4, sh["start"] + 1.2))
    d.rectangle([cx - 380, cy - 220, cx + 380, cy + 220], fill=(30, 22, 15, 255))
    gl = Image.new("RGBA", fr.size, (0, 0, 0, 0)); gd = ImageDraw.Draw(gl); gd.ellipse([cx - 300, cy - 260, cx + 300, cy + 260], fill=(255, 220, 140, int(140 * u)))
    fr.paste(gl.filter(ImageFilter.GaussianBlur(50)), (0, 0), gl.filter(ImageFilter.GaussianBlur(50)))
    d = ImageDraw.Draw(fr, "RGBA")
    d.ellipse([cx - 190, cy - 190, cx + 190, cy + 190], fill=(15, 15, 15, 255))
    for r in range(60, 190, 18): d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(45, 45, 45, 255), width=2)
    d.ellipse([cx - 60, cy - 60, cx + 60, cy + 60], fill=(190, 40, 40, 255))
    d.polygon([(cx - 380, cy - 220), (cx + 380, cy - 220), (cx + 380 - 700 * u, cy - 220 - 120 * u), (cx - 380, cy - 220 - 120 * u)], fill=(110, 70, 40, 255), outline=(40, 25, 15, 255))
    return fr
def rec_card(tt, sh):
    fr, d = ins_bg((20, 16, 12)); cx, cy = W / 2, H / 2 + 40; a = (tt - sh["start"]) * 3.5
    d.ellipse([cx - 380, cy - 380, cx + 380, cy + 380], fill=(110, 70, 40, 255))
    d.ellipse([cx - 330, cy - 330, cx + 330, cy + 330], fill=(15, 15, 15, 255))
    for r in range(110, 330, 22): d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(48, 48, 48, 255), width=2)
    d.line([(cx + math.cos(a) * 120, cy + math.sin(a) * 120), (cx + math.cos(a) * 320, cy + math.sin(a) * 320)], fill=(90, 90, 90, 180), width=6)
    d.ellipse([cx - 100, cy - 100, cx + 100, cy + 100], fill=(190, 40, 40, 255))
    text(fr, cx, cy - 22, "أغنية العمارة", 30, (255, 230, 200), (100, 10, 10), 1)
    ltr(fr, cx, cy + 28, "1958", 30, (255, 230, 200), (100, 10, 10), 1)
    d.line([(cx + 480, cy - 380), (cx + 420, cy - 60), (cx + 200, cy - 80)], fill=(200, 200, 205, 255), width=14)
    return fr
def live_card(tt, sh):
    fr = ImageEnhance.Brightness(bg_crop(SRC["street"], (600, 200, 1.5), True).resize((W, H))).enhance(0.95)
    d = ImageDraw.Draw(fr, "RGBA")
    d.rounded_rectangle([40, 40, 300, 120], 20, fill=(220, 30, 40, 255)); ltr(fr, 170, 80, "LIVE", 52, (255, 255, 255), (120, 0, 0), 2)
    d.rounded_rectangle([330, 40, 700, 120], 20, fill=(0, 0, 0, 150)); ltr(fr, 515, 80, f"{25000 + int((tt - sh['start']) * 9000)}", 46, (255, 255, 255), (0, 0, 0), 2)
    for i in range(8):
        v = ((tt - sh["start"]) * 0.9 + i / 8) % 1; x, y = W - 160 + math.sin(i * 2 + tt * 3) * 50, H - 120 - v * 650
        d.ellipse([x - 22, y - 22, x + 22, y + 22], fill=(255, 60, 90, int(255 * (1 - v))))
    return fr
def key_card(tt, sh):
    """Nana takes the «الدور الأخير» key from Tota and locks it in her drawer (S3 plant)"""
    fr, d = ins_bg((40, 30, 22)); u = kk(tt, sh["start"], sh["end"]); cx, cy = W / 2, H / 2
    d.rectangle([cx - 600, cy + 80, cx + 600, cy + 420], fill=(110, 70, 40, 255), outline=(50, 30, 15, 255), width=8)   # drawer
    d.rectangle([cx - 560, cy + 80, cx + 560, cy + 120], fill=(80, 50, 28, 255))
    ky = lerp(cy - 300, cy + 200, ease(kk(tt, sh["start"] + 0.5, sh["start"] + 1.6)))
    d.ellipse([cx - 60, ky - 60, cx + 60, ky + 60], outline=(200, 160, 60, 255), width=16); d.rectangle([cx + 55, ky - 10, cx + 300, ky + 10], fill=(200, 160, 60, 255))
    d.rounded_rectangle([cx - 40, ky + 80, cx + 230, ky + 150], 10, fill=(176, 170, 160, 255)); text(fr, cx + 95, ky + 115, "الدور الأخير", 40, (60, 40, 20), (176, 170, 160), 1)
    d.line([(cx - 700, ky - 600), (cx - 60, ky - 20)], fill=(22, 22, 22, 255), width=30)   # Nana's arm
    sl = ease(kk(tt, sh["start"] + 1.7, sh["end"] - 0.1))   # drawer closes over it
    d.rectangle([cx - 600, cy + 80 - 10, cx + 600, cy + 80 + 340 * sl], fill=(120, 78, 45, 255), outline=(50, 30, 15, 255), width=8)
    if sl > 0.9: d.ellipse([cx - 22, cy + 230, cx + 22, cy + 274], fill=(200, 160, 60, 255))
    return fr

def card_s3(tt, sh):
    k = (tt - sh["start"]) / (sh["end"] - sh["start"]); fr = Image.new("RGB", (W, H), (8, 8, 12))
    g = lambda c: tuple(int(v * min(1, k * 4)) for v in c)
    text(fr, W / 2, H / 2 - 250, "نهاية الموسم التاني", 70, g((235, 235, 235)))
    text(fr, W / 2, H / 2 - 120, "الموسم التالت: ليلة التماثيل", 100, g((255, 214, 90)), (40, 10, 10), 6)
    text(fr, W / 2, H / 2 + 10, "قريبًا...", 70, g((255, 120, 90)), (30, 5, 5), 5)
    text(fr, W / 2, H / 2 + 130, "المفتاح ده بيفتح إيه؟ اكتبوا توقعاتكم في الكومنتات", 48, g((235, 235, 235)))
    text(fr, W / 2 + 230, H - 90, "تابعونا:", 50, g((255, 214, 90)), (40, 10, 10), 4)
    ltr(fr, W / 2 - 110, H - 90, "@shattawzalata", 50, g((255, 214, 90)), (40, 10, 10), 4)
    return fr

def hud(fr, tt, v=False):
    sc = 0.85 if v else 1.0; cx = 540 if v else W / 2; y = 1700 if v else 120
    d = ImageDraw.Draw(fr, "RGBA")
    if ANS + 1.0 <= tt < ANS + DUR["N03"] + 0.4:
        d.rounded_rectangle([cx - 430 * sc, y - 50 * sc, cx + 430 * sc, y + 50 * sc], int(22 * sc), fill=(20, 60, 30, 220), outline=(120, 230, 120, 255), width=4)
        text(fr, cx, y, "إجابة امبارح: راديو الدور السابع ✓", int(42 * sc), (200, 255, 200))
    if T("N05") + DUR["N05"] * 0.55 <= tt < T("N05") + DUR["N05"] + 0.3:
        d.rounded_rectangle([cx - 150 * sc, y - 50 * sc, cx + 150 * sc, y + 50 * sc], int(22 * sc), fill=(60, 20, 20, 220), outline=(255, 120, 90, 255), width=4)
        ltr(fr, cx, y, "30%", int(56 * sc), (255, 160, 120))
    if 0.2 <= tt < 2.0:
        d.rounded_rectangle([cx - 150 * sc, y - 46 * sc, cx + 150 * sc, y + 46 * sc], int(20 * sc), fill=(10, 10, 14, 200), outline=(230, 200, 120, 255), width=3)
        ltr(fr, cx, y, "6:55", int(50 * sc), (255, 230, 170))

PUZ_TXT = "المفتاح ده بيفتح إيه؟"
def puzzle_box(fr, tt, cx, y, sc=1.0):
    d = ImageDraw.Draw(fr, "RGBA"); k = ease(kk(tt, PUZ + 0.2, PUZ + 0.7))
    d.rounded_rectangle([cx - 560 * sc, y - 70 * sc, cx + 560 * sc, y + 90 * sc], int(26 * sc), fill=(20, 20, 30, int(225 * k)), outline=(255, 214, 90, int(255 * k)), width=5)
    text(fr, cx, y - 15 * sc, "لغز آخر الموسم: " + PUZ_TXT, int(42 * sc), (255, 214, 90))
    text(fr, cx, y + 45 * sc, "اكتبوا توقعاتكم في الكومنتات", int(34 * sc), (235, 235, 235))

TINT = {"street": (255, 236, 205), "lobby": (255, 246, 228), "stairs": (255, 238, 210), "apt7": (200, 205, 230), "lobbyn": (150, 165, 225)}
INS = (("radioins", radio_card), ("liveins", live_card), ("recins", rec_card), ("keyins", key_card))
def frame(tt, plat="yt"):
    sh = shot_at(tt); set_ = sh["set"]
    if set_ == "title": return finish(card(set_, tt, sh), tt)
    if set_ == "endcard": return finish(card_s3(tt, sh), tt)
    if set_ == "black": return Image.new("RGB", (W, H), (0, 0, 0))
    if set_ == "phone": return finish(phone_card(tt, sh, plat), tt)
    for k_, fn in INS:
        if sh.get(k_): return finish(fn(tt, sh), tt, True)
    cam = cam_at(sh, tt)
    img = bg_frame(set_, cam, sh, tt)
    layer, lights = draw_scene_chars(set_, tt, cam, sh)
    layer = tint_layer(layer, TINT.get(set_, (255, 244, 225)), 0.97)
    if set_ == "street": props(img, set_, tt, cam, sh)   # the loader stands behind the people
    img.paste(layer, (0, 0), layer)
    if set_ != "street": props(img, set_, tt, cam, sh)
    fr = img.resize((W, H), Image.LANCZOS)
    lm = light_map(set_, sh, tt, cam, lights)
    if lm is not None: fr = ImageEnhance.Brightness(ImageChops.multiply(fr, lm)).enhance(1.5)
    return finish(fr, tt, set_ in ("lobbyn", "facaden", "apt7"))

def build_audio(path="mix.wav"):
    buf = np.zeros(int(TOTAL * SR) + SR * 3, dtype=np.float32)
    dr = drone(TOTAL + 1); env = np.zeros(len(dr), np.float32)
    for a_, b_ in ((0, TITLE), (T("N07"), SONG_T[0]), (NIGHT[0], TOTAL - 5.5)):
        env[int(a_ * SR):int(b_ * SR)] = 1.0
    env = np.convolve(env, np.ones(4410) / 4410, mode="same")
    mix_into(buf, dr * env, 0, 1.2)
    r = np.random.default_rng(9)
    S = {"boom": sfx_boom(), **SFXF}
    for t0, nme, g in sfx:
        if nme in S and g > 0: mix_into(buf, S[nme], t0, g)
    # loader diesel under the street scenes until the song
    a_, b_ = 0, SONG_T[0]; tp = np.arange(int((b_ - a_) * SR)) / SR
    die = (np.sign(np.sin(2 * np.pi * 38 * tp)) * 0.035 + np.sin(2 * np.pi * 76 * tp) * 0.03).astype(np.float32)
    for st in shots:
        if st["set"] != "street" or st["start"] >= b_: continue
        i0, i1 = int(st["start"] * SR), min(len(die), int(st["end"] * SR))
        if i1 > i0: buf[i0:i1] += die[i0:i1] * (2.0 if ROLL[0] <= st["start"] < RED else 1.0)
    # THE SONG: from the record insert to the end of Nana's lines, ducked under the dialogue
    a_, b_ = SONG_T[0] + 0.3, SONG_T[1] + 2.5
    n = int((b_ - a_) * SR); song = SONGA[int(2.0 * SR): int(2.0 * SR) + n]
    if len(song) < n: song = np.pad(song, (0, n - len(song)))
    e = np.ones(n, np.float32); fi = int(1.0 * SR); e[:int(0.3 * SR)] = np.linspace(0, 1, int(0.3 * SR)); e[-fi:] = np.linspace(1, 0, fi)
    duck = np.ones(n, np.float32)
    for st, k in lines:
        if a_ <= st < b_:
            i0 = int((st - a_) * SR); i1 = min(n, int((st + DUR[k] - a_) * SR)); duck[max(0, i0 - 4000):i1 + 4000] = 0.3
    duck = np.convolve(duck, np.ones(4410) / 4410, mode="same")
    mix_into(buf, song.astype(np.float32) * e * duck, a_, 0.9)
    # comic stings: 30%, «أنا صاحي أهو», the slipper
    for t_, notes in ((T("N05") + DUR["N05"] * 0.55, [523, 494, 440, 392]), (T("N18") + DUR["N18"] - 0.3, [784, 659, 523]), (T("N02") + 0.2, [392, 523, 659])):
        for i, f in enumerate(notes):
            tt_ = np.arange(int(SR * 0.4)) / SR
            mix_into(buf, np.sin(2 * np.pi * f * tt_) * np.exp(-tt_ * 12) * 0.09, t_ + i * 0.18, 1.0)
    # applause + cheer when the Pasha leaves
    n = int(3.0 * SR); cl = np.zeros(n, np.float32)
    for _ in range(260):
        i = r.integers(0, n - 2000); cl[i:i + 600] += r.normal(0, 1, 600).astype(np.float32) * np.exp(-np.arange(600) / 120)
    mix_into(buf, cl * 0.12 * np.minimum(1, np.linspace(3, 0, n)), PEXIT[0], 1.0)
    # night: music box + rising tension to the shadow
    for i in range(int((TILT[1] - NIGHT[0]) / 0.5)):
        f = [523, 659, 784, 659][i % 4]; tb = np.arange(int(SR * 0.45)) / SR
        mix_into(buf, np.sin(2 * np.pi * f * tb) * np.exp(-tb * 6) * 0.03, NIGHT[0] + i * 0.5, 1.0)
    tsx = np.arange(int(SR * 0.25)) / SR
    for st, g in STEPS:
        nz = np.convolve(r.normal(0, 1, len(tsx)), np.ones(12) / 12, mode="same")
        mix_into(buf, (np.sin(2 * np.pi * 80 * tsx) * np.exp(-tsx * 30) * 0.9 + nz * np.exp(-tsx * 25) * 0.9) * 0.6, st, g)
    for st, k in lines:
        a = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8
        if k == "N21":
            out = np.zeros(len(a) + int(SR * 0.6), np.float32); out[:len(a)] += a
            for dl, g in ((0.2, 0.35), (0.4, 0.18)): i = int(dl * SR); out[i:i + len(a)] += a * g
            a = out
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
    bgc = bg_crop(SRC["street"], (600, 100, 1.6), True).resize((W, H))
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
