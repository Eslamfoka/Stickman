# «مين الكداب؟» — القضية 14: «الطرد على الدكة» (27/11). Voices approved by Eslam (17:41), one take each (gens.txt).
# Canonical lobby only (s1e10/bg/morning.png) — no new place. The parcel and the CCTV look are drawn by code.
# Structure (growth rules 35–37): CCTV hook (parcel on the bench 06:09→06:12, cut → 06:15 empty) → Nana comes down the stairs to an
#   empty bench → Zalata + Tota come down after her shout → Tota replays the lobby camera → the suspects arrive (Shatta + Sawsan down the
#   stairs, the doorman in from the street door) → each statement acted as a sepia flashback «حسب كلامه» (stairs shots keep the bench
#   OUT of frame, as in the script) → «حل القضية ١٣» (case-13 visuals only) → final card (the ONE ask, voiced on the card).
# ANSWER (producer only, opens case 15): ② سوسن — the camera shows the parcel on the bench until 06:12; she says it was empty at 06:11.
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont, ImageChops, ImageOps
sys.path.insert(0, ROOT + "/s2"); import vnative as VN
os.chdir(ROOT + "/kaddab/14")
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"; DJ = ROOT + "/brand/fonts/DejaVuSans-Bold.ttf"
TXT = {"T0": "واحد فيهم بيكدب.", "N1": "طردي راح! الشبشب جايلكم!", "Z1": "راح بين ستة واتناشر وستة وربع. أنا حاسبها بالقلم.",
       "T1": "اللقطة دي من كاميرا المدخل.",
       "S1": "نزلت أجيب عيش ستة وعشرة… شفت الطرد على الدكة من على السلم، وما لمستوش! ثقوا فيا المرة دي!",
       "W1": "أنا نزلت ستة وحداشر دقيقة. بصيت من على السلم لقيت الدكة فاضية، فرجعت فوق. كنت لايف!",
       "B1": "كنت عند الكشك. رجعت ستة وربع لقيتها فاضية. أنا صاحي أهو!",
       "T2": "إجابة القضية اللي فاتت: الكداب كان شطة! قال «خاتم»… وعزيزة ما قالتش «خاتم»… وهو فوق على السطوح… وحبات السمسم على غطا العلبة من ساندوتشه!",
       "T3": "اكتب رقم الكداب!"}
KEYS = list(TXT)
WHO = {"T0": "tota", "N1": "nana", "Z1": "zalata", "T1": "tota", "S1": "shatta", "W1": "sawsan", "B1": "bondo2", "T2": "tota", "T3": "tota"}
NAME = {"nana": ("نعناعة", (150, 220, 190)), "zalata": ("زلطة", (140, 220, 120)), "tota": ("توتة", (255, 130, 190)),
        "shatta": ("شطة", (255, 140, 80)), "sawsan": ("سوسن", (255, 170, 80)), "bondo2": ("البواب", (230, 170, 110))}
EXPR = {"T0": "scared", "N1": [(0, "shock"), (0.35, "angry")], "Z1": [(0, "neutral"), (0.6, "smug")], "T1": "smug",
        "S1": [(0, "happy"), (0.62, "scared")], "W1": [(0, "neutral"), (0.85, "happy")], "B1": [(0, "sleepy"), (0.7, "happy")],
        "T2": "smug", "T3": "smug"}
load_lines(KEYS)
CHV = {k: VN.chunk_times(TXT[k], ENV[k], FPS) for k in KEYS}
# T2 = the approved take with «غير في المدخل،» cut out (5.965–6.62 s of the original; original kept as audio/T2_orig_take.mp3):
#   Aziza said «خاتمي» in the room AND in the lobby — both while Shatta was on the roof — so «only in the lobby» was not accurate.
CHV["T2"] = [(0.0, "إجابة القضية اللي فاتت:"), (1.62, "الكداب كان شطة!"), (3.3, "قال «خاتم»…"), (4.6, "وعزيزة ما قالتش «خاتم»…"),
             (6.2, "وهو فوق على السطوح…"), (7.8, "وحبات السمسم على غطا"), (8.75, "العلبة من ساندوتشه!")]
VN.set_font(LZ)

def tinted(img, lvl, tint): return ImageChops.multiply(ImageEnhance.Brightness(img).enhance(lvl), Image.new("RGB", img.size, tint))
LOB0 = _ld(ROOT + "/s1e10/bg/morning.png")
LOB = tinted(LOB0, 0.97, (236, 238, 255))                         # 06:15 — early morning (canonical lobby, light only)
LOBF = ImageOps.colorize(ImageOps.grayscale(LOB0), (46, 30, 16), (250, 222, 176))      # flashback «حسب كلامه» = sepia
CC = {(k, o): Image.open(f"c13/{k}_{o}.png").convert("RGB") for k in ("roof", "lob", "sesame", "seeds") for o in "hv"}
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
FEET = 1040
PARCEL = (318, 650)                     # on the doorman's bench (seat top ≈ y 660)
STAIR = (1340, 905, 1.3)                # bottom steps — «من على السلم»
STAIR_IN = (1400, 860, 1.2)             # where people come down from
STREET = (745, 640, 0.75)               # street door
POS = {"nana": (560, FEET, 1.55), "tota": (770, FEET, 1.42), "zalata": (985, FEET, 1.6),
       "shatta": (1215, FEET, 1.55), "sawsan": (1440, FEET, 1.55), "bondo2": (1665, FEET, 1.55)}
NUMS = (("shatta", (210, 60, 40)), ("sawsan", (150, 70, 190)), ("bondo2", (150, 96, 50)))

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
HOOK_END = 3.0; GL = (2.15, 2.45)                                       # CCTV glitch 06:12 → 06:15
shot("cctv", 0.0, HOOK_END, None, v=None, cc="hook"); say(0.5, "T0")
A0 = HOOK_END; NANA_IN = (A0 + 0.15, A0 + 1.55)                         # Nana comes down the stairs to the empty bench
shot("lob", A0, NANA_IN[1] + 0.1, (1100, 620, 1.12), (760, 640, 1.3), v=((1250, 650, 1.8), (700, 650, 1.85)), title="٦:١٥", follow=("nana",))
s = NANA_IN[1] + 0.1; t = say(s + 0.05, "N1") + 0.1; shakes.append((T("N1") + 0.9, 12))
shot("lob", s, t, (560, 690, 2.2), (560, 720, 2.55), v=((560, 640, 2.5), (560, 630, 2.75)), tin="zoom")
Z_IN = (t - 0.6, t + 1.3)                                               # her shout brings Zalata + Tota down the stairs
shot("lob", t, Z_IN[1] + 0.05, (1100, 620, 1.2), (900, 630, 1.3), v=((1200, 650, 1.85), (900, 650, 1.85)), follow=("zalata", "tota"), tin="whip")
s = Z_IN[1] + 0.05; t = say(s + 0.05, "Z1") + 0.15
shot("lob", s, t, (985, 640, 1.8), (985, 640, 1.95), v=((985, 650, 2.25), (985, 650, 2.35)))
s = t; t = say(t + 0.05, "T1") + 0.05
shot("lob", s, t, (770, 650, 1.85), (770, 650, 2.0), v=((770, 660, 2.3), (770, 660, 2.4)), tin="whip")
CC2 = (t, t + 2.7); shot("cctv", t, CC2[1], None, v=None, cc="replay", tin="flash"); t = CC2[1]
GATHER = (t, t + 2.3)                                                   # the three suspects arrive
shot("lob", t, GATHER[1], (960, 600, 1.0), (1000, 610, 1.05), v=((1250, 650, 1.85), (1300, 650, 1.85)), tin="whip"); t = GATHER[1]
BADGES = t - 0.55
def fb_win(k, upto):                                                    # flashback covers phrases [0, upto) of line k
    return (T(k) + 0.9, T(k) + CHV[k][upto][0])
FB = {}
for k, who, ts_, upto in (("S1", "shatta", "٦:١٠", 2), ("W1", "sawsan", "٦:١١", 4), ("B1", "bondo2", "٦:١٥", 2)):
    s = t; t = say(t + 0.15, k) + 0.25; x_ = POS[who][0]; FB[who] = fb_win(k, upto)
    a_, b_ = FB[who]
    shot("lob", s, a_, (x_, 640, 1.8), (x_, 640, 1.85), v=((x_, 650, 2.25), (x_, 650, 2.3)), tin="whip")
    if who == "bondo2": shot("fb", a_, b_, (900, 640, 1.2), (700, 660, 1.3), v=((780, 650, 1.85), (560, 650, 1.85)), who=who, title=ts_, tin="fade", follow=(who,))
    else: shot("fb", a_, b_, (1360, 660, 1.9), (1340, 680, 2.1), v=((1340, 660, 2.0), (1340, 680, 2.15)), who=who, title=ts_, tin="fade")
    shot("lob", b_, t, (x_, 640, 1.85), (x_, 640, 1.95), v=((x_, 650, 2.3), (x_, 650, 2.4)), tin="fade")
SUS = (t, t + 1.6)                                                      # the silent beat: slow push across the three suspects
shot("lob", t, SUS[1], (1440, 640, 1.25), (1440, 640, 1.4), v=((1215, 650, 1.85), (1665, 650, 1.85))); t = SUS[1]
SEG0 = t; s_ = say(t + 0.5, "T2"); SEG1 = s_ + 0.4
shot("c13", SEG0, SEG1, None, v=None, tin="flash"); t = SEG1
Q = t; say(Q + 0.35, "T3"); t = Q + 0.35 + DUR["T3"] + 1.1
shot("q", Q, t, None, v=None)
TOTAL = t

def _fol(sh, tt):
    names = sh.get("follow")
    if not names: return None
    xs = [p[1] for p in cast_at(sh, tt) if p[0] in names]
    return sum(xs) / len(xs) if xs else None
def vcam(sh, tt):
    c0, c1 = sh["v"]; k = ease((tt - sh["start"]) / max(0.01, sh["end"] - sh["start"]))
    cx, cy, z = [a_ + (b_ - a_) * k for a_, b_ in zip(c0, c1)]; z = max(z, 1920 / 1080)
    f = _fol(sh, tt)
    if f is not None: cx = f
    shake = 0
    for st, amp in shakes:
        if 0 <= tt - st < 0.45: shake = max(shake, amp * (1 - (tt - st) / 0.45))
    cw, ch = 1080 / z, 1920 / z
    x0 = min(max(cx - cw / 2, 0), 1920 - cw); y0 = min(max(cy - ch / 2, 0), 1080 - ch)
    if shake: x0 = min(max(x0 + rng.normal(0, shake / z), 0), 1920 - cw)
    return x0, y0, z
def hcam(sh, tt):
    c0, c1 = sh["c0"], sh["c1"]; k = ease((tt - sh["start"]) / max(0.01, sh["end"] - sh["start"]))
    cx, cy, z = [a_ + (b_ - a_) * k for a_, b_ in zip(c0, c1)]
    f = _fol(sh, tt)
    if f is not None: cx = lerp(cx, f, 0.6)
    shake = 0
    for st, amp in shakes:
        if 0 <= tt - st < 0.45: shake = max(shake, amp * (1 - (tt - st) / 0.45))
    cw, ch = 1920 / z, 1080 / z
    x0 = min(max(cx - cw / 2, 0), 1920 - cw); y0 = min(max(cy - ch / 2, 0), 1080 - ch)
    if shake: x0 = min(max(x0 + rng.normal(0, shake / z), 0), 1920 - cw)
    return x0, y0, z

# ---------------- who is where (continuity) ----------------
def walker(p0, p1, win, tt, rate=8):
    u = ease(kk(tt, *win)); return lerp(p0[0], p1[0], u), lerp(p0[1], p1[1], u), lerp(p0[2], p1[2], u), (tt * rate if 0 < kk(tt, *win) < 1 else None)
def cast_at(sh, tt):
    """[(who, x, y, s, look, arms, held, walk)]"""
    C = []
    if sh["set"] == "fb":
        who = sh["who"]; u = tt - sh["start"]
        if who == "shatta":                                           # 06:10 — down the stairs with the bread, glances at the bench (off frame left)
            x, y, s, w = walker(STAIR_IN, STAIR, (sh["start"], sh["start"] + 0.8), tt, 8)
            C.append(("shatta", x, y, s, -1, "hold", "basket", w))
        elif who == "sawsan":                                         # 06:11 — her claim: on the stairs, live on the phone, looks, goes back up
            back = sh["end"] - 0.9
            x, y, s, w = walker(STAIR_IN, STAIR, (sh["start"], sh["start"] + 0.8), tt, 8)
            if tt >= back: x, y, s, w = walker(STAIR, STAIR_IN, (back, sh["end"] + 0.1), tt, 8)
            C.append(("sawsan", x, y, s, 1 if tt >= back else -1, "phone", "phone", w))
        else:                                                         # 06:15 — in from the street door to the empty bench
            x, y, s, w = walker(STREET, (520, 1000, 1.5), (sh["start"] + 0.1, sh["end"] - 0.6), tt, 8)
            C.append(("bondo2", x, y, s, -1, "down", None, w))
        return C
    if sh["set"] != "lob": return C
    x, y, s, w = walker(STAIR_IN, POS["nana"], NANA_IN, tt, 9)
    C.append(("nana", x, y, s, -1 if tt < Z_IN[0] + 0.5 else 1, "down", "slipper", w))
    if tt >= Z_IN[0]:
        x, y, s, w = walker(STAIR_IN, POS["zalata"], Z_IN, tt, 9); C.append(("zalata", x, y, s, -1, "hold", "nbpen", w))
        x, y, s, w = walker(STAIR_IN, POS["tota"], (Z_IN[0] + 0.25, Z_IN[1] + 0.2), tt, 9); C.append(("tota", x, y, s, -1 if w else 1, "hold", "phone", w))
    if tt >= GATHER[0]:
        x, y, s, w = walker(STAIR_IN, POS["shatta"], (GATHER[0], GATHER[0] + 1.2), tt, 9); C.append(("shatta", x, y, s, -1, "hold", "basket", w))
        x, y, s, w = walker(STAIR_IN, POS["sawsan"], (GATHER[0] + 0.35, GATHER[0] + 1.6), tt, 9); C.append(("sawsan", x, y, s, -1, "phone", "phone", w))
        x, y, s, w = walker(STREET, POS["bondo2"], (GATHER[0] + 0.1, GATHER[0] + 2.0), tt, 9); C.append(("bondo2", x, y, s, -1, "down", None, w))
    C.sort(key=lambda c: c[2])                                        # far first
    return C

def draw_cast(lay, cam, sh, tt):
    k, lt = line_at(tt); fbk = sh["set"] == "fb"
    for who, x, y, s, look, arms, held, walk in cast_at(sh, tt):
        talking = (not fbk) and k is not None and WHO.get(k) == who
        if talking: e = expr_of(k, lt)
        elif fbk: e = {"shatta": "happy", "sawsan": "happy", "bondo2": "sleepy"}[who]
        elif who == "nana": e = "shock" if tt < T("N1") else "angry"
        elif who in ("shatta", "sawsan", "bondo2") and tt >= BADGES: e = "scared" if k in ("Z1", None) or WHO.get(k) in ("shatta", "sawsan", "bondo2") else "neutral"
        elif who == "tota": e = "smug"
        else: e = "neutral"
        mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
        a = arms
        if talking and arms == "down": a = "talk"
        if who == "nana" and k == "N1": a = "up"
        if who == "nana" and walk is None and tt < T("N1") and not talking: a = "hold"
        if who == "bondo2" and talking and lt > DUR["B1"] * 0.7: a = "up"
        X, Y_ = W2S(cam, x, y); S = s * cam[2]
        lk = look
        if not fbk and walk is None and who in ("shatta", "sawsan", "bondo2", "zalata", "tota", "nana") and k and WHO.get(k) != who and tt >= BADGES:
            sp = POS.get(WHO.get(k)); lk = (1 if sp and sp[0] > x else -1) if sp else look      # listeners turn to the speaker
        draw_char(P(lay), who, X, Y_, S, e, mouth, lk, ((tt + len(who) * 0.37) % 3.6) < 0.11 and e != "sleepy", a, tt, held, 0.0, walk)

# ---------------- props ----------------
def parcel(d, QW, zz):
    q = QW(*PARCEL); w, h = 46 * zz, 30 * zz
    d.rectangle([q[0] - w, q[1] - h, q[0] + w, q[1]], fill=(176, 128, 74), outline=(80, 52, 24), width=max(1, int(2 * zz)))
    d.polygon([(q[0] - w, q[1] - h), (q[0] + w, q[1] - h), (q[0] + w - 10 * zz, q[1] - h - 9 * zz), (q[0] - w + 10 * zz, q[1] - h - 9 * zz)], fill=(196, 148, 92), outline=(80, 52, 24))
    lw = max(1, int(3 * zz))
    d.line([(q[0], q[1] - h - 9 * zz), (q[0], q[1])], fill=(200, 30, 40), width=lw)                 # red string
    d.line([(q[0] - w + 5 * zz, q[1] - h - 4 * zz), (q[0] + w - 5 * zz, q[1] - h - 4 * zz)], fill=(200, 30, 40), width=lw)
    d.line([(q[0] - w, q[1] - h * 0.5), (q[0] + w, q[1] - h * 0.5)], fill=(200, 30, 40), width=lw)
    d.rectangle([q[0] + 10 * zz, q[1] - h * 0.42, q[0] + 34 * zz, q[1] - h * 0.08], fill=(245, 240, 225))      # address label

def scene(tt, sh, cam, size):
    Wd, Hd = size; x0, y0, z = cam; fbk = sh["set"] == "fb"
    src = LOBF if fbk else LOB
    img = src.resize((int(Wd * SS), int(Hd * SS)), Image.BICUBIC, box=(x0, y0, x0 + Wd / z, y0 + Hd / z))
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); draw_cast(lay, cam, sh, tt)
    if fbk: lay = _sepia_layer(lay)
    else: lay = tint_layer(lay, (240, 242, 255))
    img.paste(lay, (0, 0), lay)
    fr = img.resize((Wd, Hd), Image.LANCZOS)
    if fbk:
        d = ImageDraw.Draw(fr, "RGBA"); vert = Hd > Wd
        if sh["who"] == "sawsan":                                         # «كنت لايف» — her live badge
            for who, x, y, s, *_ in cast_at(sh, tt):
                S_ = s * CH[who]["scale"]; q = W2S(cam, x, y - 236 * S_ - 40 * S_)
                if int(tt * 3) % 2: d.ellipse([q[0] - 70, q[1] - 22, q[0] - 50, q[1] - 2], fill=(230, 30, 40))
                d.rounded_rectangle([q[0] - 44, q[1] - 30, q[0] + 50, q[1] + 6], 10, fill=(230, 30, 40, 235)); lzt(fr, q[0] + 3, q[1] - 12, "LIVE", 26, (255, 255, 255), font=DJ, stroke=False)
        lzt(fr, Wd / 2, Hd * (0.24 if not vert else 0.86), "حسب كلامه" if sh["who"] != "sawsan" else "حسب كلامها", 52 if not vert else 60, (255, 236, 190), (40, 24, 10))
    if sh.get("title"): lzt(fr, Wd / 2, Hd * (0.12 if Hd > Wd else 0.13), sh["title"], int(96 * popk(tt, sh["start"] + 0.1) * (1 - kk(tt, sh["start"] + 1.6, sh["start"] + 2.0))), (255, 230, 150))
    return fr
def _sepia_layer(lay):
    a = np.asarray(lay).astype(np.float32); g = (a[..., 0] * 0.3 + a[..., 1] * 0.59 + a[..., 2] * 0.11)[..., None] / 255
    lo, hi = np.array([40, 26, 14], np.float32), np.array([255, 234, 196], np.float32)
    out = np.concatenate([lo + (hi - lo) * g, a[..., 3:4]], -1)
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), "RGBA")

# ---------------- CCTV (the lobby camera) ----------------
def _ts(sec):
    sec = int(sec); return f"27-11-2026  {sec // 3600:02d}:{sec % 3600 // 60:02d}:{sec % 60:02d}"
T609 = 6 * 3600 + 9 * 60
def cctv(tt, sh, Wd, Hd):
    vert = Hd > Wd; u = tt - sh["start"]; kind = sh["cc"]
    box = (0, 230, 540, 1190) if vert else (0, 395, 900, 901)                # high corner view of the bench
    if vert: box = (0, 120, 540, 1080)
    bx0, by0, bx1, by1 = box; zc = Wd / (bx1 - bx0)
    if kind == "hook":
        if u < GL[0]: sec = T609 + (u / GL[0]) * 239; present = True
        else: sec = 6 * 3600 + 15 * 60 + 3 + (u - GL[1]) * 1.0; present = False
    else:
        dur = sh["end"] - sh["start"]; sec = T609 + 5 + min(1, u / (dur - 0.35)) * 230; present = True
    img = LOB0.resize((int(Wd * SS), int(Hd * SS)), Image.BICUBIC, box=box)
    d = ImageDraw.Draw(img, "RGBA"); QW = lambda x, y: ((x - bx0) * zc * SS, (y - by0) * zc * SS)
    if present: parcel(d, QW, zc * SS)
    fr = img.resize((Wd, Hd), Image.LANCZOS)
    a = np.asarray(ImageOps.grayscale(fr), np.float32)
    a = a * 0.9 + np.random.default_rng(int(tt * FPS)).normal(0, 9, a.shape)
    rgb = np.stack([a * 0.78, a * 0.98, a * 0.82], -1)
    rgb[::4] *= 0.82                                                       # scanlines
    if kind == "hook" and GL[0] <= u < GL[1]:                              # glitch between 06:12 and 06:15
        r_ = np.random.default_rng(int(tt * 97)); rgb = r_.uniform(20, 200, rgb.shape).astype(np.float32)
        for _ in range(6):
            y_ = int(r_.uniform(0, Hd - 40)); rgb[y_:y_ + int(r_.uniform(8, 40))] = 240
    fr = Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8)); fr = ImageChops.multiply(fr, VIG.resize(fr.size))
    d = ImageDraw.Draw(fr, "RGBA"); m = 40 if not vert else 50
    if int(tt * 2.5) % 2: d.ellipse([m, m, m + 30, m + 30], fill=(235, 30, 30))
    lzt(fr, m + 92, m + 15, "REC", 34, (255, 255, 255), font=DJ, stroke=False)
    lzt(fr, Wd - m - 150, m + 15, "CAM 01", 34, (255, 255, 255), font=DJ, stroke=False)
    if not (kind == "hook" and GL[0] <= u < GL[1]) and not sh.get("cover"):
        ty = (Hd - 190) if not vert else Hd - 330; sz = 52 if not vert else 50
        d.rectangle([0, ty - sz, Wd, ty + sz], fill=(0, 0, 0, 150))
        lzt(fr, Wd / 2, ty, _ts(sec), sz, (255, 255, 255), font=DJ, stroke=False)
        if present and (kind != "hook" or u < GL[0]):
            lzt(fr, Wd - m - 110, m + 80, "▶▶ ×60", 34, (255, 230, 120), font=DJ, stroke=False)
    if kind == "replay": lzt(fr, Wd / 2, Hd * (0.16 if vert else 0.2), "كاميرا المدخل", 70 if vert else 64, (255, 255, 255), (10, 10, 10))
    return fr

# ---------------- helpers ----------------
def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255, font=None, stroke=True):
    if size < 4: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(font or LZ, size)
    kw = dict(font=f, anchor="mm", direction="rtl", language="ar") if font is None else dict(font=f, anchor="mm")
    if stroke: d.text((x, y), s, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), **kw)
    d.text((x, y), s, fill=fill + (alpha,), **kw)
    img.paste(lay, (0, 0), lay)
def popk(tt, t0, d=0.22):
    u = kk(tt, t0, t0 + d); return 0 if u <= 0 else (1 + 0.25 * math.sin(u * math.pi)) if u < 1 else 1
def badge(fr, x, y, n, sc, col):
    if sc <= 0: return
    d = ImageDraw.Draw(fr, "RGBA"); r = 44 * sc
    d.ellipse([x - r, y - r, x + r, y + r], fill=col + (255,), outline=(255, 255, 255, 255), width=max(1, int(6 * sc)))
    lzt(fr, x, y + 4 * sc, n, int(66 * sc), (255, 255, 255), font=DJ)
_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/kaddab/14")
def add_badges(fr, tt, sh, cam):
    if sh["set"] != "lob" or tt < BADGES: return
    Wd, Hd = fr.size
    for i, (who, col) in enumerate(NUMS):
        x, y, s = POS[who]; S_ = s * CH[who]["scale"]; q = W2S(cam, x, y - 236 * S_ - 60 * S_)
        if -100 < q[0] < Wd + 100: badge(fr, q[0], max(q[1], 120 if Hd < Wd else 300), str(i + 1), min(1.15, cam[2] * 0.55) * popk(tt, BADGES + i * 0.12), col)

def seg13(tt, Wd, Hd):
    vert = Hd > Wd; o = "v" if vert else "h"; lt = tt - T("T2"); ch = CHV["T2"]
    idx = max([i for i, (off, _) in enumerate(ch) if lt >= off] or [0])
    key = {0: "roof", 1: "roof", 2: "roof", 3: "lob", 4: "roof", 5: "seeds", 6: "sesame"}[idx]
    if lt < 0: key = "roof"
    fr = CC[(key, o)].copy(); u = lt - (ch[idx][0] if lt >= 0 else 0)
    sc = 1 + 0.06 * min(1, max(0, u) / 2.5)                                   # slow push on each still
    fr = fr.resize((int(Wd * sc), int(Hd * sc)), Image.BICUBIC).crop((int(Wd * (sc - 1) / 2), int(Hd * (sc - 1) / 2), int(Wd * (sc - 1) / 2) + Wd, int(Hd * (sc - 1) / 2) + Hd))
    fr = ImageEnhance.Brightness(fr).enhance(0.88); d = ImageDraw.Draw(fr, "RGBA")
    if key == "roof" and idx in (1, 2, 4) and lt > 0:                            # circle Shatta (the case-13 liar)
        cx, cy = (Wd * 0.5, Hd * 0.55) if vert else (1060, 470)
        r = (260 if vert else 170) * popk(u, 0.15)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(110, 220, 255), width=10)
    by = Hd * (0.06 if vert else 0.07); bh = 120 if vert else 100
    d.rectangle([0, by - bh / 2, Wd, by + bh / 2], fill=(30, 120, 60, 255)); lzt(fr, Wd / 2, by, "حل القضية ١٣", 78 if vert else 70, (255, 255, 255), (10, 40, 20))
    return fr
def q_card(tt, sh, Wd, Hd):
    vert = Hd > Wd; fr = Image.new("RGB", (Wd, Hd), (40, 12, 14)); d = ImageDraw.Draw(fr, "RGBA")
    for i in range(18):
        a0 = math.radians(i * 20 + tt * 6); b = a0 + math.radians(9); R = 3000
        d.polygon([(Wd / 2, Hd * 0.5), (Wd / 2 + R * math.cos(a0), Hd * 0.5 + R * math.sin(a0)), (Wd / 2 + R * math.cos(b), Hd * 0.5 + R * math.sin(b))], fill=(58, 18, 20))
    g = 1.25 if vert else 1.0; cy = Hd * 0.15
    d.rounded_rectangle([Wd / 2 - 210 * g, cy - 150 * g, Wd / 2 + 210 * g, cy - 70 * g], 30, fill=(200, 30, 40, 240))
    lzt(fr, Wd / 2, cy - 110 * g, "قضية ١٤", int(56 * g), (255, 255, 255), stroke=False)
    lzt(fr, Wd / 2, cy + 10 * g, "مين الكداب؟", int(120 * g * popk(tt, sh["start"] + 0.05, 0.3)), (255, 214, 90))
    lay = Image.new("RGBA", (int(Wd * SS), int(Hd * SS)), (0, 0, 0, 0)); p = P(lay)
    pos = [(Wd * 0.3, Hd * 0.5), (Wd * 0.7, Hd * 0.5), (Wd * 0.5, Hd * 0.8)] if vert else [(Wd * (0.25 + 0.25 * j), Hd * 0.78) for j in range(3)]
    sc = 1.4 if vert else 1.6
    for (who, col), (x, y) in zip(NUMS, pos):
        if popk(tt, sh["start"] + 0.2) > 0: draw_char(p, who, x, y, sc, "neutral", 0.0, 1, False, "down", tt, None, 0.0, None)
    L = lay.resize((Wd, Hd), Image.LANCZOS); fr.paste(L, (0, 0), L)
    for i, ((who, col), (x, y)) in enumerate(zip(NUMS, pos)):
        u = popk(tt, sh["start"] + 0.2 + i * 0.12); S_ = sc * CH[who]["scale"]
        badge(fr, x, y - 236 * S_ - 70 * S_, str(i + 1), 1.0 * g * u, col)
        lzt(fr, x, y + (46 if vert else 40), NAME[who][0], int(50 * g * u), (255, 255, 255))
    lzt(fr, Wd / 2, Hd * (0.93 if vert else 0.95), "اكتب رقم الكداب", int(66 * g * popk(tt, sh["start"] + 0.6)), (255, 255, 255))
    return fr

def hook_text(fr, tt, Wd, Hd):
    if tt >= HOOK_END: return
    vert = Hd > Wd; a_ = int(255 * min(1, (HOOK_END - tt) / 0.3))
    lzt(fr, Wd / 2, Hd * (0.24 if vert else 0.2), "مين خد الطرد؟", int((116 if vert else 100) * popk(tt, 0.35, 0.3)), (255, 214, 90), alpha=a_)
def tag(fr, Wd, Hd, tt):
    if tt >= SEG0 or tt < HOOK_END: return
    d = ImageDraw.Draw(fr, "RGBA"); vert = Hd > Wd; x, y = (Wd / 2, 110) if vert else (Wd - 150, 60)
    d.rounded_rectangle([x - 110, y - 32, x + 110, y + 32], 26, fill=(200, 30, 40, 220)); lzt(fr, x, y, "قضية ١٤", 42, (255, 255, 255), stroke=False)

def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "c13": return finish(seg13(tt, W, H), tt)
    if sh["set"] == "q": return finish(q_card(tt, sh, W, H), tt)
    if sh["set"] == "cctv": fr = cctv(tt, sh, W, H)
    else: cam = hcam(sh, tt); fr = scene(tt, sh, cam, (W, H)); add_badges(fr, tt, sh, cam)
    hook_text(fr, tt, W, H); tag(fr, W, H, tt)
    return finish(fr, tt)
def VWHO(k): return WHO.get(k) if k else None
def subtitle(img, tt):
    if shot_at(tt)["set"] != "q": k, lt = line_at(tt); VN.sub_v(img, k, lt, CHV, VWHO(k), cy=H - 80, size=60)
VN.NAMES.update({w: NAME[w] for w in NAME})
VIGV = VIG.resize((1080, 1920))
def vertical(_base, tt):
    sh = shot_at(tt); Wd, Hd = 1080, 1920
    if sh["set"] == "c13": fr = seg13(tt, Wd, Hd)
    elif sh["set"] == "q": return q_card(tt, sh, Wd, Hd)
    elif sh["set"] == "cctv": fr = cctv(tt, sh, Wd, Hd)
    else:
        cam = vcam(sh, tt); fr = scene(tt, sh, cam, (Wd, Hd)); add_badges(fr, tt, sh, cam); fr = ImageChops.multiply(fr, VIGV)
        if sh.get("tin") == "whip" and tt - sh["start"] < 0.16: fr = fr.filter(ImageFilter.BoxBlur(int(2 + 16 * (1 - (tt - sh["start"]) / 0.16))))
        if sh.get("tin") == "fade" and tt - sh["start"] < 0.3: fr = Image.blend(Image.new("RGB", fr.size, (255, 240, 210)), fr, ease((tt - sh["start"]) / 0.3))
    if sh["set"] == "cctv" and sh.get("tin") == "flash" and tt - sh["start"] < 0.25: fr = Image.blend(fr, Image.new("RGB", fr.size, (255, 255, 255)), 0.8 * (1 - (tt - sh["start"]) / 0.25))
    hook_text(fr, tt, Wd, Hd); tag(fr, Wd, Hd, tt)
    k, lt = line_at(tt)
    cy = {"c13": 330, "cctv": 1260}.get(sh["set"], 560)
    VN.sub_v(fr, k, lt, CHV, VWHO(k), cy=cy, size=74)
    return fr

# ---------------- audio ----------------
def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def noise(dur, amp, seed=1): return (np.random.default_rng(seed).normal(0, 1, int(SR * dur)) * amp).astype(np.float32)
SFXF = {n: load_audio(ROOT + f"/trend/01/sfx/{n}.mp3") for n in ("whoosh", "stinger", "gasp")}
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 3; buf = np.zeros(n, dtype=np.float32)
    dr = np.arange(int(GL[0] * SR)) / SR                                                     # CCTV hum + fast-forward whirr
    mix_into(buf, (np.sin(2 * np.pi * 60 * dr) * 0.03 + np.sin(2 * np.pi * 1200 * dr * (1 + dr * 0.1)) * 0.012).astype(np.float32), 0.0, 1.0)
    mix_into(buf, SFXF["stinger"] * 0.3, 0.25, 1.0)
    mix_into(buf, lowpass(noise(GL[1] - GL[0], 0.25, 3), 5000), GL[0], 1.0)                 # glitch static
    mix_into(buf, tone(110, 0.8, 0.2, 3), GL[1], 1.0); mix_into(buf, tone(165, 0.8, 0.12, 3), GL[1], 1.0)   # DUN: empty bench
    mix_into(buf, tone(880, 0.25, 0.1, 8), A0 + 0.2, 1.0)
    for a_, b_ in (NANA_IN, Z_IN, GATHER):
        for j in range(int((b_ - a_) / 0.3)): mix_into(buf, tone(150, 0.07, 0.08, 30), a_ + j * 0.3, 1.0)       # footsteps
    mix_into(buf, SFXF["gasp"] * 0.25, NANA_IN[1] - 0.1, 1.0)
    mix_into(buf, SFXF["whoosh"] * 0.25, T("N1") + 0.8, 1.0); mix_into(buf, tone(90, 0.2, 0.35, 18), T("N1") + 0.92, 1.0)  # slipper swish + slap
    mix_into(buf, tone(1400, 0.08, 0.1, 20), CC2[0], 1.0); mix_into(buf, tone(1800, 0.08, 0.1, 20), CC2[0] + 0.1, 1.0)    # CCTV beep
    dr2 = np.arange(int((CC2[1] - CC2[0]) * SR)) / SR
    mix_into(buf, (np.sin(2 * np.pi * 1300 * dr2) * 0.01 + np.sin(2 * np.pi * 60 * dr2) * 0.03).astype(np.float32), CC2[0], 1.0)
    for who, (a_, b_) in FB.items():                                                         # flashback in/out: rewind swoosh
        mix_into(buf, SFXF["whoosh"][::-1].copy() * 0.2, a_ - 0.25, 1.0); mix_into(buf, SFXF["whoosh"] * 0.15, b_ - 0.1, 1.0)
        mix_into(buf, tone(523, 0.6, 0.05, 3), a_ + 0.05, 1.0)
    dr = np.arange(int((SEG0 - HOOK_END) * SR)) / SR
    mix_into(buf, ((np.sin(2 * np.pi * 55 * dr) * 0.035 + np.sin(2 * np.pi * 82.5 * dr) * 0.018)).astype(np.float32), HOOK_END, 1.0)
    for j in range(3): mix_into(buf, tone(60, 0.18, 0.3, 14), SUS[0] + 0.1 + j * 0.5, 1.0); mix_into(buf, tone(58, 0.15, 0.22, 14), SUS[0] + 0.28 + j * 0.5, 1.0)  # heartbeat
    for i in range(3): mix_into(buf, tone(660 + i * 165, 0.18, 0.14, 12), BADGES + i * 0.12, 1.0)
    for k_, f in enumerate((523, 659, 784)): mix_into(buf, tone(f, 0.4, 0.13, 7), SEG0 + 0.1 + k_ * 0.08, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.13, 6), Q + k_ * 0.09, 1.0)
    for s_ in shots:
        if s_.get("tin") == "whip": mix_into(buf, SFXF["whoosh"] * 0.14, s_["start"] - 0.1, 1.0)
    for st_, k in lines:
        a = AUD[k]; v = a / max(1e-6, np.percentile(np.abs(a), 99.5)) * 0.8; mix_into(buf, v, st_, 1.0)
    write_wav(buf[:int(TOTAL * SR)], path)

def make_covers():
    def comp(Wd, Hd, vert):
        fr = cctv(1.2, {"cc": "hook", "start": 0.0, "end": HOOK_END, "cover": True}, Wd, Hd)
        d0 = ImageDraw.Draw(fr); px, py = (PARCEL[0] * Wd / 540, (PARCEL[1] - 120) * Wd / 540 - 25) if vert else (PARCEL[0] * Wd / 900, (PARCEL[1] - 395) * Wd / 900 - 25); r0 = 130 if vert else 150
        d0.ellipse([px - r0, py - r0 * 0.75, px + r0, py + r0 * 0.75], outline=(255, 214, 60), width=12)
        img = fr.resize((int(Wd * SS), int(Hd * SS))); lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); p = P(lay)
        if vert: draw_char(p, "nana", Wd * 0.8, Hd * 0.66, 3.0, "angry", 0.6, -1, False, "up", 0.0, "slipper", 0.0, None)
        else: draw_char(p, "nana", Wd * 0.8, Hd * 1.12, 4.0, "angry", 0.6, -1, False, "up", 0.0, "slipper", 0.0, None)
        img.paste(lay, (0, 0), lay); fr = img.resize((Wd, Hd), Image.LANCZOS); d = ImageDraw.Draw(fr, "RGBA")
        if vert:
            d.rectangle([0, Hd * 0.67, Wd, Hd * 0.87], fill=(10, 6, 4, 180))
            lzt(fr, Wd / 2, Hd * 0.72, "مين خد", 160, (255, 255, 255)); lzt(fr, Wd / 2, Hd * 0.81, "الطرد؟", 170, (255, 214, 60))
            for i, (who, col) in enumerate(NUMS): badge(fr, Wd * (0.28 + 0.22 * i), Hd * 0.92, str(i + 1), 1.1, col)
            bx, by = Wd / 2, 140
        else:
            d.rectangle([0, Hd * 0.78, Wd, Hd * 0.97], fill=(10, 6, 4, 180)); lzt(fr, Wd * 0.42, Hd * 0.875, "مين خد الطرد؟", 150, (255, 214, 60)); bx, by = 1620, 150
        d = ImageDraw.Draw(fr, "RGBA"); d.rounded_rectangle([bx - 200, by - 46, bx + 200, by + 46], 34, fill=(200, 30, 40, 240))
        lzt(fr, bx, by, "مين الكداب؟ • قضية ١٤", 42, (255, 255, 255), stroke=False)
        return fr
    comp(1080, 1920, True).save(ROOT + "/publish/thumbs/kaddab_e14_cover.jpg", quality=92)
    comp(1920, 1080, False).resize((1280, 720), Image.LANCZOS).save(ROOT + "/publish/thumbs/kaddab_e14_yt.jpg", quality=92)

def contact_sheet(path="speaker_check.jpg"):
    tiles = []
    for st_, k in lines:
        for fr_ in (0.3, 0.8):
            tt = st_ + DUR[k] * fr_; v = vertical(None, tt).resize((270, 480)); h = frame(tt).copy(); subtitle(h, tt); h = h.resize((480, 270))
            tile = Image.new("RGB", (760, 520), (20, 20, 24)); tile.paste(v, (5, 35)); tile.paste(h, (275, 35))
            lzt(tile, 380, 18, f"{k} • {NAME[WHO[k]][0]} • {tt:.1f}s", 26, (255, 214, 90), stroke=False); tiles.append(tile)
    cols = 4; rows = -(-len(tiles) // cols); sheet = Image.new("RGB", (760 * cols, 520 * rows), (10, 10, 12))
    for i, t_ in enumerate(tiles): sheet.paste(t_, ((i % cols) * 760, (i // cols) * 520))
    sheet.save(path, quality=85)

if __name__ == "__main__":
    print("TOTAL", round(TOTAL, 1))
    if sys.argv[1:2] == ["stills"]: render(None, None, [float(v) for v in sys.argv[2:]])
    elif sys.argv[1:2] == ["times"]:
        for s_ in shots: print(s_["set"], round(s_["start"], 2), round(s_["end"], 2), s_.get("who", s_.get("cc", "")))
        for st, k in lines: print(k, round(st, 2), round(DUR[k], 2))
    elif sys.argv[1:2] == ["part"]:
        i, n = int(sys.argv[2]), int(sys.argv[3]); a = round(TOTAL * i / n * FPS) / FPS; b = round(TOTAL * (i + 1) / n * FPS) / FPS
        render(f"h_{i}.mp4", f"v_{i}.mp4", None, a, b)
    elif sys.argv[1:2] == ["audio"]: build_audio()
    elif sys.argv[1:2] == ["cover"]: make_covers()
    elif sys.argv[1:2] == ["sheet"]: contact_sheet()
