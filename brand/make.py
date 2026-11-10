# Brand assets for «شطة وزلطة»: avatar, YouTube banner, Facebook cover, ep-1 thumbnail
import sys, os, math
sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import numpy as np
from engine import *

os.chdir(ROOT + "/brand")
BRAND = "شطة وزلطة"
NB = ROOT + "/trend/01/bg/neighbors.png"

def canvas(w, h, col=(0, 0, 0, 0)):
    return Image.new("RGBA", (int(w * SS), int(h * SS)), col)

def trio(layer, cx, base, s, t=0.3, exprs=("happy", "happy", "happy"), sp=None, arms="up"):
    """Zalata (left), Shatta (centre, front), Tota (right)"""
    p = P(layer)
    sp = sp or 150 * s
    draw_char(p, "zalata", cx - sp, base, s, exprs[0], 0.0, 1, False, arms, t, None)
    draw_char(p, "tota", cx + sp, base, s * 0.98, exprs[2], 0.0, -1, False, arms, t, None)
    draw_char(p, "shatta", cx, base + 18 * s, s * 1.08, exprs[1], 0.35, 0, False, arms, t, None)

def radial(w, h, c0, c1):
    yy, xx = np.mgrid[0:h, 0:w]
    r = np.sqrt(((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2)
    k = np.clip(r / 1.2, 0, 1)[..., None]
    a = np.array(c0)[None, None] * (1 - k) + np.array(c1)[None, None] * k
    return Image.fromarray(a.astype(np.uint8)).convert("RGBA")

def rays(img, cx, cy, n=18, col=(255, 255, 255, 28)):
    d = ImageDraw.Draw(img, "RGBA"); w, h = img.size; R = max(w, h) * 1.5
    for i in range(n):
        a0 = i * 2 * math.pi / n; a1 = a0 + math.pi / n
        d.polygon([(cx, cy), (cx + R * math.cos(a0), cy + R * math.sin(a0)), (cx + R * math.cos(a1), cy + R * math.sin(a1))], fill=col)
    return img

def finish(layer, w, h):
    return layer.resize((w, h), Image.LANCZOS).convert("RGB")

# ---------- 1) avatar (800x800, circle-safe) ----------
w = h = 800
bg = radial(int(w * SS), int(h * SS), (255, 214, 90), (240, 120, 40))
bg.alpha_composite(rays(Image.new("RGBA", bg.size, (0, 0, 0, 0)), w * SS / 2, h * SS * 0.45, 16, (255, 255, 255, 40)))
lay = canvas(w, h); trio(lay, w / 2, 770, 2.15, sp=210, arms="hips")
bg.alpha_composite(lay)
d = ImageDraw.Draw(bg, "RGBA"); d.rounded_rectangle([int(150 * SS), int(625 * SS), int(650 * SS), int(745 * SS)], int(40 * SS), fill=(150, 35, 20, 235))
av = finish(bg, w, h)
text(av, w / 2, 683, BRAND, 84, (255, 225, 120), (60, 10, 5), 6)
av.save("avatar.png")

# ---------- 2) YouTube banner (2560x1440; safe area 1546x423 centred) ----------
W2, H2 = 2560, 1440
src = Image.open(NB).convert("RGB").resize((W2, int(W2 * 720 / 1280)), Image.LANCZOS)
src = src.crop((0, (src.size[1] - H2) // 2, W2, (src.size[1] - H2) // 2 + H2)) if src.size[1] >= H2 else src.resize((W2, H2))
src = ImageEnhance.Brightness(src.filter(ImageFilter.GaussianBlur(6))).enhance(0.55)
ban = src.convert("RGBA")
ov = Image.new("RGBA", ban.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
d.rectangle([0, 490, W2, 950], fill=(20, 10, 10, 90))
ban.alpha_composite(ov)
big = ban.resize((int(W2 * SS), int(H2 * SS)), Image.BICUBIC)
lay = canvas(W2, H2); trio(lay, 930, 975, 1.8, sp=235)
big.alpha_composite(lay)
ban = finish(big, W2, H2)
text(ban, 1720, 640, BRAND, 150, (255, 214, 90), (60, 15, 5), 9)
text(ban, 1720, 790, "كرتون مصري للعيلة كلها", 64, (255, 255, 255), (20, 10, 10), 5)
text(ban, 1720, 880, "حلقة جديدة كل يوم", 54, (255, 150, 110), (20, 10, 10), 4)
ban.save("youtube_banner.png")

# ---------- 3) Facebook cover (1640x624; keep content central) ----------
W3, H3 = 1640, 624
src = Image.open(NB).convert("RGB").resize((W3, int(W3 * 720 / 1280)), Image.LANCZOS)
src = src.crop((0, (src.size[1] - H3) // 2, W3, (src.size[1] - H3) // 2 + H3))
src = ImageEnhance.Brightness(src.filter(ImageFilter.GaussianBlur(5))).enhance(0.55).convert("RGBA")
big = src.resize((int(W3 * SS), int(H3 * SS)), Image.BICUBIC)
lay = canvas(W3, H3); trio(lay, 560, 590, 0.95)
big.alpha_composite(lay)
cov = finish(big, W3, H3)
text(cov, 1100, 250, BRAND, 120, (255, 214, 90), (60, 15, 5), 8)
text(cov, 1100, 370, "كرتون مصري للعيلة كلها", 52, (255, 255, 255), (20, 10, 10), 4)
text(cov, 1100, 445, "حلقة جديدة كل يوم", 44, (255, 150, 110), (20, 10, 10), 4)
cov.save("facebook_cover.png")
print("ok")
