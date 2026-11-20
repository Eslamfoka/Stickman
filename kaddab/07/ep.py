# «مين الكداب؟» — القضية 7: مين خد فلوس الجمعية؟  (H 1920x1080 + V 1080x1920 in one pass)
# Midnight, thunderstorm, the canonical lobby (s1e10/bg/morning.png graded to night). Narrator = Tota (torch under her chin).
# HOOK: lightning flash → a black silhouette runs up the stairs with an envelope → dark.
# Clue: Bandaq just came in from the street → soaked, dripping, a puddle + wet footprints from the door. Nana says she
#   "just came in from the street" too — but her closed umbrella is BONE DRY, no puddle, no footprints → she never went out.
#   Red herrings: Shatta's muddy sneakers, Zalata's flashlight.
# ANSWER (say it at the END of case 8): نعناعة (3) — she took the envelope to collect her turn early; dry umbrella, no wet steps.
# Case-6 answer told here (A1): Aziza — all the glass fell outside → broken from inside.
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont, ImageChops
os.chdir(ROOT + "/kaddab/07")
SERIES = "مين الكداب؟"; EPT = "مين خد فلوس الجمعية؟"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"; DJ = ROOT + "/brand/fonts/DejaVuSans-Bold.ttf"
SFXF = {"whoosh": load_audio(ROOT + "/trend/01/sfx/whoosh.mp3"), "sting": load_audio(ROOT + "/trend/01/sfx/stinger.mp3"),
        "gasp": load_audio(ROOT + "/trend/01/sfx/gasp.mp3")}

SUB = {"AZ1": "فلوس الجمعية! حد خد الظرف من على الترابيزة!",
       "B1": "إيه؟! أنا لسه جاي من الكشك... والدنيا بتشتي بره!",
       "N1": "الساعة اتناشر بالليل... والظرف اختفى في خمس دقايق!",
       "S1": "أنا كنت نايم... والطين ده من الصبح، والله!",
       "Z1": "أنا سمعت رجلين بتجري على السلم... نزلت بالكشاف ألحق الحرامي!",
       "NN1": "وأنا لسه داخلة من الشارع حالًا... كنت عند أختي، وما شفتش حد!",
       "N2": "مين فيهم الكداب؟ شطة بالطين؟ ولا زلطة بالكشاف؟ ولا حد تاني؟ ركزوا كويس... الحل قدامكم! واكتبوا في الكومنتات!",
       "A1": "وحل الفزورة اللي فاتت: الكدابة كانت عزيزة! الإزاز كله وقع بره... يعني الشباك اتكسر من جوه!",
       "C1": "ولو ما شفتوش الحلقة اللي فاتت... شوفوها! وما تنسوش اللايك والفولو والشير!", "LAUGH": ""}
WHO = {"AZ1": "aziza", "B1": "bondo2", "N1": "tota", "S1": "shatta", "Z1": "zalata", "NN1": "nana", "N2": "tota", "A1": "tota",
       "C1": "nana", "LAUGH": "-"}
EXPR = {"AZ1": "shout", "B1": "scared", "N1": "smug", "S1": "scared", "Z1": "angry", "NN1": "happy", "N2": "smug", "A1": "happy",
        "C1": "happy", "LAUGH": "laugh"}
load_lines([k for k in SUB if k != "LAUGH"])
LIT = _ld(ROOT + "/s1e10/bg/morning.png")                                    # canonical lobby
NIGHT = ImageChops.multiply(ImageEnhance.Brightness(LIT).enhance(0.62), Image.new("RGB", LIT.size, (150, 165, 215)))
FLASH = ImageChops.screen(ImageEnhance.Brightness(LIT).enhance(0.9), Image.new("RGB", LIT.size, (90, 100, 140)))
COVER6 = Image.open(ROOT + "/publish/thumbs/kaddab_e06_cover.jpg").convert("RGB")
STREET6 = Image.open("street6.png").convert("RGB").crop((0, 0, 1920, 900))
DOOR = (590, 85, 905, 600)                                                    # door glass (world)

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
WIDE = (980, 650, 1.22)
BOLTS = [0.25, 0.45]                                                          # lightning flashes (start times)
shot("lobby", 0.0, 1.1, (1250, 330, 1.7), (1270, 300, 1.85))                 # HOOK: the stairs — a silhouette runs up in the flash
t = say(1.05, "AZ1"); shakes.append((1.1, 14))
shot("lobby", 1.1, t + 0.05, (1190, 300, 2.5), (1190, 292, 2.7), tin="whip", ease="crash")       # Aziza on the landing, screaming
t += 0.05
s = t; t = say(t + 0.05, "B1") + 0.1; BOLTS.append(s + 0.05)
shot("lobby", s, t, (840, 640, 1.75), (850, 655, 1.95), tin="whipl")         # the street door: Bandaq soaked, dripping
n1 = say(t + 0.1, "N1"); N1 = T("N1")
shot("lobby", t, n1 + 0.15, (430, 760, 2.4), (430, 752, 2.55), tin="whipl")  # Tota, torch under her chin
LINEUP = n1 + 0.15; shot("lobby", LINEUP, LINEUP + 1.1, WIDE, (980, 655, 1.28), tin="whip"); BOLTS.append(LINEUP + 0.2)
t = LINEUP + 1.1
s = t; t = say(t + 0.05, "S1") + 0.1; shot("lobby", s, t, (640, 760, 2.35), (640, 752, 2.5), tin="whipl")     # Shatta + muddy sneakers
MUD = T("S1") + 1.3
s = t; t = say(t + 0.05, "Z1") + 0.1; shot("lobby", s, t, (1500, 740, 2.3), (1500, 732, 2.45), tin="whip")    # Zalata + flashlight
s = t; t = say(t + 0.05, "NN1") + 0.15; nn = T("NN1")
shot("lobby", s, nn + 3.0, (975, 640, 1.85), (975, 632, 2.0), tin="whipl")   # Nana (dry umbrella) next to dripping Bandaq
FEET = nn + 3.0; shot("lobby", FEET, t, (960, 880, 2.5), (960, 886, 2.62), tin="whip")    # the clue: floor — puddle vs. nothing
ASK = t; n2 = say(t + 0.05, "N2"); a = T("N2")
shot("lobby", ASK, a + 1.0, (430, 760, 2.4), (430, 752, 2.6), tin="whip")
shot("lobby", a + 1.0, a + 6.2, WIDE, (980, 660, 1.3), tin="whipl"); BOLTS.append(a + 5.0)
REPRISE = a + 6.2; shot("lobby", REPRISE, a + 8.5, (960, 880, 2.4), (960, 888, 2.7), tin="zoom")       # «ركزوا كويس… الحل قدامكم»
shot("lobby", a + 8.5, n2 + 0.3, WIDE, (980, 655, 1.28), tin="whip")
t = n2 + 0.3
Q = t; shot("q", t, t + 1.3, None); t += 1.3; BOLTS.append(Q + 0.1)
ANS = t; t = say(t + 0.25, "A1") + 0.35; shot("ans", ANS, t, None, tin="flash")
CTA = t; t = say(t + 0.15, "C1") + 0.8; shot("cta", CTA, t, None, tin="whip")
TOTAL = t

def bolt(tt):
    """lightning intensity 0..1 (double flicker)"""
    v = 0.0
    for b in BOLTS:
        u = tt - b
        if 0 <= u < 0.32: v = max(v, (1.0 if u < 0.06 else 0.25 if u < 0.11 else 0.8 if u < 0.16 else max(0, 0.8 - (u - 0.16) * 5)))
    return v

# ---------------- staging (world = lobby 1920x1080) ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
POS = {"tota": (430, 1030, 2.0), "shatta": (640, 1010, 1.7), "bondo2": (860, 1012, 1.7), "nana": (1090, 1010, 1.7),
       "zalata": (1500, 1010, 1.7), "aziza": (1190, 470, 1.25)}
NUMS = (("shatta", (230, 90, 40)), ("zalata", (60, 150, 80)), ("nana", (196, 40, 96)))

def body(who, x, y, s):
    S = s * CH[who]["scale"]; sh = y - 134 * S; return S, sh, (x, sh - 56 * S)
def hand(who, x, y, s, arms, side):
    S, sh, _ = body(who, x, y, s)
    A = {"down": ((x - 34 * S, sh + 72 * S), (x + 34 * S, sh + 72 * S)), "talk": ((x - 50 * S, sh + 52 * S), (x + 60 * S, sh + 8 * S)),
         "hold": ((x - 36 * S, sh + 70 * S), (x + 46 * S, sh + 30 * S)), "up": ((x - 72 * S, sh - 52 * S), (x + 72 * S, sh - 52 * S)),
         "hips": ((x - 48 * S, sh + 40 * S), (x + 48 * S, sh + 40 * S))}
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
os.chdir(ROOT + "/kaddab/07")

# ---------------- props ----------------
WATER = (120, 170, 230)
def umbrella(p, x, y, s, wet=False):
    """closed umbrella, hook handle at (x,y), tip down-left"""
    tip = (x - 10 * s, y + 120 * s)
    p.poly([(x - 9 * s, y + 18 * s), (x + 9 * s, y + 18 * s), (tip[0] + 2 * s, tip[1] - 14 * s), (tip[0] - 2 * s, tip[1] - 14 * s)], (40, 40, 70, 255), INK, 1.6 * s)
    p.line([(x, y + 18 * s), (x, y - 6 * s)], (40, 30, 20, 255), 3 * s)
    p.line([(x, y - 6 * s), (x - 8 * s, y - 14 * s), (x - 15 * s, y - 8 * s)], (40, 30, 20, 255), 3 * s)
    p.line([(tip[0], tip[1] - 14 * s), tip], INK, 2 * s)
def newspaper(p, x, y, s, tt):
    p.poly([(x - 46 * s, y + 4 * s), (x + 46 * s, y + 8 * s), (x + 40 * s, y - 10 * s), (x - 42 * s, y - 14 * s)], (200, 205, 190, 255), INK, 1.6 * s)
    for i in range(3): p.line([(x - 32 * s, y - 6 * s + i * 4 * s), (x + 28 * s, y - 4 * s + i * 4 * s)], (90, 90, 90, 255), 1.2 * s)

def drops(d, cam, x, y0, w, tt, n=7, seed=0):
    z = cam[2]; rr = random.Random(seed)
    for i in range(n):
        ph = rr.random(); dx = (rr.random() - 0.5) * w; u = (tt * 1.6 + ph) % 1.0
        q = W2S(cam, x + dx, y0 + u * 120); r = 4 * z
        d.ellipse([q[0] - r * 0.7, q[1] - r, q[0] + r * 0.7, q[1] + r], fill=WATER + (int(220 * (1 - u * 0.6)),))

def floor_wet(d, cam, tt):
    """puddle under Bandaq (grows) + wet footprints from the street door to him. Nothing under Nana."""
    z = cam[2]; k = min(1.0, 0.35 + 0.65 * kk(tt, T("B1"), T("B1") + 8))
    bx = POS["bondo2"][0]; q = W2S(cam, bx, 1016); rx, ry = (90 + 70 * k) * z, (16 + 10 * k) * z
    d.ellipse([q[0] - rx, q[1] - ry, q[0] + rx, q[1] + ry], fill=(70, 100, 150, 150), outline=(150, 190, 240, 120), width=max(1, int(2 * z)))
    d.ellipse([q[0] - rx * 0.5, q[1] - ry * 0.6, q[0] - rx * 0.1, q[1] - ry * 0.2], fill=(200, 220, 255, 80))
    for i in range(7):                                                           # footprints: door (750,640) → Bandaq
        u = i / 7; fx = lerp(752, bx - 20, u) + (14 if i % 2 else -14); fy = lerp(650, 985, u ** 1.3)
        sc = 0.45 + 0.55 * u; q = W2S(cam, fx, fy); w_, h_ = 13 * sc * z, 7 * sc * z
        d.ellipse([q[0] - w_, q[1] - h_, q[0] + w_, q[1] + h_], fill=(60, 85, 130, 140))

def rain_door(fr, cam, tt, fl):
    """rain + sky glow seen through the street-door glass"""
    d = ImageDraw.Draw(fr, "RGBA"); z = cam[2]
    a = W2S(cam, DOOR[0], DOOR[1]); b = W2S(cam, DOOR[2], DOOR[3])
    if b[0] < 0 or a[0] > W or b[1] < 0: return
    if fl > 0: d.rectangle([a[0], a[1], b[0], b[1]], fill=(230, 235, 255, int(150 * fl)))
    rr = random.Random(int(tt * 24))
    for i in range(70):
        x = a[0] + rr.random() * (b[0] - a[0]); y = a[1] + rr.random() * (b[1] - a[1]); L = (18 + rr.random() * 22) * z
        d.line([(x, y), (x - 4 * z, y + L)], fill=(190, 205, 240, 120), width=max(1, int(1.5 * z)))

def silhouette(lay, cam, tt):
    """the thief: a black shape running up the stairs with an envelope (only in the hook)"""
    if not (0.18 <= tt < 0.95): return
    u = kk(tt, 0.18, 0.95); x = lerp(1120, 1420, u); y = lerp(560, 230, u)
    X, Y_ = W2S(cam, x, y); S = 1.3 * cam[2]; p = P(lay); c = (8, 8, 14, 255); st = math.sin(tt * 30)
    p.ell(X, Y_ - 190 * S, 34 * S, 34 * S, c, None)
    p.line([(X, Y_ - 156 * S), (X + 6 * S, Y_ - 80 * S)], c, 16 * S)
    p.line([(X + 6 * S, Y_ - 80 * S), (X + 30 * S * st, Y_)], c, 12 * S); p.line([(X + 6 * S, Y_ - 80 * S), (X - 26 * S * st, Y_ - 10 * S)], c, 12 * S)
    p.line([(X, Y_ - 140 * S), (X + 40 * S, Y_ - 110 * S)], c, 10 * S); p.line([(X, Y_ - 140 * S), (X - 38 * S, Y_ - 116 * S)], c, 10 * S)
    p.rect(X + 34 * S, Y_ - 128 * S, X + 70 * S, Y_ - 104 * S, (236, 226, 196, 255), c, 2 * S, 1)   # the envelope

def torch_glow(fr, cam, tt):
    """Tota's torch under her chin + Zalata's flashlight beam"""
    lay = Image.new("RGBA", fr.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); z = cam[2]
    S, sh, (hx, hy) = body("tota", *POS["tota"]); q = W2S(cam, hx, hy + 30 * S)
    for i in range(8, 0, -1):
        r = (40 + i * 22) * S * z / 2; d.ellipse([q[0] - r, q[1] - r, q[0] + r, q[1] + r], fill=(255, 230, 160, 10))
    x, y, s = POS["zalata"]; S, sh, _ = body("zalata", x, y, s)
    q0 = W2S(cam, x - 40 * S, sh + 60 * S); sw = math.sin(tt * 0.9) * 120
    q1 = W2S(cam, 1250 + sw, 420); q2 = W2S(cam, 1420 + sw, 300)
    d.polygon([q0, q1, q2], fill=(255, 240, 190, 40))
    lay = lay.filter(ImageFilter.GaussianBlur(10)); fr.paste(lay, (0, 0), lay)

# ---------------- lobby ----------------
def lobby_frame(tt, sh):
    cam = cam_at(sh, tt); z = cam[2]; fl = bolt(tt)
    img = bg_crop(NIGHT, cam)
    if fl > 0: img = Image.blend(img, bg_crop(FLASH, cam), fl * 0.85)
    d0 = ImageDraw.Draw(img, "RGBA")
    floor_wet(d0, cam, tt)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    silhouette(lay, cam, tt)
    HOOKONLY = tt < 1.05
    # Aziza on the landing
    if tt >= 0.95:
        person(lay, cam, "aziza", *POS["aziza"], tt, "shout" if tt < T("B1") else "angry", 1, "up" if tt < T("B1") else "hips")
    if HOOKONLY:
        lay = tint_layer(lay, (240, 244, 255)); img.paste(lay, (0, 0), lay); fr = img.resize((W, H), Image.LANCZOS); rain_door(fr, cam, tt, fl); return fr
    # Tota + torch
    tarms = "talk" if (T("N1") <= tt < T("N1") + DUR["N1"]) or (T("N2") <= tt < T("N2") + 1.0) else "hold"
    person(lay, cam, "tota", *POS["tota"], tt, "smug", 1, tarms, held="torch")
    # Shatta: muddy sneakers
    sarms = "talk" if T("S1") <= tt < T("S1") + DUR["S1"] else "hold"
    person(lay, cam, "shatta", *POS["shatta"], tt, "scared", 1, sarms)
    x, y, s = POS["shatta"]; S_ = s * CH["shatta"]["scale"]
    for dx in (-22, 22):
        q = W2S(cam, x + dx * S_, y - 2 * S_); r = 13 * S_ * z
        p.ell(q[0], q[1], r, r * 0.55, (110, 74, 40, 255), INK, 1.5 * z); p.ell(q[0] - r * 0.3, q[1] - r * 0.2, r * 0.35, r * 0.2, (140, 98, 56, 255), None)
    # Bandaq: soaked, newspaper on his head, dripping
    x, y, s = POS["bondo2"]; S_b, shb, (hxb, hyb) = body("bondo2", x, y, s)
    barms = "talk" if T("B1") <= tt < T("B1") + DUR["B1"] else "up"
    person(lay, cam, "bondo2", x, y, s, tt, "scared" if tt < T("N1") else "flat", 1, barms)
    q = W2S(cam, hxb, hyb - 60 * S_b); newspaper(p, q[0], q[1], S_b * z, tt)
    # Nana: closed umbrella, dry
    x, y, s = POS["nana"]; narms = "talk" if T("NN1") <= tt < T("NN1") + DUR["NN1"] else "hold"
    person(lay, cam, "nana", x, y, s, tt, "happy" if tt < Q else "smug", -1, narms)
    lh = hand("nana", x, y, s, narms, -1); q = W2S(cam, *lh); umbrella(p, q[0], q[1], s * CH["nana"]["scale"] * z)
    # Zalata: flashlight
    zarms = "talk" if T("Z1") <= tt < T("Z1") + DUR["Z1"] else "hold"
    person(lay, cam, "zalata", *POS["zalata"], tt, "angry", -1, zarms, held="torch")
    lay = tint_layer(lay, (200, 210, 240) if fl < 0.3 else (240, 244, 255)); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    d = ImageDraw.Draw(fr, "RGBA")
    drops(d, cam, POS["bondo2"][0], hyb - 70 * S_b, 120 * S_b, tt, 9, 1)                    # dripping from Bandaq + newspaper
    drops(d, cam, POS["bondo2"][0], shb + 100 * S_b, 70 * S_b, tt + 0.3, 5, 2)
    rain_door(fr, cam, tt, fl)
    torch_glow(fr, cam, tt)
    # badges
    if LINEUP + 0.3 <= tt < Q and not (FEET <= tt < ASK) and not (REPRISE <= tt < T("N2") + 8.5):
        a = T("N2"); hit = {0: (a + 1.7, a + 2.7), 1: (a + 3.0, a + 4.3), 2: (a + 4.9, a + 5.7)}
        for i, (who, col) in enumerate(NUMS):
            x, y, s = POS[who]; S_, _, (_, hy2) = body(who, x, y, s); q = W2S(cam, x, hy2 - 46 * S_ - 50)
            h0, h1 = hit[i]; pulse = 1 + (0.45 * math.sin(kk(tt, h0, h1) * math.pi) if h0 <= tt < h1 else 0)
            if tt >= a + 8.5: pulse = 1 + 0.12 * math.sin(tt * 8)
            badge(fr, q[0], q[1], str(i + 1), min(1.1, z * 0.75) * popk(tt, LINEUP + 0.3 + i * 0.2) * pulse, col)
    if REPRISE <= tt < T("N2") + 8.5:                                                       # magnifier lens over the floor
        u = ease(kk(tt, REPRISE, T("N2") + 8.3)); lx = W * (0.25 + 0.5 * u); ly = H * 0.72; r = 170
        src = fr.resize((int(W * 1.5), int(H * 1.5)), Image.LANCZOS)
        crop = src.crop((int(lx * 1.5 - r), int(ly * 1.5 - r), int(lx * 1.5 + r), int(ly * 1.5 + r)))
        mask = Image.new("L", crop.size, 0); ImageDraw.Draw(mask).ellipse([0, 0, 2 * r - 1, 2 * r - 1], fill=255)
        fr.paste(crop, (int(lx - r), int(ly - r)), mask); d = ImageDraw.Draw(fr, "RGBA")
        d.ellipse([lx - r - 6, ly - r - 6, lx + r + 6, ly + r + 6], outline=(40, 40, 46), width=16)
        d.line([(lx + r * 0.72, ly + r * 0.72), (lx + r * 1.4, ly + r * 1.4)], fill=(110, 70, 36), width=34)
        lzt(fr, W / 2, 200, "ركّزوا كويس… الحل قدامكم!", 72, (255, 214, 90))
    return fr

def q_card(tt, sh):
    fr = ImageEnhance.Brightness(frame_cache(sh["start"] - 0.05)).enhance(0.45).filter(ImageFilter.GaussianBlur(5)).convert("RGBA")
    fl = bolt(tt)
    if fl > 0: fr = Image.blend(fr, Image.new("RGBA", fr.size, (230, 235, 255, 255)), fl * 0.5)
    lzt(fr, W / 2, 300, "اكتب رقم الكداب في الكومنتات!", int(92 * popk(tt, sh["start"] + 0.05, 0.3)), (255, 214, 90))
    for i, (_, col) in enumerate(NUMS): badge(fr, W / 2 + (i - 1) * 200, 470, str(i + 1), 1.3 * popk(tt, sh["start"] + 0.3 + i * 0.15), col)
    lzt(fr, W / 2, 640, "الدليل في الصورة...", int(60 * popk(tt, sh["start"] + 0.75)), (255, 255, 255))
    return fr.convert("RGB")

def ans_card(tt, sh):
    """case-6 answer: Aziza — all the glass fell OUTSIDE → the window was broken from inside"""
    st = T("A1"); fr = Image.new("RGB", (W, H), (16, 20, 44)); d = ImageDraw.Draw(fr, "RGBA")
    for i in range(18):
        a0 = i * 20 + tt * 6; a_ = math.radians(a0); b = math.radians(a0 + 9)
        d.polygon([(W / 2, H * 0.6), (W / 2 + 2400 * math.cos(a_), H * 0.6 + 2400 * math.sin(a_)), (W / 2 + 2400 * math.cos(b), H * 0.6 + 2400 * math.sin(b))], fill=(30, 38, 80, 255))
    lzt(fr, W / 2, 110, "حل الفزورة اللي فاتت", int(86 * popk(tt, sh["start"] + 0.15)), (255, 214, 90))
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    caught = tt >= st + 1.7
    draw_char(p, "aziza", 470, 1080 + 150, 3.4, "scared" if caught else "smug", 0.0, 1, ((tt + 0.3) % 3.4) < 0.1, "scared" if caught else "hips", tt, None, 0.0, None)
    L2 = lay.resize((W, H), Image.LANCZOS); fr.paste(L2, (0, 0), L2)
    if caught: lzt(fr, 470, 250, "الكدابة!", int(150 * popk(tt, st + 1.7, 0.25)), (255, 255, 255), (170, 20, 20), rot=8)
    if tt >= st + 3.5:
        k = popk(tt, st + 3.5, 0.3); w_, h_ = int(860 * k), int(403 * k)
        if w_ > 10:
            im = STREET6.resize((w_, h_), Image.LANCZOS); bx = Image.new("RGB", (w_ + 20, h_ + 20), (255, 214, 90)); bx.paste(im, (10, 10))
            fr.paste(bx, (int(1350 - bx.size[0] / 2), int(470 - bx.size[1] / 2)))
        if k >= 1: lzt(fr, 1350, 760, "الإزاز كله بره!", 70, (255, 255, 255))
    if tt >= st + 5.4: lzt(fr, 1350, 870, "يعني اتكسر من جوه!", int(76 * popk(tt, st + 5.4, 0.3)), (255, 214, 90))
    return fr

def cta_card(tt, sh):
    fr = Image.new("RGB", (W, H), (20, 12, 10)); d = ImageDraw.Draw(fr, "RGBA")
    for i in range(18):
        a0 = i * 20 - tt * 6; a_ = math.radians(a0); b = math.radians(a0 + 9)
        d.polygon([(W / 2, H / 2), (W / 2 + 2400 * math.cos(a_), H / 2 + 2400 * math.sin(a_)), (W / 2 + 2400 * math.cos(b), H / 2 + 2400 * math.sin(b))], fill=(44, 24, 16, 255))
    k = popk(tt, sh["start"] + 0.15, 0.3)
    if k > 0:
        ch = int(690 * k); cw = int(ch * 1080 / 1920)
        cov = COVER6.resize((cw, ch), Image.LANCZOS)
        fr_c = Image.new("RGBA", (cw + 24, ch + 24), (255, 214, 90, 255)); fr_c.paste(cov, (12, 12))
        fr_c = fr_c.rotate(-4, expand=True, resample=Image.BICUBIC)
        fr.paste(fr_c, (int(560 - fr_c.size[0] / 2), int(480 - fr_c.size[1] / 2)), fr_c)
        lzt(fr, 560, 72, "شوفوا القضية 6", int(70 * k), (255, 214, 90))
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

HOOK = "فلوس الجمعية اختفت… الساعة 12 بالليل!"
def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "q": return finish(q_card(tt, sh), tt)
    elif sh["set"] == "ans": return finish(ans_card(tt, sh), tt)
    elif sh["set"] == "cta": return finish(cta_card(tt, sh), tt)
    fr = lobby_frame(tt, sh)
    if tt < 3.4:
        a_ = int(255 * min(1, (3.4 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([W / 2 - 720, 40, W / 2 + 720, 150], 30, fill=(20, 12, 8, int(a_ * 0.8)))
        lzt(fr, W / 2, 95, HOOK, 66, (255, 214, 90), alpha=a_)
    return finish(fr, tt)

def vertical(fr, tt):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = ImageEnhance.Brightness(small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.35)
    bgv.paste(fr.resize((1080, 608), Image.LANCZOS), (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(255, 214, 90)); d.rectangle([0, 1168, 1080, 1171], fill=(255, 214, 90))
    if tt < ANS:
        lzt(bgv, 540, 240, "مين خد", 116, (255, 255, 255)); lzt(bgv, 540, 390, "فلوس الجمعية؟", 110, (255, 214, 90))
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

def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def thunder(seed, amp=0.6, dur=2.6):
    r = np.random.default_rng(seed); n = int(SR * dur); x = r.normal(0, 1, n).astype(np.float32)
    x = lowpass(lowpass(x, 180), 140); env = np.exp(-np.arange(n) / SR * 1.6) * (0.4 + 0.6 * np.abs(np.sin(np.arange(n) / SR * 7)))
    crack = r.normal(0, 1, int(SR * 0.12)).astype(np.float32) * np.exp(-np.arange(int(SR * 0.12)) / SR * 30)
    x = x / (np.abs(x).max() + 1e-9) * env * amp; x[:len(crack)] += crack * amp * 0.5; return x
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 3; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(77)
    rain = r.normal(0, 1, n).astype(np.float32); rain = (rain - lowpass(rain, 1200)) * 0.05 + lowpass(rain, 500) * 0.04
    rain[int(ANS * SR):] *= 0.0; mix_into(buf, rain, 0, 1.0)                                           # rain bed until the answer card
    for i, b in enumerate(BOLTS): mix_into(buf, thunder(10 + i, 0.75 if i == 0 else 0.5), b + 0.05, 1.0)
    mix_into(buf, SFXF["sting"] * 0.45, 0.3, 1.0)
    for j in range(40):                                                                               # running steps on the stairs (hook)
        if j < 6: mix_into(buf, tone(90, 0.08, 0.35, 30), 0.2 + j * 0.12, 1.0)
    rr = random.Random(5)
    for j in range(int((ANS - T("B1")) / 0.45)):                                                      # drip… drip… (Bandaq)
        mix_into(buf, tone(1700 + rr.random() * 600, 0.06, 0.06, 40), T("B1") + j * 0.45 + rr.random() * 0.1, 1.0)
    for i in range(3): mix_into(buf, tone(660 + i * 220, 0.18, 0.2, 12), LINEUP + 0.3 + i * 0.2, 1.0)
    mix_into(buf, SFXF["gasp"] * 0.3, FEET, 1.0); mix_into(buf, tone(180, 0.5, 0.22, 4), FEET, 1.0)
    a = T("N2")
    for i, h in enumerate((1.7, 3.0, 4.9)): mix_into(buf, tone(700 + i * 180, 0.2, 0.18, 10), a + h, 1.0)
    mix_into(buf, SFXF["sting"] * 0.3, REPRISE, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), Q + k_ * 0.09, 1.0)
    mix_into(buf, tone(180, 0.5, 0.3, 4), T("A1") + 1.7, 1.0); mix_into(buf, tone(120, 0.5, 0.3, 4), T("A1") + 1.7, 1.0)
    mix_into(buf, tone(988, 0.3, 0.16, 8), T("A1") + 3.5, 1.0); mix_into(buf, tone(1318, 0.3, 0.16, 8), T("A1") + 5.4, 1.0)
    for i, t0 in enumerate((2.4, 2.9, 3.4)): mix_into(buf, tone(880 + i * 220, 0.2, 0.2, 10), T("C1") + t0, 1.0)
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 1.0: mix_into(buf, SFXF["whoosh"] * 0.22, s_["start"] - 0.1, 1.0)
    for st, k in lines:
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8; mix_into(buf, v, st, 1.0)
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
