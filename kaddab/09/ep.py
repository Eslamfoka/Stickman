# «مين الكداب؟» — القضية 9: «مين طيّر البغبغان؟» (22/11, 20:00 Kuwait) — growth rules (native 9:16, phrase subs, speaker names, hook 3 s)
# Canonical Nana living room (lit). Nana's parrot cage hangs by the balcony door; the cage door is open, feathers float.
# HOOK: the parrot on the balcony rail squawks «يا نهار أبيض! يا نهار أبيض!» and flies off into the night.
# Clue (audio): a parrot only repeats what it hears OFTEN. Each suspect opens with a different exclamation:
#   عزيزة «يا لهوي!» · توتة «يا خبر!» · شطة «يا نهار أبيض!» (+ «عمري ما دخلت شقة طنط نعناعة») ; Nana herself says «يا مصيبتي!».
#   → the parrot learned Shatta's phrase → Shatta visits the flat a lot → he LIES.   ANSWER (end of case 10): شطة (3).
# Case-8 answer told here (A1, Tota): بندق — cake «68» → 1958 = the safe code + his signed card on the table.
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont, ImageChops
os.chdir(ROOT + "/kaddab/09")
SERIES = "مين الكداب؟"; EPT = "مين طيّر البغبغان؟"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"; RUQ = ROOT + "/brand/fonts/Cairo.ttf"; DJ = ROOT + "/brand/fonts/DejaVuSans-Bold.ttf"
SFXF = {n: load_audio(ROOT + f"/trend/01/sfx/{n}.mp3") for n in ("whoosh", "stinger", "gasp")}
SUB = {"PAR": "يا نهار أبيض! يا نهار أبيض!", "N1": "يا مصيبتي! البغبغان بتاعي طار! حد فتح القفص وأنا نايمة!",
       "Z1": "القفص ده ما بيتفتحش غير من برّه… يبقى حد دخل الشقة!", "AZ1": "يا لهوي! أنا من الصبح بنشر الغسيل فوق السطح!",
       "T1": "يا خبر! أنا لسه راجعة من المدرسة!", "S1": "يا نهار أبيض! أنا عمري ما دخلت شقة طنط نعناعة… ولا أعرف شكل البغبغان ده أصلًا!",
       "Z2": "البغبغان ما بيقولش غير الكلام اللي بيسمعه كتير… ركزوا في أول الحلقة! مين الكداب؟ اكتبوا في الكومنتات… والحل بكرة!",
       "A1": "حل الفزورة اللي فاتت: الكداب كان بندق! التورتة عليها 68… يعني طنط نعناعة مواليد 1958… وده رقم الخزنة! وكارت بندق كان على الترابيزة… يعني كان عندها النهارده!",
       "C1": "ولو ما شفتوش الحلقة اللي فاتت… شوفوها! وما تنسوش اللايك والفولو والشير!"}
CHUNKS = {"PAR": [(0.0, "يا نهار أبيض!", None), (2.1, "يا نهار أبيض!", None)],
          "N1": [(0.0, "يا مصيبتي!", None), (1.4, "البغبغان بتاعي طار!", "طار"), (3.5, "حد فتح القفص…", "فتح القفص"), (5.0, "وأنا نايمة!", None)],
          "Z1": [(0.0, "القفص ده ما بيتفتحش غير من برّه…", "من برّه"), (3.5, "يبقى حد دخل الشقة!", "دخل الشقة")],
          "AZ1": [(0.0, "يا لهوي!", None), (2.15, "أنا من الصبح…", None), (3.3, "بنشر الغسيل فوق السطح!", "السطح")],
          "T1": [(0.0, "يا خبر!", None), (1.2, "أنا لسه راجعة من المدرسة!", "المدرسة")],
          "S1": [(0.0, "يا نهار أبيض!", None), (1.45, "أنا عمري ما دخلت شقة طنط نعناعة…", "عمري ما دخلت"), (4.65, "ولا أعرف شكل البغبغان ده أصلًا!", "البغبغان")],
          "Z2": [(0.0, "البغبغان…", "البغبغان"), (1.45, "ما بيقولش غير الكلام اللي بيسمعه كتير…", "بيسمعه كتير"), (4.85, "ركزوا في أول الحلقة!", "أول الحلقة"),
                 (7.35, "مين الكداب؟", "مين الكداب؟"), (8.6, "اكتبوا في الكومنتات…", "الكومنتات"), (10.2, "والحل بكرة!", "بكرة")],
          "A1": [(0.0, "حل الفزورة اللي فاتت:", None), (2.25, "الكداب كان بندق!", "بندق"), (4.3, "التورتة عليها 68…", "68"),
                 (6.34, "يعني طنط نعناعة مواليد 1958…", "1958"), (10.2, "وده رقم الخزنة!", "رقم الخزنة"), (11.6, "وكارت بندق كان على الترابيزة…", "كارت بندق"),
                 (13.6, "يعني كان عندها النهارده!", "النهارده")],
          "C1": [(0.0, "ولو ما شفتوش الحلقة اللي فاتت…", None), (1.95, "شوفوها!", "شوفوها"), (2.8, "وما تنسوش اللايك والفولو والشير!", "الشير")]}
WHO = {"PAR": "parrot", "N1": "nana", "Z1": "zalata", "AZ1": "aziza", "T1": "tota", "S1": "shatta", "Z2": "zalata", "A1": "tota", "C1": "nana"}
NAME = {"parrot": ("البغبغان", (90, 200, 90)), "nana": ("نعناعة", (150, 140, 255)), "zalata": ("زلطة", (140, 210, 80)), "shatta": ("شطة", (255, 140, 80)),
        "aziza": ("عزيزة", (255, 110, 170)), "tota": ("توتة", (255, 130, 190)), "bondo2": ("بندق", (230, 170, 110))}
EXPR = {"PAR": "flat", "N1": [(0, "shout"), (0.45, "scared")], "Z1": "flat", "AZ1": "angry", "T1": "scared", "S1": "flat",
        "Z2": "smug", "A1": "happy", "C1": "happy"}
load_lines(list(SUB))
LIVING = _ld(ROOT + "/s1e1/bg/living_1080.png")                                 # canonical «الصالة» (docs/locations.md)
RLIT = ImageChops.multiply(ImageEnhance.Brightness(LIVING).enhance(1.55), Image.new("RGB", LIVING.size, (255, 236, 214)))
COVER8 = Image.open(ROOT + "/publish/thumbs/kaddab_e08_cover.jpg").convert("RGB")

# ---------------- staging (world = living room 1920x1080) ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
POS = {"zalata": (330, 1012, 1.6), "nana": (580, 1012, 1.6), "aziza": (1060, 1012, 1.6), "tota": (1300, 1012, 1.6), "shatta": (1560, 1012, 1.6)}
CAGE = (1290, 130)                                     # hook point; cage hangs below (by the balcony door)
RAIL = (1500, 560)                                     # parrot on the balcony rail in the hook
CARD = (668, 548); CAKE = (868, 566)                   # case-8 props (answer insert)
NUMS = (("aziza", (196, 40, 96)), ("tota", (230, 90, 150)), ("shatta", (230, 90, 40)))
def body(who, x, y, s):
    S = s * CH[who]["scale"]; sh = y - 134 * S; return S, sh, (x, sh - 56 * S)
def hand(who, x, y, s, arms, side):
    S, sh, _ = body(who, x, y, s)
    A = {"down": ((x - 34 * S, sh + 72 * S), (x + 34 * S, sh + 72 * S)), "talk": ((x - 50 * S, sh + 52 * S), (x + 60 * S, sh + 8 * S)),
         "hold": ((x - 36 * S, sh + 70 * S), (x + 46 * S, sh + 30 * S)), "up": ((x - 72 * S, sh - 52 * S), (x + 72 * S, sh - 52 * S))}
    return A.get(arms, A["down"])[0 if side < 0 else 1]

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
WIDE_H = (960, 640, 1.18)
say(0.15, "PAR"); P0 = T("PAR")
shot("room", 0.0, 1.35, (1290, 330, 3.0), (1300, 300, 3.4), ease="crash", v=((1290, 330, 3.2), (1300, 300, 3.6)))       # empty swinging cage, feathers
shot("room", 1.35, P0 + DUR["PAR"] + 0.2, (1480, 480, 3.0), (1500, 420, 2.6), tin="whip", v=((1490, 480, 3.1), (1500, 420, 2.8)))   # parrot on the rail → flies off
FLY = P0 + 2.6
t = P0 + DUR["PAR"] + 0.2
s = t; t = say(t + 0.05, "N1") + 0.1; shakes.append((s + 0.1, 14))
shot("room", s, t, (580, 700, 2.7), (580, 690, 2.95), tin="whipl", ease="crash", v=((580, 700, 2.9), (580, 690, 3.15)))
s = t; z1 = say(t + 0.05, "Z1"); Z1 = T("Z1")
shot("room", s, Z1 + 3.4, (900, 560, 1.5), (1180, 470, 1.9), tin="whip", v=((800, 560, 1.8), (1220, 450, 2.0)))       # Zalata walks to the cage with the lens
CAGE_CU = Z1 + 3.4; shot("room", CAGE_CU, z1 + 0.15, (1290, 290, 3.6), (1290, 285, 3.9), tin="zoom", v=((1290, 290, 3.8), (1290, 285, 4.1)))   # latch outside
LINEUP = z1 + 0.15; shot("room", LINEUP, LINEUP + 1.3, WIDE_H, (1100, 650, 1.25), tin="whipl", v=((1080, 620, 1.8), (1560, 620, 1.85)))
t = LINEUP + 1.3
for k_, who in (("AZ1", "aziza"), ("T1", "tota"), ("S1", "shatta")):
    s = t; t = say(t + 0.05, k_) + 0.1; x_ = POS[who][0]
    shot("room", s, t, (x_, 700, 2.7), (x_, 690, 2.95), tin="whip", v=((x_, 700, 2.9), (x_, 690, 3.15)))
ASK = t; z2 = say(t + 0.05, "Z2"); a = T("Z2")
shot("room", ASK, a + 4.85, (330, 700, 2.6), (330, 690, 2.8), tin="whipl", v=((330, 700, 2.8), (330, 690, 3.0)))      # «ما بيقولش غير الكلام اللي بيسمعه كتير»
FLASH = a + 4.85; shot("flash", FLASH, a + 7.35, (1490, 480, 3.0), (1500, 450, 3.2), tin="flash", v=((1490, 480, 3.1), (1500, 450, 3.3)))  # «ركزوا في أول الحلقة!» — flashback
shot("room", a + 7.35, a + 8.6, WIDE_H, (1060, 645, 1.24), tin="whip", v=((1080, 620, 1.8), (1560, 620, 1.85)))         # «مين الكداب؟» — badges
shot("room", a + 8.6, z2 + 0.3, (330, 700, 2.6), (330, 690, 2.75), tin="whip", v=((330, 700, 2.8), (330, 690, 2.95)))
t = z2 + 0.3
Q = t; shot("q", t, t + 1.4, None, v=None); t += 1.4
ANS = t; t = say(t + 0.25, "A1") + 0.35; shot("ans", ANS, t, None, tin="flash", v=None)
CTA = t; t = say(t + 0.15, "C1") + 1.4; shot("cta", CTA, t, None, tin="whip", v=None)
TOTAL = t

def hcam(sh, tt):
    """H camera (top-left form): z = output px per world unit"""
    return cam_at(sh, tt)
def vcam(sh, tt):
    c0, c1 = sh["v"]; k = ease((tt - sh["start"]) / max(0.01, sh["end"] - sh["start"]), sh.get("ease"))
    cx, cy, z = [a_ + (b_ - a_) * k for a_, b_ in zip(c0, c1)]; z = max(z, 1920 / 1080)
    shake = 0
    for st, amp in shakes:
        if 0 <= tt - st < 0.45: shake = max(shake, amp * (1 - (tt - st) / 0.45))
    cw, ch = 1080 / z, 1920 / z
    x0 = min(max(cx - cw / 2 + math.sin(tt * 0.9) * 3, 0), 1920 - cw); y0 = min(max(cy - ch / 2 + math.sin(tt * 1.3) * 2, 0), 1080 - ch)
    if shake: x0 = min(max(x0 + rng.normal(0, shake / z), 0), 1920 - cw); y0 = min(max(y0 + rng.normal(0, shake / z), 0), 1080 - ch)
    return x0, y0, z

# ---------------- helpers ----------------
def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255, font=None, rot=0, stroke=True):
    if size < 4: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(font or LZ, size)
    kw = dict(font=f, anchor="mm", direction="rtl", language="ar") if font is None else dict(font=f, anchor="mm")
    if stroke: d.text((x, y), s, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), **kw)
    d.text((x, y), s, fill=fill + (alpha,), **kw)
    if rot: lay = lay.rotate(rot, center=(x, y), resample=Image.BICUBIC)
    img.paste(lay, (0, 0), lay)
def popk(tt, t0, d=0.22):
    u = kk(tt, t0, t0 + d); return 0 if u <= 0 else (1 + 0.25 * math.sin(u * math.pi)) if u < 1 else 1
def badge(fr, x, y, n, sc, col):
    if sc <= 0: return
    d = ImageDraw.Draw(fr, "RGBA"); r = 46 * sc
    d.ellipse([x - r, y - r, x + r, y + r], fill=col + (255,), outline=(255, 255, 255, 255), width=max(1, int(6 * sc)))
    lzt(fr, x, y + 4 * sc, n, int(70 * sc), (255, 255, 255), font=DJ)

_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/kaddab/09")

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, held=None):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    blink = ((tt + len(who) * 0.37) % 3.6) < 0.11 and expr not in ("laugh", "scared", "shout")
    if not talking: lean += math.sin(tt * 1.7 + len(who)) * 0.04
    X, Y_ = W2S(cam, x, y); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, held, lean, None)

def hazelnut(d, cx, cy, r):
    d.ellipse([cx - r, cy - r * 0.95, cx + r, cy + r * 1.05], fill=(150, 92, 40), outline=(60, 34, 14), width=max(1, int(r / 6)))
    d.polygon([(cx - r * 0.95, cy - r * 0.15), (cx, cy - r * 1.35), (cx + r * 0.95, cy - r * 0.15)], fill=(110, 66, 28), outline=(60, 34, 14))
    d.line([(cx - r * 0.3, cy + r * 0.2), (cx - r * 0.1, cy + r * 0.7)], fill=(200, 140, 80), width=max(1, int(r / 5)))

def draw_table(img, d, Q, zz, tt):
    # birthday card (tent card): «كل سنة وإنتي طيبة يا طنط نعناعة» + a small hazelnut signature (= بندق)
    cx, cy = CARD; a = Q(cx - 58, cy - 46); b = Q(cx + 58, cy + 22)
    d.polygon([Q(cx - 58, cy + 22), Q(cx - 50, cy - 46), Q(cx + 50, cy - 46), Q(cx + 58, cy + 22)], fill=(250, 244, 226), outline=(60, 50, 40))
    d.rectangle([Q(cx - 50, cy - 46)[0], Q(cx - 50, cy - 46)[1], Q(cx + 50, cy - 40)[0], Q(cx + 50, cy - 40)[1]], fill=(220, 60, 80))
    if zz > 2.6:
        f = ImageFont.truetype(LZ, max(6, int(10.5 * zz)))
        d.text(Q(cx, cy - 25), "كل سنة وإنتي طيبة", font=f, fill=(170, 40, 60), anchor="mm", direction="rtl", language="ar")
        d.text(Q(cx, cy - 9), "يا طنط نعناعة", font=f, fill=(170, 40, 60), anchor="mm", direction="rtl", language="ar")
        h = Q(cx - 38, cy + 9); hazelnut(d, h[0], h[1], 5.5 * zz)
        sg = Q(cx - 2, cy + 8); fs = ImageFont.truetype(RUQ, max(6, int(17 * zz)))      # handwritten signature «بندق» (user 21/11)
        sl = Image.new("RGBA", (int(60 * zz), int(30 * zz)), (0, 0, 0, 0)); sd = ImageDraw.Draw(sl)
        sd.text((sl.size[0] / 2, sl.size[1] * 0.45), "بندق", font=fs, fill=(30, 40, 120, 255), anchor="mm", direction="rtl", language="ar")
        sd.line([(sl.size[0] * 0.12, sl.size[1] * 0.85), (sl.size[0] * 0.88, sl.size[1] * 0.72)], fill=(30, 40, 120, 255), width=max(1, int(1.2 * zz)))
        sl = sl.transform(sl.size, Image.AFFINE, (1, 0.35, -0.35 * sl.size[1] * 0.5, 0, 1, 0), resample=Image.BICUBIC).rotate(7, resample=Image.BICUBIC); img.paste(sl, (int(sg[0] - sl.size[0] / 2), int(sg[1] - sl.size[1] / 2)), sl)
        hh = Q(cx + 28, cy + 9); r = 4 * zz
        d.ellipse([hh[0] - r * 2, hh[1] - r, hh[0], hh[1] + r * 0.8], fill=(230, 60, 80)); d.ellipse([hh[0], hh[1] - r, hh[0] + r * 2, hh[1] + r * 0.8], fill=(230, 60, 80))
        d.polygon([(hh[0] - r * 2, hh[1]), (hh[0] + r * 2, hh[1]), (hh[0], hh[1] + r * 2)], fill=(230, 60, 80))
    # bouquet in front-left of the card
    fx_, fy_ = 742, 560
    for i, (dx, dy, col) in enumerate(((-10, -40, (230, 60, 90)), (6, -48, (250, 200, 60)), (16, -34, (240, 120, 160)), (-2, -30, (250, 250, 250)))):
        s0, s1 = Q(fx_, fy_), Q(fx_ + dx, fy_ + dy); d.line([s0, s1], fill=(60, 120, 50), width=max(1, int(2.5 * zz)))
        r = 7 * zz; d.ellipse([s1[0] - r, s1[1] - r, s1[0] + r, s1[1] + r], fill=col, outline=(90, 40, 40))
    p0, p1 = Q(fx_ - 12, fy_ - 8), Q(fx_ + 12, fy_ + 14); d.polygon([p0, (p1[0], p0[1]), (p1[0] - 4 * zz, p1[1]), (p0[0] + 4 * zz, p1[1])], fill=(240, 220, 200), outline=(120, 90, 70))
    # cake with number candles «68»
    cx, cy = CAKE; a = Q(cx - 46, cy - 34); b = Q(cx + 46, cy + 6)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=(250, 228, 236), outline=(120, 70, 80), width=max(1, int(1.5 * zz)))
    e0, e1 = Q(cx - 46, cy - 44), Q(cx + 46, cy - 24); d.ellipse([e0[0], e0[1], e1[0], e1[1]], fill=(255, 240, 246), outline=(120, 70, 80), width=max(1, int(1.5 * zz)))
    for i in range(7):
        q = Q(cx - 40 + i * 13, cy - 22); r = 3.2 * zz; d.ellipse([q[0] - r, q[1] - r, q[0] + r, q[1] + r], fill=(220, 70, 110))
    f = ImageFont.truetype(DJ, max(6, int(26 * zz)))
    for j, n in enumerate("68"):
        q = Q(cx - 13 + j * 26, cy - 50)
        d.text(q, n, font=f, fill=(90, 170, 240), anchor="mb", stroke_width=max(1, int(1.5 * zz)), stroke_fill=(30, 60, 110))
        fl = Q(cx - 13 + j * 26, cy - 82 + math.sin(tt * 13 + j) * 1.2); r = 3.5 * zz
        d.ellipse([fl[0] - r, fl[1] - r * 1.8, fl[0] + r, fl[1] + r], fill=(255, 200, 80))
        for i in range(3, 0, -1): rr = r * (1 + i); d.ellipse([fl[0] - rr, fl[1] - rr, fl[0] + rr, fl[1] + rr], fill=(255, 210, 120, 18))

def magnifier(p, x, y, s, ang=-0.7):
    """lens centered (x,y) in output px; s = output px per world unit"""
    r = 22 * s; hx, hy = x + math.cos(ang + math.pi) * -r * 1.0, y + math.sin(ang + math.pi) * -r * 1.0
    p.line([(x + math.cos(ang) * r, y - math.sin(ang) * r * -1), (x + math.cos(ang) * r * 2.3, y + math.sin(-ang) * -r * 2.3)], (110, 70, 36, 255), 6 * s)
    p.ell(x, y, r, r, (200, 230, 255, 70), (40, 40, 46, 255), 4 * s)

def sweat(d, cam, x, hy, S, tt, n=2):
    z = cam[2]
    for i in range(n):
        u = (tt * 0.9 + i * 0.5) % 1.0; q = W2S(cam, x + (-40 + 80 * i) * S, hy - 20 * S + u * 50 * S); r = 5 * S * z
        d.ellipse([q[0] - r, q[1] - r * 1.5, q[0] + r, q[1] + r * 1.5], fill=(190, 225, 255, int(230 * (1 - u))), outline=(60, 110, 170, int(255 * (1 - u))), width=2)


# ---------------- props ----------------
def cage_swing(tt): return math.sin(tt * 2.6) * 0.09 * (1.0 if tt < Q else 0.3) + 0.0
def draw_cage(d, Q_, zz, tt):
    hx, hy = CAGE; ang = cage_swing(tt); L = 60
    top = (hx + math.sin(ang) * L, hy + math.cos(ang) * L)
    d.line([Q_(hx, hy), Q_(*top)], fill=(40, 34, 28), width=max(1, int(2.5 * zz)))
    cx, cy0, w, h = top[0], top[1], 120, 150
    R = lambda dx, dy: Q_(cx + dx * math.cos(ang) - dy * math.sin(ang), cy0 + dx * math.sin(ang) + dy * math.cos(ang))
    d.chord([R(-w / 2, -30)[0], R(-w / 2, -30)[1], R(w / 2, 30)[0], R(w / 2, 30)[1]], 180, 360, fill=None, outline=(190, 150, 60), width=max(1, int(4 * zz)))
    for i in range(9):                                                     # bars
        x = -w / 2 + i * w / 8; d.line([R(x, 0 if abs(x) > w / 2 - 1 else -24 * (1 - (2 * x / w) ** 2) ** 0.5), R(x, h)], fill=(200, 160, 70), width=max(1, int(2.2 * zz)))
    d.line([R(-w / 2, h), R(w / 2, h)], fill=(160, 120, 50), width=max(1, int(6 * zz)))
    d.line([R(-w / 2, 0), R(w / 2, 0)], fill=(190, 150, 60), width=max(1, int(3 * zz)))
    d.line([R(-w / 2 + 8, h * 0.62), R(w / 2 - 8, h * 0.62)], fill=(120, 80, 40), width=max(1, int(4 * zz)))   # perch — EMPTY
    # open door (latch outside): swung out to the right
    d.polygon([R(w / 2, h * 0.35), R(w / 2 + 46, h * 0.28), R(w / 2 + 46, h * 0.9), R(w / 2, h * 0.95)], outline=(200, 160, 70))
    for j in range(4): d.line([R(w / 2 + 12 * j, h * 0.34 - j * 2), R(w / 2 + 12 * j, h * 0.93 - j * 1.5)], fill=(200, 160, 70), width=max(1, int(2 * zz)))
    lt = R(w / 2 + 2, h * 0.6); r = 5 * zz; d.ellipse([lt[0] - r, lt[1] - r, lt[0] + r, lt[1] + r], fill=(220, 180, 60), outline=(90, 60, 20))   # the latch (outside)
    # seed cup + a feather on the floor of the cage
    a_, b_ = R(-30, h - 18), R(-6, h - 2); d.rectangle([min(a_[0], b_[0]), min(a_[1], b_[1]), max(a_[0], b_[0]), max(a_[1], b_[1])], fill=(230, 220, 190))
def feathers(d, cam, tt):
    if tt > Q: return
    z = cam[2]
    for i in range(7):
        ph = ((tt * 0.25 + i / 7) % 1.0); x = CAGE[0] - 120 + i * 40 + math.sin(tt * 2 + i) * 25; y = CAGE[1] + 120 + ph * 760
        q = W2S(cam, x, y); r = 9 * z; a = int(230 * math.sin(ph * math.pi)); rot = math.sin(tt * 3 + i) * 0.8
        pts = [(q[0] + math.cos(rot + k * math.pi / 2) * r * (1.8 if k % 2 == 0 else 0.6), q[1] + math.sin(rot + k * math.pi / 2) * r * (1.8 if k % 2 == 0 else 0.6)) for k in range(4)]
        d.polygon(pts, fill=(80, 190, 90, a) if i % 3 else (240, 200, 60, a))
def parrot(p, x, y, s, tt, flap=0.0, open_=0.0):
    """small green parrot (output px), s = px per world unit"""
    p.ell(x, y, 26 * s, 34 * s, (70, 180, 80, 255), INK, 2.5 * s)                                 # body
    p.ell(x + 4 * s, y - 40 * s, 20 * s, 19 * s, (90, 200, 90, 255), INK, 2.5 * s)                  # head
    p.ell(x + 10 * s, y - 44 * s, 6 * s, 6 * s, (255, 255, 255, 255), INK, 1.5 * s); p.ell(x + 11 * s, y - 44 * s, 2.6 * s, 2.6 * s, INK, None)
    p.poly([(x + 20 * s, y - 42 * s), (x + 34 * s, y - 34 * s - open_ * 4 * s), (x + 22 * s, y - 30 * s)], (250, 190, 50, 255), INK, 1.5 * s)   # beak
    if open_ > 0.2: p.poly([(x + 21 * s, y - 32 * s), (x + 32 * s, y - 28 * s + open_ * 6 * s), (x + 21 * s, y - 27 * s)], (240, 170, 40, 255), INK, 1.2 * s)
    wy = -18 * s * flap
    p.poly([(x - 18 * s, y - 14 * s), (x - 46 * s, y - 2 * s + wy), (x - 14 * s, y + 18 * s)], (50, 150, 70, 255), INK, 2 * s)     # wing
    p.poly([(x - 8 * s, y + 28 * s), (x - 24 * s, y + 70 * s), (x + 4 * s, y + 32 * s)], (220, 60, 50, 255), INK, 2 * s)           # tail
    p.line([(x - 6 * s, y + 32 * s), (x - 8 * s, y + 42 * s)], INK, 2 * s); p.line([(x + 6 * s, y + 32 * s), (x + 8 * s, y + 42 * s)], INK, 2 * s)
def parrot_at(tt):
    """position on the rail; after FLY it flaps off up-right into the night"""
    if tt < FLY: return RAIL[0], RAIL[1] - 45, 0.0
    u = tt - FLY; return RAIL[0] + u * 380, RAIL[1] - 45 - u * 260, 1.0

def scene(tt, cam, size, flash=False):
    Wd, Hd = size; x0, y0, z = cam
    box = (x0, y0, x0 + Wd / z, y0 + Hd / z)
    img = RLIT.resize((int(Wd * SS), int(Hd * SS)), Image.BICUBIC, box=box)
    if z > 2.0: img = img.filter(ImageFilter.GaussianBlur(min(1.6, (z - 2.0) * 0.8)))
    zz = z * SS; QW = lambda x, y: ((x - x0) * zz, (y - y0) * zz)
    d = ImageDraw.Draw(img, "RGBA")
    # the balcony door is OPEN (night air), rail
    a_, b_ = QW(1420, 520), QW(1600, 528); d.rectangle([a_[0], a_[1], b_[0], b_[1]], fill=(40, 30, 24))
    for x in range(1430, 1600, 22): q0, q1 = QW(x, 528), QW(x, 640); d.line([q0, q1], fill=(40, 30, 24), width=max(1, int(3 * zz)))
    draw_cage(d, QW, zz, tt)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); p = P(lay)
    k, lt = line_at(tt)
    if tt < FLY + 1.2 or flash:                                                       # the parrot
        tt_p = tt if not flash else P0 + 0.2 + (tt - FLASH) * 0.8
        px, py, fl = parrot_at(tt_p); q = W2S(cam, px, py)
        talking = (k == "PAR") or flash
        op = 0.0
        if k == "PAR": op = float(ENV["PAR"][min(int(lt * FPS) + 2, len(ENV["PAR"]) - 1)])
        elif flash: op = abs(math.sin(tt * 12))
        flap = abs(math.sin(tt * 18)) if fl > 0 else (0.3 * abs(math.sin(tt * 9)) if talking else 0.0)
        parrot(p, q[0], q[1], z * 1.25, tt, flap, op)
    if not flash and tt >= P0 + DUR["PAR"]:
        nx, ny, ns = POS["nana"]; narms = "up" if (k == "N1" and lt < 1.2) else ("talk" if k == "N1" else "hips")
        person(lay, cam, "nana", nx, ny, ns, tt, "scared" if tt < LINEUP else "angry", 1 if tt < LINEUP else -1, narms)
        zx = zal_pos(tt); zy, zs = POS["zalata"][1], POS["zalata"][2]
        zarms = "talk" if k in ("Z1", "Z2") else "hold"
        walk = tt * 8 if Z1 - 0.2 < tt < Z1 + 2.8 else None
        lk = 1 if tt < LINEUP else 1
        X, Y_ = W2S(cam, zx, zy); S = zs * z
        talking = k in ("Z1", "Z2"); ex = expr_of(k, lt) if talking else ("flat" if tt < LINEUP else "smug")
        mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
        draw_char(p, "zalata", X, Y_, S, ex, mouth, lk, ((tt + 1.1) % 3.6) < 0.11, zarms, tt, None, 0.0, walk)
        hx, hy = hand("zalata", zx, zy, zs, zarms, lk); q = W2S(cam, hx, hy - 30 * zs); magnifier(p, q[0], q[1], zs * z * 0.9)
        if tt >= LINEUP - 0.5:
            person(lay, cam, "aziza", *POS["aziza"], tt, "angry", -1, "talk" if k == "AZ1" else "hips", held=None)
            person(lay, cam, "tota", *POS["tota"], tt, "scared", -1, "talk" if k == "T1" else "down")
            sx = POS["shatta"]; sarms = "talk" if k == "S1" else "hold"
            person(lay, cam, "shatta", *sx, tt, "flat", -1, sarms)
    lay = tint_layer(lay, (255, 238, 214)); img.paste(lay, (0, 0), lay)
    fr = img.resize((Wd, Hd), Image.LANCZOS)
    d = ImageDraw.Draw(fr, "RGBA")
    feathers(d, cam, tt)
    if flash:                                                                          # flashback look
        fr = ImageEnhance.Color(fr).enhance(0.25); fr = ImageChops.multiply(fr, Image.new("RGB", fr.size, (255, 230, 190)))
        d = ImageDraw.Draw(fr, "RGBA")
        for i in range(0, Hd, 6): d.line([(0, i), (Wd, i)], fill=(0, 0, 0, 22))
        px, py, _ = parrot_at(P0 + 0.2); q = W2S(cam, px, py - 110)
        k2 = popk(tt, FLASH + 0.3, 0.3)
        if False:
            bw, bh = 300 * k2 * (1.4 if Hd > Wd else 1), 90 * k2 * (1.4 if Hd > Wd else 1)
            bx = min(max(q[0], bw / 2 + 20), Wd - bw / 2 - 20); by = max(q[1], bh / 2 + 260 if Hd > Wd else bh / 2 + 20)
            d.rounded_rectangle([bx - bw / 2, by - bh / 2, bx + bw / 2, by + bh / 2], int(40 * k2), fill=(255, 255, 255, 240), outline=(20, 20, 20, 255), width=5)
            lzt(fr, bx, by, "يا نهار أبيض!", int(52 * k2 * (1.4 if Hd > Wd else 1)), (20, 20, 20), stroke=False)
        lzt(fr, Wd / 2, Hd * (0.2 if Hd > Wd else 0.1), "فلاش باك", 64, (255, 214, 90))
    return fr

def zal_pos(tt):
    k = ease(kk(tt, Z1 - 0.2, Z1 + 2.8)); return lerp(POS["zalata"][0], 1160, k) if tt < LINEUP - 0.4 else lerp(1160, POS["zalata"][0], ease(kk(tt, LINEUP - 0.4, LINEUP + 0.6)))

def rays(fr, Wd, Hd, c0, c1, tt, sign=1, cy=0.6):
    d = ImageDraw.Draw(fr, "RGBA")
    for i in range(18):
        a0 = i * 20 + sign * tt * 6; a_ = math.radians(a0); b = math.radians(a0 + 9); R = 3000
        d.polygon([(Wd / 2, Hd * cy), (Wd / 2 + R * math.cos(a_), Hd * cy + R * math.sin(a_)), (Wd / 2 + R * math.cos(b), Hd * cy + R * math.sin(b))], fill=c1 + (255,))


# ---------------- cards ----------------
def q_card(tt, sh, Wd, Hd, base):
    fr = ImageEnhance.Brightness(base).enhance(0.4).filter(ImageFilter.GaussianBlur(6)).convert("RGB")
    vert = Hd > Wd; cy = Hd * (0.3 if vert else 0.28); g = 1.25 if vert else 1.0
    lzt(fr, Wd / 2, cy, "مين طيّر البغبغان؟", int(100 * g * popk(tt, sh["start"] + 0.05, 0.3)), (255, 214, 90))
    lzt(fr, Wd / 2, cy + 140 * g, "اكتب رقم الكداب في الكومنتات!", int(62 * g * popk(tt, sh["start"] + 0.2, 0.3)), (255, 255, 255))
    for i, (_, col) in enumerate(NUMS): badge(fr, Wd / 2 + (i - 1) * 200 * g, cy + 320 * g, str(i + 1), 1.3 * g * popk(tt, sh["start"] + 0.35 + i * 0.15), col)
    lzt(fr, Wd / 2, cy + 480 * g, "الدليل بيتسمع… مش بيتشاف!", int(58 * g * popk(tt, sh["start"] + 0.8)), (255, 160, 120))
    return fr

def table_insert(tt, Wd, Hd, z):
    """the case-8 coffee table (cake «68» + Bandaq's card) at zoom z, centered on the table"""
    cx, cy = 770, 540; x0, y0 = cx - Wd / z / 2, cy - Hd / z / 2
    img = RLIT.resize((int(Wd * SS), int(Hd * SS)), Image.BICUBIC, box=(x0, y0, x0 + Wd / z, y0 + Hd / z)).filter(ImageFilter.GaussianBlur(1.2))
    zz = z * SS; QW = lambda x, y: ((x - x0) * zz, (y - y0) * zz); d = ImageDraw.Draw(img, "RGBA")
    draw_table(img, d, QW, zz, tt); return img.resize((Wd, Hd), Image.LANCZOS), (x0, y0, z)

def ans_card(tt, sh, Wd, Hd):
    """case-8 answer (Tota): Bandaq — cake «68» → 1958 = the code + his card on the table"""
    st = T("A1"); vert = Hd > Wd
    fr, cam = table_insert(tt, Wd, Hd, 3.0 if not vert else 3.4)
    fr = ImageEnhance.Brightness(fr).enhance(0.85)
    d = ImageDraw.Draw(fr, "RGBA")
    lzt(fr, Wd / 2, Hd * (0.17 if vert else 0.1), "حل القضية 8", int((96 if vert else 86) * popk(tt, sh["start"] + 0.15)), (255, 214, 90))
    def ring(wx, wy, r, t0, t1):
        if t0 <= tt < t1:
            q = W2S(cam, wx, wy); k = popk(tt, t0, 0.25); rr = r * cam[2] * k
            d.ellipse([q[0] - rr, q[1] - rr * 0.8, q[0] + rr, q[1] + rr * 0.8], outline=(255, 214, 60, 255), width=10)
    ring(CAKE[0], CAKE[1] - 30, 80, st + 4.3, st + 10.2)
    ring(CARD[0], CARD[1] - 10, 85, st + 11.6, st + 20)
    if tt >= st + 6.34:
        k = popk(tt, st + 6.34, 0.3); y0 = Hd * (0.64 if vert else 0.64)
        lzt(fr, Wd / 2, y0, "2026 − 68 = 1958", int((84 if vert else 78) * k), (255, 255, 255), font=DJ)
    if tt >= st + 10.2: lzt(fr, Wd / 2, Hd * (0.71 if vert else 0.76), "= رقم الخزنة!", int(80 * popk(tt, st + 10.2, 0.3)), (255, 214, 60))
    if tt >= st + 2.25:                                                                  # Bandaq pops in, caught
        lay = Image.new("RGBA", (int(Wd * SS), int(Hd * SS)), (0, 0, 0, 0)); p = P(lay)
        caught = popk(tt, st + 2.25, 0.3); bx, by, bs = ((Wd * 0.8, Hd * 0.6, 2.0) if vert else (Wd * 0.86, Hd + 60, 2.6))
        draw_char(p, "bondo2", bx, by + (1 - min(1, caught)) * 300, bs, "scared", 0.0, -1, ((tt + 0.3) % 3.4) < 0.1, "scared", tt, None, 0.0, None)
        L2 = lay.resize((Wd, Hd), Image.LANCZOS); fr.paste(L2, (0, 0), L2)
        if tt < st + 4.3: lzt(fr, bx, Hd * (0.3 if vert else 0.3), "الكداب!", int(120 * popk(tt, st + 2.25, 0.25)), (255, 255, 255), (170, 20, 20), rot=8)
    return fr

def cta_card(tt, sh, Wd, Hd):
    fr = Image.new("RGB", (Wd, Hd), (20, 12, 10)); rays(fr, Wd, Hd, None, (44, 24, 16), tt, -1, 0.5); vert = Hd > Wd
    st = T("C1"); k = popk(tt, sh["start"] + 0.15, 0.3)
    cxv, cyv, chh = (Wd * 0.5, Hd * 0.33, 760) if vert else (560, 480, 690)
    if k > 0:
        ch = int(chh * k); cw = int(ch * 1080 / 1920)
        cov = COVER8.resize((cw, ch), Image.LANCZOS)
        fr_c = Image.new("RGBA", (cw + 24, ch + 24), (255, 214, 90, 255)); fr_c.paste(cov, (12, 12))
        fr_c = fr_c.rotate(-4, expand=True, resample=Image.BICUBIC)
        fr.paste(fr_c, (int(cxv - fr_c.size[0] / 2), int(cyv - fr_c.size[1] / 2)), fr_c)
        lzt(fr, cxv, cyv - chh / 2 - 40 if vert else 72, "شوفوا القضية 8", int(70 * k), (255, 214, 90))
    for i, (lab, col, t0) in enumerate((("لايك", (230, 50, 70), 2.9), ("فولو", (40, 140, 230), 3.6), ("شير", (60, 170, 90), 4.3))):
        k2 = popk(tt, st + t0, 0.25)
        if k2 <= 0: continue
        cx, cy = ((Wd * 0.78 - i * Wd * 0.28, Hd * 0.66) if vert else (1380, 220 + i * 190)); sw_ = 150 if vert else 260
        d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([cx - sw_ * k2, cy - 70 * k2, cx + sw_ * k2, cy + 70 * k2], int(55 * k2), fill=col + (255,), outline=(255, 255, 255, 255), width=6)
        lzt(fr, cx, cy + 4, lab, int(76 * k2), (255, 255, 255), (20, 20, 20))
    if tt >= st + 4.8:
        y0 = Hd * (0.74 if vert else 0.86); k3 = popk(tt, st + 4.8, 0.3)
        lzt(fr, Wd / 2 if vert else 1380, y0, "الحل بكره…", int(84 * k3), (255, 214, 90))
        lzt(fr, Wd / 2 if vert else 1380, y0 + (95 if vert else 85), "تابع عشان ما يفوتكش!", int(64 * k3), (255, 255, 255))
    return fr

# ---------------- subtitles (phrase chunks + speaker name) ----------------
def sub_chunk(img, tt, cx, cy, size):
    k, lt = line_at(tt)
    if not k or k not in CHUNKS: return
    cur = None
    for off, txt, key in CHUNKS[k]:
        if lt >= off: cur = (off, txt, key)
    if cur is None: return
    off, txt, key = cur; sc = popk(lt, off, 0.15) if lt - off < 0.15 else 1
    f = ImageFont.truetype(LZ, max(6, int(size * sc)))
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    kw = dict(font=f, direction="rtl", language="ar", stroke_width=max(4, size // 10), stroke_fill=(10, 10, 10, 255))
    if key and key in txt:
        a_, b_ = txt.split(key, 1); parts = [(a_, (255, 255, 255)), (key, (255, 214, 60)), (b_, (255, 255, 255))]
    else: parts = [(txt, (255, 255, 255))]
    widths = [d.textlength(s, font=f, direction="rtl", language="ar") if s else 0 for s, _ in parts]
    maxw = img.size[0] * 0.88
    if sum(widths) > maxw:                                                          # never cut a long phrase: shrink to fit
        f = ImageFont.truetype(LZ, max(6, int(size * sc * maxw / sum(widths)))); kw["font"] = f
        widths = [d.textlength(s, font=f, direction="rtl", language="ar") if s else 0 for s, _ in parts]
    tot = sum(widths); x = cx + tot / 2
    for (s, col), w_ in zip(parts, widths):
        if s: d.text((x - w_, cy), s, fill=col + (255,), anchor="lm", **kw)
        x -= w_
    nm, ncol = NAME[WHO[k]]; fn = ImageFont.truetype(LZ, int(size * 0.62))           # growth rule 9: speaker name in his colour
    nw = d.textlength(nm, font=fn, direction="rtl", language="ar")
    nx = cx + tot / 2 - nw / 2 - 10; ny = cy - size * 0.95
    d.rounded_rectangle([nx - nw / 2 - 18, ny - size * 0.38, nx + nw / 2 + 18, ny + size * 0.38], int(size * 0.3), fill=ncol + (235,))
    d.text((nx, ny), nm, font=fn, fill=(20, 12, 8, 255), anchor="mm", direction="rtl", language="ar")
    img.paste(lay, (0, 0), lay)

def subtitle(img, tt): sub_chunk(img, tt, W / 2, H - 80, 62)

# ---------------- frames ----------------
HOOK = "مين طيّر البغبغان؟!"
_FREEZE = {}
def tag(fr, Wd, Hd, tt):
    if tt < 3.0 or tt >= Q: return
    d = ImageDraw.Draw(fr, "RGBA"); vert = Hd > Wd; x, y = (Wd / 2, 200) if vert else (Wd - 150, 60)
    d.rounded_rectangle([x - 110, y - 32, x + 110, y + 32], 26, fill=(200, 30, 40, 220)); lzt(fr, x, y, "قضية 9", 44, (255, 255, 255), stroke=False)

def add_overlays(fr, tt, sh, Wd, Hd, cam):
    if cam is None or sh["set"] != "room": return
    a_ = T("Z2")
    show = (LINEUP + 0.3 <= tt < T("AZ1")) or (a_ + 7.35 <= tt < a_ + 8.6)
    if show:
        t0 = LINEUP + 0.3 if tt < a_ else a_ + 7.35
        for i, (who, col) in enumerate(NUMS):
            x, y, s = POS[who]; S_, _, (_, hy2) = body(who, x, y, s); q = W2S(cam, x, hy2 - 46 * S_ - 40)
            pulse = 1 + (0.4 * math.sin(kk(tt, t0 + 0.3 + i * 0.25, t0 + 0.7 + i * 0.25) * math.pi))
            badge(fr, q[0], q[1], str(i + 1), min(1.15, cam[2] * 0.7) * popk(tt, t0 + i * 0.2) * pulse, col)
    if CAGE_CU <= tt < LINEUP:                                                         # «من برّه» — arrow at the latch
        ang = cage_swing(tt); q = W2S(cam, CAGE[0] + math.sin(ang) * 60 + 62, CAGE[1] + 60 + 90); k = popk(tt, CAGE_CU + 0.3, 0.3)
        if k > 0:
            d = ImageDraw.Draw(fr, "RGBA"); r = 34 * cam[2] * k
            d.ellipse([q[0] - r, q[1] - r, q[0] + r, q[1] + r], outline=(255, 214, 60, 255), width=8)
            lzt(fr, Wd / 2, Hd * (0.2 if Hd > Wd else 0.12), "الترباس من برّه!", int(70 * k), (255, 214, 90))

def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "q":
        if "h" not in _FREEZE: _FREEZE["h"] = scene(sh["start"] - 0.05, hcam(shots[shots.index(sh) - 1], sh["start"] - 0.05), (W, H))
        return finish(q_card(tt, sh, W, H, _FREEZE["h"]), tt)
    if sh["set"] == "ans": return finish(ans_card(tt, sh, W, H), tt)
    if sh["set"] == "cta": return finish(cta_card(tt, sh, W, H), tt)
    cam = hcam(sh, tt); fr = scene(tt, cam, (W, H), flash=sh["set"] == "flash")
    add_overlays(fr, tt, sh, W, H, cam)
    if tt < 3.0:
        a_ = int(255 * min(1, (3.0 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([W / 2 - 480, 40, W / 2 + 480, 150], 30, fill=(20, 12, 8, int(a_ * 0.8)))
        lzt(fr, W / 2, 95, HOOK, 72, (255, 214, 90), alpha=a_)
    tag(fr, W, H, tt)
    return finish(fr, tt)

VIGV = VIG.resize((1080, 1920))
def vertical(_base, tt):
    sh = shot_at(tt); Wd, Hd = 1080, 1920
    if sh["set"] == "q":
        if "v" not in _FREEZE: _FREEZE["v"] = scene(sh["start"] - 0.05, vcam(shots[shots.index(sh) - 1], sh["start"] - 0.05), (Wd, Hd))
        return q_card(tt, sh, Wd, Hd, _FREEZE["v"])
    if sh["set"] == "ans": fr = ans_card(tt, sh, Wd, Hd); sub_chunk(fr, tt, 520, 1560, 70); return fr
    if sh["set"] == "cta": fr = cta_card(tt, sh, Wd, Hd); sub_chunk(fr, tt, 520, 1480, 66); return fr
    cam = vcam(sh, tt); fr = scene(tt, cam, (Wd, Hd), flash=sh["set"] == "flash")
    add_overlays(fr, tt, sh, Wd, Hd, cam)
    fr = ImageChops.multiply(fr, VIGV)
    u = tt - sh["start"]
    if sh.get("tin") in ("whip", "whipl") and u < 0.18: fr = fr.filter(ImageFilter.BoxBlur(int(2 + 18 * (1 - u / 0.18))))
    if tt < 3.0:
        a_ = int(255 * min(1, (3.0 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([90, 230, 990, 470], 40, fill=(20, 12, 8, int(a_ * 0.75)))
        lzt(fr, 540, 300, "مين طيّر", 96, (255, 255, 255), alpha=a_); lzt(fr, 540, 405, "البغبغان؟!", 96, (255, 214, 90), alpha=a_)
    tag(fr, Wd, Hd, tt)
    sub_chunk(fr, tt, 500, 1470, 76)
    return fr

# ---------------- audio ----------------
def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def creak(dur=0.9, amp=0.25):
    n = int(SR * dur); t_ = np.arange(n) / SR; f = 180 + 90 * np.sin(t_ * 9) + 40 * np.sin(t_ * 31)
    x = np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * (0.5 + 0.5 * np.abs(np.sin(t_ * 47)))
    return (lowpass(x.astype(np.float32), 1600) * np.hanning(n) * amp).astype(np.float32)

def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 3; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(99)
    dr = np.arange(int(Q * SR)) / SR
    drone = (np.sin(2 * np.pi * 55 * dr) * 0.045 + np.sin(2 * np.pi * 82.5 * dr) * 0.025) * (0.7 + 0.3 * np.sin(dr * 0.8))
    mix_into(buf, drone.astype(np.float32), 0, 1.0)
    mix_into(buf, lowpass(r.normal(0, 1, int(Q * SR)).astype(np.float32), 500) * 0.02, 0, 1.0)            # night air from the balcony
    for j in range(int(Q / 1.0)): mix_into(buf, tone(2400, 0.03, 0.04, 80), 0.5 + j * 1.0, 1.0); mix_into(buf, tone(1900, 0.03, 0.03, 80), 1.0 + j * 1.0, 1.0)
    for j in range(8): mix_into(buf, tone(300 + 40 * (j % 3), 0.05, 0.06, 30), 0.05 + j * 0.16, 1.0)       # cage creak
    mix_into(buf, SFXF["stinger"] * 0.4, 0.05, 1.0)
    for j in range(10): mix_into(buf, lowpass((r.normal(0, 1, int(SR * 0.06)) * 0.25).astype(np.float32), 1500), FLY + j * 0.07, 1.0)  # wing flaps
    mix_into(buf, SFXF["gasp"] * 0.35, T("N1") - 0.1, 1.0)
    for j in range(int(2.8 / 0.33)): mix_into(buf, tone(110, 0.06, 0.12, 35), Z1 + j * 0.33, 1.0)
    mix_into(buf, tone(1200, 0.06, 0.18, 30), CAGE_CU + 0.3, 1.0)
    for i in range(3): mix_into(buf, tone(660 + i * 220, 0.18, 0.2, 12), LINEUP + 0.3 + i * 0.2, 1.0)
    mix_into(buf, tone(140, 0.7, 0.2, 3), T("S1") + 0.05, 1.0)
    a_ = T("Z2"); mix_into(buf, SFXF["stinger"] * 0.35, FLASH, 1.0)
    pq = AUD["PAR"] / max(1e-6, np.percentile(np.abs(AUD["PAR"]), 99.5)) * 0.35; mix_into(buf, pq[:int(SR * 1.5)], FLASH + 0.3, 1.0)   # flashback squawk (quiet)
    for i in range(3): mix_into(buf, tone(700 + i * 180, 0.2, 0.18, 10), a_ + 7.6 + i * 0.25, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), Q + k_ * 0.09, 1.0)
    st = T("A1"); mix_into(buf, tone(180, 0.5, 0.3, 4), st + 2.25, 1.0)
    for t0 in (4.3, 6.34, 10.2, 11.6): mix_into(buf, tone(988, 0.3, 0.14, 8), st + t0, 1.0)
    for i, t0 in enumerate((2.9, 3.6, 4.3)): mix_into(buf, tone(880 + i * 220, 0.2, 0.2, 10), T("C1") + t0, 1.0)
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 1.0: mix_into(buf, SFXF["whoosh"] * 0.2, s_["start"] - 0.1, 1.0)
    for st_, k in lines:
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8; mix_into(buf, v, st_, 1.0)
    write_wav(buf[:int(TOTAL * SR)], path)

def make_covers():
    def comp(Wd, Hd, vert):
        bgc = ImageEnhance.Brightness(RLIT.crop((900, 60, 1800, 900)).resize((Wd, Hd), Image.LANCZOS).filter(ImageFilter.GaussianBlur(7))).enhance(0.75)
        img = bgc.resize((int(Wd * SS), int(Hd * SS))); d = ImageDraw.Draw(img, "RGBA")
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); p = P(lay)
        if vert:
            draw_char(p, "nana", Wd * 0.33, Hd * 0.80, 4.6, "shock", 0.6, 1, False, "up", 0.0, None, 0.0, None)
            parrot(p, Wd * 0.77, Hd * 0.25, 4.2, 0, 0.6, 1.0)
            for i, (who, col) in enumerate(NUMS):
                draw_char(p, who, Wd * (0.2 + 0.3 * i), Hd * 1.08, 2.3, "flat", 0.0, -1, False, "down", 0.0, None, 0.0, None)
        else:
            draw_char(p, "nana", Wd * 0.3, Hd * 1.28, 5.4, "shock", 0.6, 1, False, "up", 0.0, None, 0.0, None)
            parrot(p, Wd * 0.75, Hd * 0.3, 5.0, 0, 0.6, 1.0)
        img.paste(lay, (0, 0), lay); fr = img.resize((Wd, Hd), Image.LANCZOS); d = ImageDraw.Draw(fr, "RGBA")
        if vert:
            d.rectangle([0, Hd * 0.535, Wd, Hd * 0.725], fill=(10, 6, 4, 150))
            lzt(fr, Wd / 2, Hd * 0.575, "مين طيّر", 150, (255, 255, 255)); lzt(fr, Wd / 2, Hd * 0.67, "البغبغان؟", 170, (255, 214, 60))
            for i, (who, col) in enumerate(NUMS): badge(fr, Wd * (0.2 + 0.3 * i), Hd * 0.765, str(i + 1), 1.2, col)
            bx, by = Wd * 0.3, 110
        else:
            lzt(fr, Wd * 0.62, Hd * 0.78, "مين طيّر البغبغان؟", 130, (255, 214, 60)); bx, by = 260, 90
        d = ImageDraw.Draw(fr, "RGBA"); d.rounded_rectangle([bx - 190, by - 46, bx + 190, by + 46], 34, fill=(200, 30, 40, 240))
        lzt(fr, bx, by, "مين الكداب؟ • قضية 9", 42, (255, 255, 255), stroke=False)
        return fr
    comp(1080, 1920, True).save(ROOT + "/publish/thumbs/kaddab_e09_cover.jpg", quality=92)
    comp(1920, 1080, False).resize((1280, 720), Image.LANCZOS).save(ROOT + "/publish/thumbs/kaddab_e09_yt.jpg", quality=92)

if __name__ == "__main__":
    print("TOTAL", round(TOTAL, 1))
    if sys.argv[1:2] == ["stills"]: render(None, None, [float(v) for v in sys.argv[2:]])
    elif sys.argv[1:2] == ["times"]:
        for s_ in shots: print(s_["set"], round(s_["start"], 2), round(s_["end"], 2), s_.get("tin", ""))
        for st, k in lines: print(k, round(st, 2))
    elif sys.argv[1:2] == ["part"]:
        i, n = int(sys.argv[2]), int(sys.argv[3]); a = round(TOTAL * i / n * FPS) / FPS; b = round(TOTAL * (i + 1) / n * FPS) / FPS
        render(f"h_{i}.mp4", f"v_{i}.mp4", None, a, b)
    elif sys.argv[1:2] == ["audio"]: build_audio()
    elif sys.argv[1:2] == ["cover"]: make_covers()
