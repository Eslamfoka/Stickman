# «يوميات شطة وزلطة» — «الشامبو اللي مابيخلصش» (H 1920x1080 + V 1080x1920 in one pass)
# Viral-format adaptation (endless-shampoo prank, 2011 — idea only): Zalata showers humming; Shatta's long arm keeps squeezing
# shampoo on his head. Time cards «بعد 10 دقايق» / «بعد ساعة», foam grows to the ceiling, Zalata screams, REVEAL: Shatta on a
# stool with a giant «عبوة عائلي» bottle → «ششش…» to camera → squeeze → foam explodes → audience laugh (sound only).
# NEW canonical location «حمام شقة شطة وزلطة» daily/bg/bathroom.png. Zalata's head pokes out of the curtain (body wrapped, family-safe).
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/daily/15")
SERIES = "يوميات شطة وزلطة"; EPT = "الشامبو"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"
SFXF = {"whoosh": load_audio(ROOT + "/trend/01/sfx/whoosh.mp3")}
SUB = {"H1": "♪ ترارا را را… لا لا لا ♪", "Z1": "هو… لسه فيه رغوة؟!", "H2": "♪ لا لا… لااا ♪", "Z2": "الرغوة دي ما بتخلصش لييه؟!",
       "SH": "ششش…", "GROUP": ""}
WHO = {"H1": "zalata", "Z1": "zalata", "H2": "zalata", "Z2": "zalata", "SH": "shatta", "GROUP": "-"}
EXPR = {"H1": "happy", "Z1": "shock", "H2": "sad", "Z2": "shout", "SH": "smug", "GROUP": "laugh"}
load_lines(list(SUB))
BATH = _ld(ROOT + "/daily/bg/bathroom.png")
CURT = (660, 1455, 700)                     # curtain wrap x0, x1, bottom y (top = Zalata's neck)

# ---------------- staging ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
ZL = (730, 790, 1.9); SHP = (250, 900, 1.9)            # Zalata standing in the tub · Shatta standing on the stool (feet on the seat)
def body(who, x, y, s):
    S = s * CH[who]["scale"]; sh = y - 134 * S; return S, sh, (x, sh - 56 * S)
_, ZSH, ZHEAD = body("zalata", *ZL)

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
CU = lambda z=2.4, dy=0: (ZHEAD[0] + 40, ZHEAD[1] + 85 + dy, z)
WIDE = (960, 560, 1.0)
SQ = []                                                   # squeeze moments
t = say(0.25, "H1")
shot("bath", 0.0, t + 0.2, CU(2.2), CU(2.45, -6))
SQ.append(2.6)
t = say(t + 0.35, "Z1") + 0.25
shot("bath", T("H1") + DUR["H1"] + 0.2, t, CU(2.6), CU(2.75, -6), tin="whip")
SQ.append(t - 0.1)
CARD1 = t; shot("card", CARD1, CARD1 + 1.0, None, txt="بعد 10 دقايق", tin="whip")
s = CARD1 + 1.0; shot("bath", s, s + 1.2, CU(2.3), CU(2.4, -4), tin="whip"); SQ.append(s + 0.5)
CARD2 = s + 1.2; shot("card", CARD2, CARD2 + 1.0, None, txt="بعد ساعة", tin="whip")
s = CARD2 + 1.0; t = say(s + 0.25, "H2")
shot("bath", s, t + 0.1, CU(1.7, -60), CU(1.85, -70), tin="whip")                  # wider: the foam tower
s = t + 0.1; SQ.append(s - 0.5); t = say(s + 0.05, "Z2") + 0.2; shakes.append((s + 0.4, 14))
shot("bath", s, t, CU(2.8), CU(3.2, -8), tin="whip", ease="crash")
REVEAL = t; shot("bath", REVEAL, REVEAL + 1.0, CU(2.4), WIDE, ease="ease")         # pull back → Shatta on the stool
t = say(REVEAL + 1.1, "SH")
shot("bath", REVEAL + 1.0, t + 0.1, (SHP[0] + 160, 520, 1.6), (SHP[0] + 160, 515, 1.75), tin="whip")   # Shatta → camera «ششش»
SQ.append(t + 0.15)
BOOM = t + 0.45; shot("bath", t + 0.1, BOOM + 2.8, WIDE, (960, 560, 1.05), tin="whip"); shakes.append((BOOM, 22))
LAUGH = BOOM + 0.25; say(LAUGH, "GROUP"); LU = min(2.6, DUR["GROUP"])
t = BOOM + 2.8
shot("end", t, t + 2.3, None); t += 2.3
TOTAL = t

def foam_level(tt):
    lv = 0.0
    for i, q in enumerate(SQ):
        if tt >= q: lv = [0.35, 0.6, 1.0, 1.6, 2.2, 2.4][min(i, 5)]
    if tt >= CARD1 + 1.0: lv = max(lv, 1.2)
    if tt >= CARD2 + 1.0: lv = max(lv, 2.0)
    return lv

# ---------------- drawing ----------------
def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, held=None):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    blink = (((tt + len(who) * 0.37) % 3.6) < 0.11 and expr not in ("laugh", "shock", "shout")) or (who == "zalata" and k in ("H1",) and talking)
    if not talking: lean += math.sin(tt * 1.7 + len(who)) * 0.04
    X, Y_ = W2S(cam, x, y); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, held, lean, None)

def foam(p, cam, tt, lv):
    """bubbly foam on Zalata's head; lv 0..2.4 (height in head-units)"""
    if lv <= 0: return
    S, sh, (hx, hy) = body("zalata", *ZL); z = cam[2]; rr = random.Random(9)
    n = int(10 + 26 * lv)
    for i in range(n):
        u = rr.random(); h = u * lv
        bx = hx + (rr.random() - 0.5) * (62 - 10 * min(h, 1.5)) * S * (1.2 if h < 0.6 else 1.0)
        by = hy - 40 * S - h * 50 * S + math.sin(tt * 3 + i) * 2 * S
        r = (12 + rr.random() * 12) * S * (1.0 - 0.15 * min(h, 2)); q = W2S(cam, bx, by)
        p.ell(q[0], q[1], r * z, r * z, (250, 252, 255, 255), (170, 200, 225, 255), 1.4 * z)
        p.ell(q[0] - r * z * 0.3, q[1] - r * z * 0.35, r * z * 0.25, r * z * 0.2, (215, 235, 255, 255), None)

def curtain(p, cam):
    """the bg curtain wrapped around Zalata from the neck down (he peeks out of the left edge)"""
    z = cam[2]; S, sh, _ = body("zalata", *ZL); top = sh - 6 * S
    a = W2S(cam, CURT[0], top); b = W2S(cam, CURT[1], CURT[2])
    pts = []
    for i in range(13): pts.append((a[0] + (b[0] - a[0]) * i / 12, a[1] + math.sin(i * 2.1) * 5 * z + (14 * z if i == 0 else 0)))
    for i in range(13): pts.append((a[0] + (b[0] - a[0]) * (1 - i / 12), b[1] + math.sin(i * 1.7) * 6 * z))
    p.poly(pts, (150, 196, 232, 255), (90, 130, 170, 255), 2 * z)
    for i in range(1, 9):
        x = a[0] + (b[0] - a[0]) * i / 9; q0 = W2S(cam, 0, top + 60)[1]
        p.line([(x, max(a[1] + 20 * z, q0 - 40 * z)), (x + 4 * z, b[1] - 6 * z)], (120, 168, 210, 255), 3 * z)

def stool(p, cam):
    z = cam[2]; x, y = SHP[0], SHP[1]
    a = W2S(cam, x - 70, y); b = W2S(cam, x + 70, y + 22); p.rect(a[0], a[1], b[0], b[1], (196, 120, 60, 255), INK, 2 * z, 4 * z)
    for dx in (-55, 55):
        q0 = W2S(cam, x + dx, y + 22); q1 = W2S(cam, x + dx * 1.15, 1075); p.line([q0, q1], (160, 96, 46, 255), 9 * z)

def bottle(p, cam, x, y, s, tt, squeeze=0.0):
    z = cam[2]; q = W2S(cam, x, y); k = s * z; w = 40 * k * (1 - 0.18 * squeeze)
    p.rect(q[0] - w, q[1] - 70 * k, q[0] + w, q[1] + 70 * k, (60, 170, 200, 255), INK, 2 * z, 14 * k)
    p.rect(q[0] - 12 * k, q[1] + 70 * k, q[0] + 12 * k, q[1] + 96 * k, (240, 240, 245, 255), INK, 2 * z, 4 * k)   # nozzle down
    p.rect(q[0] - w * 0.8, q[1] - 30 * k, q[0] + w * 0.8, q[1] + 30 * k, (250, 250, 250, 255), None)

def arm_and_bottle(lay, cam, tt):
    """Shatta's long sneaky arm: shoulder (on the stool) → over Zalata's head"""
    act = [q for q in SQ if q - 0.7 <= tt < q + 0.6]
    if not act and not (REVEAL <= tt): return 0.0
    q0 = act[0] if act else SQ[-1]
    S, sh, (hx, hy) = body("zalata", *ZL); Ss, ssh, _ = body("shatta", *SHP)
    if act:
        u_in = kk(tt, q0 - 0.7, q0 - 0.25); u_out = kk(tt, q0 + 0.2, q0 + 0.6); reach = ease(u_in) * (1 - ease(u_out))
    else: reach = 1.0 if tt < BOOM + 0.6 else 1.0
    sx, sy = SHP[0] + 22 * Ss, ssh + 8 * Ss
    tx, ty = hx - 10 * S, hy - 150 * S - 40 * S * foam_level(tt) * 0.4
    hx2, hy2 = lerp(sx, tx, reach), lerp(sy, ty, reach)
    p = P(lay); a = W2S(cam, sx, sy); b = W2S(cam, hx2, hy2)
    if act or tt >= REVEAL: p.line([a, b], INK, 7 * Ss * cam[2] / 1.9 * 1.2)
    sq = math.sin(kk(tt, q0 - 0.05, q0 + 0.2) * math.pi) if act else (math.sin(kk(tt, SQ[-1] - 0.05, SQ[-1] + 0.2) * math.pi) if tt >= SQ[-1] - 0.05 else 0)
    bottle(p, cam, hx2, hy2 + 20, 1.3 * Ss / 1.9 * (1.6 if tt >= REVEAL else 1.0), tt, sq)
    if sq > 0.2:                                                              # the squirt
        q = W2S(cam, hx2, hy2 + 20 + 120 * Ss / 1.9); r = W2S(cam, hx, hy - 50 * S)
        p.line([q, r], (250, 250, 255, 255), 6 * cam[2])
    return reach

def bath_frame(tt, sh):
    cam = cam_at(sh, tt); z = cam[2]
    img = bg_crop(BATH, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    lv = foam_level(tt)
    k, _ = line_at(tt)
    zex = "happy" if tt < T("Z1") else ("shock" if tt < CARD1 else ("flat" if tt < T("H2") else ("sad" if tt < T("Z2") else ("shout" if tt < REVEAL + 1.0 else "scared"))))
    zarms = "up" if (k in ("H1", "H2") or (T("Z1") <= tt < T("Z1") + DUR["Z1"])) else ("up" if T("Z2") <= tt < T("Z2") + DUR["Z2"] else "down")
    person(lay, cam, "zalata", *ZL, tt, zex, -1, zarms, 0.0)
    curtain(p, cam)
    foam(p, cam, tt, lv)
    if tt >= REVEAL - 0.01:
        stool(p, cam); person(lay, cam, "shatta", *SHP, tt, "smug" if tt < BOOM else "laugh", 0 if T("SH") <= tt < T("SH") + DUR["SH"] + 0.3 else 1, "shush" if T("SH") <= tt < T("SH") + DUR["SH"] else "down")
    arm_and_bottle(lay, cam, tt)
    base = img.copy()
    lay = tint_layer(lay, (250, 246, 236)); img.paste(lay, (0, 0), lay)
    a = W2S(cam, 700, 652); b = W2S(cam, 1470, 815); box = (int(max(0, a[0] * SS)), int(max(0, a[1] * SS)), int(min(SSW, b[0] * SS)), int(min(SSH, b[1] * SS)))
    if box[2] > box[0] and box[3] > box[1]: img.paste(base.crop(box), box[:2])          # tub front hides his legs
    fr = img.resize((W, H), Image.LANCZOS)
    d = ImageDraw.Draw(fr, "RGBA")
    if k in ("H1", "H2") and tt < REVEAL:                                     # water drops on his head while rinsing
        rr = random.Random(int(tt * 20)); S, _, (hx, hy) = body("zalata", *ZL)
        for i in range(14):
            q = W2S(cam, hx + (rr.random() - 0.5) * 140 * S, hy - 130 * S + rr.random() * 160 * S)
            d.line([q, (q[0], q[1] + 16 * z)], fill=(150, 200, 255, 170), width=max(1, int(2 * z)))
    if k in ("H1", "H2"):                                                      # floating music notes
        S, _, (hx, hy) = body("zalata", *ZL)
        for i in range(3):
            u = (tt * 0.6 + i / 3) % 1; q = W2S(cam, hx + 90 * S + i * 30 * S, hy - 40 * S - u * 120 * S)
            lzt(fr, q[0], q[1], "♪", int(34 * z), (255, 214, 90), alpha=int(255 * (1 - u)))
    if tt >= BOOM:                                                             # FOAM EXPLOSION fills the room
        u = kk(tt, BOOM, BOOM + 0.9); rr = random.Random(4)
        for i in range(int(40 + 160 * u)):
            ang = rr.random() * 6.28; dist = rr.random() * 1300 * ease(u); cx, cy = W2S(cam, ZHEAD[0], ZHEAD[1] - 60)
            x = cx + math.cos(ang) * dist; y = cy + math.sin(ang) * dist * 0.8; r = (30 + rr.random() * 70) * min(1, 0.4 + u)
            d.ellipse([x - r, y - r, x + r, y + r], fill=(252, 253, 255, 255), outline=(180, 205, 230, 255), width=3)
    return fr

def card(tt, sh):
    """time card on a bubbly blue backdrop"""
    fr = Image.new("RGB", (W, H), (40, 120, 200)); d = ImageDraw.Draw(fr, "RGBA"); rr = random.Random(2)
    for i in range(60):
        x = rr.random() * W; y = (rr.random() * H - (tt - sh["start"]) * 260 * (0.5 + rr.random())) % (H + 200) - 100; r = 10 + rr.random() * 40
        d.ellipse([x - r, y - r, x + r, y + r], outline=(200, 235, 255, 160), width=4)
    lzt(fr, W / 2, H / 2, sh["txt"], int(170 * popk(tt, sh["start"], 0.25)), (255, 255, 255), (20, 50, 100), rot=-3)
    return fr

_FC = {}
def frame_cache(t_):
    if t_ not in _FC: _FC[t_] = frame(t_)
    return _FC[t_]
def endcard(tt, sh):
    k = kk(tt, sh["start"], sh["start"] + 0.4)
    fr = ImageEnhance.Brightness(frame_cache(sh["start"] - 0.05)).enhance(1 - 0.5 * k).filter(ImageFilter.GaussianBlur(6 * k)).convert("RGBA")
    sc = popk(tt, sh["start"] + 0.1, 0.3)
    if sc > 0: lzt(fr, W / 2, 380, "منشن أخوك اللي يعمل كده! 😂".replace(" 😂", ""), int(104 * sc), (255, 214, 90))
    if tt >= sh["start"] + 0.5:
        logo(fr, W / 2, 660, 130); text(fr, W / 2, 810, "@shattawzalata", 52, (255, 214, 90))
    return fr.convert("RGB")

HOOK = "لما أخوك يعمل فيك مقلب الشامبو…"
def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "end": return finish(endcard(tt, sh), tt)
    if sh["set"] == "card": return finish(card(tt, sh), tt)
    fr = bath_frame(tt, sh)
    if tt < 3.0:
        a_ = int(255 * min(1, (3.0 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([W / 2 - 640, 40, W / 2 + 640, 150], 30, fill=(20, 12, 8, int(a_ * 0.8)))
        lzt(fr, W / 2, 95, HOOK, 70, (255, 214, 90), alpha=a_)
    return finish(fr, tt)

def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255, rot=0, stroke=True):
    if size < 4: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    f = ImageFont.truetype(ROOT + "/brand/fonts/DejaVuSans-Bold.ttf" if s == "♪" else LZ, size)
    kw = dict(anchor="mm") if s == "♪" else dict(anchor="mm", direction="rtl", language="ar")
    if stroke: d.text((x, y), s, font=f, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), **kw)
    d.text((x, y), s, font=f, fill=fill + (alpha,), **kw)
    if rot: lay = lay.rotate(rot, center=(x, y), resample=Image.BICUBIC)
    img.paste(lay, (0, 0), lay)
def popk(tt, t0, d=0.22):
    u = kk(tt, t0, t0 + d); return 0 if u <= 0 else (1 + 0.25 * math.sin(u * math.pi)) if u < 1 else 1

_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/daily/15")

def vertical(fr, tt):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = ImageEnhance.Brightness(small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.35)
    bgv.paste(fr.resize((1080, 608), Image.LANCZOS), (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(255, 214, 90)); d.rectangle([0, 1168, 1080, 1171], fill=(255, 214, 90))
    lzt(bgv, 540, 250, "مقلب الشامبو", 116, (255, 255, 255))
    lzt(bgv, 540, 400, "اللي مابيخلصش!", 104, (255, 214, 90))
    lzt(bgv, 540, 1840, SERIES, 44, (255, 150, 110))
    k, _ = line_at(tt)
    if k and SUB.get(k):
        for i, l in enumerate(wrap(SUB[k])[:3]): text(bgv, 540, 1300 + i * 84, l, 66, sw=6)
    return bgv

def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def squelch(seed):
    r = np.random.default_rng(seed); n = int(SR * 0.25); d_ = np.arange(n) / SR
    f = 260 + 500 * d_ / 0.25; x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-d_ * 8) * 0.25
    x += lowpass(r.normal(0, 1, n).astype(np.float32), 1500) * np.exp(-d_ * 10) * 0.25; return x.astype(np.float32)
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(15)
    shower = r.normal(0, 1, n).astype(np.float32); shower = (shower - lowpass(shower, 2500)) * 0.035
    shower[int(REVEAL * SR):int((REVEAL + 1.0) * SR)] *= np.linspace(1, 0.5, int(SR * 1.0)); shower[int((TOTAL - 2.3) * SR):] *= 0.0
    mix_into(buf, shower, 0, 1.0)                                                                        # shower running
    for i, q in enumerate(SQ): mix_into(buf, squelch(i), q, 1.0)
    for c in (CARD1, CARD2):
        mix_into(buf, SFXF["whoosh"] * 0.3, c - 0.08, 1.0)
        for k_, f in enumerate((523, 659, 784)): mix_into(buf, tone(f, 0.3, 0.12, 8), c + 0.05 + k_ * 0.07, 1.0)
    mix_into(buf, tone(140, 0.5, 0.25, 5) + tone(95, 0.5, 0.25, 5), REVEAL, 1.0)
    rr = random.Random(3)                                                                                # BOOM: whoosh + bubble pops
    mix_into(buf, SFXF["whoosh"] * 0.7, BOOM - 0.05, 1.0)
    for j in range(40): mix_into(buf, tone(500 + rr.random() * 1500, 0.06, 0.12, 40), BOOM + rr.random() * 1.2, 1.0)
    for s_ in shots:
        if s_.get("tin") == "whip" and s_["start"] > 0.5 and s_["set"] == "bath": mix_into(buf, SFXF["whoosh"] * 0.15, s_["start"] - 0.1, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), TOTAL - 2.2 + k_ * 0.09, 1.0)
    rms = lambda x: float(np.sqrt(np.mean(x ** 2))) + 1e-9; ref = []
    for st, k in lines:
        if k == "GROUP": continue
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8
        if k in ("H1", "H2"): v = v + np.concatenate([np.zeros(int(SR * 0.06), np.float32), v[:-int(SR * 0.06)]]) * 0.25   # bathroom echo
        ref.append(rms(v)); mix_into(buf, v, st, 1.0)
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
