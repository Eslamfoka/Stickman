# «يوميات شطة وزلطة» — بص على رجلي  (H 1920x1080 + V 1080x1920 in one pass)
# render:  python ep.py audio  →  python ep.py part 0 2 & python ep.py part 1 2  →  concat  →  mux mix.wav
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/daily/02")
SERIES = "يوميات شطة وزلطة"; EPT = "بص على رجلي"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"
SFXP = {"whoosh": "/trend/01/sfx/whoosh.mp3", "switch": "/trend/01/sfx/switch.mp3", "slam": "/s2e1/sfx/slam.mp3",
        "giggle": "/daily/02/sfx/giggle.mp3", "crinkle": "/s2e1/sfx/crinkle.mp3"}
SFXF = {n: load_audio(ROOT + p) for n, p in SFXP.items()}

SUB = {"F01": "النهارده امتحان شفوي!", "F02": "زلطة! قوم. الحيوان ده إيه... من رجليه بس؟", "Z01": "حمار؟", "F03": "غلط!",
       "Z02": "معزة؟", "F04": "غلط!!", "F05": "إنت اسمك إيه يا ولد؟!", "Z03": "بص على رجلي... واعرف اسمي.", "GROUP": ""}
WHO = {"F01": "fahmy", "F02": "fahmy", "Z01": "zalata", "F03": "fahmy", "Z02": "zalata", "F04": "fahmy", "F05": "fahmy", "Z03": "zalata", "GROUP": "shatta"}
EXPR = {"F01": "smug", "F02": [(0, "angry"), (0.35, "smug")], "Z01": "neutral", "F03": "angry", "Z02": "happy", "F04": "shout", "F05": "angry",
        "Z03": "flat", "GROUP": "laugh"}
ARMS = {}
load_lines(list(SUB))
CLASS = _ld(ROOT + "/daily/bg/classroom.png")      # canonical «فصل المدرسة» (docs/locations.md)

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear()
TAPS = (0.25, 0.55, 0.85)
shot("st", 0.0, 1.0, (300, 290, 2.3), (300, 290, 2.4))                                    # hook: CU the mystery legs, stick taps
t = say(1.0, "F01") + 0.1
shot("st", 1.0, t, (330, 300, 1.9), (420, 330, 1.75), tin="zoom")
GROAN = (t, t + 1.1); shot("st", t, GROAN[1], (1000, 560, 1.0), (1010, 560, 1.04), tin="whip"); t = GROAN[1]   # the crowded class groans
s = t; t = say(t + 0.1, "F02") + 0.15; STAND = s + 0.95
shot("st", s, t, (900, 650, 1.55), (900, 650, 1.62), tin="whipl")
s = t; t = say(t + 0.1, "Z01") + 0.05; GIG = t
shot("st", s, t, (880, 660, 1.75), (880, 660, 1.8))
t += 1.0; shot("st", GIG, t, (1300, 560, 1.3), (1300, 560, 1.34), tin="whip")             # class snickers, Fahmy's eye twitches
s = t; t = say(t + 0.05, "F03") + 0.15
shot("st", s, t, (880, 660, 1.8), (880, 660, 1.86), tin="whipl")
s = t; t = say(t + 0.1, "Z02") + 0.1
shot("st", s, t, (890, 660, 1.75), (890, 660, 1.75))
SNORT = t; t += 1.1; shot("st", SNORT, t, (1450, 560, 1.7), (1450, 560, 1.75), tin="whip")   # Abdo snorts, Tota hides behind her notebook
WALK = (SNORT, t)                                                                          # meanwhile Fahmy marches to the desk
s = t; t = say(t + 0.1, "F04") + 0.35; SLAM = s + 0.15
shot("st", s, t, (980, 640, 1.35), (960, 650, 1.75), ease="crash", tin="whipl")
s = t; t = say(t + 0.1, "F05") + 0.25
shot("st", s, t, (880, 660, 1.75), (860, 650, 1.95))
LEG = (t, t + 0.9); shot("st", t, LEG[1], (900, 670, 1.7), (900, 670, 1.7)); t = LEG[1]  # Zalata calmly puts his foot up
s = t; t = say(t + 0.05, "Z03") + 0.2; PUNCH = s
shot("st", s, t, (900, 660, 1.7), (930, 650, 1.95))
BEAT = (t, t + 1.1); shot("st", t, BEAT[1], (800, 560, 2.4), (800, 560, 2.5), tin="whip"); t = BEAT[1]   # Fahmy blinks… chalk drops
LAUGH = t; t = say(t, "GROUP") + 0.2
FREEZE = t - 0.25
shot("st", LAUGH, t, (1240, 610, 1.32), (1240, 610, 1.4), tin="whipl")
shot("end", t, t + 2.6, None); t += 2.6
TOTAL = t

# ---------------- cast / staging (world = 1920x1080 classroom) ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
for i, sh_ in enumerate(((70, 120, 200), (230, 200, 60), (60, 160, 160), (200, 70, 70), (130, 90, 170), (240, 140, 60))):
    CH[f"kid{i}"] = dict(shirt=sh_, hair=((40, 30, 24), (90, 50, 30), (20, 20, 22), (120, 70, 40), (30, 26, 24), (70, 40, 26))[i], scale=0.95)
ROWS = [  # (desk x0, x1, desk top y, panel bottom y, scale, [(who, x, feet_y)])  — back to front
    (1290, 1910, 548, 598, 0.62, [("kid0", 1390, 585), ("kid1", 1560, 585), ("kid2", 1740, 585), ("kid3", 1860, 585)]),
    (1170, 1830, 625, 690, 0.82, [("tota", 1290, 674), ("kid4", 1460, 674), ("abdo", 1650, 674), ("kid5", 1790, 674)]),
    (1060, 1640, 735, 820, 1.05, [("zalata", 1150, 798), ("shatta", 1440, 798)]),
]
FX0, FX1 = 700, 800                    # Fahmy: by the board → at the front desk
def fahmy_x(tt): return lerp(FX0, FX1, ease(kk(tt, *WALK)))
def zal_pos(tt):                       # sits at desk → stands & steps into the aisle (x 975)
    k = ease(kk(tt, STAND, STAND + 0.6)); return lerp(1150, 990, k), lerp(798, 905, k), k

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, walk=None, hop=0.0, held=None, eat=None, mouth_k=0.0):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking and k != "GROUP": expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    mouth = max(mouth, mouth_k)
    blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11 and expr not in ("sleepy", "laugh")
    X, Y_ = W2S(cam, x, y - jump_off(who, tt) - hop); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, held, lean, walk, eat)
    if who.startswith("kid"):          # generic students get a simple hair cap
        sc = S * CH[who]["scale"]; hx, hy = X, Y_ - 190 * sc
        P(lay).d.chord([P(lay).S(hx - 47 * sc), P(lay).S(hy - 50 * sc), P(lay).S(hx + 47 * sc), P(lay).S(hy + 30 * sc)], 180, 360,
                       fill=C(CH[who]["hair"]), outline=INK, width=P(lay).S(2.5 * sc))
    return X, Y_, S * CH[who]["scale"]

WOOD = (150, 98, 52, 255); WOOD_D = (112, 70, 36, 255)
def desk(p, cam, x0, x1, top, bot, s):
    z = cam[2]; a, b = W2S(cam, x0, top), W2S(cam, x1, bot)
    p.rect(a[0], a[1] - 14 * s * z, b[0], a[1] + 4 * z, (176, 120, 66, 255), INK, 3 * z, 4 * z)       # desk top
    p.rect(a[0] + 8 * z, a[1] + 4 * z, b[0] - 8 * z, b[1], WOOD, INK, 3 * z, 2 * z)                    # front panel
    for xx in range(int(x0) + 160, int(x1) - 40, 290):
        q = W2S(cam, xx, top); p.line([(q[0], a[1] + 10 * z), (q[0], b[1] - 6 * z)], WOOD_D, 3 * z)      # seat dividers
    for xx in (x0 + 20, x1 - 20):
        q = W2S(cam, xx, bot); p.line([q, (q[0], q[1] + 40 * s * z)], (60, 60, 64, 255), 6 * z)        # iron legs

def legs_drawing(p, cam, tt):
    """chalk drawing on the board: two hairy animal legs with hooves (nobody can tell what animal)"""
    z = cam[2]; CHK = (240, 240, 230, 235)
    def L(pts, w=4): p.line([W2S(cam, *q) for q in pts], CHK, w * z)
    for ox in (0, 110):
        L([(200 + ox, 160), (215 + ox, 250), (205 + ox, 300), (222 + ox, 380), (214 + ox, 420)])
        L([(232 + ox, 160), (240 + ox, 245), (232 + ox, 300), (244 + ox, 380), (240 + ox, 420)])
        L([(208 + ox, 420), (250 + ox, 420), (246 + ox, 440), (212 + ox, 440), (208 + ox, 420)], 4)     # hoof
        for j in range(5):
            yy = 190 + j * 30; L([(214 + ox, yy), (198 + ox, yy + 12)], 2); L([(236 + ox, yy + 8), (252 + ox, yy + 20)], 2)   # fur
    L([(180, 150), (380, 150)], 3)
    p.ell(*W2S(cam, 285, 112), 12 * z, 12 * z, None, CHK, 3 * z); p.line([W2S(cam, 285, 124), W2S(cam, 285, 132)], CHK, 3 * z)   # «?»

def stick(p, cam, hand, ang, L=230):
    z = cam[2]; ex, ey = hand[0] + math.cos(ang) * L * z, hand[1] + math.sin(ang) * L * z
    p.line([hand, (ex, ey)], (120, 80, 40, 255), 7 * z); p.ell(ex, ey, 4 * z, 4 * z, (240, 240, 230, 255), None)

def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255):
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(LZ, size)
    kw = dict(font=f, anchor="mm", direction="rtl", language="ar")
    d.text((x, y), s, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), **kw)
    d.text((x, y), s, fill=fill + (alpha,), **kw); img.paste(lay, (0, 0), lay)
def popk(tt, t0, d=0.22):
    u = kk(tt, t0, t0 + d); return 0 if u <= 0 else (1 + 0.25 * math.sin(u * math.pi)) if u < 1 else 1
def series_tag(fr, tt, t0, t1):
    k = min(ease(kk(tt, t0, t0 + 0.35)), 1 - ease(kk(tt, t1 - 0.35, t1)))
    if k <= 0: return
    d = ImageDraw.Draw(fr, "RGBA"); x = -620 + 680 * k
    d.rounded_rectangle([x, 60, x + 620, 170], 26, fill=(230, 120, 30, 235), outline=(255, 255, 255, 255), width=4)
    lzt(fr, x + 310, 108, "يوميات شطة وزلطة", 60, (255, 255, 255))

_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/daily/02")
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
    img = bg_crop(CLASS, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    legs_drawing(p, cam, tt)
    laughing = tt >= LAUGH
    lu = (tt - LAUGH) if laughing else 0
    jolt = 22 if SLAM <= tt < SLAM + 0.25 else 0                      # everyone jumps at the slam
    zx, zy, zk = zal_pos(tt)
    for ri, (x0, x1, top, bot, s, kids) in enumerate(ROWS):
        for who, x, fy in kids:
            if who == "zalata": continue
            ex, look, hop, arms = "neutral", -1, 0, "down"
            if GROAN[0] <= tt < GROAN[1]: ex = "sad"
            if GIG <= tt < GIG + 1.0 and who not in ("shatta",): ex = "happy"; hop = abs(math.sin(tt * 18)) * 5 * s
            if tt >= PUNCH: look = -1
            if who == "abdo" and SNORT <= tt < SNORT + 1.1: ex = "laugh"; hop = abs(math.sin(tt * 14)) * 10
            if who == "tota" and SNORT <= tt < SLAM: ex = "happy"; arms = "scared"
            if tt >= SLAM: ex = "shock" if tt < SLAM + 1.2 else "neutral"
            if PUNCH <= tt < LAUGH: ex = "shock"
            if laughing: ex = "laugh"; hop = abs(math.sin(lu * (9 + ri) + x)) * 14 * s; arms = "up" if (x // 10) % 2 else "hips"
            if who == "shatta":
                eat = None if (tt >= SLAM or laughing) else (tt * 0.5) % 1.0
                person(lay, cam, who, x, fy - jolt * s, s, tt, ex, look, arms, 0, None, hop,
                       "chipsbag" if tt < SLAM else None, eat)
            else:
                person(lay, cam, who, x, fy - jolt * s, s, tt, ex, look, arms, 0, None, hop)
        if ri == 1 and SNORT <= tt < SLAM:      # Tota's notebook in front of her face
            q = W2S(cam, 1290, 674 - 190 * 0.82 * 0.74 + 10); p.rect(q[0] - 30 * z, q[1] - 6 * z, q[0] + 34 * z, q[1] + 40 * z, (230, 230, 210, 255), INK, 2 * z, 3 * z)
        if ri == 2 and zk < 0.5:               # Zalata still seated
            person(lay, cam, "zalata", zx, zy, s, tt, "neutral", -1)
        desk(p, cam, x0, x1, top, bot, s)
    # chips bag flying off the desk at the slam
    if SLAM <= tt < SLAM + 1.0:
        u = kk(tt, SLAM, SLAM + 1.0); bx_, by_ = W2S(cam, 1490 + 160 * u, 640 - 420 * u + 520 * u * u)
        p.rect(bx_ - 18 * z, by_ - 26 * z, bx_ + 18 * z, by_ + 26 * z, (230, 60, 50, 255), INK, 2 * z, 4 * z)
        for i in range(6):
            cxp, cyp = W2S(cam, 1480 + i * 40 * u + 20, 650 - 300 * u + 400 * u * u + i * 8)
            p.ell(cxp, cyp, 7 * z, 5 * z, (240, 190, 70, 255), INK, 1 * z)
    # Zalata standing in the aisle (after «قوم»)
    if zk >= 0.5:
        CH["zalata"]["legup"] = ease(kk(tt, LEG[0], LEG[0] + 0.6)) if tt >= LEG[0] else 0
        zex = "flat" if tt >= LEG[0] else "neutral"
        if laughing: zex = "smug"
        person(lay, cam, "zalata", zx, zy, ROWS[2][4], tt, zex, -1, "hips" if tt >= LEG[0] else "down")
        CH["zalata"]["legup"] = 0
    # Fahmy
    fx = fahmy_x(tt); fs = 1.42
    fex = "smug"
    if GIG <= tt < SNORT: fex = "angry"
    if tt >= SNORT: fex = "angry"
    if PUNCH + 1.6 <= tt: fex = "shock"
    if laughing: fex = "shock"
    walk = tt * 6 if WALK[0] <= tt < WALK[1] else None
    FXs, FYs, FSs = person(lay, cam, "fahmy", fx, 905, fs, tt, fex, 1, "point" if not laughing else "down", 0, walk,
                           12 if BEAT[0] <= tt < BEAT[0] + 0.15 else 0)
    shy = FYs - 134 * FSs
    hand = (FXs + 84 * FSs, shy - 6 * FSs)
    if tt < GROAN[0]: ang = -2.5                                   # pointing back at the board
    elif SLAM - 0.2 <= tt < SLAM + 0.3: ang = lerp(-0.9, 0.55, ease(kk(tt, SLAM - 0.2, SLAM)))
    elif laughing: ang = 1.4
    else: ang = 0.25 + math.sin(tt * 3) * 0.05
    if not laughing: stick(p, cam, hand, ang, 230 if SLAM - 0.2 <= tt < SLAM + 0.3 or tt < GROAN[0] else 120)
    else: stick(p, cam, (FXs + 34 * FSs, shy + 72 * FSs), ang, 200)
    # eye twitch / steam / chalk drop
    hx_, hy_ = FXs, FYs - 190 * FSs
    if GIG <= tt < GIG + 1.0 and (int(tt * 12) % 2):
        p.line([(hx_ + 30 * FSs, hy_ - 30 * FSs), (hx_ + 44 * FSs, hy_ - 38 * FSs)], INK, 3 * FSs)
    if (SLAM <= tt < PUNCH) or laughing:
        for i in range(2):
            u = (tt * 1.4 + i * 0.5) % 1
            p.ell(hx_ + (i * 2 - 1) * 40 * FSs, hy_ - (60 + 50 * u) * FSs, (8 + 14 * u) * FSs, (6 + 10 * u) * FSs, (255, 255, 255, int(200 * (1 - u))), None)
    if BEAT[0] + 0.45 <= tt < LAUGH + 0.4:
        u = kk(tt, BEAT[0] + 0.45, BEAT[0] + 0.85); cxp, cyp = W2S(cam, fx - 20, 905 - 95 * fs * 0.82 + 300 * u * u)
        p.rect(cxp - 10 * z, cyp - 4 * z, cxp + 10 * z, cyp + 4 * z, (245, 245, 240, 255), INK, 1 * z)
    lay = tint_layer(lay, (255, 240, 220)); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    if laughing:   # red-faced Fahmy
        pass
    series_tag(fr, tt, GROAN[0] + 0.1, GROAN[1] + 1.6)
    if SLAM <= tt < SLAM + 0.3:
        fr = Image.blend(fr, Image.new("RGB", fr.size, (255, 255, 255)), 0.25 * (1 - kk(tt, SLAM, SLAM + 0.3)))
    if laughing:
        for i, (dx, dy, sz) in enumerate(((-560, -300, 110), (420, -360, 96), (-320, -120, 84), (600, -100, 100), (60, -420, 90), (-700, 40, 80))):
            t0_ = LAUGH + 0.2 + i * 0.35
            if tt >= t0_: lzt(fr, W / 2 + dx + math.sin(tt * 6 + i) * 10, H / 2 + dy, "ههههه", int(sz * popk(tt, t0_)), (255, 214, 90))
        if tt >= FREEZE:
            fr = Image.blend(fr, Image.new("RGB", fr.size, (255, 255, 255)), 0.6 * (1 - kk(tt, FREEZE, FREEZE + 0.2)))
    return finish(fr, tt)

def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(41)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 400) * 0.02, 0, 1.0)                 # class room tone
    d = np.arange(int(SR * 0.08)) / SR; tap = (np.sin(2 * np.pi * 700 * d) * np.exp(-d * 60) + r.normal(0, 1, len(d)) * np.exp(-d * 120) * 0.4) * 0.7
    for tp in TAPS: mix_into(buf, tap.astype(np.float32), tp, 1.0)
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 0.5: mix_into(buf, SFXF["whoosh"] * 0.3, s_["start"] - 0.1, 1.0)
    mix_into(buf, SFXF["switch"] * 0.6, GROAN[0] + 0.1, 1.0)
    mix_into(buf, SFXF["giggle"] * 0.8, GIG, 1.0)
    mix_into(buf, SFXF["giggle"][int(SR * 0.3):] * 0.6, SNORT, 1.0)
    mix_into(buf, SFXF["slam"] * 1.0, SLAM, 1.0); mix_into(buf, SFXF["crinkle"] * 0.6, SLAM + 0.05, 1.0)
    d = np.arange(int(SR * 0.05)) / SR; tick = (np.sin(2 * np.pi * 1800 * d) * np.exp(-d * 80) * 0.4).astype(np.float32)
    mix_into(buf, tick, BEAT[0] + 0.85, 1.0)                                                         # chalk hits the floor
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
