import json, math, subprocess, random, wave, os
import paths  # noqa: F401  (repo root + Windows FriBiDi DLL path; must come before PIL)
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

W, H, FPS, SR = 1920, 1080, 24, 44100
SS = 1.5
FONT = paths.ROOT + "/brand/fonts/DejaVuSans-Bold.ttf"  # bundled copy of the Linux DejaVu font (same look everywhere)
INK = (22, 22, 22, 255)

# ======================= drawing primitives =======================
class P:
    def __init__(self, img):
        self.img = img; self.d = ImageDraw.Draw(img)
    def S(self, v): return int(round(v * SS))
    def pts(self, ps): return [(self.S(x), self.S(y)) for x, y in ps]
    def line(self, ps, c=INK, w=4):
        self.d.line(self.pts(ps), fill=c, width=max(1, self.S(w)), joint="curve")
        for x, y in (ps[0], ps[-1]):
            r = w / 2
            self.d.ellipse([self.S(x - r), self.S(y - r), self.S(x + r), self.S(y + r)], fill=c)
    def poly(self, ps, fill, out=INK, w=3):
        self.d.polygon(self.pts(ps), fill=fill)
        if out: self.line(list(ps) + [ps[0]], out, w)
    def ell(self, cx, cy, rx, ry, fill, out=INK, w=3):
        box = [self.S(cx - rx), self.S(cy - ry), self.S(cx + rx), self.S(cy + ry)]
        self.d.ellipse(box, fill=fill, outline=out, width=self.S(w) if out else 0)
    def rect(self, x0, y0, x1, y1, fill, out=None, w=3, r=0):
        self.d.rounded_rectangle([self.S(x0), self.S(y0), self.S(x1), self.S(y1)], radius=self.S(r),
                                 fill=fill, outline=out, width=self.S(w) if out else 0)
    def arc(self, cx, cy, rx, ry, a0, a1, c=INK, w=3):
        self.d.arc([self.S(cx - rx), self.S(cy - ry), self.S(cx + rx), self.S(cy + ry)], a0, a1, fill=c, width=self.S(w))

def text(img, x, y, s, size, fill=(255, 255, 255), stroke=(15, 15, 15), sw=4, anchor="mm"):
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(FONT, size)
    d.text((x, y), s, font=f, fill=fill, anchor=anchor, stroke_width=sw, stroke_fill=stroke,
           direction="rtl", language="ar")

# ======================= characters =======================
CH = {
    "shatta": dict(shirt=(216, 90, 48), hair=(139, 58, 30), scale=1.0),
    "zalata": dict(shirt=(99, 153, 34), hair=(44, 44, 42), scale=1.0),
    "tota":   dict(shirt=(212, 83, 126), hair=(61, 42, 30), scale=0.74),
    "nana":   dict(shirt=(83, 74, 183), hair=(93, 202, 165), scale=0.95),
    "bondo2": dict(shirt=(160, 104, 58), hair=(250, 250, 250), scale=1.0),
    "fahmy": dict(shirt=(62, 70, 92), hair=(24, 22, 26), scale=0.82),
    "roshdy": dict(shirt=(140, 110, 80), hair=(40, 32, 26), scale=1.0),
    "youngnana": dict(shirt=(190, 120, 140), hair=(50, 38, 30), scale=0.86),
    "sawsan": dict(shirt=(236, 150, 40), hair=(150, 40, 50), scale=0.92),
    "pasha": dict(shirt=(30, 30, 36), hair=(200, 200, 205), scale=1.05),
    "abdo": dict(shirt=(120, 120, 130), hair=(30, 28, 26), scale=1.1),
}
WHITE = (255, 255, 255, 255)

def C(c): return tuple(c) + (255,) if len(c) == 3 else c

def draw_char(p, who, x, y, s=1.0, expr="neutral", mouth=0.0, look=0, blink=False,
              arms="down", t=0.0, held=None, lean=0.0, walk=None, eat=None):
    c = CH[who]; s *= c["scale"]
    breath = math.sin(t * 2.2 + x) * 1.6 * s
    hip = y - 62 * s; sh = hip - 72 * s + breath * 0.4; hr = 46 * s
    hy = sh - 10 * s - hr + breath
    hx = x + lean * 18 * s
    lw = max(3, 5 * s)
    gal = who in ("nana", "bondo2", "youngnana", "sawsan")
    shirt = C(c["shirt"]); hair = C(c["hair"])
    # legs
    if walk is not None and gal:
        a1 = math.sin(walk) * 16 * s; l1 = max(0, math.cos(walk)) * 8 * s; l2 = max(0, -math.cos(walk)) * 8 * s
        p.line([(x - 6 * s, y - 30 * s), (x + a1, y - l1)], INK, lw)
        p.line([(x + 6 * s, y - 30 * s), (x - a1, y - l2)], INK, lw)
    elif walk is not None:
        for ph in (walk, walk + math.pi):
            fx = x + math.sin(ph) * 24 * s; lift = max(0, math.cos(ph)) * 12 * s
            kx = (x + fx) / 2 + 6 * s; ky = (hip + y) / 2 - lift * 0.5
            p.line([(x, hip), (kx, ky), (fx, y - lift)], INK, lw)
            p.line([(fx, y - lift), (fx + 10 * s, y - lift)], INK, lw)
    elif gal:
        p.line([(x - 12 * s, y - 30 * s), (x - 14 * s, y)], INK, lw)
        p.line([(x + 12 * s, y - 30 * s), (x + 14 * s, y)], INK, lw)
    else:
        p.line([(x, hip), (x - 17 * s, y)], INK, lw); p.line([(x, hip), (x + 17 * s, y)], INK, lw)
        p.line([(x - 17 * s, y), (x - 27 * s, y)], INK, lw); p.line([(x + 17 * s, y), (x + 27 * s, y)], INK, lw)
    # arms
    lsh, rsh = (x - 22 * s, sh + 8 * s), (x + 22 * s, sh + 8 * s)
    sw = math.sin(t * 5.5) * 10 * s
    A = {
        "down": ((x - 34 * s, sh + 72 * s), (x + 34 * s, sh + 72 * s)),
        "talk": ((x - 50 * s, sh + 52 * s), (x + 60 * s, sh + 8 * s + sw)),
        "up": ((x - 72 * s, sh - 52 * s), (x + 72 * s, sh - 52 * s)),
        "point": ((x - 38 * s, sh + 68 * s), (x + 84 * s, sh - 6 * s)),
        "hips": ((x - 48 * s, sh + 40 * s), (x + 48 * s, sh + 40 * s)),
        "scared": ((x - 30 * s, sh - 30 * s), (x + 30 * s, sh - 30 * s)),
        "hold": ((x - 36 * s, sh + 70 * s), (x + 46 * s, sh + 30 * s)),
        "shush": ((x - 36 * s, sh + 70 * s), (hx + 4 * s, hy + 26 * s)),
    }
    la, ra = A.get(arms, A["down"])
    chip_hand = None
    if eat is not None:
        bag = (x + 44 * s, sh + 46 * s); ra = bag
        top = (x + 40 * s, sh + 10 * s); mth = (hx + 6 * s, hy + 30 * s)
        if eat < 0.3: u = 0; la = (top[0] - 6 * s + math.sin(eat * 60) * 4 * s, top[1] + 6 * s)
        elif eat < 0.55:
            u = (eat - 0.3) / 0.25; u = u * u * (3 - 2 * u); la = (top[0] + (mth[0] - top[0]) * u, top[1] + (mth[1] - top[1]) * u - math.sin(u * math.pi) * 18 * s)
        elif eat < 0.75: la = mth
        else:
            u = (eat - 0.75) / 0.25; la = (mth[0] + (top[0] - mth[0]) * u, mth[1] + (top[1] - mth[1]) * u)
        if 0.3 <= eat < 0.62: chip_hand = la
    # elbows for nicer arms
    def arm(sh_, hand, side):
        ex = (sh_[0] + hand[0]) / 2 + side * 10 * s; ey = (sh_[1] + hand[1]) / 2 + 8 * s
        p.line([sh_, (ex, ey), hand], INK, lw)
        p.ell(hand[0], hand[1], 5 * s, 5 * s, INK, None)
    arm(lsh, la, -1); arm(rsh, ra, 1)
    # body
    if gal:
        p.poly([(x - 24 * s, sh), (x + 24 * s, sh), (x + 44 * s, y - 26 * s), (x - 44 * s, y - 26 * s)], shirt, INK, 2.5 * s)
    elif who == "tota":
        p.poly([(x - 18 * s, sh), (x + 18 * s, sh), (x + 40 * s, hip + 12 * s), (x - 40 * s, hip + 12 * s)], shirt, INK, 2.5 * s)
    else:
        p.poly([(x - 26 * s, sh), (x + 26 * s, sh), (x + 30 * s, hip + 4 * s), (x - 30 * s, hip + 4 * s)], shirt, INK, 2.5 * s)
        if who == "zalata":
            p.poly([(x - 9 * s, sh), (x, sh + 12 * s), (x + 9 * s, sh)], WHITE, INK, 2 * s)
        if who == "shatta":
            p.line([(x, sh + 6 * s), (x, hip)], (170, 60, 30, 255), 2 * s)
        if who == "pasha":
            p.poly([(x - 12 * s, sh), (x, sh + 30 * s), (x + 12 * s, sh)], WHITE, INK, 2 * s)
            p.poly([(x - 4 * s, sh + 6 * s), (x + 4 * s, sh + 6 * s), (x + 6 * s, sh + 44 * s), (x, sh + 52 * s), (x - 6 * s, sh + 44 * s)], (150, 20, 30, 255), INK, 1.5 * s)
            p.line([(x - 22 * s, sh + 34 * s), (x - 14 * s, sh + 40 * s)], (230, 190, 60, 255), 3 * s)
            p.rect(x + 10 * s, sh + 18 * s, x + 22 * s, sh + 22 * s, (230, 230, 230, 255), None)
        if who == "abdo":
            p.line([(x - 14 * s, sh), (x - 10 * s, sh + 20 * s)], (210, 210, 215, 255), 4 * s)
            p.line([(x + 14 * s, sh), (x + 10 * s, sh + 20 * s)], (210, 210, 215, 255), 4 * s)
        if who == "fahmy":
            p.poly([(x - 12 * s, sh), (x, sh + 30 * s), (x + 12 * s, sh)], WHITE, INK, 2 * s)
            p.line([(x - 12 * s, sh), (x - 4 * s, hip)], INK, 2 * s); p.line([(x + 12 * s, sh), (x + 4 * s, hip)], INK, 2 * s)
            p.poly([(x - 13 * s, sh + 3 * s), (x, sh + 8 * s), (x - 13 * s, sh + 13 * s)], (180, 30, 40, 255), INK, 1.5 * s)
            p.poly([(x + 13 * s, sh + 3 * s), (x, sh + 8 * s), (x + 13 * s, sh + 13 * s)], (180, 30, 40, 255), INK, 1.5 * s)
            p.ell(x, sh + 8 * s, 3 * s, 3 * s, (150, 20, 30, 255), INK, 1 * s)
            for yy_ in (sh + 40 * s, sh + 56 * s): p.ell(x + 2 * s, yy_, 2.2 * s, 2.2 * s, (220, 200, 120, 255), None)
    # props
    if held == "key":
        p.ell(ra[0], ra[1] - 6 * s, 7 * s, 7 * s, None, (210, 170, 60, 255), 3 * s)
        p.line([(ra[0], ra[1] + 1 * s), (ra[0], ra[1] + 20 * s)], (210, 170, 60, 255), 3 * s)
    elif held == "torch":
        p.rect(ra[0] - 5 * s, ra[1] - 20 * s, ra[0] + 5 * s, ra[1] + 4 * s, (60, 60, 70, 255), INK, 2 * s, 2 * s)
    elif held == "paper":
        p.rect(ra[0] - 14 * s, ra[1] - 30 * s, ra[0] + 16 * s, ra[1] + 6 * s, (245, 240, 220, 255), INK, 2 * s)
    elif held == "lantern":
        p.line([(ra[0], ra[1]), (ra[0], ra[1] + 14 * s)], INK, 2 * s)
        p.rect(ra[0] - 11 * s, ra[1] + 14 * s, ra[0] + 11 * s, ra[1] + 44 * s, (255, 210, 110, 255), INK, 2.5 * s, 3 * s)
        p.ell(ra[0], ra[1] + 29 * s, 5 * s, 8 * s, (255, 250, 220, 255), None)
        p.rect(ra[0] - 13 * s, ra[1] + 12 * s, ra[0] + 13 * s, ra[1] + 17 * s, INK, None)
    elif held == "broom":
        p.line([(ra[0] - 10 * s, ra[1] - 40 * s), (ra[0] + 30 * s, ra[1] + 70 * s)], (150, 110, 60, 255), 4 * s)
        p.poly([(ra[0] + 18 * s, ra[1] + 62 * s), (ra[0] + 44 * s, ra[1] + 58 * s), (ra[0] + 58 * s, ra[1] + 92 * s), (ra[0] + 20 * s, ra[1] + 98 * s)],
               (210, 180, 90, 255), INK, 2 * s)
    elif held == "basket":
        p.arc(ra[0], ra[1] + 6 * s, 16 * s, 16 * s, 180, 360, INK, 3 * s)
        p.poly([(ra[0] - 24 * s, ra[1] + 6 * s), (ra[0] + 24 * s, ra[1] + 6 * s), (ra[0] + 18 * s, ra[1] + 40 * s), (ra[0] - 18 * s, ra[1] + 40 * s)],
               (196, 150, 80, 255), INK, 2 * s)
        p.line([(ra[0] - 20 * s, ra[1] + 18 * s), (ra[0] + 20 * s, ra[1] + 18 * s)], (150, 105, 50, 255), 2 * s)
        p.ell(ra[0] - 8 * s, ra[1] + 2 * s, 8 * s, 7 * s, (90, 160, 60, 255), INK, 1.5 * s)
    elif held == "photo":
        p.rect(ra[0] - 16 * s, ra[1] - 30 * s, ra[0] + 16 * s, ra[1] + 6 * s, (120, 80, 40, 255), INK, 2 * s)
        p.rect(ra[0] - 12 * s, ra[1] - 26 * s, ra[0] + 12 * s, ra[1] + 2 * s, (205, 180, 140, 255), None)
    elif held == "nbpen":
        p.rect(ra[0] - 4 * s, ra[1] - 28 * s, ra[0] + 22 * s, ra[1] + 4 * s, (250, 248, 230, 255), INK, 2 * s)
        p.line([(ra[0] + 18 * s, ra[1] - 34 * s), (ra[0] + 18 * s, ra[1] - 8 * s)], (220, 30, 30, 255), 3 * s)
    elif held == "phone":
        p.rect(ra[0] - 7 * s, ra[1] - 22 * s, ra[0] + 7 * s, ra[1] + 2 * s, (30, 30, 36, 255), INK, 2 * s, 2 * s)
        p.rect(ra[0] - 5 * s, ra[1] - 19 * s, ra[0] + 5 * s, ra[1] - 1 * s, (190, 225, 255, 255), None)
    elif held == "slipper":
        p.ell(ra[0], ra[1] - 4 * s, 9 * s, 18 * s, (60, 140, 200, 255), INK, 2 * s)
        p.line([(ra[0] - 7 * s, ra[1] - 10 * s), (ra[0] + 7 * s, ra[1] - 10 * s)], (240, 240, 240, 255), 3 * s)
    elif held == "tray":
        p.ell(ra[0], ra[1] - 4 * s, 34 * s, 8 * s, (200, 205, 215, 255), INK, 2.5 * s)
        for i in range(5):
            p.ell(ra[0] - 20 * s + i * 10 * s, ra[1] - 12 * s - (i % 2) * 4 * s, 7 * s, 5 * s, (226, 160, 70, 255), (150, 90, 30, 255), 1.5 * s)
    elif held == "sweet":
        p.ell(ra[0], ra[1] - 6 * s, 9 * s, 6 * s, (226, 160, 70, 255), (150, 90, 30, 255), 1.5 * s)
    elif held == "keys":
        p.ell(ra[0], ra[1] - 4 * s, 8 * s, 8 * s, None, (210, 170, 60, 255), 2.5 * s)
        p.line([(ra[0] + 4 * s, ra[1]), (ra[0] + 10 * s, ra[1] + 18 * s)], (210, 170, 60, 255), 3 * s)
        p.line([(ra[0] - 4 * s, ra[1]), (ra[0] - 9 * s, ra[1] + 16 * s)], (190, 190, 200, 255), 3 * s)
    elif held == "chipsbag":
        bx, by = ra; bw, bh = 30 * s, 50 * s
        top = by - bh * 0.9; bot = by + bh * 0.5
        zz = [(bx - bw + i * bw / 4, top - (5 * s if i % 2 else 0)) for i in range(9)]
        body = zz + [(bx + bw * 1.08, bot - 6 * s), (bx + bw * 0.9, bot), (bx - bw * 0.9, bot), (bx - bw * 1.08, bot - 6 * s)]
        for i in range(4):
            cx_ = bx - bw * 0.55 + i * bw * 0.36
            p.ell(cx_, top - 2 * s - (i % 2) * 5 * s, 9 * s, 6 * s, (242, 196, 72, 255), (170, 120, 30, 255), 1.5 * s)
        p.poly(body, (36, 92, 190, 255), INK, 2.5 * s)
        p.poly([(bx - bw * 0.95, top + 4 * s), (bx + bw * 0.95, top + 4 * s), (bx + bw * 0.98, top + 12 * s), (bx - bw * 0.98, top + 12 * s)], (230, 40, 40, 255), None)
        p.ell(bx + 3 * s, by - 6 * s, 15 * s, 13 * s, (250, 205, 70, 255), (150, 100, 20, 255), 2 * s)
        p.ell(bx + 3 * s, by - 6 * s, 9 * s, 7 * s, (252, 225, 120, 255), None)
        p.line([(bx - bw * 0.7, top + 18 * s), (bx - bw * 0.62, bot - 10 * s)], (255, 255, 255, 110), 4 * s)
        p.line([(bx + bw * 0.5, top + 20 * s), (bx + bw * 0.6, top + 34 * s)], (10, 30, 80, 160), 1.5 * s)
        p.ell(ra[0] - 26 * s, ra[1] + 2 * s, 6 * s, 6 * s, INK, None)
    elif held == "chips":
        p.poly([(ra[0] - 16 * s, ra[1] - 34 * s), (ra[0] + 18 * s, ra[1] - 34 * s), (ra[0] + 14 * s, ra[1] + 8 * s),
                (ra[0] - 12 * s, ra[1] + 8 * s)], (230, 50, 40, 255), INK, 2.5 * s)
        p.ell(ra[0] + 1 * s, ra[1] - 14 * s, 8 * s, 8 * s, (255, 210, 60, 255), INK, 2 * s)
    elif held == "notebook":
        p.rect(ra[0] - 4 * s, ra[1] - 28 * s, ra[0] + 22 * s, ra[1] + 4 * s, (250, 248, 230, 255), INK, 2 * s)
    if eat is not None:
        arm(lsh, la, -1)
    # head back
    if who == "tota":
        p.ell(hx - hr, hy - 8 * s, 12 * s, 12 * s, hair, INK, 2 * s)
        p.ell(hx + hr, hy - 8 * s, 12 * s, 12 * s, hair, INK, 2 * s)
    if who in ("nana", "youngnana"):
        p.ell(hx, hy + 4 * s, hr + 14 * s, hr + 16 * s, hair, INK, 3 * s)
    if who == "sawsan":
        for a_ in range(11):
            ang = math.pi * (0.95 + a_ * 1.1 / 10)
            p.ell(hx + math.cos(ang) * (hr + 4 * s), hy - 2 * s + math.sin(ang) * (hr + 6 * s), 17 * s, 17 * s, hair, INK, 2.5 * s)
        p.ell(hx - hr - 2 * s, hy + 16 * s, 15 * s, 22 * s, hair, INK, 2.5 * s)
        p.ell(hx + hr + 2 * s, hy + 16 * s, 15 * s, 22 * s, hair, INK, 2.5 * s)
    p.ell(hx, hy, hr, hr, WHITE, INK, 3.5 * s)
    # hair
    if who == "shatta":
        pts = [(hx - hr - 2 * s, hy + 2 * s)]
        for i in range(9):
            a = math.pi + i * math.pi / 8; r = hr + (16 if i % 2 else 2) * s
            pts.append((hx + math.cos(a) * r, hy + math.sin(a) * r))
        pts.append((hx + hr + 2 * s, hy + 2 * s))
        for i in range(8, -1, -1):
            a = math.pi + i * math.pi / 8
            pts.append((hx + math.cos(a) * (hr - 14 * s), hy - 6 * s + math.sin(a) * (hr - 20 * s)))
        p.poly(pts, hair, INK, 2.5 * s)
    elif who in ("zalata", "roshdy"):
        p.poly([(hx - hr - 1 * s, hy - 4 * s), (hx - hr + 6 * s, hy - 30 * s), (hx - 10 * s, hy - hr - 4 * s),
                (hx + 20 * s, hy - hr - 2 * s), (hx + hr, hy - 20 * s), (hx + hr + 1 * s, hy - 4 * s),
                (hx + 18 * s, hy - 22 * s), (hx - 20 * s, hy - 18 * s)], hair, INK, 2.5 * s)
    elif who == "tota":
        p.poly([(hx - hr, hy - 2 * s), (hx - hr + 8 * s, hy - 32 * s), (hx, hy - hr - 2 * s), (hx + hr - 8 * s, hy - 32 * s),
                (hx + hr, hy - 2 * s), (hx + 12 * s, hy - 24 * s), (hx - 12 * s, hy - 24 * s)], hair, INK, 2.5 * s)
    elif who == "fahmy":
        p.poly([(hx - hr - 1 * s, hy - 2 * s), (hx - hr + 2 * s, hy - 26 * s), (hx - 18 * s, hy - hr - 4 * s), (hx + 14 * s, hy - hr - 6 * s),
                (hx + hr - 2 * s, hy - 26 * s), (hx + hr + 1 * s, hy - 4 * s), (hx + hr - 8 * s, hy - 22 * s), (hx - 8 * s, hy - 28 * s),
                (hx - hr + 8 * s, hy - 20 * s)], hair, INK, 2.5 * s)
        p.line([(hx - 8 * s, hy - 28 * s), (hx - 14 * s, hy - hr - 2 * s)], (90, 90, 100, 255), 2 * s)
        p.arc(hx + 14 * s, hy - hr + 8 * s, 14 * s, 6 * s, 200, 320, (140, 140, 160, 255), 2.5 * s)
    elif who == "pasha":
        p.poly([(hx - hr - 1 * s, hy - 4 * s), (hx - hr + 4 * s, hy - 30 * s), (hx - 6 * s, hy - hr - 6 * s), (hx + 26 * s, hy - hr - 2 * s),
                (hx + hr, hy - 22 * s), (hx + hr + 1 * s, hy - 4 * s), (hx + 20 * s, hy - 26 * s), (hx - 26 * s, hy - 24 * s)], hair, INK, 2.5 * s)
    elif who == "abdo":
        p.arc(hx, hy, hr - 2 * s, hr - 2 * s, 200, 340, hair, 8 * s)
    elif who == "bondo2":
        p.poly([(hx - hr + 4 * s, hy - 18 * s), (hx - 20 * s, hy - hr - 6 * s), (hx + 20 * s, hy - hr - 6 * s),
                (hx + hr - 4 * s, hy - 18 * s)], WHITE, INK, 2.5 * s)
    # eyes
    ex = 15 * s; ey = hy + 2 * s; lx = look * 4 * s
    big = expr in ("scared", "shock")
    er = 12 * s if big else 9 * s
    if expr == "sleepy" or blink:
        for sx in (-1, 1): p.arc(hx + sx * ex, ey, 8 * s, 5 * s, 0, 180, INK, 3 * s)
    else:
        for sx in (-1, 1):
            p.ell(hx + sx * ex, ey, er * 0.82, er, WHITE, INK, 2.5 * s)
            pr = 2.6 * s if big else 4.2 * s
            p.ell(hx + sx * ex + lx, ey + 1.5 * s, pr, pr, INK, None)
            if expr in ("flat", "smug", "sad"):
                p.d.pieslice([p.S(hx + sx * ex - er), p.S(ey - er - 1), p.S(hx + sx * ex + er), p.S(ey + (0 if expr != "sad" else -2 * s))],
                             180, 360, fill=WHITE)
                p.line([(hx + sx * ex - er * 0.85, ey), (hx + sx * ex + er * 0.85, ey)], INK, 3 * s)
    if who in ("zalata", "nana"):
        for sx in (-1, 1):
            if who == "zalata":
                p.rect(hx + sx * ex - 13 * s, ey - 11 * s, hx + sx * ex + 13 * s, ey + 11 * s, None, INK, 2.5 * s, 3 * s)
            else:
                p.ell(hx + sx * ex, ey, 12 * s, 12 * s, None, INK, 2.5 * s)
        p.line([(hx - 2 * s, ey), (hx + 2 * s, ey)], INK, 2.5 * s)
    # brows
    by = ey - 17 * s
    if expr in ("angry", "shout"):
        p.line([(hx - ex - 11 * s, by - 5 * s), (hx - ex + 9 * s, by + 4 * s)], INK, 4 * s)
        p.line([(hx + ex + 11 * s, by - 5 * s), (hx + ex - 9 * s, by + 4 * s)], INK, 4 * s)
    elif expr in ("scared", "shock", "sad"):
        p.line([(hx - ex - 10 * s, by + 2 * s), (hx - ex + 8 * s, by - 6 * s)], INK, 3.5 * s)
        p.line([(hx + ex + 10 * s, by + 2 * s), (hx + ex - 8 * s, by - 6 * s)], INK, 3.5 * s)
    elif expr == "smug":
        p.line([(hx - ex - 10 * s, by), (hx - ex + 9 * s, by)], INK, 3.5 * s)
        p.line([(hx + ex - 9 * s, by - 2 * s), (hx + ex + 10 * s, by - 9 * s)], INK, 3.5 * s)
    elif expr == "happy":
        p.arc(hx - ex, by + 4 * s, 10 * s, 6 * s, 200, 340, INK, 3.5 * s)
        p.arc(hx + ex, by + 4 * s, 10 * s, 6 * s, 200, 340, INK, 3.5 * s)
    else:
        p.line([(hx - ex - 9 * s, by), (hx - ex + 9 * s, by)], INK, 3 * s)
        p.line([(hx + ex - 9 * s, by), (hx + ex + 9 * s, by)], INK, 3 * s)
    if who == "pasha":
        p.poly([(hx - 22 * s, hy + 20 * s), (hx, hy + 15 * s), (hx + 22 * s, hy + 20 * s), (hx + 12 * s, hy + 25 * s), (hx, hy + 21 * s), (hx - 12 * s, hy + 25 * s)], (190, 190, 195, 255), INK, 1.5 * s)
        p.ell(hx + hr - 2 * s, hy + 6 * s, 3 * s, 3 * s, (230, 190, 60, 255), None)
    if who == "abdo":
        p.line([(hx - 26 * s, ey - 16 * s), (hx + 26 * s, ey - 16 * s)], INK, 5 * s)
        for i_ in range(14):
            p.ell(hx - 20 * s + (i_ % 7) * 7 * s, hy + 32 * s + (i_ // 7) * 6 * s, 1.2 * s, 1.2 * s, (90, 90, 90, 255), None)
    if who == "sawsan":
        for sx in (-1, 1):
            p.ell(hx + sx * 16 * s, hy - hr + 6 * s, 13 * s, 9 * s, (30, 30, 40, 255), INK, 2 * s)
            p.ell(hx + sx * 16 * s - 4 * s, hy - hr + 3 * s, 4 * s, 2.5 * s, (200, 220, 255, 200), None)
            p.ell(hx + sx * (hr + 1 * s), hy + 26 * s, 6 * s, 6 * s, None, (230, 190, 60, 255), 2.5 * s)
        p.line([(hx - 4 * s, hy - hr + 5 * s), (hx + 4 * s, hy - hr + 5 * s)], INK, 2 * s)
    if who == "bondo2":
        p.poly([(hx - 18 * s, hy + 18 * s), (hx, hy + 14 * s), (hx + 18 * s, hy + 18 * s), (hx + 10 * s, hy + 24 * s),
                (hx, hy + 20 * s), (hx - 10 * s, hy + 24 * s)], (60, 50, 44, 255), INK, 2 * s)
    if who == "fahmy":
        p.poly([(hx, hy + 19 * s), (hx - 9 * s, hy + 19 * s), (hx - 17 * s, hy + 23 * s), (hx - 21 * s, hy + 17 * s),
                (hx - 17 * s, hy + 20 * s), (hx - 9 * s, hy + 16 * s), (hx, hy + 16 * s)], INK, INK, 1 * s)
        p.poly([(hx, hy + 19 * s), (hx + 9 * s, hy + 19 * s), (hx + 17 * s, hy + 23 * s), (hx + 21 * s, hy + 17 * s),
                (hx + 17 * s, hy + 20 * s), (hx + 9 * s, hy + 16 * s), (hx, hy + 16 * s)], INK, INK, 1 * s)
    # mouth
    my = hy + 28 * s
    if mouth > 0.06:
        k = 1.3 if expr in ("shout", "shock") else 1.0
        p.ell(hx + look * 2 * s, my, (7 + 3 * mouth) * s * k, (2.5 + 10 * mouth) * s * k, (130, 24, 24, 255), INK, 2.5 * s)
        if mouth > 0.4:
            p.ell(hx + look * 2 * s, my + (2 + 6 * mouth) * s * k, 5 * s, 2.5 * s, (220, 90, 90, 255), None)
    elif expr in ("happy", "smug"):
        p.arc(hx + (4 * s if expr == "smug" else 0), my - 6 * s, 11 * s, 8 * s, 20, 160, INK, 3 * s)
    elif expr in ("scared", "shock"):
        p.ell(hx, my, 5 * s, 6 * s, (130, 24, 24, 255), INK, 2.5 * s)
    elif expr == "sad":
        p.arc(hx, my + 6 * s, 9 * s, 6 * s, 200, 340, INK, 3 * s)
    else:
        p.line([(hx - 8 * s, my), (hx + 8 * s, my)], INK, 3 * s)
    if expr in ("scared", "shock"):
        p.ell(hx + hr * 0.8, hy - hr * 0.5, 4 * s, 7 * s, (150, 200, 255, 255), INK, 1.5 * s)
    if chip_hand:
        cx_, cy_ = chip_hand
        p.poly([(cx_ - 11 * s, cy_ - 4 * s), (cx_ - 3 * s, cy_ - 12 * s), (cx_ + 10 * s, cy_ - 9 * s), (cx_ + 12 * s, cy_ + 2 * s),
                (cx_ + 2 * s, cy_ + 9 * s), (cx_ - 9 * s, cy_ + 6 * s)], (246, 200, 76, 255), (160, 110, 25, 255), 1.6 * s)
        p.ell(cx_ - 2 * s, cy_ - 2 * s, 2 * s, 1.5 * s, (200, 140, 40, 255), None)
        p.ell(cx_ + 5 * s, cy_ + 2 * s, 1.5 * s, 1.5 * s, (200, 140, 40, 255), None)

# ======================= back view (walking away from camera) — S2E5 =======================
def draw_back(p, who, x, y, s=1.0, t=0.0, walk=None, arms="down", held=None):
    """Character seen from behind: no face, back of the hair, arms swinging. Same proportions as draw_char."""
    c = CH[who]; s *= c["scale"]
    breath = math.sin(t * 2.2 + x) * 1.6 * s
    hip = y - 62 * s; sh = hip - 72 * s + breath * 0.4; hr = 46 * s
    hy = sh - 10 * s - hr + breath; hx = x
    lw = max(3, 5 * s)
    gal = who in ("nana", "bondo2", "youngnana", "sawsan")
    shirt = C(c["shirt"]); hair = C(c["hair"])
    # legs (feet point away: short heel stubs only)
    if walk is not None:
        for ph in (walk, walk + math.pi):
            fx = x + math.sin(ph) * 9 * s; lift = max(0, math.cos(ph)) * 14 * s
            p.line([(x + (fx - x) * 0.3, hip), (fx, y - lift)], INK, lw)
            p.line([(fx, y - lift), (fx, y - lift + 4 * s)], INK, lw + 2 * s)
    elif gal:
        p.line([(x - 12 * s, y - 30 * s), (x - 14 * s, y)], INK, lw); p.line([(x + 12 * s, y - 30 * s), (x + 14 * s, y)], INK, lw)
    else:
        p.line([(x, hip), (x - 14 * s, y)], INK, lw); p.line([(x, hip), (x + 14 * s, y)], INK, lw)
    # arms swing opposite to legs
    sw_ = math.sin(walk) * 16 * s if walk is not None else 0
    lsh, rsh = (x - 22 * s, sh + 8 * s), (x + 22 * s, sh + 8 * s)
    if arms == "up":
        la, ra = (x - 70 * s, sh - 50 * s), (x + 70 * s, sh - 50 * s)
    elif arms == "wave":
        la, ra = (x - 34 * s, sh + 72 * s), (x + 64 * s, sh - 60 * s + math.sin(t * 9) * 12 * s)
    else:
        la, ra = (x - 30 * s - sw_ * 0.3, sh + 72 * s + sw_), (x + 30 * s + sw_ * 0.3, sh + 72 * s - sw_)
    for a_, h_, sd in ((lsh, la, -1), (rsh, ra, 1)):
        ex = (a_[0] + h_[0]) / 2 + sd * 8 * s; ey = (a_[1] + h_[1]) / 2 + 6 * s
        p.line([a_, (ex, ey), h_], INK, lw); p.ell(h_[0], h_[1], 5 * s, 5 * s, INK, None)
    if held == "phone":
        p.rect(ra[0] - 7 * s, ra[1] - 22 * s, ra[0] + 7 * s, ra[1] + 2 * s, (30, 30, 36, 255), INK, 2 * s, 2 * s)
    # body
    if gal:
        p.poly([(x - 24 * s, sh), (x + 24 * s, sh), (x + 44 * s, y - 26 * s), (x - 44 * s, y - 26 * s)], shirt, INK, 2.5 * s)
    elif who == "tota":
        p.poly([(x - 18 * s, sh), (x + 18 * s, sh), (x + 40 * s, hip + 12 * s), (x - 40 * s, hip + 12 * s)], shirt, INK, 2.5 * s)
    else:
        p.poly([(x - 26 * s, sh), (x + 26 * s, sh), (x + 30 * s, hip + 4 * s), (x - 30 * s, hip + 4 * s)], shirt, INK, 2.5 * s)
        p.line([(x - 16 * s, sh + 4 * s), (x + 16 * s, sh + 4 * s)], (0, 0, 0, 60), 2 * s)   # collar seam
    # head: white skull, then the hair seen from behind
    if who == "tota":
        p.ell(hx - hr - 2 * s, hy - 4 * s, 13 * s, 13 * s, hair, INK, 2 * s); p.ell(hx + hr + 2 * s, hy - 4 * s, 13 * s, 13 * s, hair, INK, 2 * s)
    if who in ("nana", "youngnana", "sawsan"):
        p.ell(hx, hy + 4 * s, hr + 14 * s, hr + 16 * s, hair, INK, 3 * s); return
    p.ell(hx, hy, hr, hr, WHITE, INK, 3.5 * s)
    p.ell(hx - hr + 1 * s, hy + 6 * s, 5 * s, 9 * s, WHITE, INK, 2 * s); p.ell(hx + hr - 1 * s, hy + 6 * s, 5 * s, 9 * s, WHITE, INK, 2 * s)  # ears
    if who == "shatta":
        pts = []
        for i in range(17):
            a = math.pi * 0.92 + i * math.pi * 1.16 / 16; r = hr + (14 if i % 2 else 3) * s
            pts.append((hx + math.cos(a) * r, hy - 2 * s + math.sin(a) * r))
        pts += [(hx + hr * 0.95, hy + hr * 0.5), (hx + hr * 0.5, hy + hr * 0.8), (hx, hy + hr * 0.86), (hx - hr * 0.5, hy + hr * 0.8), (hx - hr * 0.95, hy + hr * 0.5)]
        p.poly(pts, hair, INK, 2.5 * s)
    elif who in ("zalata", "roshdy", "pasha", "fahmy", "tota", "abdo"):
        # hair covers the whole back of the head down to the nape (only a white strip of neck shows)
        cover = [(hx - hr - 1 * s, hy)] + [(hx + math.cos(math.pi + math.pi * i / 20) * (hr + 1 * s), hy + math.sin(math.pi + math.pi * i / 20) * (hr + 1 * s)) for i in range(21)]
        cover += [(hx + hr - 2 * s, hy + hr * 0.55), (hx + hr * 0.5, hy + hr * 0.78), (hx, hy + hr * 0.84), (hx - hr * 0.5, hy + hr * 0.78), (hx - hr + 2 * s, hy + hr * 0.55)]
        p.poly(cover, hair, INK, 2.5 * s)
        if who == "zalata":   # glasses temples
            p.line([(hx - hr + 2 * s, hy + 2 * s), (hx - hr - 6 * s, hy + 4 * s)], INK, 2.5 * s)
            p.line([(hx + hr - 2 * s, hy + 2 * s), (hx + hr + 6 * s, hy + 4 * s)], INK, 2.5 * s)
        if who == "tota":
            p.line([(hx, hy - hr + 2 * s), (hx, hy + 10 * s)], (0, 0, 0, 90), 2 * s)   # parting
    elif who == "bondo2":
        p.poly([(hx - hr + 4 * s, hy - 18 * s), (hx - 20 * s, hy - hr - 6 * s), (hx + 20 * s, hy - hr - 6 * s), (hx + hr - 4 * s, hy - 18 * s)], WHITE, INK, 2.5 * s)

# ======================= Safeeh — Roshdy's tin robot (S2E5 on) =======================
TIN = (168, 174, 180, 255); TIN_D = (120, 126, 134, 255); RUST = (150, 92, 52, 255)
EYE_COL = {"red": (255, 40, 30), "green": (60, 255, 110), "off": (60, 50, 50)}
def draw_safeeh(p, x, y, s=1.0, t=0.0, eye="red", eye_on=1.0, mouth=0.0, look=0, walk=None, arms="down",
                drawer=0.0, lean=0.0, sad=False, reach=None):
    """Old boxy tin robot. x,y = feet (ground). ~ same height as an adult character (head top ≈ y-300*s)."""
    lw = max(2, 3 * s)
    hum = math.sin(t * 3.0) * 1.2 * s
    # legs: two pipe legs with boxy feet, clunky step (only one foot lifts at a time)
    for sd, ph in ((-1, 0), (1, math.pi)):
        lift = max(0, math.sin((walk or 0) + ph)) * 16 * s if walk is not None else 0
        fwd = math.cos((walk or 0) + ph) * 10 * s if walk is not None else 0
        lx = x + sd * 26 * s + fwd
        p.rect(lx - 9 * s, y - 92 * s - lift, lx + 9 * s, y - 14 * s - lift, TIN_D, INK, lw)
        for k in range(3): p.line([(lx - 9 * s, y - 70 * s + k * 18 * s - lift), (lx + 9 * s, y - 70 * s + k * 18 * s - lift)], INK, 1.5 * s)
        p.rect(lx - 22 * s, y - 18 * s - lift, lx + 22 * s, y - lift, TIN, INK, lw, 4 * s)
    by = y - 90 * s + hum
    # arms (pipes with elbow bolts and two-finger claws)
    sh_l, sh_r = (x - 62 * s, by - 120 * s), (x + 62 * s, by - 120 * s)
    sw_ = math.sin(walk) * 14 * s if walk is not None else 0
    H_ = {"down": ((x - 76 * s, by - 20 * s + sw_), (x + 76 * s, by - 20 * s - sw_)),
          "up": ((x - 110 * s, by - 210 * s), (x + 110 * s, by - 210 * s)),
          "block": ((x - 150 * s, by - 110 * s), (x + 150 * s, by - 110 * s)),
          "point": ((x - 76 * s, by - 20 * s), (x + 150 * s, by - 130 * s)),
          "chest": ((x - 76 * s, by - 20 * s), (x + 10 * s, by - 70 * s))}
    la, ra = H_.get(arms, H_["down"])
    if reach is not None: ra = reach
    for sh_, hd, sd in ((sh_l, la, -1), (sh_r, ra, 1)):
        el = ((sh_[0] + hd[0]) / 2 + sd * 14 * s, (sh_[1] + hd[1]) / 2 + 10 * s)
        p.line([sh_, el], INK, 13 * s); p.line([sh_, el], TIN_D, 9 * s)
        p.line([el, hd], INK, 13 * s); p.line([el, hd], TIN_D, 9 * s)
        p.ell(el[0], el[1], 8 * s, 8 * s, TIN, INK, lw)
        p.line([hd, (hd[0] + sd * 10 * s, hd[1] + 14 * s)], INK, 5 * s); p.line([hd, (hd[0] - sd * 4 * s, hd[1] + 16 * s)], INK, 5 * s)
        p.ell(hd[0], hd[1], 9 * s, 9 * s, TIN, INK, lw)
    # torso box
    tx0, tx1, ty0, ty1 = x - 62 * s, x + 62 * s, by - 150 * s, by
    p.rect(tx0, ty0, tx1, ty1, TIN, INK, lw * 1.2, 8 * s)
    p.rect(tx0 + 4 * s, ty0 + 4 * s, tx0 + 18 * s, ty1 - 4 * s, (205, 210, 215, 255), None, 0, 4 * s)   # highlight
    for rx in (tx0 + 10 * s, tx1 - 10 * s):
        for ry in (ty0 + 10 * s, ty1 - 10 * s): p.ell(rx, ry, 3 * s, 3 * s, TIN_D, INK, 1 * s)
    p.ell(tx1 - 28 * s, ty0 + 30 * s, 9 * s, 6 * s, RUST, None); p.ell(tx0 + 30 * s, ty1 - 22 * s, 6 * s, 4 * s, RUST, None)
    # chest drawer (slides out toward camera = grows + shifts down)
    dx0, dx1, dy0, dy1 = x - 34 * s, x + 34 * s, ty0 + 52 * s, ty0 + 96 * s
    p.rect(dx0, dy0, dx1, dy1, (40, 40, 44, 255), INK, lw, 3 * s)
    if drawer > 0:
        o = drawer * 26 * s
        p.rect(dx0 - o * 0.4, dy0 + o * 0.5, dx1 + o * 0.4, dy1 + o, TIN, INK, lw, 3 * s)
        if drawer > 0.6:   # the little tape inside
            cx_, cy_ = x, (dy0 + dy1) / 2 + o * 0.7
            p.rect(cx_ - 22 * s, cy_ - 11 * s, cx_ + 22 * s, cy_ + 11 * s, (40, 34, 30, 255), INK, 1.5 * s, 2 * s)
            for sx in (-1, 1): p.ell(cx_ + sx * 10 * s, cy_, 6 * s, 6 * s, (230, 225, 210, 255), INK, 1 * s)
    else:
        p.ell(x, (dy0 + dy1) / 2, 4 * s, 4 * s, (220, 190, 80, 255), INK, 1 * s)
    for k in range(4): p.line([(x - 30 * s, ty0 + 18 * s + k * 7 * s), (x + 30 * s, ty0 + 18 * s + k * 7 * s)], INK, 2 * s)   # speaker grill
    # neck spring
    hx = x + look * 6 * s + lean * 14 * s; hb = ty0 - 4 * s
    for k in range(4): p.ell(hx, hb - k * 6 * s, 14 * s, 4 * s, None, INK, 2 * s)
    # head box with a dark screen face
    hy0, hy1 = hb - 96 * s, hb - 22 * s
    tilt = -10 * s if sad else 0
    p.rect(hx - 56 * s, hy0 + tilt * 0.3, hx + 56 * s, hy1, TIN, INK, lw * 1.2, 10 * s)
    p.rect(hx - 44 * s, hy0 + 10 * s, hx + 44 * s, hy1 - 10 * s, (18, 20, 24, 255), INK, lw, 6 * s)
    for sd in (-1, 1): p.rect(hx + sd * 56 * s - 6 * s, hy0 + 26 * s, hx + sd * 56 * s + 6 * s, hy0 + 52 * s, TIN_D, INK, 1.5 * s, 2 * s)  # ear bolts
    # eyes = round lamps
    col = EYE_COL.get(eye, EYE_COL["red"]); on = max(0.0, min(1.0, eye_on))
    for sd in (-1, 1):
        ex, ey = hx + sd * 22 * s + look * 4 * s, hy0 + 34 * s + (4 * s if sad else 0)
        for r_, a_ in ((15, 70), (10, 150), (6.5, 255)):
            p.ell(ex, ey, r_ * s, r_ * s * (0.6 if sad else 1.0), col + (int(a_ * on),), None)
        if on < 0.2: p.ell(ex, ey, 8 * s, 8 * s, (55, 45, 45, 255), INK, 1.5 * s)
    # mouth grill lights up with speech
    mb = min(1.0, mouth * 1.4)
    for k in range(5):
        hh = (3 + 9 * mb * (0.6 + 0.4 * math.sin(k * 1.7 + t * 30))) * s
        mx = hx - 20 * s + k * 10 * s; my = hy1 - 22 * s
        p.rect(mx - 3 * s, my - hh, mx + 3 * s, my + hh, col + (int(90 + 165 * mb),) if mb > 0.05 else (70, 70, 76, 255), None, 0, 1 * s)
    # antenna with blinking bulb
    p.line([(hx + 24 * s, hy0), (hx + 30 * s, hy0 - 36 * s)], INK, 3 * s)
    bl = 0.5 + 0.5 * math.sin(t * 4)
    p.ell(hx + 30 * s, hy0 - 40 * s, 6 * s, 6 * s, (255, int(80 + 120 * bl), 60, 255), INK, 1.5 * s)

# ======================= audio analysis =======================
def load_audio(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()

def envelope(a):
    hop = SR // FPS
    n = len(a) // hop + 1
    e = np.array([np.sqrt(np.mean(a[i * hop:(i + 1) * hop] ** 2) + 1e-12) for i in range(n)])
    m = np.percentile(e, 95) + 1e-6
    e = np.clip((e / m - 0.12) / 0.75, 0, 1)
    return e

# ======================= sfx synthesis =======================
def sfx_knock():
    n = int(SR * 0.45); t = np.arange(n) / SR
    body = np.sin(2 * np.pi * 70 * t) * np.exp(-t * 14) + 0.6 * np.sin(2 * np.pi * 140 * t) * np.exp(-t * 22)
    noise = np.random.default_rng(1).normal(0, 1, n) * np.exp(-t * 60) * 0.5
    return (body + noise) * 0.9

def sfx_tick():
    n = int(SR * 0.05); t = np.arange(n) / SR
    return np.random.default_rng(2).normal(0, 1, n) * np.exp(-t * 300) * 0.35

def sfx_powercut():
    n = int(SR * 1.1); t = np.arange(n) / SR
    f = 120 * np.exp(-t * 1.5)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sign(np.sin(ph)) * 0.25 * np.exp(-t * 2.2)

def sfx_paper():
    n = int(SR * 1.2); t = np.arange(n) / SR
    x = np.random.default_rng(3).normal(0, 1, n)
    x = np.convolve(x, np.ones(6) / 6, mode="same")
    return x * 0.25 * np.sin(np.pi * t / 1.2)

def sfx_boom():
    n = int(SR * 2.5); t = np.arange(n) / SR
    low = np.sin(2 * np.pi * 45 * t) * np.exp(-t * 1.6)
    hi = np.sin(2 * np.pi * (900 + 300 * t) * t) * np.exp(-t * 3) * 0.12
    return (low + hi) * 0.9

def drone(dur):
    n = int(SR * dur); t = np.arange(n) / SR
    x = (np.sin(2 * np.pi * 55 * t) + 0.7 * np.sin(2 * np.pi * 55.7 * t) + 0.4 * np.sin(2 * np.pi * 82.4 * t + np.sin(t * 0.3) * 2))
    x *= 0.5 + 0.5 * np.sin(2 * np.pi * t / 9) ** 2
    nz = np.convolve(np.random.default_rng(4).normal(0, 1, n), np.ones(40) / 40, mode="same")
    return (x * 0.05 + nz * 0.04)

def mix_into(buf, clip, t, gain=1.0):
    i = int(t * SR)
    if i >= len(buf): return
    j = min(len(buf), i + len(clip))
    buf[i:j] += clip[:j - i] * gain
