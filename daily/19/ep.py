# «يوميات شطة وزلطة» — «اللمبة» (27/11) — growth_rules: native 9:16, phrase subs + yellow key word + speaker name,
#   motion+sound on frame 1, ONE ask end card («تابع بندق وعزيزة»), own cover, laugh = SOUND only.
# Canonical «أوضة بندق وعزيزة» (bandaq_room.png) at night, ceiling bulb ON. The door creaks open — Aziza comes home;
# Bandaq jumps off the sofa and switches the bulb OFF. In the dark (moonlight beam from the window) he recites a love verse,
# then confesses the electricity bill… she sees through it: he wants her «جمعية» money. Hearts → banknotes → red ✗.
# He switches the light back ON, embarrassed: «اللمبة أرخص… ومش محتاجة قصايد.» → audience laugh (sound only) → end card.
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/daily/19")
SERIES = "يوميات شطة وزلطة"; EPT = "اللمبة"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"
SFXF = {n: load_audio(ROOT + f"/trend/01/sfx/{n}.mp3") for n in ("whoosh", "gasp")}
SUB = {"A1": "طفّيت اللمبة ليه يا راجل؟", "B1": "نورك يا عزيزة ملا الدار… واللمبة جنبك بتنطفي من العار!", "A2": "يا سلام…",
       "B2": "يعني نطفّي اللمبات كام يوم… فاتورة الكهربا الشهر ده نار، وأنا مزنوق.",
       "A3": "فهمتك من أول «نور»! عينك على الجمعية اللي لسه واخداها! والنبي لو بقيت عنترة بن شداد وفضلت تغزّل فيا لحد العصر… قرش واحد من الجمعية مش هتشوفه!",
       "B3": "اللمبة أرخص… ومش محتاجة قصايد.", "GROUP": ""}
CHUNKS = {"A1": [(0.0, "طفّيت اللمبة ليه يا راجل؟", "اللمبة")],
          "B1": [(0.0, "نورك يا عزيزة ملا الدار…", "نورك"), (2.79, "واللمبة جنبك بتنطفي من العار!", "العار")],
          "A2": [(0.0, "يا سلام…", "يا سلام")],
          "B2": [(0.0, "يعني نطفّي اللمبات كام يوم…", "كام يوم"), (3.33, "فاتورة الكهربا الشهر ده نار،", "نار"), (5.24, "وأنا مزنوق.", "مزنوق")],
          "A3": [(0.0, "فهمتك من أول «نور»!", "فهمتك"), (2.11, "عينك على الجمعية اللي لسه واخداها!", "الجمعية"),
                 (4.51, "والنبي لو بقيت عنترة بن شداد", "عنترة"), (6.81, "وفضلت تغزّل فيا لحد العصر…", "لحد العصر"),
                 (9.28, "قرش واحد من الجمعية مش هتشوفه!", "قرش واحد")],
          "B3": [(0.0, "اللمبة أرخص…", "أرخص"), (1.74, "ومش محتاجة قصايد.", "قصايد")]}
WHO = {k: ("aziza" if k.startswith("A") else "bondo2") for k in SUB}; WHO["GROUP"] = "-"
NAME = {"bondo2": ("بندق", (230, 170, 110)), "aziza": ("عزيزة", (255, 110, 170))}
EXPR = {"A1": "angry", "B1": [(0, "happy"), (2.8, "sad")], "A2": "flat", "B2": [(0, "scared"), (3.3, "sad"), (5.2, "scared")],
        "A3": [(0, "smug"), (2.1, "angry"), (4.5, "smug"), (9.2, "shout")], "B3": [(0, "scared"), (1.7, "flat")], "GROUP": "laugh"}
load_lines(list(SUB))
ROOM = _ld(ROOT + "/daily/bg/bandaq_room.png")

def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
SOFA = (560, 1370, 800)
DOOR = (187, 208, 422, 752)                 # door leaf in the canonical picture
SWITCH = (1528, 612)                        # wall switch right of the sofa (new prop, drawn in code)
BULB = (1090, 330)                           # bare bulb hanging from the ceiling
FEET = 1060

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
TW = lambda z, cy=640, cx=965: (cx, cy, z)
DOOR_OPEN = 0.05; JUMP = 0.30; OFF = 1.30                     # frame 1: creak + door opens; he leaps; CLICK — dark
ENTER = (0.35, 2.4)                                            # she walks in from the door to her mark
t = say(1.55, "A1") + 0.15
shot("room", 0.0, JUMP + 0.2, TW(1.0, 540), TW(1.02, 545, 980), v=(TW(1.78, 640, 400), TW(1.8, 650, 430)))
shot("room", JUMP + 0.2, OFF, TW(1.02, 545, 980), TW(1.1, 570, 1020), tin="whip", v=(TW(1.8, 700, 1300), TW(1.85, 720, 1380)))
shot("room", OFF, t, TW(1.25, 640, 1060), TW(1.9, 790, 760), v=(TW(1.85, 790, 760), TW(1.95, 790, 740)))
POEM = t; t = say(t + 0.05, "B1") + 0.15                       # moonlight spotlight on him, hearts
shot("room", POEM, t, TW(1.6, 740, 1300), TW(1.85, 760, 1380), tin="zoom", v=(TW(1.8, 750, 1380), TW(1.95, 770, 1400)))
s = t; t = say(t + 0.05, "A2") + 0.15
shot("room", s, t, TW(2.0, 795, 740), TW(2.08, 795, 740), tin="whipl", v=(TW(1.95, 790, 730), TW(2.05, 790, 730)))
s = t; t = say(t + 0.1, "B2") + 0.15; BILL = T("B2") + 3.33
shot("room", s, t, TW(1.3, 700, 1060), TW(1.5, 760, 1200), tin="whip", v=(TW(1.85, 780, 1380), TW(1.95, 790, 1400)))
REV = t; t = say(t + 0.1, "A3") + 0.15; MONEY = T("A3") + 2.11; ANTAR = T("A3") + 4.51; ASR = T("A3") + 6.81; NOPE = T("A3") + 9.28
shakes.append((REV + 0.1, 14)); shakes.append((NOPE + 0.05, 18))
shot("room", REV, MONEY, TW(2.1, 790, 740), TW(1.98, 795, 740), ease="crash", v=(TW(2.1, 790, 730), TW(1.98, 795, 730)))
shot("room", MONEY, ANTAR, TW(1.3, 680, 1060), TW(1.38, 690, 1060), v=(TW(1.8, 720, 1380), TW(1.85, 730, 1380)))
shot("room", ANTAR, NOPE, TW(1.8, 760, 1330), TW(1.6, 740, 1060), tin="whip", v=(TW(1.85, 740, 1380), TW(1.9, 790, 740)))
shot("room", NOPE, t, TW(2.12, 790, 740), TW(2.05, 792, 740), ease="crash", v=(TW(2.1, 790, 730), TW(2.04, 792, 730)))
ON = t + 0.25                                                    # CLICK — light back on
s = t; t = say(ON + 0.45, "B3") + 0.05
shot("room", s, t, TW(1.2, 640, 1060), TW(1.55, 760, 1250), tin="flash", v=(TW(1.85, 760, 1380), TW(2.05, 790, 1400)))
LAUGH = t - 0.1; say(LAUGH, "GROUP"); LU = min(2.6, DUR["GROUP"])
shot("room", t, LAUGH + LU, TW(1.55, 760, 1250), TW(1.2, 640, 1060), v=(TW(2.05, 790, 1400), TW(1.8, 760, 1060)))
t = LAUGH + LU
shot("end", t, t + 2.6, None, v=None); t += 2.6
TOTAL = t

def light_at(tt):
    """1 = bulb on, 0 = off (flicker on the click)"""
    if tt < OFF: return 1.0
    if tt < ON: return 0.0
    u = tt - ON; return 1.0 if u > 0.25 else (0.0 if int(u * 30) % 2 else 1.0)

# ---------------- who is where ----------------
AZM = (720, FEET, 2.2)                     # her mark
BDS = (1140, 800, 1.8)                      # seated on the sofa
BDM = (1400, FEET, 2.25)                    # standing by the switch
def walker(p0, p1, win, tt, rate=8):
    u = ease(kk(tt, *win)); return lerp(p0[0], p1[0], u), lerp(p0[1], p1[1], u), lerp(p0[2], p1[2], u), (tt * rate if 0 < kk(tt, *win) < 1 else None)
def cast(tt):
    """(who, x, y, s, look, arms, held, walk, sit)"""
    C = []
    ax, ay, as_, aw = walker((300, 752, 1.0), AZM, ENTER, tt, 9)
    aarms = arms_at([(0, "hold"), (ENTER[1], "hips"), (T("A1"), "point"), (T("A1") + 1.6, "hips"), (T("A2"), "hips"),
                     (REV, "point"), (MONEY, "hips"), (ANTAR, "talk"), (ASR, "hips"), (NOPE - 0.15, "raise"), (ON + 0.4, "hips")], tt, 0.18)
    held = "slipper" if NOPE - 0.15 <= tt < ON + 0.4 else None
    C.append(("aziza", ax, ay, as_, 1, aarms if aw is None else "down", held, aw, 0))
    if tt < JUMP:
        C.append(("bondo2", *BDS, -1, "down", None, None, -1))
    else:
        bx, by, bs, bw = walker((BDS[0], 1010, 2.0), BDM, (JUMP, OFF - 0.25), tt, 14)
        look = 1 if tt < OFF + 0.35 or (ON - 0.35 <= tt < ON + 0.3) else -1
        barms = arms_at([(0, "scared"), (OFF - 0.3, "point"), (OFF + 0.35, "down"), (POEM, "up"), (POEM + 2.79, "clap"),
                         (T("B2"), "talk"), (T("B2") + 5.2, "scared"), (REV, "scared"), (MONEY, "scared"), (NOPE, "scared"),
                         (ON - 0.35, "point"), (ON + 0.3, "shush"), (T("B3") + 1.7, "talk"), (LAUGH, "scared")], tt, 0.18)
        C.append(("bondo2", bx, by, bs, look, barms if bw is None else "scared", None, bw, 0))
    return C

def arms_at(sched, tt, d=0.22):
    prev = sched[0][1]
    for i, (t0, pose) in enumerate(sched):
        if tt < t0: break
        if tt < t0 + d and i > 0: return (sched[i - 1][1], pose, (tt - t0) / d)
        prev = pose
    return prev

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, held=None, sit=0, nod=0.0, hop=0.0, walk=None):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    blink = ((tt + len(who) * 0.37) % 3.6) < 0.11 and expr not in ("sleepy", "laugh", "shock", "angry", "shout")
    if talking and arms == "down" and walk is None: arms = "talk"
    if not talking: lean += math.sin(tt * 1.7 + len(who)) * 0.04
    X, Y_ = W2S(cam, x, y - hop); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, held, lean, walk, sit=sit, nod=nod)

SOF = (150, 62, 58, 255); SOF_D = (112, 42, 40, 255); SOF_L = (178, 84, 76, 255)
def sofa_back(p, cam):
    z = cam[2]; x0, x1, sy = SOFA
    a = W2S(cam, x0, sy - 230); b = W2S(cam, x1, sy + 6); p.rect(a[0], a[1], b[0], b[1], SOF_D, INK, 3 * z, 26 * z)
    for i in range(3):
        cx = x0 + 40 + i * (x1 - x0 - 80) / 3
        a = W2S(cam, cx + 6, sy - 205); b = W2S(cam, cx + (x1 - x0 - 80) / 3 - 6, sy - 10); p.rect(a[0], a[1], b[0], b[1], SOF, INK, 2.5 * z, 18 * z)
    a = W2S(cam, x0 - 10, sy); b = W2S(cam, x1 + 10, sy + 70); p.rect(a[0], a[1], b[0], b[1], SOF_L, INK, 3 * z, 12 * z)
    a = W2S(cam, x0 - 10, sy + 70); b = W2S(cam, x1 + 10, sy + 120); p.rect(a[0], a[1], b[0], b[1], SOF_D, INK, 3 * z, 6 * z)
def sofa_front(p, cam):
    z = cam[2]; x0, x1, sy = SOFA
    for xx in (x0 - 60, x1 - 10):
        a = W2S(cam, xx, sy - 120); b = W2S(cam, xx + 70, sy + 120); p.rect(a[0], a[1], b[0], b[1], SOF, INK, 3 * z, 22 * z)
    for xx in (x0 + 10, x1 - 30):
        a = W2S(cam, xx, sy + 120); b = W2S(cam, xx + 20, sy + 160); p.rect(a[0], a[1], b[0], b[1], (60, 36, 20, 255), INK, 2 * z, 3 * z)

def kk2(tt, a, b): return max(0.0, min(1.0, (tt - a) / max(1e-6, b - a)))
def popk(tt, t0, d=0.22):
    u = kk(tt, t0, t0 + d); return 0 if u <= 0 else (1 + 0.25 * math.sin(u * math.pi)) if u < 1 else 1

def heart(d, x, y, r, col):
    d.ellipse([x - 2 * r, y - r, x, y + r * 0.6], fill=col); d.ellipse([x, y - r, x + 2 * r, y + r * 0.6], fill=col)
    d.polygon([(x - 2 * r + 1, y), (x + 2 * r - 1, y), (x, y + 2 * r)], fill=col)

def sweat(fr, cam, tt, n):
    if n <= 0: return
    d = ImageDraw.Draw(fr, "RGBA"); z = cam[2]; S = BD[2] * CH["bondo2"]["scale"]
    for i in range(n):
        u = (tt * (0.9 + 0.15 * i) + i * 0.37) % 1.0
        q = W2S(cam, BD[0] + (-50 + 100 * (i % 2) + 12 * (i // 2)) * S, BD[1] - 260 * S + u * 55 * S); r = (4.5 + i * 0.4) * S * z
        d.ellipse([q[0] - r, q[1] - r * 1.5, q[0] + r, q[1] + r * 1.5], fill=(190, 225, 255, int(230 * (1 - u))), outline=(60, 110, 170, int(255 * (1 - u))), width=2)


def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255, rot=0, stroke=True):
    if size < 4: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(LZ, size)
    if stroke: d.text((x, y), s, font=f, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), anchor="mm", direction="rtl", language="ar")
    d.text((x, y), s, font=f, fill=fill + (alpha,), anchor="mm", direction="rtl", language="ar")
    if rot: lay = lay.rotate(rot, center=(x, y), resample=Image.BICUBIC)
    img.paste(lay, (0, 0), lay)

def sub_chunk(img, tt, cx, cy, size, maxw=None):
    k, lt = line_at(tt)
    if not k or k not in CHUNKS: return
    cur = None
    for off, txt, key in CHUNKS[k]:
        if lt >= off: cur = (off, txt, key)
    if cur is None: return
    off, txt, key = cur; sc = popk(lt, off, 0.15) if lt - off < 0.15 else 1
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    sz = size
    if maxw:
        while sz > 30 and d.textlength(txt, font=ImageFont.truetype(LZ, sz), direction="rtl", language="ar") > maxw: sz -= 4
    f = ImageFont.truetype(LZ, max(6, int(sz * sc)))
    kw = dict(font=f, direction="rtl", language="ar", stroke_width=max(4, sz // 10), stroke_fill=(10, 10, 10, 255))
    if key and key in txt:
        a, b = txt.split(key, 1); parts = [(a, (255, 255, 255)), (key, (255, 214, 60)), (b, (255, 255, 255))]
    else: parts = [(txt, (255, 255, 255))]
    widths = [d.textlength(s, font=f, direction="rtl", language="ar") if s else 0 for s, _ in parts]
    tot = sum(widths); x = cx + tot / 2
    for (s, col), w in zip(parts, widths):
        if s: d.text((x - w, cy), s, fill=col + (255,), anchor="lm", **kw)
        x -= w
    nm, ncol = NAME[WHO[k]]; fn = ImageFont.truetype(LZ, int(size * 0.62))
    nw = d.textlength(nm, font=fn, direction="rtl", language="ar"); nx = cx + tot / 2 - nw / 2 - 10; ny = cy - size * 0.95
    d.rounded_rectangle([nx - nw / 2 - 18, ny - size * 0.38, nx + nw / 2 + 18, ny + size * 0.38], int(size * 0.3), fill=ncol + (235,))
    d.text((nx, ny), nm, font=fn, fill=(20, 12, 8, 255), anchor="mm", direction="rtl", language="ar")
    img.paste(lay, (0, 0), lay)


def vcam(sh, tt):
    c0, c1 = sh["v"]; k = ease((tt - sh["start"]) / max(0.01, sh["end"] - sh["start"]), sh.get("ease"))
    cx, cy, z = [a + (b - a) * k for a, b in zip(c0, c1)]; z = max(z, 1920 / 1080)
    shake = 0
    for st, amp in shakes:
        if 0 <= tt - st < 0.45: shake = max(shake, amp * (1 - (tt - st) / 0.45))
    cw, ch = 1080 / z, 1920 / z
    x0 = min(max(cx - cw / 2 + math.sin(tt * 0.9) * 3, 0), 1920 - cw); y0 = min(max(cy - ch / 2 + math.sin(tt * 1.3) * 2, 0), 1080 - ch)
    if shake: x0 = min(max(x0 + rng.normal(0, shake / z), 0), 1920 - cw); y0 = min(max(y0 + rng.normal(0, shake / z), 0), 1080 - ch)
    return x0, y0, z


def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def buzzer(dur=0.42, amp=0.13):
    d_ = np.arange(int(SR * dur)) / SR; w = np.sign(np.sin(2 * np.pi * 110 * d_)) + 0.5 * np.sign(np.sin(2 * np.pi * 116 * d_))
    return lowpass((w * amp * np.minimum(1, (dur - d_) * 12)).astype(np.float32), 2200)


def sweat_at(fr, cam, tt, x, y, s, n):
    if n <= 0: return
    d = ImageDraw.Draw(fr, "RGBA"); z = cam[2]; S = s * CH["bondo2"]["scale"]
    for i in range(n):
        u = (tt * (0.9 + 0.15 * i) + i * 0.37) % 1.0
        q = W2S(cam, x + (-52 + 104 * (i % 2) + 10 * (i // 2)) * S, y - 225 * S + u * 55 * S); r = (4.5 + i * 0.4) * S * z
        d.ellipse([q[0] - r, q[1] - r * 1.5, q[0] + r, q[1] + r * 1.5], fill=(190, 225, 255, int(230 * (1 - u))), outline=(60, 110, 170, int(255 * (1 - u))), width=2)

def door_open(p, cam, tt):
    """the canonical door swings open while she comes in, then closes behind her"""
    k = kk2(tt, DOOR_OPEN, DOOR_OPEN + 0.35) * (1 - kk2(tt, ENTER[0] + 1.1, ENTER[0] + 1.5))
    if k <= 0: return
    x0, y0, x1, y1 = DOOR; z = cam[2]
    a = W2S(cam, x0 + 18, y0 + 18); b = W2S(cam, x1 - 16, y1 - 2)
    p.rect(a[0], a[1], b[0], b[1], (18, 14, 12, int(255 * min(1, k * 1.4))), None, 0, 0)
    w = (x1 - x0 - 34) * (1 - k * 0.82)                      # the leaf, foreshortened as it opens inward
    L = W2S(cam, x0 + 18, y0 + 18); R = W2S(cam, x0 + 18 + w, y1 - 2)
    p.rect(L[0], L[1] - 6 * z * k, R[0], R[1] + 4 * z * k, (92, 56, 34, 255), INK, 2.5 * z, 2 * z)

def bulb(fr, cam, tt, lit):
    d = ImageDraw.Draw(fr, "RGBA"); z = cam[2]
    sw = math.sin(tt * 1.6) * 6 if tt < ON + 1.5 else math.sin(tt * 4) * 10 * max(0, 1 - (tt - ON - 1.5))
    top = W2S(cam, BULB[0], -40); c = W2S(cam, BULB[0] + sw, BULB[1])
    d.line([top, (c[0], c[1] - 26 * z)], fill=(25, 20, 18, 255), width=max(2, int(3 * z)))
    d.rectangle([c[0] - 9 * z, c[1] - 30 * z, c[0] + 9 * z, c[1] - 16 * z], fill=(120, 110, 100, 255))
    r = 20 * z
    if lit > 0.5:
        g = Image.new("RGBA", fr.size, (0, 0, 0, 0)); gd = ImageDraw.Draw(g)
        for i in range(8, 0, -1):
            R = r * (1 + i * 1.1); gd.ellipse([c[0] - R, c[1] - R, c[0] + R, c[1] + R], fill=(255, 220, 140, int(14 + 4 * (8 - i))))
        fr.paste(g, (0, 0), g)
        d.ellipse([c[0] - r, c[1] - r, c[0] + r, c[1] + r], fill=(255, 246, 200, 255), outline=(200, 160, 60, 255), width=max(2, int(2 * z)))
    else:
        d.ellipse([c[0] - r, c[1] - r, c[0] + r, c[1] + r], fill=(150, 150, 140, 255), outline=(40, 40, 40, 255), width=max(2, int(2 * z)))

def switch(p, cam):
    z = cam[2]; a = W2S(cam, SWITCH[0] - 16, SWITCH[1] - 24); b = W2S(cam, SWITCH[0] + 16, SWITCH[1] + 24)
    p.rect(a[0], a[1], b[0], b[1], (236, 228, 210, 255), INK, 2 * z, 4 * z)
    a = W2S(cam, SWITCH[0] - 5, SWITCH[1] - 10); b = W2S(cam, SWITCH[0] + 5, SWITCH[1] + 10); p.rect(a[0], a[1], b[0], b[1], (200, 190, 170, 255), INK, 1.5 * z, 2 * z)

def moon_beam(fr, cam, tt, k):
    """moonlight through the window lands on him like a theatre spotlight (his poem)"""
    if k <= 0: return
    z = cam[2]; lay = Image.new("RGBA", fr.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    w0 = W2S(cam, 1830, 30); w1 = W2S(cam, 1920, 190); f0 = W2S(cam, BDM[0] - 170, FEET + 10); f1 = W2S(cam, BDM[0] + 150, FEET + 10)
    d.polygon([w0, w1, f1, f0], fill=(170, 200, 255, int(70 * k)))
    c = W2S(cam, BDM[0], FEET + 4); d.ellipse([c[0] - 170 * z, c[1] - 26 * z, c[0] + 170 * z, c[1] + 26 * z], fill=(190, 215, 255, int(80 * k)))
    lay = lay.filter(ImageFilter.GaussianBlur(10 * z)); fr.paste(lay, (0, 0), lay)

def floaters(fr, cam, tt, t0, t1, kind, ox, oy):
    """hearts (his poem) / banknotes (her reveal) rising around a head"""
    if not (t0 <= tt < t1 + 0.6): return
    d = ImageDraw.Draw(fr, "RGBA"); z = cam[2]; fade = 1 - kk2(tt, t1, t1 + 0.6)
    for i in range(9):
        r_ = np.random.default_rng(40 + i); ph = r_.uniform(0, 1); sx = r_.uniform(-170, 170)
        u = ((tt - t0) * 0.45 + ph) % 1.0
        x, y = W2S(cam, ox + sx + math.sin((tt + i) * 2.2) * 18, oy - u * 260)
        a = int(255 * fade * min(1, u * 5) * (1 - u)); sc = z * (0.8 + 0.4 * r_.uniform())
        if kind == "heart": heart(d, x, y, 9 * sc, (235, 60, 95, a))
        else:
            rot = math.sin(tt * 3 + i) * 0.4; w_, h_ = 30 * sc, 15 * sc
            pts = [(x + math.cos(rot) * dx - math.sin(rot) * dy, y + math.sin(rot) * dx + math.cos(rot) * dy) for dx, dy in ((-w_, -h_), (w_, -h_), (w_, h_), (-w_, h_))]
            d.polygon(pts, fill=(120, 190, 110, a), outline=(40, 90, 40, a)); d.ellipse([x - 6 * sc, y - 6 * sc, x + 6 * sc, y + 6 * sc], outline=(40, 90, 40, a), width=2)

def money_bubble(fr, cam, tt, ox, oy):
    """«عينك على الجمعية»: a thought bubble over him — a fat envelope of cash; a red ✗ slams it on «قرش واحد»"""
    if not (MONEY <= tt < ON): return
    z = cam[2]; sc = popk(tt, MONEY, 0.25) * (1 - kk2(tt, NOPE + 1.4, NOPE + 1.8))
    if sc <= 0.02: return
    cx, cy = W2S(cam, ox + 80, oy - 120); R = 86 * z / 1.5 * sc
    lay = Image.new("RGBA", fr.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    hx, hy = W2S(cam, ox + 20, oy + 10)
    for dx, dy, rr in ((0.3, 0.75, 0.12), (0.6, 0.45, 0.2)):
        px, py = hx + (cx - hx) * dx, hy + (cy - hy) * dy; r = R * rr * 1.4
        d.ellipse([px - r, py - r, px + r, py + r], fill=(255, 255, 255, 240), outline=(20, 12, 8, 255), width=max(2, int(3 * z)))
    d.ellipse([cx - R * 1.3, cy - R, cx + R * 1.3, cy + R], fill=(255, 255, 255, 245), outline=(20, 12, 8, 255), width=max(3, int(4 * z)))
    u = R / 60; w = max(2, int(3 * z))
    for i in range(3):
        d.rectangle([cx - 34 * u + i * 4 * u, cy - 26 * u + i * 6 * u, cx + 30 * u + i * 4 * u, cy - 4 * u + i * 6 * u], fill=(130, 200, 120, 255), outline=(40, 90, 40, 255), width=w)
    d.rectangle([cx - 38 * u, cy - 2 * u, cx + 38 * u, cy + 30 * u], fill=(235, 215, 170, 255), outline=(20, 12, 8, 255), width=w)
    d.polygon([(cx - 38 * u, cy - 2 * u), (cx, cy + 16 * u), (cx + 38 * u, cy - 2 * u)], outline=(20, 12, 8, 255), fill=(225, 200, 150, 255))
    if tt >= NOPE:
        k = popk(tt, NOPE, 0.18); r = R * 1.15 * k; wx = max(8, int(16 * z * k))
        for s_ in (1, -1):
            d.line([(cx - r, cy - r * s_), (cx + r, cy + r * s_)], fill=(30, 8, 8, 255), width=wx + 8); d.line([(cx - r, cy - r * s_), (cx + r, cy + r * s_)], fill=(230, 40, 40, 255), width=wx)
    fr.paste(lay, (0, 0), lay)

def antar(fr, cam, tt, ox, oy):
    """«عنترة بن شداد»: a cardboard knight's helmet + sword pop onto Bandaq for a beat"""
    if not (ANTAR + 0.6 <= tt < ASR + 0.4): return
    z = cam[2]; S = BDM[2] * CH["bondo2"]["scale"]; k = popk(tt, ANTAR + 0.6, 0.2) * (1 - kk2(tt, ASR, ASR + 0.4))
    if k <= 0.02: return
    d = ImageDraw.Draw(fr, "RGBA"); hx, hy = W2S(cam, ox, oy - 196 * S); r = 50 * S * z * k
    d.chord([hx - r, hy - r * 1.05, hx + r, hy + r * 0.6], 180, 360, fill=(190, 190, 200, 255), outline=(20, 12, 8, 255), width=max(2, int(3 * z)))
    d.polygon([(hx - 4 * z, hy - r * 1.0), (hx + 4 * z, hy - r * 1.0), (hx + 10 * z, hy - r * 1.55), (hx - 10 * z, hy - r * 1.55)], fill=(220, 40, 40, 255))
    sx, sy = W2S(cam, ox + 70 * S, oy - 150 * S)
    d.line([(sx, sy), (sx + 30 * S * z * k, sy - 120 * S * z * k)], fill=(225, 225, 235, 255), width=max(4, int(8 * S * z)))
    d.line([(sx - 14 * S * z, sy - 4 * S * z), (sx + 16 * S * z, sy + 6 * S * z)], fill=(200, 160, 40, 255), width=max(4, int(6 * S * z)))

def scene(tt, cam, size):
    Wd, Hd = size; x0, y0, z = cam
    box = (x0, y0, x0 + Wd / z, y0 + Hd / z)
    img = ROOM.resize((int(Wd * SS), int(Hd * SS)), Image.BICUBIC, box=box)
    if z > 1.9: img = img.filter(ImageFilter.GaussianBlur(min(2.5, (z - 1.8) * 1.4)))
    pl = Image.new("RGBA", img.size, (0, 0, 0, 0)); p = P(pl)
    door_open(p, cam, tt); switch(p, cam)
    sofa_back(p, cam)
    C = cast(tt); k, lt = line_at(tt)
    for who, x, y, s, look, arms, held, walk, sit in C:
        if sit:
            person(pl, cam, who, x, y, s, tt, "sleepy" if tt < 0.2 else "shock", look, arms, 0.0, held, sit=sit)
    sofa_front(p, cam)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    for who, x, y, s, look, arms, held, walk, sit in C:
        if sit: continue
        if who == "aziza":
            e = "neutral" if tt < OFF else ("shock" if tt < T("A1") else ("flat" if tt < REV else "angry"))
            if POEM <= tt < T("A2"): e = "flat"
            if tt >= ON: e = "smug"
            lean = 0.25 if REV <= tt < REV + 0.5 or NOPE <= tt < NOPE + 0.6 else 0.0
        else:
            e = "scared" if tt < OFF + 0.3 else "happy"
            if T("A2") <= tt < T("B2"): e = "scared"
            if REV <= tt < ON: e = "scared"
            if tt >= ON: e = "sad"
            if tt >= LAUGH: e = "scared"
            lean = -0.25 if REV <= tt < REV + 0.5 or NOPE <= tt < NOPE + 0.6 else (0.15 if POEM <= tt < T("A2") else 0.0)
        hop = abs(math.sin((tt - JUMP) * 9)) * 30 if who == "bondo2" and JUMP <= tt < JUMP + 0.35 else 0.0
        person(lay, cam, who, x, y, s, tt, e, look, arms, lean, held, hop=hop, walk=walk)
    lit = light_at(tt)
    # ---- night lighting: bulb on = warm; off = blue dark room, the characters stay readable (moon/ambient)
    if lit > 0.5:
        pl = tint_layer(pl, (255, 236, 205)); img.paste(pl, (0, 0), pl); lay = tint_layer(lay, (255, 236, 205))
        img = ImageChops.multiply(ImageEnhance.Brightness(img).enhance(0.86), Image.new("RGB", img.size, (255, 236, 210)))
    else:
        pl = tint_layer(pl, (255, 236, 205)); img.paste(pl, (0, 0), pl); lay = tint_layer(lay, (175, 190, 240), 0.8)
        img = ImageChops.multiply(ImageEnhance.Brightness(img).enhance(0.34), Image.new("RGB", img.size, (150, 170, 235)))
    img.paste(lay, (0, 0), lay)
    fr = img.resize((Wd, Hd), Image.LANCZOS)
    if lit <= 0.5: moon_beam(fr, cam, tt, kk2(tt, OFF + 0.2, OFF + 0.8) * (1.0 if tt < REV else 0.6))
    bulb(fr, cam, tt, lit)
    for who, x, y, s, look, arms, held, walk, sit in C:
        if who == "bondo2" and not sit:
            floaters(fr, cam, tt, POEM + 0.2, T("A2"), "heart", x + 140, y - 200 * s)
            money_bubble(fr, cam, tt, x, y - 236 * s); antar(fr, cam, tt, x, y)
            n = 0
            if REV <= tt < ON: n = 2 if tt < MONEY else 4
            if T("B2") <= tt < REV: n = 2
            if tt >= ON: n = 3
            sweat_at(fr, cam, tt, x, y, s, n)
    d = ImageDraw.Draw(fr, "RGBA")
    if OFF - 0.05 <= tt < OFF + 0.6:                                   # «تِك!» spark at the switch
        c = W2S(cam, *SWITCH); u = kk2(tt, OFF - 0.05, OFF + 0.6)
        for i in range(8):
            a_ = i / 8 * 2 * math.pi; r0, r1 = 26 * z, (26 + 40 * u) * z
            d.line([(c[0] + math.cos(a_) * r0, c[1] + math.sin(a_) * r0), (c[0] + math.cos(a_) * r1, c[1] + math.sin(a_) * r1)], fill=(255, 230, 120, int(255 * (1 - u))), width=max(2, int(3 * z)))
    if REV <= tt < REV + 1.0:                                          # «!» over her — she got it
        c = W2S(cam, AZM[0] + 40, AZM[1] - 236 * AZM[2] - 50); lzt(fr, c[0], c[1], "!", int(110 * z / 2 * popk(tt, REV, 0.2)), (255, 214, 60))
    return fr

def endcard(fr, tt, sh, Wd, Hd):
    """growth rule 30: ONE ask only"""
    k = kk(tt, sh["start"], sh["start"] + 0.4)
    fr = ImageEnhance.Brightness(fr).enhance(1 - 0.55 * k).filter(ImageFilter.GaussianBlur(6 * k))
    sc = popk(tt, sh["start"] + 0.1, 0.3); vert = Hd > Wd
    if sc > 0: lzt(fr, Wd / 2, Hd * (0.36 if vert else 0.33), "تابع بندق وعزيزة…", int((118 if vert else 116) * sc), (255, 214, 90))
    if tt >= sh["start"] + 0.5:
        logo(fr, Wd / 2, Hd * (0.56 if vert else 0.64), 130); text(fr, Wd / 2, Hd * (0.56 if vert else 0.64) + 140, "@shattawzalata", 52, (255, 214, 90))
    return fr

_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/daily/19")


def subtitle(img, tt): sub_chunk(img, tt, W / 2, H - 85, 64)

HOOK = "طفّى النور ليه؟!"
_FREEZE = {}
def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "end":
        if "h" not in _FREEZE: _FREEZE["h"] = scene(sh["start"] - 0.05, cam_at(shots[-2], sh["start"] - 0.05), (W, H))
        return finish(endcard(_FREEZE["h"].copy(), tt, sh, W, H), tt)
    fr = scene(tt, cam_at(sh, tt), (W, H))
    if tt < 3.0:
        a_ = int(255 * min(1, (3.0 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([W / 2 - 420, 40, W / 2 + 420, 150], 30, fill=(20, 12, 8, int(a_ * 0.8)))
        lzt(fr, W / 2, 95, HOOK, int(76 * popk(tt, 0.0, 0.25)) or 76, (255, 214, 90), alpha=a_)
    return finish(fr, tt)

VIGV = VIG.resize((1080, 1920))
def vertical(_base, tt):
    sh = shot_at(tt)
    if sh["set"] == "end":
        if "v" not in _FREEZE: _FREEZE["v"] = scene(sh["start"] - 0.05, vcam(shots[-2], sh["start"] - 0.05), (1080, 1920))
        return endcard(_FREEZE["v"].copy(), tt, sh, 1080, 1920)
    fr = scene(tt, vcam(sh, tt), (1080, 1920))
    fr = ImageChops.multiply(fr, VIGV)
    if tt < 3.0:
        a_ = int(255 * min(1, (3.0 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([140, 240, 940, 440], 40, fill=(20, 12, 8, int(a_ * 0.75)))
        lzt(fr, 540, 340, HOOK, int(100 * popk(tt, 0.0, 0.25)) or 100, (255, 214, 90), alpha=a_)
    sub_chunk(fr, tt, 530, 600, 76, maxw=940)
    return fr

def click(amp=0.35):
    n = int(SR * 0.04); r = np.random.default_rng(3); return (r.normal(0, 1, n) * np.exp(-np.arange(n) / SR * 160) * amp).astype(np.float32)
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(19)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 300) * 0.012, 0, 1.0)                  # room tone
    d_ = np.arange(int(SR * 0.7)) / SR                                                                  # door creak (frame 1)
    creak = (np.sin(2 * np.pi * (180 + 260 * d_ + 40 * np.sin(d_ * 37)) * d_) * 0.09 * np.minimum(1, (0.7 - d_) * 6)).astype(np.float32)
    mix_into(buf, creak, 0.0, 1.0)
    mix_into(buf, SFXF["whoosh"] * 0.3, JUMP, 1.0)                                                     # he leaps
    mix_into(buf, click(), OFF - 0.02, 1.0); mix_into(buf, tone(80, 0.5, 0.15, 5), OFF, 1.0)            # CLICK — dark
    for k_, (f1, f2) in enumerate(((523, 659), (587, 740), (659, 784), (523, 659))):                    # soft «romantic» chords under the poem
        mix_into(buf, (tone(f1, 1.4, 0.035, 1.2) + tone(f2, 1.4, 0.03, 1.2)), T("B1") + k_ * 1.4, 1.0)
    mix_into(buf, tone(196, 0.6, 0.1, 3), T("B2") + 0.05, 1.0)                                         # deflate
    mix_into(buf, tone(140, 0.8, 0.28, 2.5), REV, 1.0); mix_into(buf, tone(95, 0.8, 0.22, 2.5), REV + 0.03, 1.0)   # «DUN» — she got it
    mix_into(buf, tone(1568, 0.3, 0.1, 9) + tone(2093, 0.3, 0.08, 8), MONEY + 0.1, 1.0)               # ka-ching
    mix_into(buf, tone(392, 0.3, 0.09, 6) + tone(523, 0.3, 0.09, 5), ANTAR + 0.6, 1.0)                 # knight fanfare
    mix_into(buf, buzzer(0.5, 0.15), NOPE + 0.02, 1.0)                                                 # ✗
    mix_into(buf, click(), ON - 0.02, 1.0); mix_into(buf, click(0.2), ON + 0.08, 1.0)                  # CLICK — light back
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), TOTAL - 2.5 + k_ * 0.09, 1.0)
    rms = lambda x: float(np.sqrt(np.mean(x ** 2))) + 1e-9; ref = []
    for st, k in lines:
        if k == "GROUP": continue
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8
        ref.append(rms(v)); mix_into(buf, v, st, 1.0)
    g = AUD["GROUP"][:int(SR * LU)].copy(); g[-int(SR * 0.4):] *= np.linspace(1, 0, int(SR * 0.4))
    mix_into(buf, g / rms(g) * float(np.mean(ref)) * 1.2, LAUGH, 1.0)
    write_wav(buf[:int(TOTAL * SR)], path)

def make_covers():
    """dark room, the bulb, Bandaq at the switch caught red-handed, Aziza with the slipper; 2-word question"""
    def comp(Wd, Hd, vert):
        bgc = ROOM.crop((400, 0, 1700, 1000)).resize((Wd, Hd), Image.LANCZOS).filter(ImageFilter.GaussianBlur(5))
        img = ImageEnhance.Brightness(bgc).enhance(0.45)
        img = ImageChops.multiply(img, Image.new("RGB", img.size, (160, 175, 235))).resize((int(Wd * SS), int(Hd * SS)))
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); p = P(lay)
        if vert:
            draw_char(p, "aziza", Wd * 0.24, Hd * 0.62, 2.6, "angry", 0.4, 1, False, "raise", 0.0, "slipper", 0.15, None)
            draw_char(p, "bondo2", Wd * 0.66, Hd * 0.98, 4.6, "scared", 0.5, -1, False, "point", 0.0, None, -0.05, None)
        else:
            draw_char(p, "aziza", Wd * 0.2, Hd * 1.0, 3.3, "angry", 0.4, 1, False, "raise", 0.0, "slipper", 0.15, None)
            draw_char(p, "bondo2", Wd * 0.64, Hd * 1.36, 4.6, "scared", 0.5, -1, False, "point", 0.0, None, -0.05, None)
        img.paste(lay, (0, 0), lay); fr = img.resize((Wd, Hd), Image.LANCZOS); d = ImageDraw.Draw(fr, "RGBA")
        bx, by = (Wd * 0.5, Hd * 0.12) if vert else (Wd * 0.42, Hd * 0.12)
        for i in range(8, 0, -1):
            R = 26 * (1 + i * 1.2); d.ellipse([bx - R, by - R, bx + R, by + R], fill=(255, 220, 140, 10 + 5 * (8 - i)))
        d.line([(bx, 0), (bx, by - 30)], fill=(20, 16, 14, 255), width=4)
        d.ellipse([bx - 26, by - 26, bx + 26, by + 26], fill=(255, 246, 200, 255), outline=(200, 160, 60, 255), width=3)
        if vert:
            d.rectangle([0, Hd * 0.69, Wd, Hd * 0.88], fill=(10, 6, 4, 150))
            lzt(fr, Wd / 2, Hd * 0.74, "طفّى النور", 140, (255, 255, 255)); lzt(fr, Wd / 2, Hd * 0.83, "ليه؟!", 190, (255, 214, 60))
            bx2, by2 = Wd / 2, 330
        else:
            d.rectangle([0, Hd * 0.76, Wd, Hd * 0.97], fill=(10, 6, 4, 150)); lzt(fr, Wd * 0.5, Hd * 0.865, "طفّى النور ليه؟!", 150, (255, 214, 60)); bx2, by2 = 1600, 90
        d.rounded_rectangle([bx2 - 175, by2 - 40, bx2 + 175, by2 + 40], 30, fill=(200, 30, 40, 240))
        lzt(fr, bx2, by2, "يوميات شطة وزلطة", 40, (255, 255, 255), stroke=False)
        return fr
    comp(1080, 1920, True).save(ROOT + "/publish/thumbs/daily_e19_cover.jpg", quality=92)
    comp(1920, 1080, False).resize((1280, 720), Image.LANCZOS).save(ROOT + "/publish/thumbs/daily_e19_yt.jpg", quality=92)

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
