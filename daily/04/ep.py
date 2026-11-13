# «يوميات شطة وزلطة» — الواجب  (H 1920x1080 + V 1080x1920 in one pass)
# render:  python ep.py audio  →  python ep.py part 0 2 & python ep.py part 1 2  →  concat  →  mux mix.wav
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/daily/04")
SERIES = "يوميات شطة وزلطة"; EPT = "الواجب"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"
SFXP = {"whoosh": "/trend/01/sfx/whoosh.mp3", "slam": "/s2e1/sfx/slam.mp3", "crinkle": "/s2e1/sfx/crinkle.mp3",
        "steps": "/s2e1/sfx/footsteps.mp3", "giggle": "/daily/02/sfx/giggle.mp3"}
SFXF = {n: load_audio(ROOT + p) for n, p in SFXP.items()}

SUB = {"F01": "كل واحد يطلّع كشكول الواجب... حالاً!", "Z01": "أستاذ فهمي... ممكن سؤال؟", "F02": "اتفضل يا زلطة.",
       "Z02": "هو حضرتك... ممكن تعاقب حد على حاجة هو ما عملهاش؟", "F03": "لأ طبعاً! أنا أستاذ عادل! إزاي أعاقب حد على حاجة ما عملهاش؟!",
       "Z03": "طب الحمد لله... أصل أنا معملتش الواجب.", "F04": "أنا... إنت... إإإ...", "GROUP": ""}
WHO = {k: ("fahmy" if k[0] == "F" else "zalata") for k in SUB}; WHO["GROUP"] = "-"
EXPR = {"F01": "shout", "Z01": "happy", "F02": "neutral", "Z02": "neutral", "F03": [(0, "angry"), (0.3, "smug")],
        "Z03": [(0, "happy"), (0.45, "smug")], "F04": "shock", "GROUP": "laugh"}
load_lines(list(SUB))
CLASS = _ld(ROOT + "/daily/bg/classroom.png")      # canonical «فصل المدرسة» (docs/locations.md)

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear()
SLAM = 0.35
shot("st", 0.0, 0.55, (960, 660, 2.3), (970, 665, 2.4))                                   # insert: the stick crashes on the desk
shakes.append((SLAM, 26))
t = say(0.6, "F01") + 0.1
shot("st", 0.55, t, (900, 650, 2.2), (900, 660, 1.85), ease="crash", tin="zoom")
PANIC = (t, t + 1.8); shot("st", t, PANIC[1], (1330, 590, 1.4), (1330, 590, 1.48), tin="whip"); t = PANIC[1]   # bags, papers, Shatta proud, Zalata calm
WALK = (t, t + 2.3); shot("st", t, WALK[1], (760, 640, 1.45), (1010, 650, 1.55), tin="whipl"); t = WALK[1]     # Fahmy patrols → Zalata's hand goes up
RAISE = WALK[0] + 1.3
s = t; t = say(t + 0.05, "Z01") + 0.1; t = say(t + 0.05, "F02") + 0.1
shot("st", s, t, (1070, 680, 1.75), (1070, 680, 1.85))
s = t; t = say(t + 0.1, "Z02") + 0.15
shot("st", s, t, (1090, 660, 2.0), (1100, 655, 2.2))                                   # tighter: the trap question
s = t; t = say(t + 0.1, "F03") + 0.2; SPEECH = s
shot("st", s, t, (1180, 620, 1.35), (1120, 630, 1.6), tin="whip")                       # Fahmy addresses the whole class
NOD = (SPEECH + DUR["F03"] * 0.55, t)
s = t; t = say(t + 0.1, "Z03") + 0.25; PUNCH = s + 1.7                                  # «أصل أنا…» lands at ~1.7 s
GLINT = s + DUR["Z03"] - 0.3
shot("st", s, t, (1150, 650, 2.3), (1150, 640, 2.6), tin="whipl")
BEAT = (t, t + 1.6)
shot("st", t, t + 0.7, (1330, 590, 1.4), (1330, 590, 1.42), tin="whip")                 # the class: frozen
shot("st", t + 0.7, t + 1.6, (990, 640, 2.4), (990, 630, 2.75))                        # Fahmy: mouth opens… closes
t += 1.6
s = t; t = say(t, "F04") + 0.1; STAM = s
shot("st", s, t, (990, 630, 2.75), (990, 625, 3.0))
LAUGH = t; LU = DUR["GROUP"]
shot("st", t, t + 1.9, (1240, 610, 1.32), (1240, 610, 1.4), tin="whipl")
shot("st", t + 1.9, t + 3.3, (1480, 610, 1.75), (1480, 615, 1.85), tin="whip")          # Shatta/Tota/Abdo in tears
shot("st", t + 3.3, t + LU + 0.2, (1060, 650, 2.1), (1080, 650, 1.6), tin="whipl")     # Fahmy fuming, Zalata smug
t += LU + 0.2; FREEZE = t - 0.25
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
FX0, FX1, FY, FS = 800, 960, 905, 1.42             # Fahmy: by his desk → in the aisle in front of Zalata
def fahmy_x(tt): return lerp(FX0, FX1, ease(kk(tt, WALK[0] + 0.1, WALK[1] - 0.1)))

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, walk=None, hop=0.0, mouth_k=0.0):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    mouth = max(mouth, mouth_k)
    if talking and arms == "down": arms = "talk"
    blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11 and expr not in ("sleepy", "laugh")
    X, Y_ = W2S(cam, x, y - hop); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, None, lean, walk)
    if who.startswith("kid"):
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

def notebook(p, cx, cy, sc, open_=False, col=(60, 110, 200, 255)):
    if open_:
        p.rect(cx - 30 * sc, cy - 20 * sc, cx, cy + 20 * sc, (245, 245, 235, 255), INK, 2 * sc, 2 * sc)
        p.rect(cx, cy - 20 * sc, cx + 30 * sc, cy + 20 * sc, (245, 245, 235, 255), INK, 2 * sc, 2 * sc)
        for j in range(3):
            p.line([(cx - 24 * sc, cy - 10 * sc + j * 9 * sc), (cx - 6 * sc, cy - 10 * sc + j * 9 * sc)], (90, 90, 160, 255), 1.5 * sc)
            p.line([(cx + 6 * sc, cy - 10 * sc + j * 9 * sc), (cx + 24 * sc, cy - 10 * sc + j * 9 * sc)], (90, 90, 160, 255), 1.5 * sc)
    else:
        p.rect(cx - 20 * sc, cy - 26 * sc, cx + 20 * sc, cy + 26 * sc, col, INK, 2.5 * sc, 3 * sc)
        p.rect(cx - 12 * sc, cy - 14 * sc, cx + 12 * sc, cy - 4 * sc, (250, 250, 240, 255), None)

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
os.chdir(ROOT + "/daily/04")
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
    laughing = tt >= LAUGH; lu = tt - LAUGH
    jolt = 20 if SLAM <= tt < SLAM + 0.25 else 0
    fx = fahmy_x(tt)
    for ri, (x0, x1, top, bot, s, kids) in enumerate(ROWS):
        for j, (who, x, fy) in enumerate(kids):
            ex, look, hop, arms, lean = "neutral", -1, 0, "down", 0
            if tt < PANIC[0]: ex = "shock" if tt >= SLAM else "neutral"
            if PANIC[0] <= tt < WALK[1] and who not in ("zalata", "shatta"):          # digging for the notebook
                ex = "scared"; hop = abs(math.sin(tt * 13 + j * 2.1)) * 8 * s; look = 1 if int(tt * 4 + j) % 2 else -1
                arms = "hold" if int(tt * 5 + j) % 2 else "down"
            if who == "shatta" and PANIC[0] <= tt < LAUGH:                           # proud: notebook held high
                ex = "happy" if tt < PUNCH else "shock"; arms = "up" if tt < SPEECH else "hold"
            if who == "zalata":
                ex = "smug" if PANIC[0] <= tt < RAISE else "neutral"
                if tt >= RAISE: arms = "raise" if tt < SPEECH else "down"
                if tt >= PUNCH: ex = "smug"
                if laughing: ex = "smug"; arms = "hips"
            if NOD[0] <= tt < NOD[1] and who not in ("zalata",):
                ex = "happy"; hop = abs(math.sin((tt - NOD[0]) * 7 + j)) * 6 * s; look = -1
                if who == "tota": arms = "clap" if int(tt * 9) % 2 else "clap2"
            if BEAT[0] <= tt < LAUGH and who != "zalata": ex = "shock"; look = 1 if who != "shatta" else -1
            if laughing and who != "zalata":
                ex = "laugh"; hop = abs(math.sin(lu * (9 + ri) + x)) * 14 * s; arms = "up" if (x // 10) % 2 else "hips"
                look = 0; lean = math.sin(lu * 6 + x) * 0.25
                if who == "shatta": arms = "hips"
            X, Y_, SC = person(lay, cam, who, x, fy - jolt * s, s, tt, ex, look, arms, lean, None, hop)
            if who == "shatta" and PANIC[0] <= tt < LAUGH:                          # the notebook he is SO proud of
                sh_y = Y_ - 134 * SC
                if arms == "up": notebook(p, X + 72 * SC, sh_y - 70 * SC, SC * 1.1)
                else: notebook(p, X + 46 * SC, sh_y + 20 * SC, SC)
            if PANIC[0] <= tt < WALK[1] and who not in ("zalata", "shatta") and arms == "hold":
                notebook(p, X + 46 * SC, Y_ - 134 * SC + 30 * SC, SC * 0.9, col=((200, 60, 60, 255), (60, 160, 90, 255), (220, 180, 40, 255))[j % 3])
            if who == "zalata" and tt >= GLINT and tt < GLINT + 0.35:              # glasses glint ✦
                u = kk(tt, GLINT, GLINT + 0.35); gx, gy = X + 18 * SC, Y_ - 196 * SC; r = 26 * SC * math.sin(u * math.pi)
                p.line([(gx - r, gy), (gx + r, gy)], (255, 255, 255, 255), 3 * SC); p.line([(gx, gy - r), (gx, gy + r)], (255, 255, 255, 255), 3 * SC)
        desk(p, cam, x0, x1, top, bot, s)
    # flying papers in the panic
    if PANIC[0] <= tt < PANIC[1]:
        for k_ in range(7):
            u = ((tt - PANIC[0]) * 0.9 + k_ * 0.14) % 1
            q = W2S(cam, 1250 + k_ * 85 + math.sin(u * 6 + k_) * 30, 640 - 260 * u + 300 * u * u)
            a = u * 6 + k_; c, s_ = math.cos(a) * 14 * z, math.sin(a) * 10 * z
            p.poly([(q[0] - c, q[1] - s_), (q[0] + s_, q[1] - c), (q[0] + c, q[1] + s_), (q[0] - s_, q[1] + c)], (250, 250, 240, 255), INK, 1.5 * z)
    # Fahmy
    fex = "angry"
    if WALK[0] <= tt < WALK[1]: fex = "flat"
    if RAISE <= tt < SPEECH: fex = "neutral"
    if PUNCH <= tt: fex = "shock"
    if BEAT[0] + 0.7 <= tt < LAUGH: fex = "shock" if int((tt - BEAT[0]) * 3) % 2 else "flat"
    if laughing: fex = "angry"
    farms = "hips"
    if NOD[0] - 1.2 <= tt < NOD[1]: farms = "up" if tt < NOD[0] else "hips"
    walk = tt * 6 if WALK[0] + 0.1 <= tt < WALK[1] - 0.1 else None
    mk = 0
    if BEAT[0] + 0.7 <= tt < STAM: mk = 0.5 + 0.5 * math.sin((tt - BEAT[0]) * 9)     # mouth opens… closes… nothing comes out
    flook = 1 if tt >= WALK[0] + 0.6 else -1
    if NOD[0] - 1.2 <= tt < PUNCH: flook = 0
    if tt < SLAM + 0.5: farms = "point"
    FXs, FYs, FSs = person(lay, cam, "fahmy", fx, FY, FS, tt, fex, flook, farms, 0, walk,
                           10 if SLAM <= tt < SLAM + 0.15 else 0, mk)
    shy = FYs - 134 * FSs
    # the stick: smashes the teacher's desk at the hook, then rests in his hand (goes up/down in the beat)
    if tt < SLAM + 0.5:                                    # raised high → smashed flat onto the front desk
        hand = (FXs + 84 * FSs, shy - 6 * FSs); tgt = W2S(cam, 1078, 733)
        L = math.hypot(tgt[0] - hand[0], tgt[1] - hand[1]); a1 = math.atan2(tgt[1] - hand[1], tgt[0] - hand[0])
        ang = lerp(-1.35, a1, ease(kk(tt, 0.05, SLAM)) ** 2) if tt < SLAM else a1
        ex_, ey_ = hand[0] + math.cos(ang) * L, hand[1] + math.sin(ang) * L
        p.line([hand, (ex_, ey_)], (120, 80, 40, 255), 7 * z); p.ell(ex_, ey_, 4 * z, 4 * z, (240, 240, 230, 255), None)
    elif farms == "hips":
        ang = 1.25 + math.sin(tt * 3) * 0.05
        if BEAT[0] + 0.7 <= tt < LAUGH: ang = 1.25 - 0.9 * abs(math.sin((tt - BEAT[0]) * 4))
        hand = (FXs + 48 * FSs, shy + 40 * FSs); ex_, ey_ = hand[0] + math.cos(ang) * 170 * z, hand[1] + math.sin(ang) * 170 * z
        p.line([hand, (ex_, ey_)], (120, 80, 40, 255), 7 * z); p.ell(ex_, ey_, 4 * z, 4 * z, (240, 240, 230, 255), None)
    hx_, hy_ = FXs, FYs - 190 * FSs
    if BEAT[0] + 0.7 <= tt < LAUGH and int(tt * 12) % 2:                               # eye twitch
        p.line([(hx_ + 30 * FSs, hy_ - 30 * FSs), (hx_ + 44 * FSs, hy_ - 38 * FSs)], INK, 3 * FSs)
    if STAM <= tt:                                                                    # steam
        for k_ in range(2):
            u = (tt * 1.6 + k_ * 0.5) % 1
            p.ell(hx_ + (k_ * 2 - 1) * 40 * FSs, hy_ - (60 + 50 * u) * FSs, (8 + 14 * u) * FSs, (6 + 10 * u) * FSs, (255, 255, 255, int(200 * (1 - u))), None)
    # impact dust where the stick hits the desk
    if SLAM <= tt < SLAM + 0.4:
        u = kk(tt, SLAM, SLAM + 0.4); q = W2S(cam, 1078, 728)
        for k_ in range(6):
            a = k_ * math.pi / 3 + 0.3; p.ell(q[0] + math.cos(a) * 60 * u * z, q[1] + math.sin(a) * 25 * u * z, 10 * z * (1 - u) + 2, 6 * z * (1 - u) + 2, (230, 220, 200, int(220 * (1 - u))), None)
    lay = tint_layer(lay, (255, 240, 220)); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    series_tag(fr, tt, PANIC[0] + 0.1, PANIC[1] + 1.8)
    if SLAM <= tt < SLAM + 0.25:
        fr = Image.blend(fr, Image.new("RGB", fr.size, (255, 255, 255)), 0.35 * (1 - kk(tt, SLAM, SLAM + 0.25)))
    if SLAM <= tt < SLAM + 0.5: lzt(fr, W / 2 - 330, 230, "طـــاخ!", int(140 * popk(tt, SLAM, 0.15)), (255, 214, 90))
    if BEAT[0] <= tt < BEAT[0] + 0.7: fr = ImageEnhance.Color(fr).enhance(0.3)
    if BEAT[0] + 0.7 <= tt < LAUGH:
        q = W2S(cam, fx + 40, FY - 330); lzt(fr, q[0], q[1], "؟!", int(150 * popk(tt, BEAT[0] + 1.0)), (255, 214, 90))
    if laughing:
        for k_, (dx, dy, sz) in enumerate(((-560, -300, 110), (420, -360, 96), (-320, -120, 84), (600, -100, 100), (60, -420, 90), (-700, 40, 80))):
            t0_ = LAUGH + 0.2 + k_ * 0.3
            if tt >= t0_: lzt(fr, W / 2 + dx + math.sin(tt * 6 + k_) * 10, H / 2 + dy, "ههههه", int(sz * popk(tt, t0_)), (255, 214, 90))
        if tt >= FREEZE:
            fr = Image.blend(fr, Image.new("RGB", fr.size, (255, 255, 255)), 0.6 * (1 - kk(tt, FREEZE, FREEZE + 0.2)))
    return finish(fr, tt)

def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(44)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 400) * 0.02, 0, 1.0)
    mix_into(buf, SFXF["whoosh"] * 0.4, SLAM - 0.25, 1.0); mix_into(buf, SFXF["slam"] * 1.0, SLAM, 1.0)
    mix_into(buf, tone(60, 0.6, 0.6, 5), SLAM, 1.0)
    for k_ in range(4): mix_into(buf, SFXF["crinkle"] * 0.45, PANIC[0] + k_ * 0.4, 1.0)              # bags & pages
    mix_into(buf, SFXF["steps"] * 0.55, WALK[0] + 0.1, 1.0)
    mix_into(buf, SFXF["giggle"][:int(SR * 0.7)] * 0.2, NOD[0] + 0.1, 1.0)
    for k_ in range(6): mix_into(buf, tone(1500, 0.05, 0.25, 50) + tone(900, 0.05, 0.2, 50), NOD[0] + 0.15 + k_ * 0.11, 1.0)   # Tota claps
    for k_, f in enumerate((2637, 3520)): mix_into(buf, tone(f, 0.5, 0.12, 7), GLINT + k_ * 0.07, 1.0)                    # glint ✦
    b0 = BEAT[0]
    for k_ in range(3):
        ch_ = np.concatenate([tone(4300, 0.05, 0.12, 20), np.zeros(int(SR * 0.04), np.float32)] * 3); mix_into(buf, ch_, b0 + 0.1 + k_ * 0.32, 1.0)
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 0.5: mix_into(buf, SFXF["whoosh"] * 0.25, s_["start"] - 0.1, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), TOTAL - 2.4 + k_ * 0.09, 1.0)
    rms = lambda x: float(np.sqrt(np.mean(x ** 2))) + 1e-9
    ref = []
    for st, k in lines:
        if k == "GROUP": continue
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8; ref.append(rms(v)); mix_into(buf, v, st, 1.0)
    g = AUD["GROUP"]; mix_into(buf, g / rms(g) * float(np.mean(ref)) * 1.25, LAUGH, 1.0)
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
