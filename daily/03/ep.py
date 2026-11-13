# «يوميات شطة وزلطة» — بابا في المستشفى  (H 1920x1080 + V 1080x1920 in one pass)
# render:  python ep.py audio  →  python ep.py part 0 2 & python ep.py part 1 2  →  concat  →  mux mix.wav
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/daily/03")
SERIES = "يوميات شطة وزلطة"; EPT = "بابا في المستشفى"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"
SFXP = {"whoosh": "/trend/01/sfx/whoosh.mp3", "steps": "/s2e1/sfx/footsteps.mp3", "aww": "/daily/03/sfx/aww.mp3",
        "groan": "/daily/03/sfx/groan.mp3", "run": "/daily/03/sfx/runaway.mp3", "giggle": "/daily/02/sfx/giggle.mp3"}
SFXF = {n: load_audio(ROOT + p) for n, p in SFXP.items()}

SUB = {"F01": "إنت متأخر ليه؟", "S01": "معلش يا أستاذ... أصل بابا في المستشفى.", "F02": "يا حبيبي... خلاص، خش اتفضل.",
       "F03": "اتأخرت تاني النهارده ليه؟", "S02": "معلش... بابا في المستشفى.", "F04": "طيب... خش اقعد مكانك.",
       "F05": "وبعدين؟ اتأخرت ليه؟", "S03": "بابا لسه في المستشفى يا أستاذ.",
       "F06": "اتأخرت ليه؟", "S04": "أصل بابا لسه في المستشفى.", "F07": "هو أبوك في المستشفى ليه بقى؟!",
       "S05": "أصل بابا شغال دكتور.", "F08": "شطة!!!", "GROUP": ""}
WHO = {k: ("fahmy" if k[0] == "F" else "shatta") for k in SUB}; WHO["GROUP"] = "-"
EXPR = {"F01": "angry", "S01": "sad", "F02": [(0, "sad"), (0.45, "happy")], "F03": "angry", "S02": "sad", "F04": "flat",
        "F05": "angry", "S03": "sad", "F06": "flat", "S04": "sad", "F07": "angry", "S05": [(0, "neutral"), (0.7, "happy")],
        "F08": "shout", "GROUP": "laugh"}
load_lines(list(SUB))
CLASS = _ld(ROOT + "/daily/bg/classroom.png")      # canonical «فصل المدرسة» (docs/locations.md)

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear()
TWO = lambda z=1.72, cx=690, cy=690: (cx, cy, z)          # Fahmy + Shatta two-shot (Zalata at the right edge listens)
WIDE = (1000, 560, 1.0)
REACT = (1380, 600, 1.45)
CLOCKCAM = (850, 200, 2.6)
DAYN = ["اليوم الأول", "اليوم التاني", "اليوم التالت", "اليوم الرابع"]
CLOCKT = [(8, 5), (8, 15), (8, 30), (8, 45)]
DAYS = []; t = 0.0
for i in range(4):
    d = dict(i=i, clk=t)
    shot("clk", t, t + 1.45, CLOCKCAM, (850, 195, 2.85), tin=None if i == 0 else "fade", day=i)
    d["knock"] = t + 0.75; t += 1.45
    d["enter"] = (t + 0.1, t + 1.35)
    if i < 3:
        shot("st", t, t + 1.5, WIDE, (930, 600, 1.12), tin="whipl"); t += 1.5
    else:                                                           # day 4: the class is already waiting for him
        shot("st", t, t + 1.7, (1200, 600, 1.25), (800, 640, 1.35), tin="whipl"); t += 1.7
    if i == 0:
        s = t; t = say(t + 0.1, "F01") + 0.1; t = say(t + 0.05, "S01") + 0.2
        shot("st", s, t, TWO(1.7), TWO(1.8))
        d["aww"] = (t, t + 1.4); shot("st", t, t + 1.4, REACT, (1380, 600, 1.52), tin="whip"); t += 1.4
        s = t; t = say(t + 0.05, "F02") + 0.2; shot("st", s, t, TWO(1.78), TWO(1.84), tin="whipl")
    elif i == 1:
        s = t; t = say(t + 0.1, "F03") + 0.1; t = say(t + 0.05, "S02") + 0.15
        shot("st", s, t, TWO(1.75), TWO(1.85))
        d["glance"] = (t, t + 1.1); shot("st", t, t + 1.1, REACT, REACT, tin="whip"); t += 1.1
        s = t; t = say(t + 0.05, "F04") + 0.2; shot("st", s, t, TWO(1.8), TWO(1.86), tin="whipl")
    elif i == 2:
        s = t; t = say(t + 0.1, "F05") + 0.1; t = say(t + 0.05, "S03") + 0.15
        shot("st", s, t, TWO(1.78), TWO(1.9))
        d["groan"] = (t, t + 1.4); shot("st", t, t + 1.4, REACT, (1300, 620, 1.6), tin="whip"); t += 1.4
        d["susp"] = (t, t + 1.3); shot("st", t, t + 1.3, (840, 730, 2.4), (840, 725, 2.75), tin="whipl"); t += 1.3
    else:
        s = t; t = say(t + 0.15, "F06") + 0.15; t = say(t + 0.05, "S04") + 0.15
        shot("st", s, t, TWO(1.8), TWO(1.95))
        s = t; t = say(t + 0.1, "F07") + 0.2; shot("st", s, t, TWO(2.05, 720, 670), TWO(2.25, 740, 660))
        s = t; t = say(t + 0.1, "S05") + 0.1; d["punch"] = s
        shot("st", s, t, (560, 700, 2.35), (560, 690, 2.55), tin="whipl")
        d["beat"] = (t, t + 1.5)
        shot("st", t, t + 0.75, (1380, 600, 1.4), (1380, 600, 1.45), tin="whip")             # the class: frozen
        shot("st", t + 0.75, t + 1.5, (840, 620, 2.4), (840, 610, 2.7))                     # Fahmy: slow boil
        t += 1.5
        s = t; t = say(t, "F08") + 0.15; d["shout"] = s
        shot("st", s, t, (780, 640, 1.9), (800, 620, 2.4), ease="crash"); shakes.append((s, 30))
        d["run"] = (t, t + 1.0); shot("st", t, t + 1.0, (640, 640, 1.3), (600, 640, 1.34)); t += 1.0
    if i < 3:
        d["seat"] = (t, t + 1.5); shot("st", t, t + 1.5, WIDE, (1040, 580, 1.06)); t += 1.5
    d["end"] = t; DAYS.append(d)
LAUGH = t; LU = DUR["GROUP"]
shot("st", t, t + 1.9, (1240, 610, 1.32), (1240, 610, 1.4), tin="whipl")
shot("st", t + 1.9, t + 3.3, (1350, 610, 1.8), (1350, 615, 1.9), tin="whip")              # Zalata/Tota/Abdo in tears
shot("st", t + 3.3, t + LU + 0.2, (820, 610, 2.1), (1100, 600, 1.35), tin="whipl")        # Fahmy fuming → pull back
t += LU + 0.2; FREEZE = t - 0.25
shot("end", t, t + 2.6, None); t += 2.6
TOTAL = t
def day_of(tt):
    for d in DAYS:
        if tt < d["end"]: return d
    return DAYS[-1]
def win(tt, d, key): return key in d and d[key][0] <= tt < d[key][1]

# ---------------- cast / staging (world = 1920x1080 classroom) ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
for i, sh_ in enumerate(((70, 120, 200), (230, 200, 60), (60, 160, 160), (200, 70, 70), (130, 90, 170), (240, 140, 60))):
    CH[f"kid{i}"] = dict(shirt=sh_, hair=((40, 30, 24), (90, 50, 30), (20, 20, 22), (120, 70, 40), (30, 26, 24), (70, 40, 26))[i], scale=0.95)
ROWS = [  # (desk x0, x1, desk top y, panel bottom y, scale, [(who, x, feet_y)])  — back to front; Shatta's seat (1440) is empty
    (1290, 1910, 548, 598, 0.62, [("kid0", 1390, 585), ("kid1", 1560, 585), ("kid2", 1740, 585), ("kid3", 1860, 585)]),
    (1170, 1830, 625, 690, 0.82, [("tota", 1290, 674), ("kid4", 1460, 674), ("abdo", 1650, 674), ("kid5", 1790, 674)]),
    (1060, 1640, 735, 820, 1.05, [("zalata", 1150, 798)]),
]
FX, FY, FS = 830, 905, 1.42
DOOR, STAND, SEAT = (-120, 950, 1.12), (545, 945, 1.12), (1260, 1050, 1.25)

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, walk=None, hop=0.0, back=False):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    if talking and arms == "down": arms = "talk"
    blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11 and expr not in ("sleepy", "laugh")
    X, Y_ = W2S(cam, x, y - hop); S = s * cam[2]
    if back: draw_back(P(lay), who, X, Y_, S, tt, walk, arms)
    else: draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, None, lean, walk)
    if who.startswith("kid"):          # generic students get a simple hair cap
        sc = S * CH[who]["scale"]; hx, hy = X + lean * 18 * sc, Y_ - 190 * sc
        P(lay).d.chord([P(lay).S(hx - 47 * sc), P(lay).S(hy - 50 * sc), P(lay).S(hx + 47 * sc), P(lay).S(hy + 30 * sc)], 180, 360,
                       fill=C(CH[who]["hair"]), outline=INK, width=P(lay).S(2.5 * sc))
    return X, Y_, S * CH[who]["scale"]

WOOD = (150, 98, 52, 255); WOOD_D = (112, 70, 36, 255)
def desk(p, cam, x0, x1, top, bot, s):
    z = cam[2]; a, b = W2S(cam, x0, top), W2S(cam, x1, bot)
    p.rect(a[0], a[1] - 14 * s * z, b[0], a[1] + 4 * z, (176, 120, 66, 255), INK, 3 * z, 4 * z)
    p.rect(a[0] + 8 * z, a[1] + 4 * z, b[0] - 8 * z, b[1], WOOD, INK, 3 * z, 2 * z)
    for xx in range(int(x0) + 160, int(x1) - 40, 290):
        q = W2S(cam, xx, top); p.line([(q[0], a[1] + 10 * z), (q[0], b[1] - 6 * z)], WOOD_D, 3 * z)
    for xx in (x0 + 20, x1 - 20):
        q = W2S(cam, xx, bot); p.line([q, (q[0], q[1] + 40 * s * z)], (60, 60, 64, 255), 6 * z)

def clock(p, cam, tt):
    """wall clock between the cupboard and the map — fast-forwards to the day's (later and later) time on the day card"""
    z = cam[2]; cx, cy = W2S(cam, 852, 168); r = 46 * z
    d = day_of(tt); h, m = CLOCKT[d["i"]]
    mins = h * 60 + m
    if shot_at(tt)["set"] == "clk": mins -= 40 * (1 - ease(kk(tt, d["clk"] + 0.05, d["clk"] + 0.85)))
    p.ell(cx, cy + 3 * z, r + 4 * z, r + 4 * z, (0, 0, 0, 70), None)
    p.ell(cx, cy, r + 5 * z, r + 5 * z, (150, 40, 40, 255), INK, 3 * z); p.ell(cx, cy, r, r, (250, 248, 238, 255), INK, 2 * z)
    for j in range(12):
        a = j * math.pi / 6; r0 = r * (0.78 if j % 3 else 0.68)
        p.line([(cx + math.cos(a) * r0, cy + math.sin(a) * r0), (cx + math.cos(a) * r * 0.9, cy + math.sin(a) * r * 0.9)], INK, (3 if j % 3 else 5) * z / 1.4)
    am = (mins % 60) / 60 * 2 * math.pi - math.pi / 2; ah = (mins / 60 % 12) / 12 * 2 * math.pi - math.pi / 2
    p.line([(cx, cy), (cx + math.cos(ah) * r * 0.5, cy + math.sin(ah) * r * 0.5)], INK, 6 * z / 1.4)
    p.line([(cx, cy), (cx + math.cos(am) * r * 0.78, cy + math.sin(am) * r * 0.78)], INK, 4 * z / 1.4)
    p.ell(cx, cy, 4 * z, 4 * z, (200, 40, 40, 255), INK, 1 * z)

def stick(p, cam, hand, ang, L=170):
    z = cam[2]; ex, ey = hand[0] + math.cos(ang) * L * z, hand[1] + math.sin(ang) * L * z
    p.line([hand, (ex, ey)], (120, 80, 40, 255), 7 * z); p.ell(ex, ey, 4 * z, 4 * z, (240, 240, 230, 255), None)

def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255):
    if size < 4: return
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
os.chdir(ROOT + "/daily/03")
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

# ---------------- Shatta's blocking ----------------
def shatta_state(tt, d):
    """-> (x, y, s, walk, back, expr, arms) or None when he's not in the room"""
    if tt < d["enter"][0] or d["i"] == 3 and "run" in d and tt >= d["run"][1]: return None
    if tt < d["enter"][1]:                                        # comes in from the door (off-screen left), schoolbag on
        k = kk(tt, *d["enter"]); e = ease(k) * 0.3 + k * 0.7
        return (lerp(DOOR[0], STAND[0], e), lerp(DOOR[1], STAND[1], e), STAND[2], tt * 9, False, "sad", "down")
    if "seat" in d and tt >= d["seat"][0]:                         # walks to his seat (back to the camera)
        k = ease(kk(tt, d["seat"][0] + 0.1, d["seat"][1]))
        if tt >= d["seat"][1] - 0.05: return None
        return (lerp(STAND[0], SEAT[0], k), lerp(STAND[1], SEAT[1], k), lerp(STAND[2], SEAT[2], k), tt * 8, True, "sad", "down")
    if "run" in d and tt >= d["run"][0]:                           # bolts out of the door, back to camera
        k = kk(tt, d["run"][0] + 0.12, d["run"][0] + 0.75)
        return (lerp(STAND[0], -260, k * k), STAND[1], STAND[2], tt * 22, True, "scared", "up")
    ex = "sad"; arms = "down"
    if d["i"] == 3 and tt >= d["punch"] + DUR["S05"]: ex = "neutral"
    if "shout" in d and tt >= d["shout"]: ex, arms = "scared", "scared"
    return (*STAND, None, False, ex, arms)

# ---------------- frame ----------------
def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "end": return finish(endcard(tt, sh), tt)
    cam = cam_at(sh, tt); z = cam[2]
    img = bg_crop(CLASS, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    clock(p, cam, tt)
    d = day_of(tt); i = d["i"]
    laughing = tt >= LAUGH; lu = tt - LAUGH
    knocked = tt >= d["knock"] + 0.15 and not laughing
    lean4 = -0.35 * ease(kk(tt, d["knock"], d["knock"] + 0.6)) if i == 3 and not laughing else 0
    for ri, (x0, x1, top, bot, s, kids) in enumerate(ROWS):
        for j, (who, x, fy) in enumerate(kids):
            ex, look, hop, arms, lean = "neutral", (-1 if knocked else 0), 0, "down", 0
            if i == 3: lean = lean4; ex = "flat" if not laughing else ex
            if win(tt, d, "aww"):
                ex = "sad"; lean = -0.15
                if who == "tota": arms = "scared"
            if win(tt, d, "glance"):
                u = tt - d["glance"][0]; look = (1 if (j + ri) % 2 else -1) if 0.25 < u < 0.8 else -1; ex = "flat"
            if win(tt, d, "groan"):
                ex = "flat"; look = 1 if (j + ri) % 2 else -1
                if who == "zalata": ex, arms, look = "smug", "talk", -1
                if who == "abdo": ex = "sleepy"
            if i == 3 and d["punch"] <= tt < d["shout"]: ex = "shock" if tt >= d["punch"] + 0.6 else "flat"
            if i == 3 and tt >= d["shout"] and not laughing: ex = "shock"; hop = 18 * s if tt < d["shout"] + 0.25 else 0; look = -1
            if laughing:
                ex = "laugh"; hop = abs(math.sin(lu * (9 + ri) + x)) * 14 * s; arms = "up" if (x // 10) % 2 else "hips"
                look = 0; lean = math.sin(lu * 6 + x) * 0.25
            if i in (0, 1, 2) and win(tt, d, "seat") and who == "zalata": look = -1
            person(lay, cam, who, x, fy, s, tt, ex, look, arms, lean, None, hop)
        if ri == 2 and win(tt, d, "groan"):                         # Zalata counts on his fingers: 1… 2… 3
            u = tt - d["groan"][0]; n = min(3, 1 + int(u / 0.32))
            q = W2S(cam, 1150 + 70, 798 - 190 * 1.05 * 0.8)
        desk(p, cam, x0, x1, top, bot, s)
    # Fahmy
    fex = ["flat", "flat", "angry", "flat"][i]
    farms = "hips" if i >= 2 else "down"
    if win(tt, d, "aww"): fex = "sad"
    if win(tt, d, "susp"): fex = "flat"
    if i == 3 and tt >= d["enter"][1]: farms = "hips"
    if i == 3 and "beat" in d and tt >= d["beat"][0]: fex = "angry"
    if i == 3 and "shout" in d and tt >= d["shout"]: fex, farms = "shout", "up"
    if laughing: fex, farms = "angry", "hips"
    flook = -1 if knocked else 0
    boil = 0
    if i == 3 and "beat" in d and d["beat"][0] + 0.75 <= tt < d["shout"]: boil = kk(tt, d["beat"][0] + 0.75, d["shout"])
    FXs, FYs, FSs = person(lay, cam, "fahmy", FX + (math.sin(tt * 60) * 3 * boil), FY, FS, tt, fex, flook, farms,
                           -0.2 if (i == 3 and tt >= d.get("punch", 1e9)) else 0, None, 10 if ("shout" in d and d["shout"] <= tt < d["shout"] + 0.2) else 0)
    shy = FYs - 134 * FSs
    if farms == "down": stick(p, cam, (FXs + 34 * FSs, shy + 72 * FSs), 1.35, 160)
    elif farms == "hips": stick(p, cam, (FXs + 48 * FSs, shy + 40 * FSs), 1.2 + math.sin(tt * 3) * 0.05, 170)
    hx_, hy_ = FXs, FYs - 190 * FSs
    if (i == 3 and "beat" in d and d["beat"][0] + 0.75 <= tt) or laughing:          # steam
        for k_ in range(2):
            u = (tt * 1.6 + k_ * 0.5) % 1
            p.ell(hx_ + (k_ * 2 - 1) * 40 * FSs, hy_ - (60 + 50 * u) * FSs, (8 + 14 * u) * FSs, (6 + 10 * u) * FSs, (255, 255, 255, int(200 * (1 - u))), None)
    # Shatta
    st_ = None if laughing else shatta_state(tt, d)
    if st_:
        x, y, s, walk, back, ex, arms = st_
        SX, SY, SS_ = person(lay, cam, "shatta", x, y, s, tt, ex, 1, arms, 0, walk, 0, back)
        if not back:   # schoolbag strap
            p.line([(SX - 20 * SS_, SY - 134 * SS_), (SX + 24 * SS_, SY - 70 * SS_)], (70, 50, 120, 255), 5 * SS_)
        else:          # schoolbag on his back
            p.rect(SX - 26 * SS_, SY - 140 * SS_, SX + 26 * SS_, SY - 76 * SS_, (90, 60, 150, 255), INK, 3 * SS_, 8 * SS_)
        if "run" in d and tt >= d["run"][0]:                     # dust puffs behind the runner
            for k_ in range(4):
                u = (tt * 3 + k_ * 0.25) % 1
                p.ell(SX + (30 + 70 * u) * SS_, SY - 6 * SS_, (10 + 22 * u) * SS_, (6 + 10 * u) * SS_, (225, 215, 195, int(170 * (1 - u))), None)
    lay = tint_layer(lay, (255, 240, 220)); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    # ---- overlays ----
    if sh["set"] == "clk":
        u = tt - sh["start"]
        lzt(fr, W / 2, H - 250, DAYN[i], int(130 * popk(tt, sh["start"] + 0.15, 0.3)), (255, 214, 90) if i < 3 else (255, 110, 80))
        h, m = CLOCKT[i]
        if u > 0.85: lzt(fr, W / 2, H - 125, f"{h}:{m:02d}", int(70 * popk(tt, sh["start"] + 0.85)), (255, 255, 255))
    if i == 0: series_tag(fr, tt, DAYS[0]["enter"][0], DAYS[0]["enter"][0] + 2.6)
    if win(tt, d, "groan"):
        u = tt - d["groan"][0]; q = W2S(cam, 1150, 560)
        if u < 0.95:
            for f_, ch_ in enumerate("١٢٣"):
                if u >= 0.1 + f_ * 0.28: lzt(fr, q[0] + (1 - f_) * 70, q[1], ch_, int(70 * popk(tt, d["groan"][0] + 0.1 + f_ * 0.28)), (255, 255, 255))
        else: lzt(fr, q[0], q[1], "٣ أيام؟!", int(68 * popk(tt, d["groan"][0] + 0.95)), (255, 214, 90))
    if win(tt, d, "susp"):
        q = W2S(cam, FX + 70, FY - 300); lzt(fr, q[0], q[1], "؟", int(150 * popk(tt, d["susp"][0] + 0.45)), (255, 214, 90))
    if i == 3 and "beat" in d and d["beat"][0] <= tt < d["beat"][0] + 0.75:
        fr = ImageEnhance.Color(fr).enhance(0.35)                 # the room freezes
    if "shout" in d and d["shout"] <= tt < d["shout"] + 0.3:
        fr = Image.blend(fr, Image.new("RGB", fr.size, (255, 60, 40)), 0.28 * (1 - kk(tt, d["shout"], d["shout"] + 0.3)))
    if laughing:
        for k_, (dx, dy, sz) in enumerate(((-560, -300, 110), (420, -360, 96), (-320, -120, 84), (600, -100, 100), (60, -420, 90), (-700, 40, 80))):
            t0_ = LAUGH + 0.2 + k_ * 0.35
            if tt >= t0_: lzt(fr, W / 2 + dx + math.sin(tt * 6 + k_) * 10, H / 2 + dy, "ههههه", int(sz * popk(tt, t0_)), (255, 214, 90))
        if tt >= FREEZE:
            fr = Image.blend(fr, Image.new("RGB", fr.size, (255, 255, 255)), 0.6 * (1 - kk(tt, FREEZE, FREEZE + 0.2)))
    return finish(fr, tt)

def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(43)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 400) * 0.02, 0, 1.0)                 # class room tone
    tick = tone(2400, 0.03, 0.25, 90)
    knock = sfx_knock().astype(np.float32)
    for d in DAYS:
        for k_ in range(6): mix_into(buf, tick, d["clk"] + 0.1 + k_ * 0.13, 1.0)                     # clock racing forward
        mix_into(buf, knock * 0.8, d["knock"], 1.0); mix_into(buf, knock * 0.7, d["knock"] + 0.22, 1.0)
        if d["i"] == 3: mix_into(buf, knock * 0.6, d["knock"] + 0.44, 1.0)
        mix_into(buf, SFXF["steps"] * 0.7, d["enter"][0], 1.0)
        if "seat" in d: mix_into(buf, SFXF["steps"] * 0.5, d["seat"][0] + 0.1, 1.0)
        if "aww" in d: mix_into(buf, SFXF["aww"] * 0.9, d["aww"][0] + 0.05, 1.0)
        if "glance" in d: mix_into(buf, SFXF["giggle"][:int(SR * 0.6)] * 0.25, d["glance"][0] + 0.3, 1.0)
        if "groan" in d: mix_into(buf, SFXF["groan"] * 0.9, d["groan"][0] + 0.05, 1.0)
        if "susp" in d:
            for k_, f in enumerate((220, 208)): mix_into(buf, tone(f, 0.5, 0.18, 4), d["susp"][0] + 0.2 + k_ * 0.35, 1.0)
        if "beat" in d:                                           # silence… a cricket… then the slow-boil rumble
            b0 = d["beat"][0]
            for k_ in range(3):
                ch_ = np.concatenate([tone(4300, 0.05, 0.12, 20), np.zeros(int(SR * 0.04), np.float32)] * 3)
                mix_into(buf, ch_, b0 + 0.1 + k_ * 0.3, 1.0)
            mix_into(buf, lowpass(r.normal(0, 1, int(SR * 0.8)).astype(np.float32), 120) * np.linspace(0, 0.5, int(SR * 0.8)).astype(np.float32), b0 + 0.7, 1.0)
        if "shout" in d:
            mix_into(buf, tone(55, 0.9, 0.9, 3) + tone(82, 0.9, 0.5, 4), d["shout"], 1.0)
        if "run" in d: mix_into(buf, SFXF["run"] * 1.0, d["run"][0], 1.0)
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 0.5: mix_into(buf, SFXF["whoosh"] * 0.25, s_["start"] - 0.1, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), TOTAL - 2.4 + k_ * 0.09, 1.0)
    rms = lambda x: float(np.sqrt(np.mean(x ** 2))) + 1e-9
    ref = []
    for st, k in lines:
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8
        if k == "GROUP": continue
        ref.append(rms(v)); mix_into(buf, v, st, 1.0)
    g = AUD["GROUP"]; mix_into(buf, g / rms(g) * float(np.mean(ref)) * 1.25, LAUGH, 1.0)   # crowd laugh ~2 dB above the dialogue
    write_wav(buf[:int(TOTAL * SR)], path)

if __name__ == "__main__":
    print("TOTAL", round(TOTAL, 1))
    if sys.argv[1:2] == ["stills"]: render(None, None, [float(v) for v in sys.argv[2:]])
    elif sys.argv[1:2] == ["times"]:
        for s_ in shots: print(s_["set"], round(s_["start"], 2), round(s_["end"], 2), s_.get("tin", ""))
        for st, k in lines: print(k, round(st, 2))
        for d in DAYS: print({k: (tuple(round(v, 2) for v in val) if isinstance(val, tuple) else round(val, 2)) for k, val in d.items()})
    elif sys.argv[1:2] == ["part"]:
        i, n = int(sys.argv[2]), int(sys.argv[3]); a = round(TOTAL * i / n * FPS) / FPS; b = round(TOTAL * (i + 1) / n * FPS) / FPS
        render(f"h_{i}.mp4", f"v_{i}.mp4", None, a, b)
    elif sys.argv[1:2] == ["audio"]: build_audio()
