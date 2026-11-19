# «ترند الأسبوع» 02 — «م.م» (مقابلة شغل)  (H 1920x1080 + V 1080x1920 in one pass) — user approved 17/11, voices 19/11
# Zalata = HR manager behind the desk (glasses, serious → fed up). Shatta = grinning candidate: every answer is «م.م يا فندم».
# Punchline: «عندك م.م» → «مجنون مية مية!» → CU Shatta's frozen grin + audience laugh (sound only, no laugh text).
# NEW canonical location «مكتب الشركة» trend/02/bg/office.png (door left, water cooler, certificate, clock, blinds window, cabinet).
#   The desk + chair + papers are drawn in code (DESK below) — reuse the same numbers in later episodes.
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/trend/02")
SERIES = "ترند الأسبوع"; EPT = "م.م"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"
SFXF = {"whoosh": load_audio(ROOT + "/trend/01/sfx/whoosh.mp3"), "press": load_audio(ROOT + "/trend/01/sfx/press.mp3")}

SUB = {"L01": "اسمك إيه؟", "L02": "م.م يا فندم.", "L03": "بالكامل لو سمحت.", "L04": "محمد منصور.",
       "L05": "اسم الوالد؟", "L06": "م.م يا فندم!", "L07": "يعني إيه؟", "L08": "منصور محمود.",
       "L09": "مؤهلك إيه؟", "L10": "م.م يا فندم.", "L11": "وده إيه؟", "L12": "ماجستير محاسبة.",
       "L13": "طب ليه عايز الوظيفة دي؟", "L14": "عشان م.م يا فندم.", "L15": "وده إيه بقى؟", "L16": "مشاكل مادية.",
       "L17": "تمام... هنبقى نكلمك.", "L18": "طب يا فندم... أدائي كان عامل إزاي؟",
       "L19": "بصراحة... أنا شايف إن عندك م.م", "L20": "يعني إيه يا فندم؟", "L21": "مجنون مية مية!", "GROUP": ""}
Z_LINES = {"L01", "L03", "L05", "L07", "L09", "L11", "L13", "L15", "L17", "L19", "L21"}
WHO = {k: ("zalata" if k in Z_LINES else "shatta") for k in SUB}; WHO["GROUP"] = "-"
EXPR = {"L01": "flat", "L02": "happy", "L03": "flat", "L04": "happy", "L05": "flat", "L06": "happy", "L07": "shock",
        "L08": "happy", "L09": "flat", "L10": "happy", "L11": "angry", "L12": "happy", "L13": "sad", "L14": "happy",
        "L15": "angry", "L16": "happy", "L17": "flat", "L18": "happy", "L19": "smug", "L20": "happy", "L21": "smug", "GROUP": "laugh"}
MM = {"L02", "L06", "L10", "L14"}
load_lines(list(SUB))
OFFICE = _ld(ROOT + "/trend/02/bg/office.png")

# ---------------- staging (world = office 1920x1080) ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
ZL = (1300, 900, 2.0)        # Zalata seated behind the desk, facing left (hip on his chair)
SH = (640, 900, 2.0)         # Shatta seated on the visitor chair, facing right
DESK = (930, 1600, 830)      # desk x0, x1, top y (in front of Zalata)
def head_of(who, x, y, s, sit=1):
    S = s * CH[who]["scale"]
    if sit: y = y + 62 * S
    sh = y - 134 * S; return S, sh, (x, sh - 56 * S)
_, _, ZH = head_of("zalata", *ZL); _, _, SHH = head_of("shatta", *SH)

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
WIDE = (980, 640, 1.18)
CUZ = lambda z=2.6, dy=0: (ZH[0] - 40, ZH[1] + 60 + dy, z)
CUS = lambda z=2.6, dy=0: (SHH[0] + 60, SHH[1] + 30 + dy, z)
t = 0.0
SITDOWN = 0.0
shot("o", 0.0, 1.2, WIDE, (990, 650, 1.25))                                              # wide: he's just sat down, grinning
t = say(0.3, "L01") + 0.12
gap = {"S": 0.12, "Z": 0.16}
plan = [("L02", "S", 2.6, "whipl"), ("L03", "Z", 2.5, "whip"), ("L04", "S", 2.5, "whipl"), ("L05", "Z", 2.3, "whip"),
        ("L06", "S", 2.9, "whipl"), ("L07", "Z", 2.9, "whip"), ("L08", "S", 2.5, "whipl"), ("L09", "W", 1.3, "whip"),
        ("L10", "S", 3.1, "whipl"), ("L11", "Z", 2.7, "whip"), ("L12", "S", 2.5, "whipl"), ("L13", "Z", 2.3, "whip"),
        ("L14", "S", 3.0, "whipl"), ("L15", "Z", 3.2, "whip"), ("L16", "S", 2.6, "whipl"), ("L17", "F", 0, "zoom"),
        ("L18", "W", 1.3, "whipl"), ("L19", "Z", 2.4, "whip"), ("L20", "S", 2.6, "whipl"), ("L21", "Z", 3.3, "whip")]
shots[-1]["end"] = T("L01") - 0.0 + DUR["L01"] + 0.12 if False else shots[-1]["end"]
shot("o", 1.2, t, (ZH[0] - 40, ZH[1] + 70, 2.3), (ZH[0] - 40, ZH[1] + 66, 2.45), tin="whip")       # L01 on Zalata
STAMP = None
for k, who, z, tin in plan:
    s = t; t = say(t + 0.06, k) + (gap["S"] if who == "S" else gap["Z"])
    if who == "S": shot("o", s, t, CUS(z), CUS(z + 0.12, -4), tin=tin, ease="crash" if k in MM else None)
    elif who == "Z": shot("o", s, t, CUZ(z), CUZ(z + 0.15, -4), tin=tin, ease="crash" if k == "L21" else None)
    elif who == "W": shot("o", s, t, WIDE, (980, 640, 1.3), tin=tin)
    elif who == "F": STAMP = T(k) + DUR[k] - 0.3; shot("form", s, t + 0.35, None, tin=tin); t += 0.35
REACT = t; shot("o", t, t + 1.0, CUS(2.8), CUS(3.2, -8), tin="whip", ease="crash")              # Shatta: frozen grin
LAUGH = t + 0.55; say(LAUGH, "GROUP"); LU = min(3.0, DUR["GROUP"])
shot("o", t + 1.0, LAUGH + LU, CUS(3.2, -8), CUS(3.3, -10))
t = LAUGH + LU; FREEZE = t - 0.2
shot("end", t, t + 2.4, None); t += 2.4
TOTAL = t

# ---------------- drawing ----------------
def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, held=None, sit=0, nod=0.0):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    blink = ((tt + len(who) * 0.37) % 3.6) < 0.11 and expr not in ("laugh", "shock", "gasp")
    if not talking: lean += math.sin(tt * 1.7 + len(who)) * 0.04
    X, Y_ = W2S(cam, x, y); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, held, lean, None, sit=sit, nod=nod)

def chair(p, cam, x, y, s, face):
    z = cam[2]; k = s * z
    a = W2S(cam, x - 40 * face * s, y - 95 * s); b = W2S(cam, x - 28 * face * s, y + 8 * s)
    p.rect(min(a[0], b[0]), a[1], max(a[0], b[0]), b[1], (40, 40, 46, 255), INK, 2 * z, 4 * z)          # backrest
    a = W2S(cam, x - 44 * s, y); b = W2S(cam, x + 44 * s, y + 12 * s); p.rect(a[0], a[1], b[0], b[1], (40, 40, 46, 255), INK, 2 * z, 4 * z)
    q = W2S(cam, x, y + 12 * s); r = W2S(cam, x, y + 58 * s); p.line([q, r], (60, 60, 66, 255), 5 * k)
    for dx in (-30, 30):
        r2 = W2S(cam, x + dx * s, y + 66 * s); p.line([r, r2], (60, 60, 66, 255), 4 * k)

def desk(p, cam, tt):
    z = cam[2]; x0, x1, ty = DESK
    a = W2S(cam, x0 - 20, ty - 24); b = W2S(cam, x1 + 20, ty); p.rect(a[0], a[1], b[0], b[1], (122, 84, 50, 255), INK, 3 * z, 3 * z)
    a = W2S(cam, x0, ty); b = W2S(cam, x1, 1120); p.rect(a[0], a[1], b[0], b[1], (96, 64, 36, 255), INK, 3 * z, 2 * z)
    a = W2S(cam, x0 + 40, ty + 40); b = W2S(cam, x1 - 40, 1100); p.rect(a[0], a[1], b[0], b[1], (84, 54, 30, 255), INK, 2 * z, 3 * z)
    # name plate «شؤون الموظفين»
    a = W2S(cam, 1180, ty - 24); p.poly([(a[0], a[1]), (a[0] + 200 * z, a[1]), (a[0] + 186 * z, a[1] - 34 * z), (a[0] + 14 * z, a[1] - 34 * z)], (30, 30, 34, 255), INK, 2 * z)
    # papers + pen + mug
    a = W2S(cam, 1000, ty - 24); p.poly([(a[0], a[1]), (a[0] + 150 * z, a[1]), (a[0] + 140 * z, a[1] - 8 * z), (a[0] + 6 * z, a[1] - 8 * z)], (245, 245, 240, 255), INK, 1.5 * z)
    a = W2S(cam, 1450, ty - 24); p.rect(a[0], a[1] - 44 * z, a[0] + 34 * z, a[1], (200, 60, 50, 255), INK, 2 * z, 4 * z)
    p.ell(a[0] + 40 * z, a[1] - 24 * z, 9 * z, 12 * z, None, INK, 3 * z)

def nameplate_text(fr, cam):
    z = cam[2]; a = W2S(cam, 1280, DESK[2] - 41)
    if z > 0: lzt(fr, a[0], a[1], "شؤون الموظفين", int(17 * z), (230, 210, 150), stroke=False)

def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255, rot=0, stroke=True):
    if size < 4: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(LZ, size)
    if stroke: d.text((x, y), s, font=f, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), anchor="mm", direction="rtl", language="ar")
    d.text((x, y), s, font=f, fill=fill + (alpha,), anchor="mm", direction="rtl", language="ar")
    if rot: lay = lay.rotate(rot, center=(x, y), resample=Image.BICUBIC)
    img.paste(lay, (0, 0), lay)
def popk(tt, t0, d=0.22):
    u = kk(tt, t0, t0 + d); return 0 if u <= 0 else (1 + 0.25 * math.sin(u * math.pi)) if u < 1 else 1

def sweat(fr, cam, who, x, y, s, tt, t0):
    if tt < t0: return
    z = cam[2]; d = ImageDraw.Draw(fr, "RGBA"); S, sh, (hx, hy) = head_of(who, x, y, s)
    for i, (dx, ph) in enumerate(((-40, 0.0), (38, 0.5))):
        u = (tt * 0.8 + ph) % 1.0; q = W2S(cam, hx + dx * S, hy - 22 * S + u * 46 * S); r = 5 * S * z
        d.ellipse([q[0] - r, q[1] - r * 1.5, q[0] + r, q[1] + r * 1.5], fill=(190, 225, 255, int(230 * (1 - u))), outline=(60, 110, 170, int(255 * (1 - u))), width=2)

def mm_pop(fr, cam, tt):
    """a big «م.م» badge bounces next to Shatta every time he says it"""
    for k in MM:
        t0 = T(k); t1 = t0 + DUR[k] + 0.25
        if not (t0 + 0.05 <= tt < t1): continue
        sc = popk(tt, t0 + 0.05, 0.25) * (1 - kk(tt, t1 - 0.2, t1))
        S, sh, (hx, hy) = head_of("shatta", *SH); q = W2S(cam, hx + 140 * S, hy + 5 * S)
        x = max(140, min(W - 140, q[0])); y = max(200, min(H - 300, q[1]))
        d = ImageDraw.Draw(fr, "RGBA"); sc *= 1.25; r = 95 * sc
        d.ellipse([x - r, y - r * 0.75, x + r, y + r * 0.75], fill=(255, 214, 90, 255), outline=(45, 12, 8, 255), width=max(1, int(7 * sc)))
        lzt(fr, x, y + 4, "م.م", int(96 * sc), (200, 30, 40), (255, 255, 255), rot=-6)

_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/trend/02")

def office_frame(tt, sh):
    cam = cam_at(sh, tt); z = cam[2]
    img = bg_crop(OFFICE, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    # Zalata (behind the desk)
    k, _ = line_at(tt)
    zex = "flat"
    if tt >= T("L07"): zex = "shock" if tt < T("L08") else "flat"
    if tt >= T("L11"): zex = "angry"
    if tt >= T("L17"): zex = "flat"
    if tt >= T("L19"): zex = "smug"
    zarms = "talk" if WHO.get(k) == "zalata" else "clap2"
    if T("L09") <= tt < T("L09") + DUR["L09"] + 0.8: zarms = ("talk", "salute", kk(tt, T("L09"), T("L09") + 0.3))   # scratches his head
    if T("L05") <= tt < T("L05") + DUR["L05"]: zarms = "hold"                                                     # writing
    chair(p, cam, ZL[0] + 20, ZL[1], 2.0, -1)
    person(lay, cam, "zalata", *ZL, tt, zex, -1, zarms, 0.08 if tt >= T("L19") else 0.0, sit=-1)
    desk(p, cam, tt)
    # Shatta (visitor chair, in front-left)
    chair(p, cam, SH[0] - 20, SH[1], 2.0, 1)
    sex = "happy"
    if tt >= REACT: sex = "happy"
    sarms = "talk" if WHO.get(k) == "shatta" else "clap"
    person(lay, cam, "shatta", *SH, tt, sex, 1, sarms, 0.0, sit=1)
    lay = tint_layer(lay, (240, 240, 236)); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    nameplate_text(fr, cam)
    mm_pop(fr, cam, tt)
    if tt >= REACT + 0.35: sweat(fr, cam, "shatta", *SH, tt, REACT + 0.35)
    return fr

def make_form():
    w, h = 900, 760; im = Image.new("RGB", (w, h), (250, 250, 244)); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, w - 1, h - 1], outline=(60, 60, 70), width=8)
    f1 = ImageFont.truetype(LZ, 64); f2 = ImageFont.truetype(LZ, 58)
    d.text((w / 2, 70), "استمارة مقابلة", font=f1, fill=(40, 40, 60), anchor="mm", direction="rtl", language="ar")
    for i, lab in enumerate(("الاسم:", "اسم الوالد:", "المؤهل:", "السبب:")):
        y = 190 + i * 125
        d.text((w - 70, y), lab, font=f2, fill=(40, 40, 60), anchor="rm", direction="rtl", language="ar")
        d.line([(80, y + 38), (w - 340, y + 38)], fill=(170, 170, 190), width=3)
        d.text((330, y), "م.م", font=f2, fill=(30, 70, 200), anchor="mm", direction="rtl", language="ar")
    return im
FORM = make_form()

def form_frame(tt, sh):
    u = kk(tt, sh["start"], sh["end"])
    cam = (ZH[0] - 960 / 2.2, ZH[1] - 380, 2.2)
    fr = bg_crop(OFFICE, (max(0, cam[0]), max(0, min(1080 - 1080 / 2.2, cam[1])), 2.2)).resize((W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(12))
    fr = ImageEnhance.Brightness(fr).enhance(0.55)
    zz = 1.0 + 0.06 * u; fw, fh = int(1000 * zz), int(1000 * zz * 760 / 900)
    im = FORM.resize((fw, fh), Image.LANCZOS).convert("RGBA").rotate(-2 + u * 2, expand=True, resample=Image.BICUBIC)
    fr.paste(im, (int(W / 2 - im.size[0] / 2), int(H / 2 - im.size[1] / 2 + 10)), im)
    if tt >= STAMP:                                                                              # «مرفوض» stamp slams on «هنبقى نكلمك»
        sc = 1.6 - 0.6 * min(1, kk(tt, STAMP, STAMP + 0.12))
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        f = ImageFont.truetype(LZ, int(150 * sc)); cx, cy = W / 2 + 120, H / 2 + 60
        d.rounded_rectangle([cx - 270 * sc, cy - 110 * sc, cx + 270 * sc, cy + 110 * sc], int(24 * sc), outline=(210, 30, 40, 235), width=int(14 * sc))
        d.text((cx, cy + 6 * sc), "مرفوض", font=f, fill=(210, 30, 40, 235), anchor="mm", direction="rtl", language="ar")
        lay = lay.rotate(12, center=(cx, cy), resample=Image.BICUBIC); fr.paste(lay, (0, 0), lay)
    return fr

_FC = {}
def frame_cache(t_):
    if t_ not in _FC: _FC[t_] = frame(t_)
    return _FC[t_]
def endcard(tt, sh):
    k = kk(tt, sh["start"], sh["start"] + 0.4)
    fr = ImageEnhance.Brightness(frame_cache(FREEZE)).enhance(1 - 0.55 * k).filter(ImageFilter.GaussianBlur(6 * k)).convert("RGBA")
    sc = popk(tt, sh["start"] + 0.1, 0.3)
    if sc > 0: lzt(fr, W / 2, 400, "منشن صاحبك اللي عنده م.م!", int(100 * sc), (255, 214, 90))
    if tt >= sh["start"] + 0.5:
        logo(fr, W / 2, 680, 130); text(fr, W / 2, 830, "@shattawzalata", 52, (255, 214, 90))
    return fr.convert("RGB")

HOOK = "مقابلة شغل… وكل إجابة عنده «م.م»!"
def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "end": return finish(endcard(tt, sh), tt)
    fr = form_frame(tt, sh) if sh["set"] == "form" else office_frame(tt, sh)
    if tt < 3.0:
        a_ = int(255 * min(1, (3.0 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([W / 2 - 700, 40, W / 2 + 700, 150], 30, fill=(20, 12, 8, int(a_ * 0.8)))
        lzt(fr, W / 2, 95, HOOK, 68, (255, 214, 90), alpha=a_)
    return finish(fr, tt)

def vertical(fr, tt):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = ImageEnhance.Brightness(small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.35)
    bgv.paste(fr.resize((1080, 608), Image.LANCZOS), (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(255, 214, 90)); d.rectangle([0, 1168, 1080, 1171], fill=(255, 214, 90))
    lzt(bgv, 540, 250, "مقابلة شغل", 110, (255, 255, 255))
    lzt(bgv, 540, 400, "وكل إجابة: م.م!", 104, (255, 214, 90))
    lzt(bgv, 540, 1840, SERIES, 44, (255, 150, 110))
    k, _ = line_at(tt)
    if k and SUB.get(k):
        for i, l in enumerate(wrap(SUB[k])[:4]): text(bgv, 540, 1300 + i * 84, l, 66, sw=6)
    return bgv

def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(71)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 260) * 0.018, 0, 1.0)                   # office air
    for j in range(int(TOTAL)):                                                                         # wall clock tick
        mix_into(buf, tone(2600, 0.02, 0.035, 80), 0.2 + j, 1.0)
    for k in MM: mix_into(buf, tone(1046, 0.16, 0.16, 12) + tone(1318, 0.16, 0.12, 12), T(k) + 0.08, 1.0)   # «ding» on every م.م
    mix_into(buf, tone(120, 0.25, 0.4, 14), STAMP, 1.0); mix_into(buf, lowpass(r.normal(0, 1, int(SR * 0.12)).astype(np.float32), 900) * 0.35, STAMP, 1.0)   # STAMP
    mix_into(buf, tone(160, 0.5, 0.25, 5) + tone(110, 0.5, 0.25, 5), REACT, 1.0)
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 0.5: mix_into(buf, SFXF["whoosh"] * 0.16, s_["start"] - 0.1, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), TOTAL - 2.3 + k_ * 0.09, 1.0)
    rms = lambda x: float(np.sqrt(np.mean(x ** 2))) + 1e-9; ref = []
    for st, k in lines:
        if k == "GROUP": continue
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8; ref.append(rms(v)); mix_into(buf, v, st, 1.0)
    g = AUD["GROUP"][:int(SR * LU)].copy(); g[-int(SR * 0.4):] *= np.linspace(1, 0, int(SR * 0.4))
    mix_into(buf, g / rms(g) * float(np.mean(ref)) * 1.2, LAUGH, 1.0)
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
