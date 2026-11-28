# «مين الكداب؟» — «فانوس البواب» (28/11). Public number: قضية ١٥ (owner 17:17: previous = case 14 «الطرد»).
# Script approved by Eslam in chat 17:11 («النص تمام امشي عليه»); voices: one take each (gens.txt). T2 = new: case-14 answer (سوسن).
# Canonical places only: lobby s1e10/bg/morning.png (night grade) + stairwell s1e1/bg/stairs_1080.png (night grade). Fanous + shadow drawn by code.
# Structure: frame 1 = the lit fanous beside the sleeping doorman (motion + sound) → stairwell: a shadow climbs carrying the SAME fanous shape
#   (knotted tarha, swinging hoop, ladle) → lobby: the fanous is gone, the doorman wakes → everyone arrives (motivated: his shout) →
#   statements with badges 1 سوسن · 2 شطة · 3 عزيزة → silent push → «حل القضية ١٣» → final card (ONE ask).
# ANSWER (producer only, opens the next case): ③ عزيزة — she says she never climbed the stairs since Maghrib, but the shadow going up
#   with the fanous has her knotted tarha, big hoop earring and ladle (she holds the ladle in the line-up too).
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont, ImageChops, ImageOps
sys.path.insert(0, ROOT + "/s2"); import vnative as VN
os.chdir(ROOT + "/kaddab/15"); sys.path.insert(0, ROOT + "/kaddab/15"); import props as PR
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"; DJ = ROOT + "/brand/fonts/DejaVuSans-Bold.ttf"
TXT = {"H0": "بعد المغرب… العمارة ساكتة… بس فيه حد طالع السلم.", "B1": "الفانوس… راح فين؟! أنا صاحي أهو!",
       "T1": "فانوس عم البواب اختفى من على الدكة… كل واحد كان فين بعد المغرب؟",
       "W1": "أنا كنت لايف في شقتي من المغرب! الشات كله شاهد!", "S1": "وأنا كنت بذاكر مع زلطة… ثقوا فيا المرة دي!",
       "Z1": "صحيح… كان معايا.",
       "A1": "أنا ما طلعتش السلم خالص من المغرب، رجلي واجعاني! حتى العيش وصل لنعناعة بالبكرة!",
       "N1": "والعيش لقيته متعلّق على أوكرة باب شقتي… الحمد لله إن فيه حد فاكرني!",
       "T2": "إجابة القضية اللي فاتت: الكدابة كانت سوسن! قالت إنها شافت الدكة فاضية ستة وحداشر… بس الكاميرا صوّرت الطرد على الدكة لحد ستة واتناشر!",
       "T3": "الدليل قدامكم من أول الحلقة… مين الكداب؟ اكتب رقم الكداب!"}
KEYS = list(TXT)
WHO = {"H0": "tota", "B1": "bondo2", "T1": "tota", "W1": "sawsan", "S1": "shatta", "Z1": "zalata", "A1": "aziza", "N1": "nana", "T2": "tota", "T3": "tota"}
NAME = {"nana": ("نعناعة", (150, 220, 190)), "zalata": ("زلطة", (140, 220, 120)), "tota": ("توتة", (255, 130, 190)),
        "shatta": ("شطة", (255, 140, 80)), "sawsan": ("سوسن", (255, 170, 80)), "bondo2": ("البواب", (230, 170, 110)), "aziza": ("عزيزة", (230, 90, 140))}
EXPR = {"H0": "scared", "B1": [(0, "shock"), (0.55, "angry")], "T1": "neutral", "W1": [(0, "happy")], "S1": [(0, "happy"), (0.55, "scared")],
        "Z1": "neutral", "A1": [(0, "angry"), (0.6, "happy")], "N1": "happy", "T2": "smug", "T3": "smug"}
load_lines(KEYS)
CHV = {k: VN.chunk_times(TXT[k], ENV[k], FPS) for k in KEYS}
VN.set_font(LZ)

def tinted(img, lvl, tint): return ImageChops.multiply(ImageEnhance.Brightness(img).enhance(lvl), Image.new("RGB", img.size, tint))
LOB0 = _ld(ROOT + "/s1e10/bg/morning.png")
LOB = tinted(LOB0, 0.62, (160, 178, 240))                               # after Maghrib — night grade of the canonical lobby
STA0 = _ld(ROOT + "/s1e1/bg/stairs_1080.png")
STA = tinted(STA0, 0.52, (150, 170, 235))
CC = {(k, o): Image.open(f"c14/{k}_{o}.png").convert("RGB") for k in ("cam", "saw", "empty") for o in "hv"}
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
FEET = 1040
BENCH = (250, 655, 1.5)                 # doorman seated on the bench (hip on the seat)
FAN = (395, 600)                        # the fanous on the bench, beside him
STAIR_IN = (1400, 860, 1.2); AZ_DOOR = (1700, 905, 1.35)
POS = {"bondo2": (430, FEET, 1.55), "nana": (640, FEET, 1.5), "tota": (845, FEET, 1.4), "zalata": (1040, FEET, 1.55),
       "sawsan": (1240, FEET, 1.55), "shatta": (1440, FEET, 1.5), "aziza": (1650, FEET, 1.55)}
NUMS = (("sawsan", (150, 70, 190)), ("shatta", (210, 60, 40)), ("aziza", (200, 40, 110)))

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
say(0.25, "H0")
FAN_END = 1.7; HOOK_END = T("H0") + DUR["H0"] + 0.25
shot("lob", 0.0, FAN_END, (360, 560, 1.75), (370, 570, 1.95), v=((340, 600, 2.1), (350, 600, 2.3)), fan=True, sleep=True)
shot("stairs", FAN_END, HOOK_END, None, v=None)
A0 = HOOK_END; s = A0; t = say(s + 0.55, "B1") + 0.15; shakes.append((T("B1") + 0.1, 14))
shot("lob", s, t, (360, 580, 1.75), (360, 590, 1.95), v=((340, 620, 2.1), (340, 620, 2.3)), tin="whip", wake=True)
GATHER = (t, t + 2.4)                                                       # his shout brings everybody
shot("lob", t, GATHER[1], (1000, 600, 1.0), (980, 610, 1.05), v=((1300, 650, 1.85), (900, 650, 1.85)), tin="whip"); t = GATHER[1]
BADGES = None
def close(k, who, tin="whip"):
    global t
    s = t; t = say(t + 0.12, k) + 0.22; x_ = POS[who][0]
    shot("lob", s, t, (x_, 640, 1.85), (x_, 640, 1.98), v=((x_, 650, 2.3), (x_, 650, 2.42)), tin=tin)
close("T1", "tota")
BADGES = t - 0.3
shot("lob", t, t + 1.0, (1440, 630, 1.3), (1440, 630, 1.35), v=((1240, 650, 1.85), (1650, 650, 1.85))); t += 1.0
for k, who in (("W1", "sawsan"), ("S1", "shatta"), ("Z1", "zalata"), ("A1", "aziza"), ("N1", "nana")): close(k, who)
SUS = (t, t + 1.7)
shot("lob", t, SUS[1], (1440, 640, 1.25), (1440, 640, 1.4), v=((1240, 650, 1.85), (1650, 650, 1.85))); t = SUS[1]
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
def _shake(tt):
    sk = 0
    for st, amp in shakes:
        if 0 <= tt - st < 0.45: sk = max(sk, amp * (1 - (tt - st) / 0.45))
    return sk
def vcam(sh, tt):
    c0, c1 = sh["v"]; k = ease((tt - sh["start"]) / max(0.01, sh["end"] - sh["start"]))
    cx, cy, z = [a_ + (b_ - a_) * k for a_, b_ in zip(c0, c1)]; z = max(z, 1920 / 1080)
    cw, ch = 1080 / z, 1920 / z
    x0 = min(max(cx - cw / 2, 0), 1920 - cw); y0 = min(max(cy - ch / 2, 0), 1080 - ch); sk = _shake(tt)
    if sk: x0 = min(max(x0 + rng.normal(0, sk / z), 0), 1920 - cw)
    return x0, y0, z
def hcam(sh, tt):
    c0, c1 = sh["c0"], sh["c1"]; k = ease((tt - sh["start"]) / max(0.01, sh["end"] - sh["start"]))
    cx, cy, z = [a_ + (b_ - a_) * k for a_, b_ in zip(c0, c1)]
    cw, ch = 1920 / z, 1080 / z
    x0 = min(max(cx - cw / 2, 0), 1920 - cw); y0 = min(max(cy - ch / 2, 0), 1080 - ch); sk = _shake(tt)
    if sk: x0 = min(max(x0 + rng.normal(0, sk / z), 0), 1920 - cw)
    return x0, y0, z

# ---------------- who is where ----------------
def walker(p0, p1, win, tt, rate=8):
    u = ease(kk(tt, *win)); return lerp(p0[0], p1[0], u), lerp(p0[1], p1[1], u), lerp(p0[2], p1[2], u), (tt * rate if 0 < kk(tt, *win) < 1 else None)
def cast_at(sh, tt):
    """[(who, x, y, s, look, arms, held, walk, sit)]"""
    C = []
    if sh["set"] != "lob": return C
    if tt < GATHER[0] + 0.2:
        C.append(("bondo2", BENCH[0], BENCH[1], BENCH[2], 1, "down", None, None, 1))
    else:
        x, y, s, w = walker((BENCH[0] + 60, FEET - 20, 1.5), POS["bondo2"], (GATHER[0] + 0.2, GATHER[0] + 1.3), tt, 9)
        C.append(("bondo2", x, y, s, 1 if w else 1, "down", None, w, 0))
    if tt >= GATHER[0]:
        g = GATHER[0]
        for i, who in enumerate(("tota", "zalata", "sawsan", "shatta", "nana")):
            x, y, s, w = walker(STAIR_IN, POS[who], (g + 0.15 * i, g + 1.2 + 0.2 * i), tt, 9)
            held = {"sawsan": "phone", "zalata": "nbpen", "nana": None, "tota": None, "shatta": None}[who]
            C.append((who, x, y, s, -1, "hold" if held else "down", held, w, 0))
        x, y, s, w = walker(AZ_DOOR, POS["aziza"], (g + 0.3, g + 1.6), tt, 9)
        C.append(("aziza", x, y, s, -1, "hold", "ladle", w, 0))
    C.sort(key=lambda c: c[2])
    return C

def draw_cast(lay, cam, sh, tt):
    k, lt = line_at(tt)
    for who, x, y, s, look, arms, held, walk, sit in cast_at(sh, tt):
        talking = k is not None and WHO.get(k) == who and sh["set"] == "lob"
        if talking: e = expr_of(k, lt)
        elif who == "bondo2" and tt < T("B1"): e = "sleepy"
        elif who in ("sawsan", "shatta", "aziza") and BADGES and tt >= BADGES: e = "scared" if WHO.get(k) in ("sawsan", "shatta", "aziza") else "neutral"
        elif who == "tota": e = "smug"
        else: e = "neutral"
        mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
        a = arms
        if talking and arms == "down": a = "talk"
        if who == "bondo2" and k == "B1": a = "up"
        X, Y_ = W2S(cam, x, y); S = s * cam[2]
        lk = look
        if walk is None and k and WHO.get(k) != who and BADGES and tt >= BADGES:
            sp = POS.get(WHO.get(k)); lk = (1 if sp and sp[0] > x else -1) if sp else look
        nod = 0.0
        if who == "bondo2" and tt < T("B1"): nod = 0.6 + 0.4 * math.sin(tt * 2.2)
        draw_char(P(lay), who, X, Y_, S, e, mouth, lk, ((tt + len(who) * 0.37) % 3.6) < 0.11 and e != "sleepy", a, tt, held, 0.0, walk, None, sit, nod)

def scene(tt, sh, cam, size):
    Wd, Hd = size; x0, y0, z = cam
    img = LOB.resize((int(Wd * SS), int(Hd * SS)), Image.BICUBIC, box=(x0, y0, x0 + Wd / z, y0 + Hd / z))
    if sh.get("fan"):                                                     # the lit fanous on the bench (world coords → screen)
        q = W2S(cam, *FAN); PR.fanous(img, q[0] * SS, q[1] * SS, 0.55 * z * SS, 1.0)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); draw_cast(lay, cam, sh, tt)
    lay = tint_layer(lay, (226, 230, 255)); img.paste(lay, (0, 0), lay)
    fr = img.resize((Wd, Hd), Image.LANCZOS)
    if sh.get("wake"):                                                    # empty place on the bench: a faint ring in the dust
        q = W2S(cam, FAN[0], FAN[1] + 40); d = ImageDraw.Draw(fr, "RGBA"); r = 30 * z
        d.ellipse([q[0] - r, q[1] - r * 0.35, q[0] + r, q[1] + r * 0.35], outline=(220, 200, 150, 150), width=max(2, int(3 * z)))
    return fr

def stairs_world(tt, sh):
    u = kk(tt, sh["start"], sh["end"])
    x = lerp(1330, 1620, u); y = lerp(820, 600, u)                          # the shadow climbs the wall along the flight
    L = PR.shadow_layer((1920, 1080), x, y, 1.15, tt - sh["start"], 232)
    return PR.cast_shadow(STA.copy(), L, glow=(x + 180, y - 120, 560)), x
def stairs(tt, sh, Wd, Hd):
    img, x = stairs_world(tt, sh)
    if Wd > Hd: fr = img.resize((Wd, Hd), Image.LANCZOS)
    else:
        cw = 1080 * 9 / 16; x0 = min(max(x - cw / 2 + 60, 0), 1920 - cw); fr = img.crop((int(x0), 0, int(x0 + cw), 1080)).resize((Wd, Hd), Image.LANCZOS)
    return ImageChops.multiply(fr, VIG.resize(fr.size))

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
os.chdir(ROOT + "/kaddab/15")
def add_badges(fr, tt, sh, cam):
    if sh["set"] != "lob" or not BADGES or tt < BADGES: return
    Wd, Hd = fr.size
    for i, (who, col) in enumerate(NUMS):
        x, y, s = POS[who]; S_ = s * CH[who]["scale"]; q = W2S(cam, x, y - 236 * S_ - 60 * S_)
        if -100 < q[0] < Wd + 100: badge(fr, q[0], max(q[1], 120 if Hd < Wd else 300), str(i + 1), min(1.15, cam[2] * 0.55) * popk(tt, BADGES + i * 0.12), col)

def seg13(tt, Wd, Hd):                                                     # «حل القضية ١٤» (kept the name: shot set "c13")
    vert = Hd > Wd; o = "v" if vert else "h"; lt = tt - T("T2"); ch = CHV["T2"]
    idx = max([i for i, (off, _) in enumerate(ch) if lt >= off] or [0])
    txt = ch[idx][1] if lt >= 0 else ""
    key = "cam" if any(w in txt for w in ("الكاميرا", "الطرد", "واتناشر", "لحد")) else "saw"
    fr = CC[(key, o)].copy(); u = lt - (ch[idx][0] if lt >= 0 else 0)
    sc = 1 + 0.06 * min(1, max(0, u) / 2.5)
    fr = fr.resize((int(Wd * sc), int(Hd * sc)), Image.BICUBIC).crop((int(Wd * (sc - 1) / 2), int(Hd * (sc - 1) / 2), int(Wd * (sc - 1) / 2) + Wd, int(Hd * (sc - 1) / 2) + Hd))
    fr = ImageEnhance.Brightness(fr).enhance(0.92); d = ImageDraw.Draw(fr, "RGBA")
    if key == "cam" and lt > 0:                                            # circle the parcel + the 06:11 timestamp
        cx, cy = (Wd * 0.585, Hd * 0.53) if vert else (Wd * 0.355, Hd * 0.47); r = (110 if vert else 120) * popk(u, 0.1)
        d.ellipse([cx - r, cy - r * 0.7, cx + r, cy + r * 0.7], outline=(255, 214, 60), width=10)
    by = Hd * (0.06 if vert else 0.07); bh = 120 if vert else 100
    d.rectangle([0, by - bh / 2, Wd, by + bh / 2], fill=(30, 120, 60, 255)); lzt(fr, Wd / 2, by, "حل القضية ١٤", 78 if vert else 70, (255, 255, 255), (10, 40, 20))
    return fr
def q_card(tt, sh, Wd, Hd):
    vert = Hd > Wd; fr = Image.new("RGB", (Wd, Hd), (40, 12, 14)); d = ImageDraw.Draw(fr, "RGBA")
    for i in range(18):
        a0 = math.radians(i * 20 + tt * 6); b = a0 + math.radians(9); R = 3000
        d.polygon([(Wd / 2, Hd * 0.5), (Wd / 2 + R * math.cos(a0), Hd * 0.5 + R * math.sin(a0)), (Wd / 2 + R * math.cos(b), Hd * 0.5 + R * math.sin(b))], fill=(58, 18, 20))
    g = 1.25 if vert else 1.0; cy = Hd * 0.15
    d.rounded_rectangle([Wd / 2 - 210 * g, cy - 150 * g, Wd / 2 + 210 * g, cy - 70 * g], 30, fill=(200, 30, 40, 240))
    lzt(fr, Wd / 2, cy - 110 * g, "قضية ١٥", int(56 * g), (255, 255, 255), stroke=False)
    lzt(fr, Wd / 2, cy + 10 * g, "مين الكداب؟", int(120 * g * popk(tt, sh["start"] + 0.05, 0.3)), (255, 214, 90))
    lay = Image.new("RGBA", (int(Wd * SS), int(Hd * SS)), (0, 0, 0, 0)); p = P(lay)
    pos = [(Wd * 0.3, Hd * 0.5), (Wd * 0.7, Hd * 0.5), (Wd * 0.5, Hd * 0.8)] if vert else [(Wd * (0.25 + 0.25 * j), Hd * 0.78) for j in range(3)]
    sc = 1.4 if vert else 1.6
    for (who, col), (x, y) in zip(NUMS, pos):
        if popk(tt, sh["start"] + 0.2) > 0: draw_char(p, who, x, y, sc, "neutral", 0.0, 1, False, "hold" if who != "shatta" else "down", tt, {"sawsan": "phone", "aziza": "ladle"}.get(who), 0.0, None)
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
    lzt(fr, Wd / 2, Hd * (0.13 if vert else 0.12), "مين خد الفانوس؟", int((116 if vert else 100) * popk(tt, 0.3, 0.3)), (255, 214, 90), alpha=a_)
def tag(fr, Wd, Hd, tt):
    if tt >= SEG0 or tt < HOOK_END: return
    d = ImageDraw.Draw(fr, "RGBA"); vert = Hd > Wd; x, y = (Wd / 2, 110) if vert else (Wd - 150, 60)
    d.rounded_rectangle([x - 110, y - 32, x + 110, y + 32], 26, fill=(200, 30, 40, 220)); lzt(fr, x, y, "قضية ١٥", 42, (255, 255, 255), stroke=False)

def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "c13": return finish(seg13(tt, W, H), tt)
    if sh["set"] == "q": return finish(q_card(tt, sh, W, H), tt)
    if sh["set"] == "stairs": fr = stairs(tt, sh, W, H)
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
    elif sh["set"] == "stairs": fr = stairs(tt, sh, Wd, Hd)
    else:
        cam = vcam(sh, tt); fr = scene(tt, sh, cam, (Wd, Hd)); add_badges(fr, tt, sh, cam); fr = ImageChops.multiply(fr, VIGV)
        if sh.get("tin") == "whip" and tt - sh["start"] < 0.16: fr = fr.filter(ImageFilter.BoxBlur(int(2 + 16 * (1 - (tt - sh["start"]) / 0.16))))
    hook_text(fr, tt, Wd, Hd); tag(fr, Wd, Hd, tt)
    k, lt = line_at(tt)
    cy = {"c13": 330}.get(sh["set"], 1500 if (sh["set"] == "stairs" or sh.get("fan") or sh.get("wake")) else 560)
    VN.sub_v(fr, k, lt, CHV, VWHO(k), cy=cy, size=74)
    return fr

# ---------------- audio ----------------
def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def noise(dur, amp, seed=1): return (np.random.default_rng(seed).normal(0, 1, int(SR * dur)) * amp).astype(np.float32)
SFXF = {n: load_audio(ROOT + f"/trend/01/sfx/{n}.mp3") for n in ("whoosh", "stinger", "gasp")}
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 3; buf = np.zeros(n, dtype=np.float32)
    dr = np.arange(int(SEG0 * SR)) / SR                                                     # night drone under the case
    mix_into(buf, ((np.sin(2 * np.pi * 55 * dr) * 0.03 + np.sin(2 * np.pi * 82.5 * dr) * 0.015)).astype(np.float32), 0.0, 1.0)
    for j in range(int(FAN_END / 0.9) + 1): mix_into(buf, lowpass(noise(0.5, 0.05, 10 + j), 2500), j * 0.9, 1.0)       # snoring breath
    mix_into(buf, SFXF["stinger"] * 0.28, FAN_END, 1.0)
    for j in range(int((HOOK_END - FAN_END) / 0.42)): mix_into(buf, tone(140, 0.08, 0.1, 30), FAN_END + 0.15 + j * 0.42, 1.0)   # slow steps up
    mix_into(buf, tone(110, 0.8, 0.2, 3), HOOK_END, 1.0); mix_into(buf, tone(165, 0.8, 0.12, 3), HOOK_END, 1.0)                # DUN: the fanous is gone
    mix_into(buf, SFXF["gasp"] * 0.25, T("B1") - 0.15, 1.0)
    for j in range(int((GATHER[1] - GATHER[0]) / 0.25)): mix_into(buf, tone(150, 0.07, 0.07, 30), GATHER[0] + j * 0.25, 1.0)
    for j in range(3): mix_into(buf, tone(60, 0.18, 0.3, 14), SUS[0] + 0.1 + j * 0.5, 1.0); mix_into(buf, tone(58, 0.15, 0.22, 14), SUS[0] + 0.28 + j * 0.5, 1.0)
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
        sh = {"start": FAN_END, "end": HOOK_END}; fr = stairs(FAN_END + 1.6, sh, Wd, Hd)
        d = ImageDraw.Draw(fr, "RGBA")
        if vert:
            d.rectangle([0, Hd * 0.68, Wd, Hd * 0.88], fill=(10, 6, 4, 180))
            lzt(fr, Wd / 2, Hd * 0.73, "مين خد", 160, (255, 255, 255)); lzt(fr, Wd / 2, Hd * 0.82, "الفانوس؟", 170, (255, 214, 60))
            for i, (who, col) in enumerate(NUMS): badge(fr, Wd * (0.28 + 0.22 * i), Hd * 0.93, str(i + 1), 1.1, col)
            bx, by = Wd / 2, 140
        else:
            d.rectangle([0, Hd * 0.78, Wd, Hd * 0.97], fill=(10, 6, 4, 180)); lzt(fr, Wd * 0.42, Hd * 0.875, "مين خد الفانوس؟", 150, (255, 214, 60)); bx, by = 1620, 150
        d = ImageDraw.Draw(fr, "RGBA"); d.rounded_rectangle([bx - 200, by - 46, bx + 200, by + 46], 34, fill=(200, 30, 40, 240))
        lzt(fr, bx, by, "مين الكداب؟ • قضية ١٥", 42, (255, 255, 255), stroke=False)
        return fr
    os.makedirs(ROOT + "/publish/thumbs", exist_ok=True)
    comp(1080, 1920, True).save(ROOT + "/publish/thumbs/kaddab_fanoos_cover.jpg", quality=92)
    comp(1920, 1080, False).resize((1280, 720), Image.LANCZOS).save(ROOT + "/publish/thumbs/kaddab_fanoos_yt.jpg", quality=92)

if __name__ == "__main__":
    print("TOTAL", round(TOTAL, 1))
    if sys.argv[1:2] == ["stills"]: render(None, None, [float(v) for v in sys.argv[2:]])
    elif sys.argv[1:2] == ["times"]:
        for s_ in shots: print(s_["set"], round(s_["start"], 2), round(s_["end"], 2))
        for st, k in lines: print(k, round(st, 2), round(DUR[k], 2))
    elif sys.argv[1:2] == ["part"]:
        i, n = int(sys.argv[2]), int(sys.argv[3]); a = round(TOTAL * i / n * FPS) / FPS; b = round(TOTAL * (i + 1) / n * FPS) / FPS
        render(f"h_{i}.mp4", f"v_{i}.mp4", None, a, b)
    elif sys.argv[1:2] == ["audio"]: build_audio()
    elif sys.argv[1:2] == ["cover"]: make_covers()
