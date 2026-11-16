# «مين الكداب؟» — القضية 3: مين صوّر عزيزة؟  (H 1920x1080 + V 1080x1920 in one pass)
# render:  python ep.py audio  →  python ep.py part 0 2 & python ep.py part 1 2  →  concat  →  mux mix.wav
# Format v2: standalone; case-2 answer at the END (A1) + «شوفوا الحلقة اللي فاتت» + case-2 cover + like/follow/share (C1 reused from kaddab/02).
# Answer of THIS case (tell it at the end of case 4): عم بندق — in the photo the pillow next to Aziza is EMPTY and the blanket is thrown back
# on his side, so he was not asleep beside her. Shatta's laughing + Zalata = group admin are red herrings. The clue is never pointed at.
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/kaddab/03")
SERIES = "مين الكداب؟"; EPT = "مين صوّر عزيزة؟"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"; DJ = ROOT + "/brand/fonts/DejaVuSans-Bold.ttf"
SFXP = {"whoosh": "/trend/01/sfx/whoosh.mp3", "sting": "/trend/01/sfx/stinger.mp3", "creak": "/s1e9/sfx/creak.mp3",
        "steps": "/s1e10/sfx/footsteps.mp3"}
SFXF = {n: load_audio(ROOT + p) for n, p in SFXP.items()}

SUB = {"AZ1": "مين اللي صوّرني وأنا نايمة... ونزّل الصورة على جروب العمارة؟!",
       "T1": "الصورة اتبعتت الساعة تلاتة العصر... وقت نومة خالتي عزيزة!",
       "S1": "أنا كنت في التمرين من الضهر... ولسه راجع حالاً!",
       "Z1": "أنا أدمن الجروب آه... بس مش أنا اللي نزّلتها!",
       "B1": "أنا كنت نايم جنبها طول الوقت... ولا حسّيت بحاجة!",
       "T2": "مين فيهم الكداب؟ واحد... ولا اتنين... ولا تلاتة؟ بصّوا على الصورة كويس... واكتبوا في الكومنتات!",
       "A1": "وحل الفزورة اللي فاتت: الكداب كان شطة! عشان شعره كان مبلول... يعني هو اللي كان في الحمّام!",
       "C1": "ولو ما شفتوش الحلقة اللي فاتت... شوفوها! وما تنسوش اللايك والفولو والشير!", "LAUGH": ""}
WHO = {"AZ1": "aziza", "T1": "tota", "S1": "shatta", "Z1": "zalata", "B1": "bondo2", "T2": "tota", "A1": "nana", "C1": "nana", "LAUGH": "-"}
EXPR = {"AZ1": "shout", "T1": "smug", "S1": "neutral", "Z1": "flat", "B1": "neutral", "T2": "smug", "A1": "happy", "C1": "happy", "LAUGH": "laugh"}
load_lines(list(SUB))
ROOM = _ld(ROOT + "/daily/bg/bandaq_room.png")       # canonical «أوضة بندق وعزيزة» (docs/locations.md) — warm afternoon = 3 PM, fits the story
COVER2 = Image.open(ROOT + "/publish/thumbs/kaddab_e02_cover.jpg").convert("RGB")
LAUGH_D = 1.3                                         # audience laugh: only the first 1.3 s

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
WIDE = (1100, 640, 1.3)
t = say(0.1, "AZ1")                                                                           # first word at 0.1 s (hook rule)
shakes.append((0.15, 16))
PH0 = 0.1 + 1.85                                                                             # «ونزّل الصورة على الجروب» → phone insert
shot("room", 0.0, PH0, (1350, 690, 2.6), (1350, 700, 2.35), ease="crash")                   # CU Aziza: phone up + slipper
t1 = say(t + 0.15, "T1"); t = t1 + 0.1
PHZ = T("T1") + 2.7                                                                          # «وقت نومة خالتي عزيزة» → the photo fills the frame
shot("phone", PH0, PHZ, None, tin="zoom")
shot("photo", PHZ, t, None, tin="flash")
ENTER = t; LINEUP = ENTER + 1.25
shot("room", ENTER, LINEUP + 0.55, (900, 640, 1.22), WIDE, tin="whip")                      # the 3 come in through the door (called by her shout)
t = LINEUP + 0.55
s = t; t = say(t + 0.05, "S1") + 0.05; shot("room", s, t, (630, 715, 2.3), (630, 708, 2.45), tin="whipl")
LAUGH1 = t; say(t, "LAUGH"); shot("room", t, t + 0.95, (630, 708, 2.45), (630, 700, 2.65))      # Shatta can't hold his laugh (red herring)
t += 0.95
GLARE = t; shakes.append((GLARE + 0.1, 14)); shot("room", t, t + 0.75, (1350, 700, 2.5), (1350, 690, 2.8), tin="whip", ease="crash")  # Aziza: slipper up!
t += 0.75
s = t; t = say(t + 0.05, "Z1") + 0.1; shot("room", s, t, (870, 715, 2.3), (870, 708, 2.45), tin="whipl")
s = t; t = say(t + 0.05, "B1") + 0.15; shot("room", s, t, (1110, 715, 2.3), (1110, 708, 2.45), tin="whip")
ASK = t; t2 = say(t + 0.05, "T2"); a = T("T2")
shot("room", ASK, a + 1.4, (1570, 790, 2.8), (1570, 782, 3.0), tin="whip")                    # Tota + magnifier, to camera
shot("room", a + 1.4, a + 4.35, WIDE, (1130, 650, 1.38), tin="whipl")                       # 1… 2… 3 — badges light up on each word
REPRISE = a + 4.35; shot("photo2", REPRISE, a + 6.1, None, tin="zoom")                      # «بصّوا على الصورة كويس» — magnifier sweeps the photo
shot("room", a + 6.1, t2 + 0.3, WIDE, (1130, 650, 1.36), tin="whip")
t = t2 + 0.3
Q = t; shot("q", t, t + 1.2, None); t += 1.2
ANS = t; t = say(t + 0.25, "A1") + 0.35; shot("ans", ANS, t, None, tin="flash")
CTA = t; t = say(t + 0.15, "C1") + 0.8; shot("cta", CTA, t, None, tin="whip")
TOTAL = t

# ---------------- staging (world = Bandaq & Aziza's room 1920x1080) ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
POS = {"shatta": (630, 1010, 1.7), "zalata": (870, 1010, 1.7), "bondo2": (1110, 1012, 1.7), "aziza": (1350, 1012, 1.75), "tota": (1570, 1030, 2.0)}
DOOR = (300, 760)
NUMS = (("shatta", (230, 90, 40)), ("zalata", (60, 150, 80)), ("bondo2", (196, 40, 96)))

def arms_at(sched, tt, d=0.22):
    prev = sched[0][1]
    for i, (t0, pose) in enumerate(sched):
        if tt < t0: break
        if tt < t0 + d and i > 0: return (sched[i - 1][1], pose, (tt - t0) / d)
        prev = pose
    return prev

def body(who, x, y, s):
    S = s * CH[who]["scale"]; sh = y - 134 * S
    return S, sh, (x, sh - 56 * S)                                                          # scale, shoulder y, head centre

def hand(who, x, y, s, arms, side):
    S, sh, _ = body(who, x, y, s)
    A = {"down": ((x - 34 * S, sh + 72 * S), (x + 34 * S, sh + 72 * S)), "talk": ((x - 50 * S, sh + 52 * S), (x + 60 * S, sh + 8 * S)),
         "hold": ((x - 36 * S, sh + 70 * S), (x + 46 * S, sh + 30 * S)), "up": ((x - 70 * S, sh - 50 * S), (x + 70 * S, sh - 50 * S)),
         "hips": ((x - 48 * S, sh + 40 * S), (x + 48 * S, sh + 40 * S)), "point": ((x - 38 * S, sh + 68 * S), (x + 84 * S, sh - 6 * S))}
    if isinstance(arms, tuple): arms = arms[1] if arms[2] > 0.5 else arms[0]
    return A.get(arms, A["down"])[0 if side < 0 else 1]

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, walk=None, held=None, nod=0.0):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11 and expr not in ("sleepy", "laugh")
    if not talking and walk is None: lean += math.sin(tt * 1.7 + len(who)) * 0.06
    X, Y_ = W2S(cam, x, y); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, held, lean, walk, nod=nod)

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
os.chdir(ROOT + "/kaddab/03")

# ---------------- props drawn over the characters ----------------
def slipper(p, x, y, s, rot=0.0):
    c, sn = math.cos(rot), math.sin(rot)
    R = lambda dx, dy: (x + dx * c - dy * sn, y + dx * sn + dy * c)
    sole = [R(13 * s * math.cos(a / 16 * 2 * math.pi), 27 * s * math.sin(a / 16 * 2 * math.pi)) for a in range(16)]
    p.poly(sole, (70, 150, 210, 255), INK, 2 * s)                                            # rubber sole
    p.poly([R(-14 * s, -10 * s), R(14 * s, -10 * s), R(11 * s, 4 * s), R(-11 * s, 4 * s)], (240, 240, 240, 255), INK, 1.5 * s)   # strap

def magnifier(p, x, y, s):
    p.line([(x, y), (x + 14 * s, y - 26 * s)], (90, 60, 30, 255), 6 * s)
    p.ell(x + 22 * s, y - 42 * s, 17 * s, 17 * s, (200, 230, 255, 120), (40, 40, 46, 255), 4 * s)
    p.line([(x + 14 * s, y - 50 * s), (x + 20 * s, y - 54 * s)], (255, 255, 255, 220), 2.5 * s)

def sweat(p, cam, who, tt):
    x, y, s = POS[who]; S, sh, (hx, hy) = body(who, x, y, s); z = cam[2]
    for i, (dx, ph) in enumerate(((-30, 0.0), (34, 0.45), (-8, 0.8))):
        u = (tt * 0.9 + ph) % 1.0
        q = W2S(cam, hx + dx * S, hy - 30 * S + u * 50 * S)
        p.ell(q[0], q[1], 3.2 * S * z, 5 * S * z, (190, 225, 255, int(230 * (1 - u))), (60, 110, 170, int(255 * (1 - u))), 1 * z)

def glint(fr, cam, tt, t0):
    """Zalata's glasses flash a little star"""
    u = kk(tt, t0, t0 + 0.45)
    if not 0 < u < 1: return
    x, y, s = POS["zalata"]; S, sh, (hx, hy) = body("zalata", x, y, s)
    q = W2S(cam, hx + 16 * S, hy + 2 * S); r = 40 * cam[2] * math.sin(u * math.pi)
    d = ImageDraw.Draw(fr, "RGBA")
    d.polygon([(q[0], q[1] - r), (q[0] + r * 0.18, q[1] - r * 0.18), (q[0] + r, q[1]), (q[0] + r * 0.18, q[1] + r * 0.18),
               (q[0], q[1] + r), (q[0] - r * 0.18, q[1] + r * 0.18), (q[0] - r, q[1]), (q[0] - r * 0.18, q[1] - r * 0.18)], fill=(255, 255, 255, 240))

def door_open(p, cam, tt):
    """the room door (left) opens while the three come in"""
    k = ease(kk(tt, ENTER - 0.1, ENTER + 0.35)) * (1 - ease(kk(tt, LINEUP + 0.1, LINEUP + 0.5)))
    if k <= 0: return
    a = W2S(cam, 215, 230); b = W2S(cam, 402, 745)
    p.rect(a[0], a[1], b[0], b[1], (34, 26, 20, 255), None)                                  # dark doorway (the stairwell)
    lw = (b[0] - a[0]) * (1 - 0.82 * k)
    p.poly([(a[0], a[1]), (a[0] + lw, a[1] + 14 * k * cam[2]), (a[0] + lw, b[1] - 14 * k * cam[2]), (a[0], b[1])], (92, 58, 36, 255), INK, 2 * cam[2])

# ---------------- the photo (the clue is IN it: the pillow next to her is empty, his side of the blanket thrown back) ----------------
def make_photo():
    PW, PHh = 960, 640
    im = Image.new("RGBA", (int(PW * SS), int(PHh * SS)), (232, 208, 172, 255)); p = P(im)
    p.rect(0, 0, PW, 60, (214, 186, 150, 255), None)
    p.rect(-20, 60, PW + 20, 250, (122, 74, 42, 255), INK, 4, 40)                           # headboard
    for x_ in range(80, PW, 160): p.line([(x_, 90), (x_, 230)], (98, 58, 32, 255), 5)
    p.rect(-20, 210, PW + 20, PHh + 40, (246, 242, 234, 255), INK, 3)                         # sheet
    for (x0, x1) in ((70, 440), (520, 890)):                                                 # two pillows
        p.rect(x0, 200, x1, 330, (255, 236, 240, 255), INK, 3, 50)
        p.line([(x0 + 40, 300), (x1 - 40, 300)], (230, 200, 210, 255), 3)
    ch = Image.new("RGBA", im.size, (0, 0, 0, 0)); pc = P(ch)                                 # Aziza asleep, mouth wide open
    draw_char(pc, "aziza", 255, 520, 1.55, "sleepy", 0.95, 0, False, "down", 0.0)
    ch = ch.rotate(14, center=(int(255 * SS), int(250 * SS)), resample=Image.BICUBIC)
    im.alpha_composite(ch)
    p.ell(276, 296, 5, 8, (150, 205, 255, 255), (40, 90, 160, 255), 1.5)                    # drool drop
    blanket = [(-20, 372), (60, 352), (150, 340), (330, 336), (460, 352), (520, 372), (560, 380), (PW + 20, 380), (PW + 20, PHh + 40), (-20, PHh + 40)]
    p.poly(blanket, (186, 66, 92, 255), INK, 4)                                              # blanket (flowers)
    for i in range(26):
        fx, fy = 30 + (i * 137) % 900, 420 + (i * 71) % 200
        for a_ in range(5):
            q = (fx + math.cos(a_ * 1.26) * 10, fy + math.sin(a_ * 1.26) * 10); p.ell(q[0], q[1], 6, 6, (246, 196, 206, 255), None)
        p.ell(fx, fy, 5, 5, (250, 220, 90, 255), None)
    p.ell(260, 470, 190, 70, (196, 76, 102, 255), None)                                      # her body under it
    p.poly([(560, 380), (PW + 20, 380), (PW + 20, 520), (720, 470)], (232, 228, 220, 255), INK, 3)   # HIS side: thrown back, empty
    p.poly([(560, 380), (720, 470), (PW + 20, 520), (PW + 20, 560), (700, 500), (548, 396)], (150, 50, 74, 255), INK, 3)
    out = im.resize((PW, PHh), Image.LANCZOS).convert("RGB")
    return ImageEnhance.Color(out).enhance(0.92)
PHOTO = make_photo()

def chat_screen(tt, w, h, t0):
    """generic group chat (own design, no real app branding): header + the photo message + seen counter + 😂 reactions"""
    sc = Image.new("RGB", (w, h), (236, 229, 221)); d = ImageDraw.Draw(sc, "RGBA")
    d.rectangle([0, 0, w, 130], fill=(52, 40, 74))
    d.ellipse([w - 110, 28, w - 36, 102], fill=(255, 214, 90))
    lzt(sc, w - 73, 66, "ع", 40, (52, 40, 74), (255, 214, 90))
    lzt(sc, w / 2 - 20, 52, "سكان عمارة نعناعة", 44, (255, 255, 255), (52, 40, 74))
    lzt(sc, w / 2 - 20, 100, "62 عضو", 28, (200, 190, 230), (52, 40, 74))
    k = popk(tt, t0 + 0.25, 0.3)                                                              # the photo message pops in
    if k > 0:
        bx0, by0, bx1 = 22, 170, w - 22
        bh = int((bx1 - bx0 - 24) * 2 / 3)
        d.rounded_rectangle([bx0, by0, bx1, by0 + bh + 110], 26, fill=(255, 255, 255))
        ph = PHOTO.resize((bx1 - bx0 - 24, bh), Image.LANCZOS); sc.paste(ph, (bx0 + 12, by0 + 12))
        lzt(sc, bx0 + 175, by0 + bh + 60, "3:00", 40, (90, 90, 100), (255, 255, 255), font=DJ); lzt(sc, bx0 + 85, by0 + bh + 56, "م", 44, (90, 90, 100), (255, 255, 255))
        n = 3 + int(44 * ease(kk(tt, t0 + 0.6, t0 + 3.0)))                                   # seen counter racing
        d.ellipse([bx1 - 250, by0 + bh + 40, bx1 - 200, by0 + bh + 80], outline=(90, 90, 100), width=5)
        d.ellipse([bx1 - 233, by0 + bh + 52, bx1 - 217, by0 + bh + 68], fill=(90, 90, 100))
        lzt(sc, bx1 - 120, by0 + bh + 60, str(n), 42, (90, 90, 100), (255, 255, 255), font=DJ)
        for i in range(min(9, int((tt - t0 - 0.9) / 0.28) + 1) if tt > t0 + 0.9 else 0):    # laughing reactions keep coming
            rx = bx0 + 70 + (i % 5) * 100; ry = by0 + bh + 190 + (i // 5) * 96
            r = 38 * popk(tt, t0 + 0.9 + i * 0.28, 0.2)
            d.ellipse([rx - r, ry - r, rx + r, ry + r], fill=(255, 205, 50), outline=(150, 100, 20), width=3)
            d.arc([rx - r * 0.55, ry - r * 0.5, rx - r * 0.1, ry - r * 0.05], 200, 340, fill=(80, 50, 10), width=4)
            d.arc([rx + r * 0.1, ry - r * 0.5, rx + r * 0.55, ry - r * 0.05], 200, 340, fill=(80, 50, 10), width=4)
            d.chord([rx - r * 0.55, ry - r * 0.05, rx + r * 0.55, ry + r * 0.65], 0, 180, fill=(120, 40, 30))
            d.ellipse([rx - r * 0.95, ry - r * 0.2, rx - r * 0.6, ry + r * 0.25], fill=(120, 200, 255))
            d.ellipse([rx + r * 0.6, ry - r * 0.2, rx + r * 0.95, ry + r * 0.25], fill=(120, 200, 255))
        hl = kk(tt, T("T1") + 1.1, T("T1") + 1.3) * (1 - kk(tt, T("T1") + 2.5, T("T1") + 2.7))   # «الساعة تلاتة العصر»: the time gets circled
        if hl > 0:
            cx, cy = bx0 + 145, by0 + bh + 60
            d.ellipse([cx - 105, cy - 46, cx + 105, cy + 46], outline=(230, 40, 40, int(255 * hl)), width=9)
    return sc

def phone_insert(tt, sh):
    u = kk(tt, sh["start"], sh["end"])
    cam = (1350 - 960 / 2.3, 700 - 540 / 2.3, 2.3)
    fr = bg_crop(ROOM, cam).resize((W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(14))
    fr = ImageEnhance.Brightness(fr).enhance(0.55)
    pw, ph = 600, 1150
    scr = chat_screen(tt, pw - 40, ph - 80, sh["start"])
    phone = Image.new("RGBA", (pw, ph), (0, 0, 0, 0)); d = ImageDraw.Draw(phone)
    d.rounded_rectangle([0, 0, pw - 1, ph - 1], 70, fill=(24, 24, 30), outline=(80, 80, 90), width=6)
    phone.paste(scr, (20, 50)); d.rounded_rectangle([pw / 2 - 70, 14, pw / 2 + 70, 36], 11, fill=(10, 10, 12))
    zz = 0.92 + 0.10 * ease(u)
    phone = phone.resize((int(pw * zz), int(ph * zz)), Image.LANCZOS).rotate(-3 + 3 * ease(u), expand=True, resample=Image.BICUBIC)
    slide = (1 - ease(kk(tt, sh["start"], sh["start"] + 0.3))) * 700
    fr.paste(phone, (int(W / 2 - phone.size[0] / 2), int(H / 2 - phone.size[1] / 2 + 40 + slide)), phone)
    return fr

def photo_full(tt, sh, lens=False):
    u = kk(tt, sh["start"], sh["end"]); zz = 1.0 + 0.06 * u
    fr = Image.new("RGB", (W, H), (12, 10, 14))
    pw = int(1500 * zz); ph = int(pw * 2 / 3)
    big = PHOTO.resize((pw, ph), Image.LANCZOS)
    card = Image.new("RGB", (pw + 40, ph + 40), (250, 250, 248)); card.paste(big, (20, 20))
    ox, oy = int(W / 2 - card.size[0] / 2), int(H / 2 - card.size[1] / 2)
    fr.paste(card, (ox, oy))
    if lens:                                                                                 # magnifier sweeps the WHOLE photo (never stops on the clue)
        v = ease(u); lx = ox + 20 + pw * (0.12 + 0.76 * v); ly = oy + 20 + ph * (0.42 + 0.12 * math.sin(v * math.pi * 2))
        r = 170; m = 1.7
        sx, sy = (lx - ox - 20) / pw * PHOTO.size[0], (ly - oy - 20) / ph * PHOTO.size[1]
        src = PHOTO.resize((int(pw * m), int(ph * m)), Image.LANCZOS)
        cx_, cy_ = sx / PHOTO.size[0] * src.size[0], sy / PHOTO.size[1] * src.size[1]
        crop = src.crop((int(cx_ - r), int(cy_ - r), int(cx_ + r), int(cy_ + r)))
        mask = Image.new("L", crop.size, 0); ImageDraw.Draw(mask).ellipse([0, 0, 2 * r - 1, 2 * r - 1], fill=255)
        fr.paste(crop, (int(lx - r), int(ly - r)), mask)
        d = ImageDraw.Draw(fr, "RGBA")
        d.ellipse([lx - r - 6, ly - r - 6, lx + r + 6, ly + r + 6], outline=(40, 40, 46), width=16)
        d.line([(lx + r * 0.72, ly + r * 0.72), (lx + r * 1.45, ly + r * 1.45)], fill=(110, 70, 36), width=34)
        lzt(fr, W / 2, 70, "بُصّ كويس!", 80, (255, 214, 90))
    return fr

def q_card(tt, sh):
    fr = ImageEnhance.Brightness(frame_cache(sh["start"] - 0.05)).enhance(0.45).filter(ImageFilter.GaussianBlur(5)).convert("RGBA")
    lzt(fr, W / 2, 300, "اكتب رقم الكداب في الكومنتات!", int(92 * popk(tt, sh["start"] + 0.05, 0.3)), (255, 214, 90))
    for i, (_, col) in enumerate(NUMS):
        badge(fr, W / 2 + (i - 1) * 200, 470, str(i + 1), 1.3 * popk(tt, sh["start"] + 0.3 + i * 0.15), col)
    lzt(fr, W / 2, 640, "الدليل في الصورة...", int(60 * popk(tt, sh["start"] + 0.75)), (255, 255, 255))
    return fr.convert("RGB")

def ans_card(tt, sh):
    """answer of case 2: Shatta lied — his hair was wet, he was the one in the bathroom"""
    st = T("A1"); fr = Image.new("RGB", (W, H), (16, 20, 44)); d = ImageDraw.Draw(fr, "RGBA")
    for i in range(18):
        a0 = i * 20 + tt * 6; a_ = math.radians(a0); b = math.radians(a0 + 9)
        d.polygon([(W / 2, H * 0.6), (W / 2 + 2400 * math.cos(a_), H * 0.6 + 2400 * math.sin(a_)), (W / 2 + 2400 * math.cos(b), H * 0.6 + 2400 * math.sin(b))], fill=(30, 38, 80, 255))
    lzt(fr, W / 2, 110, "حل الفزورة اللي فاتت", int(86 * popk(tt, sh["start"] + 0.15)), (255, 214, 90))
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    caught = tt >= st + 1.6
    x, y, s = 640, 1080 + 130, 3.3
    draw_char(p, "shatta", x, y, s, "scared" if caught else "sleepy", 0.0, 1, ((tt + 0.3) % 3.4) < 0.1, "scared" if caught else "down", tt, None, 0.0, None)
    S = s * CH["shatta"]["scale"]; hy = y - 190 * S
    for i, (dx, ph) in enumerate(((-46, 0.0), (40, 0.37), (-20, 0.71), (52, 0.18))):      # wet hair dripping (the case-2 clue)
        u = (tt * 1.1 + ph) % 1.0
        p.ell(x + dx * S, hy - 20 * S + u * 160 * S, 4.2 * S, 6.5 * S, (150, 205, 255, 230), (40, 90, 160, 255), 1.2 * S)
    fr.paste(lay.resize((W, H), Image.LANCZOS), (0, 0), lay.resize((W, H), Image.LANCZOS))
    if caught:
        lzt(fr, 640, 250, "الكداب!", int(150 * popk(tt, st + 1.6, 0.25)), (255, 255, 255), (170, 20, 20), rot=8)
    if tt >= st + 3.0:                                                                    # big water drop + «شعره كان مبلول»
        k = popk(tt, st + 3.0, 0.3); cx, cy = 1360, 400; s2 = 1.4 * k
        d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([cx - 270 * k, cy - 250 * k, cx + 270 * k, cy + 250 * k], 40, fill=(8, 8, 16, 230), outline=(255, 214, 90, 255), width=6)
        d.ellipse([cx - 80 * s2, cy - 20 * s2, cx + 80 * s2, cy + 140 * s2], fill=(120, 190, 255))
        d.polygon([(cx - 70 * s2, cy + 30 * s2), (cx + 70 * s2, cy + 30 * s2), (cx, cy - 150 * s2)], fill=(120, 190, 255))
        d.ellipse([cx - 40 * s2, cy + 10 * s2, cx - 12 * s2, cy + 60 * s2], fill=(230, 245, 255))
        lzt(fr, cx, cy + 300 * k, "شعره كان مبلول!", int(78 * k), (255, 214, 90))
    if tt >= st + 4.5:
        lzt(fr, 1360, 820, "يعني هو اللي كان في الحمّام!", int(54 * popk(tt, st + 4.5)), (255, 255, 255))
    return fr

def cta_card(tt, sh):
    fr = Image.new("RGB", (W, H), (20, 12, 10)); d = ImageDraw.Draw(fr, "RGBA")
    for i in range(18):
        a0 = i * 20 - tt * 6; a_ = math.radians(a0); b = math.radians(a0 + 9)
        d.polygon([(W / 2, H / 2), (W / 2 + 2400 * math.cos(a_), H / 2 + 2400 * math.sin(a_)), (W / 2 + 2400 * math.cos(b), H / 2 + 2400 * math.sin(b))], fill=(44, 24, 16, 255))
    k = popk(tt, sh["start"] + 0.15, 0.3)
    if k > 0:                                                                             # case-2 cover, tilted like a card
        ch = int(690 * k); cw = int(ch * 1080 / 1920)
        cov = COVER2.resize((cw, ch), Image.LANCZOS)
        fr_c = Image.new("RGBA", (cw + 24, ch + 24), (255, 214, 90, 255)); fr_c.paste(cov, (12, 12))
        fr_c = fr_c.rotate(-4, expand=True, resample=Image.BICUBIC)
        fr.paste(fr_c, (int(560 - fr_c.size[0] / 2), int(480 - fr_c.size[1] / 2)), fr_c)
        lzt(fr, 560, 72, "شوفوا القضية 2", int(70 * k), (255, 214, 90))
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

# ---------------- frame ----------------
def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "phone": return finish(phone_insert(tt, sh), tt)
    if sh["set"] == "photo": return finish(photo_full(tt, sh), tt)
    if sh["set"] == "photo2": return finish(photo_full(tt, sh, lens=True), tt)
    if sh["set"] == "q": return finish(q_card(tt, sh), tt)
    if sh["set"] == "ans": return finish(ans_card(tt, sh), tt)
    if sh["set"] == "cta": return finish(cta_card(tt, sh), tt)
    cam = cam_at(sh, tt); z = cam[2]
    img = bg_crop(ROOM, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    door_open(p, cam, tt)
    # --- the three suspects come in through the door (only after the phone insert; before that they are not in the room)
    ent = {}
    for i, (who, _) in enumerate(NUMS):
        x, y, s = POS[who]; w0 = ENTER + i * 0.28; k = kk(tt, w0, w0 + 1.0); e = ease(k)
        ent[who] = (lerp(DOOR[0], x, e), lerp(DOOR[1] + 230, y, e), s * lerp(0.82, 1.0, e), (tt * 8 if 0 < k < 1 else None), k)
    # --- expressions / arms
    sex, zex, bex, aex, tex = "neutral", "flat", "neutral", "angry", "smug"
    if LAUGH1 <= tt < GLARE + 0.15: sex = "laugh"
    if GLARE + 0.15 <= tt < GLARE + 1.6: sex = "scared"
    if tt < ENTER: aex = "shout"
    if LAUGH1 <= tt < GLARE: aex = "angry"
    if tt >= ASK: sex, zex, bex = "neutral", "flat", "neutral"
    sarms = arms_at([(0, "down"), (T("S1"), "talk"), (T("S1") + DUR["S1"], "down"), (GLARE + 0.15, "scared"), (GLARE + 1.4, "down")], tt)
    zarms = arms_at([(0, "hold"), (T("Z1") + 0.2, "talk"), (T("Z1") + DUR["Z1"], "hold")], tt)
    barms = arms_at([(0, "down"), (T("B1") + 0.3, "talk"), (T("B1") + DUR["B1"], "down")], tt)
    aarms = arms_at([(0, "up"), (1.8, "hold"), (ENTER, "hips"), (GLARE, "up"), (GLARE + 0.75, "hips")], tt)
    tarms = arms_at([(0, "hold"), (ASK, "talk"), (T("T2") + 1.4, "hold")], tt)
    order = []
    if tt >= ENTER:
        for who, _ in NUMS:
            x, y, s, wk, k = ent[who]
            if k > 0: order.append((y, who, x, s, wk))
    order.sort()
    for y, who, x, s, wk in order:
        if who == "shatta":
            person(lay, cam, "shatta", x, y, s, tt, sex, 1 if LAUGH1 <= tt < GLARE + 1.6 else 0, sarms, walk=wk)
            hx_, hy_ = hand("shatta", x, y, s, sarms if wk is None else "down", -1); q = W2S(cam, hx_, hy_)
            ball(p, q[0] - 10 * s * z, q[1] - 6 * s * z, 22 * s * z)                           # football under his arm (just back from practice)
            if wk is None and tt >= LINEUP: sweat(p, cam, "shatta", tt)
        elif who == "zalata":
            person(lay, cam, "zalata", x, y, s, tt, zex, 0, zarms, walk=wk, held="phone")
        else:
            person(lay, cam, "bondo2", x, y, s, tt, bex, 0, barms, walk=wk)
    ax, ay, as_ = POS["aziza"]
    person(lay, cam, "aziza", ax, ay, as_, tt, aex, -1 if ENTER <= tt < ASK else 0, aarms, held="phone")
    lh = hand("aziza", ax, ay, as_, aarms, -1); q = W2S(cam, *lh)
    slipper(p, q[0], q[1] - 8 * z, as_ * z, -0.5 if aarms == "up" else 0.2)
    person(lay, cam, "tota", *POS["tota"], tt, tex, -1, tarms)
    rh = hand("tota", *POS["tota"], tarms, 1); q = W2S(cam, *rh); magnifier(p, q[0], q[1], POS["tota"][2] * z)
    lay = tint_layer(lay, (255, 236, 210)); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    glint(fr, cam, tt, T("Z1") + 0.2)
    # --- number badges + highlight on «واحد / اتنين / تلاتة»
    if tt >= LINEUP:
        a = T("T2"); hit = {0: (a + 1.58, a + 2.3), 1: (a + 2.43, a + 3.2), 2: (a + 3.43, a + 4.2)}
        for i, (who, col) in enumerate(NUMS):
            x, y, s = POS[who]; S_, _, (_, hy_) = body(who, x, y, s); q = W2S(cam, x, hy_ - 46 * S_ - 52)
            pulse = 1 + (0.12 * math.sin(tt * 8) if tt >= a + 6.1 else 0)
            h0, h1 = hit[i]
            if h0 <= tt < h1: pulse = 1 + 0.45 * math.sin(kk(tt, h0, h1) * math.pi)
            badge(fr, q[0], q[1], str(i + 1), min(1.1, z * 0.75) * popk(tt, LINEUP + i * 0.2) * pulse, col)
    if GLARE <= tt < GLARE + 0.6:
        lzt(fr, W * 0.30, H * 0.22, "!!!", int(170 * popk(tt, GLARE, 0.2)), (255, 80, 60))
    return finish(fr, tt)

HOOK1, HOOK2 = "حد صوّر خالتي عزيزة", "وهي نايمة!"
def hook_banner(fr, tt):
    if tt >= 3.0: return
    a = int(255 * min(1, (3.0 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
    d.rounded_rectangle([W / 2 - 640, 30, W / 2 + 640, 160], 30, fill=(20, 12, 8, int(a * 0.8)))
    lzt(fr, W / 2, 95, HOOK1 + " " + HOOK2, 72, (255, 214, 90), alpha=a)

_render = render
def render(out_h, out_v, stills=None, t0=0.0, t1=None):
    base_frame = frame
    def frame2(tt):
        fr = base_frame(tt); hook_banner(fr, tt); return fr
    globals()["frame"] = frame2
    _render(out_h, out_v, stills, t0, t1)

def vertical(fr, tt):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = ImageEnhance.Brightness(small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.35)
    bgv.paste(fr.resize((1080, 608), Image.LANCZOS), (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(255, 214, 90)); d.rectangle([0, 1168, 1080, 1171], fill=(255, 214, 90))
    if tt < ANS:
        lzt(bgv, 540, 240, HOOK1, 100, (255, 255, 255)); lzt(bgv, 540, 390, HOOK2 + " 📸".replace(" 📸", ""), 120, (255, 214, 90))
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
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(47)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 400) * 0.025, 0, 1.0)          # afternoon room tone / distant street
    for k_ in range(14):                                                                     # a few birds outside the window
        st = 0.8 + k_ * 2.9 + r.uniform(0, 1.2)
        if st < TOTAL - 8: mix_into(buf, tone(3200 + r.uniform(-300, 300), 0.07, 0.025, 30) + tone(3900, 0.07, 0.02, 35), st, 1.0)
    mix_into(buf, SFXF["sting"] * 0.45, 0.0, 1.0)
    mix_into(buf, SFXF["whoosh"] * 0.35, PH0 - 0.1, 1.0)
    mix_into(buf, tone(1320, 0.16, 0.25, 18) + tone(1760, 0.16, 0.2, 14), PH0 + 0.25, 1.0)    # message ping
    for j in range(9): mix_into(buf, tone(1100, 0.05, 0.08, 40), PH0 + 0.9 + j * 0.28, 1.0)  # reactions pop
    mix_into(buf, tone(900, 0.08, 0.06, 30), PHZ, 1.0)                                       # camera-shutter-ish click
    mix_into(buf, lowpass(r.normal(0, 1, int(SR * 0.06)).astype(np.float32), 5000) * 0.25, PHZ + 0.04, 1.0)
    mix_into(buf, SFXF["creak"] * 0.5, ENTER - 0.05, 1.0)
    mix_into(buf, SFXF["steps"] * 0.4, ENTER + 0.1, 1.0)
    for i in range(3): mix_into(buf, tone(660 + i * 220, 0.18, 0.2, 12), LINEUP + i * 0.2, 1.0)
    mix_into(buf, SFXF["whoosh"] * 0.5, GLARE - 0.05, 1.0)
    mix_into(buf, tone(140, 0.35, 0.35, 6) + tone(95, 0.35, 0.3, 6), GLARE + 0.1, 1.0)       # slipper «thump» stab
    a = T("T2")
    for i, h in enumerate((1.58, 2.43, 3.43)): mix_into(buf, tone(700 + i * 180, 0.2, 0.18, 10), a + h, 1.0)
    mix_into(buf, SFXF["sting"] * 0.3, REPRISE, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), Q + k_ * 0.09, 1.0)
    mix_into(buf, tone(180, 0.5, 0.3, 4) + tone(120, 0.5, 0.3, 4), T("A1") + 1.6, 1.0)       # «الكداب!» stamp
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
    elif sys.argv[1:2] == ["photo"]: PHOTO.save("photo.png")
    elif sys.argv[1:2] == ["times"]:
        for s_ in shots: print(s_["set"], round(s_["start"], 2), round(s_["end"], 2), s_.get("tin", ""))
        for st, k in lines: print(k, round(st, 2))
    elif sys.argv[1:2] == ["part"]:
        i, n = int(sys.argv[2]), int(sys.argv[3]); a = round(TOTAL * i / n * FPS) / FPS; b = round(TOTAL * (i + 1) / n * FPS) / FPS
        render(f"h_{i}.mp4", f"v_{i}.mp4", None, a, b)
    elif sys.argv[1:2] == ["audio"]: build_audio()
