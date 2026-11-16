# «مين الكداب؟» — القضية 4: مين قطع النور؟  (H 1920x1080 + V 1080x1920 in one pass)
# Whole case in the DARK lobby: Tota's torch beam picks each suspect out of the black.
# Clue (layered): the meter box was painted red this morning (sign «احترس... الدهان لسه طري») and the switch has a small red fingerprint.
#   Bandaq has paint on him but EXPLAINS it (he painted it in the morning). Zalata says he never came down — yet his fingertip is red.
#   ANSWER (say it at the END of case 5): زلطة.  Case-3 answer (عم بندق — empty pillow) is told at the END here (A1) + C1 reused.
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont, ImageChops
os.chdir(ROOT + "/kaddab/04")
SERIES = "مين الكداب؟"; EPT = "مين قطع النور؟"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"; DJ = ROOT + "/brand/fonts/DejaVuSans-Bold.ttf"
SFXF = {"whoosh": load_audio(ROOT + "/trend/01/sfx/whoosh.mp3"), "sting": load_audio(ROOT + "/trend/01/sfx/stinger.mp3")}

SUB = {"N1": "مين قطع النور على العمارة كلها؟!",
       "T1": "النور اتقطع من العدّاد اللي تحت... وواحد فيكم هو اللي نزل!",
       "S1": "أنا كنت بلعب بلايستيشن... ولما النور قطع اتخضّيت وصرّخت!",
       "Z1": "أنا كنت فوق بذاكر... ولا نزلت السلم خالص!",
       "B1": "أنا دهنت العدّاد الصبح... وبالليل كنت بتعشّى مع عزيزة!",
       "T2": "مين فيهم الكداب؟ واحد... ولا اتنين... ولا تلاتة؟ بصّوا كويس في النور... واكتبوا في الكومنتات!",
       "A1": "وحل الفزورة اللي فاتت: الكداب كان عم بندق! عشان المخدة اللي جنبها كانت فاضية... يعني ماكانش نايم جنبها!",
       "C1": "ولو ما شفتوش الحلقة اللي فاتت... شوفوها! وما تنسوش اللايك والفولو والشير!"}
WHO = {"N1": "nana", "T1": "tota", "S1": "shatta", "Z1": "zalata", "B1": "bondo2", "T2": "tota", "A1": "nana", "C1": "nana"}
EXPR = {"N1": "shout", "T1": "smug", "S1": "scared", "Z1": "smug", "B1": "flat", "T2": "smug", "A1": "happy", "C1": "happy"}
load_lines(list(SUB))
LIT = _ld(ROOT + "/s1e10/bg/morning.png")                                    # canonical lobby
LIT = ImageChops.multiply(ImageEnhance.Brightness(LIT).enhance(0.8), Image.new("RGB", LIT.size, (210, 205, 230)))   # night, lamp on
COVER3 = Image.open(ROOT + "/publish/thumbs/kaddab_e03_cover.jpg").convert("RGB")
PHOTO3 = Image.open("photo3.png").convert("RGB")

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
WIDE = (1000, 650, 1.25)
CUT = 0.3                                                                        # the click: power dies
t = say(0.3, "N1"); shakes.append((0.5, 14))
shot("lobby", 0.0, t + 0.1, (450, 700, 2.4), (450, 690, 2.6), ease="crash")    # black → torch hits Nana's face
t += 0.1
t1 = say(t, "T1"); a = T("T1")
shot("lobby", t, a + 0.7, (1560, 720, 2.6), (1560, 712, 2.75), tin="whip")      # Tota, torch under her chin
METER = a + 0.7; shot("meter", METER, a + 2.45, None, tin="zoom")              # «من العدّاد اللي تحت» → insert: sign + red fingerprint
SWEEP = a + 2.45; shot("lobby", SWEEP, t1 + 0.2, WIDE, (1000, 660, 1.3), tin="whipl")   # «وواحد فيكم…» torch sweeps the three
LINEUP = SWEEP + 0.5; t = t1 + 0.2
s = t; t = say(t + 0.05, "S1") + 0.1; shot("lobby", s, t, (700, 720, 2.4), (700, 712, 2.55), tin="whipl")
s = t; t = say(t + 0.05, "Z1") + 0.15; ZT = T("Z1"); shot("lobby", s, t, (940, 720, 2.4), (940, 712, 2.6), tin="whip")
s = t; t = say(t + 0.05, "B1") + 0.15; shot("lobby", s, t, (1180, 720, 2.4), (1180, 712, 2.55), tin="whip")
ASK = t; t2 = say(t + 0.05, "T2"); a = T("T2")
shot("lobby", ASK, a + 1.3, (1560, 720, 2.6), (1560, 712, 2.8), tin="whip")
shot("lobby", a + 1.3, t2 + 0.3, WIDE, (1000, 665, 1.33), tin="whipl")            # 1… 2… 3 + slow sweep on «بصّوا كويس في النور»
t = t2 + 0.3
Q = t; shot("q", t, t + 1.3, None); t += 1.3                                    # lights flicker back on behind the question card
ANS = t; t = say(t + 0.25, "A1") + 0.35; shot("ans", ANS, t, None, tin="flash")
CTA = t; t = say(t + 0.15, "C1") + 0.8; shot("cta", CTA, t, None, tin="whip")
TOTAL = t

# ---------------- staging (world = lobby 1920x1080) ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
POS = {"nana": (450, 1010, 1.7), "shatta": (700, 1010, 1.7), "zalata": (940, 1010, 1.7), "bondo2": (1180, 1012, 1.7), "tota": (1560, 1030, 2.0)}
NUMS = (("shatta", (230, 90, 40)), ("zalata", (60, 150, 80)), ("bondo2", (196, 40, 96)))
MBOX = (965, 250, 1095, 430)                                                    # meter box on the wall right of the street door

def body(who, x, y, s):
    S = s * CH[who]["scale"]; sh = y - 134 * S; return S, sh, (x, sh - 56 * S)

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, held=None):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    blink = ((tt + len(who) * 0.37) % 3.6) < 0.11 and expr not in ("scared", "shout")
    if not talking: lean += math.sin(tt * 1.7 + len(who)) * 0.05
    X, Y_ = W2S(cam, x, y); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, held, lean, None)

def meter_box(p, cam, wet=True):
    z = cam[2]; a_ = W2S(cam, MBOX[0], MBOX[1]); b = W2S(cam, MBOX[2], MBOX[3])
    p.rect(a_[0], a_[1], b[0], b[1], (190, 36, 34, 255), INK, 3 * z, 4 * z)                            # freshly painted red
    p.rect(a_[0] + 14 * z, a_[1] + 16 * z, b[0] - 14 * z, a_[1] + 70 * z, (230, 230, 220, 255), INK, 2 * z, 3 * z)   # dial window
    for i in range(4): p.ell(a_[0] + (34 + i * 22) * z, a_[1] + 43 * z, 7 * z, 7 * z, (40, 40, 40, 255), None)
    q = W2S(cam, (MBOX[0] + MBOX[2]) / 2, MBOX[1] + 128); p.rect(q[0] - 14 * z, q[1] - 26 * z, q[0] + 14 * z, q[1] + 26 * z, (60, 60, 64, 255), INK, 2 * z, 3 * z)
    p.rect(q[0] - 8 * z, q[1] + 2 * z, q[0] + 8 * z, q[1] + 20 * z, (30, 30, 30, 255), None)           # the main switch: DOWN (off)
    p.ell(q[0] + 4 * z, q[1] - 12 * z, 4 * z, 5 * z, (150, 20, 20, 255), None)                        # tiny red fingerprint smudge
    for i_ in (1, 2): p.ell(q[0] + 4 * z, q[1] - 12 * z, (4 - i_ * 1.2) * z, (5 - i_ * 1.4) * z, None, (230, 120, 110, 255), 0.5 * z)   # print ridges
    for i in range(3):                                                                             # wet drips
        x_ = a_[0] + (20 + i * 40) * z; p.line([(x_, b[1]), (x_, b[1] + (10 + i * 6) * z)], (190, 36, 34, 255), 3 * z)
    s0 = W2S(cam, MBOX[0] - 10, MBOX[3] + 30); s1 = W2S(cam, MBOX[2] + 10, MBOX[3] + 90)
    p.rect(s0[0], s0[1], s1[0], s1[1], (250, 240, 200, 255), INK, 2 * z, 2 * z)                       # the sign (text drawn later)

def gamepad(p, x, y, s):
    p.rect(x - 22 * s, y - 10 * s, x + 22 * s, y + 10 * s, (40, 40, 48, 255), INK, 2 * s, 9 * s)
    p.ell(x - 10 * s, y, 3 * s, 3 * s, (220, 220, 220, 255), None); p.ell(x + 10 * s, y - 3 * s, 2.5 * s, 2.5 * s, (220, 60, 60, 255), None)
    p.ell(x + 15 * s, y + 3 * s, 2.5 * s, 2.5 * s, (60, 120, 220, 255), None)

def brush(p, x, y, s):
    p.line([(x, y), (x + 10 * s, y - 34 * s)], (150, 100, 50, 255), 4 * s)
    p.rect(x + 4 * s, y - 50 * s, x + 20 * s, y - 34 * s, (200, 200, 200, 255), INK, 1.5 * s, 2 * s)
    p.rect(x + 5 * s, y - 60 * s, x + 19 * s, y - 50 * s, (190, 36, 34, 255), None)

def torch_target(tt):
    """where the torch spot is (world x, y, radius) — the light picks out who is talking"""
    k, lt = line_at(tt)
    hd = lambda w: (POS[w][0], body(w, *POS[w])[2][1] + 40, 150)
    if tt < CUT + 0.25: return None
    if tt < T("T1"): return hd("nana")
    if tt < SWEEP:
        x, y, r = hd("tota"); return (x, y + 30, 160)                         # under her chin
    if tt < T("S1"):
        u = ease(kk(tt, SWEEP, T("S1") - 0.1)); return (lerp(560, 1240, u), 760 + 40 * math.sin(u * 6), 190)
    for key, who in (("S1", "shatta"), ("Z1", "zalata"), ("B1", "bondo2")):
        if T(key) - 0.05 <= tt < T(key) + DUR[key] + 0.2:
            x, y, r = hd(who); return (x, y + 60, 230)
    a = T("T2")
    if tt < a + 1.3: x, y, r = hd("tota"); return (x, y + 30, 170)
    for i, (h0, h1) in enumerate(((1.49, 2.32), (2.33, 3.35), (3.36, 4.53))):
        if a + h0 <= tt < a + h1: x, y, r = hd(NUMS[i][0]); return (x, y + 80, 220)
    if a + 4.53 <= tt < a + 6.07:                                                # «بصّوا كويس في النور» — slow sweep over all three (never stops on the clue)
        u = kk(tt, a + 4.53, a + 6.07); return (lerp(600, 1280, u), 800, 230)
    return (940, 800, 380)

def light_mask(cam, tt, extra=()):
    m = Image.new("L", (W // 4, H // 4), 0); d = ImageDraw.Draw(m); z = cam[2]
    tg = torch_target(tt)
    spots = list(extra)
    if tg: spots.append(tg)
    for (x, y, r) in spots:
        q = W2S(cam, x, y); R = r * z / 4; qx, qy = q[0] / 4, q[1] / 4
        for i in range(10, 0, -1):
            rr = R * (0.55 + 0.07 * i); d.ellipse([qx - rr, qy - rr * 1.05, qx + rr, qy + rr * 1.05], fill=int(255 * (1 - i / 11) ** 0.7))
    if tg and tt >= T("T1"):                                                   # faint cone from Tota's torch to the spot
        q0 = W2S(cam, POS["tota"][0] + 70, POS["tota"][1] - 250); q = W2S(cam, tg[0], tg[1])
        d.polygon([(q0[0] / 4, q0[1] / 4), (q[0] / 4 - tg[2] * z / 5, q[1] / 4), (q[0] / 4 + tg[2] * z / 5, q[1] / 4)], fill=40)
    return m.filter(ImageFilter.GaussianBlur(6)).resize((W, H), Image.BILINEAR)

def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255, font=None, rot=0):
    if size < 4: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(font or LZ, size)
    kw = dict(font=f, anchor="mm", direction="rtl", language="ar") if font is None else dict(font=f, anchor="mm")
    d.text((x, y), s, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), **kw)
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
os.chdir(ROOT + "/kaddab/04")

def lobby_lit(tt, cam, lights=False):
    img = bg_crop(LIT, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay); z = cam[2]
    meter_box(p, cam)
    nex = "shout" if tt < T("T1") + 0.5 else "angry"
    person(lay, cam, "nana", *POS["nana"], tt, nex, 1, "hips" if tt >= T("T1") else "up")
    # Shatta: scared, gamepad in hand
    x, y, s = POS["shatta"]; sarms = "hold"
    person(lay, cam, "shatta", x, y, s, tt, "scared" if tt < ASK else "neutral", 0, sarms)
    S, sh, _ = body("shatta", x, y, s); q = W2S(cam, x - 36 * S, sh + 70 * S); gamepad(p, q[0], q[1], S * z)
    # Zalata: confident, talking hand — RED PAINT on the fingertip (the clue, never pointed at)
    x, y, s = POS["zalata"]; zarms = "talk" if T("Z1") <= tt < T("Z1") + DUR["Z1"] else "hold"
    person(lay, cam, "zalata", x, y, s, tt, "smug", 0, zarms)
    S, sh, _ = body("zalata", x, y, s)
    hx, hy = (x + 60 * S, sh + 8 * S) if zarms == "talk" else (x + 46 * S, sh + 30 * S)
    q = W2S(cam, hx + 3 * S, hy - 4 * S); p.ell(q[0], q[1], 3.4 * S * z, 3.4 * S * z, (200, 30, 30, 255), None)
    # Bandaq: brush in hand, red paint dots on his galabeya (explained: he painted the box this morning)
    x, y, s = POS["bondo2"]; barms = "talk" if T("B1") <= tt < T("B1") + DUR["B1"] else "hold"
    person(lay, cam, "bondo2", x, y, s, tt, "flat", 0, barms)
    S, sh, _ = body("bondo2", x, y, s)
    for (dx, dy) in ((-18, 40), (10, 70), (-6, 100), (20, 120)):
        q = W2S(cam, x + dx * S, sh + dy * S); p.ell(q[0], q[1], 4 * S * z, 3 * S * z, (190, 36, 34, 255), None)
    q = W2S(cam, x + 46 * S, sh + 30 * S) if barms == "hold" else W2S(cam, x + 60 * S, sh + 8 * S); brush(p, q[0], q[1], S * z)
    # Tota: the torch
    tarms = "talk" if (T("T1") <= tt < T("T1") + DUR["T1"]) or (T("T2") <= tt < T("T2") + 1.3) else "hold"
    person(lay, cam, "tota", *POS["tota"], tt, "smug", -1, tarms, held="torch")
    img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    s0 = W2S(cam, MBOX[0] - 10, MBOX[3] + 30); s1 = W2S(cam, MBOX[2] + 10, MBOX[3] + 90)
    lzt(fr, (s0[0] + s1[0]) / 2, (s0[1] + s1[1]) / 2, "احترس... الدهان طري", int(15 * z), (190, 30, 30), (250, 240, 200))
    return fr

def lobby_frame(tt, sh, cam=None):
    cam = cam or cam_at(sh, tt)
    lit = lobby_lit(tt, cam)
    if tt < CUT: return lit                                                             # 0.3 s of normal light, then the click
    dark = ImageEnhance.Brightness(lit).enhance(0.07)
    dark = ImageChops.multiply(dark, Image.new("RGB", dark.size, (150, 165, 230)))
    warm = ImageChops.multiply(lit, Image.new("RGB", lit.size, (255, 244, 214)))
    fr = Image.composite(warm, dark, light_mask(cam, tt))
    if tt >= LINEUP and tt < Q:
        a = T("T2"); hit = {0: (a + 1.49, a + 2.32), 1: (a + 2.33, a + 3.35), 2: (a + 3.36, a + 4.53)}; z = cam[2]
        for i, (who, col) in enumerate(NUMS):
            x, y, s = POS[who]; S_, _, (_, hy_) = body(who, x, y, s); q = W2S(cam, x, hy_ - 46 * S_ - 50)
            h0, h1 = hit[i]; pulse = 1 + (0.45 * math.sin(kk(tt, h0, h1) * math.pi) if h0 <= tt < h1 else 0)
            if tt >= a + 6.07: pulse = 1 + 0.12 * math.sin(tt * 8)
            badge(fr, q[0], q[1], str(i + 1), min(1.1, z * 0.75) * popk(tt, LINEUP + i * 0.2) * pulse, col)
    return fr

def meter_insert(tt, sh):
    """close-up of the meter box in the torch light: switch down, wet-paint sign, a red fingerprint"""
    u = kk(tt, sh["start"], sh["end"]); cam0 = (0, 0, 3.5 + 0.35 * ease(u))
    cam = (1030 - 960 / cam0[2], 412 - 540 / cam0[2], cam0[2])
    lit = lobby_lit(tt, cam)
    dark = ImageChops.multiply(ImageEnhance.Brightness(lit).enhance(0.07), Image.new("RGB", lit.size, (150, 165, 230)))
    fr = Image.composite(lit, dark, light_mask(cam, tt, [(1030 + 30 * math.sin(tt * 2), 395, 140)]))
    return fr

PH_ANS = None
def q_card(tt, sh):
    k_on = kk(tt, sh["start"] + 0.2, sh["start"] + 0.5)
    flick = 1 if (k_on >= 1 or (int(tt * 20) % 3 == 0 and k_on > 0)) else 0                 # lights flicker back on
    cam = (WIDE[0] - 960 / WIDE[2], 1080 - 1080 / WIDE[2], WIDE[2]); base = lobby_lit(tt, cam) if flick else lobby_frame(tt, sh, cam)
    fr = ImageEnhance.Brightness(base).enhance(0.45).filter(ImageFilter.GaussianBlur(5)).convert("RGBA")
    lzt(fr, W / 2, 300, "اكتب رقم الكداب في الكومنتات!", int(92 * popk(tt, sh["start"] + 0.05, 0.3)), (255, 214, 90))
    for i, (_, col) in enumerate(NUMS):
        badge(fr, W / 2 + (i - 1) * 200, 470, str(i + 1), 1.3 * popk(tt, sh["start"] + 0.3 + i * 0.15), col)
    lzt(fr, W / 2, 640, "الدليل في النور...", int(60 * popk(tt, sh["start"] + 0.75)), (255, 255, 255))
    return fr.convert("RGB")

def ans_card(tt, sh):
    """case-3 answer: Bandaq lied — the pillow next to Aziza in the photo was EMPTY"""
    st = T("A1"); fr = Image.new("RGB", (W, H), (16, 20, 44)); d = ImageDraw.Draw(fr, "RGBA")
    for i in range(18):
        a0 = i * 20 + tt * 6; a_ = math.radians(a0); b = math.radians(a0 + 9)
        d.polygon([(W / 2, H * 0.6), (W / 2 + 2400 * math.cos(a_), H * 0.6 + 2400 * math.sin(a_)), (W / 2 + 2400 * math.cos(b), H * 0.6 + 2400 * math.sin(b))], fill=(30, 38, 80, 255))
    lzt(fr, W / 2, 110, "حل الفزورة اللي فاتت", int(86 * popk(tt, sh["start"] + 0.15)), (255, 214, 90))
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    caught = tt >= st + 2.0
    x, y, s = 520, 1080 + 130, 3.3
    draw_char(p, "bondo2", x, y, s, "scared" if caught else "neutral", 0.0, 1, ((tt + 0.3) % 3.4) < 0.1, "scared" if caught else "down", tt, None, 0.0, None)
    L2 = lay.resize((W, H), Image.LANCZOS); fr.paste(L2, (0, 0), L2)
    if caught: lzt(fr, 520, 250, "الكداب!", int(150 * popk(tt, st + 2.0, 0.25)), (255, 255, 255), (170, 20, 20), rot=8)
    if tt >= st + 3.85:                                                                      # the photo again, the empty pillow circled
        k = popk(tt, st + 3.85, 0.3); pw = int(820 * k); ph = int(pw * 2 / 3)
        if pw > 20:
            ph_img = PHOTO3.resize((pw, ph), Image.LANCZOS); card = Image.new("RGB", (pw + 24, ph + 24), (250, 250, 248)); card.paste(ph_img, (12, 12))
            cx, cy = 1340, 500; fr.paste(card, (int(cx - card.size[0] / 2), int(cy - card.size[1] / 2)))
            if tt >= st + 4.5:
                d = ImageDraw.Draw(fr, "RGBA"); ox, oy = cx - pw / 2, cy - ph / 2
                ex, ey = ox + pw * 0.73, oy + ph * 0.42
                d.ellipse([ex - 150 * k, ey - 80 * k, ex + 150 * k, ey + 80 * k], outline=(230, 40, 40), width=10)
                lzt(fr, cx, cy + ph / 2 + 70, "المخدة فاضية!", int(72 * popk(tt, st + 4.5)), (255, 214, 90))
    return fr

def cta_card(tt, sh):
    fr = Image.new("RGB", (W, H), (20, 12, 10)); d = ImageDraw.Draw(fr, "RGBA")
    for i in range(18):
        a0 = i * 20 - tt * 6; a_ = math.radians(a0); b = math.radians(a0 + 9)
        d.polygon([(W / 2, H / 2), (W / 2 + 2400 * math.cos(a_), H / 2 + 2400 * math.sin(a_)), (W / 2 + 2400 * math.cos(b), H / 2 + 2400 * math.sin(b))], fill=(44, 24, 16, 255))
    k = popk(tt, sh["start"] + 0.15, 0.3)
    if k > 0:
        ch = int(690 * k); cw = int(ch * 1080 / 1920)
        cov = COVER3.resize((cw, ch), Image.LANCZOS)
        fr_c = Image.new("RGBA", (cw + 24, ch + 24), (255, 214, 90, 255)); fr_c.paste(cov, (12, 12))
        fr_c = fr_c.rotate(-4, expand=True, resample=Image.BICUBIC)
        fr.paste(fr_c, (int(560 - fr_c.size[0] / 2), int(480 - fr_c.size[1] / 2)), fr_c)
        lzt(fr, 560, 72, "شوفوا القضية 3", int(70 * k), (255, 214, 90))
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

HOOK = "حد قطع النور على العمارة كلها!"
def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "meter": fr = meter_insert(tt, sh)
    elif sh["set"] == "q": return finish(q_card(tt, sh), tt)
    elif sh["set"] == "ans": return finish(ans_card(tt, sh), tt)
    elif sh["set"] == "cta": return finish(cta_card(tt, sh), tt)
    else: fr = lobby_frame(tt, sh)
    if tt < 3.2:
        a_ = int(255 * min(1, (3.2 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([W / 2 - 560, 40, W / 2 + 560, 150], 30, fill=(20, 12, 8, int(a_ * 0.8)))
        lzt(fr, W / 2, 95, HOOK, 72, (255, 214, 90), alpha=a_)
    return finish(fr, tt)

def vertical(fr, tt):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = ImageEnhance.Brightness(small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.35)
    bgv.paste(fr.resize((1080, 608), Image.LANCZOS), (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(255, 214, 90)); d.rectangle([0, 1168, 1080, 1171], fill=(255, 214, 90))
    if tt < ANS:
        lzt(bgv, 540, 240, "حد قطع النور", 110, (255, 255, 255)); lzt(bgv, 540, 390, "على العمارة كلها!", 104, (255, 214, 90))
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
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(51)
    hum = (np.sin(2 * np.pi * 50 * np.arange(int(SR * CUT)) / SR) * 0.05).astype(np.float32); mix_into(buf, hum, 0, 1.0)   # fridge/lamp hum… then silence
    mix_into(buf, tone(2200, 0.05, 0.4, 60) + tone(180, 0.05, 0.4, 30), CUT, 1.0)                     # the CLICK
    dr = lowpass(r.normal(0, 1, n).astype(np.float32), 140) * 0.05
    dr[:int(SR * CUT)] = 0; mix_into(buf, dr, 0, 1.0)                                                # low dark drone
    mix_into(buf, SFXF["sting"] * 0.5, CUT + 0.15, 1.0)
    mix_into(buf, tone(900, 0.06, 0.15, 40), CUT + 0.22, 1.0)                                         # torch click on
    mix_into(buf, SFXF["whoosh"] * 0.4, METER - 0.1, 1.0)
    mix_into(buf, tone(110, 0.8, 0.3, 3) + tone(73, 0.8, 0.3, 3), METER + 0.1, 1.0)                    # «dun» on the box
    for k_ in range(3): mix_into(buf, tone(140, 0.25, 0.16, 8), SWEEP + 0.15 + k_ * 0.32, 1.0)        # heartbeat on the sweep
    for i in range(3): mix_into(buf, tone(660 + i * 220, 0.18, 0.2, 12), LINEUP + i * 0.2, 1.0)
    a = T("T2")
    for i, h in enumerate((1.49, 2.33, 3.36)): mix_into(buf, tone(700 + i * 180, 0.2, 0.18, 10), a + h, 1.0)
    for j in range(4): mix_into(buf, tone(2200, 0.04, 0.3, 60), Q + 0.2 + j * 0.07, 1.0)               # lights flicker back on
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), Q + 0.5 + k_ * 0.09, 1.0)
    mix_into(buf, tone(180, 0.5, 0.3, 4) + tone(120, 0.5, 0.3, 4), T("A1") + 2.0, 1.0)
    for i, t0 in enumerate((2.4, 2.9, 3.4)): mix_into(buf, tone(880 + i * 220, 0.2, 0.2, 10), T("C1") + t0, 1.0)
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 0.5: mix_into(buf, SFXF["whoosh"] * 0.25, s_["start"] - 0.1, 1.0)
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
