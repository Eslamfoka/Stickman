# Shared toolkit for «أزمة منتخب العمارة» parts — exec()'d at the top of each partN.py
import sys, os, math, subprocess, wave, copy
sys.path.insert(0, "/home/claude/s1e1")
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter, ImageFont
from engine import *

os.chdir("/home/claude/repo/Stickman/trend/01")
SSW, SSH = int(W * SS), int(H * SS)
rng = np.random.default_rng(1101)
SERIES = "أزمة منتخب العمارة"
RED_KIT = (205, 35, 45); BLUE_KIT = (40, 95, 205); YELLOW_KIT = (240, 200, 40)
# extra (generic) people are clones of simple-haired base characters with new colors
CH["koko"] = dict(shirt=RED_KIT, hair=(40, 30, 22), scale=0.95)
def extra(base, shirt, hair=None, scale=None):
    k = f"x{len(CH)}"; d = dict(CH[base]); d["shirt"] = shirt
    if hair: d["hair"] = hair
    if scale: d["scale"] = scale
    CH[k] = d; BASE[k] = base; return k
BASE = {}
_draw_char = draw_char
def draw_char(p, who, *a, **kw):
    if who in BASE:   # draw as the base character with this clone's colours
        b = BASE[who]; old = CH[b]; CH[b] = CH[who]
        try: _draw_char(p, b, *a, **kw)
        finally: CH[b] = old
    else: _draw_char(p, who, *a, **kw)

lines, sfx, shots, jumps, shakes = [], [], [], {}, []
def load_lines(keys):
    global AUD, ENV, DUR
    AUD = {k: load_audio(f"audio/{k}.mp3") for k in keys}
    ENV = {k: envelope(v) for k, v in AUD.items()}
    DUR = {k: len(v) / SR for k, v in AUD.items()}
def load_sfx(names):
    global SFXF
    SFXF = {n: load_audio(f"sfx/{n}.mp3") for n in names}
def say(t, k): lines.append((t, k)); return t + DUR[k]
def fx(t, n, g=1.0): sfx.append((t, n, g))
def jump(w, t): jumps.setdefault(w, []).append(t)
def shot(set_, s, e, c0, c1=None, **kw): shots.append(dict(set=set_, start=s, end=e, c0=c0, c1=c1 or c0, **kw))
def cut(t, g=0.4): fx(t - 0.12, "whoosh", g)
def T(k): return [st for st, kk_ in lines if kk_ == k][0]

def shot_at(tt):
    for s_ in shots:
        if s_["start"] <= tt < s_["end"]: return s_
    return shots[-1]
def line_at(tt):
    for st, k in lines:
        if st <= tt < st + DUR[k]: return k, tt - st
    return None, 0
def ease(k, kind=None):
    k = min(1, max(0, k))
    if kind == "crash": return 1 - (1 - min(1, k * 3.5)) ** 3
    return k * k * (3 - 2 * k)
def lerp(a, b, k): return a + (b - a) * k
def kk(tt, a, b): return min(1, max(0, (tt - a) / max(1e-3, b - a)))
def _ld(p): return Image.open(p).convert("RGB").resize((1920, 1080), Image.LANCZOS)

yy, xx = np.mgrid[0:H, 0:W]
vg = 1 - 0.5 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) ** 1.2
VIG = Image.fromarray((np.clip(vg, 0.3, 1) * 255).astype(np.uint8)).convert("RGB")
GRAIN = [np.random.default_rng(i).normal(0, 4.0, (H // 2, W // 2)).astype(np.float32) for i in range(6)]

def cam_at(sh, tt):
    k = ease((tt - sh["start"]) / max(0.01, sh["end"] - sh["start"]), sh.get("ease"))
    cx, cy, z = [a + (b - a) * k for a, b in zip(sh["c0"], sh["c1"])]
    shake = 0
    for st, amp in shakes:
        if 0 <= tt - st < 0.45: shake = max(shake, amp * (1 - (tt - st) / 0.45))
    cw, ch = W / z, H / z
    cx += math.sin(tt * 0.9) * 4 + math.sin(tt * 2.3) * 2; cy += math.sin(tt * 1.3 + 1) * 3
    x0 = min(max(cx - cw / 2, 0), W - cw); y0 = min(max(cy - ch / 2, 0), H - ch)
    if shake:
        x0 = min(max(x0 + rng.normal(0, shake / z), 0), W - cw); y0 = min(max(y0 + rng.normal(0, shake / z), 0), H - ch)
    return x0, y0, z

def bg_crop(src, cam, blur_on=True):
    x0, y0, z = cam; sw, sh = src.size; f = sw / W
    box = (x0 * f, y0 * f, (x0 + W / z) * f, (y0 + H / z) * f)
    if z > 1.7 and blur_on:
        b = tuple(int(v) for v in box); b = (max(0, b[0] - 20), max(0, b[1] - 20), min(sw, b[2] + 20), min(sh, b[3] + 20))
        part = src.crop(b).filter(ImageFilter.GaussianBlur(min(2.5, (z - 1.6) * 1.2)))
        box = (box[0] - b[0], box[1] - b[1], box[2] - b[0], box[3] - b[1]); src = part
    return src.resize((SSW, SSH), Image.BICUBIC, box=box)

def A_(who, pos, **kw):
    x, y, s = pos; d = dict(who=who, x=x, y=y, s=s, look=0, expr="neutral", arms="down"); d.update(kw); return d
def walk_to(a, p0, p1, win, tt, rate=8):
    k = kk(tt, *win); e = ease(k)
    a["x"], a["y"], a["s"] = lerp(p0[0], p1[0], e), lerp(p0[1], p1[1], e), lerp(p0[2], p1[2], e)
    if 0 < k < 1: a["walk"] = tt * rate
    return k
def jump_off(who, tt):
    for j in jumps.get(who, []):
        if 0 <= tt - j < 0.4: return math.sin((tt - j) / 0.4 * math.pi) * 45
    return 0
def expr_of(k, lt):
    e = EXPR.get(k, "neutral")
    if isinstance(e, str): return e
    cur = e[0][1]
    for f, ex in e:
        if lt / DUR[k] >= f: cur = ex
    return cur

HANDS = {"hold": (46, 104), "up": (72, 186), "point": (84, 140), "talk": (60, 126), "hips": (48, 94), "down": (34, 62), "scared": (40, 150)}

def flag(p, x, y, s, kind, tt, ph=0.0):
    """small waving flag on a pole, pole bottom at (x, y)"""
    p.line([(x, y), (x, y - 120 * s)], (90, 70, 50, 255), 3 * s)
    w, h = 70 * s, 46 * s; top = y - 120 * s
    def pt(u, v):
        return (x + u * w, top + v * h + math.sin(tt * 7 + ph + u * 4) * 6 * s * u)
    def band(v0, v1, col):
        p.poly([pt(0, v0), pt(1, v0), pt(1, v1), pt(0, v1)], col, None)
    if kind == "eg":
        band(0, 1 / 3, (206, 17, 38, 255)); band(1 / 3, 2 / 3, (255, 255, 255, 255)); band(2 / 3, 1, (20, 20, 20, 255))
        c = pt(0.5, 0.5); p.ell(c[0], c[1], 5 * s, 5 * s, (200, 160, 40, 255), None)
    else:   # Palestine
        band(0, 1 / 3, (20, 20, 20, 255)); band(1 / 3, 2 / 3, (255, 255, 255, 255)); band(2 / 3, 1, (0, 122, 61, 255))
        p.poly([pt(0, 0), pt(0.38, 0.5), pt(0, 1)], (206, 17, 38, 255), None)
    p.poly([pt(0, 0), pt(1, 0), pt(1, 1), pt(0, 1)], None, INK, 1.5 * s)

def trophy(p, x, y, s):
    """gold cup, base centre at (x, y)"""
    g = (240, 195, 50, 255); d = (170, 120, 20, 255)
    p.rect(x - 26 * s, y - 14 * s, x + 26 * s, y, (90, 60, 30, 255), INK, 2 * s)
    p.rect(x - 8 * s, y - 40 * s, x + 8 * s, y - 14 * s, g, INK, 2 * s)
    p.poly([(x - 40 * s, y - 100 * s), (x + 40 * s, y - 100 * s), (x + 22 * s, y - 46 * s), (x - 22 * s, y - 46 * s)], g, INK, 2.5 * s)
    p.ell(x - 44 * s, y - 82 * s, 12 * s, 14 * s, None, d, 4 * s); p.ell(x + 44 * s, y - 82 * s, 12 * s, 14 * s, None, d, 4 * s)
    p.line([(x - 18 * s, y - 92 * s), (x - 10 * s, y - 60 * s)], (255, 240, 180, 255), 3 * s)

def ball(p, x, y, r):
    p.ell(x, y, r, r, (250, 250, 250, 255), INK, max(1, r * 0.12))
    p.poly([(x, y - r * 0.35), (x + r * 0.33, y - r * 0.1), (x + r * 0.2, y + r * 0.3), (x - r * 0.2, y + r * 0.3), (x - r * 0.33, y - r * 0.1)], (30, 30, 30, 255), None)

def draw_people(layer, set_, tt, cam, sh, people):
    x0, y0, z = cam
    k, lt = line_at(tt)
    for a in sorted(people, key=lambda a: (a["s"], a["y"])):
        who = a["who"]; talking = k is not None and WHO.get(k) == who
        expr = a.get("expr", "neutral")
        if talking: expr = expr_of(k, lt)
        mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
        arms = a.get("arms", "down")
        if talking and not a.get("held") and k in ARMS and not a.get("lockarms"): arms = ARMS[k]
        bob = abs(math.sin(a["walk"])) * 5 * a["s"] if a.get("walk") is not None else 0
        hop = abs(math.sin(tt * 9 + a.get("ph", 0))) * 26 * a["s"] if a.get("hop") else 0
        wy = a["y"] - jump_off(who, tt) - bob - hop - a.get("lift", 0)
        blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11 and expr != "sleepy"
        X = (a["x"] - x0) * z; Y = (wy - y0) * z; s = a["s"] * z
        p = P(layer)
        if not a.get("noshadow"): p.ell(X, (a["y"] - y0) * z + 4 * s, 46 * s, 9 * s, (0, 0, 0, 100), None)
        kit = a.get("kit")
        if kit:
            base = BASE.get(who, who); old = dict(CH[who]); CH[who]["shirt"] = kit
        draw_char(p, who, X, Y, s, expr, mouth, a.get("look", 0), blink, arms, tt, a.get("held"), a.get("lean", 0), a.get("walk"))
        if kit: CH[who].update(old)
        S = s * CH[who]["scale"]
        hip = Y - 62 * S; shy = hip - 72 * S
        if a.get("num"):
            text(layer, X * SS, (shy + 34 * S) * SS, str(a["num"]), max(8, int(22 * S * SS)), (255, 255, 255), (0, 0, 0), max(1, int(1.5 * S * SS)))
        if who == "pasha":
            hy = Y - 190 * S; hx = X
            p.rect(hx - 30 * S, hy - 70 * S, hx + 30 * S, hy - 34 * S, (22, 22, 28, 255), INK, 2.5 * S, 14 * S)
            p.rect(hx - 29 * S, hy - 46 * S, hx + 29 * S, hy - 38 * S, (140, 25, 30, 255), None)
            p.ell(hx, hy - 36 * S, 60 * S, 10 * S, (22, 22, 28, 255), INK, 2.5 * S)
            lk = a.get("look", 0); cxg = hx + (30 if lk >= 0 else -30) * S
            p.line([(cxg - 2 * S, hy + 30 * S), (cxg + (16 if lk >= 0 else -16) * S, hy + 27 * S)], (110, 70, 40, 255), 5 * S)
            ex = cxg + (17 if lk >= 0 else -17) * S
            p.ell(ex, hy + 27 * S, 3.5 * S, 3.5 * S, (255, 170, 40, 255), None)
        hx_, hy_ = HANDS.get(arms, (46, 104))
        if a.get("flag"): flag(p, X + hx_ * S, Y - hy_ * S + 20 * S, S, a["flag"], tt, a.get("ph", 0))
        if a.get("trophy"): trophy(p, X, Y - 196 * S, S * 1.1)
        if a.get("whistle"): p.line([(X + 6 * S, shy + 4 * S), (X + 2 * S, shy + 26 * S)], (220, 220, 220, 255), 1.5 * S); p.ell(X + 2 * S, shy + 28 * S, 4 * S, 3 * S, (200, 200, 205, 255), INK, 1 * S)
        if who == "bondo2" and a.get("lean", 0) < 0:
            for i in range(3):
                u = ((tt * 0.6) + i / 3) % 1
                text(layer, (X + (40 + 30 * u + i * 6) * S) * SS, (Y - (220 + 140 * u) * S) * SS, "Z", int((26 + 18 * i) * S * SS), (255, 255, 255, int(255 * (1 - u))), sw=2)

def tint_layer(layer, tint, lvl=0.97):
    rgb = layer.convert("RGB"); al = layer.getchannel("A")
    c = tuple(int((v * 0.55 + 255 * 0.45) * min(1.0, lvl)) for v in tint)
    rgb = ImageChops.multiply(rgb, Image.new("RGB", rgb.size, c))
    out = rgb.convert("RGBA"); out.putalpha(al); return out

CONF = np.random.default_rng(7).uniform(0, 1, (160, 5))
CCOL = [(230, 40, 50), (250, 210, 40), (60, 160, 230), (60, 200, 90), (240, 240, 240), (240, 120, 200)]
def confetti(img, tt, t0, dens=1.0):
    if tt < t0: return
    d = ImageDraw.Draw(img, "RGBA"); w, h = img.size; u = tt - t0
    for i, (a, b, c, e, f) in enumerate(CONF[:int(160 * dens)]):
        y = ((b * h * 1.2 + u * (180 + 220 * c) * SS) % (h * 1.2)) - 0.1 * h
        x = a * w + math.sin(u * (2 + 3 * e) + i) * 40 * SS
        r = (5 + 6 * f) * SS; ang = u * (4 + 6 * c) + i
        dx, dy = math.cos(ang) * r, math.sin(ang) * r * 0.4
        col = CCOL[i % len(CCOL)]
        d.polygon([(x - dx, y - dy), (x + dy, y - dx * 0.4), (x + dx, y + dy), (x - dy, y + dx * 0.4)], fill=col + (230,))

def ltr(img, x, y, s, size, fill, stroke=(10, 10, 10), sw=3):
    ImageDraw.Draw(img).text((x, y), s, font=ImageFont.truetype(FONT, size), fill=fill, anchor="mm", direction="ltr", stroke_width=sw, stroke_fill=stroke)

HEARTS = np.random.default_rng(3).uniform(0, 1, (14, 3))
def live_ui(fr, tt, t0, ticker="عاجل", comments=()):
    """Sawsan's live-stream phone frame"""
    d = ImageDraw.Draw(fr, "RGBA")
    d.rounded_rectangle([60, 40, 250, 100], 14, fill=(230, 30, 50, 255))
    ltr(fr, 155, 70, "LIVE", 36, (255, 255, 255), sw=0)
    d.rounded_rectangle([270, 40, 460, 100], 14, fill=(0, 0, 0, 140))
    ltr(fr, 365, 70, f"{1200 + int((tt - t0) * 340)}", 30, (255, 255, 255), sw=0)
    for i, (a, b, c) in enumerate(HEARTS):
        u = ((tt - t0) * (0.35 + 0.3 * b) + a) % 1
        x = W - 120 + math.sin(u * 8 + i) * 30; y = H - 200 - u * 520
        col = [(255, 60, 90), (255, 160, 60), (255, 90, 200)][i % 3]
        r = 16 + 10 * c
        d.ellipse([x - r, y - r, x, y], fill=col + (int(255 * (1 - u)),)); d.ellipse([x, y - r, x + r, y], fill=col + (int(255 * (1 - u)),))
        d.polygon([(x - r, y - r / 2), (x + r, y - r / 2), (x, y + r)], fill=col + (int(255 * (1 - u)),))
    for i, c in enumerate(comments):
        st = t0 + 0.6 + i * 0.9
        if tt >= st:
            al = int(230 * min(1, (tt - st) * 3)); y = H - 330 + i * 0 - (len([1 for j in range(len(comments)) if t0 + 0.6 + j * 0.9 <= tt]) - 1 - i) * 70
            if y < 140: continue
            d.rounded_rectangle([60, y - 28, 60 + 22 * len(c) + 60, y + 28], 22, fill=(0, 0, 0, int(al * 0.6)))
            text(fr, 60 + (22 * len(c) + 60) / 2, y, c, 30, (255, 255, 255), sw=0)
    d.rectangle([0, H - 150, W, H - 96], fill=(200, 20, 30, 235))
    d.rectangle([0, H - 150, 260, H - 96], fill=(255, 255, 255, 255))
    text(fr, 130, H - 123, ticker, 38, (200, 20, 30), sw=0)
    scroll = "  •  ".join(["منتخب العمارة", SERIES, "تابعونا"])
    text(fr, (W + 400 - ((tt - t0) * 220) % (W + 600)), H - 123, scroll, 34, (255, 255, 255), sw=0)

def subtitle(img, tt):
    k, _ = line_at(tt)
    if not k: return
    s = SUB[k]
    if len(s) > 44:
        sp = [i for i, ch in enumerate(s) if ch == " "]; c = min(sp, key=lambda i: abs(i - len(s) // 2))
        text(img, W / 2, H - 125, s[:c], 48, sw=5); text(img, W / 2, H - 60, s[c + 1:], 48, sw=5)
    else:
        text(img, W / 2, H - 70, s, 48, sw=5)
def wrap(s, n=24):
    out = [""]
    for w_ in s.split(" "):
        if len(out[-1]) + len(w_) + 1 > n and out[-1]: out.append(w_)
        else: out[-1] = (out[-1] + " " + w_).strip()
    return out
def vertical(fr, tt):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = ImageEnhance.Brightness(small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.35)
    bgv.paste(fr.resize((1080, 608), Image.LANCZOS), (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(255, 214, 90)); d.rectangle([0, 1168, 1080, 1171], fill=(255, 214, 90))
    text(bgv, 540, 300, SERIES, 90, (255, 120, 90), (40, 10, 10), 6)
    text(bgv, 540, 425, EPT, 52, (235, 235, 235))
    k, _ = line_at(tt)
    if k:
        ls_ = wrap(SUB[k])
        if len(ls_) <= 4:
            for i, l in enumerate(ls_): text(bgv, 540, 1290 + i * 80, l, 60, sw=6)
        else:
            for i, l in enumerate(wrap(SUB[k], 30)[:6]): text(bgv, 540, 1270 + i * 64, l, 50, sw=5)
    return bgv
def finish(fr, tt):
    fr = ImageChops.multiply(fr, VIG)
    a = np.asarray(fr, np.float32)
    g = GRAIN[int(tt * FPS) % len(GRAIN)]
    g = np.repeat(np.repeat(g, 2, 0), 2, 1)[..., None]
    return Image.fromarray(np.clip(a + g, 0, 255).astype(np.uint8))
def title_card(tt, sh, l1, l2, l3=""):
    k = (tt - sh["start"]) / (sh["end"] - sh["start"])
    fr = Image.new("RGB", (W, H), (10, 8, 12)); g = lambda c: tuple(int(v * min(1, k * 4)) for v in c)
    text(fr, W / 2, H / 2 - 90, l1, 100, g((255, 214, 90)), (40, 10, 10), 6)
    text(fr, W / 2, H / 2 + 40, l2, 64, g((255, 120, 90)), (30, 5, 5), 5)
    if l3: text(fr, W / 2, H / 2 + 140, l3, 46, g((220, 220, 220)))
    return fr

def _hblur(fr, k):
    n = max(1, int(1 + 40 * k))
    return fr.resize((max(8, W // n), H), Image.BILINEAR).resize((W, H), Image.BILINEAR)
def transit(tt, fr):
    """cinematic transitions: shot['tin'] in ('whip', 'whipl', 'flash', 'zoom', 'fade')"""
    sh = shot_at(tt); i = shots.index(sh); u = tt - sh["start"]
    nxt = shots[i + 1] if i + 1 < len(shots) else None
    tin = sh.get("tin")
    if tin in ("whip", "whipl") and u < 0.22:
        k = 1 - u / 0.22; d = 1 if tin == "whip" else -1
        fr = ImageChops.offset(_hblur(fr, k), int(d * 260 * k * k), 0)
    if nxt is not None and nxt.get("tin") in ("whip", "whipl") and sh["end"] - tt < 0.18:
        k = 1 - (sh["end"] - tt) / 0.18; d = 1 if nxt.get("tin") == "whip" else -1
        fr = ImageChops.offset(_hblur(fr, k), int(-d * 260 * k * k), 0)
    if tin == "flash" and u < 0.3:
        fr = Image.blend(fr, Image.new("RGB", fr.size, (255, 255, 255)), 0.9 * (1 - u / 0.3))
    if tin == "zoom" and u < 0.35:
        k = 1 - ease(u / 0.35); sc = 1 + 0.35 * k
        big = fr.resize((int(W * sc), int(H * sc)), Image.BILINEAR)
        ox, oy = (big.size[0] - W) // 2, (big.size[1] - H) // 2
        z_ = big.crop((ox, oy, ox + W, oy + H))
        fr = Image.blend(z_, z_.filter(ImageFilter.GaussianBlur(14 * k)), min(1, k * 1.5))
    if tin == "fade" and u < 0.45:
        fr = Image.blend(Image.new("RGB", fr.size), fr, ease(u / 0.45))
    if nxt is not None and nxt.get("tin") == "fade" and sh["end"] - tt < 0.35:
        fr = Image.blend(Image.new("RGB", fr.size), fr, ease((sh["end"] - tt) / 0.35))
    return fr

def render(out_h, out_v, stills=None, t0=0.0, t1=None):
    fh = fv = None
    if not stills:
        mk = lambda w, h, o: subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}",
                                   "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
                                   "-pix_fmt", "yuv420p", o], stdin=subprocess.PIPE)
        fh = mk(W, H, out_h); fv = mk(1080, 1920, out_v)
    t1 = TOTAL if t1 is None else t1
    times = stills or [i / FPS for i in range(int(round(t0 * FPS)), int(round(t1 * FPS)))]
    for i, tt in enumerate(times):
        base = transit(tt, frame(tt))
        h = base.copy(); subtitle(h, tt)
        if stills:
            h.save(f"still_h_{tt:.1f}.png"); vertical(base, tt).save(f"still_v_{tt:.1f}.png")
        else:
            fh.stdin.write(h.tobytes()); fv.stdin.write(vertical(base, tt).tobytes())
        if i % 240 == 0: print("frame", i, round(tt, 1), flush=True)
    if fh:
        fh.stdin.close(); fv.stdin.close(); fh.wait(); fv.wait()

def lowpass(x, fc):
    from numpy.fft import rfft, irfft
    X = rfft(x); fq = np.fft.rfftfreq(len(x), 1 / SR); X[fq > fc] *= 0.12; return irfft(X, len(x)).astype(np.float32)
def write_wav(buf, path="mix.wav"):
    buf = np.clip(buf / max(1e-6, np.abs(buf).max()) * 0.95, -1, 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((buf * 32767).astype(np.int16).tobytes())
def mix_lines(buf):
    for st, k in lines: mix_into(buf, AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8, st, 1.0)
def mux(v, out, wav="mix.wav"):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", v, "-i", wav, "-c:v", "copy", "-af",
                    "loudnorm=I=-15:TP=-1.5", "-c:a", "aac", "-b:a", "192k", "-shortest", out], check=True)
def main(tag):
    print("TOTAL", round(TOTAL, 1))
    if sys.argv[1:2] == ["stills"]: render(None, None, [float(v) for v in sys.argv[2:]])
    elif sys.argv[1:2] == ["times"]:
        for s_ in shots: print(s_["set"], round(s_["start"], 2), round(s_["end"], 2))
        for st, k in lines: print(k, round(st, 2))
    elif sys.argv[1:2] == ["part"]:
        i, n = int(sys.argv[2]), int(sys.argv[3]); a = round(TOTAL * i / n * FPS) / FPS; b = round(TOTAL * (i + 1) / n * FPS) / FPS
        render(f"{tag}_h_{i}.mp4", f"{tag}_v_{i}.mp4", None, a, b)
    elif sys.argv[1:2] == ["audio"]: build_audio(f"{tag}_mix.wav")
