# «مين الكداب؟» — القضية 10: «مين سرق كاس زلطة؟» (23/11, 20:00 Kuwait) — growth rules 1–32
# Canonical lobby (s1e10/bg/morning.png, night grade) + «أوضة بندق وعزيزة» (daily/bg/bandaq_room.png, night).
# Opening = separate «حل القضية السابقة» (parrot → Shatta). Then a SILENT hook with readable clues:
#   8:59 trophy in the showcase · Aziza's room TV glowing · 9:00 blackout (lobby AND her TV die) · flashlight theft,
#   a gold hoop earring with a red bead drops and rolls under the showcase (beam lingers ~1.25 s) · clock spins to 9:30 ·
#   lights + her TV come back · Zalata finds the empty showcase. Suspects ① بندق ② شطة ③ عزيزة (badges on screen).
#   Aziza comes OUT of that same room before her alibi; she wears ONE hoop (same design).
# ANSWER (say it at the END of case 11 only): عزيزة ③ — TV was dark 9:00–9:30 (we saw it) + her missing earring at the showcase.
#   Comic motive for case 11: she took the trophy to use it as a flower vase for her room.
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont, ImageChops
import engine as ENG
os.chdir(ROOT + "/kaddab/10")
SERIES = "مين الكداب؟"; EPT = "مين سرق كاس زلطة؟"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"; DJ = ROOT + "/brand/fonts/DejaVuSans-Bold.ttf"
SFXF = {n: load_audio(ROOT + f"/trend/01/sfx/{n}.mp3") for n in ("whoosh", "stinger", "gasp", "switch")}
SUB = {"A0": "الكداب في قضية البغبغان كان شطة! البغبغان بيقول «يا نهار أبيض»… ودي جملة شطة… يعني شطة بيدخل الشقة كتير!",
       "Z1": "كاس مسابقة العلوم بتاعي… اختفى!", "T1": "آخر مرة شفته إمتى؟",
       "Z2": "الساعة تسعة كان هنا… ولما نزلت تسعة ونص، لقيت الفاترينة فاضية!",
       "B1": "أنا كنت قاعد على الدكة قدام باب العمارة… ومحدش خرج!", "S1": "أنا كنت نايم في أوضتي من بدري!",
       "AZ1": "أنا كنت بتفرج على المسلسل في أوضتي… من تسعة لتسعة ونص ما قمتش من قدام التلفزيون!",
       "T2": "الدليل قدامكم من أول الحلقة… مين اللي خد الكاس؟ اكتبوا رقمه في الكومنتات!"}
CHUNKS = {"A0": [(0.0, "الكداب في قضية البغبغان كان شطة!", "شطة"), (3.3, "البغبغان بيقول «يا نهار أبيض»…", "يا نهار أبيض"),
                 (6.1, "ودي جملة شطة…", None), (7.45, "يعني شطة بيدخل الشقة كتير!", "كتير")],
          "Z1": [(0.0, "كاس مسابقة العلوم بتاعي…", "كاس"), (3.0, "اختفى!", "اختفى")],
          "T1": [(0.0, "آخر مرة شفته إمتى؟", "إمتى")],
          "Z2": [(0.0, "الساعة تسعة كان هنا…", None), (1.65, "ولما نزلت تسعة ونص، لقيت الفاترينة فاضية!", "فاضية")],
          "B1": [(0.0, "(بيتثاوب)", None), (1.95, "أنا كنت قاعد على الدكة قدام باب العمارة…", "الدكة"), (5.15, "ومحدش خرج!", "محدش خرج")],
          "S1": [(0.0, "أنا كنت نايم في أوضتي من بدري!", "نايم")],
          "AZ1": [(0.0, "أنا كنت بتفرج على المسلسل في أوضتي…", None), (2.5, "من تسعة لتسعة ونص ما قمتش من قدام التلفزيون!", None)],
          "T2": [(0.0, "الدليل قدامكم من أول الحلقة…", "من أول الحلقة"), (3.35, "مين اللي خد الكاس؟", "مين"), (4.8, "اكتبوا رقمه في الكومنتات!", "رقمه")]}
WHO = {"A0": "zalata", "Z1": "zalata", "T1": "tota", "Z2": "zalata", "B1": "bondo2", "S1": "shatta", "AZ1": "aziza", "T2": "tota"}
NAME = {"zalata": ("زلطة", (140, 210, 80)), "shatta": ("شطة", (255, 140, 80)), "aziza": ("عزيزة", (255, 110, 170)),
        "tota": ("توتة", (255, 130, 190)), "bondo2": ("بندق", (230, 170, 110))}
EXPR = {"A0": "smug", "Z1": [(0, "shock"), (0.5, "sad")], "T1": "flat", "Z2": "sad", "B1": [(0, "sleepy"), (0.3, "neutral")],
        "S1": "angry", "AZ1": "smug", "T2": "smug"}
load_lines(list(SUB))
def tinted(img, lvl, tint): return ImageChops.multiply(ImageEnhance.Brightness(img).enhance(lvl), Image.new("RGB", img.size, tint))
LOBBY = tinted(_ld(ROOT + "/s1e10/bg/morning.png"), 0.95, (160, 172, 232))        # night, lamps on (canonical lobby)
ROOMN = tinted(_ld(ROOT + "/daily/bg/bandaq_room.png"), 0.75, (200, 190, 235))     # Aziza & Bandaq's room at night (lamp)
COVER9 = None

def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
SHOW = (1050, 430, 1195, 640)             # showcase on the pillar (glass box), legs to 668
CLOCK = (1122, 240)                        # wall clock above it
EAR_REST = (1206, 676)                     # where the dropped earring ends (under the showcase)
TV = (1560, 560)                           # TV in Aziza's room (centre of the screen)
POS = {"tota": (640, 1012, 1.6), "zalata": (900, 1012, 1.6), "bondo2": (1270, 1012, 1.6), "shatta": (1480, 1012, 1.6), "aziza": (1690, 1012, 1.6)}
NUMS = (("bondo2", (150, 96, 50)), ("shatta", (230, 90, 40)), ("aziza", (196, 40, 96)))
def body(who, x, y, s):
    S = s * CH[who]["scale"]; sh = y - 134 * S; return S, sh, (x, sh - 56 * S)

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
say(0.45, "A0"); PREV_END = T("A0") + DUR["A0"] + 0.5
shot("prev", 0.0, PREV_END, None, v=None)
t = PREV_END
H1 = t; shot("lobby", t, t + 2.6, (1000, 560, 1.35), (1110, 380, 2.2), v=((1000, 560, 1.85), (1120, 420, 2.4))); t += 2.6        # trophy + clock 8:59
H2 = t; shot("room", t, t + 1.5, (1150, 520, 1.45), (1450, 540, 1.9), tin="whip", v=((1000, 500, 1.8), (1500, 540, 2.2))); t += 1.5  # her TV glowing
TICK = t + 0.55; H3 = t; shot("clock", t, t + 1.0, (CLOCK[0], CLOCK[1], 4.2), (CLOCK[0], CLOCK[1], 4.6), tin="whip", v=((CLOCK[0], CLOCK[1], 4.4), (CLOCK[0], CLOCK[1], 4.8))); t += 1.0
H4 = t; shot("room", t, t + 1.0, (1560, 560, 2.85), (1560, 555, 3.0), v=((1560, 560, 2.95), (1560, 555, 3.1))); t += 1.0      # her TV dies with everything
THEFT = t; shot("lobby", t, t + 4.4, (1120, 560, 2.2), (1160, 600, 2.6), v=((1120, 560, 2.4), (1170, 600, 2.8))); t += 4.4  # flashlight theft + earring
TAKE = THEFT + 1.2; DROP = THEFT + 1.9; LAND = DROP + 0.45; BEAM_OFF = LAND + 1.6
JUMP = t; shot("clock", t, t + 2.0, (CLOCK[0], CLOCK[1], 4.0), (CLOCK[0], CLOCK[1], 4.3), v=((CLOCK[0], CLOCK[1], 4.2), (CLOCK[0], CLOCK[1], 4.5))); t += 2.0
LIGHTS = t - 0.3
H7 = t; shot("room", t, t + 0.8, (1560, 560, 2.7), (1560, 555, 2.8), v=((1560, 560, 2.8), (1560, 555, 2.9))); t += 0.8           # her TV back on
H8 = t; shot("lobby", t, t + 2.2, (1150, 520, 1.7), (1000, 600, 1.5), tin="whip", v=((1130, 520, 2.0), (1000, 600, 1.9))); t += 2.2   # empty showcase, Zalata comes down
ZDOWN = (H8 + 0.2, H8 + 2.0)
s = t; t = say(t, "Z1") + 0.2; shakes.append((s + 0.05, 10))
shot("lobby", s, t, (930, 700, 2.6), (930, 690, 2.9), ease="crash", v=((920, 700, 2.8), (920, 690, 3.1)))
s = t; TIN = (s - 0.4, s + 0.8); t = say(t + 0.1, "T1") + 0.2
shot("lobby", s, t, (700, 700, 2.4), (680, 690, 2.6), tin="whip", v=((660, 700, 2.7), (650, 690, 2.9)))
s = t; t = say(t, "Z2") + 0.2
shot("lobby", s, t, (950, 650, 2.0), (1000, 640, 2.2), tin="whip", v=((930, 650, 2.3), (980, 640, 2.4)))
LINE = t; BIN = (t, t + 1.6); SIN = (t, t + 1.6)
shot("lobby", t, t + 1.7, (1050, 640, 1.25), (1180, 650, 1.3), tin="whipl", v=((1280, 620, 1.8), (1480, 620, 1.85))); t += 1.7     # ① ② walk in
ROOMX = t; shot("room", t, t + 1.8, (1300, 600, 1.4), (750, 600, 1.45), tin="whip", v=((1450, 600, 1.8), (500, 600, 1.85))); t += 1.8   # Aziza leaves HER room (TV on behind)
AIN = (t, t + 1.4); shot("lobby", t, t + 1.5, (1250, 640, 1.25), (1250, 650, 1.28), v=((1500, 620, 1.8), (1700, 620, 1.85))); t += 1.5  # ③ walks in from the right
BADGES = AIN[1] - 0.2
for k_, who in (("B1", "bondo2"), ("S1", "shatta"), ("AZ1", "aziza")):
    s = t; t = say(t + 0.1, k_) + 0.2; x_ = POS[who][0]
    shot("lobby", s, t, (x_, 700, 2.6), (x_, 690, 2.85), tin="whip", v=((x_, 700, 2.85), (x_, 690, 3.05)))
s = t; t = say(t + 0.1, "T2") + 0.2; ASK = s
shot("lobby", s, t, (660, 700, 2.4), (650, 680, 2.8), tin="whipl", v=((650, 700, 2.7), (650, 680, 3.0)))
Q = t; shot("q", t, t + 1.8, None, v=None); t += 1.8
TOTAL = t
ENG.AZIZA_EARS[:] = [-1, 1]
def hcam(sh, tt):
    """H camera (top-left form): z = output px per world unit"""
    return cam_at(sh, tt)
def vcam(sh, tt):
    c0, c1 = sh["v"]; k = ease((tt - sh["start"]) / max(0.01, sh["end"] - sh["start"]), sh.get("ease"))
    cx, cy, z = [a_ + (b_ - a_) * k for a_, b_ in zip(c0, c1)]; z = max(z, 1920 / 1080)
    shake = 0
    for st, amp in shakes:
        if 0 <= tt - st < 0.45: shake = max(shake, amp * (1 - (tt - st) / 0.45))
    cw, ch = 1080 / z, 1920 / z
    x0 = min(max(cx - cw / 2 + math.sin(tt * 0.9) * 3, 0), 1920 - cw); y0 = min(max(cy - ch / 2 + math.sin(tt * 1.3) * 2, 0), 1080 - ch)
    if shake: x0 = min(max(x0 + rng.normal(0, shake / z), 0), 1920 - cw); y0 = min(max(y0 + rng.normal(0, shake / z), 0), 1080 - ch)
    return x0, y0, z

# ---------------- helpers ----------------
def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255, font=None, rot=0, stroke=True):
    if size < 4: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(font or LZ, size)
    kw = dict(font=f, anchor="mm", direction="rtl", language="ar") if font is None else dict(font=f, anchor="mm")
    if stroke: d.text((x, y), s, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), **kw)
    d.text((x, y), s, fill=fill + (alpha,), **kw)
    if rot: lay = lay.rotate(rot, center=(x, y), resample=Image.BICUBIC)
    img.paste(lay, (0, 0), lay)
def popk(tt, t0, d=0.22):
    u = kk(tt, t0, t0 + d); return 0 if u <= 0 else (1 + 0.25 * math.sin(u * math.pi)) if u < 1 else 1
def badge(fr, x, y, n, sc, col):
    if sc <= 0: return
    d = ImageDraw.Draw(fr, "RGBA"); r = 46 * sc
    d.ellipse([x - r, y - r, x + r, y + r], fill=col + (255,), outline=(255, 255, 255, 255), width=max(1, int(6 * sc)))
    lzt(fr, x, y + 4 * sc, n, int(70 * sc), (255, 255, 255), font=DJ)

_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/kaddab/10")

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, held=None):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    blink = ((tt + len(who) * 0.37) % 3.6) < 0.11 and expr not in ("laugh", "scared", "shout")
    if not talking: lean += math.sin(tt * 1.7 + len(who)) * 0.04
    X, Y_ = W2S(cam, x, y); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, held, lean, None)


def magnifier(p, x, y, s, ang=-0.7):
    """lens centered (x,y) in output px; s = output px per world unit"""
    r = 22 * s; hx, hy = x + math.cos(ang + math.pi) * -r * 1.0, y + math.sin(ang + math.pi) * -r * 1.0
    p.line([(x + math.cos(ang) * r, y - math.sin(ang) * r * -1), (x + math.cos(ang) * r * 2.3, y + math.sin(-ang) * -r * 2.3)], (110, 70, 36, 255), 6 * s)
    p.ell(x, y, r, r, (200, 230, 255, 70), (40, 40, 46, 255), 4 * s)

def sweat(d, cam, x, hy, S, tt, n=2):
    z = cam[2]
    for i in range(n):
        u = (tt * 0.9 + i * 0.5) % 1.0; q = W2S(cam, x + (-40 + 80 * i) * S, hy - 20 * S + u * 50 * S); r = 5 * S * z
        d.ellipse([q[0] - r, q[1] - r * 1.5, q[0] + r, q[1] + r * 1.5], fill=(190, 225, 255, int(230 * (1 - u))), outline=(60, 110, 170, int(255 * (1 - u))), width=2)



def rays(fr, Wd, Hd, c0, c1, tt, sign=1, cy=0.6):
    d = ImageDraw.Draw(fr, "RGBA")
    for i in range(18):
        a0 = i * 20 + sign * tt * 6; a_ = math.radians(a0); b = math.radians(a0 + 9); R = 3000
        d.polygon([(Wd / 2, Hd * cy), (Wd / 2 + R * math.cos(a_), Hd * cy + R * math.sin(a_)), (Wd / 2 + R * math.cos(b), Hd * cy + R * math.sin(b))], fill=c1 + (255,))



# ---------------- subtitles (phrase chunks + speaker name) ----------------
def sub_chunk(img, tt, cx, cy, size):
    k, lt = line_at(tt)
    if not k or k not in CHUNKS: return
    cur = None
    for off, txt, key in CHUNKS[k]:
        if lt >= off: cur = (off, txt, key)
    if cur is None: return
    off, txt, key = cur; sc = popk(lt, off, 0.15) if lt - off < 0.15 else 1
    f = ImageFont.truetype(LZ, max(6, int(size * sc)))
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    kw = dict(font=f, direction="rtl", language="ar", stroke_width=max(4, size // 10), stroke_fill=(10, 10, 10, 255))
    if key and key in txt:
        a_, b_ = txt.split(key, 1); parts = [(a_, (255, 255, 255)), (key, (255, 214, 60)), (b_, (255, 255, 255))]
    else: parts = [(txt, (255, 255, 255))]
    widths = [d.textlength(s, font=f, direction="rtl", language="ar") if s else 0 for s, _ in parts]
    maxw = img.size[0] * 0.88
    if sum(widths) > maxw:                                                          # never cut a long phrase: shrink to fit
        f = ImageFont.truetype(LZ, max(6, int(size * sc * maxw / sum(widths)))); kw["font"] = f
        widths = [d.textlength(s, font=f, direction="rtl", language="ar") if s else 0 for s, _ in parts]
    tot = sum(widths); x = cx + tot / 2
    for (s, col), w_ in zip(parts, widths):
        if s: d.text((x - w_, cy), s, fill=col + (255,), anchor="lm", **kw)
        x -= w_
    nm, ncol = NAME[WHO[k]]; fn = ImageFont.truetype(LZ, int(size * 0.62))           # growth rule 9: speaker name in his colour
    nw = d.textlength(nm, font=fn, direction="rtl", language="ar")
    nx = cx + tot / 2 - nw / 2 - 10; ny = cy - size * 0.95
    d.rounded_rectangle([nx - nw / 2 - 18, ny - size * 0.38, nx + nw / 2 + 18, ny + size * 0.38], int(size * 0.3), fill=ncol + (235,))
    d.text((nx, ny), nm, font=fn, fill=(20, 12, 8, 255), anchor="mm", direction="rtl", language="ar")
    img.paste(lay, (0, 0), lay)

def subtitle(img, tt): sub_chunk(img, tt, W / 2, H - 80, 62)

# ---------------- audio ----------------
def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def creak(dur=0.9, amp=0.25):
    n = int(SR * dur); t_ = np.arange(n) / SR; f = 180 + 90 * np.sin(t_ * 9) + 40 * np.sin(t_ * 31)
    x = np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * (0.5 + 0.5 * np.abs(np.sin(t_ * 47)))
    return (lowpass(x.astype(np.float32), 1600) * np.hanning(n) * amp).astype(np.float32)

# ---------------- props ----------------
def clock_time(tt):
    """minutes after 8:00 shown on the wall clock"""
    if tt < TICK - 0.05: return 59 - 0.05 * (TICK - 0.05 - tt) * 0
    if tt < JUMP: return 60
    if tt < JUMP + 1.5: return 60 + 30 * ease(kk(tt, JUMP + 0.2, JUMP + 1.5))
    return 90
def lights_on(tt): return not (TICK <= tt < LIGHTS)
def draw_clock(d, Q_, zz, tt, dark):
    cx, cy = Q_(*CLOCK); R = 34 * zz
    d.ellipse([cx - R - 4 * zz, cy - R - 4 * zz, cx + R + 4 * zz, cy + R + 4 * zz], fill=(80, 50, 30))
    d.ellipse([cx - R, cy - R, cx + R, cy + R], fill=(240, 232, 210) if not dark else (60, 62, 80), outline=(40, 30, 20), width=max(1, int(2 * zz)))
    for i in range(12):
        a = i * math.pi / 6; d.line([(cx + math.sin(a) * R * 0.8, cy - math.cos(a) * R * 0.8), (cx + math.sin(a) * R * 0.92, cy - math.cos(a) * R * 0.92)], fill=(30, 30, 30), width=max(1, int(2 * zz)))
    m = clock_time(tt); am = (m % 60) / 60 * 2 * math.pi; ah = (8 + m / 60) / 12 * 2 * math.pi
    d.line([(cx, cy), (cx + math.sin(ah) * R * 0.5, cy - math.cos(ah) * R * 0.5)], fill=(20, 20, 20), width=max(2, int(4 * zz)))
    d.line([(cx, cy), (cx + math.sin(am) * R * 0.8, cy - math.cos(am) * R * 0.8)], fill=(20, 20, 20), width=max(1, int(2.5 * zz)))
    d.ellipse([cx - 3 * zz, cy - 3 * zz, cx + 3 * zz, cy + 3 * zz], fill=(160, 30, 30))
def trophy(d, cx, by, zz, col=(240, 200, 60)):
    """small gold cup, base centre at (cx, by) in SS px"""
    d.rectangle([cx - 16 * zz, by - 8 * zz, cx + 16 * zz, by], fill=(120, 80, 30))
    d.rectangle([cx - 4 * zz, by - 24 * zz, cx + 4 * zz, by - 8 * zz], fill=col)
    d.pieslice([cx - 22 * zz, by - 62 * zz, cx + 22 * zz, by - 18 * zz], 0, 180, fill=col, outline=(150, 110, 20))
    d.rectangle([cx - 22 * zz, by - 42 * zz, cx + 22 * zz, by - 40 * zz], fill=col)
    for sx in (-1, 1): d.arc([cx + sx * 22 * zz - 9 * zz, by - 56 * zz, cx + sx * 22 * zz + 9 * zz, by - 36 * zz], 90 if sx > 0 else -90, 270 if sx > 0 else 90, fill=col, width=max(1, int(3 * zz)))
    d.ellipse([cx - 14 * zz, by - 54 * zz, cx - 6 * zz, by - 44 * zz], fill=(255, 245, 200))
def earring(d, x, y, zz, rot=0.0):
    r = 14 * zz; d.ellipse([x - r, y - r, x + r, y + r], outline=(230, 190, 60), width=max(2, int(4.5 * zz)))
    bx, by = x + math.sin(rot) * r, y + math.cos(rot) * r; rb = 5 * zz
    d.ellipse([bx - rb, by - rb, bx + rb, by + rb], fill=(210, 30, 40), outline=(40, 10, 10))
def trophy_in(tt): return not (TAKE <= tt)
def earring_pos(tt):
    if tt < DROP: return None
    if tt < LAND:
        u = kk(tt, DROP, LAND); return (1165 + 10 * u, 560 + (EAR_REST[1] - 560) * u * u, u * 4)
    u = ease(kk(tt, LAND, LAND + 0.8)); bounce = abs(math.sin(u * math.pi * 2)) * 10 * (1 - u)
    return (lerp(1175, EAR_REST[0], u), EAR_REST[1] - bounce, 4 + u * 6)
def draw_showcase(d, Q_, zz, tt):
    x0, y0, x1, y1 = SHOW; a = Q_(x0, y0); b = Q_(x1, y1)
    for lx in (x0 + 8, x1 - 8):
        p0, p1 = Q_(lx, y1), Q_(lx, y1 + 28); d.line([p0, p1], fill=(70, 45, 25), width=max(1, int(5 * zz)))
    d.rectangle([a[0], a[1], b[0], b[1]], fill=(40, 60, 70, 90), outline=(90, 60, 30), width=max(1, int(5 * zz)))
    sh_ = Q_(x0, y1 - 60); d.line([sh_, (b[0], sh_[1])], fill=(110, 80, 40), width=max(1, int(4 * zz)))
    if trophy_in(tt): c = Q_((x0 + x1) / 2, y1 - 62); trophy(d, c[0], c[1], zz)
    pl = Q_((x0 + x1) / 2, y1 - 22); d.rectangle([pl[0] - 26 * zz, pl[1] - 6 * zz, pl[0] + 26 * zz, pl[1] + 6 * zz], fill=(200, 170, 80))
    # glass door (opens toward camera during the theft)
    op = ease(kk(tt, TAKE - 0.6, TAKE - 0.2)) * (1 - ease(kk(tt, TAKE + 0.3, TAKE + 0.8)))
    dx = (x1 - x0) * 0.25 * op
    d.polygon([Q_(x0 + dx, y0 + 4), Q_(x1 + dx * 0.4, y0 + 4 - 10 * op), Q_(x1 + dx * 0.4, y1 - 4 + 10 * op), Q_(x0 + dx, y1 - 4)], fill=(200, 230, 255, 40), outline=(220, 240, 255, 120))
    gl = Q_(x0 + 12, y0 + 10); gl2 = Q_(x0 + 40, y0 + 60); d.line([gl, gl2], fill=(255, 255, 255, 90), width=max(1, int(3 * zz)))
def draw_tv(d, Q_, zz, tt, on):
    cx, cy = Q_(*TV); w, h = 150 * zz, 104 * zz
    tb = Q_(TV[0], TV[1] + 70); d.rectangle([tb[0] - 120 * zz, tb[1], tb[0] + 120 * zz, tb[1] + 110 * zz], fill=(90, 55, 30), outline=(40, 25, 10))   # small table
    d.rounded_rectangle([cx - w / 2 - 10 * zz, cy - h / 2 - 10 * zz, cx + w / 2 + 10 * zz, cy + h / 2 + 10 * zz], int(12 * zz), fill=(50, 45, 40), outline=(20, 20, 20), width=max(1, int(3 * zz)))
    if on:
        fl = 0.75 + 0.25 * math.sin(tt * 23) * math.sin(tt * 7.3)
        d.rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], fill=(int(80 * fl), int(140 * fl), int(230 * fl)))
        d.ellipse([cx - 22 * zz, cy - 30 * zz, cx + 6 * zz, cy - 2 * zz], fill=(230, 200, 170)); d.rectangle([cx - 26 * zz, cy - 2 * zz, cx + 10 * zz, cy + 40 * zz], fill=(180, 60, 80))   # actress
        d.ellipse([cx + 18 * zz, cy - 26 * zz, cx + 44 * zz, cy], fill=(230, 200, 170)); d.rectangle([cx + 14 * zz, cy, cx + 48 * zz, cy + 40 * zz], fill=(40, 60, 120))
    else: d.rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], fill=(18, 20, 22))
    for sx in (-1, 1): a0 = Q_(TV[0] + sx * 20, TV[1] - 62); a1 = Q_(TV[0] + sx * 44, TV[1] - 100); d.line([a0, a1], fill=(30, 30, 30), width=max(1, int(2 * zz)))
def tv_glow(fr, cam, tt, Wd, Hd):
    if not lights_on(tt): return fr
    X, Y = W2S(cam, *TV); R = 420 * cam[2] / 2.6 * 2.6
    g = Image.new("L", fr.size, 0); ImageDraw.Draw(g).ellipse([X - R, Y - R * 0.8, X + R, Y + R * 0.8], fill=int(70 + 30 * math.sin(tt * 19)))
    return Image.composite(ImageChops.screen(fr, Image.new("RGB", fr.size, (40, 80, 170))), fr, g.filter(ImageFilter.GaussianBlur(60)))

def beam_target(tt):
    """flashlight spot (world) during the theft"""
    k = tt - THEFT
    if k < 0.9: return lerp(700, 1110, ease(kk(k, 0, 0.9))), lerp(800, 560, ease(kk(k, 0, 0.9)))
    if tt < LAND: return 1120, 560
    if tt < LAND + 1.25 + 0.6: return lerp(1130, EAR_REST[0], kk(tt, LAND, LAND + 0.5)), lerp(570, EAR_REST[1], kk(tt, LAND, LAND + 0.5))
    u = kk(tt, LAND + 1.85, BEAM_OFF + 0.4); return lerp(EAR_REST[0], 1700, u), lerp(EAR_REST[1], 640, u)
def darkness(fr, cam, tt, beam=False):
    m = Image.new("L", fr.size, 24)
    if beam and THEFT <= tt < BEAM_OFF + 0.4:
        X, Y = W2S(cam, *beam_target(tt)); R = 95 * cam[2]
        ImageDraw.Draw(m).ellipse([X - R, Y - R * 0.8, X + R, Y + R * 0.8], fill=235)
        m = m.filter(ImageFilter.GaussianBlur(R * 0.25))
    dark = ImageChops.multiply(fr, Image.new("RGB", fr.size, (90, 100, 150)))
    lit = ImageEnhance.Brightness(fr).enhance(1.05)
    return Image.composite(lit, ImageEnhance.Brightness(dark).enhance(0.35), m)
def hand(p, cam, tt):
    """a dark sleeve reaching into the showcase in the beam"""
    if not (TAKE - 0.6 <= tt < TAKE + 0.7): return
    u = kk(tt, TAKE - 0.6, TAKE) if tt < TAKE else 1 - kk(tt, TAKE + 0.1, TAKE + 0.7)
    z = cam[2]; tx, ty = W2S(cam, 1125, 580); sx, sy = W2S(cam, 1500, 760)
    hx, hy = lerp(sx, tx, u), lerp(sy, ty, u)
    p.line([(sx + 200 * z, sy + 120 * z), (hx, hy)], (40, 36, 44, 255), 26 * z)
    p.ell(hx, hy, 15 * z, 12 * z, (235, 200, 170, 255), INK, 2 * z)

def lobby_people(lay, cam, tt):
    k, lt = line_at(tt); ppl = []
    if tt >= ZDOWN[0]:
        u = ease(kk(tt, *ZDOWN)); zx, zy = lerp(1380, POS["zalata"][0], u), lerp(820, POS["zalata"][1], u)
        if tt < ZDOWN[1] + 0.3: ppl.append(("zalata", zx, zy, 1.6 * lerp(0.8, 1, u), "shock" if u > 0.8 else "neutral", -1, "down", tt * 8 if u < 1 else None))
        else: ppl.append(("zalata", *POS["zalata"], "sad", 1 if tt < LINE else 1, "hold", None))
    if tt >= TIN[0]:
        u = ease(kk(tt, *TIN)); x = lerp(760, POS["tota"][0], u); y = lerp(760, POS["tota"][1], u)
        ppl.append(("tota", x, y, 1.6 * lerp(0.75, 1, u), "flat", 1, "hold", tt * 8 if u < 1 else None))
    if tt >= BIN[0]:
        u = ease(kk(tt, *BIN)); ppl.append(("bondo2", lerp(760, POS["bondo2"][0], u), lerp(760, POS["bondo2"][1], u), 1.6 * lerp(0.75, 1, u), "sleepy", -1, "down", tt * 7 if u < 1 else None))
        u = ease(kk(tt, *SIN)); ppl.append(("shatta", lerp(1380, POS["shatta"][0], u), lerp(820, POS["shatta"][1], u), 1.6 * lerp(0.8, 1, u), "flat", -1, "down", tt * 8 if u < 1 else None))
    if tt >= AIN[0]:
        u = ease(kk(tt, *AIN)); ppl.append(("aziza", lerp(2050, POS["aziza"][0], u), POS["aziza"][1], 1.6, "smug", -1, "hips" if u >= 1 else "down", tt * 8 if u < 1 else None))
    ppl.sort(key=lambda a: a[3])
    for who, x, y, s, ex, look, arms, walk in ppl:
        talking = k is not None and WHO.get(k) == who
        e = expr_of(k, lt) if talking else ex
        mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
        a = ("talk" if talking and who != "aziza" else arms)
        if who == "tota" and k == "T2": a = "point"
        X, Y_ = W2S(cam, x, y); S = s * cam[2]
        draw_char(P(lay), who, X, Y_, S, e, mouth, look, ((tt + len(who) * 0.37) % 3.6) < 0.11, a, tt, "nbpen" if who == "tota" else None, 0.0, walk)

def scene(tt, sh, cam, size):
    Wd, Hd = size; x0, y0, z = cam; set_ = sh["set"]
    src = LOBBY if set_ in ("lobby", "clock") else ROOMN
    box = (x0, y0, x0 + Wd / z, y0 + Hd / z)
    img = src.resize((int(Wd * SS), int(Hd * SS)), Image.BICUBIC, box=box)
    if z > 2.2: img = img.filter(ImageFilter.GaussianBlur(min(1.6, (z - 2.2) * 0.8)))
    zz = z * SS; QW = lambda x, y: ((x - x0) * zz, (y - y0) * zz); d = ImageDraw.Draw(img, "RGBA")
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); p = P(lay)
    ENG.AZIZA_EARS[:] = [-1, 1] if tt < THEFT else [1]
    if set_ in ("lobby", "clock"):
        draw_clock(d, QW, zz, tt, not lights_on(tt)); draw_showcase(d, QW, zz, tt)
        ep = earring_pos(tt)
        if ep: e = QW(ep[0], ep[1]); earring(d, e[0], e[1], zz, ep[2])
        if set_ == "lobby":
            lobby_people(lay, cam, tt); hand(p, cam, tt)
    else:
        draw_tv(d, QW, zz, tt, lights_on(tt) or tt < TICK)
        if ROOMX <= tt < AIN[0]:                     # Aziza leaves HER room (TV on behind her), back to camera at the door
            u = ease(kk(tt, ROOMX + 0.1, ROOMX + 1.6)); x = lerp(1400, 300, u); X, Y_ = W2S(cam, x, 1010); S = 1.6 * z
            if u < 0.97: draw_char(P(lay), "aziza", X, Y_, S, "smug", 0.0, -1, False, "down", tt, None, 0.0, tt * 8)
    lay = tint_layer(lay, (225, 225, 255)); img.paste(lay, (0, 0), lay)
    fr = img.resize((Wd, Hd), Image.LANCZOS)
    if set_ == "room": fr = tv_glow(fr, cam, tt, Wd, Hd)
    if not lights_on(tt): fr = darkness(fr, cam, tt, beam=(set_ == "lobby"))
    if set_ == "lobby" and THEFT <= tt < THEFT + 4.4 and TAKE <= tt < TAKE + 0.6:      # the cup leaving with the hand (in the beam)
        d2 = ImageDraw.Draw(fr, "RGBA"); u = kk(tt, TAKE, TAKE + 0.6); c = W2S(cam, lerp(1122, 1400, u), lerp(578, 720, u)); trophy(d2, c[0], c[1], z)
    if set_ == "clock" and JUMP <= tt < JUMP + 2.0:
        lzt(fr, Wd / 2, Hd * (0.78 if Hd > Wd else 0.84), "بعد نص ساعة…", int(74 * popk(tt, JUMP + 0.15, 0.3)), (255, 230, 160))
    return fr

# ---------------- cards ----------------
def parrot(p, x, y, s, flap=0.0, open_=0.0):
    p.ell(x, y, 26 * s, 34 * s, (70, 180, 80, 255), INK, 2.5 * s)
    p.ell(x + 4 * s, y - 40 * s, 20 * s, 19 * s, (90, 200, 90, 255), INK, 2.5 * s)
    p.ell(x + 10 * s, y - 44 * s, 6 * s, 6 * s, (255, 255, 255, 255), INK, 1.5 * s); p.ell(x + 11 * s, y - 44 * s, 2.6 * s, 2.6 * s, INK, None)
    p.poly([(x + 20 * s, y - 42 * s), (x + 34 * s, y - 34 * s - open_ * 4 * s), (x + 22 * s, y - 30 * s)], (250, 190, 50, 255), INK, 1.5 * s)
    p.poly([(x - 18 * s, y - 14 * s), (x - 46 * s, y - 2 * s - 18 * s * flap), (x - 14 * s, y + 18 * s)], (50, 150, 70, 255), INK, 2 * s)
    p.poly([(x - 8 * s, y + 28 * s), (x - 24 * s, y + 70 * s), (x + 4 * s, y + 32 * s)], (220, 60, 50, 255), INK, 2 * s)
def prev_card(tt, Wd, Hd):
    """separate opening: «حل القضية السابقة» (parrot → Shatta)"""
    vert = Hd > Wd; fr = Image.new("RGB", (Wd, Hd), (14, 24, 18)); rays(fr, Wd, Hd, None, (22, 40, 28), tt, 1, 0.55)
    d = ImageDraw.Draw(fr, "RGBA"); by = Hd * (0.16 if vert else 0.13); bh = 120 if vert else 100
    d.rectangle([0, by - bh / 2, Wd, by + bh / 2], fill=(30, 120, 60, 255)); lzt(fr, Wd / 2, by, "حل القضية السابقة", 80 if vert else 70, (255, 255, 255), (10, 40, 20))
    lay = Image.new("RGBA", (int(Wd * SS), int(Hd * SS)), (0, 0, 0, 0)); p = P(lay)
    k, lt = line_at(tt); op = float(ENV["A0"][min(int(lt * FPS) + 2, len(ENV["A0"]) - 1)]) if k == "A0" else 0.0
    if vert:
        parrot(p, Wd * 0.28, Hd * 0.36, 3.4, abs(math.sin(tt * 6)) * 0.4, 0.3 * abs(math.sin(tt * 9)))
        draw_char(p, "shatta", Wd * 0.7, Hd * 0.66, 2.6, "scared" if tt > 2.5 else "neutral", 0.0, -1, ((tt + 0.5) % 3.2) < 0.1, "scared" if tt > 2.5 else "down", tt, None, 0.0, None)
        draw_char(p, "zalata", Wd * 0.3, Hd * 0.76, 2.2, expr_of(k, lt) if k else "smug", op, 1, False, "talk", tt, None, 0.0, None)
    else:
        parrot(p, Wd * 0.25, Hd * 0.5, 3.4, abs(math.sin(tt * 6)) * 0.4, 0.3 * abs(math.sin(tt * 9)))
        draw_char(p, "shatta", Wd * 0.5, Hd * 1.02, 3.0, "scared" if tt > 2.5 else "neutral", 0.0, -1, ((tt + 0.5) % 3.2) < 0.1, "scared" if tt > 2.5 else "down", tt, None, 0.0, None)
        draw_char(p, "zalata", Wd * 0.8, Hd * 1.0, 2.6, expr_of(k, lt) if k else "smug", op, -1, False, "talk", tt, None, 0.0, None)
    L = lay.resize((Wd, Hd), Image.LANCZOS); fr.paste(L, (0, 0), L)
    if tt >= 2.4:
        k2 = popk(tt, 2.4, 0.3); cx, cy = (Wd * 0.7, Hd * 0.25) if vert else (Wd * 0.5, Hd * 0.3); r = 50 * k2
        d = ImageDraw.Draw(fr, "RGBA"); d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(40, 170, 80, 255), outline=(255, 255, 255, 255), width=5)
        d.line([(cx - r * 0.45, cy), (cx - r * 0.1, cy + r * 0.38), (cx + r * 0.5, cy - r * 0.35)], fill=(255, 255, 255, 255), width=max(4, int(r * 0.22)))
    f = kk(tt, PREV_END - 0.35, PREV_END)
    if f > 0: fr = Image.blend(fr, Image.new("RGB", fr.size, (0, 0, 0)), f)
    return fr

def q_card(tt, sh, Wd, Hd, base):
    fr = ImageEnhance.Brightness(base).enhance(0.38).filter(ImageFilter.GaussianBlur(6)).convert("RGB")
    vert = Hd > Wd; cy = Hd * (0.32 if vert else 0.3); g = 1.25 if vert else 1.0
    lzt(fr, Wd / 2, cy, "مين سرق الكاس؟", int(110 * g * popk(tt, sh["start"] + 0.05, 0.3)), (255, 214, 90))
    for i, (who, col) in enumerate(NUMS):
        bx = Wd / 2 + (i - 1) * 220 * g; badge(fr, bx, cy + 230 * g, str(i + 1), 1.3 * g * popk(tt, sh["start"] + 0.3 + i * 0.15), col)
        lzt(fr, bx, cy + 330 * g, NAME[who][0], int(54 * g * popk(tt, sh["start"] + 0.3 + i * 0.15)), (255, 255, 255))
    return fr

# ---------------- frames ----------------
_FREEZE = {}
def tag(fr, Wd, Hd, tt):
    if tt < PREV_END + 3.0 or tt >= Q: return
    d = ImageDraw.Draw(fr, "RGBA"); vert = Hd > Wd; x, y = (Wd / 2, 200) if vert else (Wd - 150, 60)
    d.rounded_rectangle([x - 115, y - 32, x + 115, y + 32], 26, fill=(200, 30, 40, 220)); lzt(fr, x, y, "قضية 10", 44, (255, 255, 255), stroke=False)
def add_overlays(fr, tt, sh, Wd, Hd, cam):
    if sh["set"] != "lobby" or tt < BADGES: return
    k, _ = line_at(tt)
    for i, (who, col) in enumerate(NUMS):
        x, y, s = POS[who]; S_, _, (_, hy2) = body(who, x, y, s); q = W2S(cam, x, hy2 - 46 * S_ - 40)
        if -120 < q[0] < Wd + 120:
            badge(fr, q[0], max(q[1], 110 if Hd < Wd else 330), str(i + 1), min(1.1, cam[2] * 0.5) * popk(tt, BADGES + i * 0.15), col)
def cam_for(sh, tt, vert):
    return vcam(sh, tt) if vert else hcam(sh, tt)
def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "prev": return finish(prev_card(tt, W, H), tt)
    if sh["set"] == "q":
        if "h" not in _FREEZE: ps = shots[shots.index(sh) - 1]; _FREEZE["h"] = scene(sh["start"] - 0.05, ps, hcam(ps, sh["start"] - 0.05), (W, H))
        return finish(q_card(tt, sh, W, H, _FREEZE["h"]), tt)
    cam = hcam(sh, tt); fr = scene(tt, sh, cam, (W, H)); add_overlays(fr, tt, sh, W, H, cam); tag(fr, W, H, tt)
    return finish(fr, tt)
def subtitle(img, tt):
    if shot_at(tt)["set"] != "q": sub_chunk(img, tt, W / 2, H - 80, 62)
VIGV = VIG.resize((1080, 1920))
def vertical(_base, tt):
    sh = shot_at(tt); Wd, Hd = 1080, 1920
    if sh["set"] == "prev": fr = prev_card(tt, Wd, Hd); sub_chunk(fr, tt, 520, 1560, 72); return fr
    if sh["set"] == "q":
        if "v" not in _FREEZE: ps = shots[shots.index(sh) - 1]; _FREEZE["v"] = scene(sh["start"] - 0.05, ps, vcam(ps, sh["start"] - 0.05), (Wd, Hd))
        return q_card(tt, sh, Wd, Hd, _FREEZE["v"])
    cam = vcam(sh, tt); fr = scene(tt, sh, cam, (Wd, Hd)); add_overlays(fr, tt, sh, Wd, Hd, cam)
    fr = ImageChops.multiply(fr, VIGV)
    u = tt - sh["start"]
    if sh.get("tin") in ("whip", "whipl") and u < 0.18: fr = fr.filter(ImageFilter.BoxBlur(int(2 + 18 * (1 - u / 0.18))))
    tag(fr, Wd, Hd, tt); sub_chunk(fr, tt, 500, 1470, 76)
    return fr

# ---------------- audio ----------------
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 3; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(10)
    for k_, f in enumerate((523, 659, 784)): mix_into(buf, tone(f, 0.5, 0.16, 7), 0.1 + k_ * 0.08, 1.0)
    mix_into(buf, tone(1047, 0.6, 0.14, 6), 2.4, 1.0)
    dr = np.arange(int((Q - PREV_END) * SR)) / SR
    drone = (np.sin(2 * np.pi * 55 * dr) * 0.045 + np.sin(2 * np.pi * 82.5 * dr) * 0.025) * (0.7 + 0.3 * np.sin(dr * 0.8))
    mix_into(buf, drone.astype(np.float32), PREV_END, 1.0)
    for j in range(int((Q - PREV_END) / 1.0)):                                   # wall clock tick-tock
        if not (TICK <= PREV_END + j < LIGHTS): mix_into(buf, tone(2300, 0.03, 0.05, 80), PREV_END + 0.5 + j, 1.0)
    # TV series murmur from Aziza's room (only heard in her room shots, cut at 9:00)
    def tv_bed(a, b, g):
        if b <= a: return
        nn = int((b - a) * SR); x = lowpass(r.normal(0, 1, nn).astype(np.float32), 900) * 0.04
        tt_ = np.arange(nn) / SR; x += (np.sin(2 * np.pi * 220 * tt_) * 0.03 * (0.5 + 0.5 * np.sin(tt_ * 3))).astype(np.float32)
        mix_into(buf, x * g, a, 1.0)
    tv_bed(H2, H3, 1.0); tv_bed(H4, TICK, 1.0); tv_bed(H7, H7 + 0.8, 0.9); tv_bed(ROOMX, ROOMX + 1.8, 0.8)
    mix_into(buf, tone(1500, 0.06, 0.35, 40), TICK - 0.02, 1.0)                    # «طق»
    mix_into(buf, SFXF["switch"] * 0.6, TICK, 1.0); mix_into(buf, tone(90, 0.8, 0.25, 4), TICK + 0.02, 1.0)
    mix_into(buf, SFXF["stinger"] * 0.35, THEFT + 0.2, 1.0)
    for j in range(5): mix_into(buf, tone(300 + 30 * j, 0.06, 0.08, 30), TAKE - 0.6 + j * 0.1, 1.0)   # glass door creak
    mix_into(buf, tone(2600, 0.25, 0.28, 18) + tone(3900, 0.25, 0.12, 22), LAND, 1.0)            # «تِنّ»
    for j in range(4): mix_into(buf, tone(2400 - j * 200, 0.08, 0.08, 40), LAND + 0.15 + j * 0.18, 1.0)
    for j in range(10): mix_into(buf, tone(1800 + j * 60, 0.04, 0.06, 60), JUMP + 0.2 + j * 0.13, 1.0)  # clock spinning
    mix_into(buf, SFXF["switch"] * 0.6, LIGHTS, 1.0)
    for j in range(5): mix_into(buf, tone(110, 0.06, 0.1, 35), ZDOWN[0] + j * 0.35, 1.0)
    mix_into(buf, SFXF["gasp"] * 0.3, ZDOWN[1] - 0.2, 1.0)
    for i in range(3): mix_into(buf, tone(660 + i * 220, 0.18, 0.18, 12), BADGES + i * 0.15, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), Q + k_ * 0.09, 1.0)
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > PREV_END: mix_into(buf, SFXF["whoosh"] * 0.18, s_["start"] - 0.1, 1.0)
    for st_, k in lines:
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8; mix_into(buf, v, st_, 1.0)
    write_wav(buf[:int(TOTAL * SR)], path)

def make_covers():
    def comp(Wd, Hd, vert):
        bgc = ImageEnhance.Brightness(LOBBY.crop((700, 150, 1700, 950)).resize((Wd, Hd), Image.LANCZOS).filter(ImageFilter.GaussianBlur(7))).enhance(0.8)
        img = bgc.resize((int(Wd * SS), int(Hd * SS))); d = ImageDraw.Draw(img, "RGBA")
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); p = P(lay)
        ENG.AZIZA_EARS[:] = [-1, 1]
        if vert:
            tx, ty, tz = Wd * 0.72 * SS, Hd * 0.36 * SS, 5.0 * SS; trophy(d, tx, ty, tz)
            draw_char(p, "zalata", Wd * 0.34, Hd * 0.82, 4.6, "shock", 0.6, 1, False, "up", 0.0, None, 0.0, None)
            for i, (who, col) in enumerate(NUMS): draw_char(p, who, Wd * (0.2 + 0.3 * i), Hd * 1.08, 2.3, "flat", 0.0, -1, False, "down", 0.0, None, 0.0, None)
        else:
            tx, ty, tz = Wd * 0.78 * SS, Hd * 0.55 * SS, 5.5 * SS; trophy(d, tx, ty, tz)
            draw_char(p, "zalata", Wd * 0.3, Hd * 1.3, 5.4, "shock", 0.6, 1, False, "up", 0.0, None, 0.0, None)
        img.paste(lay, (0, 0), lay); fr = img.resize((Wd, Hd), Image.LANCZOS); d = ImageDraw.Draw(fr, "RGBA")
        if vert:
            d.rectangle([0, Hd * 0.535, Wd, Hd * 0.725], fill=(10, 6, 4, 150))
            lzt(fr, Wd / 2, Hd * 0.575, "مين سرق", 160, (255, 255, 255)); lzt(fr, Wd / 2, Hd * 0.67, "الكاس؟", 180, (255, 214, 60))
            for i, (who, col) in enumerate(NUMS): badge(fr, Wd * (0.2 + 0.3 * i), Hd * 0.765, str(i + 1), 1.2, col)
            bx, by = Wd / 2, 130
        else:
            d.rectangle([0, Hd * 0.76, Wd, Hd * 0.97], fill=(10, 6, 4, 150)); lzt(fr, Wd * 0.58, Hd * 0.865, "مين سرق الكاس؟", 150, (255, 214, 60)); bx, by = 1620, 90
        d = ImageDraw.Draw(fr, "RGBA"); d.rounded_rectangle([bx - 200, by - 46, bx + 200, by + 46], 34, fill=(200, 30, 40, 240))
        lzt(fr, bx, by, "مين الكداب؟ • قضية 10", 42, (255, 255, 255), stroke=False)
        return fr
    comp(1080, 1920, True).save(ROOT + "/publish/thumbs/kaddab_e10_cover.jpg", quality=92)
    comp(1920, 1080, False).resize((1280, 720), Image.LANCZOS).save(ROOT + "/publish/thumbs/kaddab_e10_yt.jpg", quality=92)

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
