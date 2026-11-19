# «مين الكداب؟» — القضية 6: مين كسر شباك عزيزة؟  (H 1920x1080 + V 1080x1920 in one pass)
# Narrator = Tota (back to innocent). Location: «أوضة بندق وعزيزة» (day) — its window (top-right of the bg) is now broken.
# Clue: ALL the glass fell OUTSIDE (outer ledge + the street pavement), the inside sill/floor is clean → it was broken from
#   INSIDE. Aziza says the thief broke it from outside and jumped in → she lies (she wants a new bangle). Red herrings:
#   Shatta's football, Zalata's wooden ladder. Never pointed at.
# ANSWER (say it at the END of case 7): عزيزة — broke it from inside with her slipper so Bandaq buys her a new bangle.
# Case-5 answer told at the end here (A1): Tota — «عم بندء» in her notebook = same mistake as the letter.
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/kaddab/06")
SERIES = "مين الكداب؟"; EPT = "مين كسر الشباك؟"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"; DJ = ROOT + "/brand/fonts/DejaVuSans-Bold.ttf"
SFXF = {"whoosh": load_audio(ROOT + "/trend/01/sfx/whoosh.mp3"), "sting": load_audio(ROOT + "/trend/01/sfx/stinger.mp3"),
        "gasp": load_audio(ROOT + "/trend/01/sfx/gasp.mp3")}

SUB = {"AZ1": "الحقوني! حرامي كسر الشباك... ونط جوه وسرق غويشتي الدهب!",
       "B1": "غويشتك يا عزيزة؟! دي اللي كنتي بتقولي إمبارح إنها بقت قديمة؟",
       "N1": "الشباك اتكسر بعد الضهر... والمتهمين تلاتة!",
       "S1": "أنا كنت بلعب كورة تحت... بس والله الكورة كانت بعيد عن الشباك خالص!",
       "Z1": "أنا كنت في المدخل بصلّح النور!",
       "AZ2": "الحرامي جه من بره... كسر الإزاز بإيده ودخل!",
       "N2": "مين فيهم الكداب؟ شطة بالكورة؟ ولا زلطة بالسلم؟ ولا حد تاني خالص؟ ركزوا في الصورة... واكتبوا في الكومنتات!",
       "A1": "وحل الفزورة اللي فاتت: الكدابة كانت أنا! عشان اسم عم بندق في كشكولي مكتوب غلط... زي الجواب بالظبط!",
       "C1": "ولو ما شفتوش الحلقة اللي فاتت... شوفوها! وما تنسوش اللايك والفولو والشير!", "LAUGH": ""}
WHO = {"AZ1": "aziza", "B1": "bondo2", "N1": "tota", "S1": "shatta", "Z1": "zalata", "AZ2": "aziza", "N2": "tota", "A1": "tota",
       "C1": "nana", "LAUGH": "-"}
EXPR = {"AZ1": "shout", "B1": "scared", "N1": "smug", "S1": "scared", "Z1": "smug", "AZ2": "sad", "N2": "smug", "A1": "happy",
        "C1": "happy", "LAUGH": "laugh"}
load_lines(list(SUB))
ROOM = _ld(ROOT + "/daily/bg/bandaq_room.png")
STREET = _ld(ROOT + "/s2e3/bg/street_day.png")
COVER5 = Image.open(ROOT + "/publish/thumbs/kaddab_e05_cover.jpg").convert("RGB")
PINK = (226, 70, 150)
GLASS = (205, 232, 245)

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
WIDE = (960, 640, 1.2)
CRASH = 0.0
t = say(0.35, "AZ1"); shakes.append((0.05, 18)); a = T("AZ1")
shot("win", 0.0, 0.35, None, tin="flash")                                                    # glass shatters (insert)
shot("room", 0.35, a + 1.3, (1450, 700, 2.6), (1450, 705, 2.35), ease="crash")              # CU Aziza screaming
WIN1 = a + 1.3; shot("win", WIN1, a + 2.75, None, tin="zoom")                                 # «كسر الشباك» → the window
shot("room", a + 2.75, t + 0.1, (1450, 700, 2.45), (1450, 708, 2.6), tin="whip")
t += 0.1
s = t; t = say(t + 0.05, "B1") + 0.1; shot("room", s, t, (1180, 715, 2.4), (1180, 708, 2.55), tin="whipl")     # Bandaq doubts
GLARE = t; shakes.append((GLARE + 0.1, 14)); shot("room", t, t + 0.75, (1450, 700, 2.5), (1450, 690, 2.85), tin="whip", ease="crash")
LAUGH0 = t + 0.25; say(LAUGH0, "LAUGH"); t += 0.75
n1 = say(t + 0.1, "N1"); N1 = T("N1")
shot("room", t, N1 + 2.0, (420, 770, 2.4), (420, 762, 2.55), tin="whipl")                     # Tota the detective, magnifier
LINEUP = N1 + 2.0; shot("room", LINEUP, n1 + 0.2, WIDE, (960, 650, 1.28), tin="whipl")       # «والمتهمين تلاتة!»
t = n1 + 0.2
s = t; t = say(t + 0.05, "S1") + 0.1; shot("room", s, t, (640, 715, 2.35), (640, 708, 2.5), tin="whipl")        # Shatta + ball
s = t; t = say(t + 0.05, "Z1") + 0.15; shot("room", s, t, (900, 700, 2.3), (900, 695, 2.45), tin="whip")        # Zalata + ladder
s = t; t = say(t + 0.05, "AZ2") + 0.1; a2 = T("AZ2")
shot("room", s, a2 + 2.9, (1450, 715, 2.4), (1450, 708, 2.6), tin="whip")                     # Aziza (liar), fake tears
STREET1 = a2 + 2.9; shot("street", STREET1, a2 + 4.1, (960, 790, 1.9), (960, 805, 2.05), tin="whip")   # the clue — 1.2 s
shot("room", a2 + 4.1, t, (1450, 715, 2.5), (1450, 708, 2.6), tin="whip")
ASK = t; n2 = say(t + 0.05, "N2"); a = T("N2")
shot("room", ASK, a + 1.0, (420, 770, 2.4), (420, 762, 2.6), tin="whip")
shot("room", a + 1.0, a + 5.9, WIDE, (960, 650, 1.3), tin="whipl")                          # 1 ball… 2 ladder… 3 someone else
REPRISE = a + 5.9; shot("win2", REPRISE, a + 7.3, None, tin="zoom")                          # «ركزوا في الصورة» — magnifier on the window
shot("room", a + 7.3, n2 + 0.3, WIDE, (960, 650, 1.28), tin="whip")
t = n2 + 0.3
Q = t; shot("q", t, t + 1.3, None); t += 1.3
ANS = t; t = say(t + 0.25, "A1") + 0.35; shot("ans", ANS, t, None, tin="flash")
CTA = t; t = say(t + 0.15, "C1") + 0.8; shot("cta", CTA, t, None, tin="whip")
TOTAL = t
LAUGH_D = 1.3

# ---------------- staging (world = room 1920x1080) ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
POS = {"tota": (360, 1025, 1.9), "shatta": (640, 1010, 1.7), "zalata": (900, 1010, 1.7), "bondo2": (1180, 1012, 1.7),
       "aziza": (1450, 1012, 1.75)}
NUMS = (("shatta", (230, 90, 40)), ("zalata", (60, 150, 80)), ("aziza", (196, 40, 96)))

def body(who, x, y, s):
    S = s * CH[who]["scale"]; sh = y - 134 * S; return S, sh, (x, sh - 56 * S)
def hand(who, x, y, s, arms, side):
    S, sh, _ = body(who, x, y, s)
    A = {"down": ((x - 34 * S, sh + 72 * S), (x + 34 * S, sh + 72 * S)), "talk": ((x - 50 * S, sh + 52 * S), (x + 60 * S, sh + 8 * S)),
         "hold": ((x - 36 * S, sh + 70 * S), (x + 46 * S, sh + 30 * S)), "up": ((x - 70 * S, sh - 50 * S), (x + 70 * S, sh - 50 * S)),
         "hips": ((x - 48 * S, sh + 40 * S), (x + 48 * S, sh + 40 * S)), "point": ((x - 38 * S, sh + 68 * S), (x + 84 * S, sh - 6 * S))}
    return A.get(arms, A["down"])[0 if side < 0 else 1]

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, held=None):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    blink = ((tt + len(who) * 0.37) % 3.6) < 0.11 and expr not in ("laugh", "scared", "shout")
    if not talking: lean += math.sin(tt * 1.7 + len(who)) * 0.05
    X, Y_ = W2S(cam, x, y); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, held, lean, None)

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
os.chdir(ROOT + "/kaddab/06")

# ---------------- props ----------------
def slipper(p, x, y, s, rot=0.0):
    c, sn = math.cos(rot), math.sin(rot); R = lambda dx, dy: (x + dx * c - dy * sn, y + dx * sn + dy * c)
    sole = [R(13 * s * math.cos(a_ / 16 * 2 * math.pi), 27 * s * math.sin(a_ / 16 * 2 * math.pi)) for a_ in range(16)]
    p.poly(sole, (70, 150, 210, 255), INK, 2 * s)
    p.poly([R(-14 * s, -10 * s), R(14 * s, -10 * s), R(11 * s, 4 * s), R(-11 * s, 4 * s)], (240, 240, 240, 255), INK, 1.5 * s)

def football(p, x, y, r, rot=0.0):
    p.ell(x, y, r, r, (250, 250, 250, 255), INK, max(1.5, r * 0.12))
    p.poly([(x + r * 0.42 * math.cos(rot + i * 1.2566), y + r * 0.42 * math.sin(rot + i * 1.2566)) for i in range(5)], (30, 30, 34, 255), None)
    for i in range(5):
        a_ = rot + i * 1.2566 + 0.628; cx, cy = x + r * 0.86 * math.cos(a_), y + r * 0.86 * math.sin(a_)
        p.ell(cx, cy, r * 0.17, r * 0.17, (30, 30, 34, 255), None)

def ladder(p, x0, y0, x1, y1, w):
    """wooden ladder from foot (x0,y0) to top (x1,y1), width w (screen px)"""
    dx, dy = x1 - x0, y1 - y0; L = math.hypot(dx, dy); nx, ny = -dy / L * w / 2, dx / L * w / 2
    wood, dark = (168, 112, 58, 255), (96, 60, 28, 255)
    for k in range(1, 9):
        u = k / 9; cx, cy = x0 + dx * u, y0 + dy * u; p.line([(cx - nx, cy - ny), (cx + nx, cy + ny)], wood, w * 0.13)
    for sgn in (-1, 1): p.line([(x0 + sgn * nx, y0 + sgn * ny), (x1 + sgn * nx, y1 + sgn * ny)], dark, w * 0.2)
    for sgn in (-1, 1): p.line([(x0 + sgn * nx * 0.9, y0 + sgn * ny * 0.9), (x1 + sgn * nx * 0.9, y1 + sgn * ny * 0.9)], wood, w * 0.12)

def magnifier(p, x, y, s):
    p.line([(x, y), (x + 14 * s, y - 26 * s)], (90, 60, 30, 255), 6 * s)
    p.ell(x + 22 * s, y - 42 * s, 17 * s, 17 * s, (200, 230, 255, 120), (40, 40, 46, 255), 4 * s)

def broken_room_window(fr, cam):
    """the room bg's own window (world ≈ x1842-1920, y0-182) gets a star hole + cracks — same place, now broken"""
    d = ImageDraw.Draw(fr, "RGBA"); cx, cy = W2S(cam, 1880, 120); z = cam[2]
    if cx < -200 or cy > H + 200: return
    rr = random.Random(6)
    hole = [(cx + (14 + rr.random() * 16) * z * math.cos(i * 0.52), cy + (14 + rr.random() * 16) * z * math.sin(i * 0.52)) for i in range(12)]
    d.polygon(hole, fill=(255, 238, 200, 230), outline=(60, 50, 40, 255))
    for i in range(9):
        a_ = i * 0.7 + rr.random() * 0.3; L = (30 + rr.random() * 40) * z
        d.line([(cx, cy), (cx + L * math.cos(a_), cy + L * math.sin(a_))], fill=(70, 60, 50, 220), width=max(1, int(1.4 * z)))

# ---------------- inserts ----------------
def shard(d, x, y, r, rot, a=255):
    pts = [(x + r * math.cos(rot), y + r * math.sin(rot)), (x + r * 0.5 * math.cos(rot + 2.2), y + r * 0.5 * math.sin(rot + 2.2)),
           (x + r * 0.8 * math.cos(rot + 3.7), y + r * 0.8 * math.sin(rot + 3.7))]
    d.polygon(pts, fill=GLASS + (a,), outline=(120, 150, 170, a))
    d.line([pts[0], pts[1]], fill=(255, 255, 255, a), width=2)

def make_window(w=W, h=H):
    """CU of the room window from INSIDE: wood frame + iron grille like the bg, palm outside, lower-left pane smashed.
       Outside ledge covered with glass; the inside sill + floor edge are clean."""
    im = Image.new("RGB", (w, h), (226, 206, 168)); d = ImageDraw.Draw(im, "RGBA")
    for y in range(h): d.line([(0, y), (w, y)], fill=(232 - y // 30, 212 - y // 28, 172 - y // 26))
    X0, Y0, X1, Y1 = 520, 60, 1400, 820
    # outside view
    for y in range(Y0, Y1):
        k = (y - Y0) / (Y1 - Y0); d.line([(X0, y), (X1, y)], fill=(int(252 - 20 * k), int(226 - 40 * k), int(170 - 50 * k)))
    d.rectangle([X0, 520, X1, Y1], fill=(214, 176, 120))                                  # opposite building
    for i in range(5): d.rectangle([X0 + 40 + i * 180, 570, X0 + 130 + i * 180, 700], fill=(150, 112, 70))
    for i in range(9):                                                                     # palm
        a_ = math.radians(200 + i * 18); d.line([(1150, 300), (1150 + 230 * math.cos(a_), 300 + 120 * math.sin(a_) + 60)], fill=(110, 112, 70), width=26)
    d.line([(1150, 300), (1170, 560)], fill=(120, 96, 64), width=26)
    # OUTSIDE ledge (beyond the glass) with shards
    d.rectangle([X0, Y1 - 70, X1, Y1], fill=(196, 176, 140)); d.line([(X0, Y1 - 70), (X1, Y1 - 70)], fill=(150, 130, 100), width=4)
    rr = random.Random(11)
    for i in range(46): shard(d, X0 + 40 + rr.random() * (X1 - X0 - 80), Y1 - 60 + rr.random() * 50, 10 + rr.random() * 18, rr.random() * 6.28)
    # glass panes (tint) except the smashed one
    panes = [(X0, Y0, (X0 + X1) // 2, 440), ((X0 + X1) // 2, Y0, X1, 440), (X0, 440, (X0 + X1) // 2, Y1), ((X0 + X1) // 2, 440, X1, Y1)]
    for i, (a0, b0, a1, b1) in enumerate(panes):
        if i == 2:
            cx, cy = (a0 + a1) / 2, (b0 + b1) / 2; ring = []
            for j in range(18):
                ang = j / 18 * 6.283; rad = 120 + rr.random() * 90
                ring.append((cx + rad * math.cos(ang), cy + rad * 0.8 * math.sin(ang)))
            ov = Image.new("RGBA", (w, h), (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
            od.rectangle([a0, b0, a1, b1], fill=GLASS + (70,)); od.polygon(ring, fill=(0, 0, 0, 0))
            im.paste(ov, (0, 0), ov); d = ImageDraw.Draw(im, "RGBA")
            for j, q in enumerate(ring):                                                     # jagged edge + cracks to the frame
                d.line([q, ring[(j + 1) % len(ring)]], fill=(90, 120, 140, 255), width=4)
                if j % 2 == 0:
                    ang = j / 18 * 6.283; d.line([q, (cx + 520 * math.cos(ang), cy + 420 * math.sin(ang))], fill=(110, 140, 160, 200), width=3)
        else:
            d.rectangle([a0, b0, a1, b1], fill=GLASS + (60,))
            d.line([(a0 + 40, b1 - 60), (a0 + 160, b0 + 50)], fill=(255, 255, 255, 120), width=10)
    # iron grille (curls like the bg window)
    for x in (X0 + 220, X0 + 440, X0 + 660): d.line([(x, Y0), (x, Y1)], fill=(36, 30, 26), width=12)
    d.line([(X0, 300), (X1, 300)], fill=(36, 30, 26), width=12)
    for x in (X0 + 110, X0 + 330, X0 + 550, X0 + 770):
        d.arc([x - 70, Y0 + 20, x + 70, Y0 + 160], 20, 340, fill=(36, 30, 26), width=10)
        d.arc([x - 40, Y0 + 150, x + 40, Y0 + 260], 200, 160, fill=(36, 30, 26), width=9)
    # wood frame + mullions
    d.rectangle([X0 - 40, Y0 - 40, X1 + 40, Y1 + 30], outline=(112, 70, 34), width=44)
    d.line([((X0 + X1) // 2, Y0), ((X0 + X1) // 2, Y1)], fill=(112, 70, 34), width=26); d.line([(X0, 440), (X1, 440)], fill=(112, 70, 34), width=26)
    # INSIDE sill + wall + floor tiles: spotless
    d.rectangle([X0 - 90, Y1 + 30, X1 + 90, Y1 + 80], fill=(238, 224, 196), outline=(180, 160, 130), width=4)
    for x in range(0, w, 160):
        d.rectangle([x, 1010, x + 158, 1080], fill=(222, 214, 190), outline=(130, 150, 140), width=3)
        d.ellipse([x + 60, 1030, x + 98, 1062], outline=(80, 120, 110), width=4)
    return im
WIN_IMG = make_window()

def window_insert(tt, sh, lens=False):
    u = kk(tt, sh["start"], sh["end"]); zz = 1.0 + 0.06 * u
    fr = WIN_IMG.resize((int(W * zz), int(H * zz)), Image.LANCZOS)
    ox, oy = (fr.size[0] - W) // 2, int((fr.size[1] - H) * 0.6); fr = fr.crop((ox, oy, ox + W, oy + H))
    if sh["start"] < 0.3 and not lens:                                                       # the smash: flying shards OUTWARD (away from us)
        d = ImageDraw.Draw(fr, "RGBA"); rr = random.Random(3); k = kk(tt, 0.0, 0.35)
        for i in range(30):
            ang = rr.random() * 6.28; sp = 60 + rr.random() * 260; sc = 1 - 0.6 * k
            shard(d, 740 + math.cos(ang) * sp * k, 640 + math.sin(ang) * sp * k * 0.6, (16 + rr.random() * 22) * sc, ang + k * 4)
    if lens:
        v = ease(u); lx = W * (0.32 + 0.4 * v); ly = H * (0.78 - 0.05 * math.sin(v * math.pi)); r = 160
        src = fr.resize((int(W * 1.6), int(H * 1.6)), Image.LANCZOS)
        crop = src.crop((int(lx * 1.6 - r), int(ly * 1.6 - r), int(lx * 1.6 + r), int(ly * 1.6 + r)))
        mask = Image.new("L", crop.size, 0); ImageDraw.Draw(mask).ellipse([0, 0, 2 * r - 1, 2 * r - 1], fill=255)
        fr.paste(crop, (int(lx - r), int(ly - r)), mask)
        d = ImageDraw.Draw(fr, "RGBA")
        d.ellipse([lx - r - 6, ly - r - 6, lx + r + 6, ly + r + 6], outline=(40, 40, 46), width=16)
        d.line([(lx + r * 0.72, ly + r * 0.72), (lx + r * 1.45, ly + r * 1.45)], fill=(110, 70, 36), width=34)
        lzt(fr, W / 2, 70, "ركّزوا في الصورة!", 80, (255, 214, 90))
    return fr

def street_frame(tt, sh):
    """the pavement under the window, outside — glass everywhere (it fell OUT)"""
    cam = cam_at(sh, tt); img = bg_crop(STREET, cam).resize((W, H), Image.LANCZOS)
    d = ImageDraw.Draw(img, "RGBA"); rr = random.Random(21)
    for i in range(110):
        wx, wy = 520 + rr.random() * 880, 830 + rr.random() * 240; X, Y = W2S(cam, wx, wy)
        shard(d, X, Y, (10 + rr.random() * 18) * cam[2], rr.random() * 6.28)
        if rr.random() < 0.25:                                                             # glints
            g = 0.5 + 0.5 * math.sin(tt * 9 + i); d.ellipse([X - 5, Y - 5, X + 5, Y + 5], fill=(255, 255, 255, int(200 * g)))
    return img

# ---------------- room ----------------
def room_frame(tt, sh):
    cam = cam_at(sh, tt); z = cam[2]
    img = bg_crop(ROOM, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    # Tota (detective)
    tarms = "talk" if (T("N1") <= tt < T("N1") + DUR["N1"]) or (T("N2") <= tt < T("N2") + 1.0) else "hold"
    person(lay, cam, "tota", *POS["tota"], tt, "smug", 1, tarms)
    hx_, hy_ = hand("tota", *POS["tota"], tarms, 1); q = W2S(cam, hx_, hy_); magnifier(p, q[0], q[1], POS["tota"][2] * z)
    # Shatta + football
    sarms = "talk" if T("S1") <= tt < T("S1") + DUR["S1"] else "hold"
    person(lay, cam, "shatta", *POS["shatta"], tt, "scared" if tt >= T("N2") else "neutral", 0, sarms)
    S_s = POS["shatta"][2] * CH["shatta"]["scale"]; bx, by = hand("shatta", *POS["shatta"], sarms, 1)
    q = W2S(cam, bx + 8 * S_s, by + 6 * S_s); football(p, q[0], q[1], 15 * S_s * z, tt * 0.4)
    # Zalata + ladder (leaning on his right)
    zarms = "talk" if T("Z1") <= tt < T("Z1") + DUR["Z1"] else "hips"
    zx, zy, zs = POS["zalata"]; S_z = zs * CH["zalata"]["scale"]
    f0 = W2S(cam, zx + 70 * S_z, zy); f1 = W2S(cam, zx + 46 * S_z, zy - 250 * S_z)
    ladder(p, f0[0], f0[1], f1[0], f1[1], 30 * S_z * z)
    person(lay, cam, "zalata", zx, zy, zs, tt, "smug", 0, zarms)
    # Bandaq: suspicious of his wife
    person(lay, cam, "bondo2", *POS["bondo2"], tt, "scared" if tt < GLARE + 0.75 else "smug", 1, "talk" if T("B1") <= tt < T("B1") + DUR["B1"] else "hips")
    # Aziza: slipper in hand (the weapon nobody looks at)
    ax, ay, as_ = POS["aziza"]
    aarms = "up" if (tt < T("AZ1") + 1.3 or GLARE <= tt < GLARE + 0.75) else ("talk" if T("AZ2") <= tt < T("AZ2") + DUR["AZ2"] else "hold")
    aex = "shout" if tt < T("B1") else ("angry" if tt < T("N1") else ("sad" if tt < Q else "smug"))
    person(lay, cam, "aziza", ax, ay, as_, tt, aex, -1, aarms)
    lh = hand("aziza", ax, ay, as_, aarms, -1); q = W2S(cam, *lh); slipper(p, q[0], q[1] - 8 * z, as_ * z, -0.5 if aarms == "up" else 0.2)
    lay = tint_layer(lay, (255, 240, 214)); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    broken_room_window(fr, cam)
    # badges
    if tt >= LINEUP and tt < Q:
        a = T("N2"); hit = {0: (a + 1.0, a + 2.4), 1: (a + 2.5, a + 4.1), 2: (a + 4.2, a + 5.6)}
        for i, (who, col) in enumerate(NUMS):
            x, y, s = POS[who]; S_, _, (_, hy2) = body(who, x, y, s); q = W2S(cam, x, hy2 - 46 * S_ - 50)
            h0, h1 = hit[i]; pulse = 1 + (0.45 * math.sin(kk(tt, h0, h1) * math.pi) if h0 <= tt < h1 else 0)
            if tt >= a + 7.3: pulse = 1 + 0.12 * math.sin(tt * 8)
            badge(fr, q[0], q[1], str(i + 1), min(1.1, z * 0.75) * popk(tt, LINEUP + i * 0.2) * pulse, col)
    if GLARE <= tt < GLARE + 0.6: lzt(fr, W * 0.70, H * 0.22, "!!!", int(170 * popk(tt, GLARE, 0.2)), (255, 80, 60))
    return fr

def q_card(tt, sh):
    fr = ImageEnhance.Brightness(frame_cache(sh["start"] - 0.05)).enhance(0.45).filter(ImageFilter.GaussianBlur(5)).convert("RGBA")
    lzt(fr, W / 2, 300, "اكتب رقم الكداب في الكومنتات!", int(92 * popk(tt, sh["start"] + 0.05, 0.3)), (255, 214, 90))
    for i, (_, col) in enumerate(NUMS): badge(fr, W / 2 + (i - 1) * 200, 470, str(i + 1), 1.3 * popk(tt, sh["start"] + 0.3 + i * 0.15), col)
    lzt(fr, W / 2, 640, "الدليل في الصورة...", int(60 * popk(tt, sh["start"] + 0.75)), (255, 255, 255))
    return fr.convert("RGB")

def paper(fr, cx, cy, w, h, txt, k, col=(250, 248, 236), lines_col=(150, 170, 220), rot=0):
    lay = Image.new("RGBA", (int(w) + 40, int(h) + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rectangle([20, 20, 20 + w, 20 + h], fill=col + (255,), outline=(40, 40, 46, 255), width=6)
    for yy in range(int(20 + h * 0.2), int(20 + h), int(h * 0.18)): d.line([(34, yy), (6 + w, yy)], fill=lines_col + (255,), width=3)
    f = ImageFont.truetype(LZ, int(h * 0.3))
    d.text((20 + w / 2, 20 + h / 2), txt, font=f, fill=PINK, anchor="mm", direction="rtl", language="ar")
    lay = lay.rotate(rot, expand=True, resample=Image.BICUBIC)
    fr.paste(lay, (int(cx - lay.size[0] / 2), int(cy - lay.size[1] / 2)), lay)

def ans_card(tt, sh):
    """case-5 answer: Tota sent the letter — «عم بندء» in her notebook, same mistake + same pink pen as «بحبك يا بندء»"""
    st = T("A1"); fr = Image.new("RGB", (W, H), (16, 20, 44)); d = ImageDraw.Draw(fr, "RGBA")
    for i in range(18):
        a0 = i * 20 + tt * 6; a_ = math.radians(a0); b = math.radians(a0 + 9)
        d.polygon([(W / 2, H * 0.6), (W / 2 + 2400 * math.cos(a_), H * 0.6 + 2400 * math.sin(a_)), (W / 2 + 2400 * math.cos(b), H * 0.6 + 2400 * math.sin(b))], fill=(30, 38, 80, 255))
    lzt(fr, W / 2, 110, "حل الفزورة اللي فاتت", int(86 * popk(tt, sh["start"] + 0.15)), (255, 214, 90))
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    caught = tt >= st + 2.6
    x, y, s = 470, 1080 + 150, 3.5
    draw_char(p, "tota", x, y, s, "laugh" if caught else "happy", 0.0, 1, ((tt + 0.3) % 3.4) < 0.1, "clap" if caught else "talk", tt, None, 0.0, None)
    L2 = lay.resize((W, H), Image.LANCZOS); fr.paste(L2, (0, 0), L2)
    if caught: lzt(fr, 470, 250, "الكدابة!", int(150 * popk(tt, st + 2.6, 0.25)), (255, 255, 255), (170, 20, 20), rot=8)
    if tt >= st + 4.64:
        k = popk(tt, st + 4.64, 0.3); paper(fr, 1180, 400, 520 * k, 300 * k, "عم بندء", k, rot=4)
        if k >= 1: lzt(fr, 1180, 600, "الكشكول", 56, (255, 255, 255))
    if tt >= st + 7.48:
        k = popk(tt, st + 7.48, 0.3); paper(fr, 1560, 720, 480 * k, 280 * k, "بحبك يا بندء", k, col=(255, 222, 236), lines_col=(240, 180, 205), rot=-5)
        if k >= 1:
            dd = ImageDraw.Draw(fr, "RGBA")
            for (ex, ey) in ((1180 - 128, 400 + 4), (1560 - 128, 720 + 0)):                   # circle the «ء» in both
                dd.ellipse([ex - 50, ey - 60, ex + 50, ey + 60], outline=(255, 60, 60), width=8)
            lzt(fr, 1180, 880, "نفس الغلطة!", 70, (255, 214, 90))
    return fr

def cta_card(tt, sh):
    fr = Image.new("RGB", (W, H), (20, 12, 10)); d = ImageDraw.Draw(fr, "RGBA")
    for i in range(18):
        a0 = i * 20 - tt * 6; a_ = math.radians(a0); b = math.radians(a0 + 9)
        d.polygon([(W / 2, H / 2), (W / 2 + 2400 * math.cos(a_), H / 2 + 2400 * math.sin(a_)), (W / 2 + 2400 * math.cos(b), H / 2 + 2400 * math.sin(b))], fill=(44, 24, 16, 255))
    k = popk(tt, sh["start"] + 0.15, 0.3)
    if k > 0:
        ch = int(690 * k); cw = int(ch * 1080 / 1920)
        cov = COVER5.resize((cw, ch), Image.LANCZOS)
        fr_c = Image.new("RGBA", (cw + 24, ch + 24), (255, 214, 90, 255)); fr_c.paste(cov, (12, 12))
        fr_c = fr_c.rotate(-4, expand=True, resample=Image.BICUBIC)
        fr.paste(fr_c, (int(560 - fr_c.size[0] / 2), int(480 - fr_c.size[1] / 2)), fr_c)
        lzt(fr, 560, 72, "شوفوا القضية 5", int(70 * k), (255, 214, 90))
    st = T("C1")
    for i, (lab, col, t0) in enumerate((("لايك", (230, 50, 70), 2.4), ("فولو", (40, 140, 230), 2.9), ("شير", (60, 170, 90), 3.4))):
        k2 = popk(tt, st + t0, 0.25)
        if k2 <= 0: continue
        cx, cy = 1380, 220 + i * 190
        d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([cx - 260 * k2, cy - 80 * k2, cx + 260 * k2, cy + 80 * k2], int(60 * k2), fill=col + (255,), outline=(255, 255, 255, 255), width=6)
        ix = cx + 170 * k2
        if i == 0:
            r = 26 * k2; d.ellipse([ix - 2 * r, cy - r, ix, cy + r * 0.6], fill=(255, 255, 255)); d.ellipse([ix, cy - r, ix + 2 * r, cy + r * 0.6], fill=(255, 255, 255))
            d.polygon([(ix - 2 * r + 2, cy), (ix + 2 * r - 2, cy), (ix, cy + 2 * r)], fill=(255, 255, 255))
        elif i == 1:
            d.rectangle([ix - 34 * k2, cy - 9 * k2, ix + 34 * k2, cy + 9 * k2], fill=(255, 255, 255)); d.rectangle([ix - 9 * k2, cy - 34 * k2, ix + 9 * k2, cy + 34 * k2], fill=(255, 255, 255))
        else:
            d.polygon([(ix - 34 * k2, cy + 20 * k2), (ix + 6 * k2, cy - 20 * k2), (ix + 6 * k2, cy - 40 * k2), (ix + 40 * k2, cy - 6 * k2), (ix + 6 * k2, cy + 28 * k2), (ix + 6 * k2, cy + 8 * k2), (ix - 20 * k2, cy + 34 * k2)], fill=(255, 255, 255))
        lzt(fr, cx - 50 * k2, cy + 4, lab, int(84 * k2), (255, 255, 255), (20, 20, 20))
    if tt >= st + 3.8:
        logo(fr, 1380, 780, 80); text(fr, 1380, 850, "@shattawzalata", 40, (255, 214, 90))
    return fr

_FC = {}
def frame_cache(t_):
    if t_ not in _FC: _FC[t_] = frame(t_)
    return _FC[t_]

HOOK = "شباك عزيزة اتكسر… وغويشتها الدهب اختفت!"
def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "win": fr = window_insert(tt, sh)
    elif sh["set"] == "win2": fr = window_insert(tt, sh, lens=True)
    elif sh["set"] == "street": fr = street_frame(tt, sh)
    elif sh["set"] == "q": return finish(q_card(tt, sh), tt)
    elif sh["set"] == "ans": return finish(ans_card(tt, sh), tt)
    elif sh["set"] == "cta": return finish(cta_card(tt, sh), tt)
    else: fr = room_frame(tt, sh)
    if tt < 3.2:
        a_ = int(255 * min(1, (3.2 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([W / 2 - 790, 40, W / 2 + 790, 150], 30, fill=(20, 12, 8, int(a_ * 0.8)))
        lzt(fr, W / 2, 95, HOOK, 64, (255, 214, 90), alpha=a_)
    return finish(fr, tt)

def vertical(fr, tt):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = ImageEnhance.Brightness(small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.35)
    bgv.paste(fr.resize((1080, 608), Image.LANCZOS), (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(255, 214, 90)); d.rectangle([0, 1168, 1080, 1171], fill=(255, 214, 90))
    if tt < ANS:
        lzt(bgv, 540, 240, "مين كسر", 116, (255, 255, 255)); lzt(bgv, 540, 390, "شباك عزيزة؟", 110, (255, 214, 90))
    else:
        lzt(bgv, 540, 240, "حل الفزورة", 110, (255, 255, 255)); lzt(bgv, 540, 390, "اللي فاتت", 120, (255, 214, 90))
    lzt(bgv, 540, 1840, "مين الكداب؟ • قضية جديدة", 46, (255, 150, 110))
    k, _ = line_at(tt)
    if k and SUB.get(k):
        ls_ = wrap(SUB[k])
        if len(ls_) <= 4:
            for i, l in enumerate(ls_): text(bgv, 540, 1290 + i * 80, l, 60, sw=6)
        else:
            for i, l in enumerate(wrap(SUB[k], 30)[:6]): text(bgv, 540, 1270 + i * 64, l, 50, sw=5)
    return bgv

class _T(np.ndarray): pass
def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def glass(seed=1, amp=0.6):
    r = np.random.default_rng(seed); n = int(SR * 1.2); x = np.zeros(n, np.float32)
    burst = r.normal(0, 1, int(SR * 0.25)).astype(np.float32) * np.exp(-np.arange(int(SR * 0.25)) / SR * 14)
    burst = burst - lowpass(burst, 2500); x[:len(burst)] += burst * amp
    for i in range(26):                                                          # tinkles
        t0 = r.uniform(0.03, 0.9); f = r.uniform(2400, 6200); tn = tone(f, 0.18, amp * r.uniform(0.08, 0.25), 25)
        s0 = int(t0 * SR); x[s0:s0 + len(tn)] += tn[:max(0, n - s0)]
    return x

def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(63)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 350) * 0.02, 0, 1.0)
    mix_into(buf, glass(1, 0.7), 0.0, 1.0)                                       # SMASH
    mix_into(buf, SFXF["sting"] * 0.4, 0.15, 1.0)
    mix_into(buf, SFXF["whoosh"] * 0.4, WIN1 - 0.1, 1.0); mix_into(buf, glass(2, 0.15), WIN1 + 0.1, 1.0)
    mix_into(buf, SFXF["whoosh"] * 0.5, GLARE - 0.05, 1.0)
    mix_into(buf, tone(140, 0.35, 0.35, 6) + tone(95, 0.35, 0.3, 6), GLARE + 0.1, 1.0)
    for i in range(3): mix_into(buf, tone(660 + i * 220, 0.18, 0.2, 12), LINEUP + i * 0.2, 1.0)
    mix_into(buf, glass(3, 0.12), STREET1 + 0.05, 1.0)
    a = T("N2")
    for i, h in enumerate((1.0, 2.5, 4.2)): mix_into(buf, tone(700 + i * 180, 0.2, 0.18, 10), a + h, 1.0)
    mix_into(buf, SFXF["sting"] * 0.3, REPRISE, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), Q + k_ * 0.09, 1.0)
    mix_into(buf, tone(180, 0.5, 0.3, 4) + tone(120, 0.5, 0.3, 4), T("A1") + 2.6, 1.0)
    mix_into(buf, tone(988, 0.3, 0.16, 8), T("A1") + 4.64, 1.0); mix_into(buf, tone(1318, 0.3, 0.16, 8), T("A1") + 7.48, 1.0)
    for i, t0 in enumerate((2.4, 2.9, 3.4)): mix_into(buf, tone(880 + i * 220, 0.2, 0.2, 10), T("C1") + t0, 1.0)
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 0.5: mix_into(buf, SFXF["whoosh"] * 0.25, s_["start"] - 0.1, 1.0)
    rms = lambda x: float(np.sqrt(np.mean(x ** 2))) + 1e-9; ref = []
    for st, k in lines:
        if k == "LAUGH": continue
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8; ref.append(rms(v)); mix_into(buf, v, st, 1.0)
    g = AUD["LAUGH"][:int(SR * LAUGH_D)].copy(); g[-int(SR * 0.35):] *= np.linspace(1, 0, int(SR * 0.35))
    mix_into(buf, g / rms(g) * float(np.mean(ref)) * 0.9, T("LAUGH"), 1.0)
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
