# «يوميات شطة وزلطة» — «قوله يا بندق!» (user idea 22/11) — growth_rules: native 9:16, phrase subs + yellow key word + speaker name,
#   hook 3 s, motion+sound on frame 1, share/follow end card, own cover.
# Bandaq & Aziza on the red sofa (canonical «أوضة بندق وعزيزة», sofa drawn in code as in daily/11).
# He defends her on the phone («لا يا ماما!»), she whispers more complaints for him to pass on, glowing with hearts…
# «كنت بتكلم مامتك؟» — «لأ… مامتِك إنتي!» — hearts POP, crash zoom on her shock «أمي أنا؟!» + audience laugh.
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/daily/17")
SERIES = "يوميات شطة وزلطة"; EPT = "قوله يا بندق!"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"
SFXF = {n: load_audio(ROOT + f"/trend/01/sfx/{n}.mp3") for n in ("whoosh", "gasp")}
SUB = {"B1": "لا يا ماما! عزيزة مش خدّامة! كل ما تيجي عندكم… طبيخ… ومواعين… ومسح!",
       "AZ1": "قول لها يا بندق… قول لها إن ضهري واجعني… ومش قادرة!",
       "B2": "وكمان هي تعبانة ومش قادرة! مراتي ملكة… والملكة مش بتاعة مواعين!",
       "B4": "ماشي يا ماما… مع السلامة!", "AZ2": "يا حبيبي يا بندق! ربنا يخليك ليا… هو انت كنت بتكلم مامتك؟",
       "B3": "لأ… مامتِك إنتي!", "AZ3": "أمي أنا؟!", "GROUP": ""}
CHUNKS = {"B1": [(0.0, "لا يا ماما!", "ماما"), (1.15, "عزيزة مش خدّامة!", "مش خدّامة"), (3.2, "كل ما تيجي عندكم…", None),
                 (4.55, "طبيخ… ومواعين… ومسح!", "ومسح")],
          "AZ1": [(0.0, "قول لها يا بندق…", "قول لها"), (2.2, "قول لها إن ضهري واجعني…", "ضهري"), (4.45, "ومش قادرة!", "مش قادرة")],
          "B2": [(0.0, "وكمان هي تعبانة ومش قادرة!", "تعبانة"), (2.65, "مراتي ملكة…", "ملكة"), (4.5, "والملكة مش بتاعة مواعين!", "مواعين")],
          "B4": [(0.0, "ماشي يا ماما…", "ماما"), (1.62, "مع السلامة!", None)],
          "AZ2": [(0.0, "يا حبيبي يا بندق!", "حبيبي"), (2.3, "ربنا يخليك ليا…", None), (4.35, "هو انت كنت بتكلم مامتك؟", "مامتك")],
          "B3": [(0.0, "لأ…", None), (1.0, "مامتِك إنتي!", "مامتِك")],
          "AZ3": [(0.0, "أمي أنا؟!", "أمي أنا؟!")]}
WHO = {"B1": "bondo2", "B2": "bondo2", "B4": "bondo2", "B3": "bondo2", "AZ1": "aziza", "AZ2": "aziza", "AZ3": "aziza", "GROUP": "-"}
NAME = {"bondo2": ("بندق", (230, 170, 110)), "aziza": ("عزيزة", (255, 110, 170))}
EXPR = {"B1": "angry", "AZ1": [(0, "happy"), (0.4, "sleepy")], "B2": "smug", "B4": "happy", "AZ2": [(0, "happy"), (0.7, "neutral")],
        "B3": "neutral", "AZ3": "shock", "GROUP": "laugh"}
load_lines(list(SUB))
ROOM = _ld(ROOT + "/daily/bg/bandaq_room.png")

# ---------------- staging (world = room 1920x1080; sofa as daily/11) ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
AZ = (790, 800, 1.8); BD = (1140, 800, 1.8)                 # (x, hip-on-seat y, scale)
SOFA = (560, 1370, 800)

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
CU_B_H, CU_B_V = (1150, 640, 2.3), (1140, 640, 2.6)
CU_A_H, CU_A_V = (780, 640, 2.3), (790, 640, 2.6)
TWO_H, TWO_V = (965, 690, 1.7), (965, 640, 1.8)
t = say(0.1, "B1"); shakes.append((0.15, 12)); b1 = T("B1")
shot("room", 0.0, b1 + 3.2, (1150, 640, 2.8), CU_B_H, ease="crash", v=((1140, 640, 3.0), CU_B_V))          # frame 1: crash-in on him, on the phone
shot("room", b1 + 3.2, t + 0.1, TWO_H, (965, 680, 1.8), tin="whip", v=(CU_A_V, (790, 630, 2.75)))         # «طبيخ ومواعين ومسح» — she glows
s = t + 0.1; t = say(s + 0.1, "AZ1") + 0.1
shot("room", s, t, CU_A_H, (800, 630, 2.55), tin="whipl", v=(CU_A_V, (800, 630, 2.85)))                      # she whispers, leaning to him
s = t; t = say(s + 0.05, "B2") + 0.05; b2 = T("B2")
shot("room", s, b2 + 2.6, (1150, 690, 2.0), (1150, 680, 2.15), tin="whip", v=((1140, 680, 2.2), (1140, 670, 2.35)))  # repeating it loud
shot("room", b2 + 2.6, t, (1150, 610, 2.4), (1150, 600, 2.75), tin="whipl", v=((1140, 610, 2.7), (1140, 600, 3.0)))  # hero push-in «مراتي ملكة»
s = t; t = say(s + 0.05, "B4") + 0.15; HANG = T("B4") + DUR["B4"] - 0.2
shot("room", s, t, TWO_H, (965, 690, 1.78), tin="whip", v=(TWO_V, (965, 640, 1.85)))                        # hangs up
s = t; t = say(s + 0.1, "AZ2") + 0.1; a2 = T("AZ2")
shot("room", s, a2 + 4.3, (790, 640, 2.4), (790, 630, 2.7), tin="whipl", v=((790, 640, 2.7), (790, 630, 3.0)))    # melting, hearts
shot("room", a2 + 4.3, t, TWO_H, (965, 685, 1.78), tin="whip", v=(TWO_V, (965, 640, 1.85)))                    # «كنت بتكلم مامتك؟»
s = t; t = say(s + 0.05, "B3") + 0.05; REVEAL = T("B3") + 1.0
shot("room", s, REVEAL, CU_B_H, (1150, 630, 2.45), tin="whip", v=(CU_B_V, (1140, 630, 2.8)))                  # «لأ…»
shot("room", REVEAL, t, CU_B_H, (1150, 625, 2.6), v=(CU_B_V, (1140, 625, 2.9)))                               # «مامتِك إنتي!»
SHOCK = t; shakes.append((SHOCK + 0.05, 18))
t = say(SHOCK + 0.15, "AZ3")
shot("room", SHOCK, t + 0.25, (790, 600, 3.3), (790, 595, 3.55), tin="whipl", ease="crash", v=((790, 600, 3.4), (790, 595, 3.7)))  # crash zoom on her shock
LAUGH = t - 0.35; say(LAUGH, "GROUP"); LU = min(2.6, DUR["GROUP"])
shot("room", t + 0.25, LAUGH + LU, TWO_H, (965, 700, 1.7), tin="whip", v=((965, 640, 1.8), (1000, 640, 1.85)))   # she turns on him, he grins
t = LAUGH + LU
shot("end", t, t + 2.4, None, v=None); t += 2.4
TOTAL = t

def vcam(sh, tt):
    c0, c1 = sh["v"]; k = ease((tt - sh["start"]) / max(0.01, sh["end"] - sh["start"]), sh.get("ease"))
    cx, cy, z = [a + (b - a) * k for a, b in zip(c0, c1)]; z = max(z, 1920 / 1080)
    shake = 0
    for st, amp in shakes:
        if 0 <= tt - st < 0.45: shake = max(shake, amp * (1 - (tt - st) / 0.45))
    cw, ch = 1080 / z, 1920 / z
    x0 = min(max(cx - cw / 2 + math.sin(tt * 0.9) * 3, 0), 1920 - cw); y0 = min(max(cy - ch / 2 + math.sin(tt * 1.3) * 2, 0), 1080 - ch)
    if shake: x0 = min(max(x0 + rng.normal(0, shake / z), 0), 1920 - cw); y0 = min(max(y0 + rng.normal(0, shake / z), 0), 1080 - ch)
    return x0, y0, z

# ---------------- drawing ----------------
def arms_at(sched, tt, d=0.22):
    prev = sched[0][1]
    for i, (t0, pose) in enumerate(sched):
        if tt < t0: break
        if tt < t0 + d and i > 0: return (sched[i - 1][1], pose, (tt - t0) / d)
        prev = pose
    return prev

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, held=None, sit=0, nod=0.0):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    if k == "AZ1" and who == "aziza": mouth *= 0.55                                     # whisper
    blink = ((tt + len(who) * 0.37) % 3.6) < 0.11 and expr not in ("sleepy", "laugh", "shock", "angry")
    if not talking: lean += math.sin(tt * 1.7 + len(who)) * 0.04
    X, Y_ = W2S(cam, x, y); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, held, lean, None, sit=sit, nod=nod)

SOF = (150, 62, 58, 255); SOF_D = (112, 42, 40, 255); SOF_L = (178, 84, 76, 255)
def sofa_back(p, cam):
    z = cam[2]; x0, x1, sy = SOFA
    a = W2S(cam, x0, sy - 230); b = W2S(cam, x1, sy + 6); p.rect(a[0], a[1], b[0], b[1], SOF_D, INK, 3 * z, 26 * z)
    for i in range(3):
        cx = x0 + 40 + i * (x1 - x0 - 80) / 3
        a = W2S(cam, cx + 6, sy - 205); b = W2S(cam, cx + (x1 - x0 - 80) / 3 - 6, sy - 10); p.rect(a[0], a[1], b[0], b[1], SOF, INK, 2.5 * z, 18 * z)
    a = W2S(cam, x0 - 10, sy); b = W2S(cam, x1 + 10, sy + 70); p.rect(a[0], a[1], b[0], b[1], SOF_L, INK, 3 * z, 12 * z)
    a = W2S(cam, x0 - 10, sy + 70); b = W2S(cam, x1 + 10, sy + 120); p.rect(a[0], a[1], b[0], b[1], SOF_D, INK, 3 * z, 6 * z)
def sofa_front(p, cam):
    z = cam[2]; x0, x1, sy = SOFA
    for xx in (x0 - 60, x1 - 10):
        a = W2S(cam, xx, sy - 120); b = W2S(cam, xx + 70, sy + 120); p.rect(a[0], a[1], b[0], b[1], SOF, INK, 3 * z, 22 * z)
    for xx in (x0 + 10, x1 - 30):
        a = W2S(cam, xx, sy + 120); b = W2S(cam, xx + 20, sy + 160); p.rect(a[0], a[1], b[0], b[1], (60, 36, 20, 255), INK, 2 * z, 3 * z)

def heart(d, x, y, r, col):
    d.ellipse([x - 2 * r, y - r, x, y + r * 0.6], fill=col); d.ellipse([x, y - r, x + 2 * r, y + r * 0.6], fill=col)
    d.polygon([(x - 2 * r + 1, y), (x + 2 * r - 1, y), (x, y + 2 * r)], fill=col)
def hearts(fr, cam, tt):
    """hearts float up around Aziza while he defends her — more and bigger as she melts; they POP at the reveal"""
    if tt >= SHOCK + 0.7 or tt < b1 + 1.0: return
    z = cam[2]; d = ImageDraw.Draw(fr, "RGBA")
    n = 4 if tt < T("B2") else (7 if tt < a2 else 10)
    for i in range(n):
        ph = (tt * 0.45 + i / n) % 1.0
        x, y = W2S(cam, AZ[0] - 150 + (i % 4) * 100 + math.sin(tt * 2 + i) * 20, 470 - ph * 220)
        a = int(220 * math.sin(ph * math.pi)); r = (11 + (i % 3) * 5) * z
        if tt >= SHOCK: r *= 1 + 3 * kk(tt, SHOCK, SHOCK + 0.7); a = int(a * (1 - kk(tt, SHOCK + 0.2, SHOCK + 0.7)))
        heart(d, x, y, r, (235, 60, 90, a))

def phone_ring(fr, cam, tt):
    """tiny sound-wave arcs from the phone while the call is on (the mother-in-law is talking)"""
    if tt >= HANG: return
    k, lt = line_at(tt)
    if k == "B1" or k == "B2" or k == "B4": return
    d = ImageDraw.Draw(fr, "RGBA"); z = cam[2]; S = BD[2] * CH["bondo2"]["scale"]
    cx, cy = W2S(cam, BD[0] + 80 * S, BD[1] - 230 * S)
    for i in range(3):
        u = (tt * 1.6 + i / 3) % 1.0; r = (12 + u * 40) * z
        d.arc([cx - r, cy - r, cx + r, cy + r], -40, 40, fill=(255, 255, 255, int(200 * (1 - u))), width=max(2, int(3 * z)))

def scene(tt, cam, size):
    Wd, Hd = size; x0, y0, z = cam
    box = (x0, y0, x0 + Wd / z, y0 + Hd / z)
    img = ROOM.resize((int(Wd * SS), int(Hd * SS)), Image.BICUBIC, box=box)
    if z > 1.9: img = img.filter(ImageFilter.GaussianBlur(min(2.5, (z - 1.8) * 1.4)))
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); p = P(lay)
    sofa_back(p, cam)
    k, lt = line_at(tt)
    # ---- Aziza (left, faces him): glows → whispers (leans in, hand at mouth) → melts → SHOCK → turns on him
    aex = "happy"
    if tt >= SHOCK: aex = "shock" if tt < SHOCK + 1.6 else "angry"
    aarms = arms_at([(0, "down"), (b1 + 3.0, "clap"), (T("AZ1") - 0.1, "shush"), (T("AZ1") + DUR["AZ1"], "clap"), (a2 + 4.3, "down"),
                     (SHOCK, "up"), (SHOCK + 1.6, "hips")], tt, 0.18)
    alean = 0.0
    if T("AZ1") - 0.2 <= tt < T("AZ1") + DUR["AZ1"] + 0.2: alean = 0.28                 # whispering into his free ear
    elif a2 <= tt < SHOCK: alean = 0.12
    if SHOCK <= tt < SHOCK + 0.5: alean = -0.2 * (1 - kk(tt, SHOCK, SHOCK + 0.5))       # recoils
    elif tt >= SHOCK + 1.6: alean = 0.2 * kk(tt, SHOCK + 1.6, SHOCK + 2.1)
    alook = 1 if not (SHOCK <= tt < SHOCK + 1.4) else 0
    person(lay, cam, "aziza", *AZ, tt, aex, alook, aarms, alean, None, sit=1)
    # ---- Bandaq (right, faces her): phone at the ear until he hangs up
    on_phone = tt < HANG
    bex = "angry" if tt < T("AZ1") else ("flat" if tt < T("B2") else "smug")
    if tt >= HANG: bex = "happy"
    if tt >= SHOCK + 1.2: bex = "scared"
    if on_phone: barms = "phone"
    else: barms = arms_at([(HANG, "phone"), (HANG + 0.01, "down"), (T("B3") + 0.9, "talk"), (SHOCK + 1.2, "scared")], tt)
    if k == "B1" and 4.55 <= lt < 6.9 and on_phone: barms = "phone"
    blean = 0.0
    if k == "AZ1": blean = 0.12                                                           # tilts to listen to her
    if k == "B2" and lt >= 2.6: blean = -0.1 * ease(kk(lt, 2.6, 3.2))                    # chest out
    if tt >= SHOCK + 1.4: blean = 0.25
    nod = math.sin((tt - T("AZ1")) * 9) * 4 if k == "AZ1" and lt > 1.0 else 0.0         # nods «حاضر حاضر»
    person(lay, cam, "bondo2", *BD, tt, bex, -1 if (k != "B1" or lt > 3.0) else 0, barms, blean, "phone" if on_phone else None, sit=-1, nod=nod)
    sofa_front(p, cam)
    lay = tint_layer(lay, (255, 238, 212)); img.paste(lay, (0, 0), lay)
    fr = img.resize((Wd, Hd), Image.LANCZOS)
    hearts(fr, cam, tt); phone_ring(fr, cam, tt)
    d = ImageDraw.Draw(fr, "RGBA")
    if HANG <= tt < HANG + 0.5:                                                           # «click» pop
        S = BD[2] * CH["bondo2"]["scale"]; q = W2S(cam, BD[0] + 70 * S, BD[1] - 150 * S); r = (10 + 30 * kk(tt, HANG, HANG + 0.4)) * z
        d.ellipse([q[0] - r, q[1] - r, q[0] + r, q[1] + r], outline=(255, 255, 255, int(220 * (1 - kk(tt, HANG, HANG + 0.5)))), width=3)
    if SHOCK <= tt < SHOCK + 0.9:                                                         # shock lines around her head
        S = AZ[2] * CH["aziza"]["scale"]; c = W2S(cam, AZ[0], AZ[1] - 210 * S); u = kk(tt, SHOCK, SHOCK + 0.25)
        for i in range(10):
            a_ = i / 10 * 2 * math.pi; r0, r1 = 95 * S * z, (95 + 45 * u) * S * z
            d.line([(c[0] + math.cos(a_) * r0, c[1] + math.sin(a_) * r0), (c[0] + math.cos(a_) * r1, c[1] + math.sin(a_) * r1)],
                   fill=(255, 255, 255, int(230 * (1 - kk(tt, SHOCK + 0.5, SHOCK + 0.9)))), width=max(3, int(4 * z)))
    if tt >= SHOCK + 0.1 and tt < SHOCK + 1.4:
        S = AZ[2] * CH["aziza"]["scale"]; c = W2S(cam, AZ[0] + 60 * S, AZ[1] - 330 * S)
        lzt(fr, c[0], c[1], "!!", int(90 * z / 2 * popk(tt, SHOCK + 0.1, 0.2)), (255, 80, 60))
    if tt >= SHOCK + 1.3:                                                                 # sweat on him
        S = BD[2] * CH["bondo2"]["scale"]
        for i in range(2):
            u = (tt * 0.9 + i * 0.5) % 1.0; q = W2S(cam, BD[0] + (-40 + 80 * i) * S, BD[1] - 250 * S + u * 50 * S); r = 5 * S * z
            d.ellipse([q[0] - r, q[1] - r * 1.5, q[0] + r, q[1] + r * 1.5], fill=(190, 225, 255, int(230 * (1 - u))), outline=(60, 110, 170, int(255 * (1 - u))), width=2)
    return fr

def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255, rot=0, stroke=True):
    if size < 4: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(LZ, size)
    if stroke: d.text((x, y), s, font=f, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), anchor="mm", direction="rtl", language="ar")
    d.text((x, y), s, font=f, fill=fill + (alpha,), anchor="mm", direction="rtl", language="ar")
    if rot: lay = lay.rotate(rot, center=(x, y), resample=Image.BICUBIC)
    img.paste(lay, (0, 0), lay)
def popk(tt, t0, d=0.22):
    u = kk(tt, t0, t0 + d); return 0 if u <= 0 else (1 + 0.25 * math.sin(u * math.pi)) if u < 1 else 1

def sub_chunk(img, tt, cx, cy, size):
    k, lt = line_at(tt)
    if not k or k not in CHUNKS: return
    cur = None
    for off, txt, key in CHUNKS[k]:
        if lt >= off: cur = (off, txt, key)
    if cur is None: return
    off, txt, key = cur; sc = popk(lt, off, 0.15) if lt - off < 0.15 else 1
    f = ImageFont.truetype(LZ, max(6, int(size * sc)))
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    kw = dict(font=f, direction="rtl", language="ar", stroke_width=max(4, size // 10), stroke_fill=(10, 10, 10, 255))
    if key and key in txt:
        a, b = txt.split(key, 1); parts = [(a, (255, 255, 255)), (key, (255, 214, 60)), (b, (255, 255, 255))]
    else: parts = [(txt, (255, 255, 255))]
    widths = [d.textlength(s, font=f, direction="rtl", language="ar") if s else 0 for s, _ in parts]
    tot = sum(widths); x = cx + tot / 2
    for (s, col), w in zip(parts, widths):
        if s: d.text((x - w, cy), s, fill=col + (255,), anchor="lm", **kw)
        x -= w
    nm, ncol = NAME[WHO[k]]; fn = ImageFont.truetype(LZ, int(size * 0.62))
    nw = d.textlength(nm, font=fn, direction="rtl", language="ar"); nx = cx + tot / 2 - nw / 2 - 10; ny = cy - size * 0.95
    d.rounded_rectangle([nx - nw / 2 - 18, ny - size * 0.38, nx + nw / 2 + 18, ny + size * 0.38], int(size * 0.3), fill=ncol + (235,))
    d.text((nx, ny), nm, font=fn, fill=(20, 12, 8, 255), anchor="mm", direction="rtl", language="ar")
    img.paste(lay, (0, 0), lay)

def endcard(fr, tt, sh, Wd, Hd):
    k = kk(tt, sh["start"], sh["start"] + 0.4)
    fr = ImageEnhance.Brightness(fr).enhance(1 - 0.55 * k).filter(ImageFilter.GaussianBlur(6 * k))
    sc = popk(tt, sh["start"] + 0.1, 0.3); vert = Hd > Wd
    if sc > 0:
        lzt(fr, Wd / 2, Hd * (0.34 if vert else 0.3), "ابعتها لجوزك", int((120 if vert else 110) * sc), (255, 214, 90))
        lzt(fr, Wd / 2, Hd * (0.34 if vert else 0.3) + (130 if vert else 115), "وقوله: قول لها يا حبيبي!", int((80 if vert else 80) * sc), (255, 255, 255))
    if tt >= sh["start"] + 0.5:
        logo(fr, Wd / 2, Hd * (0.56 if vert else 0.66), 130); text(fr, Wd / 2, Hd * (0.56 if vert else 0.66) + 140, "تابعنا @shattawzalata", 52, (255, 214, 90))
    return fr

_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/daily/17")

def subtitle(img, tt): sub_chunk(img, tt, W / 2, H - 85, 64)

HOOK = "بيدافع عن مراته… قدام مين؟!"
_FREEZE = {}
def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "end":
        if "h" not in _FREEZE: _FREEZE["h"] = scene(sh["start"] - 0.05, cam_at(shots[-2], sh["start"] - 0.05), (W, H))
        return finish(endcard(_FREEZE["h"].copy(), tt, sh, W, H), tt)
    fr = scene(tt, cam_at(sh, tt), (W, H))
    if tt < 3.0:
        a_ = int(255 * min(1, (3.0 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([W / 2 - 600, 40, W / 2 + 600, 150], 30, fill=(20, 12, 8, int(a_ * 0.8)))
        lzt(fr, W / 2, 95, HOOK, 72, (255, 214, 90), alpha=a_)
    return finish(fr, tt)

VIGV = VIG.resize((1080, 1920))
def vertical(_base, tt):
    sh = shot_at(tt)
    if sh["set"] == "end":
        if "v" not in _FREEZE: _FREEZE["v"] = scene(sh["start"] - 0.05, vcam(shots[-2], sh["start"] - 0.05), (1080, 1920))
        return endcard(_FREEZE["v"].copy(), tt, sh, 1080, 1920)
    fr = scene(tt, vcam(sh, tt), (1080, 1920))
    fr = ImageChops.multiply(fr, VIGV)
    u = tt - sh["start"]
    if sh.get("tin") in ("whip", "whipl") and u < 0.18: fr = fr.filter(ImageFilter.BoxBlur(int(2 + 18 * (1 - u / 0.18))))
    if tt < 3.0:
        a_ = int(255 * min(1, (3.0 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([90, 230, 990, 470], 40, fill=(20, 12, 8, int(a_ * 0.75)))
        lzt(fr, 540, 300, "بيدافع عن مراته…", 88, (255, 255, 255), alpha=a_); lzt(fr, 540, 405, "قدام مين؟!", 96, (255, 214, 90), alpha=a_)
    sub_chunk(fr, tt, 500, 1420, 76)
    return fr

def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(17)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 300) * 0.015, 0, 1.0)
    # mother-in-law «wah-wah» squeaks on the phone in the gaps
    for st in (T("AZ1") - 0.05, T("B2") - 0.08, T("B4") - 0.08):
        for j in range(4):
            seg = tone(520 + 140 * ((j * 7) % 3), 0.09, 0.05, 15); mix_into(buf, lowpass(seg, 1800), st - 0.4 + j * 0.1, 1.0)
    mix_into(buf, tone(220, 0.6, 0.16, 3) + tone(330, 0.6, 0.1, 3), T("B2") + 2.6, 1.0)                     # proud «dun»
    mix_into(buf, tone(1500, 0.04, 0.2, 80), HANG, 1.0)                                                        # phone click
    for i in range(3): mix_into(buf, tone(880 + i * 220, 0.25, 0.06, 6), T("AZ2") + 0.1 + i * 0.12, 1.0)      # sweet chime
    mix_into(buf, tone(140, 0.8, 0.3, 2.5), SHOCK, 1.0); mix_into(buf, tone(95, 0.8, 0.25, 2.5), SHOCK + 0.03, 1.0)   # «DUN»
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 0.5: mix_into(buf, SFXF["whoosh"] * 0.18, s_["start"] - 0.1, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), TOTAL - 2.3 + k_ * 0.09, 1.0)
    rms = lambda x: float(np.sqrt(np.mean(x ** 2))) + 1e-9; ref = []
    for st, k in lines:
        if k == "GROUP": continue
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8
        if k == "AZ1": v *= 0.85
        ref.append(rms(v)); mix_into(buf, v, st, 1.0)
    g = AUD["GROUP"][:int(SR * LU)].copy(); g[-int(SR * 0.4):] *= np.linspace(1, 0, int(SR * 0.4))
    mix_into(buf, g / rms(g) * float(np.mean(ref)) * 1.2, LAUGH, 1.0)
    write_wav(buf[:int(TOTAL * SR)], path)

def make_covers():
    """growth rules: BIG shocked Aziza face, Bandaq + phone (story object), 2-3 word question, series badge"""
    def comp(Wd, Hd, vert):
        bgc = ROOM.crop((400, 100, 1500, 1000)).resize((Wd, Hd), Image.LANCZOS).filter(ImageFilter.GaussianBlur(6))
        img = ImageEnhance.Brightness(bgc).enhance(0.8).resize((int(Wd * SS), int(Hd * SS)))
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); p = P(lay)
        if vert:
            draw_char(p, "bondo2", Wd * 0.8, Hd * 0.5, 2.3, "happy", 0.35, -1, False, "phone", 0.0, "phone", 0.0, None)
            draw_char(p, "aziza", Wd * 0.42, Hd * 0.93, 5.3, "shock", 0.7, 0, False, "up", 0.0, None, 0.0, None)
        else:
            draw_char(p, "aziza", Wd * 0.3, Hd * 1.35, 4.8, "shock", 0.7, 0, False, "up", 0.0, None, 0.0, None)
            draw_char(p, "bondo2", Wd * 0.8, Hd * 1.05, 3.3, "happy", 0.35, -1, False, "phone", 0.0, "phone", 0.0, None)
        img.paste(lay, (0, 0), lay); fr = img.resize((Wd, Hd), Image.LANCZOS); d = ImageDraw.Draw(fr, "RGBA")
        if vert:
            d.rectangle([0, Hd * 0.69, Wd, Hd * 0.88], fill=(10, 6, 4, 150))
            lzt(fr, Wd / 2, Hd * 0.74, "بيكلم", 170, (255, 255, 255)); lzt(fr, Wd / 2, Hd * 0.83, "مين؟!", 190, (255, 214, 60))
            bx, by = Wd / 2, 130
        else:
            d.rectangle([0, Hd * 0.76, Wd, Hd * 0.97], fill=(10, 6, 4, 150)); lzt(fr, Wd * 0.56, Hd * 0.865, "بيكلم مين؟!", 170, (255, 214, 60)); bx, by = 1600, 90
        d.rounded_rectangle([bx - 175, by - 40, bx + 175, by + 40], 30, fill=(200, 30, 40, 240))
        lzt(fr, bx, by, "يوميات شطة وزلطة", 40, (255, 255, 255), stroke=False)
        return fr
    comp(1080, 1920, True).save(ROOT + "/publish/thumbs/daily_e17_cover.jpg", quality=92)
    comp(1920, 1080, False).resize((1280, 720), Image.LANCZOS).save(ROOT + "/publish/thumbs/daily_e17_yt.jpg", quality=92)

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
    elif sys.argv[1:2] == ["cover"]: make_covers()
