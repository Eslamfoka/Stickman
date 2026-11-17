# «مين الكداب؟» — القضية 5: مين بعت جواب غرامي لعم بندق؟  (H 1920x1080 + V 1080x1920 in one pass)
# Narrator = Nana (Tota is a suspect for the first time). Location: «أوضة بندق وعزيزة» (day).
# Clue: the love letter says «بحبك يا بندء» (ء instead of ق), pink pen. Tota's notebook (in her hand, slightly open)
#   has «عم بندء» in the SAME pink pen with the SAME mistake — and she says she can't write letters. Never pointed at.
# ANSWER (say it at the END of case 6): توتة. Case-4 answer told at the end here (A1): Zalata — red paint on his fingertip.
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/kaddab/05")
SERIES = "مين الكداب؟"; EPT = "مين بعت الجواب؟"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"; DJ = ROOT + "/brand/fonts/DejaVuSans-Bold.ttf"
SFXF = {"whoosh": load_audio(ROOT + "/trend/01/sfx/whoosh.mp3"), "sting": load_audio(ROOT + "/trend/01/sfx/stinger.mp3")}

SUB = {"AZ1": "مين اللي باعت الجواب ده لجوزي؟! مكتوب فيه بحبك يا بندق!",
       "B1": "والله العظيم ما اعرفش مين! ده أكيد مقلب!",
       "N1": "الجواب اتحط في جيبه النهارده الصبح... والمتهمين تلاتة!",
       "S1": "أنا كنت في المدرسة طول اليوم... وماكتبتّش حاجة خالص!",
       "Z1": "أنا خطي حلو... ومستحيل أغلط في الكتابة!",
       "T1": "وأنا لسه صغيّرة... ماعرفش أكتب جوابات أصلاً!",
       "N2": "مين فيهم الكداب؟ واحد... ولا اتنين... ولا تلاتة؟ بصّوا على الجواب كويس... واكتبوا في الكومنتات!",
       "A1": "وحل الفزورة اللي فاتت: الكداب كان زلطة! عشان صباعه كان عليه دهان أحمر... وهو قال إنه ما نزلش!",
       "C1": "ولو ما شفتوش الحلقة اللي فاتت... شوفوها! وما تنسوش اللايك والفولو والشير!", "LAUGH": ""}
WHO = {"AZ1": "aziza", "B1": "bondo2", "N1": "nana", "S1": "shatta", "Z1": "zalata", "T1": "tota", "N2": "nana", "A1": "nana", "C1": "nana", "LAUGH": "-"}
EXPR = {"AZ1": "shout", "B1": "scared", "N1": "smug", "S1": "neutral", "Z1": "smug", "T1": "happy", "N2": "smug", "A1": "happy", "C1": "happy", "LAUGH": "laugh"}
load_lines(list(SUB))
ROOM = _ld(ROOT + "/daily/bg/bandaq_room.png")
COVER4 = Image.open(ROOT + "/publish/thumbs/kaddab_e04_cover.jpg").convert("RGB")
PINK = (226, 70, 150)

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
WIDE = (1000, 640, 1.22)
t = say(0.1, "AZ1"); shakes.append((0.15, 14)); a = T("AZ1")
shot("room", 0.0, a + 1.95, (1350, 700, 2.6), (1350, 705, 2.35), ease="crash")         # CU Aziza waving the letter + slipper
LETTER = a + 1.95; shot("letter", LETTER, t + 0.1, None, tin="zoom")                    # «مكتوب فيه بحبك يا بندق» → the letter
t += 0.1
s = t; t = say(t + 0.05, "B1") + 0.05; shot("room", s, t, (1570, 715, 2.4), (1570, 708, 2.55), tin="whip")   # Bandaq: hands up
GLARE = t; shakes.append((GLARE + 0.1, 14)); shot("room", t, t + 0.7, (1350, 700, 2.5), (1350, 690, 2.8), tin="whip", ease="crash")   # slipper up!
LAUGH0 = t + 0.25; say(LAUGH0, "LAUGH"); t += 0.7
n1 = say(t + 0.1, "N1"); N1 = T("N1")
shot("room", t, N1 + 3.05, (380, 715, 2.4), (380, 708, 2.55), tin="whipl")              # Nana the detective, magnifier
LINEUP = N1 + 3.05; shot("room", LINEUP, n1 + 0.2, WIDE, (1000, 650, 1.3), tin="whipl")   # «والمتهمين تلاتة!» → lineup, badges
t = n1 + 0.2
s = t; t = say(t + 0.05, "S1") + 0.1; shot("room", s, t, (630, 715, 2.35), (630, 708, 2.5), tin="whipl")
s = t; t = say(t + 0.05, "Z1") + 0.1; shot("room", s, t, (870, 715, 2.35), (870, 708, 2.5), tin="whip")
s = t; t = say(t + 0.05, "T1") + 0.15; shot("room", s, t, (1110, 790, 2.45), (1110, 782, 2.65), tin="whip")
ASK = t; n2 = say(t + 0.05, "N2"); a = T("N2")
shot("room", ASK, a + 1.5, (380, 715, 2.4), (380, 708, 2.6), tin="whip")
shot("room", a + 1.5, a + 4.5, WIDE, (1000, 650, 1.3), tin="whipl")                    # 1… 2… 3
REPRISE = a + 4.5; shot("letter2", REPRISE, a + 6.3, None, tin="zoom")                  # «بصّوا على الجواب كويس» — magnifier sweeps the letter
shot("room", a + 6.3, n2 + 0.3, WIDE, (1000, 650, 1.28), tin="whip")
t = n2 + 0.3
Q = t; shot("q", t, t + 1.2, None); t += 1.2
ANS = t; t = say(t + 0.25, "A1") + 0.35; shot("ans", ANS, t, None, tin="flash")
CTA = t; t = say(t + 0.15, "C1") + 0.8; shot("cta", CTA, t, None, tin="whip")
TOTAL = t
LAUGH_D = 1.3

# ---------------- staging (world = room 1920x1080) ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
POS = {"nana": (380, 1015, 1.7), "shatta": (630, 1010, 1.7), "zalata": (870, 1010, 1.7), "tota": (1110, 1025, 1.9),
       "aziza": (1350, 1012, 1.75), "bondo2": (1570, 1012, 1.7)}
NUMS = (("shatta", (230, 90, 40)), ("zalata", (60, 150, 80)), ("tota", (196, 40, 96)))

def body(who, x, y, s):
    S = s * CH[who]["scale"]; sh = y - 134 * S; return S, sh, (x, sh - 56 * S)
def hand(who, x, y, s, arms, side):
    S, sh, _ = body(who, x, y, s)
    A = {"down": ((x - 34 * S, sh + 72 * S), (x + 34 * S, sh + 72 * S)), "talk": ((x - 50 * S, sh + 52 * S), (x + 60 * S, sh + 8 * S)),
         "hold": ((x - 36 * S, sh + 70 * S), (x + 46 * S, sh + 30 * S)), "up": ((x - 70 * S, sh - 50 * S), (x + 70 * S, sh - 50 * S)),
         "hips": ((x - 48 * S, sh + 40 * S), (x + 48 * S, sh + 40 * S)), "point": ((x - 38 * S, sh + 68 * S), (x + 84 * S, sh - 6 * S))}
    return A.get(arms, A["down"])[0 if side < 0 else 1]

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, held=None):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    blink = ((tt + len(who) * 0.37) % 3.6) < 0.11 and expr not in ("laugh", "scared", "shout")
    if not talking: lean += math.sin(tt * 1.7 + len(who)) * 0.05
    X, Y_ = W2S(cam, x, y); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, held, lean, None)

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
os.chdir(ROOT + "/kaddab/05")

# ---------------- props ----------------
def slipper(p, x, y, s, rot=0.0):
    c, sn = math.cos(rot), math.sin(rot); R = lambda dx, dy: (x + dx * c - dy * sn, y + dx * sn + dy * c)
    sole = [R(13 * s * math.cos(a_ / 16 * 2 * math.pi), 27 * s * math.sin(a_ / 16 * 2 * math.pi)) for a_ in range(16)]
    p.poly(sole, (70, 150, 210, 255), INK, 2 * s)
    p.poly([R(-14 * s, -10 * s), R(14 * s, -10 * s), R(11 * s, 4 * s), R(-11 * s, 4 * s)], (240, 240, 240, 255), INK, 1.5 * s)

def pink_letter(p, x, y, s, rot=0.0):
    c, sn = math.cos(rot), math.sin(rot); R = lambda dx, dy: (x + dx * c - dy * sn, y + dx * sn + dy * c)
    p.poly([R(-20 * s, -26 * s), R(20 * s, -26 * s), R(20 * s, 26 * s), R(-20 * s, 26 * s)], (255, 214, 232, 255), INK, 2 * s)
    for i in range(3):
        a_, b_ = R(-13 * s, (-12 + i * 10) * s), R(13 * s, (-12 + i * 10) * s); p.line([a_, b_], PINK + (255,), 1.6 * s)
    q = R(0, 18 * s); p.ell(q[0] - 3 * s, q[1], 3.2 * s, 3.2 * s, PINK + (255,), None); p.ell(q[0] + 3 * s, q[1], 3.2 * s, 3.2 * s, PINK + (255,), None)

def notebook_open(p, x, y, s):
    """Tota's school notebook, a bit open: two pages, pink-pen line on the right page (the clue — text drawn on the frame)"""
    p.poly([(x - 30 * s, y - 22 * s), (x, y - 18 * s), (x, y + 18 * s), (x - 30 * s, y + 22 * s)], (250, 248, 236, 255), INK, 1.8 * s)
    p.poly([(x, y - 18 * s), (x + 30 * s, y - 22 * s), (x + 30 * s, y + 22 * s), (x, y + 18 * s)], (250, 248, 236, 255), INK, 1.8 * s)
    for i in range(4): p.line([(x - 26 * s, y - 10 * s + i * 8 * s), (x - 4 * s, y - 9 * s + i * 8 * s)], (150, 170, 220, 255), 1 * s)
    p.line([(x + 8 * s, y + 10 * s), (x + 24 * s, y + 9 * s)], (150, 170, 220, 255), 1 * s)

def magnifier(p, x, y, s):
    p.line([(x, y), (x + 14 * s, y - 26 * s)], (90, 60, 30, 255), 6 * s)
    p.ell(x + 22 * s, y - 42 * s, 17 * s, 17 * s, (200, 230, 255, 120), (40, 40, 46, 255), 4 * s)

def pen_ear(p, cam, tt):
    x, y, s = POS["shatta"]; S, sh, (hx, hy) = body("shatta", x, y, s); z = cam[2]
    a_ = W2S(cam, hx + 40 * S, hy - 30 * S); b_ = W2S(cam, hx + 58 * S, hy + 8 * S)
    p.line([a_, b_], (40, 90, 200, 255), 5 * S * z / 1.7)

# ---------------- the letter (insert) ----------------
def make_letter(w=760, h=560):
    im = Image.new("RGB", (w, h), (255, 222, 236)); d = ImageDraw.Draw(im)
    for yy in range(120, h - 40, 70): d.line([(50, yy), (w - 50, yy)], fill=(240, 180, 205), width=3)
    d.rectangle([0, 0, w - 1, h - 1], outline=(200, 120, 160), width=8)
    f = ImageFont.truetype(LZ, 120)
    d.text((w / 2, h / 2 - 30), "بحبك يا بندء", font=f, fill=PINK, anchor="mm", direction="rtl", language="ar")
    for (cx, cy, r) in ((w / 2, h - 110, 36), (w / 2 - 170, h - 120, 20), (w / 2 + 170, h - 120, 20)):
        d.ellipse([cx - 2 * r, cy - r, cx, cy + r * 0.6], fill=PINK); d.ellipse([cx, cy - r, cx + 2 * r, cy + r * 0.6], fill=PINK)
        d.polygon([(cx - 2 * r + 1, cy), (cx + 2 * r - 1, cy), (cx, cy + 2 * r)], fill=PINK)
    return im
LETTER_IMG = make_letter()

def letter_insert(tt, sh, lens=False):
    u = kk(tt, sh["start"], sh["end"]); zz = 1.0 + 0.08 * u
    cam = (1350 - 960 / 2.3, 700 - 540 / 2.3, 2.3)
    fr = bg_crop(ROOM, cam).resize((W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(12))
    fr = ImageEnhance.Brightness(fr).enhance(0.5)
    lw, lh = int(1240 * zz), int(1240 * zz * 560 / 760)
    lt = LETTER_IMG.resize((lw, lh), Image.LANCZOS).convert("RGBA").rotate(-3 + 2 * u, expand=True, resample=Image.BICUBIC)
    ox, oy = int(W / 2 - lt.size[0] / 2), int(H / 2 - lt.size[1] / 2 + 20); fr.paste(lt, (ox, oy), lt)
    if lens:                                                                                 # magnifier sweeps the whole letter
        v = ease(u); lx = W * (0.25 + 0.5 * v); ly = H * (0.45 + 0.08 * math.sin(v * math.pi * 2)); r = 150
        src = fr.resize((int(W * 1.6), int(H * 1.6)), Image.LANCZOS)
        crop = src.crop((int(lx * 1.6 - r), int(ly * 1.6 - r), int(lx * 1.6 + r), int(ly * 1.6 + r)))
        mask = Image.new("L", crop.size, 0); ImageDraw.Draw(mask).ellipse([0, 0, 2 * r - 1, 2 * r - 1], fill=255)
        fr.paste(crop, (int(lx - r), int(ly - r)), mask)
        d = ImageDraw.Draw(fr, "RGBA")
        d.ellipse([lx - r - 6, ly - r - 6, lx + r + 6, ly + r + 6], outline=(40, 40, 46), width=16)
        d.line([(lx + r * 0.72, ly + r * 0.72), (lx + r * 1.45, ly + r * 1.45)], fill=(110, 70, 36), width=34)
        lzt(fr, W / 2, 70, "بُصّ كويس!", 80, (255, 214, 90))
    return fr

# ---------------- room ----------------
def room_frame(tt, sh):
    cam = cam_at(sh, tt); z = cam[2]
    img = bg_crop(ROOM, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    # Nana (detective)
    narms = "talk" if (T("N1") <= tt < T("N1") + DUR["N1"]) or (T("N2") <= tt < T("N2") + 1.5) else "hold"
    person(lay, cam, "nana", *POS["nana"], tt, "smug", 1, narms)
    hx_, hy_ = hand("nana", *POS["nana"], narms, 1); q = W2S(cam, hx_, hy_); magnifier(p, q[0], q[1], POS["nana"][2] * z)
    # suspects
    sarms = "talk" if T("S1") <= tt < T("S1") + DUR["S1"] else "down"
    person(lay, cam, "shatta", *POS["shatta"], tt, "neutral" if tt < GLARE else ("scared" if tt < T("N1") else "neutral"), 0, sarms)
    pen_ear(p, cam, tt)
    zarms = "talk" if T("Z1") <= tt < T("Z1") + DUR["Z1"] else "hips"
    person(lay, cam, "zalata", *POS["zalata"], tt, "smug", 0, zarms)
    person(lay, cam, "tota", *POS["tota"], tt, "happy", 0, "clap")                                  # innocent: notebook held at her chest
    S_t, sh_t, _ = body("tota", *POS["tota"]); hx_, hy_ = POS["tota"][0], sh_t + 46 * S_t
    q = W2S(cam, hx_, hy_); notebook_open(p, q[0], q[1], S_t * z)
    # Aziza: letter (right) + slipper (left), slipper UP on the glare
    ax, ay, as_ = POS["aziza"]
    aarms = "up" if (tt < 1.9 or GLARE <= tt < GLARE + 0.7) else "hold"
    person(lay, cam, "aziza", ax, ay, as_, tt, "shout" if tt < T("B1") else "angry", -1 if tt >= T("B1") else 0, aarms)
    lh = hand("aziza", ax, ay, as_, aarms, -1); q = W2S(cam, *lh); slipper(p, q[0], q[1] - 8 * z, as_ * z, -0.5 if aarms == "up" else 0.2)
    rh = hand("aziza", ax, ay, as_, aarms, 1); q = W2S(cam, *rh); pink_letter(p, q[0], q[1] - 18 * z, as_ * z * 1.1, math.sin(tt * 9) * 0.15 if tt < 1.9 else 0.1)
    # Bandaq: terrified, hands up
    barms = "up" if tt < T("N1") + 1.0 else "scared"
    person(lay, cam, "bondo2", *POS["bondo2"], tt, "scared", -1, barms)
    lay = tint_layer(lay, (255, 240, 214)); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    # the clue text on Tota's notebook (pink pen) — small, readable only in her CU / when you look
    q = W2S(cam, hx_ + 15 * S_t, hy_ - 4 * S_t)
    if z > 1.6: lzt(fr, q[0], q[1], "عم بندء", int(8 * S_t * z), PINK, stroke=False)
    # badges
    if tt >= LINEUP and tt < Q:
        a = T("N2"); hit = {0: (a + 1.65, a + 2.5), 1: (a + 2.51, a + 3.54), 2: (a + 3.55, a + 4.5)}
        for i, (who, col) in enumerate(NUMS):
            x, y, s = POS[who]; S_, _, (_, hy2) = body(who, x, y, s); q = W2S(cam, x, hy2 - 46 * S_ - 50)
            h0, h1 = hit[i]; pulse = 1 + (0.45 * math.sin(kk(tt, h0, h1) * math.pi) if h0 <= tt < h1 else 0)
            if tt >= a + 6.3: pulse = 1 + 0.12 * math.sin(tt * 8)
            badge(fr, q[0], q[1], str(i + 1), min(1.1, z * 0.75) * popk(tt, LINEUP + i * 0.2) * pulse, col)
    if GLARE <= tt < GLARE + 0.6: lzt(fr, W * 0.30, H * 0.22, "!!!", int(170 * popk(tt, GLARE, 0.2)), (255, 80, 60))
    return fr

def q_card(tt, sh):
    fr = ImageEnhance.Brightness(frame_cache(sh["start"] - 0.05)).enhance(0.45).filter(ImageFilter.GaussianBlur(5)).convert("RGBA")
    lzt(fr, W / 2, 300, "اكتب رقم الكداب في الكومنتات!", int(92 * popk(tt, sh["start"] + 0.05, 0.3)), (255, 214, 90))
    for i, (_, col) in enumerate(NUMS): badge(fr, W / 2 + (i - 1) * 200, 470, str(i + 1), 1.3 * popk(tt, sh["start"] + 0.3 + i * 0.15), col)
    lzt(fr, W / 2, 640, "الدليل في الجواب...", int(60 * popk(tt, sh["start"] + 0.75)), (255, 255, 255))
    return fr.convert("RGB")

def ans_card(tt, sh):
    """case-4 answer: Zalata lied — red paint on his fingertip, and he said he never came down"""
    st = T("A1"); fr = Image.new("RGB", (W, H), (16, 20, 44)); d = ImageDraw.Draw(fr, "RGBA")
    for i in range(18):
        a0 = i * 20 + tt * 6; a_ = math.radians(a0); b = math.radians(a0 + 9)
        d.polygon([(W / 2, H * 0.6), (W / 2 + 2400 * math.cos(a_), H * 0.6 + 2400 * math.sin(a_)), (W / 2 + 2400 * math.cos(b), H * 0.6 + 2400 * math.sin(b))], fill=(30, 38, 80, 255))
    lzt(fr, W / 2, 110, "حل الفزورة اللي فاتت", int(86 * popk(tt, sh["start"] + 0.15)), (255, 214, 90))
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    caught = tt >= st + 1.69
    x, y, s = 520, 1080 + 130, 3.3
    draw_char(p, "zalata", x, y, s, "scared" if caught else "smug", 0.0, 1, ((tt + 0.3) % 3.4) < 0.1, "talk", tt, None, 0.0, None)
    S = s * CH["zalata"]["scale"]; sh_ = y - 134 * S; q = (x + 63 * S, sh_ + 4 * S); p.ell(q[0], q[1], 4 * S, 4 * S, (200, 30, 30, 255), None)
    L2 = lay.resize((W, H), Image.LANCZOS); fr.paste(L2, (0, 0), L2)
    if caught: lzt(fr, 520, 250, "الكداب!", int(150 * popk(tt, st + 1.69, 0.25)), (255, 255, 255), (170, 20, 20), rot=8)
    if tt >= st + 3.23:                                                                   # zoom bubble on the red fingertip
        k = popk(tt, st + 3.23, 0.3); cx, cy, r = 1340, 470, int(250 * k)
        if r > 10:
            d = ImageDraw.Draw(fr, "RGBA"); d.ellipse([cx - r - 8, cy - r - 8, cx + r + 8, cy + r + 8], fill=(255, 255, 255, 255))
            d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(250, 240, 225, 255))
            fw = 46 * k; d.rounded_rectangle([cx - fw, cy - r * 0.7, cx + fw, cy + r * 0.95], int(fw), fill=(250, 250, 250), outline=(20, 20, 20), width=6)
            d.ellipse([cx - fw * 0.9, cy - r * 0.72, cx + fw * 0.9, cy - r * 0.72 + fw * 1.6], fill=(200, 30, 30))
            lzt(fr, cx, cy + r + 60, "دهان أحمر!", int(72 * k), (255, 214, 90))
    if tt >= st + 5.39:
        lzt(fr, 1340, 900, "وهو قال إنه ما نزلش!", int(54 * popk(tt, st + 5.39)), (255, 255, 255))
    return fr

def cta_card(tt, sh):
    fr = Image.new("RGB", (W, H), (20, 12, 10)); d = ImageDraw.Draw(fr, "RGBA")
    for i in range(18):
        a0 = i * 20 - tt * 6; a_ = math.radians(a0); b = math.radians(a0 + 9)
        d.polygon([(W / 2, H / 2), (W / 2 + 2400 * math.cos(a_), H / 2 + 2400 * math.sin(a_)), (W / 2 + 2400 * math.cos(b), H / 2 + 2400 * math.sin(b))], fill=(44, 24, 16, 255))
    k = popk(tt, sh["start"] + 0.15, 0.3)
    if k > 0:
        ch = int(690 * k); cw = int(ch * 1080 / 1920)
        cov = COVER4.resize((cw, ch), Image.LANCZOS)
        fr_c = Image.new("RGBA", (cw + 24, ch + 24), (255, 214, 90, 255)); fr_c.paste(cov, (12, 12))
        fr_c = fr_c.rotate(-4, expand=True, resample=Image.BICUBIC)
        fr.paste(fr_c, (int(560 - fr_c.size[0] / 2), int(480 - fr_c.size[1] / 2)), fr_c)
        lzt(fr, 560, 72, "شوفوا القضية 4", int(70 * k), (255, 214, 90))
    st = T("C1")
    for i, (lab, col, t0) in enumerate((("لايك", (230, 50, 70), 2.4), ("فولو", (40, 140, 230), 2.9), ("شير", (60, 170, 90), 3.4))):
        k2 = popk(tt, st + t0, 0.25)
        if k2 <= 0: continue
        cx, cy = 1380, 220 + i * 190
        d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([cx - 260 * k2, cy - 80 * k2, cx + 260 * k2, cy + 80 * k2], int(60 * k2), fill=col + (255,), outline=(255, 255, 255, 255), width=6)
        ix = cx + 170 * k2
        if i == 0:
            r = 26 * k2; d.ellipse([ix - 2 * r, cy - r, ix, cy + r * 0.6], fill=(255, 255, 255)); d.ellipse([ix, cy - r, ix + 2 * r, cy + r * 0.6], fill=(255, 255, 255))
            d.polygon([(ix - 2 * r + 2, cy), (ix + 2 * r - 2, cy), (ix, cy + 2 * r)], fill=(255, 255, 255))
        elif i == 1:
            d.rectangle([ix - 34 * k2, cy - 9 * k2, ix + 34 * k2, cy + 9 * k2], fill=(255, 255, 255)); d.rectangle([ix - 9 * k2, cy - 34 * k2, ix + 9 * k2, cy + 34 * k2], fill=(255, 255, 255))
        else:
            d.polygon([(ix - 34 * k2, cy + 20 * k2), (ix + 6 * k2, cy - 20 * k2), (ix + 6 * k2, cy - 40 * k2), (ix + 40 * k2, cy - 6 * k2), (ix + 6 * k2, cy + 28 * k2), (ix + 6 * k2, cy + 8 * k2), (ix - 20 * k2, cy + 34 * k2)], fill=(255, 255, 255))
        lzt(fr, cx - 50 * k2, cy + 4, lab, int(84 * k2), (255, 255, 255), (20, 20, 20))
    if tt >= st + 3.8:
        logo(fr, 1380, 780, 80); text(fr, 1380, 850, "@shattawzalata", 40, (255, 214, 90))
    return fr

_FC = {}
def frame_cache(t_):
    if t_ not in _FC: _FC[t_] = frame(t_)
    return _FC[t_]

HOOK = "جواب غرامي في جيب عم بندق… وعزيزة شافته!"
def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "letter": fr = letter_insert(tt, sh)
    elif sh["set"] == "letter2": fr = letter_insert(tt, sh, lens=True)
    elif sh["set"] == "q": return finish(q_card(tt, sh), tt)
    elif sh["set"] == "ans": return finish(ans_card(tt, sh), tt)
    elif sh["set"] == "cta": return finish(cta_card(tt, sh), tt)
    else: fr = room_frame(tt, sh)
    if tt < 3.0:
        a_ = int(255 * min(1, (3.0 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([W / 2 - 760, 40, W / 2 + 760, 150], 30, fill=(20, 12, 8, int(a_ * 0.8)))
        lzt(fr, W / 2, 95, HOOK, 66, (255, 214, 90), alpha=a_)
    return finish(fr, tt)

def vertical(fr, tt):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = ImageEnhance.Brightness(small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.35)
    bgv.paste(fr.resize((1080, 608), Image.LANCZOS), (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(255, 214, 90)); d.rectangle([0, 1168, 1080, 1171], fill=(255, 214, 90))
    if tt < ANS:
        lzt(bgv, 540, 240, "جواب غرامي", 110, (255, 255, 255)); lzt(bgv, 540, 390, "في جيب عم بندق!", 104, (255, 214, 90))
    else:
        lzt(bgv, 540, 240, "حل الفزورة", 110, (255, 255, 255)); lzt(bgv, 540, 390, "اللي فاتت", 120, (255, 214, 90))
    lzt(bgv, 540, 1840, "مين الكداب؟ • قضية جديدة", 46, (255, 150, 110))
    k, _ = line_at(tt)
    if k and SUB.get(k):
        ls_ = wrap(SUB[k])
        if len(ls_) <= 4:
            for i, l in enumerate(ls_): text(bgv, 540, 1290 + i * 80, l, 60, sw=6)
        else:
            for i, l in enumerate(wrap(SUB[k], 30)[:6]): text(bgv, 540, 1270 + i * 64, l, 50, sw=5)
    return bgv

def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(53)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 350) * 0.02, 0, 1.0)
    mix_into(buf, SFXF["sting"] * 0.45, 0.0, 1.0)
    mix_into(buf, SFXF["whoosh"] * 0.4, LETTER - 0.1, 1.0)
    for k_, f in enumerate((659, 784, 988)): mix_into(buf, tone(f, 0.5, 0.06, 5), LETTER + 0.15 + k_ * 0.12, 1.0)   # «love» harp, ironic
    mix_into(buf, SFXF["whoosh"] * 0.5, GLARE - 0.05, 1.0)
    mix_into(buf, tone(140, 0.35, 0.35, 6) + tone(95, 0.35, 0.3, 6), GLARE + 0.1, 1.0)
    for i in range(3): mix_into(buf, tone(660 + i * 220, 0.18, 0.2, 12), LINEUP + i * 0.2, 1.0)
    a = T("N2")
    for i, h in enumerate((1.65, 2.51, 3.55)): mix_into(buf, tone(700 + i * 180, 0.2, 0.18, 10), a + h, 1.0)
    mix_into(buf, SFXF["sting"] * 0.3, REPRISE, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), Q + k_ * 0.09, 1.0)
    mix_into(buf, tone(180, 0.5, 0.3, 4) + tone(120, 0.5, 0.3, 4), T("A1") + 1.69, 1.0)
    for i, t0 in enumerate((2.4, 2.9, 3.4)): mix_into(buf, tone(880 + i * 220, 0.2, 0.2, 10), T("C1") + t0, 1.0)
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 0.5: mix_into(buf, SFXF["whoosh"] * 0.25, s_["start"] - 0.1, 1.0)
    rms = lambda x: float(np.sqrt(np.mean(x ** 2))) + 1e-9; ref = []
    for st, k in lines:
        if k == "LAUGH": continue
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8; ref.append(rms(v)); mix_into(buf, v, st, 1.0)
    g = AUD["LAUGH"][:int(SR * LAUGH_D)].copy(); g[-int(SR * 0.35):] *= np.linspace(1, 0, int(SR * 0.35))
    mix_into(buf, g / rms(g) * float(np.mean(ref)) * 0.9, T("LAUGH"), 1.0)
    write_wav(buf[:int(TOTAL * SR)], path)

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
