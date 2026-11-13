# «يوميات شطة وزلطة» — الأرض لسه مبلولة  (H 1920x1080 + V 1080x1920 in one pass)
# render:  python ep.py audio  →  python ep.py part 0 2 & python ep.py part 1 2  →  concat  →  mux mix.wav
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/daily/05")
SERIES = "يوميات شطة وزلطة"; EPT = "الأرض لسه مبلولة"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"
SFXP = {"whoosh": "/trend/01/sfx/whoosh.mp3", "slipper": "/s2e1/sfx/slipper.mp3", "stinger": "/trend/01/sfx/stinger.mp3",
        "mop": "/daily/05/sfx/mop.mp3", "bucket": "/daily/05/sfx/bucket.mp3", "news": "/daily/05/sfx/news.mp3", "gasp": "/trend/01/sfx/gasp.mp3"}
SFXF = {n: load_audio(ROOT + p) for n, p in SFXP.items()}

SUB = {"A1": "إنت رايح فين يا راجل؟!", "B1": "هعدّي.", "A2": "إنت مش شايفني بنضّف وبمسح؟!",
       "B2": "خلاص… هعدّي، وبعدين امسحي تاني.", "A3": "ماشي… وريني كده هتعدّي إزاي.", "A4": "يا نهار أسود!!",
       "S1": "لايف! إحنا دلوقتي قدام عمارة نعناعة… قدام أوضة عم البواب ومراته خالتي عزيزة… بعد ما عم البواب اختفى… عشان بوّظ الأرض وهي بتمسح!",
       "S2": "يا حضرة الظابط… إنتوا لسه ما قبضتوش على عزيزة؟", "O1": "لسه.", "S3": "ليه لسه؟!", "O2": "مستنيين الأرض تنشف.", "GROUP": ""}
WHO = {"A1": "aziza", "A2": "aziza", "A3": "aziza", "A4": "aziza", "B1": "bondo2", "B2": "bondo2",
       "S1": "sawsan", "S2": "sawsan", "S3": "sawsan", "O1": "officer", "O2": "officer", "GROUP": "-"}
EXPR = {"A1": "angry", "A2": "angry", "A3": [(0, "flat"), (0.9, "smug")], "A4": "shout", "B1": "sleepy", "B2": "neutral",
        "S1": [(0, "happy"), (6.5, "shock"), (8.3, "happy")], "S2": "neutral", "S3": "shock", "O1": "flat", "O2": "scared", "GROUP": "laugh"}
load_lines(list(SUB))
LOBBY = _ld(ROOT + "/s1e10/bg/morning.png")        # canonical «مدخل العمارة» (docs/locations.md)
WALL = _ld(ROOT + "/s2e5/bg/wall.png")             # canonical «الحيطة من بره + شباك البدروم»

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear()
STEPS0 = 1.0                                          # slippers heard on the stairs (off-screen right)
shot("lobby", 0.0, 1.9, (860, 760, 1.55), (900, 740, 1.4))                                   # hook: she mops, the floor shines
ENTER = (1.9, 3.5); shot("lobby", 1.9, 3.6, (1120, 700, 1.15), (1080, 710, 1.25), tin="whip")   # Bandaq comes in from the stairs
t = 3.6
s = t; t = say(t, "A1") + 0.1; t = say(t + 0.05, "B1") + 0.1
shot("lobby", s, t, (1060, 730, 1.5), (1060, 730, 1.58))
s = t; t = say(t + 0.05, "A2") + 0.1
shot("lobby", s, t, (980, 720, 1.75), (960, 715, 1.9), tin="whipl")
s = t; t = say(t + 0.05, "B2") + 0.25; shot("lobby", s, t, (1090, 720, 1.65), (1100, 715, 1.75))
DUNK = t; s = t; t = say(t + 0.55, "A3") + 0.2
shot("lobby", s, t, (840, 690, 2.2), (840, 680, 2.65), tin="whipl")                        # the scary smile
STEP = t + 0.55; shot("lobby", t, t + 1.2, (1230, 900, 2.8), (1230, 920, 3.1), tin="whip"); t += 1.2   # slipper → black print
SCREAM = t; t = say(t + 0.05, "A4") + 0.25
shot("lobby", SCREAM, t, (840, 700, 1.8), (840, 680, 2.7), ease="crash"); shakes.append((SCREAM + 0.05, 34))
SWEAT = (t, t + 1.1); shot("lobby", t, t + 1.1, (1250, 690, 2.4), (1250, 700, 2.6), tin="whipl"); t += 1.1
NEXT = (t, t + 1.5); shot("black", t, t + 1.5, None); t += 1.5
LIVE0 = t
shot("wall", t, t + 1.3, (960, 640, 1.0), (920, 680, 1.15), tin="fade")
t += 1.3; s = t; t = say(t, "S1") + 0.15
shot("wall", s, s + 4.0, (900, 690, 1.45), (900, 680, 1.55))
shot("wall", s + 4.0, s + 7.6, (720, 640, 2.2), (720, 630, 2.45), tin="whipl")            # Sawsan to the lens: «اختفى…»
shot("wall", s + 7.6, t, (900, 690, 1.6), (900, 685, 1.7), tin="whip")
s = t; t = say(t + 0.05, "S2") + 0.1; t = say(t + 0.05, "O1") + 0.1; t = say(t + 0.05, "S3") + 0.15
shot("wall", s, t, (920, 680, 1.7), (920, 680, 1.8), tin="whip")
s = t; t = say(t + 0.35, "O2") + 0.2; GLANCE = s
shot("wall", s, t, (960, 660, 2.0), (960, 650, 2.35))
LOOKS = (t, t + 0.7); shot("wall", t, t + 0.7, (900, 680, 1.75), (900, 680, 1.78)); t += 0.7    # they look at each other…
LAUGH = t; LU = DUR["GROUP"]; say(LAUGH, "GROUP")
shot("wall", t, t + 2.4, (900, 680, 1.8), (900, 690, 1.55), tin="whip")
shot("wall", t + 2.4, t + LU + 0.2, (900, 670, 1.5), (900, 680, 1.35))
t += LU + 0.2; FREEZE = t - 0.25
shot("end", t, t + 2.6, None); t += 2.6
TOTAL = t

# ---------------- staging ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
AX, AY, AS = 820, 1040, 1.9          # Aziza
BX0, BX1, BXS, BY, BS = 2080, 1350, 1250, 1040, 1.9   # Bandaq: stairs side → stops → steps onto the wet floor
BUCKET = (1040, 1050)
SX, OX, WY, WS = 700, 1090, 1010, 1.6      # Sawsan / officer on the pavement

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, walk=None, hop=0.0):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    if talking and arms == "down": arms = "talk"
    blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11 and expr not in ("sleepy", "laugh")
    X, Y_ = W2S(cam, x, y - hop); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, None, lean, walk)
    return X, Y_, S * CH[who]["scale"]

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
os.chdir(ROOT + "/daily/05")
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

def bandaq_state(tt):
    """(x, walk, expr, arms)"""
    if tt < ENTER[0]: return None
    if tt < ENTER[1]:
        k = kk(tt, *ENTER); return lerp(BX0, BX1, ease(k) * 0.3 + k * 0.7), tt * 7, "sleepy", "down"
    if STEP - 0.45 <= tt < STEP:
        k = ease(kk(tt, STEP - 0.45, STEP)); return lerp(BX1, BXS, k), tt * 7, "neutral", "down"
    x = BX1 if tt < STEP else BXS
    if tt >= SCREAM: return x, None, "scared", "scared"
    if tt >= STEP: return x, None, "shock", "down"
    return x, None, "sleepy" if tt < ENTER[1] + 0.5 else "neutral", "down"

def wet_floor(p, cam, tt):
    """shiny wet tiles around Aziza (+ the slipper print once he steps)"""
    z = cam[2]
    for k_, (x, y, w) in enumerate(((620, 1045, 120), (760, 1062, 150), (930, 1050, 170), (1100, 1066, 150), (1230, 1048, 110), (860, 1075, 200))):
        q = W2S(cam, x, y); a = 120 + 45 * math.sin(tt * 2 + k_)
        p.ell(q[0], q[1], w * z, 9 * z, (255, 255, 255, int(a)), None)
    for k_ in range(5):                      # little twinkles
        u = (tt * 0.8 + k_ * 0.21) % 1
        if u < 0.25:
            q = W2S(cam, 640 + k_ * 140, 1040 + (k_ % 2) * 20); r = 12 * z * math.sin(u / 0.25 * math.pi)
            p.line([(q[0] - r, q[1]), (q[0] + r, q[1])], (255, 255, 255, 230), 2 * z); p.line([(q[0], q[1] - r), (q[0], q[1] + r)], (255, 255, 255, 230), 2 * z)
    if tt >= STEP and tt < NEXT[0]:
        q = W2S(cam, BXS - 12, 1046)
        p.ell(q[0], q[1], 30 * z, 11 * z, (40, 30, 26, 235), None); p.ell(q[0] - 28 * z, q[1] + 1 * z, 13 * z, 9 * z, (40, 30, 26, 235), None)
        for k_ in range(3): p.ell(q[0] + (k_ - 1) * 26 * z, q[1] - 16 * z, 4 * z, 3 * z, (40, 30, 26, 200), None)

def bucket(p, cam):
    z = cam[2]; q = W2S(cam, *BUCKET)
    p.poly([(q[0] - 46 * z, q[1] - 74 * z), (q[0] + 46 * z, q[1] - 74 * z), (q[0] + 36 * z, q[1]), (q[0] - 36 * z, q[1])], (150, 160, 170, 255), INK, 3 * z)
    p.ell(q[0], q[1] - 74 * z, 46 * z, 9 * z, (90, 140, 190, 255), INK, 2.5 * z)
    p.arc(q[0], q[1] - 74 * z, 40 * z, 40 * z, 200, 340, INK, 2.5 * z)

def mop(p, cam, tt, X, Y_, SC):
    """mop held in her right hand; swipes on the floor, dunks in the bucket, raised like a staff while she argues"""
    z = cam[2]; shy = Y_ - 134 * SC; hand = (X + 46 * SC, shy + 30 * SC)
    if tt < ENTER[0] + 0.6:                                 # mopping
        hx_, hy_ = W2S(cam, AX + 170 + math.sin(tt * 5.5) * 70, 1048)
    elif DUNK <= tt < DUNK + 0.7:                           # into the bucket — splash
        u = math.sin(kk(tt, DUNK, DUNK + 0.7) * math.pi); hx_, hy_ = W2S(cam, BUCKET[0] - 10, 1000 + 20 * u)
    elif SCREAM <= tt:                                      # dropped in shock
        hx_, hy_ = W2S(cam, AX + 220, 1055)
    else:                                                   # planted upright like a guard's staff
        hx_, hy_ = W2S(cam, AX + 190, 1052)
    dx, dy = hx_ - hand[0], hy_ - hand[1]; L = math.hypot(dx, dy) + 1e-6
    top = (hand[0] - dx / L * 22 * SC, hand[1] - dy / L * 22 * SC)
    p.line([top, (hx_, hy_)], (150, 100, 50, 255), 6 * z)
    for k_ in range(7):
        a = math.pi * (0.15 + k_ * 0.7 / 6); p.line([(hx_, hy_ - 6 * z), (hx_ + math.cos(a) * 34 * z * (1 if k_ % 2 else 0.8), hy_ - 6 * z + math.sin(a) * 22 * z)], (230, 225, 210, 255), 5 * z)
    return hand

def mic(p, hand, SC, ang):
    ex, ey = hand[0] + math.cos(ang) * 44 * SC, hand[1] + math.sin(ang) * 44 * SC
    p.line([hand, (ex, ey)], (30, 30, 36, 255), 7 * SC); p.ell(ex, ey, 11 * SC, 11 * SC, (70, 70, 80, 255), INK, 2 * SC)
    p.rect(hand[0] - 9 * SC + (ex - hand[0]) * 0.35, hand[1] - 9 * SC + (ey - hand[1]) * 0.35, hand[0] + 9 * SC + (ex - hand[0]) * 0.35, hand[1] + 7 * SC + (ey - hand[1]) * 0.35, (220, 40, 40, 255), INK, 1.5 * SC, 2 * SC)

def speed_lines(fr, tt, t0, cx, cy):
    k = 1 - kk(tt, t0 + 0.6, t0 + 1.4)
    if k <= 0: return fr
    lay = Image.new("RGBA", fr.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); r = random.Random(int(tt * 24))
    for i in range(70):
        a = r.uniform(0, 2 * math.pi); r0 = r.uniform(330, 470); r1 = 1400
        d.line([(cx + math.cos(a) * r0, cy + math.sin(a) * r0), (cx + math.cos(a) * r1, cy + math.sin(a) * r1)], fill=(20, 20, 20, int(170 * k)), width=r.randint(2, 7))
    fr = fr.convert("RGBA"); fr.alpha_composite(lay); return fr.convert("RGB")

def live_ui(fr, tt):
    d = ImageDraw.Draw(fr, "RGBA")
    blink = (tt * 1.6) % 1 < 0.6
    d.rounded_rectangle([60, 60, 300, 140], 18, fill=(220, 30, 40, 235))
    if blink: d.ellipse([84, 86, 112, 114], fill=(255, 255, 255, 255))
    lzt(fr, 200, 98, "لايف", 52, (255, 255, 255), (120, 10, 10))
    views = int(1200 + (tt - LIVE0) * 900 + (max(0, tt - LAUGH) ** 2) * 9000)
    d.rounded_rectangle([320, 60, 640, 140], 18, fill=(0, 0, 0, 150))
    lzt(fr, 480, 98, f"{views:,} مشاهد", 46, (255, 255, 255), (0, 0, 0))

# ---------------- frame ----------------
def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "end": return finish(endcard(tt, sh), tt)
    if sh["set"] == "black":
        fr = Image.new("RGB", (W, H), (8, 8, 10)); sc = popk(tt, sh["start"] + 0.2, 0.3)
        lzt(fr, W / 2, H / 2 - 20, "تاني يوم...", int(120 * sc), (255, 255, 255), (0, 0, 0))
        return finish(fr, tt)
    cam = cam_at(sh, tt); z = cam[2]
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    if sh["set"] == "lobby":
        img = bg_crop(LOBBY, cam)
        wet_floor(p, cam, tt); bucket(p, cam)
        # Aziza
        ex = "happy"; look = 0; arms = "hold"; hop = 0
        if tt >= STEPS0 + 0.3: ex, look = "flat", 1
        if tt >= ENTER[1]: ex = "angry"
        if STEP <= tt < SCREAM: ex = "shock"
        if tt >= SCREAM: arms = "up"
        if SWEAT[0] <= tt: ex = "angry"
        wob = math.sin(tt * 5.5) * 0.12 if tt < ENTER[0] + 0.6 else 0
        X, Y_, SC = person(lay, cam, "aziza", AX, AY, AS, tt, ex, look, arms, wob, None, 14 if SCREAM <= tt < SCREAM + 0.2 else 0)
        if arms == "hold": mop(p, cam, tt, X, Y_, SC)
        else:                                          # dropped on the floor when she screams
            a_, b_ = W2S(cam, AX + 40, 1060), W2S(cam, AX + 330, 1050)
            p.line([a_, b_], (150, 100, 50, 255), 6 * z)
            for k_ in range(7): p.line([b_, (b_[0] + 30 * z, b_[1] - 18 * z + k_ * 6 * z)], (230, 225, 210, 255), 5 * z)
        if DUNK <= tt < DUNK + 0.9:                   # splash drops
            u = kk(tt, DUNK + 0.25, DUNK + 0.9); q = W2S(cam, BUCKET[0], 970)
            for k_ in range(7):
                a = -math.pi * (0.15 + k_ * 0.7 / 6); r = 90 * u * z
                p.ell(q[0] + math.cos(a) * r, q[1] + math.sin(a) * r + 120 * u * u * z, 6 * z, 8 * z, (120, 180, 230, int(230 * (1 - u))), None)
        # Bandaq
        bs = bandaq_state(tt)
        if bs:
            bx, walk, bex, barms = bs
            BXs, BYs, BSs = person(lay, cam, "bondo2", bx, BY, BS, tt, bex, -1, barms, 0, walk, 0)
            if tt >= SCREAM:                          # sweat drops
                for k_ in range(3):
                    u = (tt * 1.4 + k_ * 0.33) % 1
                    p.ell(BXs + (k_ - 1) * 30 * BSs, BYs - 250 * BSs + u * 60 * BSs, 5 * BSs, 8 * BSs, (150, 200, 255, int(255 * (1 - u))), INK, 1.2 * BSs)
        tintc = (255, 236, 210)
        if DUNK + 0.3 <= tt < STEP + 0.3: tintc = (200, 190, 220)       # the room goes cold for the scary smile
    else:
        img = bg_crop(WALL, cam)
        laughing = tt >= LAUGH; lu = tt - LAUGH
        sex = "happy"; slook = 0; sarms = "hold"; hop = 0
        if tt >= T("S2") - 0.05: slook = 1; sarms = "point"
        if laughing: sex = "laugh"; sarms = "clap" if int(lu * 6) % 2 else "hips"; hop = abs(math.sin(lu * 8)) * 16; slook = 0
        if LOOKS[0] <= tt < LAUGH: sex = "flat"; slook = 1
        X, Y_, SC = person(lay, cam, "sawsan", SX, WY, WS, tt, sex, slook, sarms, -0.15 if laughing else 0, None, hop)
        shy = Y_ - 134 * SC
        if sarms == "hold": mic(p, (X + 46 * SC, shy + 30 * SC), SC, -1.75)
        elif sarms == "point": mic(p, (X + 84 * SC, shy - 6 * SC), SC, -0.15)
        oex = "flat"; olook = -1; oarms = "down"; ohop = 0
        if T("S2") <= tt: olook = -1
        if GLANCE <= tt < GLANCE + 0.45: olook = -1; oex = "scared"
        if GLANCE + 0.45 <= tt < LOOKS[0]: olook = 1 if (tt * 3) % 1 < 0.5 else -1
        if LOOKS[0] <= tt < LAUGH: oex = "flat"; olook = -1
        if laughing: oex = "laugh"; oarms = "hips"; ohop = abs(math.sin(lu * 7 + 1)) * 14; olook = 0
        OXs, OYs, OSs = person(lay, cam, "officer", OX, WY, WS, tt, oex, olook, oarms, 0.15 if laughing else (-0.2 if GLANCE <= tt < LOOKS[0] else 0), None, ohop)
        if GLANCE <= tt < LOOKS[0]:
            p.ell(OXs + 50 * OSs, OYs - 245 * OSs, 5 * OSs, 8 * OSs, (150, 200, 255, 255), INK, 1.2 * OSs)
        tintc = (255, 240, 220)
    lay = tint_layer(lay, tintc); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    # ---- overlays ----
    if sh["set"] == "lobby":
        series_tag(fr, tt, 0.3, 3.0)
        if STEPS0 <= tt < STEPS0 + 1.2:
            lzt(fr, W - 230, 300, "طق… طق…", int(70 * popk(tt, STEPS0)), (255, 255, 255))
        if STEP <= tt < STEP + 0.6:
            lzt(fr, W / 2 + 300, 330, "تششش!", int(110 * popk(tt, STEP, 0.15)), (255, 255, 255), (30, 20, 10))
        if SCREAM <= tt < SWEAT[0]:
            q = W2S(cam, AX, AY - 300); fr = speed_lines(fr, tt, SCREAM, q[0], q[1])
        if DUNK + 0.3 <= tt < STEP + 0.3: fr = ImageEnhance.Brightness(fr).enhance(0.85)
    else:
        live_ui(fr, tt)
        if laughing:
            for k_, (dx, dy, sz) in enumerate(((-560, -300, 110), (420, -360, 96), (-320, -120, 84), (600, -100, 100), (60, -420, 90))):
                t0_ = LAUGH + 0.2 + k_ * 0.3
                if tt >= t0_: lzt(fr, W / 2 + dx + math.sin(tt * 6 + k_) * 10, H / 2 + dy, "ههههه", int(sz * popk(tt, t0_)), (255, 214, 90))
            if tt >= FREEZE: fr = Image.blend(fr, Image.new("RGB", fr.size, (255, 255, 255)), 0.6 * (1 - kk(tt, FREEZE, FREEZE + 0.2)))
    return finish(fr, tt)

def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(45)
    mix_into(buf, lowpass(r.normal(0, 1, int(NEXT[0] * SR)).astype(np.float32), 300) * 0.02, 0, 1.0)             # lobby tone
    mix_into(buf, lowpass(r.normal(0, 1, int((TOTAL - LIVE0) * SR)).astype(np.float32), 900) * 0.025, LIVE0, 1.0)  # street
    mix_into(buf, SFXF["mop"][:int(SR * 2.4)] * 0.8, 0.0, 1.0)
    for k_ in range(4): mix_into(buf, SFXF["slipper"] * 0.6, STEPS0 + k_ * 0.38, 1.0)
    for k_ in range(4): mix_into(buf, SFXF["slipper"] * 0.75, ENTER[0] + 0.1 + k_ * 0.36, 1.0)
    mix_into(buf, SFXF["bucket"] * 1.0, DUNK + 0.2, 1.0)
    dr = np.arange(int(SR * (STEP + 0.2 - DUNK))) / SR                                                             # low tension drone
    mix_into(buf, (np.sin(2 * np.pi * 55 * dr) * 0.18 * np.minimum(1, dr / 0.6)).astype(np.float32), DUNK + 0.3, 1.0)
    mix_into(buf, SFXF["slipper"] * 1.0, STEP - 0.05, 1.0); mix_into(buf, tone(140, 0.4, 0.5, 8), STEP, 1.0)
    mix_into(buf, SFXF["stinger"] * 0.8, SCREAM, 1.0); mix_into(buf, tone(50, 1.0, 0.7, 3), SCREAM, 1.0)
    mix_into(buf, tone(180, 0.25, 0.35, 12), SWEAT[0] + 0.3, 1.0)                                                   # gulp
    for k_ in range(4): mix_into(buf, tone(2200, 0.03, 0.2, 80), NEXT[0] + 0.3 + k_ * 0.3, 1.0)                     # clock ticks
    mix_into(buf, SFXF["news"] * 0.7, LIVE0, 1.0)
    mix_into(buf, SFXF["gasp"] * 0.35, GLANCE, 1.0)
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
