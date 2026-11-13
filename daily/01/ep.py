# «يوميات شطة وزلطة» 01 — التلاجة  (H 1920x1080 + V 1080x1920 in one pass)
# render:  python ep.py audio  →  python ep.py part 0 2 & python ep.py part 1 2  →  concat  →  mux mix.wav
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())          # engine + shared helpers
from PIL import ImageFont
os.chdir(ROOT + "/daily/01")
SERIES = "يوميات شطة وزلطة"; EPT = "التلاجة"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"
SFXP = {"steps": "/s2e1/sfx/footsteps.mp3", "slam": "/s2e1/sfx/slam.mp3", "whoosh": "/trend/01/sfx/whoosh.mp3",
        "stinger": "/trend/01/sfx/stinger.mp3", "switch": "/trend/01/sfx/switch.mp3"}
SFXF = {n: load_audio(ROOT + p) for n, p in SFXP.items()}

SUB = {"SPANT": "", "ZPANT": "",
       "B01": "ليكم عندي خبرين يا ولاد... واحد حلو، وواحد وحش.",
       "S01": "إيه الخبر الحلو يا عم بندق؟",
       "B02": "إحنا في الدور العاشر... وفاضل دور واحد بس!",
       "Z01": "طب إيه الخبر الوحش بأه يا عم بندق؟",
       "B03": "دي مش العمارة بتاعتنا.", "BLAUGH": ""}
WHO = {"SPANT": "shatta", "ZPANT": "zalata", "B01": "bondo2", "S01": "shatta", "B02": "bondo2", "Z01": "zalata", "B03": "bondo2", "BLAUGH": "bondo2"}
EXPR = {"SPANT": "sad", "ZPANT": "sad", "B01": "happy", "S01": "sad", "B02": "happy", "Z01": "happy", "B03": "flat", "BLAUGH": "laugh"}
ARMS = {}
load_lines(list(SUB))

STAIRS = _ld(ROOT + "/daily/bg/stairs_jeeran.png")       # canonical «سلم عمارة الجيران» (docs/locations.md)
SLOPE = 0.483
def Y(x):   # top surface of the flight (feet line); bottom floor left, landing right
    return 1000 if x < 190 else (444 if x > 1300 else 980 - SLOPE * (x - 190))
ANG = math.atan(SLOPE)

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear()
t = 0.0
say(0.15, "SPANT"); say(0.75, "ZPANT")
CLIMB = (0.0, 4.6)                         # the two inch up 2 steps with the fridge
STEPS = 3.3                                # footsteps from below (motivated entrance)
shot("st", 0.0, 2.3, (880, 600, 1.85), (930, 575, 1.95))                         # hook: tight on the struggle
shot("st", 2.3, 4.6, (760, 640, 1.45), (800, 625, 1.5), tin="whip")               # wider: the endless stairs
ENTER = (4.6, 7.3)                          # Bandaq walks up from bottom-left, hem in his teeth
shot("st", 4.6, 7.6, (700, 700, 1.12), (740, 690, 1.18), tin="whipl")
HEM_OFF = 7.45                              # lets the hem drop to talk
t = say(7.75, "B01") + 0.2
shot("st", 7.6, t, (760, 690, 1.25), (770, 685, 1.32))
s = t; t = say(t + 0.1, "S01") + 0.15
shot("st", s, t, (790, 680, 1.3), (790, 680, 1.36))
s = t; t = say(t + 0.1, "B02") + 0.1; GOOD = t - 0.75
shot("st", s, t, (740, 700, 1.3), (740, 700, 1.4))
JOY = (t, t + 1.5); shot("st", t, JOY[1], (890, 560, 1.75), (890, 560, 1.85), tin="whip"); t = JOY[1]   # they light up
s = t; t = say(t + 0.1, "Z01") + 0.15
shot("st", s, t, (770, 690, 1.28), (770, 690, 1.33), tin="whipl")
s = t; t = say(t + 0.25, "B03") + 0.35; BAD = s + 0.25
shot("st", s, t, (720, 720, 1.3), (640, 760, 1.55), ease="crash")
LOOK = (t, t + 2.0); shot("st", t, LOOK[1], (960, 545, 1.85), (960, 545, 1.95)); t = LOOK[1]           # silent look at each other
DROP = t + 0.35; t = DROP + 1.6
shot("st", LOOK[1], t, (760, 690, 1.15), (760, 690, 1.15), tin="whipl")                               # they drop the fridge
LAUGH = t; t = say(t + 0.1, "BLAUGH")
FREEZE = t - 0.2
shot("st", LAUGH, t + 0.05, (440, 690, 2.1), (440, 700, 2.35), tin="whip")
shot("end", t + 0.05, t + 2.6, None); t += 2.6
TOTAL = t

# ---------------- staging ----------------
SC = 1.25
def carriers(tt):
    k = ease(kk(tt, *CLIMB)); dx = 110 * k - 110
    return 1060 + dx, 720 + dx           # shatta (upper), zalata (lower)
def bandaq_x(tt):
    return lerp(-120, 430, ease(kk(tt, *ENTER)))
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, walk=None, hop=0.0):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11 and expr not in ("sleepy", "laugh")
    X, Y_, S = W2S(cam, x, y - jump_off(who, tt) - hop) + (s * cam[2],)
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, None, lean, walk)
    return X, Y_, S * CH[who]["scale"]

def fridge(p, cam, a, b, wob, drop_k):
    """fridge lying along the stairs between points a (lower end) and b (upper end), thickness th"""
    (ax, ay), (bx, by) = a, b
    if drop_k > 0:   # dropped: slides 2 steps down and lands on the treads
        sl = 85 * ease(drop_k); fall = 70 * min(1, drop_k * 3)
        ax -= sl; bx -= sl; ay += sl * SLOPE + fall; by += sl * SLOPE + fall
    cx, cy = (ax + bx) / 2, (ay + by) / 2; L = math.hypot(bx - ax, by - ay); th = 118
    ang = math.atan2(by - ay, bx - ax) + wob
    ux, uy = math.cos(ang), math.sin(ang); nx, ny = -uy, ux
    def Q(u, v): return W2S(cam, cx + ux * u + nx * v, cy + uy * u + ny * v)
    z = cam[2]
    p.poly([Q(-L / 2, -th / 2), Q(L / 2, -th / 2), Q(L / 2, th / 2), Q(-L / 2, th / 2)], (236, 238, 240, 255), INK, 3.5 * z)
    p.poly([Q(-L / 2, th / 2 - 22), Q(L / 2, th / 2 - 22), Q(L / 2, th / 2), Q(-L / 2, th / 2)], (205, 210, 216, 255), INK, 2.5 * z)   # side shade
    p.line([Q(L / 2 - L * 0.36, -th / 2), Q(L / 2 - L * 0.36, th / 2 - 22)], INK, 3 * z)                                               # freezer split
    for u0 in (L / 2 - L * 0.36 - 26, L / 2 - 30):
        p.line([Q(u0 - 40, -th / 2 + 26), Q(u0, -th / 2 + 26)], (150, 155, 162, 255), 7 * z)                                         # handles
    p.line([Q(-L / 2 + 20, -th / 2 + 16), Q(-L / 2 + 90, -th / 2 + 16)], (255, 255, 255, 200), 5 * z)                                 # shine
    for u0 in (-L / 2 + 30, L / 2 - 30): p.ell(*Q(u0, th / 2 + 6), 7 * z, 5 * z, (60, 60, 64, 255), None)                           # feet

STAR = [(0.0,), (2.1,), (4.2,)]
def dizzy(p, X, Y_, S, tt, ph=0.0):
    hy = Y_ - 250 * S
    for i in range(3):
        a = tt * 4 + ph + i * 2.09; sx, sy = X + math.cos(a) * 46 * S, hy + math.sin(a) * 12 * S; r = 11 * S
        p.poly([(sx, sy - r), (sx + r * 0.3, sy - r * 0.3), (sx + r, sy), (sx + r * 0.3, sy + r * 0.3), (sx, sy + r), (sx - r * 0.3, sy + r * 0.3), (sx - r, sy), (sx - r * 0.3, sy - r * 0.3)], (250, 220, 70, 255), INK, 1.5 * S)
def sweat(p, X, Y_, S, tt, ph=0.0):
    for i in range(2):
        u = ((tt * 0.9 + ph + i * 0.5) % 1); sx = X + (40 + i * 18) * S * (1 if i else -1); sy = Y_ - (230 - 60 * u) * S
        p.poly([(sx, sy - 9 * S), (sx + 5 * S, sy), (sx, sy + 5 * S), (sx - 5 * S, sy)], (140, 200, 255, int(255 * (1 - u))), INK, 1.2 * S)

def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255):
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(LZ, size)
    kw = dict(font=f, anchor="mm", direction="rtl", language="ar")
    d.text((x, y), s, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), **kw)
    d.text((x, y), s, fill=fill + (alpha,), **kw)
    img.paste(lay, (0, 0), lay)
def popk(tt, t0, d=0.22):
    u = kk(tt, t0, t0 + d); return 0 if u <= 0 else (1 + 0.25 * math.sin(u * math.pi)) if u < 1 else 1

def plaque(img_lay, cam):
    """floor plaque on the wall — this building's own plaque (part of the canonical location)"""
    z = cam[2]; x, y = W2S(cam, 560, 410)
    p = P(img_lay); p.rect(x - 70 * z, y - 40 * z, x + 70 * z, y + 40 * z, (40, 60, 90, 255), (220, 220, 225, 255), 4 * z, 10 * z)
    text(img_lay, x * SS, (y - 2 * z) * SS, "الدور 10", int(36 * z * SS), (255, 255, 255), sw=0)

def series_tag(fr, tt, t0, t1):
    k = min(ease(kk(tt, t0, t0 + 0.35)), 1 - ease(kk(tt, t1 - 0.35, t1)))
    if k <= 0: return
    d = ImageDraw.Draw(fr, "RGBA"); x = -620 + 680 * k
    d.rounded_rectangle([x, 60, x + 620, 170], 26, fill=(230, 120, 30, 235), outline=(255, 255, 255, 255), width=4)
    lzt(fr, x + 310, 108, "يوميات شطة وزلطة", 60, (255, 255, 255))

_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/daily/01")
_FC = {}
def frame_cache(t_):
    if t_ not in _FC: _FC[t_] = frame(t_)
    return _FC[t_]
def endcard(tt, sh):
    k = kk(tt, sh["start"], sh["start"] + 0.4)
    fr = ImageEnhance.Brightness(frame_cache(FREEZE)).enhance(1 - 0.55 * k).filter(ImageFilter.GaussianBlur(6 * k)).convert("RGBA")
    sc = popk(tt, sh["start"] + 0.1, 0.3)
    if sc > 0:
        lzt(fr, W / 2, 420, "يوميات شطة وزلطة", int(140 * sc), (255, 214, 90))
        d = ImageDraw.Draw(fr, "RGBA"); d.rounded_rectangle([W / 2 - 400, 520, W / 2 + 400, 600], 30, fill=(230, 120, 30, 230))
        lzt(fr, W / 2, 558, "موقف جديد كل يوم!", 54, (255, 255, 255))
    if tt >= sh["start"] + 0.6:
        logo(fr, W / 2, 760, 120); text(fr, W / 2, 900, "@shattawzalata", 50, (255, 214, 90))
    return fr.convert("RGB")

# ---------------- frame ----------------
def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "end": return finish(endcard(tt, sh), tt)
    cam = cam_at(sh, tt); z = cam[2]
    img = bg_crop(STAIRS, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    xs, xz = carriers(tt)
    carrying = tt < DROP
    climbing = CLIMB[0] <= tt < CLIMB[1]
    # expressions / looks
    se = ze = "sad"; sl = zl = 1
    if tt >= HEM_OFF - 1.2: sl = zl = -1                       # turn to the newcomer
    if GOOD <= tt < BAD: se = ze = "happy"
    if tt >= BAD: se = ze = "flat"
    if LOOK[0] <= tt < LOOK[1] + 0.3: sl, zl = -1, 1            # look at each other
    if LOOK[0] + 0.7 <= tt: se = ze = "angry"
    if tt >= DROP + 0.4: se = ze = "flat"
    hop = abs(math.sin((tt - JOY[0]) * 9)) * 16 if JOY[0] <= tt < JOY[1] else 0
    wob = math.sin(tt * 7) * 0.02 if carrying else 0
    walk = tt * 5 if climbing else None
    # Bandaq (lower on the stairs) — hem of the galabeya in his teeth while climbing
    bx = bandaq_x(tt); CH["bondo2"]["hem"] = tt < HEM_OFF
    bwalk = tt * 6.5 if ENTER[0] <= tt < ENTER[1] else None
    be = "happy"
    if tt >= BAD: be = "smug"
    if DROP <= tt < DROP + 0.5: be = "shock"
    if tt >= HEM_OFF + 0.4 or ENTER[0] <= tt: pass
    BX, BY, BS = person(lay, cam, "bondo2", bx, Y(bx), SC, tt, be, 1, "down", 0.0, bwalk)
    # carriers + fridge
    arms = "hold" if carrying else "down"
    ZX, ZY, ZS = person(lay, cam, "zalata", xz, Y(xz), SC, tt, ze, zl, arms, 0.15 if carrying else 0, walk, hop)
    SX, SY, SS_ = person(lay, cam, "shatta", xs, Y(xs), SC, tt, se, sl, "down" if not carrying else "hold", -0.15 if carrying else 0, walk, hop)
    a = (xz + 48, Y(xz) - 92 * SC); b = (xs - 48, Y(xs) - 92 * SC)
    fridge(p, cam, a, b, wob, kk(tt, DROP, DROP + 0.45))
    if carrying and tt < GOOD:
        dizzy(p, ZX, ZY, ZS, tt); dizzy(p, SX, SY, SS_, tt, 1.3)
        sweat(p, ZX, ZY, ZS, tt); sweat(p, SX, SY, SS_, tt, 0.4)
    if LOOK[0] + 0.7 <= tt < DROP + 0.4:      # steam of anger
        for X_, Y__, S_ in ((ZX, ZY, ZS), (SX, SY, SS_)):
            for i in range(2):
                u = (tt * 1.4 + i * 0.5) % 1
                p.ell(X_ + (i * 2 - 1) * 40 * S_, Y__ - (270 + 50 * u) * S_, (8 + 14 * u) * S_, (6 + 10 * u) * S_, (255, 255, 255, int(200 * (1 - u))), None)
    if DROP <= tt < DROP + 0.8:               # dust puff where it lands
        u = kk(tt, DROP + 0.12, DROP + 0.8)
        for i in range(6):
            dx_ = (i - 2.5) * 60; px, py = W2S(cam, (xz + xs) / 2 - 85 + dx_, Y((xz + xs) / 2 - 85 + dx_) - 10)
            r = (10 + 40 * u) * z; p.ell(px, py, r, r * 0.6, (220, 210, 190, int(200 * (1 - u))), None)
    lay = tint_layer(lay, (255, 236, 210)); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    if sh["set"] == "st":
        px_, py_ = W2S(cam, 560, 410); pz = cam[2]                       # floor plaque on the wall (part of the location)
        if -200 < px_ < W + 200 and -100 < py_ < H + 100:
            d_ = ImageDraw.Draw(fr, "RGBA"); d_.rounded_rectangle([px_ - 78 * pz, py_ - 38 * pz, px_ + 78 * pz, py_ + 38 * pz], int(10 * pz), fill=(40, 60, 90, 255), outline=(225, 225, 230, 255), width=max(2, int(4 * pz)))
            lzt(fr, px_, py_ - 2 * pz, "الدور 10", int(40 * pz), (255, 255, 255), outer=(40, 60, 90))
        series_tag(fr, tt, 0.6, 4.2)
        if JOY[0] <= tt < JOY[1]:
            for i, (dx, dy) in enumerate(((-260, -330), (230, -380), (0, -460))):
                if tt >= JOY[0] + i * 0.15: lzt(fr, W / 2 + dx, H / 2 + dy + 120, ("الحمد لله!", "دور واحد!", "يـــاااه!")[i], int(60 * popk(tt, JOY[0] + i * 0.15)), (255, 214, 90))
        if LAUGH + 0.3 <= tt:
            for i, (dx, dy, sz) in enumerate(((-380, -260, 110), (300, -320, 92), (-320, 120, 84), (360, 60, 100))):
                t0_ = LAUGH + 0.3 + i * 0.45
                if tt >= t0_: lzt(fr, W / 2 + dx + math.sin(tt * 6 + i) * 8, H / 2 + dy, "ههههه", int(sz * popk(tt, t0_)), (255, 214, 90))
        if tt >= FREEZE:
            fr = Image.blend(fr, Image.new("RGB", fr.size, (255, 255, 255)), 0.6 * (1 - kk(tt, FREEZE, FREEZE + 0.2)))
    return finish(fr, tt)

def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(31)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 300) * 0.025, 0, 1.0)            # stairwell room tone
    # fridge strain: creaks + bumps on each step during the climb
    d = np.arange(int(SR * 0.12)) / SR; bump = (np.sin(2 * np.pi * 110 * d) * np.exp(-d * 30) + r.normal(0, 1, len(d)) * np.exp(-d * 60) * 0.3) * 0.5
    for bt in (0.6, 1.9, 3.2, 4.3): mix_into(buf, bump.astype(np.float32), bt, 1.0)
    mix_into(buf, SFXF["steps"][: int(SR * 4.5)] * 0.9, STEPS, 1.0)
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 0.5: mix_into(buf, SFXF["whoosh"] * 0.3, s_["start"] - 0.1, 1.0)
    mix_into(buf, SFXF["switch"] * 0.6, 0.6, 1.0)
    for i, f in enumerate((523, 659, 784, 1047)):                                                     # joy sparkle
        d = np.arange(int(SR * 0.5)) / SR; mix_into(buf, (np.sin(2 * np.pi * f * d) * np.exp(-d * 6) * 0.12).astype(np.float32), JOY[0] + i * 0.06, 1.0)
    mix_into(buf, SFXF["stinger"] * 0.5, BAD + DUR["B03"] - 0.1, 1.0)
    # the silent look: a low tense hum
    d = np.arange(int(SR * (LOOK[1] - LOOK[0]))) / SR; hum = (np.sin(2 * np.pi * 55 * d) * 0.12 * np.minimum(1, d * 2)).astype(np.float32)
    mix_into(buf, hum, LOOK[0], 1.0)
    mix_into(buf, SFXF["slam"] * 0.9, DROP + 0.12, 1.0)                                              # fridge thud
    sc = (lowpass(r.normal(0, 1, int(SR * 0.4)).astype(np.float32), 900) * np.linspace(0.5, 0, int(SR * 0.4))).astype(np.float32)
    mix_into(buf, sc, DROP + 0.15, 1.0)                                                               # slide/scrape
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
