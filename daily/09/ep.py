# «يوميات شطة وزلطة» — متسجّلة باسم إيه؟  (H 1920x1080 + V 1080x1920 in one pass) — first video on the Hook rule
# render:  python ep.py audio  →  python ep.py part 0 2 & python ep.py part 1 2  →  concat  →  mux mix.wav
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/daily/09")
SERIES = "يوميات شطة وزلطة"; EPT = "متسجّلة باسم إيه؟"
HOOK_TEXT = "البواب مسجّل مراته باسم إيه؟! 😂"
HOOK_DRAW = "البواب مسجّل مراته باسم إيه؟!"          # fonts have no emoji → on screen without it
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"
SFXP = {"whoosh": "/trend/01/sfx/whoosh.mp3", "steps": "/s2e1/sfx/footsteps.mp3"}
SFXF = {n: load_audio(ROOT + p) for n, p in SFXP.items()}

SUB = {"B1": "الحكومة؟!... يا نهار أبيض!", "B2": "أيوه يا فندم!... تحت أمر سيادتك يا فندم!",
       "A1": "سيادتك؟!... أنا الحكومة يا راجل؟!", "B3": "أصل إنتي اللي ماشية البيت كله... زي الحكومة بالظبط!",
       "A2": "وإيه كمان؟", "B4": "وكل أول شهر... بتاخدي المرتب كله!", "A3": "صح كلامك.",
       "B5": "طب وإنتي مسجلاني إيه؟", "A4": "المخدة... عشان عمرك ما بتقوم من عليها!", "B6": "منطقي.",
       "B2S": "أيوه يا فندم!", "GROUP": ""}
WHO = {k: ("aziza" if k[0] == "A" else "bondo2") for k in SUB}; WHO["GROUP"] = "-"
EXPR = {"B1": "shock", "B2": "scared", "A1": "angry", "B3": "happy", "A2": "smug", "B4": "happy", "A3": "smug",
        "B5": "smug", "A4": "flat", "B6": "sleepy", "B2S": "scared", "GROUP": "laugh"}
load_lines(list(SUB))
LOBBY = _ld(ROOT + "/s1e10/bg/morning.png")        # canonical «مدخل العمارة» (docs/locations.md)

# ---------------- timeline (Hook rule: ring at 0.0, first word at ~1.0 s, hook text from frame 1) ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
RING1 = (0.0, 1.05)
shot("phone", 0.0, 1.0, None, kind="gov")                                                   # insert: «📞 الحكومة» ringing
WAKE = 1.0
shot("lobby", 1.0, 1.55, (640, 760, 2.4), (640, 760, 2.55), tin="whip")                     # Bandaq asleep → eyes pop
STAND = 1.25
t = say(1.3, "B1") + 0.08
shot("lobby", 1.55, t, (960, 700, 1.75), (980, 690, 1.95), ease="crash"); shakes.append((1.3, 22))
PICK = t - 0.25
s = t; t = say(t + 0.05, "B2") + 0.15; shot("lobby", s, t, (990, 690, 1.9), (990, 680, 2.05))
s = t; t = say(t + 0.25, "A1") + 0.15                                                       # whip to Aziza on the stairs
shot("lobby", s, t, (1330, 640, 1.9), (1330, 630, 2.25), tin="whip")
FREEZE1 = t; t += 0.75                                                                      # Bandaq frozen, sweat drop, slow turn
shot("lobby", FREEZE1, t, (990, 650, 2.6), (990, 640, 3.0), ease="crash", tin="whipl")
WALKD = (t, t + 3.0)                                                                        # Aziza comes down the stairs during B3
s = t; t = say(t + 0.05, "B3") + 0.15; shot("lobby", s, t, (1180, 700, 1.35), (1160, 700, 1.5))
s = t; t = say(t + 0.05, "A2") + 0.1; shot("lobby", s, t, (1160, 720, 1.6), (1160, 720, 1.68))
s = t; t = say(t + 0.05, "B4") + 0.1; shot("lobby", s, t, (1080, 700, 1.75), (1080, 700, 1.9), tin="whipl")
s = t; t = say(t + 0.05, "A3") + 0.25; shot("lobby", s, t, (1290, 680, 2.0), (1290, 680, 2.1), tin="whip")
PEEK = t
s = t; t = say(t + 0.05, "B5") + 0.1; shot("lobby", s, t, (1160, 700, 1.6), (1160, 700, 1.72))
s = t; shot("phone", t, t + 1.3, None, kind="pillow", tin="zoom")                           # insert: «المخدة»
t = say(t + 0.3, "A4") + 0.1
shot("lobby", s + 1.3, t, (1260, 690, 1.9), (1260, 690, 2.05), tin="whip")
YAWN = t; t = say(t + 0.1, "B6") + 0.05; shot("lobby", YAWN, t + 1.0, (960, 720, 1.5), (780, 740, 1.75))
FLOP = t; t += 1.0                                                                          # flops back onto the dikka, snores
RING2 = t; shot("phone", t, t + 0.6, None, kind="gov", tin="flash"); t += 0.6
s = t; t = say(t + 0.05, "B2S") + 0.15; STAND2 = s
shot("lobby", s, t, (1100, 700, 1.4), (1100, 700, 1.5), ease="crash"); shakes.append((s, 22))
LAUGH = t; LU = DUR["GROUP"]; say(LAUGH, "GROUP")
shot("lobby", t, t + LU, (1120, 700, 1.4), (1120, 710, 1.3))
t += LU; FREEZE = t - 0.25
shot("end", t, t + 2.4, None); t += 2.4
TOTAL = t

# ---------------- staging (world = 1920x1080 lobby) ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
SEAT_Y, BX, BS = 905, 640, 1.9            # the dikka and Bandaq sitting on it (same as daily/06)
BSTX, BSTY, BSTS = 990, 1062, 1.8         # Bandaq standing in front of the dikka
AZ0 = (1430, 820, 1.35); AZ1 = (1330, 1055, 1.78)    # Aziza: on the stairs → by Bandaq

# arm schedule with smooth blends (new engine feature): list of (time, pose) per character
def arms_at(sched, tt, d=0.22):
    prev = sched[0][1]
    for i, (t0, pose) in enumerate(sched):
        if tt < t0: break
        if tt < t0 + d and i > 0: return (sched[i - 1][1], pose, (tt - t0) / d)
        prev = pose
    return prev

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, walk=None, hop=0.0, held=None):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11 and expr not in ("sleepy", "laugh")
    if not talking and walk is None: lean += math.sin(tt * 1.7 + hash(who) % 5) * 0.06            # idle weight shift
    X, Y_ = W2S(cam, x, y - hop); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, held, lean, walk)
    return X, Y_, S * CH[who]["scale"]

WOOD = (150, 98, 52, 255); WOOD_D = (110, 68, 34, 255)
def bench_front(p, cam):
    z = cam[2]; a = W2S(cam, 440, SEAT_Y - 12); b = W2S(cam, 880, SEAT_Y + 14)
    p.rect(a[0], a[1], b[0], b[1], (172, 116, 64, 255), INK, 3 * z, 4 * z)
    for xx in (470, 850):
        q = W2S(cam, xx, SEAT_Y + 14); q2 = W2S(cam, xx, 1046); p.rect(q[0] - 9 * z, q[1], q[0] + 9 * z, q2[1], WOOD_D, INK, 2.5 * z, 2 * z)
def bench_back(p, cam):
    z = cam[2]; a = W2S(cam, 440, SEAT_Y - 170); b = W2S(cam, 880, SEAT_Y - 120)
    p.rect(a[0], a[1], b[0], b[1], WOOD, INK, 3 * z, 3 * z)
    for xx in (460, 860):
        q = W2S(cam, xx, SEAT_Y - 170); p.line([q, (q[0], q[1] + 160 * z)], WOOD_D, 8 * z)
def shins(p, cam, x, s, swing=0.0):
    z = cam[2]; S = s * z
    for dx in (-18, 18):
        top = W2S(cam, x + dx * s, SEAT_Y + 14); fx = top[0] + (dx * 0.4 + swing * (1 if dx > 0 else -1)) * S
        bot = (fx, W2S(cam, 0, 1046)[1])
        p.line([top, bot], INK, max(3, 5 * S)); p.line([bot, (bot[0] - 12 * S, bot[1])], INK, max(3, 5 * S))
def bench_phone(p, cam, tt, ringing):
    z = cam[2]; jx = (math.sin(tt * 90) * 5 if ringing else 0) * z
    a = W2S(cam, 800, SEAT_Y - 16); p.rect(a[0] - 14 * z + jx, a[1] - 8 * z, a[0] + 14 * z + jx, a[1] + 4 * z, (30, 30, 36, 255), INK, 2 * z, 3 * z)
    if ringing: p.rect(a[0] - 10 * z + jx, a[1] - 6 * z, a[0] + 10 * z + jx, a[1] + 1 * z, (120, 255, 150, 255), None)

def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255, font=None):
    if size < 4: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(font or LZ, size)
    kw = dict(font=f, anchor="mm", direction="rtl", language="ar")
    d.text((x, y), s, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), **kw)
    d.text((x, y), s, fill=fill + (alpha,), **kw); img.paste(lay, (0, 0), lay)
def popk(tt, t0, d=0.22):
    u = kk(tt, t0, t0 + d); return 0 if u <= 0 else (1 + 0.25 * math.sin(u * math.pi)) if u < 1 else 1

_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/daily/09")
_FC = {}
def frame_cache(t_):
    if t_ not in _FC: _FC[t_] = frame(t_)
    return _FC[t_]
def endcard(tt, sh):
    k = kk(tt, sh["start"], sh["start"] + 0.4)
    fr = ImageEnhance.Brightness(frame_cache(FREEZE)).enhance(1 - 0.55 * k).filter(ImageFilter.GaussianBlur(6 * k)).convert("RGBA")
    sc = popk(tt, sh["start"] + 0.1, 0.3)
    if sc > 0:
        lzt(fr, W / 2, 400, "إنت مسجّلها/مسجّله باسم إيه؟", int(96 * sc), (255, 214, 90))
        d = ImageDraw.Draw(fr, "RGBA"); d.rounded_rectangle([W / 2 - 420, 500, W / 2 + 420, 580], 30, fill=(230, 120, 30, 230))
        lzt(fr, W / 2, 538, "اكتبها في الكومنتات بصراحة!", 54, (255, 255, 255))
    if tt >= sh["start"] + 0.6:
        logo(fr, W / 2, 760, 120); text(fr, W / 2, 900, "@shattawzalata", 50, (255, 214, 90))
    return fr.convert("RGB")

def phone_insert(tt, sh):
    """full-frame close-up of a ringing phone: kind 'gov' (Bandaq's phone: «الحكومة») / 'pillow' (Aziza's phone: «المخدة»)"""
    u = tt - sh["start"]; gov = sh["kind"] == "gov"
    bg = ImageEnhance.Brightness(LOBBY.resize((W, H)).filter(ImageFilter.GaussianBlur(14))).enhance(0.45).convert("RGBA")
    jx = math.sin(u * 95) * (10 if gov else 0); jy = math.cos(u * 77) * (4 if gov else 0)
    sc = 1.0 + 0.06 * ease(min(1, u / 0.6))
    pw, ph = 470 * sc, 900 * sc; cx, cy = W / 2 + jx, H / 2 + 20 + jy
    d = ImageDraw.Draw(bg, "RGBA")
    if gov:                                                                      # vibration lines
        for side in (-1, 1):
            for i in range(3):
                x_ = cx + side * (pw / 2 + 30 + i * 26); a_ = int(200 * abs(math.sin(u * 14 + i)))
                d.arc([x_ - 30, cy - 80 - i * 20, x_ + 30, cy + 80 + i * 20], 300 if side > 0 else 120, 60 if side > 0 else 240, fill=(255, 255, 255, a_), width=6)
    d.rounded_rectangle([cx - pw / 2, cy - ph / 2, cx + pw / 2, cy + ph / 2], 70, fill=(22, 22, 28, 255), outline=(10, 10, 10, 255), width=8)
    scr = (40, 120, 70) if gov else (60, 50, 110)
    d.rounded_rectangle([cx - pw / 2 + 22, cy - ph / 2 + 22, cx + pw / 2 - 22, cy + ph / 2 - 22], 52, fill=scr + (255,))
    d.rounded_rectangle([cx - 60, cy - ph / 2 + 34, cx + 60, cy - ph / 2 + 58], 12, fill=(10, 10, 12, 255))
    bgr = bg.convert("RGB")
    lzt(bgr, cx, cy - 260 * sc, "مكالمة واردة..." if gov else "جهات الاتصال", int(46 * sc), (230, 230, 230), (20, 20, 20))
    r = 110 * sc * (1 + (0.06 * math.sin(u * 12) if gov else 0))
    d = ImageDraw.Draw(bgr, "RGBA"); d.ellipse([cx - r, cy - 120 * sc - r, cx + r, cy - 120 * sc + r], fill=(235, 235, 240, 255), outline=(20, 20, 20, 255), width=6)
    if gov:                                                                      # official badge/eagle-ish emblem
        d.polygon([(cx, cy - 200 * sc), (cx + 60 * sc, cy - 150 * sc), (cx + 40 * sc, cy - 60 * sc), (cx - 40 * sc, cy - 60 * sc), (cx - 60 * sc, cy - 150 * sc)], fill=(200, 160, 50, 255), outline=(20, 20, 20, 255))
        lzt(bgr, cx, cy - 128 * sc, "!", int(90 * sc), (120, 20, 20), (240, 220, 160))
    else:
        d.rounded_rectangle([cx - 70 * sc, cy - 150 * sc, cx + 70 * sc, cy - 90 * sc], 26, fill=(250, 250, 250, 255), outline=(20, 20, 20, 255), width=5)
        lzt(bgr, cx + 40 * sc, cy - 190 * sc, "z", int(50 * sc), (120, 140, 255), (20, 20, 40), font=ROOT + "/brand/fonts/DejaVuSans-Bold.ttf")
        lzt(bgr, cx + 70 * sc, cy - 225 * sc, "Z", int(64 * sc), (120, 140, 255), (20, 20, 40), font=ROOT + "/brand/fonts/DejaVuSans-Bold.ttf")
    name = "الحكومة" if gov else "المخدة"
    lzt(bgr, cx, cy + 60 * sc, name, int(130 * sc * popk(tt, sh["start"] + (0.0 if gov else 0.25), 0.3)), (255, 255, 255), (20, 20, 20))
    if not gov: lzt(bgr, cx, cy + 170 * sc, "(جوزي)", int(52 * sc), (200, 200, 230), (20, 20, 20))
    d = ImageDraw.Draw(bgr, "RGBA")
    for dx, col in ((-110, (220, 50, 50)), (110, (50, 200, 90))):
        if gov or dx > 0:
            q = (cx + dx * sc, cy + 300 * sc); rr = 52 * sc; d.ellipse([q[0] - rr, q[1] - rr, q[0] + rr, q[1] + rr], fill=col + (255,))
    return bgr

def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "end": return finish(endcard(tt, sh), tt)
    if sh["set"] == "phone": return finish(hook_overlay(phone_insert(tt, sh), tt), tt)
    cam = cam_at(sh, tt); z = cam[2]
    img = bg_crop(LOBBY, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    laughing = tt >= LAUGH; lu = tt - LAUGH
    bench_back(p, cam)
    # ---- Bandaq state: asleep (sitting) → stands → … → flops back asleep → jumps up again
    sitting = tt < STAND or FLOP + 0.35 <= tt < STAND2
    bex = "sleepy"; blook = 0; blean = 0; held = None; hop = 0
    barms = arms_at([(0, "down"), (STAND + 0.05, "salute"), (PICK, "phonesal"), (FREEZE1 + 0.4, "phone"), (T("B3"), "clap"),
                     (T("A2"), "down"), (T("B4"), "talk"), (T("A3"), "down"), (PEEK, "point"), (T("A4") - 0.3, "down"),
                     (STAND2 + 0.05, "phonesal"), (LAUGH + 0.8, "salute")], tt)
    if tt >= PICK and tt < T("B3") or tt >= STAND2: held = "phone"
    if WAKE <= tt < STAND: bex = "shock"
    if STAND <= tt < STAND + 0.3: hop = math.sin((tt - STAND) / 0.3 * math.pi) * 40
    if FREEZE1 <= tt < T("B3"): bex = "scared"; blook = 1
    if T("B3") <= tt < FLOP: blook = 1 if tt < PEEK else 1
    if PEEK <= tt < T("A4"): blean = 0.35; bex = "smug"
    if T("A4") <= tt < YAWN: bex = "flat"
    if YAWN <= tt: bex = "sleepy"
    if STAND2 <= tt: bex = "scared"; blook = 0
    if STAND2 <= tt < STAND2 + 0.3: hop = math.sin((tt - STAND2) / 0.3 * math.pi) * 40
    if sitting:
        sag = 5 * math.sin(tt * 1.3)
        person(lay, cam, "bondo2", BX, SEAT_Y + 62 * BS + sag, BS, tt, "sleepy" if tt < WAKE or tt >= FLOP else bex, 0, "down", 0.15)
        bench_front(p, cam); shins(p, cam, BX, BS)
        bench_phone(p, cam, tt, tt < RING1[1] or (RING2 - 0.6 <= tt < STAND2 and False))
    else:
        bench_front(p, cam)
        if tt < PICK: bench_phone(p, cam, tt, True)
        k_fl = kk(tt, FLOP, FLOP + 0.35) if FLOP <= tt < STAND2 else 0
        yb = lerp(BSTY, SEAT_Y + 62 * BS, ease(k_fl)); xb = lerp(BSTX, BX, ease(k_fl))
        BXs, BYs, BSs = person(lay, cam, "bondo2", xb, yb, BSTS, tt, bex, blook, barms, blean, None, hop, held)
        if FREEZE1 <= tt < T("B3") + 0.6:                                             # sweat drop
            u = kk(tt, FREEZE1 + 0.15, FREEZE1 + 1.1); hx, hy = BXs + 40 * BSs, BYs - 200 * BSs
            p.ell(hx, hy + u * 50 * BSs, 6 * BSs, 10 * BSs, (140, 200, 255, 255), INK, 1.5 * BSs)
    # ---- Aziza: on the stairs with her phone → walks down during B3 → by Bandaq
    if tt >= T("A1") - 0.3:
        k = kk(tt, *WALKD); e = ease(k)
        ax, ay, as_ = lerp(AZ0[0], AZ1[0], e), lerp(AZ0[1], AZ1[1], e), lerp(AZ0[2], AZ1[2], e)
        walk = tt * 7 if 0 < k < 1 else None
        aex = "angry"; alook = -1
        aarms = arms_at([(0, "phone"), (WALKD[0] + 0.2, "hips"), (T("A2"), "down"), (T("A3"), "hips"), (T("B5") + 0.3, "phone"),
                         (T("A4") + DUR["A4"], "hips"), (STAND2, "hips"), (LAUGH + 0.3, "shush")], tt)
        if T("B3") <= tt < T("A2"): aex = "smug"
        if T("A2") <= tt < T("B4"): aex = "happy"
        if T("B4") <= tt < T("B5"): aex = "smug"
        if T("B5") <= tt < YAWN: aex = "flat"
        if YAWN <= tt: aex = "angry" if tt < STAND2 else "flat"
        aheld = "phone" if tt < WALKD[0] + 0.2 or T("B5") + 0.3 <= tt < T("A4") + DUR["A4"] else None
        person(lay, cam, "aziza", ax, ay, as_, tt, aex, alook, aarms, 0, walk, 0, aheld)
    lay = tint_layer(lay, (255, 236, 210)); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    # ---- overlays
    if tt < WAKE + 0.5 or FLOP + 0.4 <= tt < RING2:                                    # Zzz
        for k_ in range(3):
            u = ((tt * 0.8) + k_ / 3) % 1; q = W2S(cam, BX + 90 + u * 120, SEAT_Y - 330 - u * 160)
            lzt(fr, q[0], q[1], "Z", int((40 + 30 * u) * z / 1.8), (180, 200, 255), font=ROOT + "/brand/fonts/DejaVuSans-Bold.ttf", alpha=int(255 * (1 - u)))
    if WAKE <= tt < WAKE + 0.5:
        lzt(fr, W * 0.7, H * 0.3, "!!", int(160 * popk(tt, WAKE)), (255, 80, 60))
    if laughing:
        for k_, (dx, dy, sz) in enumerate(((-560, -300, 110), (420, -360, 96), (600, -100, 100), (60, -420, 90))):
            t0_ = LAUGH + 0.2 + k_ * 0.3
            if tt >= t0_: lzt(fr, W / 2 + dx + math.sin(tt * 6 + k_) * 10, H / 2 + dy, "ههههه", int(sz * popk(tt, t0_)), (255, 214, 90))
        if tt >= FREEZE: fr = Image.blend(fr, Image.new("RGB", fr.size, (255, 255, 255)), 0.6 * (1 - kk(tt, FREEZE, FREEZE + 0.2)))
    return finish(hook_overlay(fr, tt), tt)

def hook_overlay(fr, tt):
    """HOOK_TEXT banner on the horizontal picture for the first 3.2 s (the vertical band carries it all the time)"""
    if tt >= 3.2: return fr
    a = int(255 * min(1, (3.2 - tt) / 0.3))
    d = ImageDraw.Draw(fr, "RGBA"); d.rounded_rectangle([W / 2 - 640, 40, W / 2 + 640, 150], 30, fill=(20, 12, 8, int(a * 0.8)))
    lzt(fr, W / 2, 95, HOOK_DRAW, 74, (255, 214, 90), alpha=a)
    return fr

def vertical(fr, tt):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = ImageEnhance.Brightness(small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.35)
    bgv.paste(fr.resize((1080, 608), Image.LANCZOS), (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(255, 214, 90)); d.rectangle([0, 1168, 1080, 1171], fill=(255, 214, 90))
    lzt(bgv, 540, 250, "البواب مسجّل مراته", 96, (255, 214, 90))
    lzt(bgv, 540, 390, "باسم إيه؟!", 120, (255, 255, 255))
    lzt(bgv, 540, 1840, SERIES, 44, (255, 150, 110))
    k, _ = line_at(tt)
    if k and SUB.get(k):
        ls_ = wrap(SUB[k])
        for i, l in enumerate(ls_[:4]): text(bgv, 540, 1290 + i * 80, l, 60, sw=6)
    return bgv

def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def ring(dur):
    d_ = np.arange(int(SR * dur)) / SR
    gate = ((d_ * 10) % 1 < 0.5).astype(np.float32) * ((d_ % 1.2) < 0.9)
    s_ = (np.sin(2 * np.pi * 1320 * d_) + 0.7 * np.sin(2 * np.pi * 1650 * d_)) * gate * 0.16
    buzz = np.sign(np.sin(2 * np.pi * 150 * d_)) * 0.05 * gate
    return (s_ + buzz).astype(np.float32)
def snore(dur):
    r = np.random.default_rng(5); n = int(SR * dur); d_ = np.arange(n) / SR
    env = np.clip(np.sin(2 * np.pi * d_ / 1.6), 0, 1) ** 2
    return (lowpass(r.normal(0, 1, n).astype(np.float32), 220) * env * 0.6 * (1 + 0.5 * np.sin(2 * np.pi * 38 * d_))).astype(np.float32)
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(46)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 300) * 0.02, 0, 1.0)
    mix_into(buf, ring(RING1[1] + 0.25), 0.0, 1.0)
    mix_into(buf, snore(1.0), 0.0, 0.5)
    mix_into(buf, tone(220, 0.3, 0.4, 14) + tone(110, 0.3, 0.4, 10), STAND, 1.0)          # jump-up thump
    mix_into(buf, tone(1900, 0.08, 0.15, 30), FREEZE1 + 0.15, 1.0)                        # sweat "ting"
    mix_into(buf, SFXF["steps"][:int(SR * 3.0)] * 0.45, WALKD[0], 1.0)
    mix_into(buf, snore(RING2 - FLOP - 0.4), FLOP + 0.4, 1.0)
    mix_into(buf, ring(0.75), RING2 - 0.05, 1.0)
    mix_into(buf, tone(220, 0.3, 0.4, 14) + tone(110, 0.3, 0.4, 10), STAND2, 1.0)
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 0.5: mix_into(buf, SFXF["whoosh"] * 0.25, s_["start"] - 0.1, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), TOTAL - 2.3 + k_ * 0.09, 1.0)
    rms = lambda x: float(np.sqrt(np.mean(x ** 2))) + 1e-9
    ref = []
    for st, k in lines:
        if k == "GROUP": continue
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8; ref.append(rms(v)); mix_into(buf, v, st, 1.0)
    g = AUD["GROUP"]; mix_into(buf, g / rms(g) * float(np.mean(ref)) * 1.2, LAUGH, 1.0)
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
