# «يوميات شطة وزلطة» — «راجل البيت» (user idea 21/11) — FIRST video under docs/growth_rules.md:
#   • frame 1 = motion + sound (no static cover)   • NATIVE 9:16 vertical (own cameras, characters fill the screen)
#   • short phrase-synced subtitles with a yellow key word, safe zones   • hook title 3 s only, then a small tag   • share CTA end card
# Bandaq clings to the window grille in «أوضة بندق وعزيزة» (canonical bg, window top-right), Aziza below with the slipper.
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/daily/16")
SERIES = "يوميات شطة وزلطة"; EPT = "راجل البيت"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"
SFXF = {"whoosh": load_audio(ROOT + "/trend/01/sfx/whoosh.mp3")}
SUB = {"A1": "انزل يا بندق!", "B1": "مش… مش نازل!", "A2": "بقولّك انزل!",
       "B2": "إنتي ما بتفهميش ولا إيه؟ أنا راجل البيت… وأنا اللي أقرر إمتى أنزل… وإمتى ما أنزلش!", "GROUP": ""}
# phrase chunks for the vertical subtitles: (offset s, text, yellow key word)
CHUNKS = {"A1": [(0.0, "انزل يا بندق!", "انزل")], "B1": [(0.0, "مش…", None), (0.8, "مش نازل!", "نازل")],
          "A2": [(0.0, "بقولّك انزل!", "انزل")],
          "B2": [(0.0, "إنتي ما بتفهميش ولا إيه؟", None), (2.45, "أنا راجل البيت…", "راجل البيت"),
                 (4.25, "وأنا اللي أقرر إمتى أنزل…", "أقرر"), (6.5, "وإمتى ما أنزلش!", "ما أنزلش")]}
WHO = {"A1": "aziza", "A2": "aziza", "B1": "bondo2", "B2": "bondo2", "GROUP": "-"}
EXPR = {"A1": "angry", "A2": "angry", "B1": "scared", "B2": [(0, "smug"), (0.8, "scared")], "GROUP": "laugh"}
load_lines(list(SUB))
ROOM = _ld(ROOT + "/daily/bg/bandaq_room.png")

# ---------------- staging (world = room 1920x1080) ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
AZ = (1560, 1012, 1.75)
def body(who, x, y, s):
    S = s * CH[who]["scale"]; sh = y - 134 * S; return S, sh, (x, sh - 56 * S)
_Sb = 1.5 * CH["bondo2"]["scale"]
BQ = (1790, 190 + 186 * _Sb, 1.5)          # feet y so that his raised hands grab the window sill/grille at y≈190

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
# each shot: H camera (center form) + "v" = vertical camera (center x, center y, px-per-world-unit)
CU_AZ_H, CU_AZ_V = (1560, 690, 2.4), (1560, 700, 2.55)
CU_BQ_H, CU_BQ_V = (1790, 300, 2.5), (1800, 330, 2.6)
WIDE_H, WIDE_V = (1440, 540, 1.35), (1640, 540, 1.78)
t = say(0.1, "A1"); shakes.append((0.15, 16))
shot("room", 0.0, t + 0.1, (1560, 700, 2.9), CU_AZ_H, ease="crash", v=((1560, 720, 3.1), CU_AZ_V))          # frame 1: crash-in on her
s = t + 0.1; t = say(s + 0.05, "B1") + 0.1
shot("room", s, t, (1790, 330, 2.3), CU_BQ_H, tin="whipl", v=((1800, 380, 2.3), CU_BQ_V))                    # up to him, shaking
s = t; t = say(s + 0.05, "A2") + 0.1; shakes.append((s + 0.2, 22))
shot("room", s, t, WIDE_H, (1440, 545, 1.42), tin="whip", v=(WIDE_V, (1640, 545, 1.85)))                     # both — she screams
s = t; b2 = say(s + 0.1, "B2"); B2 = T("B2")
shot("room", s, B2 + 2.4, CU_BQ_H, (1790, 290, 2.75), tin="whipl", v=(CU_BQ_V, (1800, 320, 2.9)))           # pompous push-in
shot("room", B2 + 2.4, B2 + 4.2, (1760, 380, 1.9), (1760, 370, 2.0), tin="whip", v=((1780, 420, 2.1), (1780, 410, 2.2)))  # low angle «راجل البيت»
shot("room", B2 + 4.2, B2 + 6.4, CU_BQ_H, (1790, 300, 2.6), tin="whipl", v=(CU_BQ_V, (1800, 330, 2.75)))     # lecturing
SLIP = B2 + 6.4; shot("room", SLIP, b2 + 0.2, CU_AZ_H, (1560, 640, 2.7), tin="whip", v=(CU_AZ_V, (1560, 650, 2.9)))   # she slowly raises the slipper
REACT = b2 + 0.2; shot("room", REACT, REACT + 2.9, (1790, 300, 2.8), (1790, 296, 3.15), tin="whipl", ease="crash", v=((1800, 330, 2.9), (1800, 326, 3.3)))  # gulp
LAUGH = REACT + 0.45; say(LAUGH, "GROUP"); LU = min(2.6, DUR["GROUP"])
t = REACT + 2.9
shot("end", t, t + 2.4, None, v=None); t += 2.4
TOTAL = t

def vcam(sh, tt):
    """vertical camera (top-left form) for 1080x1920; z = output px per world unit (>= 1920/1080)"""
    c0, c1 = sh["v"]; k = ease((tt - sh["start"]) / max(0.01, sh["end"] - sh["start"]), sh.get("ease"))
    cx, cy, z = [a + (b - a) * k for a, b in zip(c0, c1)]; z = max(z, 1920 / 1080)
    shake = 0
    for st, amp in shakes:
        if 0 <= tt - st < 0.45: shake = max(shake, amp * (1 - (tt - st) / 0.45))
    cw, ch = 1080 / z, 1920 / z
    x0 = min(max(cx - cw / 2 + math.sin(tt * 0.9) * 3, 0), 1920 - cw); y0 = min(max(cy - ch / 2 + math.sin(tt * 1.3) * 2, 0), 1080 - ch)
    if shake: x0 = min(max(x0 + rng.normal(0, shake / z), 0), 1920 - cw); y0 = min(max(y0 + rng.normal(0, shake / z), 0), 1080 - ch)
    return x0, y0, z

# ---------------- drawing ----------------
def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, held=None):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    blink = ((tt + len(who) * 0.37) % 3.6) < 0.11 and expr not in ("laugh", "scared", "angry")
    X, Y_ = W2S(cam, x, y); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, held, lean, None)

def slipper(p, x, y, s, rot=0.0):
    c, sn = math.cos(rot), math.sin(rot); R = lambda dx, dy: (x + dx * c - dy * sn, y + dx * sn + dy * c)
    sole = [R(15 * s * math.cos(a_ / 16 * 2 * math.pi), 31 * s * math.sin(a_ / 16 * 2 * math.pi)) for a_ in range(16)]
    p.poly(sole, (70, 150, 210, 255), INK, 2 * s)
    p.poly([R(-16 * s, -12 * s), R(16 * s, -12 * s), R(13 * s, 5 * s), R(-13 * s, 5 * s)], (240, 240, 240, 255), INK, 1.5 * s)

def sweat(d, cam, x, hy, S, tt, n=2):
    z = cam[2]
    for i in range(n):
        u = (tt * 0.9 + i * 0.5) % 1.0; q = W2S(cam, x + (-40 + 80 * i) * S, hy - 20 * S + u * 50 * S); r = 5 * S * z
        d.ellipse([q[0] - r, q[1] - r * 1.5, q[0] + r, q[1] + r * 1.5], fill=(190, 225, 255, int(230 * (1 - u))), outline=(60, 110, 170, int(255 * (1 - u))), width=2)

def scene(tt, cam, size):
    """the room at camera cam (top-left form, z = px/world unit) on a canvas of `size` (W,H in px) — used for BOTH formats"""
    Wd, Hd = size; x0, y0, z = cam
    box = (x0, y0, x0 + Wd / z, y0 + Hd / z)
    img = ROOM.resize((int(Wd * SS), int(Hd * SS)), Image.BICUBIC, box=box)
    if z > 1.9: img = img.filter(ImageFilter.GaussianBlur(min(2.5, (z - 1.8) * 1.4)))
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); p = P(lay)
    k, lt = line_at(tt)
    # Aziza: slipper up when screaming, slow menacing raise at the end
    if k in ("A1", "A2"): aarms, rot, aex = "up", -0.6 + 0.5 * math.sin(tt * 14), "angry"
    elif tt >= SLIP: aarms, rot, aex = ("hold", "up", ease(kk(tt, SLIP, SLIP + 1.4))), -0.3, "smug"
    else: aarms, rot, aex = "hips", 0.2, "angry"
    person(lay, cam, "aziza", *AZ, tt, aex, 1, aarms)
    arms_k = aarms if isinstance(aarms, str) else ("up" if aarms[2] > 0.5 else "hold")
    S_a, sh_a, _ = body("aziza", *AZ)
    hx, hy = (AZ[0] + 72 * S_a, sh_a - 52 * S_a) if arms_k == "up" else (AZ[0] + 46 * S_a, sh_a + 30 * S_a)
    if not isinstance(aarms, str): hy = lerp(sh_a + 30 * S_a, sh_a - 52 * S_a, aarms[2]); hx = lerp(AZ[0] + 46 * S_a, AZ[0] + 72 * S_a, aarms[2])
    q = W2S(cam, hx, hy); slipper(p, q[0], q[1] - 10 * z, AZ[2] * z, rot)
    # Bandaq clinging to the grille: legs dangle + tremble, pompous lean during his speech
    trem = (math.sin(tt * 40) * 0.035) if (k == "B1" or tt >= REACT or (k == "B2" and lt > 6.2)) else math.sin(tt * 2.1) * 0.03
    proud = 0.0
    if k == "B2" and lt < 6.2: proud = -0.06 * ease(kk(lt, 0, 0.6))
    bex = "scared" if (k == "B1" or tt >= REACT) else ("smug" if k == "B2" else "scared")
    person(lay, cam, "bondo2", *BQ, tt, bex, -1, "up", trem + proud)
    lay = tint_layer(lay, (255, 240, 214)); img.paste(lay, (0, 0), lay)
    fr = img.resize((Wd, Hd), Image.LANCZOS)
    d = ImageDraw.Draw(fr, "RGBA")
    for gx in (1832, 1866, 1900):                                                  # grille bars in FRONT of his hands
        a_ = W2S(cam, gx, 60); b_ = W2S(cam, gx, 215); d.line([a_, b_], fill=(30, 26, 24, 255), width=max(2, int(5 * z)))
    S_b, sh_b, (bhx, bhy) = body("bondo2", *BQ)
    if tt >= REACT + 0.2 or (k == "B2" and lt > 6.3): sweat(d, cam, bhx, bhy, S_b, tt, 3)
    if REACT <= tt < REACT + 0.7:                                                  # gulp ring on his throat
        q = W2S(cam, bhx, bhy + 62 * S_b); r = (8 + 20 * kk(tt, REACT, REACT + 0.4)) * z
        d.ellipse([q[0] - r, q[1] - r * 0.5, q[0] + r, q[1] + r * 0.5], outline=(255, 255, 255, int(200 * (1 - kk(tt, REACT, REACT + 0.7)))), width=3)
    return fr

def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255, rot=0, stroke=True):
    if size < 4: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(LZ, size)
    if stroke: d.text((x, y), s, font=f, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), anchor="mm", direction="rtl", language="ar")
    d.text((x, y), s, font=f, fill=fill + (alpha,), anchor="mm", direction="rtl", language="ar")
    if rot: lay = lay.rotate(rot, center=(x, y), resample=Image.BICUBIC)
    img.paste(lay, (0, 0), lay)
def popk(tt, t0, d=0.22):
    u = kk(tt, t0, t0 + d); return 0 if u <= 0 else (1 + 0.25 * math.sin(u * math.pi)) if u < 1 else 1

def sub_chunk(img, tt, cx, cy, size):
    """phrase-synced subtitle, 1 line, key word in yellow (drawn as 3 parts, RTL)"""
    k, lt = line_at(tt)
    if not k or k not in CHUNKS: return
    cur = None
    for off, txt, key in CHUNKS[k]:
        if lt >= off: cur = (off, txt, key)
    if cur is None: return
    off, txt, key = cur; sc = popk(lt, off, 0.15) if lt - off < 0.15 else 1
    f = ImageFont.truetype(LZ, int(size * sc))
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    kw = dict(font=f, direction="rtl", language="ar", stroke_width=max(4, size // 10), stroke_fill=(10, 10, 10, 255))
    if key and key in txt:
        a, b = txt.split(key, 1); parts = [(a, (255, 255, 255)), (key, (255, 214, 60)), (b, (255, 255, 255))]
    else: parts = [(txt, (255, 255, 255))]
    widths = [d.textlength(s, font=f, direction="rtl", language="ar") if s else 0 for s, _ in parts]
    x = cx + sum(widths) / 2                                                       # RTL: start from the right edge
    for (s, col), w in zip(parts, widths):
        if s: d.text((x - w, cy), s, fill=col + (255,), anchor="lm", **kw)
        x -= w
    img.paste(lay, (0, 0), lay)

def endcard(fr, tt, sh, Wd, Hd):
    k = kk(tt, sh["start"], sh["start"] + 0.4)
    fr = ImageEnhance.Brightness(fr).enhance(1 - 0.55 * k).filter(ImageFilter.GaussianBlur(6 * k))
    sc = popk(tt, sh["start"] + 0.1, 0.3); vert = Hd > Wd
    if sc > 0:
        lzt(fr, Wd / 2, Hd * (0.36 if vert else 0.34), "منشن جوزك", int((120 if vert else 110) * sc), (255, 214, 90))
        lzt(fr, Wd / 2, Hd * (0.36 if vert else 0.34) + (130 if vert else 115), "اللي بيعمل كده!", int((96 if vert else 90) * sc), (255, 255, 255))
    if tt >= sh["start"] + 0.5:
        logo(fr, Wd / 2, Hd * (0.58 if vert else 0.68), 130); text(fr, Wd / 2, Hd * (0.58 if vert else 0.68) + 140, "@shattawzalata", 52, (255, 214, 90))
    return fr

_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/daily/16")

def subtitle(img, tt): sub_chunk(img, tt, W / 2, H - 95, 66)      # H uses the same phrase chunks

HOOK = "لما مراتك تقولك انزل…"
_FREEZE = {}
def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "end":
        if "h" not in _FREEZE: _FREEZE["h"] = scene(sh["start"] - 0.05, cam_at(shots[-2], sh["start"] - 0.05), (W, H))
        return finish(endcard(_FREEZE["h"].copy(), tt, sh, W, H), tt)
    fr = scene(tt, cam_at(sh, tt), (W, H))
    if tt < 3.0:
        a_ = int(255 * min(1, (3.0 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([W / 2 - 560, 40, W / 2 + 560, 150], 30, fill=(20, 12, 8, int(a_ * 0.8)))
        lzt(fr, W / 2, 95, HOOK, 72, (255, 214, 90), alpha=a_)
    return finish(fr, tt)

VIGV = VIG.resize((1080, 1920))
def vertical(_base, tt):
    """NATIVE 9:16: re-draws the scene with its own vertical camera (no blurred bars)"""
    sh = shot_at(tt)
    if sh["set"] == "end":
        if "v" not in _FREEZE: _FREEZE["v"] = scene(sh["start"] - 0.05, vcam(shots[-2], sh["start"] - 0.05), (1080, 1920))
        return endcard(_FREEZE["v"].copy(), tt, sh, 1080, 1920)
    fr = scene(tt, vcam(sh, tt), (1080, 1920))
    fr = ImageChops.multiply(fr, VIGV)
    u = tt - sh["start"]
    if sh.get("tin") in ("whip", "whipl") and u < 0.18:                             # quick whip blur
        k_ = 1 - u / 0.18; fr = fr.filter(ImageFilter.BoxBlur(int(2 + 18 * k_)))
    if tt < 3.0:                                                                   # hook (top safe zone, 3 s only)
        a_ = int(255 * min(1, (3.0 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([90, 230, 990, 470], 40, fill=(20, 12, 8, int(a_ * 0.75)))
        lzt(fr, 540, 300, "لما مراتك", 92, (255, 255, 255), alpha=a_); lzt(fr, 540, 405, "تقولك انزل…", 92, (255, 214, 90), alpha=a_)
    sub_chunk(fr, tt, 500, 1330, 82)                                                # lower third, above the UI, off the right column
    return fr

def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(16)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 300) * 0.015, 0, 1.0)
    for st in (T("A1") + 0.05, T("A2") + 0.05):                                    # slipper whooshes
        for j in range(3): mix_into(buf, SFXF["whoosh"] * 0.25, st + j * 0.22, 1.0)
    for j in range(int(DUR["B1"] / 0.09)): mix_into(buf, tone(180 + 40 * (j % 2), 0.05, 0.05, 30), T("B1") + j * 0.09, 1.0)   # grille rattle
    mix_into(buf, tone(220, 0.6, 0.18, 3) + tone(330, 0.6, 0.12, 3), T("B2") + 2.4, 1.0)                                     # pompous «dun»
    mix_into(buf, tone(120, 0.9, 0.3, 2), SLIP, 1.0); mix_into(buf, tone(90, 0.9, 0.25, 2), SLIP + 0.05, 1.0)                # menace
    gulp = np.sin(2 * np.pi * np.cumsum(np.linspace(420, 180, int(SR * 0.18))) / SR).astype(np.float32) * np.hanning(int(SR * 0.18)).astype(np.float32) * 0.4
    mix_into(buf, gulp, REACT + 0.1, 1.0)
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 0.5: mix_into(buf, SFXF["whoosh"] * 0.18, s_["start"] - 0.1, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), TOTAL - 2.3 + k_ * 0.09, 1.0)
    rms = lambda x: float(np.sqrt(np.mean(x ** 2))) + 1e-9; ref = []
    for st, k in lines:
        if k == "GROUP": continue
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8; ref.append(rms(v)); mix_into(buf, v, st, 1.0)
    g = AUD["GROUP"][:int(SR * LU)].copy(); g[-int(SR * 0.4):] *= np.linspace(1, 0, int(SR * 0.4))
    mix_into(buf, g / rms(g) * float(np.mean(ref)) * 1.2, LAUGH, 1.0)
    write_wav(buf[:int(TOTAL * SR)], path)

def make_covers():
    """growth rules 11-14 / 22-24: BIG faces (~half the frame), the slipper (story object), 2-3 word question, badge"""
    def comp(Wd, Hd, bq, az, title_xy, tsize, badge_xy):
        bgc = ROOM.crop((1250, 0, 1920, 1080)).resize((Wd, Hd), Image.LANCZOS).filter(ImageFilter.GaussianBlur(6))
        img = ImageEnhance.Brightness(bgc).enhance(0.8).resize((int(Wd * SS), int(Hd * SS)))
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); p = P(lay)
        bx, bhy, bS = bq; sh = bhy + 56 * bS; y = sh + 134 * bS
        p.line([(bx - 260 * bS / 3, sh - 52 * bS - 6), (bx + 260 * bS / 3, sh - 52 * bS - 6)], (30, 26, 24, 255), 16)   # the grille bar he hangs on
        for gx in (-0.9, 0.9): p.line([(bx + gx * 75 * bS, sh - 160 * bS), (bx + gx * 75 * bS, sh)], (30, 26, 24, 255), 12)
        draw_char(p, "bondo2", bx, y, bS / CH["bondo2"]["scale"], "scared", 0.35, -1, False, "up", 0.0, None, 0.0, None)
        ax, ahy, aS = az; ash = ahy + 56 * aS; ay = ash + 134 * aS
        draw_char(p, "aziza", ax, ay, aS / CH["aziza"]["scale"], "angry", 0.0, 1, False, "up", 0.0, None, 0.0, None)
        slipper(p, ax + 72 * aS, ash - 60 * aS, aS * 1.3, -0.5)
        img.paste(lay, (0, 0), lay); fr = img.resize((Wd, Hd), Image.LANCZOS); d = ImageDraw.Draw(fr, "RGBA")
        for i in range(3):                                                         # sweat drops
            q = (bx + (-1) ** i * 50 * bS, bhy - 30 * bS + i * 12 * bS); r = 5 * bS
            d.ellipse([q[0] - r, q[1] - r * 1.5, q[0] + r, q[1] + r * 1.5], fill=(190, 225, 255, 240), outline=(60, 110, 170, 255), width=3)
        tx, ty = title_xy
        lzt(fr, tx, ty, "راجل", tsize, (255, 255, 255)); lzt(fr, tx, ty + tsize * 0.95, "البيت؟!", tsize, (255, 214, 60))
        bx2, by2 = badge_xy; d.rounded_rectangle([bx2 - 170, by2 - 38, bx2 + 170, by2 + 38], 30, fill=(200, 30, 40, 240))
        lzt(fr, bx2, by2, "يوميات شطة وزلطة", 40, (255, 255, 255), stroke=False)
        return fr
    v = comp(1080, 1920, (620, 600, 5.0), (300, 1560, 4.4), (540, 1050), 180, (540, 250))
    v.save(ROOT + "/publish/thumbs/daily_e16_cover.jpg", quality=92)
    h = comp(1920, 1080, (1380, 380, 4.0), (1760, 960, 3.0), (520, 420), 210, (300, 90))
    h.resize((1280, 720), Image.LANCZOS).save(ROOT + "/publish/thumbs/daily_e16_yt.jpg", quality=92)

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
