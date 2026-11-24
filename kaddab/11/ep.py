# «مين الكداب؟» — القضية 11: «كشكول رشدي» (24/11, 20:00 Kuwait) — growth rules 1–32
# Opening = separate «حل القضية السابقة» (case 10 → عزيزة ✓, Tota T0).
# STORY HOOK: Roshdy's letter («الكشكول اللي في شقتي فيه سر العمارة… محدش يفتحه غيرك») + tag «من أسرار عمارة نعناعة».
#   Then the canonical 7th-floor flat (s1e8/bg/apt7_raw.png, moonlit, dusty sheets) at 8:40 pm: the door creaks, a flashlight
#   beam finds Roshdy's notebook beside the old radio, a hand takes it, and a GREEN handprint stays on the white dust sheet
#   (the beam lingers on it). Lineup in Nana's الصالة (canonical living_1080, lit): Nana N1 → ① شطة (kitchen, sandwich)
#   ② توتة (shows her «mirror selfie» proof — PHOTO insert) ③ بندق (from the front door) → N2 ask → Q card.
# ANSWER (start of case 12 ONLY): توتة ②. Lie: the mirror-selfie clock does say 8:45 (seen reversed in the mirror) — but the
#   sun is shining in the window: 8:45 in the MORNING, not at night. Theft: green face-mask clay handprint.
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont, ImageChops, ImageOps
import engine as ENG
os.chdir(ROOT + "/kaddab/11")
SERIES = "مين الكداب؟"; EPT = "كشكول رشدي"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"; DJ = ROOT + "/brand/fonts/DejaVuSans-Bold.ttf"; CA = ROOT + "/brand/fonts/Cairo.ttf"
SFXF = {n: load_audio(ROOT + f"/trend/01/sfx/{n}.mp3") for n in ("whoosh", "stinger", "gasp", "switch")}
SUB = {"T0": "إجابة القضية اللي فاتت: الكدابة كانت عزيزة! تلفزيونها كان مطفي… والحلق اللي وقع… شبه اللي في ودنها!",
       "N1": "كشكول رشدي اتسرق!… تلاتين سنة محدش فتح الشقة دي… مين اللي كان فوق في الدور السابع الساعة تسعة إلا ربع؟!",
       "S1": "مش أنا! أنا كنت في المطبخ بعمل ساندوتشات!",
       "T1": "وأنا كنت في الحمام بعمل ماسك… ومعايا دليل! صورتي قدام المراية… والساعة ورايا تسعة إلا ربع!",
       "B1": "وأنا كنت قاعد على الدكة تحت… ومحدش عدّى من جنبي!",
       "N2": "واحد فيكم كداب… والدليل قدامكم! مين اللي خد الكشكول؟ اكتبوا رقمه في الكومنتات!"}
CHUNKS = {"T0": [(0.0, "إجابة القضية اللي فاتت:", "إجابة"), (1.85, "الكدابة كانت عزيزة!", "عزيزة"), (3.75, "تلفزيونها كان مطفي…", "مطفي"),
                 (5.2, "والحلق اللي وقع…", "الحلق"), (6.4, "شبه اللي في ودنها!", "ودنها")],
          "N1": [(0.0, "كشكول رشدي اتسرق!…", "اتسرق"), (1.8, "تلاتين سنة محدش فتح الشقة دي…", "تلاتين سنة"),
                 (4.35, "مين اللي كان فوق في الدور السابع", "الدور السابع"), (5.85, "الساعة تسعة إلا ربع؟!", "تسعة إلا ربع")],
          "S1": [(0.0, "مش أنا!", None), (1.07, "أنا كنت في المطبخ بعمل ساندوتشات!", "المطبخ")],
          "T1": [(0.0, "وأنا كنت في الحمام بعمل ماسك…", "ماسك"), (2.3, "ومعايا دليل!", "دليل"), (3.55, "صورتي قدام المراية…", "المراية"),
                 (5.17, "والساعة ورايا…", "الساعة"), (6.5, "تسعة إلا ربع!", "تسعة إلا ربع")],
          "B1": [(0.0, "وأنا كنت قاعد على الدكة تحت…", "الدكة"), (2.43, "ومحدش عدّى من جنبي!", "محدش")],
          "N2": [(0.0, "واحد فيكم كداب…", "كداب"), (2.9, "والدليل قدامكم!", "الدليل"), (4.43, "مين اللي خد الكشكول؟", "الكشكول"),
                 (5.9, "اكتبوا رقمه في الكومنتات!", "رقمه")]}
WHO = {"T0": "tota", "N1": "nana", "S1": "shatta", "T1": "tota", "B1": "bondo2", "N2": "nana"}
NAME = {"nana": ("نعناعة", (150, 220, 190)), "shatta": ("شطة", (255, 140, 80)), "tota": ("توتة", (255, 130, 190)), "bondo2": ("بندق", (230, 170, 110))}
EXPR = {"T0": "smug", "N1": [(0, "shock"), (1.8, "angry")], "S1": [(0, "scared"), (1.0, "neutral")], "T1": [(0, "neutral"), (2.3, "smug")],
        "B1": "neutral", "N2": [(0, "angry"), (4.4, "smug")]}
load_lines(list(SUB))
APT = _ld(ROOT + "/s1e8/bg/apt7_raw.png")                                                       # canonical 7th-floor flat (Roshdy)
LIVING = _ld(ROOT + "/s1e1/bg/living_1080.png")                                                 # canonical «الصالة»
RLIT = ImageChops.multiply(ImageEnhance.Brightness(LIVING).enhance(1.55), Image.new("RGB", LIVING.size, (255, 236, 214)))

def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
BOOK = (625, 498)                       # Roshdy's notebook, lying on the side table by the old radio
PRINT = (548, 566)                      # green handprint on the white dust sheet (armchair arm)
DOORL = (60, 640)                       # the flat's door (left) — beam comes from here
POS = {"nana": (470, 1010, 1.6), "shatta": (880, 1010, 1.6), "tota": (1180, 1010, 1.6), "bondo2": (1480, 1010, 1.6)}
NUMS = (("shatta", (230, 90, 40)), ("tota", (220, 80, 150)), ("bondo2", (150, 96, 50)))
def body(who, x, y, s):
    S = s * CH[who]["scale"]; sh = y - 134 * S; return S, sh, (x, sh - 56 * S)

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
say(0.4, "T0"); PREV_END = T("T0") + DUR["T0"] + 0.35
shot("prev", 0.0, PREV_END, None, v=None)
t = PREV_END
LET = t; shot("letter", t, t + 3.2, None, v=None); t += 3.2                                                                # Roshdy's letter (story)
H2 = t; shot("apt", t, t + 1.5, (980, 560, 1.0), (900, 560, 1.12), tin="whip", v=((900, 560, 1.78), (820, 560, 1.85))); t += 1.5  # 8:40 the dusty flat
THEFT = t; shot("apt", t, t + 5.0, (760, 540, 1.6), (640, 540, 2.15), v=((700, 540, 2.0), (600, 540, 2.4))); t += 5.0
TAKE = THEFT + 2.0; PRINTT = TAKE + 0.35; BEAM_OFF = PRINTT + 1.9
s = t; t = say(t + 0.25, "N1") + 0.2; shakes.append((s + 0.3, 12))
shot("living", s, t, (520, 760, 2.4), (500, 770, 2.7), tin="whip", ease="crash", v=((480, 760, 2.6), (470, 770, 2.85)))
LINE = t; SIN = (t, t + 1.6); TIN = (t + 0.1, t + 1.7); BIN = (t + 0.2, t + 1.8)
shot("living", t, t + 1.9, (980, 640, 1.2), (1000, 650, 1.25), tin="whipl", v=((900, 620, 1.8), (1250, 620, 1.85))); t += 1.9
BADGES = t - 0.5
s = t; t = say(t + 0.1, "S1") + 0.2; x_ = POS["shatta"][0]
shot("living", s, t, (x_, 700, 2.6), (x_, 690, 2.85), tin="whip", v=((x_, 700, 2.85), (x_, 690, 3.05)))
s = t; t = say(t + 0.1, "T1") + 0.2; x_ = POS["tota"][0]
PH0 = T("T1") + 3.5; PH1 = T("T1") + DUR["T1"] + 1.4; t = max(t, PH1)
shot("living", s, t, (x_, 700, 2.6), (x_, 690, 2.85), tin="whip", v=((x_, 700, 2.85), (x_, 690, 3.05)))
s = t; t = say(t + 0.1, "B1") + 0.2; x_ = POS["bondo2"][0]
shot("living", s, t, (x_, 700, 2.6), (x_, 690, 2.85), v=((x_, 700, 2.85), (x_, 690, 3.05)))
s = t; t = say(t + 0.1, "N2") + 0.2; ASK = s
shot("living", s, t, (560, 680, 2.0), (900, 660, 1.35), v=((480, 690, 2.6), (900, 640, 1.85)))        # pulls out over all of them
Q = t; shot("q", t, t + 2.0, None, v=None); t += 2.0
TOTAL = t
def hcam(sh, tt): return cam_at(sh, tt)
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
    kw = dict(font=f, anchor="mm", direction="rtl", language="ar") if font in (None, CA) else dict(font=f, anchor="mm")
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
def rays(fr, Wd, Hd, col, tt, sign=1, cy=0.6):
    d = ImageDraw.Draw(fr, "RGBA")
    for i in range(18):
        a0 = i * 20 + sign * tt * 6; a_ = math.radians(a0); b = math.radians(a0 + 9); R = 3000
        d.polygon([(Wd / 2, Hd * cy), (Wd / 2 + R * math.cos(a_), Hd * cy + R * math.sin(a_)), (Wd / 2 + R * math.cos(b), Hd * cy + R * math.sin(b))], fill=col + (255,))

_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/kaddab/11")

# ---------------- subtitles ----------------
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
    if sum(widths) > maxw:
        f = ImageFont.truetype(LZ, max(6, int(size * sc * maxw / sum(widths)))); kw["font"] = f
        widths = [d.textlength(s, font=f, direction="rtl", language="ar") if s else 0 for s, _ in parts]
    tot = sum(widths); x = cx + tot / 2
    for (s, col), w_ in zip(parts, widths):
        if s: d.text((x - w_, cy), s, fill=col + (255,), anchor="lm", **kw)
        x -= w_
    nm, ncol = NAME[WHO[k]]; fn = ImageFont.truetype(LZ, int(size * 0.62))
    nw = d.textlength(nm, font=fn, direction="rtl", language="ar")
    nx = cx + tot / 2 - nw / 2 - 10; ny = cy - size * 0.95
    d.rounded_rectangle([nx - nw / 2 - 18, ny - size * 0.38, nx + nw / 2 + 18, ny + size * 0.38], int(size * 0.3), fill=ncol + (235,))
    d.text((nx, ny), nm, font=fn, fill=(20, 12, 8, 255), anchor="mm", direction="rtl", language="ar")
    img.paste(lay, (0, 0), lay)

# ---------------- props ----------------
def notebook(d, x, y, zz, rot=0.0):
    """Roshdy's old brown notebook lying flat (centre x,y in SS px)"""
    w, h = 46 * zz, 14 * zz; c, s_ = math.cos(rot), math.sin(rot)
    pts = [(-w, -h), (w, -h), (w + 8 * zz, h), (-w + 8 * zz, h)]
    d.polygon([(x + px * c - py * s_, y + px * s_ + py * c) for px, py in pts], fill=(120, 70, 36), outline=(40, 20, 8))
    d.line([(x - w * 0.6, y - h * 0.2), (x + w * 0.5, y - h * 0.2)], fill=(220, 190, 120), width=max(1, int(2 * zz)))
def handprint(d, x, y, zz, a=255):
    col = (90, 170, 70, a); dk = (40, 100, 30, a)
    d.ellipse([x - 16 * zz, y - 12 * zz, x + 16 * zz, y + 16 * zz], fill=col)
    for i, (fx, fl) in enumerate(((-15, 16), (-6, 22), (4, 23), (13, 19))):
        d.rounded_rectangle([x + fx * zz - 4 * zz, y - 12 * zz - fl * zz, x + fx * zz + 4 * zz, y - 8 * zz], int(4 * zz), fill=col)
    d.rounded_rectangle([x + 14 * zz, y - 4 * zz, x + 30 * zz, y + 4 * zz], int(4 * zz), fill=col)
    for i in range(5): d.point((x - 8 * zz + i * 4 * zz, y + 2 * zz), fill=dk)
def beam_target(tt):
    k = tt - THEFT
    if k < 1.2: u = ease(kk(k, 0, 1.2)); return lerp(1200, 900, u), lerp(600, 560, u)          # across the covered sofa
    if tt < TAKE + 0.2: u = ease(kk(k, 1.2, 1.8)); return lerp(900, BOOK[0], u), lerp(560, BOOK[1], u)
    if tt < PRINTT + 1.6: u = ease(kk(tt, TAKE + 0.2, PRINTT)); return lerp(BOOK[0], PRINT[0], u), lerp(BOOK[1], PRINT[1], u)
    u = kk(tt, PRINTT + 1.6, BEAM_OFF + 0.4); return lerp(PRINT[0], DOORL[0], u), lerp(PRINT[1], DOORL[1], u)
def darkness(fr, cam, tt):
    m = Image.new("L", fr.size, 70)
    if THEFT <= tt < BEAM_OFF + 0.4:
        X, Y = W2S(cam, *beam_target(tt)); R = 110 * cam[2]
        ImageDraw.Draw(m).ellipse([X - R, Y - R * 0.8, X + R, Y + R * 0.8], fill=240)
        m = m.filter(ImageFilter.GaussianBlur(R * 0.25))
    dark = ImageEnhance.Brightness(ImageChops.multiply(fr, Image.new("RGB", fr.size, (150, 165, 220)))).enhance(1.05)   # moonlit, readable on a phone
    lit = ImageChops.multiply(ImageEnhance.Brightness(fr).enhance(2.3), Image.new("RGB", fr.size, (255, 246, 220)))
    return Image.composite(lit, dark, m)
def hand(p, cam, tt):
    if not (TAKE - 0.7 <= tt < PRINTT + 0.6): return
    z = cam[2]
    if tt < TAKE: u = kk(tt, TAKE - 0.7, TAKE); tx, ty = BOOK
    elif tt < PRINTT: u = 1; tx, ty = lerp(BOOK[0], PRINT[0], kk(tt, TAKE, PRINTT)), lerp(BOOK[1], PRINT[1] + 8, kk(tt, TAKE, PRINTT))
    else: u = 1 - kk(tt, PRINTT + 0.1, PRINTT + 0.6); tx, ty = PRINT[0], PRINT[1] + 8
    sx, sy = W2S(cam, 200, 820); ex, ey = W2S(cam, tx, ty); hx, hy = lerp(sx, ex, u), lerp(sy, ey, u)
    p.line([(sx - 260 * z, sy + 160 * z), (hx, hy)], (92, 84, 120, 255), 24 * z)                    # sleeve readable in the dark
    p.ell(hx, hy, 15 * z, 12 * z, (235, 200, 170, 255), INK, 2 * z)
    if tt >= TAKE: p.rect(hx - 20 * z, hy - 30 * z, hx + 22 * z, hy - 6 * z, (120, 70, 36, 255), INK, 2 * z)     # notebook in hand

# ---------------- the letter (story) ----------------
LET_LINES = ["يا نعناعة…", "الكشكول اللي في شقتي", "فيه سر العمارة…", "محدش يفتحه غيرك.", "— رشدي"]
def letter_card(tt, Wd, Hd):
    u = tt - LET; vert = Hd > Wd
    fr = Image.new("RGB", (Wd, Hd), (24, 18, 14)); d = ImageDraw.Draw(fr, "RGBA")
    for i in range(0, Wd, 6): d.line([(i, 0), (i, Hd)], fill=(30 + (i * 7) % 9, 22, 16))               # wood desk
    z = 1.0 + 0.06 * kk(u, 0, 3.2); pw, ph = (860 * z, 1100 * z) if vert else (1000 * z, 760 * z)
    cx, cy = Wd / 2, Hd * (0.47 if vert else 0.5); rot = -2.5
    paper = Image.new("RGBA", (int(pw), int(ph)), (238, 224, 186, 255)); pd = ImageDraw.Draw(paper)
    for i in range(14): pd.line([(30, 120 + i * (ph - 160) / 14), (pw - 30, 120 + i * (ph - 160) / 14)], fill=(200, 184, 150, 255), width=2)
    pd.rectangle([0, 0, pw - 1, ph - 1], outline=(170, 140, 96, 255), width=8)
    f = ImageFont.truetype(CA, int((72 if vert else 62) * z)); fs = ImageFont.truetype(CA, int((60 if vert else 52) * z))
    shown = kk(u, 0.25, 2.3) * len(LET_LINES)
    for i, ln in enumerate(LET_LINES):
        if shown <= i: break
        part = ln[:max(1, int(len(ln) * min(1, shown - i)))]
        y = ph * 0.17 + i * ph * (0.15 if vert else 0.155)
        key = i in (1, 2)
        pd.text((pw * 0.9 if i < 4 else pw * 0.5, y), part, font=fs if i == 4 else f, fill=(150, 30, 30, 255) if key else (40, 30, 60, 255),
                anchor="rm" if i < 4 else "mm", direction="rtl", language="ar")
    paper = paper.rotate(rot, expand=True, resample=Image.BICUBIC)
    sh = Image.new("RGBA", paper.size, (0, 0, 0, 120)); fr.paste(sh, (int(cx - paper.size[0] / 2 + 16), int(cy - paper.size[1] / 2 + 20)), paper)
    fr.paste(paper, (int(cx - paper.size[0] / 2), int(cy - paper.size[1] / 2)), paper)
    by = 150 if vert else 70; d = ImageDraw.Draw(fr, "RGBA")                                                     # brand tag (story, not an ask)
    d.rounded_rectangle([Wd / 2 - 330, by - 42, Wd / 2 + 330, by + 42], 34, fill=(30, 110, 70, 235))
    lzt(fr, Wd / 2, by, "من أسرار «عمارة نعناعة»", 50, (255, 255, 255), (10, 40, 20))
    f2 = kk(u, 2.9, 3.2)
    if f2 > 0: fr = Image.blend(fr, Image.new("RGB", fr.size, (0, 0, 0)), f2)
    return fr

# ---------------- Tota's «proof» photo (the key clue) ----------------
def _clock_patch(sz):
    """a normal 8:45 clock, then the WHOLE clock (numbers + hands) mirrored as seen in the bathroom mirror.
    Mirrored result: minute hand points RIGHT (to the mirrored 9), hour hand just above it. Flip back = normal 8:45."""
    im = Image.new("RGBA", (sz, sz), (0, 0, 0, 0)); d = ImageDraw.Draw(im); c = sz / 2; R = sz * 0.46
    d.ellipse([c - R - 8, c - R - 8, c + R + 8, c + R + 8], fill=(150, 100, 50, 255))
    d.ellipse([c - R, c - R, c + R, c + R], fill=(250, 246, 232, 255), outline=(40, 30, 20, 255), width=4)
    f = ImageFont.truetype(DJ, int(sz * 0.16))
    for n, a in ((12, 0), (3, 90), (6, 180), (9, 270)):
        r_ = R * 0.74; x = c + math.sin(math.radians(a)) * r_; y = c - math.cos(math.radians(a)) * r_
        d.text((x, y), str(n), font=f, fill=(30, 30, 30, 255), anchor="mm")
    for i in range(12):
        if i % 3: a = i * math.pi / 6; d.line([(c + math.sin(a) * R * 0.8, c - math.cos(a) * R * 0.8), (c + math.sin(a) * R * 0.92, c - math.cos(a) * R * 0.92)], fill=(30, 30, 30, 255), width=4)
    m = 45; am = m / 60 * 2 * math.pi; ah = (8 + m / 60) / 12 * 2 * math.pi
    d.line([(c, c), (c + math.sin(ah) * R * 0.48, c - math.cos(ah) * R * 0.48)], fill=(20, 20, 20, 255), width=int(sz * 0.07))   # hour: short + thick
    d.line([(c, c), (c + math.sin(am) * R * 0.86, c - math.cos(am) * R * 0.86)], fill=(190, 30, 30, 255), width=int(sz * 0.032))  # minute: long + red
    d.ellipse([c - 7, c - 7, c + 7, c + 7], fill=(160, 30, 30, 255))
    return ImageOps.mirror(im)
def make_photo(PW=760, PH=1080):
    im = Image.new("RGB", (PW, PH), (196, 226, 232)); d = ImageDraw.Draw(im, "RGBA")
    for x in range(0, PW, 76): d.line([(x, 0), (x, PH)], fill=(170, 205, 214), width=3)                       # bathroom tiles
    for y in range(0, PH, 76): d.line([(0, y), (PW, y)], fill=(170, 205, 214), width=3)
    wx0, wy0, wx1, wy1 = 40, 70, 330, 380                                                                      # WINDOW: blue sky + sun = DAY
    d.rectangle([wx0, wy0, wx1, wy1], fill=(120, 190, 250));
    for i in range(10):
        a = i * math.pi / 5; d.line([(230, 170), (230 + math.cos(a) * 95, 170 + math.sin(a) * 95)], fill=(255, 230, 90), width=8)
    d.ellipse([190, 130, 270, 210], fill=(255, 214, 40)); d.ellipse([70, 270, 170, 320], fill=(255, 255, 255)); d.ellipse([110, 250, 200, 310], fill=(255, 255, 255))
    d.rectangle([wx0, wy0, wx1, wy1], outline=(250, 250, 250), width=14); d.line([((wx0 + wx1) / 2, wy0), ((wx0 + wx1) / 2, wy1)], fill=(250, 250, 250), width=10)
    d.line([(wx0, (wy0 + wy1) / 2), (wx1, (wy0 + wy1) / 2)], fill=(250, 250, 250), width=10)
    im.paste(ImageEnhance.Brightness(im.crop((0, 0, PW, PH))).enhance(1.0))
    ck = _clock_patch(270); im.paste(ck, (450, 70), ck)                                                       # the clock (reflected)
    lay = Image.new("RGBA", (int(PW * SS), int(PH * SS)), (0, 0, 0, 0)); p = P(lay)
    tx, ty = PW * 0.52, PH * 1.04
    draw_char(p, "tota", tx, ty, 3.4, "happy", 0.25, 1, False, "phone", 0.0, "phone", 0.0, None)
    L = lay.resize((PW, PH), Image.LANCZOS); im.paste(L, (0, 0), L)
    S, sh, (hx, hy) = body("tota", tx, ty, 3.4)                                                             # green clay face mask
    g = Image.new("L", im.size, 0); ImageDraw.Draw(g).ellipse([hx - 44 * S, hy - 24 * S, hx + 44 * S, hy + 44 * S], fill=150)
    im = Image.composite(Image.new("RGB", im.size, (110, 185, 80)), im, g.filter(ImageFilter.GaussianBlur(6)))
    d = ImageDraw.Draw(im, "RGBA")
    d.rectangle([0, 0, PW - 1, PH - 1], outline=(200, 170, 90), width=26)                                    # mirror frame
    d.line([(PW * 0.7, 60), (PW * 0.92, 300)], fill=(255, 255, 255, 90), width=12)                             # glass glare
    return im
PHOTO = make_photo()
def photo_overlay(fr, tt, Wd, Hd):
    if not (PH0 <= tt < PH1): return fr
    k = ease(kk(tt, PH0, PH0 + 0.25))                                                    # pops in, CLEAN cut out at PH1
    fr = ImageEnhance.Brightness(fr).enhance(1 - 0.6 * k).filter(ImageFilter.GaussianBlur(5 * k))
    vert = Hd > Wd; ph = (Hd * 0.62 if vert else Hd * 0.82) * (0.7 + 0.3 * k); pw = ph * 760 / 1080
    zoom = 1.0 + 0.08 * kk(tt, PH0 + 0.4, PH1)
    ph_img = PHOTO.resize((int(pw * zoom), int(ph * zoom)), Image.LANCZOS).crop((int(pw * (zoom - 1) / 2), int(ph * (zoom - 1) / 2), int(pw * (zoom - 1) / 2) + int(pw), int(ph * (zoom - 1) / 2) + int(ph)))
    cx, cy = Wd / 2, Hd * (0.42 if vert else 0.47)
    d = ImageDraw.Draw(fr, "RGBA"); bz = 26
    d.rounded_rectangle([cx - pw / 2 - bz, cy - ph / 2 - bz * 2.2, cx + pw / 2 + bz, cy + ph / 2 + bz * 2.2], int(bz * 2), fill=(20, 20, 26, int(255 * k)))
    if k > 0.05:
        fr.paste(ph_img, (int(cx - pw / 2), int(cy - ph / 2)))                       # always opaque: no double image
        lzt(fr, cx, cy - ph / 2 - bz * 3.4, "دليل توتة", int(58 * k), (255, 214, 90))
    return fr

# ---------------- people ----------------
def living_people(lay, cam, tt):
    k, lt = line_at(tt); ppl = []
    nx, ny, ns = POS["nana"]
    ppl.append(("nana", nx, ny, ns, "angry" if tt < ASK else "smug", 1, "paper" if k != "N2" else "point"))
    if tt >= SIN[0]:
        u = ease(kk(tt, *SIN)); ppl.append(("shatta", lerp(-120, POS["shatta"][0], u), POS["shatta"][1], 1.6, "scared", -1, "sandwich", tt * 8 if u < 1 else None))
    if tt >= TIN[0]:
        u = ease(kk(tt, *TIN)); ppl.append(("tota", lerp(2060, POS["tota"][0], u), POS["tota"][1], 1.6, "neutral", -1, "phone", tt * 8 if u < 1 else None))
    if tt >= BIN[0]:
        u = ease(kk(tt, *BIN)); ppl.append(("bondo2", lerp(2160, POS["bondo2"][0], u), POS["bondo2"][1], 1.6, "neutral", -1, None, tt * 7 if u < 1 else None))
    for row in ppl:
        who, x, y, s, ex, look, held = row[:7]; walk = row[7] if len(row) > 7 else None
        talking = k is not None and WHO.get(k) == who
        e = expr_of(k, lt) if talking else ex
        if who != "nana" and tt >= ASK: e = "scared" if who == "shatta" else ("neutral" if who == "tota" else "flat")
        mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
        if who == "nana":
            a = "talk" if talking else "hold"; h = "paper" if not (k == "N2") else None
            if k == "N2": a = "point"
            if k == "N1" and lt < 1.4: a = "up"
            look = 1
        else:
            a = "talk" if talking else ("down" if walk is None else "down"); h = held
            if who == "tota" and (k == "T1" and lt > 2.3): a = "phone"
            if who == "shatta": a = "hold" if not talking else "talk"
        X, Y_ = W2S(cam, x, y); S = s * cam[2]
        draw_char(P(lay), who, X, Y_, S, e, mouth, look, ((tt + len(who) * 0.37) % 3.6) < 0.11, a, tt, h, 0.0, walk)

def scene(tt, sh, cam, size):
    Wd, Hd = size; x0, y0, z = cam; set_ = sh["set"]
    src = APT if set_ == "apt" else RLIT
    box = (x0, y0, x0 + Wd / z, y0 + Hd / z)
    img = src.resize((int(Wd * SS), int(Hd * SS)), Image.BICUBIC, box=box)
    if z > 2.2: img = img.filter(ImageFilter.GaussianBlur(min(1.6, (z - 2.2) * 0.8)))
    zz = z * SS; QW = lambda x, y: ((x - x0) * zz, (y - y0) * zz); d = ImageDraw.Draw(img, "RGBA")
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); p = P(lay)
    if set_ == "apt":
        if tt < TAKE: b = QW(*BOOK); notebook(d, b[0], b[1], zz * 1.3)
        if tt >= PRINTT: q = QW(*PRINT); handprint(d, q[0], q[1], zz, int(255 * min(1, kk(tt, PRINTT, PRINTT + 0.15))))
        hand(p, cam, tt)
    else:
        living_people(lay, cam, tt)
    lay = tint_layer(lay, (235, 235, 255) if set_ == "apt" else (255, 240, 220)); img.paste(lay, (0, 0), lay)
    fr = img.resize((Wd, Hd), Image.LANCZOS)
    if set_ == "apt":
        if tt >= THEFT: fr = darkness(fr, cam, tt)
        else: fr = ImageEnhance.Brightness(fr).enhance(1.6)
        if H2 <= tt < THEFT:
            lzt(fr, Wd / 2, Hd * (0.78 if Hd > Wd else 0.84), "الدور السابع • ٨:٤٠ بالليل", int(64 * popk(tt, H2 + 0.15, 0.3)), (230, 230, 255))
        if PRINTT + 0.3 <= tt < BEAM_OFF:                                                   # a small ring pulse on the print (fair clue, no text)
            q = W2S(cam, *PRINT); r = (40 + 30 * ((tt - PRINTT) % 0.8) / 0.8) * z; a_ = int(200 * (1 - ((tt - PRINTT) % 0.8) / 0.8))
            ImageDraw.Draw(fr, "RGBA").ellipse([q[0] - r, q[1] - r, q[0] + r, q[1] + r], outline=(255, 255, 255, a_), width=max(2, int(3 * z)))
    return fr

# ---------------- cards ----------------
def prev_card(tt, Wd, Hd):
    """separate opening: «حل القضية السابقة» (case 10 → Aziza: TV dark + earring)"""
    vert = Hd > Wd; fr = Image.new("RGB", (Wd, Hd), (14, 24, 18)); rays(fr, Wd, Hd, (22, 40, 28), tt, 1, 0.55)
    d = ImageDraw.Draw(fr, "RGBA"); by = Hd * (0.16 if vert else 0.13); bh = 120 if vert else 100
    d.rectangle([0, by - bh / 2, Wd, by + bh / 2], fill=(30, 120, 60, 255)); lzt(fr, Wd / 2, by, "حل القضية السابقة", 80 if vert else 70, (255, 255, 255), (10, 40, 20))
    lay = Image.new("RGBA", (int(Wd * SS), int(Hd * SS)), (0, 0, 0, 0)); p = P(lay)
    k, lt = line_at(tt); op = float(ENV["T0"][min(int(lt * FPS) + 2, len(ENV["T0"]) - 1)]) if k == "T0" else 0.0
    ENG.AZIZA_EARS[:] = [1]
    rev = T("T0") + 1.85
    if vert:
        draw_char(p, "aziza", Wd * 0.68, Hd * 0.66, 2.6, "scared" if tt > rev else "smug", 0.0, -1, ((tt + 0.5) % 3.2) < 0.1, "scared" if tt > rev else "hips", tt, None, 0.0, None)
        draw_char(p, "tota", Wd * 0.28, Hd * 0.78, 2.2, expr_of(k, lt) if k else "smug", op, 1, False, "talk", tt, "nbpen", 0.0, None)
    else:
        draw_char(p, "aziza", Wd * 0.5, Hd * 1.02, 3.0, "scared" if tt > rev else "smug", 0.0, -1, ((tt + 0.5) % 3.2) < 0.1, "scared" if tt > rev else "hips", tt, None, 0.0, None)
        draw_char(p, "tota", Wd * 0.8, Hd * 1.0, 2.6, expr_of(k, lt) if k else "smug", op, -1, False, "talk", tt, "nbpen", 0.0, None)
    L = lay.resize((Wd, Hd), Image.LANCZOS); fr.paste(L, (0, 0), L); ENG.AZIZA_EARS[:] = [-1, 1]
    d = ImageDraw.Draw(fr, "RGBA")
    if tt >= T("T0") + 3.75:                                                                      # dark TV icon
        k2 = popk(tt, T("T0") + 3.75, 0.25); cx, cy = (Wd * 0.25, Hd * 0.36) if vert else (Wd * 0.22, Hd * 0.42); w, h = 150 * k2, 100 * k2
        d.rounded_rectangle([cx - w / 2 - 10, cy - h / 2 - 10, cx + w / 2 + 10, cy + h / 2 + 10], 12, fill=(50, 45, 40, 255)); d.rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], fill=(14, 16, 18))
    if tt >= T("T0") + 5.2:                                                                       # the earring
        k2 = popk(tt, T("T0") + 5.2, 0.25); cx, cy = (Wd * 0.25, Hd * 0.48) if vert else (Wd * 0.22, Hd * 0.7); r = 34 * k2
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(230, 190, 60, 255), width=max(2, int(9 * k2)))
        d.ellipse([cx - 11 * k2, cy + r - 11 * k2, cx + 11 * k2, cy + r + 11 * k2], fill=(210, 30, 40, 255))
    if tt >= T("T0") + 1.85:
        k2 = popk(tt, T("T0") + 1.85, 0.3); cx, cy = (Wd * 0.68, Hd * 0.27) if vert else (Wd * 0.5, Hd * 0.3); r = 50 * k2
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(40, 170, 80, 255), outline=(255, 255, 255, 255), width=5)
        d.line([(cx - r * 0.45, cy), (cx - r * 0.1, cy + r * 0.38), (cx + r * 0.5, cy - r * 0.35)], fill=(255, 255, 255, 255), width=max(4, int(r * 0.22)))
    f = kk(tt, PREV_END - 0.35, PREV_END)
    if f > 0: fr = Image.blend(fr, Image.new("RGB", fr.size, (0, 0, 0)), f)
    return fr

def q_card(tt, sh, Wd, Hd, base):
    fr = ImageEnhance.Brightness(base).enhance(0.38).filter(ImageFilter.GaussianBlur(6)).convert("RGB")
    vert = Hd > Wd; cy = Hd * (0.32 if vert else 0.3); g = 1.25 if vert else 1.0
    lzt(fr, Wd / 2, cy, "مين خد الكشكول؟", int(110 * g * popk(tt, sh["start"] + 0.05, 0.3)), (255, 214, 90))
    for i, (who, col) in enumerate(NUMS):
        bx = Wd / 2 + (i - 1) * 220 * g; badge(fr, bx, cy + 230 * g, str(i + 1), 1.3 * g * popk(tt, sh["start"] + 0.3 + i * 0.15), col)
        lzt(fr, bx, cy + 330 * g, NAME[who][0], int(54 * g * popk(tt, sh["start"] + 0.3 + i * 0.15)), (255, 255, 255))
    lzt(fr, Wd / 2, cy + (520 if vert else 450) * g, "اكتب رقم الكداب 👇".replace(" 👇", ""), int(62 * g * popk(tt, sh["start"] + 0.8)), (255, 255, 255))
    return fr

# ---------------- frames ----------------
_FREEZE = {}
def tag(fr, Wd, Hd, tt):
    if tt < LET or tt >= Q or PH0 <= tt < PH1 or shot_at(tt)["set"] == "letter": return
    d = ImageDraw.Draw(fr, "RGBA"); vert = Hd > Wd; x, y = (Wd / 2, 200) if vert else (Wd - 150, 60)
    d.rounded_rectangle([x - 115, y - 32, x + 115, y + 32], 26, fill=(200, 30, 40, 220)); lzt(fr, x, y, "قضية 11", 44, (255, 255, 255), stroke=False)
def add_overlays(fr, tt, sh, Wd, Hd, cam):
    if sh["set"] != "living" or tt < BADGES: return
    for i, (who, col) in enumerate(NUMS):
        x, y, s = POS[who]; S_, _, (_, hy2) = body(who, x, y, s); q = W2S(cam, x, hy2 - 46 * S_ - 40)
        if -120 < q[0] < Wd + 120:
            badge(fr, q[0], max(q[1], 110 if Hd < Wd else 330), str(i + 1), min(1.1, cam[2] * 0.5) * popk(tt, BADGES + i * 0.15), col)
def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "prev": return finish(prev_card(tt, W, H), tt)
    if sh["set"] == "letter": return finish(letter_card(tt, W, H), tt)
    if sh["set"] == "q":
        if "h" not in _FREEZE: ps = shots[shots.index(sh) - 1]; _FREEZE["h"] = scene(sh["start"] - 0.05, ps, hcam(ps, sh["start"] - 0.05), (W, H))
        return finish(q_card(tt, sh, W, H, _FREEZE["h"]), tt)
    cam = hcam(sh, tt); fr = scene(tt, sh, cam, (W, H)); add_overlays(fr, tt, sh, W, H, cam)
    fr = photo_overlay(fr, tt, W, H); tag(fr, W, H, tt)
    return finish(fr, tt)
def subtitle(img, tt):
    if shot_at(tt)["set"] != "q": sub_chunk(img, tt, W / 2, H - 80, 62)
VIGV = VIG.resize((1080, 1920))
def vertical(_base, tt):
    sh = shot_at(tt); Wd, Hd = 1080, 1920
    if sh["set"] == "prev": fr = prev_card(tt, Wd, Hd); sub_chunk(fr, tt, 520, 1560, 72); return fr
    if sh["set"] == "letter": return letter_card(tt, Wd, Hd)
    if sh["set"] == "q":
        if "v" not in _FREEZE: ps = shots[shots.index(sh) - 1]; _FREEZE["v"] = scene(sh["start"] - 0.05, ps, vcam(ps, sh["start"] - 0.05), (Wd, Hd))
        return q_card(tt, sh, Wd, Hd, _FREEZE["v"])
    cam = vcam(sh, tt); fr = scene(tt, sh, cam, (Wd, Hd)); add_overlays(fr, tt, sh, Wd, Hd, cam)
    fr = ImageChops.multiply(fr, VIGV)
    u = tt - sh["start"]
    if sh.get("tin") in ("whip", "whipl") and u < 0.18: fr = fr.filter(ImageFilter.BoxBlur(int(2 + 18 * (1 - u / 0.18))))
    fr = photo_overlay(fr, tt, Wd, Hd); tag(fr, Wd, Hd, tt); sub_chunk(fr, tt, 500, 1560 if PH0 <= tt < PH1 else 1470, 76)
    return fr

# ---------------- audio ----------------
def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def creak(dur=0.9, amp=0.22):
    n = int(SR * dur); t_ = np.arange(n) / SR; f = 160 + 80 * np.sin(t_ * 9) + 40 * np.sin(t_ * 31)
    x = np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * (0.5 + 0.5 * np.abs(np.sin(t_ * 47)))
    return (lowpass(x.astype(np.float32), 1600) * np.hanning(n) * amp).astype(np.float32)
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 3; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(11)
    for k_, f in enumerate((523, 659, 784)): mix_into(buf, tone(f, 0.5, 0.16, 7), 0.05 + k_ * 0.08, 1.0)         # frame-1 sting
    mix_into(buf, tone(1047, 0.6, 0.14, 6), T("T0") + 1.85, 1.0)                                            # ✓
    dr = np.arange(int((Q - PREV_END) * SR)) / SR
    drone = (np.sin(2 * np.pi * 55 * dr) * 0.05 + np.sin(2 * np.pi * 82.5 * dr) * 0.028) * (0.7 + 0.3 * np.sin(dr * 0.8))
    mix_into(buf, drone.astype(np.float32), PREV_END, 1.0)
    pap = lowpass(r.normal(0, 1, int(SR * 0.5)).astype(np.float32), 5000) * np.hanning(int(SR * 0.5)).astype(np.float32) * 0.09
    mix_into(buf, pap, LET + 0.05, 1.0)                                                                     # paper rustle
    for j in range(16): mix_into(buf, tone(3000 + (j % 3) * 150, 0.02, 0.035, 90), LET + 0.3 + j * 0.12, 1.0)  # pen scratch
    mix_into(buf, lowpass(r.normal(0, 1, int((THEFT + 5.0 - H2) * SR)).astype(np.float32), 400) * 0.03, H2, 1.0)   # wind in the dusty flat
    mix_into(buf, creak(1.1, 0.24), H2 + 0.2, 1.0)                                                         # the old door
    mix_into(buf, SFXF["switch"] * 0.5, THEFT + 0.05, 1.0)                                                 # torch click
    mix_into(buf, SFXF["stinger"] * 0.35, TAKE, 1.0)
    for j in range(4): mix_into(buf, tone(140, 0.08, 0.1, 30), THEFT + 0.4 + j * 0.45, 1.0)               # careful footsteps
    mix_into(buf, tone(220, 0.5, 0.14, 5) + tone(330, 0.5, 0.1, 5), PRINTT + 0.2, 1.0)                      # «dun» on the print
    mix_into(buf, SFXF["gasp"] * 0.25, T("N1") - 0.15, 1.0)
    for i in range(3): mix_into(buf, tone(660 + i * 220, 0.18, 0.18, 12), BADGES + i * 0.15, 1.0)
    mix_into(buf, tone(1800, 0.12, 0.2, 20) + tone(2400, 0.12, 0.12, 20), PH0 + 0.05, 1.0)                  # camera «click»
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), Q + k_ * 0.09, 1.0)
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > PREV_END: mix_into(buf, SFXF["whoosh"] * 0.18, s_["start"] - 0.1, 1.0)
    for st_, k in lines:
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8; mix_into(buf, v, st_, 1.0)
    write_wav(buf[:int(TOTAL * SR)], path)

def make_covers():
    def comp(Wd, Hd, vert):
        bgc = ImageEnhance.Brightness(APT.crop((300, 200, 1500, 1000)).resize((Wd, Hd), Image.LANCZOS).filter(ImageFilter.GaussianBlur(5))).enhance(1.15)
        img = bgc.resize((int(Wd * SS), int(Hd * SS))); d = ImageDraw.Draw(img, "RGBA")
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); p = P(lay)
        if vert:
            notebook(d, Wd * 0.68 * SS, Hd * 0.4 * SS, 4.2 * SS, -0.2); handprint(d, Wd * 0.8 * SS, Hd * 0.25 * SS, 3.2 * SS)
            draw_char(p, "nana", Wd * 0.34, Hd * 0.82, 4.3, "shock", 0.6, 1, False, "up", 0.0, None, 0.0, None)
            for i, (who, col) in enumerate(NUMS): draw_char(p, who, Wd * (0.2 + 0.3 * i), Hd * 1.08, 2.3, "flat", 0.0, -1, False, "down", 0.0, None, 0.0, None)
        else:
            notebook(d, Wd * 0.74 * SS, Hd * 0.5 * SS, 4.6 * SS, -0.2); handprint(d, Wd * 0.88 * SS, Hd * 0.3 * SS, 3.4 * SS)
            draw_char(p, "nana", Wd * 0.3, Hd * 1.3, 5.2, "shock", 0.6, 1, False, "up", 0.0, None, 0.0, None)
        img.paste(lay, (0, 0), lay); fr = img.resize((Wd, Hd), Image.LANCZOS); d = ImageDraw.Draw(fr, "RGBA")
        if vert:
            d.rectangle([0, Hd * 0.535, Wd, Hd * 0.725], fill=(10, 6, 4, 150))
            lzt(fr, Wd / 2, Hd * 0.575, "مين خد", 160, (255, 255, 255)); lzt(fr, Wd / 2, Hd * 0.67, "كشكول رشدي؟", 150, (255, 214, 60))
            for i, (who, col) in enumerate(NUMS): badge(fr, Wd * (0.2 + 0.3 * i), Hd * 0.765, str(i + 1), 1.2, col)
            bx, by = Wd / 2, 130
        else:
            d.rectangle([0, Hd * 0.76, Wd, Hd * 0.97], fill=(10, 6, 4, 150)); lzt(fr, Wd * 0.58, Hd * 0.865, "مين خد كشكول رشدي؟", 140, (255, 214, 60)); bx, by = 1620, 90
        d = ImageDraw.Draw(fr, "RGBA"); d.rounded_rectangle([bx - 200, by - 46, bx + 200, by + 46], 34, fill=(200, 30, 40, 240))
        lzt(fr, bx, by, "مين الكداب؟ • قضية 11", 42, (255, 255, 255), stroke=False)
        return fr
    comp(1080, 1920, True).save(ROOT + "/publish/thumbs/kaddab_e11_cover.jpg", quality=92)
    comp(1920, 1080, False).resize((1280, 720), Image.LANCZOS).save(ROOT + "/publish/thumbs/kaddab_e11_yt.jpg", quality=92)

if __name__ == "__main__":
    print("TOTAL", round(TOTAL, 1))
    if sys.argv[1:2] == ["stills"]: render(None, None, [float(v) for v in sys.argv[2:]])
    elif sys.argv[1:2] == ["times"]:
        for s_ in shots: print(s_["set"], round(s_["start"], 2), round(s_["end"], 2), s_.get("tin", ""))
        for st, k in lines: print(k, round(st, 2))
        print("PH", round(PH0, 2), round(PH1, 2), "TAKE", round(TAKE, 2), "PRINT", round(PRINTT, 2))
    elif sys.argv[1:2] == ["part"]:
        i, n = int(sys.argv[2]), int(sys.argv[3]); a = round(TOTAL * i / n * FPS) / FPS; b = round(TOTAL * (i + 1) / n * FPS) / FPS
        render(f"h_{i}.mp4", f"v_{i}.mp4", None, a, b)
    elif sys.argv[1:2] == ["audio"]: build_audio()
    elif sys.argv[1:2] == ["cover"]: make_covers()
