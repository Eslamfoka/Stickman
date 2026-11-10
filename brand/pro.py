# Pro brand pack v2: logo, avatar, YouTube banner, FB cover, 6 trend thumbnails
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
import sys, os, math
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())      # engine + kit helpers (chdir -> trend/01)
from PIL import ImageFont
BR = ROOT + "/brand"; OUT = DELIVERY + "/brand_v2"; os.makedirs(OUT, exist_ok=True)
LZ = f"{BR}/fonts/Lalezar-Regular.ttf"
CHILI = (225, 40, 35); LEAF = (60, 175, 70); GOLD = (255, 214, 90); DARK = (45, 12, 8)

def lz(img, x, y, s, size, fill, outer=DARK, inner=(255, 255, 255), ow=None, iw=None, shadow=True, anchor="mm"):
    """Lalezar text with white inner stroke + dark outer stroke + drop shadow"""
    f = ImageFont.truetype(LZ, size); ow = ow or max(3, size // 9); iw = iw or max(2, size // 22)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    kw = dict(font=f, anchor=anchor, direction="rtl", language="ar")
    if shadow:
        sh = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).text((x + size * 0.05, y + size * 0.08), s, fill=(0, 0, 0, 150), stroke_width=ow, stroke_fill=(0, 0, 0, 150), **kw)
        lay.alpha_composite(sh.filter(ImageFilter.GaussianBlur(size * 0.04)))
    d.text((x, y), s, fill=outer, stroke_width=ow, stroke_fill=outer, **kw)
    d.text((x, y), s, fill=inner, stroke_width=iw, stroke_fill=inner, **kw)
    d.text((x, y), s, fill=fill, **kw)
    img.alpha_composite(lay) if img.mode == "RGBA" else img.paste(lay, (0, 0), lay)
    return f.getbbox(s, direction="rtl", language="ar")

def chili(p, x, y, s, ang=-20):
    """little chili pepper icon (logical coords)"""
    c, sn = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    R = lambda u, v: (x + u * c - v * sn, y + u * sn + v * c)
    pts = [R(u * s, v * s) for u, v in [(-38, -6), (-10, -14), (20, -12), (40, -2), (30, 6), (0, 10), (-30, 6), (-48, 14)]]
    p.poly(pts, CHILI + (255,), DARK + (255,), 3 * s)
    p.line([R(38 * s, -4 * s), R(52 * s, -14 * s), R(58 * s, -10 * s)], (50, 140, 50, 255), 5 * s)
    p.line([R(-20 * s, -8 * s), R(12 * s, -8 * s)], (255, 140, 120, 255), 3 * s)

def leaf(p, x, y, s, ang=25):
    c, sn = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    R = lambda u, v: (x + (u * c - v * sn) * s, y + (u * sn + v * c) * s)
    pts = [R(-40, 0), R(-20, -18), R(10, -20), R(40, 0), R(10, 20), R(-20, 18)]
    p.poly(pts, LEAF + (255,), DARK + (255,), 3 * s)
    p.line([R(-40, 0), R(36, 0)], (190, 240, 170, 255), 2.5 * s)
    for u in (-15, 5, 22): p.line([R(u, 0), R(u + 10, -10)], (190, 240, 170, 255), 2 * s); p.line([R(u, 0), R(u + 10, 10)], (190, 240, 170, 255), 2 * s)

def logo(img, cx, cy, size):
    """«شطة» (chili red, right) + «وزلطة» (leaf green, left) + icons"""
    f = ImageFont.truetype(LZ, size)
    w1 = f.getlength("شطة", direction="rtl", language="ar"); w2 = f.getlength("وزلطة", direction="rtl", language="ar")
    gap = size * 0.18; tot = w1 + w2 + gap
    xr = cx + tot / 2 - w1 / 2; xl = cx - tot / 2 + w2 / 2
    lz(img, xr, cy - size * 0.04, "شطة", size, CHILI)
    lz(img, xl, cy + size * 0.06, "وزلطة", size, LEAF)
    ic = Image.new("RGBA", (int(img.size[0] * SS), int(img.size[1] * SS)), (0, 0, 0, 0)); p = P(ic)
    chili(p, xr + w1 * 0.38, cy - size * 0.62, size / 110, -25)
    leaf(p, xl - w2 * 0.30, cy - size * 0.52, size / 120, 20)
    ic = ic.resize(img.size, Image.LANCZOS)
    img.alpha_composite(ic) if img.mode == "RGBA" else img.paste(ic, (0, 0), ic)

def radial(w, h, c0, c1, cx=0.5, cy=0.5):
    yy, xx = np.mgrid[0:h, 0:w]
    r = np.sqrt(((xx - w * cx) / (w * 0.6)) ** 2 + ((yy - h * cy) / (h * 0.6)) ** 2)
    k = np.clip(r / 1.3, 0, 1)[..., None]
    return Image.fromarray((np.array(c0) * (1 - k) + np.array(c1) * k).astype(np.uint8)).convert("RGBA")
def rays(size, cx, cy, n, col):
    im = Image.new("RGBA", size, (0, 0, 0, 0)); d = ImageDraw.Draw(im); R = max(size) * 1.6
    for i in range(n):
        a0 = i * 2 * math.pi / n; a1 = a0 + math.pi / n
        d.polygon([(cx, cy), (cx + R * math.cos(a0), cy + R * math.sin(a0)), (cx + R * math.cos(a1), cy + R * math.sin(a1))], fill=col)
    return im

def figure(who, S, expr="happy", mouth=0.0, look=0, arms="down", held=None, shirt=None, num=None, lean=0.0, zzz=False, pad=60):
    """draw one character big on its own transparent layer (logical px), white sticker outline + shadow"""
    w_, h_ = int(420 * S / 2.0 + 2 * pad), int(560 * S / 2.0 + 2 * pad)
    lay = Image.new("RGBA", (int(w_ * SS), int(h_ * SS)), (0, 0, 0, 0)); p = P(lay)
    X, Y = w_ / 2, h_ - pad
    old = dict(CH[who])
    if shirt: CH[who]["shirt"] = shirt
    draw_char(p, who, X, Y, S, expr, mouth, look, False, arms, 0.4, held, lean, None)
    CH[who].update(old)
    Sc = S * CH[who]["scale"]; hip = Y - 62 * Sc; shy = hip - 72 * Sc
    if num: text(lay, X * SS, (shy + 34 * Sc) * SS, str(num), int(22 * Sc * SS), (255, 255, 255), (0, 0, 0), int(1.5 * Sc * SS))
    if zzz:
        for i, (dx, dy, sz) in enumerate(((60, 230, 40), (95, 300, 60), (140, 390, 85))):
            lz_ = lay; f = ImageFont.truetype(LZ, int(sz * Sc / 2.0 * SS))
            ImageDraw.Draw(lz_).text(((X + dx * Sc / 2.0 * 2) * SS, (Y - dy * Sc / 2.0 * 2) * SS), "Z", font=f, fill=(255, 255, 255), stroke_width=int(6 * SS), stroke_fill=DARK, anchor="mm")
    lay = lay.resize((w_, h_), Image.LANCZOS)
    a = lay.getchannel("A")
    out = a.filter(ImageFilter.MaxFilter(15)).filter(ImageFilter.GaussianBlur(1))
    sticker = Image.new("RGBA", lay.size, (255, 255, 255, 0)); sticker.putalpha(out)
    sh = Image.new("RGBA", lay.size, (0, 0, 0, 0)); sh.putalpha(out.point(lambda v: v * 0.55))
    sh = sh.filter(ImageFilter.GaussianBlur(10))
    res = Image.new("RGBA", lay.size, (0, 0, 0, 0)); res.alpha_composite(sh, (10, 14)); res.alpha_composite(sticker); res.alpha_composite(lay)
    return res

def place(img, fig, x, ybottom):
    img.alpha_composite(fig, (int(x - fig.size[0] / 2), int(ybottom - fig.size[1])))

# ================= logo (transparent PNG) =================
lg = Image.new("RGBA", (1600, 600), (0, 0, 0, 0)); logo(lg, 800, 330, 260); lg.save(f"{OUT}/logo.png")

# ================= avatar =================
A = radial(800, 800, (255, 222, 110), (235, 95, 30), 0.5, 0.4)
A.alpha_composite(rays((800, 800), 400, 330, 16, (255, 255, 255, 38)))
place(A, figure("zalata", 2.45, "happy", 0.25, 1, "down"), 205, 840)
place(A, figure("tota", 2.35, "happy", 0.2, -1, "down"), 600, 850)
place(A, figure("shatta", 2.75, "happy", 0.45, 0, "down"), 400, 880)
rib = Image.new("RGBA", A.size, (0, 0, 0, 0)); ImageDraw.Draw(rib).rounded_rectangle([110, 610, 690, 740], 60, fill=(255, 245, 225, 245), outline=DARK, width=6)
A.alpha_composite(rib); logo(A, 400, 680, 96)
A.convert("RGB").save(f"{OUT}/avatar.png")

# ================= drawn rooftop / skyline backdrop =================
def skyline(w, h, seed=3):
    im = Image.new("RGBA", (w, h)); a = np.zeros((h, w, 3))
    top, bot = np.array((48, 36, 92)), np.array((250, 140, 70))
    for y in range(h): a[y] = top + (bot - top) * (y / h) ** 1.3
    im = Image.fromarray(a.astype(np.uint8)).convert("RGBA"); d = ImageDraw.Draw(im)
    d.ellipse([w * 0.78, h * 0.12, w * 0.78 + h * 0.16, h * 0.28], fill=(255, 240, 200))
    r = np.random.default_rng(seed); x = 0
    while x < w:      # far buildings
        bw = r.integers(60, 160) * w / 2560; bh = r.integers(120, 380) * h / 1440
        d.rectangle([x, h * 0.62 - bh, x + bw, h], fill=(70, 45, 95)); x += bw
    for mx in (w * 0.18, w * 0.63):   # minarets
        d.rectangle([mx - 14, h * 0.18, mx + 14, h * 0.62], fill=(70, 45, 95)); d.polygon([(mx - 22, h * 0.18), (mx + 22, h * 0.18), (mx, h * 0.1)], fill=(70, 45, 95))
        d.ellipse([mx - 30, h * 0.28, mx + 30, h * 0.31], fill=(70, 45, 95))
    x = 0
    while x < w:      # near buildings with lit windows
        bw = r.integers(140, 300) * w / 2560; bh = r.integers(200, 480) * h / 1440
        col = tuple(int(v) for v in r.integers(95, 140, 3) * np.array([1.0, 0.75, 0.75]))
        d.rectangle([x, h * 0.78 - bh, x + bw, h], fill=col)
        for wy in np.arange(h * 0.78 - bh + 30, h * 0.95, 70 * h / 1440):
            for wx in np.arange(x + 20, x + bw - 30, 60 * w / 2560):
                if r.random() < 0.5: d.rectangle([wx, wy, wx + 26 * w / 2560, wy + 34 * h / 1440], fill=(255, 205, 110) if r.random() < 0.7 else (60, 40, 50))
        x += bw + r.integers(0, 30)
    for i in range(int(w / 40)):      # string lights
        u = i / (w / 40); yy_ = h * 0.5 + math.sin(u * math.pi * 3) * h * 0.05
        d.ellipse([u * w - 7, yy_ - 7, u * w + 7, yy_ + 7], fill=[(255, 90, 90), (255, 220, 90), (90, 200, 255), (120, 230, 120)][i % 4])
    return im

# ================= YouTube banner =================
B = skyline(2560, 1440)
sh = Image.new("RGBA", B.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).rectangle([0, 480, 2560, 960], fill=(20, 8, 30, 70)); B.alpha_composite(sh)
place(B, figure("zalata", 1.3, "happy", 0.3, 1, "up"), 745, 958)
place(B, figure("tota", 1.25, "happy", 0.25, -1, "up"), 1075, 958)
place(B, figure("shatta", 1.4, "happy", 0.5, 0, "up"), 905, 968)
logo(B, 1600, 680, 165)
lz(B, 1600, 850, "كرتون مصري للعيلة كلها  •  حلقة جديدة كل يوم", 50, (255, 255, 255), ow=8, iw=1)
B.convert("RGB").save(f"{OUT}/youtube_banner.png")

# ================= Facebook cover =================
C = skyline(1640, 624, 5)
place(C, figure("zalata", 1.8, "happy", 0.3, 1, "up"), 250, 640)
place(C, figure("tota", 1.75, "happy", 0.25, -1, "up"), 720, 645)
place(C, figure("shatta", 2.0, "happy", 0.5, 0, "up"), 485, 660)
logo(C, 1210, 300, 150)
lz(C, 1210, 450, "كرتون مصري للعيلة كلها", 54, (255, 255, 255), ow=7, iw=1)
C.convert("RGB").save(f"{OUT}/facebook_cover.png")
print("brand ok")
