# «فانوس البواب» props drawn by code (no new place): the brass fanous + the stairwell shadow (knotted scarf, swinging hoop, ladle, lit fanous).
import math
from PIL import Image, ImageDraw, ImageFilter, ImageChops, ImageEnhance

BRASS = (196, 150, 70); BRASS_D = (120, 84, 30); GLASS = (255, 214, 120)

def fanous(img, cx, cy, s=1.0, lit=1.0):
    """Brass fanous: pointed dome + top ring + glass body. (cx,cy) = centre of the glass body."""
    d = ImageDraw.Draw(img, "RGBA")
    w, h = 46 * s, 70 * s
    if lit > 0:   # glow
        g = Image.new("RGBA", img.size, (0, 0, 0, 0)); gd = ImageDraw.Draw(g)
        r = 170 * s
        gd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 190, 90, int(90 * lit)))
        g = g.filter(ImageFilter.GaussianBlur(60 * s)); img.paste(g, (0, 0), g); d = ImageDraw.Draw(img, "RGBA")
    d.polygon([(cx - w * .75, cy + h / 2), (cx + w * .75, cy + h / 2), (cx + w * .55, cy + h / 2 + 14 * s), (cx - w * .55, cy + h / 2 + 14 * s)], fill=BRASS_D)
    d.rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], fill=GLASS if lit > 0 else (90, 80, 60), outline=BRASS_D, width=max(2, int(4 * s)))
    for k in (-1, 0, 1): d.line([(cx + k * w / 3, cy - h / 2), (cx + k * w / 3, cy + h / 2)], fill=BRASS_D, width=max(1, int(3 * s)))
    if lit > 0: d.ellipse([cx - 9 * s, cy - 2 * s, cx + 9 * s, cy + 22 * s], fill=(255, 250, 220))
    d.polygon([(cx - w * .8, cy - h / 2), (cx + w * .8, cy - h / 2), (cx, cy - h / 2 - 48 * s)], fill=BRASS, outline=BRASS_D)   # pointed dome
    d.ellipse([cx - 14 * s, cy - h / 2 - 76 * s, cx + 14 * s, cy - h / 2 - 48 * s], outline=BRASS_D, width=max(2, int(5 * s)))  # top ring

def shadow_layer(size, x, y, s=1.0, t=0.0, alpha=200):
    """Silhouette on the wall: knotted scarf head, big hoop earring swinging, ladle in one hand, the fanous (same shape) in the other."""
    L = Image.new("L", size, 0); d = ImageDraw.Draw(L)
    a = alpha
    # body + head with knotted scarf (knot = two lobes on top)
    d.ellipse([x - 48 * s, y - 250 * s, x + 48 * s, y - 150 * s], fill=a)
    d.ellipse([x - 30 * s, y - 286 * s, x - 2 * s, y - 248 * s], fill=a); d.ellipse([x + 2 * s, y - 286 * s, x + 30 * s, y - 248 * s], fill=a)
    d.polygon([(x - 60 * s, y - 150 * s), (x + 60 * s, y - 150 * s), (x + 85 * s, y + 160 * s), (x - 85 * s, y + 160 * s)], fill=a)
    # hoop earring: swings (3 swings over the shot)
    sw = math.sin(t * 2 * math.pi * 1.4) * 0.5
    hx, hy = x - 48 * s + math.sin(sw) * 22 * s, y - 176 * s + math.cos(sw) * 22 * s
    d.ellipse([hx - 22 * s, hy - 22 * s, hx + 22 * s, hy + 22 * s], outline=a, width=max(3, int(8 * s)))
    # arm + ladle (left)
    d.line([(x - 55 * s, y - 120 * s), (x - 150 * s, y - 40 * s), (x - 165 * s, y - 210 * s)], fill=a, width=int(20 * s))
    d.ellipse([x - 200 * s, y - 280 * s, x - 132 * s, y - 220 * s], fill=a)
    # arm + fanous (right): same silhouette as the prop (dome + ring)
    d.line([(x + 55 * s, y - 120 * s), (x + 140 * s, y - 70 * s)], fill=a, width=int(20 * s))
    fx, fy = x + 150 * s, y - 30 * s
    d.rectangle([fx - 34 * s, fy - 50 * s, fx + 34 * s, fy + 50 * s], fill=a)
    d.polygon([(fx - 40 * s, fy - 50 * s), (fx + 40 * s, fy - 50 * s), (fx, fy - 110 * s)], fill=a)
    d.ellipse([fx - 16 * s, fy - 142 * s, fx + 16 * s, fy - 110 * s], outline=a, width=max(3, int(7 * s)))
    return L.filter(ImageFilter.GaussianBlur(3 * s))

def cast_shadow(img, L, tint=(8, 6, 6), glow=None):
    """glow=(x,y,r): warm fanous light spilling on the wall around the shadow."""
    if glow:
        gx, gy, r = glow; g = Image.new("L", img.size, 0); ImageDraw.Draw(g).ellipse([gx - r, gy - r, gx + r, gy + r], fill=150)
        g = g.filter(ImageFilter.GaussianBlur(r * 0.45))
        img = Image.composite(ImageChops.screen(img, Image.new("RGB", img.size, (210, 140, 60))), img, g)
    return Image.composite(Image.new("RGB", img.size, tint), img, L)
