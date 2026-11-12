# «ميكروفون توتة» 01 — السجاير والعربية  (H 1920x1080 + V 1080x1920 in one pass)
# render:  python ep.py audio  →  python ep.py part 0 2 & python ep.py part 1 2  →  concat  →  mux mix.wav
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())          # engine + shared helpers (cam, transitions, vertical, finish…)
from locations import loc
from PIL import ImageFont
os.chdir(ROOT + "/mic/01")
SERIES = "ميكروفون توتة"; EPT = "الحلقة 1: السجاير والعربية"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"
def load_sfx(names):
    global SFXF
    SFXF = {n: load_audio(f"{ROOT}/trend/01/sfx/{n}.mp3") for n in names}

SUB = {"P01": "أنا صاحي أهو!",
       "P02": "إزيك يا عم بندق! معاك «ميكروفون توتة». ممكن سؤال؟",
       "P03": "اتفضلي يا ست الصحفية.",
       "P04": "إنت بتدخن؟", "P05": "آه، بدخن.",
       "P06": "كام علبة في اليوم؟", "P07": "علبتين.",
       "P08": "والعلبة بكام؟", "P09": "خمسين جنيه.",
       "P10": "بقالك كام سنة بتدخن؟", "P11": "تلاتين سنة.",
       "P12": "يعني مية جنيه في اليوم... تلات تلاف في الشهر... ستة وتلاتين ألف وخمسمية في السنة... يعني في تلاتين سنة: مليون وخمسة وتسعين ألف جنيه!",
       "P13": "لو كنت بطلت السجاير... كان زمانك راكب عربية زيرو... موديل ألفين ستة وعشرين!",
       "P14": "طب وإنتي... بتشربي سجاير؟", "P15": "لأ.",
       "P16": "أمال فين عربيتك؟", "P17": ""}
WHO = {k: ("tota" if k in ("P02", "P04", "P06", "P08", "P10", "P12", "P13", "P15") else "bondo2") for k in SUB}
WHO["P17"] = "shatta"
EXPR = {"P01": "shock", "P02": "happy", "P03": "happy", "P04": "neutral", "P05": "flat", "P06": "neutral", "P07": "flat",
        "P08": "neutral", "P09": "flat", "P10": "flat", "P11": "smug", "P12": [(0, "flat"), (0.6, "shock")],
        "P13": [(0, "happy"), (0.35, "smug")], "P14": "smug", "P15": "smug", "P16": "flat", "P17": "laugh"}
ARMS = {}
load_lines(list(SUB)); load_sfx(["whoosh", "switch", "gasp"])

STREET = loc("street", "day")          # canonical street (the parked car there is painted over by Bandaq's old Fiat)
# ---------------- staging (world coords on the 1920x1080 street) ----------------
BW = (800, 643, 1.15)                  # البواب in the driver's seat (head in the open front window)
TW = (560, 862, 1.5)                   # توتة on the pavement by the front fender, mic in her right hand
SWP = (1565, 1065, 1.75)               # شطة leaning on the building doorway (foreground right), eating chips
def headc(pos, who):
    x, y, s = pos; S = s * CH[who]["scale"]; return x, y - 190 * S, S
def CU(who, pos, z=2.5, dx=0, dy=0):
    x, hy, S = headc(pos, who); return (x + dx, hy + 30 * S + dy, z)
WIDE = (960, 560, 1.0); TWO = (700, 560, 1.55)
TA0, TA1 = (670, 560, 1.8), (670, 560, 1.9); TB0, TB1 = (725, 565, 2.0), (725, 565, 2.1)   # two-shots: both in frame while they talk (user rule)
CU_B = CU("bondo2", BW, 2.6, -10); CU_T = CU("tota", TW, 2.3, 30, 10); CU_S = CU("shatta", SWP, 2.0, -40, 30)

# ---------------- timeline ----------------
t = 0.0; TAPS = (0.15, 0.38)
shot("st", 0.0, 0.72, CU("bondo2", BW, 2.35, -10), CU("bondo2", BW, 2.45, -10))            # hook: asleep, Zzz, smoke… tap tap
WAKE = 0.72; jump("bondo2", WAKE); shakes.append((WAKE, 10))
t = say(WAKE + 0.02, "P01") + 0.2
shot("st", WAKE, t, CU("bondo2", BW, 2.85, -10), CU("bondo2", BW, 2.95, -10), tin="zoom")
EST = (t, 0)                                                                                 # establishing wide + series logo
s = t; t = say(t + 0.3, "P02") + 0.2; EST = (s, t)
shot("st", s, t, WIDE, (880, 575, 1.12), tin="whip")
s = t; t = say(t + 0.15, "P03") + 0.2; PROUD = s                                             # proud, sits up straight
shot("st", s, t, TA0, TA1, tin="whipl")
s = t; t = say(t + 0.1, "P04") + 0.12
shot("st", s, t, TB0, TB1)
s = t; t = say(t + 0.1, "P05") + 0.1; PUFF = t                                                # «آه بدخن» + a big puff of smoke
t += 0.75; shot("st", s, t, TA0, TA1)
SH1 = (t, t + 0.85); shot("st", t, SH1[1], CU_S, CU("shatta", SWP, 2.1, -40, 30), tin="whip"); t = SH1[1]   # Shatta munching, watching
s = t; t = say(t + 0.1, "P06") + 0.1
shot("st", s, t, TB0, TB1, tin="whipl")
s = t; t = say(t + 0.1, "P07") + 0.12; F1 = s + 0.25
shot("st", s, t, TA0, TA1)
s = t; t = say(t + 0.1, "P08") + 0.08
shot("st", s, t, TB0, TB1)
s = t; t = say(t + 0.1, "P09") + 0.12; F2 = s + 0.3
shot("st", s, t, TA0, TA1)
s = t; t = say(t + 0.1, "P10") + 0.1; SUSP = s
shot("st", s, t, TB0, TB1)
s = t; t = say(t + 0.1, "P11") + 0.15; F3 = s + 0.25
shot("st", s, t, TA0, TA1)
CALC = t + 0.15; t = say(CALC, "P12")                                                       # the calculation
NUMS = [(CALC + 0.56, "100 جنيه", "في اليوم"), (CALC + 2.16, "3,000 جنيه", "في الشهر"), (CALC + 3.76, "36,500 جنيه", "في السنة")]
X30 = CALC + 6.72; MIL = CALC + 7.84
CUTB = CALC + 7.62
shot("st", CALC - 0.15, CUTB, (900, 600, 1.5), (870, 600, 1.72), tin="whip")
t += 0.35; shot("st", CUTB, t, (730, 560, 1.9), (745, 550, 2.35), ease="crash", tin="zoom")   # Bandaq: ash falls
DROP = MIL + 0.15
s = t; t = say(t + 0.1, "P13"); DREAM = s + 0.1 + 1.93; M26 = s + 0.1 + 3.95                 # «لو كنت بطلت»… dream bubble
shot("st", s, DREAM - 0.05, TB0, TB1, tin="whip")
POP = t + 0.55; t = POP + 0.7
shot("st", DREAM - 0.05, t, (930, 430, 1.32), (930, 450, 1.42), tin="whipl")
s = t; t = say(t + 0.15, "P14") + 0.15; SLY = s                                              # the counter-question (slow push-in)
shot("st", s, t, (700, 570, 1.8), (720, 555, 2.2))
s = t; t = say(t + 0.1, "P15") + 0.15; NO = s
shot("st", s, t, (720, 555, 2.2), (720, 555, 2.25))
s = t; t = say(t + 0.12, "P16") + 0.5; PUNCH = s
shot("st", s, t, (720, 555, 2.25), (730, 550, 2.4))
STUN = (t, t + 0.9); shot("st", t, STUN[1], (730, 550, 2.4), (730, 550, 2.45)); t = STUN[1]   # Tota frozen (crickets)
LAUGH = t; t = say(t + 0.1, "P17")                                                           # trademark: Shatta's laugh
FREEZE = t - 0.25
shot("st", LAUGH, t + 0.05, CU_S, CU("shatta", SWP, 2.25, -40, 30), tin="whip")
shot("end", t + 0.05, t + 2.6, None); t += 2.6
TOTAL = t

# ---------------- props ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
CREAM = (222, 208, 168, 255); CREAM_D = (190, 174, 132, 255); RUST = (150, 92, 52, 255); CHROME = (205, 208, 212, 255)
FRONT_WIN = [(612, 500), (705, 352), (930, 352), (930, 500)]
REAR_WIN = [(962, 500), (962, 352), (1250, 352), (1400, 500)]
def car_back(p, cam):
    z = cam[2]; T = lambda pts: [W2S(cam, *q) for q in pts]
    p.poly(T(FRONT_WIN), (52, 46, 44, 255), None)
    p.poly(T(REAR_WIN), (52, 46, 44, 255), None)
    x, y = W2S(cam, 905, 420); p.rect(x - 16 * z, y - 50 * z, x + 16 * z, y + 80 * z, (88, 70, 60, 255), INK, 2 * z, 12 * z)   # seat back
    x, y = W2S(cam, 1150, 440); p.rect(x - 90 * z, y - 30 * z, x + 90 * z, y + 70 * z, (88, 70, 60, 255), INK, 2 * z, 18 * z)   # rear seat
def car_front(p, cam, tt):
    z = cam[2]; T = lambda pts: [W2S(cam, *q) for q in pts]
    # lower body (hood → doors → trunk)
    body = [(386, 520), (400, 500), (1550, 500), (1556, 520), (1556, 690), (1540, 712), (402, 712), (386, 690)]
    p.poly(T(body), CREAM, INK, 3 * z)
    p.poly(T([(390, 640), (1552, 640), (1552, 690), (1540, 712), (402, 712), (390, 690)]), CREAM_D, None)       # lower shade
    # pillars + roof
    p.poly(T([(600, 500), (612, 500), (705, 352), (690, 350)]), CREAM, INK, 3 * z)                             # A
    p.poly(T([(690, 350), (1262, 350), (1250, 352), (705, 352)]), CREAM, INK, 3 * z)
    p.poly(T([(680, 352), (1265, 352), (1270, 336), (700, 336)]), CREAM, INK, 3 * z)                           # roof
    p.poly(T([(930, 352), (962, 352), (962, 500), (930, 500)]), CREAM, INK, 3 * z)                             # B
    p.poly(T([(1250, 352), (1268, 342), (1430, 500), (1400, 500)]), CREAM, INK, 3 * z)                         # C
    p.poly(T(REAR_WIN), (190, 215, 230, 70), INK, 3 * z)                                                       # rear glass (tinted)
    p.line(T([(1000, 372), (1060, 480)]), (255, 255, 255, 90), 6 * z); p.line(T([(1040, 372), (1080, 440)]), (255, 255, 255, 70), 4 * z)
    p.line(T(FRONT_WIN + [FRONT_WIN[0]]), INK, 3 * z)                                                         # open front window frame
    # door lines, handles, beltline chrome
    for x0_, x1_ in ((640, 946), (946, 1262)):
        p.line(T([(x0_, 500), (x0_, 700)]), INK, 2.5 * z)
    p.line(T([(1262, 500), (1262, 690)]), INK, 2.5 * z)
    p.line(T([(400, 515), (1550, 515)]), CHROME, 3 * z)
    for hx in (895, 1215): p.rect(*W2S(cam, hx - 22, 532), *W2S(cam, hx + 22, 542), CHROME, INK, 1.5 * z, 4 * z)
    # rust & a dent (it's OLD)
    for rx, ry, rw, rh in ((1120, 668, 50, 16), (470, 676, 34, 12), (1480, 560, 26, 30), (760, 690, 40, 10)):
        p.ell(*W2S(cam, rx, ry), rw * z / 2, rh * z / 2, RUST, None)
    p.arc(*W2S(cam, 1050, 600), 40 * z, 18 * z, 200, 340, (120, 108, 80, 255), 3 * z)
    # bumpers, lights, mirror, antenna
    p.rect(*W2S(cam, 372, 646), *W2S(cam, 412, 664), CHROME, INK, 2 * z, 5 * z)
    p.rect(*W2S(cam, 1532, 646), *W2S(cam, 1570, 664), CHROME, INK, 2 * z, 5 * z)
    p.rect(*W2S(cam, 386, 540), *W2S(cam, 404, 578), (255, 240, 190, 255), INK, 2 * z, 3 * z)
    p.rect(*W2S(cam, 1540, 540), *W2S(cam, 1556, 570), (200, 40, 30, 255), INK, 2 * z, 3 * z)
    mx, my = W2S(cam, 600, 486); p.rect(mx - 30 * z, my - 18 * z, mx + 4 * z, my + 8 * z, CREAM_D, INK, 2 * z, 6 * z)
    p.line([(mx - 26 * z, my - 14 * z), (mx - 6 * z, my + 4 * z)], (200, 200, 200, 255), 3 * z)                  # tape on the mirror
    p.line(T([(1500, 500), (1540 + math.sin(tt * 3) * 4, 300)]), INK, 2 * z)
    # wheel arches + wheels
    for wx in (560, 1300):
        cx, cy = W2S(cam, wx, 706)
        p.d.pieslice([p.S(cx - 86 * z), p.S(cy - 86 * z), p.S(cx + 86 * z), p.S(cy + 86 * z)], 180, 360, fill=(30, 28, 28, 255))
        p.ell(cx, cy, 64 * z, 64 * z, (28, 28, 30, 255), INK, 3 * z)
        p.ell(cx, cy, 34 * z, 34 * z, CHROME, INK, 2 * z)
        p.ell(cx, cy, 10 * z, 10 * z, (140, 140, 145, 255), None)
    # shadow under the car
    p.ell(*W2S(cam, 970, 772), 640 * z, 18 * z, (0, 0, 0, 70), None)

def mic(p, hand, ang, S):
    """reporter mic: stick from the hand at angle ang (radians, 0 = right), ball head + pink logo cube"""
    hx, hy = hand; ex, ey = hx + math.cos(ang) * 46 * S, hy + math.sin(ang) * 46 * S
    p.line([(hx, hy), (ex, ey)], (30, 30, 34, 255), 7 * S)
    cx, cy = hx + math.cos(ang) * 34 * S, hy + math.sin(ang) * 34 * S
    p.rect(cx - 11 * S, cy - 11 * S, cx + 11 * S, cy + 11 * S, (212, 83, 126, 255), INK, 1.5 * S, 3 * S)
    gx, gy = hx + math.cos(ang) * 56 * S, hy + math.sin(ang) * 56 * S
    p.ell(gx, gy, 14 * S, 14 * S, (70, 70, 76, 255), INK, 2 * S)
    p.line([(gx - 9 * S, gy - 4 * S), (gx + 9 * S, gy - 4 * S)], (120, 120, 128, 255), 1.5 * S)
    p.line([(gx - 9 * S, gy + 4 * S), (gx + 9 * S, gy + 4 * S)], (120, 120, 128, 255), 1.5 * S)
    return cx, cy

SMOKE = np.random.default_rng(5).uniform(0, 1, (18, 3))
def smoke(p, x, y, z, tt, dens=1.0, big=0.0):
    for i, (a, b, c) in enumerate(SMOKE[:int(18 * dens)]):
        u = (tt * (0.28 + 0.2 * b) + a) % 1
        sx = x + (math.sin(u * 5 + i) * 18 + u * 30) * z; sy = y - u * 170 * z
        r = (5 + 16 * u + big * 30 * u) * z
        p.ell(sx, sy, r, r, (235, 235, 240, int(120 * (1 - u))), None)

def person(lay, cam, who, pos, tt, expr="neutral", look=0, arms="down", held=None, lean=0.0, eat=None, hop=0.0, mouth_k=None):
    x0, y0, z = cam; x, y, s = pos
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    if mouth_k is not None: mouth = max(mouth, mouth_k)
    blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11 and expr != "sleepy"
    yy_ = y - jump_off(who, tt) - hop
    X, Y, S = (x - x0) * z, (yy_ - y0) * z, s * z
    draw_char(P(lay), who, X, Y, S, expr, mouth, look, blink, arms, tt, held, lean, None, eat)
    return X, Y, S * CH[who]["scale"]

STARS = np.random.default_rng(9).uniform(0, 1, (10, 3))
def dream(p, cam, tt):
    """thought bubble over the car: a shiny new 2026 car"""
    if not (DREAM <= tt < POP + 0.25): return
    z = cam[2]; grow = ease(kk(tt, DREAM, DREAM + 0.35)); popk = kk(tt, POP, POP + 0.25)
    if popk > 0: grow = 1 + popk * 0.25
    al = int(255 * (1 - popk))
    bx, by = W2S(cam, 1190, 230); rw, rh = 300 * z * grow, 150 * z * grow
    for i, (dx, dy, r) in enumerate(((-150, 190, 14), (-200, 245, 9))):                 # trail of dots to his head
        if grow > 0.3: p.ell(*W2S(cam, 1190 + dx * 1.2 - 100, 230 + dy), r * z, r * z, (255, 255, 255, al), INK if al > 200 else None, 2 * z)
    for ox, oy, rr in ((-0.6, 0.1, 0.55), (-0.2, -0.35, 0.6), (0.3, -0.3, 0.6), (0.65, 0.05, 0.5), (0.2, 0.35, 0.55), (-0.3, 0.35, 0.55)):
        p.ell(bx + ox * rw, by + oy * rh, rr * rw * 0.6, rr * rh * 0.95, (255, 255, 255, al), INK, 2.5 * z)
    for ox, oy, rr in ((-0.6, 0.1, 0.55), (-0.2, -0.35, 0.6), (0.3, -0.3, 0.6), (0.65, 0.05, 0.5), (0.2, 0.35, 0.55), (-0.3, 0.35, 0.55)):
        p.ell(bx + ox * rw, by + oy * rh, max(0.5, rr * rw * 0.6 - 3 * z), max(0.5, rr * rh * 0.95 - 3 * z), (255, 255, 255, al), None)
    p.ell(bx, by, rw * 0.92, rh * 0.82, (255, 255, 255, al), None)
    if grow < 0.8 or popk > 0: return
    # the dream car (sleek, red, chrome) — slides in
    sl = 1 - ease(kk(tt, DREAM + 0.3, DREAM + 0.8)); cx = bx + sl * 180 * z; cy = by + 30 * z; s2 = z * 0.9
    red = (205, 28, 40, 255)
    p.poly([(cx - 190 * s2, cy + 20 * s2), (cx - 170 * s2, cy - 10 * s2), (cx - 70 * s2, cy - 22 * s2), (cx - 30 * s2, cy - 62 * s2),
            (cx + 80 * s2, cy - 62 * s2), (cx + 140 * s2, cy - 20 * s2), (cx + 190 * s2, cy - 12 * s2), (cx + 196 * s2, cy + 22 * s2)], red, INK, 2.5 * s2)
    p.poly([(cx - 20 * s2, cy - 22 * s2), (cx + 6 * s2, cy - 54 * s2), (cx + 74 * s2, cy - 54 * s2), (cx + 118 * s2, cy - 22 * s2)], (150, 200, 235, 255), INK, 2 * s2)
    p.line([(cx - 180 * s2, cy + 2 * s2), (cx + 190 * s2, cy + 2 * s2)], CHROME, 3 * s2)
    for wx in (-110, 125):
        p.ell(cx + wx * s2, cy + 22 * s2, 30 * s2, 30 * s2, (25, 25, 28, 255), INK, 2 * s2); p.ell(cx + wx * s2, cy + 22 * s2, 15 * s2, 15 * s2, CHROME, None)
    p.rect(cx + 150 * s2, cy - 6 * s2, cx + 192 * s2, cy + 4 * s2, (255, 245, 200, 255), None)
    for i, (a, b, c) in enumerate(STARS):                                                  # sparkles
        u = (tt * 1.4 + a) % 1; sx, sy = cx + (a - 0.5) * 380 * s2, cy - 70 * s2 + (b - 0.5) * 110 * s2; r = (4 + 10 * math.sin(u * math.pi)) * s2
        p.poly([(sx, sy - r), (sx + r * 0.3, sy - r * 0.3), (sx + r, sy), (sx + r * 0.3, sy + r * 0.3), (sx, sy + r), (sx - r * 0.3, sy + r * 0.3), (sx - r, sy), (sx - r * 0.3, sy - r * 0.3)], (255, 230, 120, 255), None)

def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255):
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(LZ, size)
    kw = dict(font=f, anchor="mm", direction="rtl", language="ar")
    d.text((x, y), s, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), **kw)
    d.text((x, y), s, fill=(255, 255, 255, alpha), stroke_width=max(2, size // 22), stroke_fill=(255, 255, 255, alpha), **kw)
    d.text((x, y), s, fill=fill + (alpha,), **kw)
    img.paste(lay, (0, 0), lay)
def popk(tt, t0, d=0.22):
    u = kk(tt, t0, t0 + d); return 0 if u <= 0 else (1 + 0.25 * math.sin(u * math.pi)) if u < 1 else 1

def mic_logo(fr, tt, t0, t1):
    """lower-third: «ميكروفون توتة» series tag"""
    k = min(ease(kk(tt, t0, t0 + 0.35)), 1 - ease(kk(tt, t1 - 0.35, t1)))
    if k <= 0: return
    d = ImageDraw.Draw(fr, "RGBA"); x = -520 + 580 * k
    d.rounded_rectangle([x, 60, x + 560, 170], 26, fill=(212, 83, 126, 235), outline=(255, 255, 255, 255), width=4)
    lzt(fr, x + 320, 108, "ميكروفون توتة", 64, (255, 255, 255))
    ic = Image.new("RGBA", (int(W * SS), int(H * SS)), (0, 0, 0, 0)); mic(P(ic), (x + 70, 140), -1.1, 1.4)
    ic = ic.resize((W, H), Image.LANCZOS); fr.paste(ic, (0, 0), ic)

def chip(fr, y, txt, t0, tt, out_t=None):
    sc = popk(tt, t0)
    if sc <= 0: return
    al = 255 if out_t is None else int(255 * (1 - kk(tt, out_t, out_t + 0.3)))
    if al <= 0: return
    d = ImageDraw.Draw(fr, "RGBA"); w = 420 * sc; h = 70 * sc; x1 = W - 60; x0 = x1 - w
    d.rounded_rectangle([x0, y - h / 2, x1, y + h / 2], int(20 * sc), fill=(20, 20, 26, int(al * 0.85)), outline=(255, 214, 90, al), width=3)
    lzt(fr, (x0 + x1) / 2, y - 2, txt, int(42 * sc), (255, 214, 90), alpha=al)

def calc_cards(fr, tt):
    if not (CALC <= tt < CUTB + 0.01): return
    for i, (t0, a, b) in enumerate(NUMS):
        sc = popk(tt, t0)
        if sc <= 0: continue
        d = ImageDraw.Draw(fr, "RGBA"); cx, cy = 1450, 250 + i * 175; w, h = 560 * sc, 140 * sc
        d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], int(28 * sc), fill=(255, 255, 255, 235), outline=(30, 30, 30, 255), width=4)
        lzt(fr, cx + 90 * sc, cy - 4, a, int(64 * sc), (30, 150, 70))
        lzt(fr, cx - 175 * sc, cy, b, int(40 * sc), (60, 60, 70), outer=(255, 255, 255))
    if tt >= X30:
        sc = popk(tt, X30); lzt(fr, 1450, 790, "× 30 سَنَه", int(70 * sc), (255, 214, 90))
def million(fr, tt):
    if not (MIL <= tt < CUTB + 0.9): return
    sc = popk(tt, MIL, 0.3); sh_ = rng.normal(0, 6) if tt - MIL < 0.4 else 0
    d = ImageDraw.Draw(fr, "RGBA"); al = int(255 * (1 - kk(tt, CUTB + 0.6, CUTB + 0.9)))
    d.rounded_rectangle([W / 2 - 560 * sc, 80, W / 2 + 560 * sc, 260 * sc + 40], 34, fill=(20, 20, 26, int(al * 0.85)), outline=(255, 214, 90, al), width=5)
    lzt(fr, W / 2 + sh_, 170 * sc + 10, "1,095,000 جنيه!", int(118 * sc), (255, 214, 90), alpha=al)

def endcard(tt, sh):
    k = kk(tt, sh["start"], sh["start"] + 0.4)
    base = frame_cache(FREEZE)
    fr = ImageEnhance.Brightness(base).enhance(1 - 0.55 * k).filter(ImageFilter.GaussianBlur(6 * k))
    fr = fr.convert("RGBA")
    sc = popk(tt, sh["start"] + 0.1, 0.3)
    if sc > 0:
        lzt(fr, W / 2, 420, "ميكروفون توتة", int(150 * sc), (255, 255, 255))
        d = ImageDraw.Draw(fr, "RGBA"); d.rounded_rectangle([W / 2 - 420, 520, W / 2 + 420, 600], 30, fill=(212, 83, 126, 230))
        lzt(fr, W / 2, 558, "حلقة جديدة… سؤال جديد!", 54, (255, 255, 255))
    if tt >= sh["start"] + 0.6:
        logo(fr, W / 2, 760, 120)
        text(fr, W / 2, 900, "@shattawzalata", 50, (255, 214, 90))
    return fr.convert("RGB")
_FC = {}
def frame_cache(t_):
    if t_ not in _FC: _FC[t_] = frame(t_)
    return _FC[t_]
# brand logo helpers (chili / leaf / logo) without running the brand-pack script
_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/mic/01")

# ---------------- frame ----------------
def frame(tt):
    sh = shot_at(tt); set_ = sh["set"]
    if set_ == "end": return finish(endcard(tt, sh), tt)
    cam = cam_at(sh, tt); x0, y0, z = cam
    img = bg_crop(STREET, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    car_back(p, cam)
    # --- البواب ---
    asleep = tt < WAKE
    bexpr = "sleepy" if asleep else "happy"
    if tt >= PUFF: bexpr = "smug"
    if tt >= DROP: bexpr = "shock"
    if DREAM <= tt < POP: bexpr = "happy"
    if tt >= POP: bexpr = "flat"
    if tt >= SLY: bexpr = "smug"
    blook = 0 if asleep else -1
    if DREAM + 0.2 <= tt < POP: blook = 1
    lift = 10 if PROUD <= tt < PROUD + 3 else 0
    bpos = (BW[0], BW[1] - lift, BW[2])
    BX, BY, BS = person(lay, cam, "bondo2", bpos, tt, bexpr, blook, "down", None, -0.6 if asleep else 0.0)
    if asleep:   # Zzz
        for i in range(3):
            u = ((tt * 0.8) + i / 3) % 1
            text(lay, (BX + (50 + 30 * u + i * 6) * BS) * SS, (BY - (230 + 120 * u) * BS) * SS, "Z", int((24 + 16 * i) * BS * SS), (255, 255, 255, int(255 * (1 - u))), sw=2)
    car_front(p, cam, tt)
    # his hand on the window sill with the cigarette (drops on «مليون»)
    hx, hy = W2S(cam, 690, 494)
    p.line([(BX - 22 * BS, BY - 126 * BS), (hx + 14 * z, hy - 6 * z)], INK, 5 * BS)
    p.ell(hx, hy, 9 * z, 8 * z, INK, None)
    if tt < DROP:
        p.line([(hx - 4 * z, hy - 2 * z), (hx - 40 * z, hy - 8 * z)], (245, 245, 240, 255), 6 * z)
        p.line([(hx - 32 * z, hy - 6.5 * z), (hx - 40 * z, hy - 8 * z)], (230, 150, 60, 255), 6 * z)
        smoke(p, hx - 42 * z, hy - 10 * z, z, tt, 1.0)
    elif tt < DROP + 0.6:   # falls
        u = kk(tt, DROP, DROP + 0.6); cy_ = hy + u * u * 260 * z
        p.line([(hx - 10 * z, cy_), (hx - 44 * z, cy_ + 10 * z)], (245, 245, 240, 255), 6 * z)
    if PUFF <= tt < PUFF + 1.8:   # a big puff from his mouth drifting to Tota
        u = kk(tt, PUFF, PUFF + 1.8)
        for j in range(5):
            r = (14 + 40 * u + j * 6) * z; sx = BX - (30 + 260 * u + j * 18) * z; sy = BY - 200 * BS + (40 * u + j * 6) * z
            p.ell(sx, sy, r, r * 0.7, (238, 238, 242, int(150 * (1 - u))), None)
    # --- توتة + mic ---
    t_ex = "happy"
    if tt >= SUSP: t_ex = "flat"
    if PUFF + 0.3 <= tt < PUFF + 1.6: t_ex = "sleepy"     # squints in the smoke
    if tt >= PUNCH + DUR["P16"]: t_ex = "shock"
    k, lt = line_at(tt); tota_talks = k is not None and WHO.get(k) == "tota"
    tarms = "hold" if tota_talks else "point"
    if tt >= PUNCH + DUR["P16"] + 0.2: tarms = "down"
    TX, TY, TS = person(lay, cam, "tota", TW, tt, t_ex, 1, tarms)
    shy = TY - 134 * TS
    if tarms != "down":
        hand = (TX + 46 * TS, shy + 30 * TS) if tarms == "hold" else (TX + 84 * TS, shy - 6 * TS)
        if tota_talks: tgt = (TX + 6 * TS, TY - 168 * TS)
        else: tgt = (BX - 20 * BS, BY - 168 * BS)
        ang = math.atan2(tgt[1] - hand[1], tgt[0] - hand[0])
        mic(p, hand, ang, TS)
    else:   # mic drops to her side
        mic(p, (TX + 34 * TS, shy + 76 * TS), 1.9, TS)
    # --- شطة in the doorway ---
    if LAUGH <= tt:
        lt2 = tt - LAUGH; shake = math.sin(lt2 * 34) * 8 * (1 if tt < FREEZE else 0)
        person(lay, cam, "shatta", (SWP[0] + shake, SWP[1], SWP[2]), tt, "laugh", -1, "hips", None, 0.0, None, abs(math.sin(lt2 * 9)) * 14)
    else:
        eat = ((tt * 0.55) % 1.0)
        if SH1[0] <= tt < SH1[1]: eat = 0.62 + 0.1 * kk(tt, *SH1)        # stops mid-bite, watching
        person(lay, cam, "shatta", SWP, tt, "neutral", -1, "down", "chipsbag", 0.0, eat)
    dream(p, cam, tt)
    lay = tint_layer(lay, (255, 232, 205)); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    # --- overlays ---
    mic_logo(fr, tt, EST[0] + 0.4, EST[1] - 0.1)
    if F1 <= tt < CALC + 0.3:
        chip(fr, 90, "علبتين في اليوم", F1, tt, CALC); chip(fr, 175, "العلبة بـ 50 جنيه", F2, tt, CALC); chip(fr, 260, "بقاله 30 سَنَه", F3, tt, CALC)
    calc_cards(fr, tt); million(fr, tt)
    if M26 <= tt < POP:
        cam2 = cam; bx, by = W2S(cam2, 1190, 230); sc = popk(tt, M26)
        lzt(fr, bx, by - 105 * z * 0.9 + 12, "موديل 2026", int(48 * sc * z / 1.37), (205, 28, 40))
    if LAUGH + 0.3 <= tt and set_ == "st":
        for i, (dx, dy, sz) in enumerate(((-360, -250, 110), (280, -320, 92), (-300, 60, 84), (330, -30, 100))):
            t0_ = LAUGH + 0.3 + i * 0.45
            if tt >= t0_:
                sc = popk(tt, t0_); wob = math.sin(tt * 6 + i) * 8
                hx_, hy_ = W2S(cam, SWP[0], SWP[1] - 330)
                lzt(fr, hx_ + dx + wob, hy_ + dy, "ههههه", int(sz * sc), (255, 214, 90))
    if tt >= FREEZE and set_ == "st":   # freeze-frame flash on the trademark laugh
        fr = Image.blend(fr, Image.new("RGB", fr.size, (255, 255, 255)), 0.6 * (1 - kk(tt, FREEZE, FREEZE + 0.2)))
    return finish(fr, tt)

def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(21)
    ts = np.arange(n) / SR
    # street bed: low traffic rumble + birds
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 260) * 0.05, 0, 1.0)
    for bt in np.arange(1.0, TOTAL, 2.7):
        d = np.arange(int(SR * 0.18)) / SR; f0 = 3200 + r.uniform(-400, 600)
        chirp = np.sin(2 * np.pi * (f0 + 1600 * d) * d) * np.exp(-d * 18) * 0.035
        mix_into(buf, chirp.astype(np.float32), bt, 1.0); mix_into(buf, chirp.astype(np.float32), bt + 0.22, 0.7)
    # snore before the taps
    d = np.arange(int(SR * 0.7)) / SR
    mix_into(buf, (lowpass(r.normal(0, 1, len(d)).astype(np.float32), 180) * np.sin(np.pi * d / 0.7) * 0.5), 0.0, 1.0)
    # finger taps on the car roof (light tok)
    d = np.arange(int(SR * 0.09)) / SR; tok = (np.sin(2 * np.pi * 900 * d) * np.exp(-d * 70) + r.normal(0, 1, len(d)) * np.exp(-d * 120) * 0.4) * 0.7
    for tp in TAPS: mix_into(buf, tok.astype(np.float32), tp, 1.0)
    # whooshes on whip cuts
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 0.5: fx(s_["start"] - 0.1, "whoosh", 0.35)
    fx(EST[0] + 0.4, "switch", 0.6)
    for t0, nme, g in sfx:
        if nme in SFXF: mix_into(buf, SFXF[nme], t0, g)
    # pops for chips / cards
    d = np.arange(int(SR * 0.08)) / SR; pop = np.sin(2 * np.pi * (500 + 2500 * d) * d) * np.exp(-d * 45) * 0.45
    for tp in [F1, F2, F3] + [a for a, _, _ in NUMS] + [X30]: mix_into(buf, pop.astype(np.float32), tp, 1.0)
    # ka-ching on the million
    d = np.arange(int(SR * 1.0)) / SR
    ching = (np.sin(2 * np.pi * 2093 * d) + 0.6 * np.sin(2 * np.pi * 2637 * d) + 0.4 * np.sin(2 * np.pi * 3136 * d)) * np.exp(-d * 4) * 0.3
    mix_into(buf, ching.astype(np.float32), MIL, 1.0)
    clk = (r.normal(0, 1, int(SR * 0.04)) * np.exp(-np.arange(int(SR * 0.04)) / SR * 90) * 0.5).astype(np.float32)
    mix_into(buf, clk, MIL - 0.08, 1.0)
    # dream: harp-ish sparkle up, then bubble pop
    for i, f in enumerate((523, 659, 784, 1047, 1319)):
        d = np.arange(int(SR * 0.6)) / SR; mix_into(buf, (np.sin(2 * np.pi * f * d) * np.exp(-d * 5) * 0.12).astype(np.float32), DREAM + i * 0.07, 1.0)
    d = np.arange(int(SR * 0.12)) / SR; mix_into(buf, (np.sin(2 * np.pi * (900 - 3000 * d) * d) * np.exp(-d * 30) * 0.6).astype(np.float32), POP, 1.0)
    # awkward silence: crickets
    cr = (np.sin(2 * np.pi * 4300 * ts) * (np.sin(2 * np.pi * 28 * ts) > 0.6) * (np.sin(2 * np.pi * 1.4 * ts) > 0) * 0.03).astype(np.float32)
    a, b = int((PUNCH + DUR["P16"]) * SR), int(STUN[1] * SR); buf[a:b] += cr[a:b]
    # end: little jingle (brand)
    for i, f in enumerate((784, 988, 1175, 1568)):
        d = np.arange(int(SR * 0.4)) / SR; mix_into(buf, (np.sin(2 * np.pi * f * d) * np.exp(-d * 6) * 0.14).astype(np.float32), TOTAL - 2.4 + i * 0.09, 1.0)
    mix_lines(buf)
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
