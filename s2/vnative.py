# Native-vertical helpers for the «عمارة نعناعة» episodes (growth rules 29 + 32, user 23/11).
# The old episodes drew a 1920x1080 frame and letterboxed it inside 9:16 with a permanent title.
# Here the vertical is cut from the SUPERSAMPLED scene (2880x1620 when SS=1.5) around whoever speaks,
# so the characters fill the phone screen; subtitles are short phrase chunks (1–2 lines) with a
# speaker-name pill; the title is NOT kept on screen.
#   from vnative import *      (after `from engine import *`, with sys.path pointing at s2/)
import math, re
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageChops, ImageFont

VW, VH = 1080, 1920
LZ_FONT = None
def set_font(path):
    global LZ_FONT; LZ_FONT = path

NAMES = {"shatta": ("شطة", (255, 140, 80)), "zalata": ("زلطة", (140, 210, 80)), "tota": ("توتة", (255, 130, 190)),
         "nana": ("نعناعة", (150, 140, 255)), "bondo2": ("بندق", (230, 170, 110)), "aziza": ("عزيزة", (255, 110, 170)),
         "sawsan": ("سوسن", (236, 150, 40)), "fahmy": ("فهمي", (120, 190, 230)), "pasha": ("الباشا", (200, 170, 90)),
         "abdo": ("عبده", (170, 170, 170)), "roshdy": ("رشدي", (230, 90, 70)), "safeeh": ("صفيح", (150, 200, 220))}

# ---------- spotlight: lift the background around the characters (rule 32) ----------
def spotlight(img_ss, points, lift=1.28, sat=0.92):
    """img_ss: RGB supersampled bg; points: [(X, Y, R)] in img_ss pixels (center of the body, radius)."""
    if not points: return img_ss
    w, h = img_ss.size; sw, sh = max(1, w // 8), max(1, h // 8)
    yy, xx = np.mgrid[0:sh, 0:sw] * 8.0
    m = np.zeros((sh, sw), np.float32)
    for X, Y, R in points:
        m = np.maximum(m, np.exp(-((xx - X) ** 2 / (R * R * 0.55) + (yy - Y) ** 2 / (R * R * 1.3))))
    mask = Image.fromarray((np.clip(m, 0, 1) * 255).astype(np.uint8), "L").resize((w, h), Image.BILINEAR)
    bright = ImageEnhance.Color(ImageEnhance.Brightness(img_ss).enhance(lift)).enhance(sat)
    return Image.composite(bright, img_ss, mask)

# ---------- speaker-follow crop ----------
class Follow:
    def __init__(self): self.x = None; self.last = None; self.shot = None
    def step(self, tt, shot_id, target):
        snap = self.x is None or self.shot != shot_id or self.last is None or abs(tt - self.last) > 0.2
        self.x = target if snap else self.x + (target - self.x) * 0.10
        self.last, self.shot = tt, shot_id
        return self.x

def crop_vertical(img_ss, cx, zoom=1.0):
    """cut a 9:16 window centred on x=cx (img_ss pixels) at full height / zoom and scale it to 1080x1920"""
    w, h = img_ss.size; ch = h / zoom; cw = ch * VW / VH
    x0 = min(max(cx - cw / 2, 0), w - cw); y0 = (h - ch) / 2
    return img_ss.resize((VW, VH), Image.LANCZOS, box=(x0, y0, x0 + cw, y0 + ch))

_VIG = None
def vig(fr, dark=False):
    global _VIG
    if _VIG is None:
        yy, xx = np.mgrid[0:VH, 0:VW]
        v = 1 - 0.45 * (((xx - VW / 2) / (VW / 2)) ** 2 * 0.6 + ((yy - VH / 2) / (VH / 2)) ** 2) ** 1.2
        _VIG = (Image.fromarray((np.clip(v, 0.3, 1) * 255).astype(np.uint8)).convert("RGB"),
                Image.fromarray((np.clip(v * 0.85, 0.15, 1) * 255).astype(np.uint8)).convert("RGB"))
    return ImageChops.multiply(fr, _VIG[1 if dark else 0])

# ---------- phrase subtitles ----------
def phrases(s):
    parts = [p.strip() for p in re.split(r"(?<=[…!؟?\.،:])\s+", s) if p.strip()]
    out = []
    for p in parts:                                    # long phrase → split on the space nearest the middle
        while len(p) > 34:
            sp = [i for i, c in enumerate(p) if c == " "]
            if not sp: break
            c = min(sp, key=lambda i: abs(i - len(p) // 2)); out.append(p[:c]); p = p[c + 1:]
        out.append(p)
    return out

def chunk_times(text, env, fps):
    """phrase start offsets spread over the voiced part of the line, proportional to length"""
    ph = phrases(text)
    e = np.asarray(env, np.float32); thr = max(0.05, float(e.max()) * 0.12)
    voiced = np.where(e > thr)[0]
    a = voiced[0] / fps if len(voiced) else 0.0; b = (voiced[-1] + 1) / fps if len(voiced) else len(e) / fps
    L = [max(4, len(p)) for p in ph]; tot = sum(L); offs = []; acc = 0
    for l in L: offs.append(a + (b - a) * acc / tot - 0.05); acc += l
    return list(zip([max(0.0, o) for o in offs], ph))

def _pop(u):
    return 0.0 if u <= 0 else (1 + 0.22 * math.sin(min(1, u) * math.pi)) if u < 1 else 1.0

def sub_v(fr, k, lt, chunks, who, cy=1430, size=74):
    """draw the current phrase of line k (offset lt) + the speaker pill"""
    if k is None or k not in chunks: return
    cur = None
    for off, txt in chunks[k]:
        if lt >= off: cur = (off, txt)
    if cur is None: return
    off, txt = cur; sc = _pop((lt - off) / 0.14)
    f = ImageFont.truetype(LZ_FONT, max(8, int(size * max(0.2, sc))))
    lay = Image.new("RGBA", fr.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    kw = dict(font=f, direction="rtl", language="ar", stroke_width=max(4, size // 10), stroke_fill=(10, 10, 10, 255), anchor="mm")
    wmax = fr.size[0] * 0.9
    tw = d.textlength(txt, font=f, direction="rtl", language="ar")
    if tw > wmax:
        f = ImageFont.truetype(LZ_FONT, max(8, int(size * max(0.2, sc) * wmax / tw))); kw["font"] = f
    d.text((fr.size[0] / 2, cy), txt, fill=(255, 255, 255, 255), **kw)
    if who in NAMES:
        nm, col = NAMES[who]; fn = ImageFont.truetype(LZ_FONT, int(size * 0.6))
        nw = d.textlength(nm, font=fn, direction="rtl", language="ar"); nx, ny = fr.size[0] / 2, cy - size * 0.98
        d.rounded_rectangle([nx - nw / 2 - 20, ny - size * 0.37, nx + nw / 2 + 20, ny + size * 0.37], int(size * 0.3), fill=col + (235,))
        d.text((nx, ny), nm, font=fn, fill=(20, 12, 8, 255), anchor="mm", direction="rtl", language="ar")
    fr.paste(lay, (0, 0), lay)

def big_text(fr, x, y, s, size, fill=(255, 255, 255), stroke=(15, 10, 8), alpha=255):
    lay = Image.new("RGBA", fr.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(LZ_FONT, size)
    wmax = fr.size[0] * 0.92; tw = d.textlength(s, font=f, direction="rtl", language="ar")
    if tw > wmax: f = ImageFont.truetype(LZ_FONT, int(size * wmax / tw))
    d.text((x, y), s, font=f, fill=fill + (alpha,), anchor="mm", direction="rtl", language="ar", stroke_width=max(3, size // 12), stroke_fill=stroke + (alpha,))
    fr.paste(lay, (0, 0), lay)
