# «ترند الأسبوع» — عزيزة في المطار (passport-photo makeup reel adaptation; user 17/11 22:29)
# NO VOICES — sound effects only (user). Ends on the stamp → our page (logo + handle + like/follow/share).
# Aziza struts in full glam → passport photo = her plain face → officer (canonical «الظابط») looks photo/her/photo → taps the photo
# → she wipes it all off (shadow, lashes, lips, earrings, blush) → matches the photo → STAMP → brand end card.
# NEW location: «جوازات المطار» trend/03/bg/airport.png (counter drawn in code).
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/trend/03")
SERIES = "ترند الأسبوع"; EPT = "عزيزة في المطار"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"
SFXF = {"whoosh": load_audio(ROOT + "/trend/01/sfx/whoosh.mp3"), "steps": load_audio(ROOT + "/s1e10/sfx/footsteps.mp3")}
SUB = {}; WHO = {}; EXPR = {}
AIR = _ld(ROOT + "/trend/03/bg/airport.png")

# ---------------- timeline (seconds) ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
WALK0, WALK1 = 0.0, 1.5
shot("air", 0.0, 2.6, (1000, 600, 1.25), (980, 620, 1.35))                       # wide: she struts in, slides the passport, blows a kiss
KISS = 1.9
PASS = 2.6; shot("pass", PASS, 4.2, None, tin="zoom")                              # passport opens: her PLAIN photo
GLAM = 4.2; shot("air", GLAM, 5.5, (640, 690, 2.7), (640, 684, 2.9), tin="whip")   # CU glam: lash flutter
OFF = 5.5; shot("air", OFF, 7.7, (1260, 560, 2.7), (1260, 554, 2.85), tin="whip")  # CU officer: photo / her / photo / her
TAP = 7.7; shot("air", TAP, 8.9, (950, 620, 1.7), (950, 615, 1.8), tin="whipl")   # two-shot: he slides it back, taps the photo
REAL = 8.9; shot("air", REAL, 9.7, (640, 690, 2.7), (640, 686, 2.8), tin="whip")  # she gets it… sigh
REM = 9.7; shot("air", REM, 14.2, (640, 690, 2.75), (640, 684, 3.0))              # wipe-off montage
MATCH = 14.2; shot("match", MATCH, 15.5, None, tin="flash")                        # her face = the photo ✔
STAMP = 15.5; shot("stamp", STAMP, 16.6, None, tin="whip")                         # officer nods → STAMP
END = 16.6; shot("end", END, 20.0, None, tin="flash")
TOTAL = 20.0

# ---------------- staging ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
AZ = (640, 1010, 1.8); OF = (1260, 900, 1.85)
COUNTER = (900, 1560, 760)                                       # x0, x1, top y

def head(who, x, y, s):
    S = s * CH[who]["scale"]; sh = y - 134 * S; return S, sh, (x, sh - 56 * S)

def makeup_state(tt):
    """1 = on, 0 = removed, per item"""
    m = dict(shadow=1.0, lashes=1.0, lips=1.0, earrings=1.0, blush=1.0, mole=1.0)
    if tt >= REM:
        r = tt - REM
        m["shadow"] = 1 - kk(r, 0.2, 0.9)
        m["lashes"] = 1 - kk(r, 1.1, 1.8)
        m["lips"] = 1 - kk(r, 2.0, 2.8)
        m["earrings"] = 1 - kk(r, 2.9, 3.5)
        m["blush"] = 1 - kk(r, 3.6, 4.2); m["mole"] = m["blush"]
    return m

def draw_makeup(p, hx, hy, S, m, tt, blink=False):
    a = lambda v: int(255 * max(0, min(1, v)))
    ex, ey = 15 * S, hy + 2 * S
    if m["shadow"] > 0:                                                            # blue/silver glitter eyeshadow
        for sx in (-1, 1):
            p.ell(hx + sx * ex, ey - 8 * S, 13 * S, 8 * S, (70, 140, 230, a(m["shadow"] * 0.85)), None)
            for k in range(5):
                gx = hx + sx * ex + (k - 2) * 4 * S; p.ell(gx, ey - 12 * S + (k % 2) * 3 * S, 1.3 * S, 1.3 * S, (255, 255, 255, a(m["shadow"])), None)
    if m["blush"] > 0:
        for sx in (-1, 1): p.ell(hx + sx * 27 * S, hy + 16 * S, 9 * S, 5.5 * S, (255, 110, 140, a(m["blush"] * 0.55)), None)
    if m["mole"] > 0: p.ell(hx + 20 * S, hy + 24 * S, 2 * S, 2 * S, (30, 20, 20, a(m["mole"])), None)
    if m["lashes"] > 0 and not blink:                                              # big curled lashes (flutter = tiny wiggle)
        fl = math.sin(tt * 30) * 0.15 if GLAM <= tt < OFF else 0
        for sx in (-1, 1):
            for k in range(5):
                ang = math.radians(-150 + k * 30) * sx if sx > 0 else math.radians(-30 - k * 30)
                bx = hx + sx * ex + math.cos(ang) * 9 * S; by = ey + math.sin(ang) * 8 * S
                L = (7 + (k == 2) * 2) * S * (1 + fl)
                p.line([(bx, by), (bx + math.cos(ang) * L, by + math.sin(ang) * L - 2 * S)], (20, 16, 18, a(m["lashes"])), 2.2 * S)
    if m["lips"] > 0:                                                              # pouty red lips
        p.ell(hx, hy + 27 * S, 11 * S, 6 * S, (214, 20, 50, a(m["lips"])), (120, 10, 30, a(m["lips"])), 1.5 * S)
        p.line([(hx - 9 * S, hy + 27 * S), (hx + 9 * S, hy + 27 * S)], (130, 10, 30, a(m["lips"])), 1.2 * S)
        p.ell(hx - 3 * S, hy + 24 * S, 3 * S, 1.4 * S, (255, 160, 170, a(m["lips"] * 0.8)), None)
    if m["earrings"] > 0:                                                          # big gold hoops
        for sx in (-1, 1):
            cx = hx + sx * (46 * S + 4 * S); cy = hy + 30 * S
            p.ell(cx, cy, 11 * S, 13 * S, None, (232, 190, 60, a(m["earrings"])), 3 * S)

def counter(p, cam):
    z = cam[2]; x0, x1, ty = COUNTER
    a_ = W2S(cam, x0 - 20, ty - 26); b = W2S(cam, x1 + 20, ty); p.rect(a_[0], a_[1], b[0], b[1], (196, 202, 210, 255), INK, 3 * z, 4 * z)
    a_ = W2S(cam, x0, ty); b = W2S(cam, x1, 1110); p.rect(a_[0], a_[1], b[0], b[1], (120, 128, 140, 255), INK, 3 * z, 2 * z)
    for xx in range(x0 + 30, x1 - 30, 160):
        a_ = W2S(cam, xx, ty + 30); b = W2S(cam, xx + 130, 1080); p.rect(a_[0], a_[1], b[0], b[1], (104, 112, 124, 255), INK, 2 * z, 3 * z)

def passport_closed(p, x, y, s, rot=0.0):
    c, sn = math.cos(rot), math.sin(rot); R = lambda dx, dy: (x + dx * c - dy * sn, y + dx * sn + dy * c)
    p.poly([R(-16 * s, -22 * s), R(16 * s, -22 * s), R(16 * s, 22 * s), R(-16 * s, 22 * s)], (24, 70, 50, 255), INK, 2 * s)   # green Egyptian passport
    q = R(0, -4 * s); p.ell(q[0], q[1], 6 * s, 6 * s, (220, 180, 70, 255), None)

def aziza(lay, cam, tt, expr="happy", arms="hips", look=1, lean=0.0, walk=None, x=None):
    z = cam[2]; x = AZ[0] if x is None else x; y, s = AZ[1], AZ[2]
    m = makeup_state(tt); blink = ((tt + 0.7) % 3.1) < 0.12
    X, Y_ = W2S(cam, x, y)
    draw_char(P(lay), "aziza", X, Y_, s * z, expr, 0.0, look, blink, arms, tt, None, lean, walk)
    S, sh, (hx, hy) = head("aziza", x, y, s)
    hX, hY = W2S(cam, hx + look * 4 * S * 0, hy); draw_makeup(P(lay), hX, hY, S * z, m, tt, blink)
    return S, sh, hx, hy

# ---------------- frames ----------------
def air_frame(tt, sh):
    cam = cam_at(sh, tt); z = cam[2]
    img = bg_crop(AIR, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    # officer (behind the counter)
    oex = "flat"
    if OFF <= tt < TAP: oex = "smug" if int((tt - OFF) / 0.55) % 2 else "flat"
    olook = 0
    if OFF <= tt < TAP: olook = -1 if int((tt - OFF) / 0.55) % 2 else 0          # photo (down/front) ↔ her (left)
    if tt < OFF: olook = -1
    oarms = "point" if TAP + 0.3 <= tt < REAL else "hold"
    X, Y_ = W2S(cam, *OF[:2]); draw_char(p, "officer", X, Y_, OF[2] * z, oex, 0.0, olook, ((tt + 1.3) % 3.3) < 0.12, oarms, tt, None, 0.0, None)
    counter(p, cam)
    # passport on the counter
    if KISS - 0.4 <= tt < REAL:
        u = kk(tt, TAP, TAP + 0.4); px = lerp(1180, 1000, u) if tt >= TAP else (lerp(860, 1180, kk(tt, KISS - 0.4, KISS)))
        q = W2S(cam, px, COUNTER[2] - 18); passport_closed(p, q[0], q[1], 1.6 * z, 1.4)
    # Aziza
    k = kk(tt, WALK0, WALK1); e = ease(k); wk = tt * 9 if 0 < k < 1 else None
    x = lerp(150, AZ[0], e)
    aex, aarms, alook = "happy", "hips", 1
    if KISS <= tt < KISS + 0.6: aarms = "salute"
    if GLAM <= tt < OFF: aex = "smug"
    if REAL <= tt < REM: aex = "shock" if tt < REAL + 0.4 else "sad"
    if tt >= REM: aex, aarms = "neutral", "salute"
    if tt >= REM + 4.3: aarms = "down"
    aziza(lay, cam, tt, aex, aarms, alook, 0.0, wk, x)
    # tissue wiping (hand-held white wipe that moves over each makeup item)
    if REM <= tt < REM + 4.3:
        S, sh_, (hx, hy) = head("aziza", *AZ)
        r = tt - REM
        if r < 0.9: tx, ty_ = hx + 15 * S * math.sin(r * 18), hy - 2 * S
        elif r < 1.9: tx, ty_ = hx + (-15 if r < 1.4 else 15) * S, hy - 4 * S
        elif r < 2.85: tx, ty_ = hx + 9 * S * math.sin(r * 22), hy + 27 * S
        elif r < 3.55: tx, ty_ = hx + (-50 if r < 3.2 else 50) * S, hy + 30 * S
        else: tx, ty_ = hx + 26 * S * math.sin(r * 16), hy + 16 * S
        q = W2S(cam, tx, ty_)
        p.rect(q[0] - 12 * S * z, q[1] - 10 * S * z, q[0] + 12 * S * z, q[1] + 10 * S * z, (250, 250, 252, 240), (180, 190, 200, 255), 1.5 * S * z, 3 * S * z)
    lay = tint_layer(lay, (236, 244, 255)); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    d = ImageDraw.Draw(fr, "RGBA")
    if KISS <= tt < KISS + 1.0:                                                   # flying kiss hearts
        for i in range(3):
            u = kk(tt, KISS + i * 0.12, KISS + 0.8 + i * 0.12); q = W2S(cam, lerp(AZ[0] + 60, OF[0] - 60, u), 560 - 60 * math.sin(u * math.pi) - i * 30)
            r = 14 * z * (1 - 0.3 * u)
            if 0 < u < 1:
                d.ellipse([q[0] - 2 * r, q[1] - r, q[0], q[1] + r * 0.6], fill=(235, 60, 90, 230)); d.ellipse([q[0], q[1] - r, q[0] + 2 * r, q[1] + r * 0.6], fill=(235, 60, 90, 230))
                d.polygon([(q[0] - 2 * r + 1, q[1]), (q[0] + 2 * r - 1, q[1]), (q[0], q[1] + 2 * r)], fill=(235, 60, 90, 230))
    if GLAM <= tt < OFF:                                                           # sparkle stars
        for i in range(4):
            ph = (tt * 1.5 + i / 4) % 1.0; S, _, (hx, hy) = head("aziza", *AZ); q = W2S(cam, hx + (i - 1.5) * 40 * S, hy - 30 * S + i % 2 * 50 * S)
            rr = 22 * z * math.sin(ph * math.pi)
            d.polygon([(q[0], q[1] - rr), (q[0] + rr * 0.2, q[1] - rr * 0.2), (q[0] + rr, q[1]), (q[0] + rr * 0.2, q[1] + rr * 0.2), (q[0], q[1] + rr), (q[0] - rr * 0.2, q[1] + rr * 0.2), (q[0] - rr, q[1]), (q[0] - rr * 0.2, q[1] - rr * 0.2)], fill=(255, 255, 255, 230))
    if TAP + 0.3 <= tt < REAL:                                                     # tap-tap marks on the photo
        if int(tt * 8) % 2: q = W2S(cam, 1000, COUNTER[2] - 40); lzt(fr, q[0], q[1], "!", int(60 * z / 1.7), (255, 220, 60))
    if REAL <= tt < REM:                                                           # sigh puff
        S, _, (hx, hy) = head("aziza", *AZ); q = W2S(cam, hx + 60 * S, hy + 20 * S); u = kk(tt, REAL + 0.3, REM)
        d.ellipse([q[0] + u * 40, q[1] - 14 - u * 20, q[0] + 50 + u * 60, q[1] + 14 - u * 20], fill=(255, 255, 255, int(180 * (1 - u))))
    return fr

def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255):
    if size < 4: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(LZ, size)
    d.text((x, y), s, font=f, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), anchor="mm", direction="rtl", language="ar")
    d.text((x, y), s, font=f, fill=fill + (alpha,), anchor="mm", direction="rtl", language="ar")
    img.paste(lay, (0, 0), lay)
def popk(tt, t0, d=0.22):
    u = kk(tt, t0, t0 + d); return 0 if u <= 0 else (1 + 0.25 * math.sin(u * math.pi)) if u < 1 else 1

def plain_face(size=420, expr="neutral"):
    """passport photo: Aziza with NO makeup"""
    im = Image.new("RGBA", (int(size * SS), int(size * 1.25 * SS)), (226, 232, 238, 255))
    draw_char(P(im), "aziza", size / 2, size * 1.25 + 120, 2.6, expr, 0.0, 0, False, "down", 0.0)
    return im.resize((size, int(size * 1.25)), Image.LANCZOS).convert("RGB")
PHOTO = plain_face()

def passport_page(w=900, h=620, stamp_k=0.0):
    pg = Image.new("RGB", (w, h), (236, 240, 226)); d = ImageDraw.Draw(pg)
    for yy in range(0, h, 18): d.line([(0, yy), (w, yy + 30)], fill=(226, 232, 214), width=2)
    d.rectangle([0, 0, w - 1, h - 1], outline=(140, 150, 130), width=6)
    ph = PHOTO.resize((300, 375), Image.LANCZOS); pg.paste(ph, (w - 340, 120)); d.rectangle([w - 340, 120, w - 40, 495], outline=(90, 90, 90), width=3)
    for i in range(6): d.rectangle([60, 140 + i * 56, 60 + (420 if i % 2 else 320), 160 + i * 56], fill=(170, 176, 160))
    d.rectangle([40, h - 90, w - 40, h - 70], fill=(150, 156, 140)); d.rectangle([40, h - 55, w - 40, h - 35], fill=(150, 156, 140))
    lzt(pg, 230, 70, "جواز سفر", 56, (40, 70, 50), (236, 240, 226))
    if stamp_k > 0:
        st = Image.new("RGBA", (360, 360), (0, 0, 0, 0)); ds = ImageDraw.Draw(st)
        ds.ellipse([10, 10, 350, 350], outline=(30, 90, 200, 230), width=14); ds.ellipse([46, 46, 314, 314], outline=(30, 90, 200, 200), width=5)
        lzt(st, 180, 150, "دخول", 76, (30, 90, 200), (236, 240, 226)); lzt(st, 180, 232, "✓".replace("✓", "مقبول"), 52, (30, 90, 200), (236, 240, 226))
        sz = int(360 * (1 + 1.5 * (1 - min(1, stamp_k)))) ; st = st.rotate(-12, resample=Image.BICUBIC).resize((sz, sz), Image.LANCZOS)
        if stamp_k < 1: st.putalpha(st.getchannel("A").point(lambda v: int(v * stamp_k)))
        pg.paste(st, (int(260 - sz / 2), int(330 - sz / 2)), st)
    return pg

def pass_insert(tt, sh):
    u = kk(tt, sh["start"], sh["end"])
    cam = (1000 - 960 / 2.0, 640 - 540 / 2.0, 2.0)
    fr = bg_crop(AIR, cam).resize((W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(12)); fr = ImageEnhance.Brightness(fr).enhance(0.55)
    op = ease(kk(tt, sh["start"] + 0.1, sh["start"] + 0.55))
    pg = passport_page(); zz = 1.0 + 0.1 * u
    pw, ph = int(1200 * zz), int(1200 * zz * 620 / 900)
    pg = pg.resize((pw, ph), Image.LANCZOS)
    vis = int(pw * (0.15 + 0.85 * op))                                                # page opens (cover slides away)
    fr.paste(pg.crop((pw - vis, 0, pw, ph)), (int(W / 2 + pw / 2 - vis), int(H / 2 - ph / 2)))
    if op < 1:
        cw = int(pw * (1 - op) * 0.5) + 1; d = ImageDraw.Draw(fr)
        d.rectangle([W / 2 - pw / 2 + (pw - vis) - cw, H / 2 - ph / 2, W / 2 - pw / 2 + (pw - vis), H / 2 + ph / 2], fill=(24, 70, 50), outline=(10, 30, 20), width=6)
    # two officer hands holding it
    d = ImageDraw.Draw(fr, "RGBA")
    for sx in (-1, 1):
        cx = W / 2 + sx * (pw / 2 - 10); cy = H / 2 + ph / 2 - 30
        d.ellipse([cx - 40, cy - 30, cx + 40, cy + 30], fill=(250, 250, 250), outline=(20, 20, 20), width=6)
    return fr

def match_frame(tt, sh):
    """her plain face next to the passport photo — a match ✔"""
    fr = Image.new("RGB", (W, H), (226, 236, 246)); d = ImageDraw.Draw(fr)
    k = popk(tt, sh["start"], 0.25)
    face = plain_face(420, "neutral").resize((520, 650), Image.LANCZOS)
    fr.paste(face, (240, 200)); d.rectangle([240, 200, 760, 850], outline=(40, 40, 40), width=6)
    ph = PHOTO.resize((520, 650), Image.LANCZOS); fr.paste(ph, (1160, 200)); d.rectangle([1160, 200, 1680, 850], outline=(40, 40, 40), width=6)
    lzt(fr, 500, 140, "دلوقتي", 70, (40, 40, 40), (226, 236, 246)); lzt(fr, 1420, 140, "الباسبور", 70, (40, 40, 40), (226, 236, 246))
    if k > 0:
        r = int(90 * k); d.ellipse([W / 2 - r, 525 - r, W / 2 + r, 525 + r], fill=(40, 170, 80), outline=(255, 255, 255), width=8)
        d.line([(W / 2 - 40 * k, 525), (W / 2 - 8 * k, 560 * 1 + 0 * k), (W / 2 + 46 * k, 490)], fill=(255, 255, 255), width=int(18 * k) + 1)
    return fr

def stamp_frame(tt, sh):
    fr = Image.new("RGB", (W, H), (20, 26, 34))
    k = kk(tt, sh["start"] + 0.35, sh["start"] + 0.5)
    pg = passport_page(stamp_k=k if k > 0 else 0.0).resize((1260, int(1260 * 620 / 900)), Image.LANCZOS)
    jit = 10 if sh["start"] + 0.5 <= tt < sh["start"] + 0.62 else 0
    fr.paste(pg, (int(W / 2 - 630), int(H / 2 - pg.size[1] / 2) + jit))
    if tt < sh["start"] + 0.5:                                                         # the stamp coming down
        u = kk(tt, sh["start"], sh["start"] + 0.45); y = lerp(-300, H / 2 - 160, ease(u))
        d = ImageDraw.Draw(fr); d.rectangle([W / 2 - 400, y - 160, W / 2 - 180, y + 40], fill=(120, 70, 40), outline=(20, 20, 20), width=6)
        d.rectangle([W / 2 - 430, y + 40, W / 2 - 150, y + 80], fill=(30, 30, 30))
    return fr

def end_card(tt, sh):
    fr = Image.new("RGB", (W, H), (20, 12, 10)); d = ImageDraw.Draw(fr, "RGBA")
    for i in range(18):
        a0 = i * 20 - tt * 6; a_ = math.radians(a0); b = math.radians(a0 + 9)
        d.polygon([(W / 2, H / 2), (W / 2 + 2400 * math.cos(a_), H / 2 + 2400 * math.sin(a_)), (W / 2 + 2400 * math.cos(b), H / 2 + 2400 * math.sin(b))], fill=(44, 24, 16, 255))
    k = popk(tt, sh["start"] + 0.1, 0.3)
    if k > 0: logo(fr, 560, 400, int(170 * k)); text(fr, 560, 590, "@shattawzalata", int(60 * k), (255, 214, 90))
    for i, (lab, col, t0) in enumerate((("لايك", (230, 50, 70), 0.6), ("فولو", (40, 140, 230), 1.0), ("شير", (60, 170, 90), 1.4))):
        k2 = popk(tt, sh["start"] + t0, 0.25)
        if k2 <= 0: continue
        cx, cy = 1380, 260 + i * 200
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
    return fr

_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/trend/03")

def frame(tt):
    sh = shot_at(tt); s_ = sh["set"]
    fr = {"air": air_frame, "pass": pass_insert, "match": match_frame, "stamp": stamp_frame, "end": end_card}[s_](tt, sh)
    if tt < 2.6:
        a_ = int(255 * min(1, (2.6 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([W / 2 - 560, 40, W / 2 + 560, 150], 30, fill=(20, 12, 8, int(a_ * 0.8)))
        lzt(fr, W / 2, 95, "لما صورة الباسبور غير الحقيقة 😂".replace(" 😂", ""), 72, (255, 214, 90), alpha=a_)
    return finish(fr, tt)

def vertical(fr, tt):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = ImageEnhance.Brightness(small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.35)
    bgv.paste(fr.resize((1080, 608), Image.LANCZOS), (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(255, 214, 90)); d.rectangle([0, 1168, 1080, 1171], fill=(255, 214, 90))
    lzt(bgv, 540, 250, "لما صورة الباسبور", 104, (255, 255, 255))
    lzt(bgv, 540, 395, "غير الحقيقة!", 116, (255, 214, 90))
    lzt(bgv, 540, 1840, SERIES, 44, (255, 150, 110))
    return bgv

class _T(np.ndarray):
    def __add__(self, o):                                   # tones of different length add safely (pad the shorter)
        n = max(len(self), len(o)); a = np.zeros(n, np.float32); a[:len(self)] += self; a[:len(o)] += o; return a
def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32).view(_T)
def noise(dur, amp, lp=4000, seed=0):
    r = np.random.default_rng(seed); return (lowpass(r.normal(0, 1, int(SR * dur)).astype(np.float32), lp) * amp * np.hanning(int(SR * dur))).astype(np.float32)
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(54)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 500) * 0.03, 0, 1.0)                     # airport hall air
    for j in range(5): mix_into(buf, tone(2400, 0.04, 0.16, 50) + tone(1200, 0.04, 0.08, 50), WALK0 + 0.15 + j * 0.28, 1.0)   # heels click
    mix_into(buf, noise(0.25, 0.15, 3000, 1), KISS - 0.4, 1.0)                                         # passport slides
    mix_into(buf, tone(1500, 0.15, 0.15, 12) + tone(2000, 0.12, 0.1, 14), KISS + 0.1, 1.0)             # «mwah» pop
    mix_into(buf, SFXF["whoosh"] * 0.35, PASS - 0.1, 1.0); mix_into(buf, noise(0.3, 0.12, 2500, 2), PASS + 0.15, 1.0)   # passport opens
    for j in range(3): mix_into(buf, tone(2600 + j * 300, 0.25, 0.08, 8), GLAM + 0.1 + j * 0.3, 1.0)     # sparkle ting
    for j in range(4): mix_into(buf, tone(420 if j % 2 else 520, 0.12, 0.16, 18), OFF + 0.1 + j * 0.55, 1.0)   # eye-dart «boing»
    for j in range(2): mix_into(buf, tone(900, 0.05, 0.25, 40), TAP + 0.45 + j * 0.22, 1.0)              # tap tap
    mix_into(buf, noise(0.7, 0.18, 900, 3), REAL + 0.3, 1.0)                                              # sigh
    for j, (t0, f) in enumerate(((0.2, 0), (1.15, 1), (1.45, 1), (2.0, 2), (2.9, 3), (3.25, 3), (3.6, 4))):
        if f == 0 or f == 2 or f == 4: mix_into(buf, noise(0.7, 0.14, 3500, 10 + j), REM + t0, 1.0)      # wipe swish
        if f == 1: mix_into(buf, tone(700, 0.08, 0.3, 30), REM + t0, 1.0)                                  # lash «pop»
        if f == 3: mix_into(buf, tone(3200, 0.2, 0.15, 10) + tone(4100, 0.15, 0.1, 12), REM + t0, 1.0)    # earring clink
    for k_, f in enumerate((660, 880, 1320)): mix_into(buf, tone(f, 0.3, 0.15, 7), MATCH + 0.05 + k_ * 0.08, 1.0)   # match ✔ ding
    mix_into(buf, tone(90, 0.4, 0.6, 8) + tone(140, 0.3, 0.4, 10), STAMP + 0.5, 1.0)                    # STAMP thunk
    for i, t0 in enumerate((0.6, 1.0, 1.4)): mix_into(buf, tone(880 + i * 220, 0.2, 0.2, 10), END + t0, 1.0)
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 0.5: mix_into(buf, SFXF["whoosh"] * 0.22, s_["start"] - 0.1, 1.0)
    write_wav(buf[:int(TOTAL * SR)], path)

if __name__ == "__main__":
    print("TOTAL", round(TOTAL, 1))
    if sys.argv[1:2] == ["stills"]: render(None, None, [float(v) for v in sys.argv[2:]])
    elif sys.argv[1:2] == ["part"]:
        i, n = int(sys.argv[2]), int(sys.argv[3]); a = round(TOTAL * i / n * FPS) / FPS; b = round(TOTAL * (i + 1) / n * FPS) / FPS
        render(f"h_{i}.mp4", f"v_{i}.mp4", None, a, b)
    elif sys.argv[1:2] == ["audio"]: build_audio()
