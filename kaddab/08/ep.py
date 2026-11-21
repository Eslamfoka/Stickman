# «مين الكداب؟» — القضية 8: «خزنة نعناعة»  (growth rules: native 9:16, phrase subtitles + yellow key word, hook 3 s, speaker names)
# Canonical Nana living room (s1e1/bg/living_1080.png = loc("living")), lights off in the hook, then the lamp comes on.
# HOOK: dark room, a small safe on the left cabinet swings open by itself — EMPTY — red LED blinking.
# Clue (2 steps): code = 1 9 5 8 (dust on every key except these). On the coffee table: a birthday cake with candles «68»
#   (2026 − 68 = 1958 → the code is Nana's birth year) + a birthday card signed «بندق» (small handwritten signature + a hazelnut doodle).
#   Bandaq says «ما شفتش طنط نعناعة النهارده خالص» — but his birthday card is on her table today → he LIES.
#   Red herrings: Shatta «مش بعرف في الأرقام», Aziza's market basket.
# ANSWER (say it at the END of case 9): بندق (3).   Case-7 answer told here (A1, Tota): نعناعة — dry umbrella.
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont, ImageChops
os.chdir(ROOT + "/kaddab/08")
SERIES = "مين الكداب؟"; EPT = "خزنة نعناعة"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"; RUQ = ROOT + "/brand/fonts/Cairo.ttf"; DJ = ROOT + "/brand/fonts/DejaVuSans-Bold.ttf"
SFXF = {n: load_audio(ROOT + f"/trend/01/sfx/{n}.mp3") for n in ("whoosh", "stinger", "gasp", "switch")}

SUB = {"N1": "فلوسي اختفت… والرقم محدش يعرفه غيري!", "Z1": "الخزنة ما اتكسرتش… يبقى الحرامي كان عارف الرقم.",
       "S1": "أنا ما بعرفش في الخزن والأرقام دي خالص!", "AZ1": "أنا كنت في السوق من الصبح… اسألوا البياع!",
       "B1": "أنا من الصبح في الكشك… وما شفتش طنط نعناعة النهارده خالص!",
       "Z2": "الرقم: 1 و 9 و 5 و 8… وواحد فيهم كان عارفه. مين؟ اكتبوا في الكومنتات… والحل بكرة!",
       "A1": "والحل بتاع الفزورة اللي فاتت: الكدابة كانت نعناعة! الشمسية كانت ناشفة… يعني هي أصلًا كانت جوه العمارة!",
       "C1": "ولو ما شفتوش الحلقة اللي فاتت… شوفوها! وما تنسوش اللايك والفولو والشير!"}
CHUNKS = {"N1": [(0.0, "فلوسي اختفت…", "اختفت"), (1.55, "والرقم محدش يعرفه غيري!", "غيري")],
          "Z1": [(0.0, "الخزنة ما اتكسرتش…", "ما اتكسرتش"), (2.55, "يبقى الحرامي كان عارف الرقم!", "عارف الرقم")],
          "S1": [(0.0, "أنا ما بعرفش في الخزن…", None), (1.45, "والأرقام دي خالص!", "الأرقام")],
          "AZ1": [(0.0, "أنا كنت في السوق من الصبح…", "السوق"), (1.78, "اسألوا البياع!", "البياع")],
          "B1": [(0.0, "أنا من الصبح في الكشك…", "الكشك"), (1.9, "وما شفتش طنط نعناعة النهارده!", "النهارده")],
          "Z2": [(0.0, "الرقم: 1 - 9 - 5 - 8", "1 - 9 - 5 - 8"), (3.5, "وواحد فيهم كان عارفه…", "كان عارفه"), (5.5, "مين؟", "مين؟"),
                 (6.25, "اكتبوا في الكومنتات…", "الكومنتات"), (7.65, "والحل بكرة!", "بكرة")],
          "A1": [(0.0, "حل الفزورة اللي فاتت:", None), (1.95, "الكدابة كانت نعناعة!", "نعناعة"), (4.45, "الشمسية كانت ناشفة…", "ناشفة"),
                 (6.15, "يعني كانت جوه العمارة!", "جوه")],
          "C1": [(0.0, "ولو ما شفتوش الحلقة اللي فاتت…", None), (1.95, "شوفوها!", "شوفوها"), (2.8, "وما تنسوش اللايك والفولو والشير!", "الشير")]}
WHO = {"N1": "nana", "Z1": "zalata", "S1": "shatta", "AZ1": "aziza", "B1": "bondo2", "Z2": "zalata", "A1": "tota", "C1": "nana"}
NAME = {"nana": ("نعناعة", (150, 140, 255)), "zalata": ("زلطة", (140, 210, 80)), "shatta": ("شطة", (255, 140, 80)),
        "aziza": ("عزيزة", (255, 110, 170)), "bondo2": ("بندق", (230, 170, 110)), "tota": ("توتة", (255, 130, 190))}
EXPR = {"N1": [(0, "shout"), (0.4, "scared")], "Z1": "flat", "S1": "scared", "AZ1": "angry", "B1": [(0, "scared"), (0.4, "smug")],
        "Z2": "smug", "A1": "happy", "C1": "happy"}
load_lines(list(SUB))
LIVING = _ld(ROOT + "/s1e1/bg/living_1080.png")                                  # canonical «الصالة» (docs/locations.md)
RLIT = ImageChops.multiply(ImageEnhance.Brightness(LIVING).enhance(1.55), Image.new("RGB", LIVING.size, (255, 236, 214)))
RDARK = ImageChops.multiply(ImageEnhance.Brightness(LIVING).enhance(0.55), Image.new("RGB", LIVING.size, (150, 165, 215)))
COVER7 = Image.open(ROOT + "/publish/thumbs/kaddab_e07_cover.jpg").convert("RGB")

# ---------------- staging (world = living room 1920x1080) ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
POS = {"zalata": (330, 1012, 1.6), "nana": (560, 1012, 1.6), "shatta": (1120, 1012, 1.6), "aziza": (1360, 1012, 1.6),
       "bondo2": (1600, 1012, 1.6)}
SAFE = (60, 222, 236, 372)                                                      # small safe on the left cabinet (world box)
CARD = (668, 548); CAKE = (868, 566)                                            # on the coffee table
NUMS = (("shatta", (230, 90, 40)), ("aziza", (196, 40, 96)), ("bondo2", (150, 96, 50)))
def body(who, x, y, s):
    S = s * CH[who]["scale"]; sh = y - 134 * S; return S, sh, (x, sh - 56 * S)
def hand(who, x, y, s, arms, side):
    S, sh, _ = body(who, x, y, s)
    A = {"down": ((x - 34 * S, sh + 72 * S), (x + 34 * S, sh + 72 * S)), "talk": ((x - 50 * S, sh + 52 * S), (x + 60 * S, sh + 8 * S)),
         "hold": ((x - 36 * S, sh + 70 * S), (x + 46 * S, sh + 30 * S)), "up": ((x - 72 * S, sh - 52 * S), (x + 72 * S, sh - 52 * S)),
         "hips": ((x - 48 * S, sh + 40 * S), (x + 48 * S, sh + 40 * S)), "point": ((x - 36 * S, sh + 70 * S), (x + 84 * S, sh - 10 * S))}
    return A.get(arms, A["down"])[0 if side < 0 else 1]

# ---------------- timeline (H camera = center form; v = vertical camera center form) ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
WIDE_H = (960, 640, 1.18)
HOOK_END = 1.45
shot("room", 0.0, HOOK_END, (150, 330, 2.6), (148, 300, 3.6), ease="crash", v=((150, 330, 2.6), (148, 300, 3.9)))      # the safe swings open, dark
LIGHT = HOOK_END                                                                # click — the lamp comes on
t = say(LIGHT + 0.25, "N1"); shakes.append((LIGHT + 0.3, 14))
shot("room", LIGHT, t + 0.1, (560, 700, 2.7), (560, 690, 2.95), tin="whipl", ease="crash", v=((560, 700, 2.9), (560, 690, 3.15)))   # Nana screams
PASS = t + 0.1; PASS_E = PASS + 1.7
shot("room", PASS, PASS_E, (640, 560, 3.2), (900, 565, 3.3), tin="whip", v=((660, 560, 3.3), (900, 565, 3.4)))        # pass over the table (card, cake, flowers) — no stop
z1 = say(PASS_E + 0.05, "Z1"); Z1 = T("Z1")
shot("room", PASS_E, Z1 + 2.5, (420, 600, 1.45), (300, 505, 1.68), tin="whip", v=((360, 560, 1.78), (280, 520, 1.9)))     # Zalata walks the lens to the safe
KEY1 = Z1 + 2.5; shot("keypad", KEY1, z1 + 0.15, None, tin="zoom")                                                  # insert: the keypad
LINEUP = z1 + 0.15; shot("room", LINEUP, LINEUP + 1.3, WIDE_H, (1060, 650, 1.25), tin="whipl", v=((1100, 620, 1.8), (1600, 620, 1.85)))
t = LINEUP + 1.3
s = t; t = say(t + 0.05, "S1") + 0.1; shot("room", s, t, (1120, 700, 2.7), (1120, 690, 2.9), tin="whip", v=((1120, 700, 2.9), (1120, 690, 3.1)))
s = t; t = say(t + 0.05, "AZ1") + 0.1; shot("room", s, t, (1360, 700, 2.7), (1360, 690, 2.9), tin="whip", v=((1360, 700, 2.9), (1360, 690, 3.1)))
s = t; t = say(t + 0.05, "B1") + 0.15; B1 = T("B1")
shot("room", s, B1 + 1.9, (1600, 700, 2.6), (1600, 690, 2.8), tin="whip", v=((1600, 700, 2.8), (1600, 690, 3.0)))
shot("room", B1 + 1.9, t, (1600, 640, 3.1), (1600, 630, 3.5), ease="crash", v=((1600, 640, 3.4), (1600, 630, 3.8)))  # «ما شفتش…» push-in, sweat
ASK = t; z2 = say(t + 0.05, "Z2"); a = T("Z2")
shot("keypad", ASK, a + 3.3, None, tin="whipl")                                                                       # «1 9 5 8» light up one by one
shot("room", a + 3.3, a + 5.4, WIDE_H, (980, 645, 1.24), tin="whip", v=((1100, 620, 1.8), (1600, 620, 1.85)))         # «وواحد فيهم كان عارفه» — badges
shot("room", a + 5.4, a + 6.2, (330, 700, 2.6), (330, 690, 3.0), tin="whipl", ease="crash", v=((330, 700, 2.8), (330, 690, 3.2)))  # «مين؟»
REPRISE = a + 6.2; shot("room", REPRISE, a + 7.65, (560, 560, 2.2), (900, 565, 2.5), tin="zoom", v=((620, 560, 2.4), (880, 565, 2.7)))  # lens over the table
shot("room", a + 7.65, z2 + 0.3, (330, 700, 2.6), (330, 690, 2.75), tin="whip", v=((330, 700, 2.8), (330, 690, 2.95)))
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
os.chdir(ROOT + "/kaddab/08")

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, held=None):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    blink = ((tt + len(who) * 0.37) % 3.6) < 0.11 and expr not in ("laugh", "scared", "shout")
    if not talking: lean += math.sin(tt * 1.7 + len(who)) * 0.04
    X, Y_ = W2S(cam, x, y); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, held, lean, None)

# ---------------- props (drawn on the supersampled canvas: Q() = world → SS px) ----------------
def safe_open(tt):
    return ease(kk(tt, 0.35, 1.25)) if tt < 30 else 1.0
def draw_safe(d, Q, zz, tt, dark):
    x0, y0, x1, y1 = SAFE; a = Q(x0, y0); b = Q(x1, y1); w_ = max(1, int(3 * zz))
    d.rectangle([a[0], a[1], b[0], b[1]], fill=(70, 74, 80), outline=(20, 20, 22), width=w_)
    ia, ib = Q(x0 + 12, y0 + 12), Q(x1 - 12, y1 - 12)
    d.rectangle([ia[0], ia[1], ib[0], ib[1]], fill=(14, 14, 16), outline=(40, 40, 44), width=w_)               # EMPTY inside
    sa, sb = Q(x0 + 12, y0 + 78), Q(x1 - 12, y0 + 84); d.rectangle([sa[0], sa[1], sb[0], sb[1]], fill=(50, 50, 56))   # shelf
    for i in range(3):                                                                                       # a few loose coins / rubber band
        c = Q(x0 + 40 + i * 30, y1 - 22); r = 4 * zz; d.ellipse([c[0] - r, c[1] - r * 0.5, c[0] + r, c[1] + r * 0.5], fill=(170, 140, 60) if i != 1 else (180, 60, 50))
    k = safe_open(tt); hw = (x1 - x0)                                               # door hinged on the LEFT, swings toward camera-left
    dw = hw * (1 - 0.86 * k)
    pts = [Q(x0, y0), Q(x0 - dw * 0.0 + dw * (1 - k) * 0 + (dw if k < 0.02 else dw), y0 - 6 * k), Q(x0 + (dw if k < 0.02 else dw), y1 + 6 * k), Q(x0, y1)]
    pts = [Q(x0, y0), Q(x0 + dw, y0 - 10 * k), Q(x0 + dw, y1 + 10 * k), Q(x0, y1)] if k < 0.5 else \
          [Q(x0, y0), Q(x0 - dw * 0.9, y0 - 14 * k), Q(x0 - dw * 0.9, y1 + 14 * k), Q(x0, y1)]
    d.polygon(pts, fill=(96, 100, 108), outline=(20, 20, 22))
    if k < 0.5:                                                                                               # keypad + handle on the closed door
        kp = Q(x0 + dw * 0.55, y0 + 60); d.rectangle([kp[0] - 18 * zz * (dw / hw), kp[1] - 26 * zz, kp[0] + 18 * zz * (dw / hw), kp[1] + 26 * zz], fill=(40, 42, 46))
    led = Q(x1 - 22, y0 + 22) if k < 0.5 else Q(x0 - (hw * 0.12) * 0.5, y0 + 20)
    on = (tt * 2.2) % 1 < 0.5; r = 5 * zz
    if on:
        for i in range(5, 0, -1): rr = r * (1 + i * 0.9); d.ellipse([led[0] - rr, led[1] - rr, led[0] + rr, led[1] + rr], fill=(255, 30, 30, int(22 if not dark else 40)))
    d.ellipse([led[0] - r, led[1] - r, led[0] + r, led[1] + r], fill=(255, 40, 40) if on else (90, 20, 20))

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

# ---------------- the room ----------------
def zal_pos(tt):
    """Zalata walks from the doorway side to the safe with his lens during Z1"""
    k = ease(kk(tt, PASS_E - 0.2, Z1 + 1.6)); return lerp(-160, POS["zalata"][0], k)

def scene(tt, cam, size):
    Wd, Hd = size; x0, y0, z = cam; dark = tt < LIGHT
    src = RDARK if dark else RLIT
    if LIGHT <= tt < LIGHT + 0.12: src = Image.blend(RDARK, RLIT, 0.4)                    # lamp flicker
    box = (x0, y0, x0 + Wd / z, y0 + Hd / z)
    img = src.resize((int(Wd * SS), int(Hd * SS)), Image.BICUBIC, box=box)
    if z > 2.0: img = img.filter(ImageFilter.GaussianBlur(min(1.6, (z - 2.0) * 0.8)))
    zz = z * SS; QW = lambda x, y: ((x - x0) * zz, (y - y0) * zz)
    d = ImageDraw.Draw(img, "RGBA")
    draw_safe(d, QW, zz, tt, dark); draw_table(img, d, QW, zz, tt)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); p = P(lay)
    k, lt = line_at(tt)
    if not dark:
        # Nana: in shock by the safe side
        nx, ny, ns = POS["nana"]; narms = "up" if (k == "N1" and lt < 1.5) else ("talk" if k == "N1" else ("scared" if tt < LINEUP else "hips"))
        person(lay, cam, "nana", nx, ny, ns, tt, "scared" if tt < LINEUP else "angry", -1, narms)
        # Zalata with the lens
        zx = zal_pos(tt); zy, zs = POS["zalata"][1], POS["zalata"][2]
        zarms = "talk" if k in ("Z1", "Z2") else "hold"
        walk = tt * 8 if PASS_E - 0.2 < tt < Z1 + 1.6 else None
        lk = -1 if tt < LINEUP else 1
        X, Y_ = W2S(cam, zx, zy); S = zs * z
        talking = k in ("Z1", "Z2"); ex = expr_of(k, lt) if talking else ("flat" if tt < LINEUP else "smug")
        mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
        draw_char(p, "zalata", X, Y_, S, ex, mouth, lk, ((tt + 1.1) % 3.6) < 0.11, zarms, tt, None, 0.0, walk)
        hx, hy = hand("zalata", zx, zy, zs, zarms, lk); q = W2S(cam, hx, hy - 30 * zs); magnifier(p, q[0], q[1], zs * z * 0.9)
        # the 3 suspects
        sarms = "talk" if k == "S1" else ("scared" if tt < T("S1") else "down")
        person(lay, cam, "shatta", *POS["shatta"], tt, "scared" if tt < T("AZ1") else "flat", -1, sarms)
        aarms = "talk" if k == "AZ1" else "hold"
        person(lay, cam, "aziza", *POS["aziza"], tt, "angry", -1, aarms, held="basket")
        barms = "talk" if k == "B1" else "hold"
        bex = "scared" if (B1 + 1.9 <= tt < ASK) else "flat"
        person(lay, cam, "bondo2", *POS["bondo2"], tt, bex, -1, barms)
    lay = tint_layer(lay, (255, 238, 214)); img.paste(lay, (0, 0), lay)
    fr = img.resize((Wd, Hd), Image.LANCZOS)
    d = ImageDraw.Draw(fr, "RGBA")
    if not dark:
        S_b, sh_b, (bhx, bhy) = body("bondo2", *POS["bondo2"])
        if B1 + 1.9 <= tt < Q: sweat(d, cam, bhx, bhy, S_b, tt, 3)
    if dark:                                                                       # red LED washes the dark room
        on = (tt * 2.2) % 1 < 0.5
        if on: fr = Image.blend(fr, ImageChops.multiply(fr, Image.new("RGB", fr.size, (255, 150, 150))), 0.35)
    return fr

# ---------------- the keypad insert ----------------
KEYS = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]
CLEAN = {"1", "9", "5", "8"}
_KP = {}
def keypad_base(Wd, Hd):
    if (Wd, Hd) in _KP: return _KP[(Wd, Hd)]
    Wb, Hb = int(Wd * 1.15), int(Hd * 1.15); im = Image.new("RGB", (Wb, Hb), (78, 82, 90)); d = ImageDraw.Draw(im)
    r = np.random.default_rng(8)
    a = np.asarray(im, np.float32) + r.normal(0, 7, (Hb, Wb, 1)); im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)); d = ImageDraw.Draw(im)
    u = min(Wb / 3.6, Hb / 6.0); cx, cy = Wb / 2, Hb / 2 + u * 0.55
    if Hb > Wb: u = Hb / 11; cy = Hb / 2 - 20
    d.rounded_rectangle([cx - u * 1.75, cy - u * 2.55, cx + u * 1.75, cy + u * 2.25], int(u * 0.2), fill=(32, 34, 38), outline=(16, 16, 18), width=int(u * 0.05))
    f = ImageFont.truetype(DJ, int(u * 0.42)); pos = {}
    for i, row in enumerate(KEYS):
        for j, kch in enumerate(row):
            x = cx + (j - 1) * u * 1.08; y = cy + (i - 1.5) * u * 1.08 + u * 0.1; h = u * 0.46
            clean = kch in CLEAN
            d.rounded_rectangle([x - h, y - h, x + h, y + h], int(h * 0.3), fill=(205, 208, 214) if clean else (150, 146, 136), outline=(20, 20, 20), width=int(u * 0.03))
            d.text((x, y), kch, font=f, fill=(30, 30, 34) if clean else (96, 92, 84), anchor="mm")
            if clean:                                                                 # shiny highlight
                d.rounded_rectangle([x - h * 0.8, y - h * 0.85, x + h * 0.2, y - h * 0.6], int(h * 0.15), fill=(245, 246, 250))
            else:                                                                     # dust specks
                for _ in range(90):
                    px, py = x + r.uniform(-h, h), y + r.uniform(-h, h); s_ = r.uniform(0.6, 2.2) * u / 120
                    d.ellipse([px - s_, py - s_, px + s_, py + s_], fill=(196, 190, 172))
            pos[kch] = (x, y, h)
    for _ in range(1400):                                                             # dust on the panel
        px, py = r.uniform(cx - u * 1.7, cx + u * 1.7), r.uniform(cy - u * 2.5, cy + u * 2.2); s_ = r.uniform(0.5, 1.8) * u / 120
        d.ellipse([px - s_, py - s_, px + s_, py + s_], fill=(120, 118, 110))
    _KP[(Wd, Hd)] = (im, pos, (cx, cy - u * 2.2, u)); return _KP[(Wd, Hd)]

def keypad(tt, sh, Wd, Hd):
    im, pos, (lx, ly, u) = keypad_base(Wd, Hd)
    k = (tt - sh["start"]) / max(0.01, sh["end"] - sh["start"]); sc = 1.0 + 0.06 * k
    Wb, Hb = im.size; cw, ch = Wd / sc, Hd / sc
    ox = (Wb - cw) / 2 + math.sin(tt * 0.9) * 6; oy = (Hb - ch) / 2 + math.sin(tt * 1.3) * 4
    fr = im.resize((Wd, Hd), Image.BICUBIC, box=(ox, oy, ox + cw, oy + ch)).convert("RGB")
    M = lambda x, y: ((x - ox) * sc, (y - oy) * sc)
    d = ImageDraw.Draw(fr, "RGBA")
    on = (tt * 2.2) % 1 < 0.5; q = M(lx + u * 1.2, ly - u * 0.05); r = u * 0.09 * sc
    if on:
        for i in range(6, 0, -1): rr = r * (1 + i * 0.8); d.ellipse([q[0] - rr, q[1] - rr, q[0] + rr, q[1] + rr], fill=(255, 30, 30, 26))
    d.ellipse([q[0] - r, q[1] - r, q[0] + r, q[1] + r], fill=(255, 40, 40) if on else (90, 20, 20))
    lzt(fr, M(lx - u * 0.4, ly)[0], M(lx, ly)[1], "LOCKED" if False else "• • • •", int(u * 0.3 * sc), (120, 255, 140), (10, 30, 10), font=DJ)
    in_z2 = tt >= ASK
    if in_z2:                                                                         # Z2: 1 9 5 8 glow one by one as he says them
        a_ = T("Z2"); times = (0.75, 1.35, 1.95, 2.5)
        for kch, t0 in zip("1958", times):
            if tt >= a_ + t0:
                x, y, h = pos[kch]; c = M(x, y); hh = h * sc * popk(tt, a_ + t0, 0.25)
                d.rounded_rectangle([c[0] - hh - 8, c[1] - hh - 8, c[0] + hh + 8, c[1] + hh + 8], int(hh * 0.35), outline=(255, 214, 60, 255), width=max(4, int(u * 0.06)))
        n = sum(1 for t0 in times if tt >= a_ + t0)
        lzt(fr, Wd / 2, Hd * (0.2 if Hd > Wd else 0.1), "1958"[:n] if n else "", int(min(u * 0.75, Hd * 0.09)), (255, 214, 60), font=DJ)
    else:                                                                             # Z1: the lens glides over the keys
        st = sh["start"]; u2 = ease(kk(tt, st + 0.2, sh["end"] - 0.2))
        path = [pos["1"], pos["5"], pos["9"], pos["8"]]; seg = min(2.999, u2 * 3); i = int(seg); f_ = seg - i
        x = lerp(path[i][0], path[i + 1][0], f_); y = lerp(path[i][1], path[i + 1][1], f_); c = M(x, y); R = u * 0.75 * sc
        src = fr.resize((int(Wd * 1.6), int(Hd * 1.6)), Image.LANCZOS)
        crop = src.crop((int(c[0] * 1.6 - R), int(c[1] * 1.6 - R), int(c[0] * 1.6 + R), int(c[1] * 1.6 + R)))
        mask = Image.new("L", crop.size, 0); ImageDraw.Draw(mask).ellipse([0, 0, crop.size[0] - 1, crop.size[1] - 1], fill=255)
        fr.paste(crop, (int(c[0] - R), int(c[1] - R)), mask); d = ImageDraw.Draw(fr, "RGBA")
        d.ellipse([c[0] - R - 8, c[1] - R - 8, c[0] + R + 8, c[1] + R + 8], outline=(40, 40, 46), width=int(u * 0.12))
        d.line([(c[0] + R * 0.72, c[1] + R * 0.72), (c[0] + R * 1.6, c[1] + R * 1.6)], fill=(110, 70, 36), width=int(u * 0.25))
        if tt >= st + 1.4: lzt(fr, Wd / 2, Hd * (0.2 if Hd > Wd else 0.09), "4 أزرار بس من غير تراب!", int(min(u * 0.36, Wd * 0.068) * popk(tt, st + 1.4, 0.3)), (255, 214, 60))
    return fr

# ---------------- cards ----------------
def q_card(tt, sh, Wd, Hd, base):
    fr = ImageEnhance.Brightness(base).enhance(0.4).filter(ImageFilter.GaussianBlur(6)).convert("RGB")
    vert = Hd > Wd; cy = Hd * (0.3 if vert else 0.28); g = 1.25 if vert else 1.0
    lzt(fr, Wd / 2, cy, "مين فتح الخزنة؟", int(110 * g * popk(tt, sh["start"] + 0.05, 0.3)), (255, 214, 90))
    lzt(fr, Wd / 2, cy + 140 * g, "اكتب رقم الكداب في الكومنتات!", int(62 * g * popk(tt, sh["start"] + 0.2, 0.3)), (255, 255, 255))
    for i, (_, col) in enumerate(NUMS): badge(fr, Wd / 2 + (i - 1) * 200 * g, cy + 320 * g, str(i + 1), 1.3 * g * popk(tt, sh["start"] + 0.35 + i * 0.15), col)
    lzt(fr, Wd / 2, cy + 480 * g, "الدليل على الترابيزة…", int(60 * g * popk(tt, sh["start"] + 0.8)), (255, 160, 120))
    return fr

def umbrella(p, x, y, s):
    tip = (x - 10 * s, y + 120 * s)
    p.poly([(x - 9 * s, y + 18 * s), (x + 9 * s, y + 18 * s), (tip[0] + 2 * s, tip[1] - 14 * s), (tip[0] - 2 * s, tip[1] - 14 * s)], (40, 40, 70, 255), INK, 1.6 * s)
    p.line([(x, y + 18 * s), (x, y - 6 * s)], (40, 30, 20, 255), 3 * s)
    p.line([(x, y - 6 * s), (x - 8 * s, y - 14 * s), (x - 15 * s, y - 8 * s)], (40, 30, 20, 255), 3 * s)
    p.line([(tip[0], tip[1] - 14 * s), tip], INK, 2 * s)

def rays(fr, Wd, Hd, c0, c1, tt, sign=1, cy=0.6):
    d = ImageDraw.Draw(fr, "RGBA")
    for i in range(18):
        a0 = i * 20 + sign * tt * 6; a_ = math.radians(a0); b = math.radians(a0 + 9); R = 3000
        d.polygon([(Wd / 2, Hd * cy), (Wd / 2 + R * math.cos(a_), Hd * cy + R * math.sin(a_)), (Wd / 2 + R * math.cos(b), Hd * cy + R * math.sin(b))], fill=c1 + (255,))

def ans_card(tt, sh, Wd, Hd):
    """case-7 answer (Tota): Nana — her umbrella was bone dry → she never went out"""
    st = T("A1"); fr = Image.new("RGB", (Wd, Hd), (16, 20, 44)); rays(fr, Wd, Hd, None, (30, 38, 80), tt); vert = Hd > Wd
    lzt(fr, Wd / 2, Hd * (0.17 if vert else 0.1), "حل الفزورة اللي فاتت", int((96 if vert else 86) * popk(tt, sh["start"] + 0.15)), (255, 214, 90))
    lay = Image.new("RGBA", (int(Wd * SS), int(Hd * SS)), (0, 0, 0, 0)); p = P(lay)
    caught = tt >= st + 2.4
    nx, ny, ns = (Wd * 0.3, Hd * 0.6, 2.3) if vert else (470, Hd + 150, 3.4)
    draw_char(p, "nana", nx, ny, ns, "scared" if caught else "smug", 0.0, 1, ((tt + 0.3) % 3.4) < 0.1, "scared" if caught else "hold", tt, None, 0.0, None)
    L2 = lay.resize((Wd, Hd), Image.LANCZOS); fr.paste(L2, (0, 0), L2)
    if caught: lzt(fr, nx + (60 if vert else 0), Hd * (0.27 if vert else 0.25), "الكدابة!", int((130 if vert else 150) * popk(tt, st + 2.4, 0.25)), (255, 255, 255), (170, 20, 20), rot=8)
    ux, uy = (Wd * 0.7, Hd * 0.42) if vert else (Wd * 0.7, Hd * 0.42)
    if tt >= st + 4.4:
        k = popk(tt, st + 4.4, 0.3); lay = Image.new("RGBA", (int(Wd * SS), int(Hd * SS)), (0, 0, 0, 0)); p = P(lay)
        d = ImageDraw.Draw(fr, "RGBA"); R = (150 if vert else 190) * k; d.ellipse([ux - R, uy - R, ux + R, uy + R], fill=(255, 214, 90, 255), outline=(255, 255, 255, 255), width=8)
        umbrella(p, ux + 20 * k, uy - 120 * k, 2.0 * k); L2 = lay.resize((Wd, Hd), Image.LANCZOS); fr.paste(L2, (0, 0), L2)
        if k >= 1: lzt(fr, ux if not vert else Wd / 2, uy + (230 if vert else 250), "ناشفة خالص!", 72, (255, 255, 255))
    if tt >= st + 6.1: lzt(fr, ux if not vert else Wd / 2, uy + (340 if vert else 370), "يعني ما خرجتش أصلًا!", int(72 * popk(tt, st + 6.1, 0.3)), (255, 214, 90))
    return fr

def cta_card(tt, sh, Wd, Hd):
    fr = Image.new("RGB", (Wd, Hd), (20, 12, 10)); rays(fr, Wd, Hd, None, (44, 24, 16), tt, -1, 0.5); vert = Hd > Wd
    st = T("C1"); k = popk(tt, sh["start"] + 0.15, 0.3)
    cxv, cyv, chh = (Wd * 0.5, Hd * 0.33, 760) if vert else (560, 480, 690)
    if k > 0:
        ch = int(chh * k); cw = int(ch * 1080 / 1920)
        cov = COVER7.resize((cw, ch), Image.LANCZOS)
        fr_c = Image.new("RGBA", (cw + 24, ch + 24), (255, 214, 90, 255)); fr_c.paste(cov, (12, 12))
        fr_c = fr_c.rotate(-4, expand=True, resample=Image.BICUBIC)
        fr.paste(fr_c, (int(cxv - fr_c.size[0] / 2), int(cyv - fr_c.size[1] / 2)), fr_c)
        lzt(fr, cxv, cyv - chh / 2 - 40 if vert else 72, "شوفوا القضية 7", int(70 * k), (255, 214, 90))
    for i, (lab, col, t0) in enumerate((("لايك", (230, 50, 70), 2.9), ("فولو", (40, 140, 230), 3.6), ("شير", (60, 170, 90), 4.3))):
        k2 = popk(tt, st + t0, 0.25)
        if k2 <= 0: continue
        cx, cy = ((Wd * 0.78 - i * Wd * 0.28, Hd * 0.66) if vert else (1380, 220 + i * 190))
        sw_ = 150 if vert else 260
        d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([cx - sw_ * k2, cy - 70 * k2, cx + sw_ * k2, cy + 70 * k2], int(55 * k2), fill=col + (255,), outline=(255, 255, 255, 255), width=6)
        lzt(fr, cx, cy + 4, lab, int(76 * k2), (255, 255, 255), (20, 20, 20))
    if tt >= st + 4.8:                                                                # growth rule 3
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
HOOK = "الخزنة اتفتحت… من غير ما تتكسر!"
_FREEZE = {}
def tag(fr, Wd, Hd, tt):
    if tt < 3.0 or tt >= Q: return
    d = ImageDraw.Draw(fr, "RGBA"); vert = Hd > Wd; x, y = (Wd / 2, 200) if vert else (Wd - 150, 60)
    d.rounded_rectangle([x - 110, y - 32, x + 110, y + 32], 26, fill=(200, 30, 40, 220)); lzt(fr, x, y, "قضية 8", 44, (255, 255, 255), stroke=False)

def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "q":
        if "h" not in _FREEZE: _FREEZE["h"] = scene(sh["start"] - 0.05, hcam(shots[shots.index(sh) - 1], sh["start"] - 0.05), (W, H))
        return finish(q_card(tt, sh, W, H, _FREEZE["h"]), tt)
    if sh["set"] == "ans": return finish(ans_card(tt, sh, W, H), tt)
    if sh["set"] == "cta": return finish(cta_card(tt, sh, W, H), tt)
    fr = keypad(tt, sh, W, H) if sh["set"] == "keypad" else scene(tt, hcam(sh, tt), (W, H))
    add_overlays(fr, tt, sh, W, H, hcam(sh, tt) if sh["set"] == "room" else None)
    if tt < 3.0:
        a_ = int(255 * min(1, (3.0 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([W / 2 - 640, 40, W / 2 + 640, 150], 30, fill=(20, 12, 8, int(a_ * 0.8)))
        lzt(fr, W / 2, 95, HOOK, 70, (255, 214, 90), alpha=a_)
    tag(fr, W, H, tt)
    return finish(fr, tt)

def add_overlays(fr, tt, sh, Wd, Hd, cam):
    if cam is None: return
    a_ = T("Z2")
    show = (LINEUP + 0.3 <= tt < T("S1")) or (a_ + 3.3 <= tt < a_ + 5.4)
    if show:
        hit = {0: (a_ + 3.6, a_ + 4.1), 1: (a_ + 4.1, a_ + 4.6), 2: (a_ + 4.6, a_ + 5.1)}
        for i, (who, col) in enumerate(NUMS):
            x, y, s = POS[who]; S_, _, (_, hy2) = body(who, x, y, s); q = W2S(cam, x, hy2 - 46 * S_ - 40)
            h0, h1 = hit[i]; pulse = 1 + (0.45 * math.sin(kk(tt, h0, h1) * math.pi) if h0 <= tt < h1 else 0)
            badge(fr, q[0], q[1], str(i + 1), min(1.15, cam[2] * 0.7) * popk(tt, max(LINEUP, a_ + 3.3) + 0.3 + i * 0.2 if tt > a_ else LINEUP + 0.3 + i * 0.2) * pulse, col)
    if REPRISE <= tt < a_ + 7.65:                                                     # «ركزوا…» magnifier lens slides over the table
        u = ease(kk(tt, REPRISE + 0.1, a_ + 7.5)); cx_, cy_ = W2S(cam, lerp(CARD[0], CAKE[0], u), 545); r = int(min(Wd, Hd) * 0.2)
        src = fr.resize((int(Wd * 1.6), int(Hd * 1.6)), Image.LANCZOS)
        crop = src.crop((int(cx_ * 1.6 - r), int(cy_ * 1.6 - r), int(cx_ * 1.6 + r), int(cy_ * 1.6 + r)))
        mask = Image.new("L", crop.size, 0); ImageDraw.Draw(mask).ellipse([0, 0, 2 * r - 1, 2 * r - 1], fill=255)
        fr.paste(crop, (int(cx_ - r), int(cy_ - r)), mask); d = ImageDraw.Draw(fr, "RGBA")
        d.ellipse([cx_ - r - 6, cy_ - r - 6, cx_ + r + 6, cy_ + r + 6], outline=(40, 40, 46), width=16)
        d.line([(cx_ + r * 0.72, cy_ + r * 0.72), (cx_ + r * 1.4, cy_ + r * 1.4)], fill=(110, 70, 36), width=34)
        lzt(fr, Wd / 2, Hd * (0.16 if Hd > Wd else 0.1), "ركّزوا… الدليل قدامكم!", 72, (255, 214, 90))

VIGV = VIG.resize((1080, 1920))
def vertical(_base, tt):
    sh = shot_at(tt); Wd, Hd = 1080, 1920
    if sh["set"] == "q":
        if "v" not in _FREEZE: _FREEZE["v"] = scene(sh["start"] - 0.05, vcam(shots[shots.index(sh) - 1], sh["start"] - 0.05), (Wd, Hd))
        return q_card(tt, sh, Wd, Hd, _FREEZE["v"])
    if sh["set"] == "ans": fr = ans_card(tt, sh, Wd, Hd); sub_chunk(fr, tt, 520, 1480, 72); return fr
    if sh["set"] == "cta": fr = cta_card(tt, sh, Wd, Hd); sub_chunk(fr, tt, 520, 1480, 66); return fr
    if sh["set"] == "keypad": fr = keypad(tt, sh, Wd, Hd); cam = None
    else: cam = vcam(sh, tt); fr = scene(tt, cam, (Wd, Hd))
    add_overlays(fr, tt, sh, Wd, Hd, cam)
    fr = ImageChops.multiply(fr, VIGV)
    u = tt - sh["start"]
    if sh.get("tin") in ("whip", "whipl") and u < 0.18: fr = fr.filter(ImageFilter.BoxBlur(int(2 + 18 * (1 - u / 0.18))))
    if tt < 3.0:
        a_ = int(255 * min(1, (3.0 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([90, 230, 990, 470], 40, fill=(20, 12, 8, int(a_ * 0.75)))
        lzt(fr, 540, 300, "الخزنة اتفتحت…", 92, (255, 255, 255), alpha=a_); lzt(fr, 540, 405, "من غير ما تتكسر!", 88, (255, 214, 90), alpha=a_)
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
    n = int(TOTAL * SR) + SR * 3; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(88)
    dr = np.arange(int(Q * SR)) / SR                                                     # low suspense drone until the question
    drone = (np.sin(2 * np.pi * 55 * dr) * 0.05 + np.sin(2 * np.pi * 82.5 * dr) * 0.03) * (0.7 + 0.3 * np.sin(dr * 0.8))
    mix_into(buf, drone.astype(np.float32), 0, 1.0)
    for j in range(int(Q / 1.0)): mix_into(buf, tone(2400, 0.03, 0.05, 80), 0.5 + j * 1.0, 1.0); mix_into(buf, tone(1900, 0.03, 0.04, 80), 1.0 + j * 1.0, 1.0)   # wall clock tick-tock
    mix_into(buf, creak(), 0.35, 1.0); mix_into(buf, SFXF["stinger"] * 0.45, 0.4, 1.0)
    for j in range(int(LIGHT / 0.45) + 1): mix_into(buf, tone(1320, 0.05, 0.08, 40), 0.1 + j * 0.45, 1.0)          # LED beeps in the dark
    mix_into(buf, SFXF["switch"] * 0.6, LIGHT - 0.05, 1.0); mix_into(buf, SFXF["gasp"] * 0.35, LIGHT + 0.05, 1.0)
    for j in range(int((Z1 + 1.6 - PASS_E) / 0.33)): mix_into(buf, tone(110, 0.06, 0.12, 35), PASS_E + j * 0.33, 1.0)   # Zalata's steps
    mix_into(buf, tone(240, 0.4, 0.16, 5), PASS + 0.2, 1.0)
    for i in range(3): mix_into(buf, tone(660 + i * 220, 0.18, 0.2, 12), LINEUP + 0.3 + i * 0.2, 1.0)
    mix_into(buf, tone(140, 0.7, 0.25, 3), B1 + 1.9, 1.0)
    a_ = T("Z2")
    for i, t0 in enumerate((0.75, 1.35, 1.95, 2.5)): mix_into(buf, tone(880 + i * 120, 0.12, 0.18, 14), a_ + t0, 1.0)       # key beeps 1 9 5 8
    for i, h in enumerate((3.6, 4.1, 4.6)): mix_into(buf, tone(700 + i * 180, 0.2, 0.18, 10), a_ + h, 1.0)
    mix_into(buf, SFXF["stinger"] * 0.3, REPRISE, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), Q + k_ * 0.09, 1.0)
    st = T("A1"); mix_into(buf, tone(180, 0.5, 0.3, 4), st + 2.4, 1.0); mix_into(buf, tone(120, 0.5, 0.3, 4), st + 2.4, 1.0)
    mix_into(buf, tone(988, 0.3, 0.16, 8), st + 4.4, 1.0); mix_into(buf, tone(1318, 0.3, 0.16, 8), st + 6.1, 1.0)
    for i, t0 in enumerate((2.9, 3.6, 4.3)): mix_into(buf, tone(880 + i * 220, 0.2, 0.2, 10), T("C1") + t0, 1.0)
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 1.0: mix_into(buf, SFXF["whoosh"] * 0.2, s_["start"] - 0.1, 1.0)
    for st_, k in lines:
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8; mix_into(buf, v, st_, 1.0)
    write_wav(buf[:int(TOTAL * SR)], path)

# ---------------- cover + YT thumbnail (growth rules 11-14, 22-24) ----------------
def make_covers():
    def comp(Wd, Hd, vert):
        bgc = ImageEnhance.Brightness(RLIT.crop((0, 120, 1000, 800)).resize((Wd, Hd), Image.LANCZOS).filter(ImageFilter.GaussianBlur(7))).enhance(0.75)
        img = bgc.resize((int(Wd * SS), int(Hd * SS))); d = ImageDraw.Draw(img, "RGBA")
        # the open empty safe (story object)
        sx, sy, su = (Wd * 0.76, Hd * 0.27, 2.4) if vert else (Wd * 0.80, Hd * 0.42, 2.9)
        Qs = lambda x, y: ((sx + (x - 148) * su) * SS, (sy + (y - 297) * su) * SS)
        draw_safe(d, Qs, su * SS, 2.0, False)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); p = P(lay)
        nx, ny, ns = (Wd * 0.34, Hd * 0.80, 4.6) if vert else (Wd * 0.33, Hd * 1.28, 5.4)          # BIG shocked Nana
        draw_char(p, "nana", nx, ny, ns, "shock", 0.6, 1, False, "up", 0.0, None, 0.0, None)
        if vert:
            for i, (who, col) in enumerate(NUMS):                                       # the 3 suspects, badges 1-2-3
                x = Wd * (0.2 + 0.3 * i); draw_char(p, who, x, Hd * 1.08, 2.3, "scared" if i == 2 else "flat", 0.0, -1, False, "down", 0.0, None, 0.0, None)
        img.paste(lay, (0, 0), lay); fr = img.resize((Wd, Hd), Image.LANCZOS)
        if vert:
            d0 = ImageDraw.Draw(fr, "RGBA"); d0.rectangle([0, Hd * 0.535, Wd, Hd * 0.725], fill=(10, 6, 4, 150))
            lzt(fr, Wd / 2, Hd * 0.575, "مين فتح", 160, (255, 255, 255)); lzt(fr, Wd / 2, Hd * 0.67, "الخزنة؟", 180, (255, 214, 60))
            for i, (who, col) in enumerate(NUMS): badge(fr, Wd * (0.2 + 0.3 * i), Hd * 0.765, str(i + 1), 1.2, col)
            bx, by = Wd / 2, 120
        else:
            lzt(fr, Wd * 0.62, Hd * 0.72, "مين فتح الخزنة؟", 150, (255, 214, 60))
            bx, by = 260, 90
        d = ImageDraw.Draw(fr, "RGBA"); d.rounded_rectangle([bx - 190, by - 46, bx + 190, by + 46], 34, fill=(200, 30, 40, 240))
        lzt(fr, bx, by, "مين الكداب؟ • قضية 8", 42, (255, 255, 255), stroke=False)
        return fr
    comp(1080, 1920, True).save(ROOT + "/publish/thumbs/kaddab_e08_cover.jpg", quality=92)
    comp(1920, 1080, False).resize((1280, 720), Image.LANCZOS).save(ROOT + "/publish/thumbs/kaddab_e08_yt.jpg", quality=92)

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
