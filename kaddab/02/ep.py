# «مين الكداب؟» — القضية 2: الساعة تلاتة الفجر  (H 1920x1080 + V 1080x1920 in one pass)
# render:  python ep.py audio  →  python ep.py part 0 2 & python ep.py part 1 2  →  concat  →  mux mix.wav
# Format v2 (user 2026-11-15): every case STANDALONE; the PREVIOUS case's answer comes at the END (A1), then «شوفوا الحلقة اللي فاتت» + case-1 cover + like/follow/share (C1).
# Answer of THIS case (tell it at the end of case 3): شطة — his hair is wet and dripping: he was the one in the bathroom. Zalata's toothpaste = red herring.
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/kaddab/02")
SERIES = "مين الكداب؟"; EPT = "الساعة تلاتة الفجر"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"; DJ = ROOT + "/brand/fonts/DejaVuSans-Bold.ttf"
SFXP = {"whoosh": "/trend/01/sfx/whoosh.mp3", "sting": "/trend/01/sfx/stinger.mp3", "creak": "/s1e9/sfx/creak.mp3",
        "snore": "/s2e2/sfx/snore.mp3", "steps": "/s1e10/sfx/footsteps.mp3"}
SFXF = {n: load_audio(ROOT + p) for n, p in SFXP.items()}

SUB = {"T1": "الساعة تلاتة الفجر... وفيه حد في الحمّام!", "T2": "صحّيت الكل... وكل واحد قال إنه كان نايم!",
       "S1": "أنا نايم من الساعة عشرة... ولسه صاحي حالاً على صوتك!",
       "Z1": "أنا كنت نايم... والمعجون ده بنام بيه عشان ما أنساش أغسل سناني الصبح!",
       "AZ1": "أنا نومي تقيل... لو العمارة وقعت مش هحس!",
       "T3": "مين فيهم الكداب؟ واحد... ولا اتنين... ولا تلاتة؟ بصّوا كويس... واكتبوا في الكومنتات!",
       "A1": "وحل الفزورة اللي فاتت: الكداب كان زلطة! عشان النور كان قاطع... إزاي كان بيذاكر على الأباجورة؟!",
       "C1": "ولو ما شفتوش الحلقة اللي فاتت... شوفوها! وما تنسوش اللايك والفولو والشير!", "LAUGH": ""}
WHO = {"T1": "tota", "T2": "tota", "S1": "shatta", "Z1": "zalata", "AZ1": "aziza", "T3": "tota", "A1": "nana", "C1": "nana", "LAUGH": "-"}
EXPR = {"T1": "scared", "T2": "scared", "S1": "sleepy", "Z1": "flat", "AZ1": "sleepy", "T3": "smug", "A1": "angry", "C1": "happy", "LAUGH": "laugh"}
load_lines(list(SUB))
LIVING = _ld(ROOT + "/s1e1/bg/living_1080.png")      # canonical «الصالة» (Nana's flat) — already the night version (candle)
COVER1 = Image.open(ROOT + "/publish/thumbs/kaddab_e01_cover.jpg").convert("RGB")

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
t = say(0.25, "T1")                                                                          # first word at 0.25 s (hook rule)
DOOR_END = 0.25 + 1.55
shot("door", 0.0, DOOR_END, None)                                                           # HOOK: bathroom door, light under it, a shadow passes
shot("living", DOOR_END, t + 0.1, (1400, 820, 2.3), (1400, 815, 2.5), tin="whip")          # Tota CU with her torch
t += 0.1
ENTER = t; t = say(t + 0.05, "T2") + 0.15
shot("living", ENTER, t, (1000, 760, 1.32), (1000, 760, 1.38), tin="fade")                 # wide: the 3 walk in, half asleep
LINEUP = t; shot("living", t, t + 1.0, (1000, 760, 1.38), (1000, 760, 1.42)); t += 1.0     # numbers pop
s = t; t = say(t + 0.05, "S1") + 0.15; shot("living", s, t, (600, 760, 2.1), (600, 752, 2.25), tin="whipl")
s = t; t = say(t + 0.05, "Z1"); shot("living", s, t - 1.2, (830, 760, 2.1), (830, 755, 2.2), tin="whip")
PASTE = t - 1.2; shot("paste", PASTE, t + 0.1, None, ease="crash"); t += 0.1                 # insert: the toothpaste
LAUGH1 = t; shot("living", t, t + 1.1, (1000, 760, 1.38), (1000, 760, 1.42)); say(t + 0.05, "LAUGH"); t += 1.1   # reactions + audience laugh (sound only)
s = t; t = say(t + 0.05, "AZ1") + 0.1; shot("living", s, t, (1080, 760, 2.1), (1080, 752, 2.25), tin="whip")
SNORE = t; shot("living", t, t + 1.4, (1080, 752, 2.25), (1080, 780, 2.0)); t += 1.4           # she falls asleep standing up
ASK = t; t = say(t + 0.05, "T3") + 0.3
shot("living", ASK, ASK + 3.0, (1400, 830, 2.5), (1400, 830, 2.75), tin="whip")             # torch under the chin, to camera
shot("living", ASK + 3.0, t, (1000, 760, 1.38), (1000, 760, 1.46))                          # back to the lineup, numbers pulse
Q = t; shot("q", t, t + 1.3, None); t += 1.3                                                  # «اكتب رقم الكداب»
ANS = t; t = say(t + 0.25, "A1") + 0.35; shot("ans", ANS, t, None, tin="flash")             # previous case answer (case 1: Zalata)
CTA = t; t = say(t + 0.15, "C1") + 0.8; shot("cta", CTA, t, None, tin="whip")               # watch case 1 + like/follow/share
TOTAL = t

# ---------------- staging (world = living room 1920x1080) ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
POS = {"shatta": (560, 1040, 1.7), "zalata": (820, 1040, 1.7), "aziza": (1080, 1045, 1.75), "tota": (1400, 1050, 2.05)}
CLOCK = (938, 292)

def arms_at(sched, tt, d=0.22):
    prev = sched[0][1]
    for i, (t0, pose) in enumerate(sched):
        if tt < t0: break
        if tt < t0 + d and i > 0: return (sched[i - 1][1], pose, (tt - t0) / d)
        prev = pose
    return prev

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, walk=None, held=None, nod=0.0):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11 and expr not in ("sleepy", "laugh")
    if not talking and walk is None: lean += math.sin(tt * 1.7 + len(who)) * 0.06
    X, Y_ = W2S(cam, x, y); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, held, lean, walk, nod=nod)
    return X, Y_, S * CH[who]["scale"]

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
    d.ellipse([x - r, y - r, x + r, y + r], fill=col + (255,), outline=(255, 255, 255, 255), width=int(6 * sc))
    lzt(fr, x, y + 4 * sc, n, int(70 * sc), (255, 255, 255), font=DJ)

_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/kaddab/02")

# ---------------- props / inserts ----------------
def clock_hands(p, cam):                                       # the wall clock reads 3:00
    z = cam[2]; cx, cy = W2S(cam, *CLOCK)
    p.line([(cx, cy), (cx, cy - 16 * z)], (235, 225, 200, 255), 2.6 * z)
    p.line([(cx, cy), (cx + 11 * z, cy)], (235, 225, 200, 255), 3.4 * z)

def drips(p, cam, tt):
    """Shatta's wet hair: drops fall from his head + a small puddle at his feet (THE clue — subtle, never pointed at)"""
    z = cam[2]; x, y, s = POS["shatta"]
    for i, (dx, ph) in enumerate(((-46, 0.0), (40, 0.37), (-20, 0.71), (52, 0.18))):
        u = (tt * 1.1 + ph) % 1.0
        hx, hy = W2S(cam, x + dx * s / 1.7, y - 300 * s / 1.7 + u * 230 * s / 1.7)
        p.ell(hx, hy, 4.2 * z, 6.5 * z, (150, 205, 255, 230), (40, 90, 160, 255), 1.2 * z)
    px, py = W2S(cam, x + 10, y + 2)
    p.ell(px, py, 62 * z, 9 * z, (120, 170, 230, 120), None)

def door_insert(tt):
    """HOOK: the bathroom door in the dark — warm light under it, water running, a shadow crosses the gap"""
    u = tt / DOOR_END; zz = 1.0 + 0.10 * ease(u)
    fr = Image.new("RGB", (W, H), (14, 14, 22)); d = ImageDraw.Draw(fr, "RGBA")
    def R(x0, y0, x1, y1): cx, cy = W / 2, H * 0.62; return [cx + (x0 - cx) * zz, cy + (y0 - cy) * zz, cx + (x1 - cx) * zz, cy + (y1 - cy) * zz]
    d.rectangle(R(0, 0, W, 860), fill=(30, 28, 40))                                    # wall
    d.rectangle(R(0, 860, W, H), fill=(22, 20, 26))                                   # floor tiles
    for i in range(0, W + 1, 160): d.line(R(i, 860, i - 80, H)[:2] + R(i, 860, i - 220, H)[2:], fill=(34, 30, 38), width=2)
    d.rectangle(R(640, 60, 1280, 860), fill=(70, 46, 30), outline=(10, 8, 6), width=8)   # the door
    for (a, b, c, e) in ((700, 120, 1220, 440), (700, 490, 1220, 810)): d.rectangle(R(a, b, c, e), outline=(48, 30, 20), width=8)
    d.ellipse(R(1180, 470, 1214, 504), fill=(200, 170, 80), outline=(10, 8, 6), width=3)  # knob
    d.rectangle(R(650, 846, 1270, 862), fill=(255, 225, 140))                            # light under the door
    for k_ in range(8):                                                                 # glow spilling on the floor
        d.polygon([tuple(R(650 - k_ * 30, 862, 0, 0)[:2]), tuple(R(1270 + k_ * 30, 862, 0, 0)[:2]),
                   tuple(R(1340 + k_ * 50, 900 + k_ * 22, 0, 0)[:2]), tuple(R(580 - k_ * 50, 900 + k_ * 22, 0, 0)[:2])], fill=(255, 210, 120, 16))
    sx = 640 + 700 * kk(tt, 0.45, 1.35)                                                  # two feet pass behind the gap
    if 0.45 < tt < 1.35:
        for fx in (sx, sx + 90): d.rectangle(R(fx, 846, fx + 55, 862), fill=(20, 14, 10))
    d.rectangle(R(900, 20, 1020, 50), fill=(220, 220, 230), outline=(10, 8, 6), width=3)  # «حمّام» plate
    lzt(fr, W / 2, R(0, 35, 0, 0)[1], "حمّام", int(30 * zz), (30, 30, 40), (220, 220, 230))
    for i in range(14):                                                                 # steam curling from under the door
        v = (tt * 0.6 + i / 14) % 1
        x_ = 700 + (i * 41) % 520 + math.sin(v * 6 + i) * 20
        q = R(x_, 846 - v * 300, 0, 0)
        d.ellipse([q[0] - 26, q[1] - 16, q[0] + 26, q[1] + 16], fill=(230, 230, 240, int(40 * (1 - v))))
    return fr

def paste_insert(tt, sh):
    """insert: Zalata's toothpaste tube, big (red herring)"""
    u = kk(tt, sh["start"], sh["end"]); zz = 1.0 + 0.12 * ease(u, "crash")
    cam = (820 - 960 / 4.2, 500 - 540 / 4.2, 4.2)
    img = bg_crop(LIVING, (max(0, cam[0]), max(0, cam[1]), 4.2)).filter(ImageFilter.GaussianBlur(6))
    fr = img.resize((W, H), Image.LANCZOS); fr = ImageEnhance.Brightness(fr).enhance(0.7)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay); s = 7.5 * zz; cx, cy = W / 2, H / 2 + 40
    p.poly([(cx - 30 * s / 3, cy - 120 * s / 3), (cx + 30 * s / 3, cy - 120 * s / 3), (cx + 24 * s / 3, cy + 30 * s / 3), (cx - 24 * s / 3, cy + 30 * s / 3)], (248, 248, 252, 255), INK, 6)
    p.rect(cx - 28 * s / 3, cy - 80 * s / 3, cx + 28 * s / 3, cy - 44 * s / 3, (40, 110, 220, 255), None)
    p.line([(cx - 28 * s / 3, cy - 20 * s / 3), (cx + 28 * s / 3, cy - 20 * s / 3)], (220, 40, 40, 255), 12)
    p.rect(cx - 16 * s / 3, cy + 30 * s / 3, cx + 16 * s / 3, cy + 58 * s / 3, (240, 240, 245, 255), INK, 5)
    fr.paste(lay.resize((W, H), Image.LANCZOS), (0, 0), lay.resize((W, H), Image.LANCZOS))
    lzt(fr, W * 0.74, H * 0.28, "معجون؟!", int(120 * popk(tt, sh["start"] + 0.15)), (255, 214, 90))
    return fr

def q_card(tt, sh):
    fr = ImageEnhance.Brightness(frame_cache(sh["start"] - 0.05)).enhance(0.45).filter(ImageFilter.GaussianBlur(5)).convert("RGBA")
    sc = popk(tt, sh["start"] + 0.05, 0.3)
    lzt(fr, W / 2, 300, "اكتب رقم الكداب في الكومنتات!", int(92 * sc), (255, 214, 90))
    for i, (n, col) in enumerate((("1", (230, 90, 40)), ("2", (60, 150, 80)), ("3", (196, 40, 96)))):
        badge(fr, W / 2 + (i - 1) * 200, 470, n, 1.3 * popk(tt, sh["start"] + 0.3 + i * 0.15), col)
    lzt(fr, W / 2, 640, "بُصّ كويس على الصورة... 👀".replace(" 👀", ""), int(60 * popk(tt, sh["start"] + 0.8)), (255, 255, 255))
    return fr.convert("RGB")

def ans_card(tt, sh):
    """answer of case 1: Zalata lied — the power was out, so his desk lamp could not be on"""
    st = T("A1"); fr = Image.new("RGB", (W, H), (16, 20, 44)); d = ImageDraw.Draw(fr, "RGBA")
    for i in range(18):                                                                 # rays
        a0 = i * 20 + tt * 6; a = math.radians(a0); b = math.radians(a0 + 9)
        d.polygon([(W / 2, H * 0.6), (W / 2 + 2400 * math.cos(a), H * 0.6 + 2400 * math.sin(a)), (W / 2 + 2400 * math.cos(b), H * 0.6 + 2400 * math.sin(b))], fill=(30, 38, 80, 255))
    lzt(fr, W / 2, 110, "حل الفزورة اللي فاتت", int(86 * popk(tt, sh["start"] + 0.15)), (255, 214, 90))
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    caught = tt >= st + 1.5
    draw_char(p, "zalata", 640, 1080 + 130, 3.3, "scared" if caught else "smug", 0.0, 1, ((tt + 0.3) % 3.4) < 0.1, "scared" if caught else "hold", tt,
              None if caught else "notebook", 0.0, None)
    fr.paste(lay.resize((W, H), Image.LANCZOS), (0, 0), lay.resize((W, H), Image.LANCZOS))
    if caught:
        k = popk(tt, st + 1.5, 0.25)
        d = ImageDraw.Draw(fr, "RGBA")
        lzt(fr, 640, 250, "الكداب!", int(150 * k), (255, 255, 255), (170, 20, 20), rot=8)
    if tt >= st + 3.0:                                                                  # the lamp + «the power was out»
        k = popk(tt, st + 3.0, 0.3); cx, cy = 1360, 520; s = 1.6 * k
        d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([cx - 260 * k, cy - 230 * k, cx + 260 * k, cy + 230 * k], 40, fill=(8, 8, 16, 230), outline=(255, 214, 90, 255), width=6)
        d.polygon([(cx - 60 * s, cy - 90 * s), (cx + 60 * s, cy - 90 * s), (cx + 90 * s, cy - 10 * s), (cx - 90 * s, cy - 10 * s)], fill=(120, 120, 130), outline=(20, 20, 20))
        d.line([(cx, cy - 10 * s), (cx, cy + 80 * s)], fill=(60, 60, 60), width=int(8 * s))
        d.rectangle([cx - 60 * s, cy + 80 * s, cx + 60 * s, cy + 96 * s], fill=(60, 60, 60))
        d.line([(cx - 130 * s, cy - 120 * s), (cx + 130 * s, cy + 110 * s)], fill=(230, 40, 40), width=int(16 * s))
        d.line([(cx + 130 * s, cy - 120 * s), (cx - 130 * s, cy + 110 * s)], fill=(230, 40, 40), width=int(16 * s))
        lzt(fr, cx, cy + 300, "النور كان قاطع!", int(78 * k), (255, 214, 90))
    return fr

def cta_card(tt, sh):
    fr = Image.new("RGB", (W, H), (20, 12, 10)); d = ImageDraw.Draw(fr, "RGBA")
    for i in range(18):
        a0 = i * 20 - tt * 6; a = math.radians(a0); b = math.radians(a0 + 9)
        d.polygon([(W / 2, H / 2), (W / 2 + 2400 * math.cos(a), H / 2 + 2400 * math.sin(a)), (W / 2 + 2400 * math.cos(b), H / 2 + 2400 * math.sin(b))], fill=(44, 24, 16, 255))
    k = popk(tt, sh["start"] + 0.15, 0.3)
    if k > 0:                                                                           # case-1 cover, slightly tilted, like a card
        ch = int(690 * k); cw = int(ch * 1080 / 1920)
        cov = COVER1.resize((cw, ch), Image.LANCZOS)
        fr_c = Image.new("RGBA", (cw + 24, ch + 24), (255, 214, 90, 255)); fr_c.paste(cov, (12, 12))
        fr_c = fr_c.rotate(-4, expand=True, resample=Image.BICUBIC)
        fr.paste(fr_c, (int(560 - fr_c.size[0] / 2), int(480 - fr_c.size[1] / 2)), fr_c)
        lzt(fr, 560, 72, "شوفوا القضية 1", int(70 * k), (255, 214, 90))
    st = T("C1")
    for i, (lab, col, t0) in enumerate((("لايك", (230, 50, 70), 2.4), ("فولو", (40, 140, 230), 2.9), ("شير", (60, 170, 90), 3.4))):
        k2 = popk(tt, st + t0, 0.25)
        if k2 <= 0: continue
        cx, cy = 1380, 220 + i * 190
        d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([cx - 260 * k2, cy - 80 * k2, cx + 260 * k2, cy + 80 * k2], int(60 * k2), fill=col + (255,), outline=(255, 255, 255, 255), width=6)
        ix = cx + 170 * k2
        if i == 0:                                                                       # heart
            r = 26 * k2; d.ellipse([ix - 2 * r, cy - r, ix, cy + r * 0.6], fill=(255, 255, 255)); d.ellipse([ix, cy - r, ix + 2 * r, cy + r * 0.6], fill=(255, 255, 255))
            d.polygon([(ix - 2 * r + 2, cy), (ix + 2 * r - 2, cy), (ix, cy + 2 * r)], fill=(255, 255, 255))
        elif i == 1:                                                                     # plus
            d.rectangle([ix - 34 * k2, cy - 9 * k2, ix + 34 * k2, cy + 9 * k2], fill=(255, 255, 255)); d.rectangle([ix - 9 * k2, cy - 34 * k2, ix + 9 * k2, cy + 34 * k2], fill=(255, 255, 255))
        else:                                                                            # arrow
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
    if sh["set"] == "door": return finish(door_insert(tt), tt)
    if sh["set"] == "paste": return finish(paste_insert(tt, sh), tt)
    if sh["set"] == "q": return finish(q_card(tt, sh), tt)
    if sh["set"] == "ans": return finish(ans_card(tt, sh), tt)
    if sh["set"] == "cta": return finish(cta_card(tt, sh), tt)
    cam = cam_at(sh, tt); z = cam[2]
    img = bg_crop(LIVING, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    clock_hands(p, cam)
    # --- entrances (T2): the three walk in from the left, half asleep, one after another
    ent = {}
    for i, who in enumerate(("shatta", "zalata", "aziza")):
        x, y, s = POS[who]; w0 = ENTER + 0.25 + i * 0.75
        k = kk(tt, w0, w0 + 1.3); e = ease(k)
        ent[who] = (lerp(-200, x, e), y, s, (tt * 7 if 0 < k < 1 else None), k)
    sx_, _, _, swalk, sk = ent["shatta"]; zx_, _, _, zwalk, zk = ent["zalata"]; ax_, _, _, awalk, ak = ent["aziza"]
    in_ = lambda kk_: tt < ENTER or kk_ > 0
    # --- expressions / arms
    sex = "sleepy"; zex = "sleepy"; aex = "sleepy"; tex = "scared"
    if tt >= LINEUP: sex = "neutral"; zex = "flat"; aex = "sleepy"; tex = "smug"
    if LAUGH1 <= tt < T("AZ1"): sex = "laugh"; aex = "laugh"; tex = "flat"
    if SNORE <= tt < ASK: tex = "shock"; sex = "laugh"
    if tt >= ASK: sex = "scared"; zex = "flat"; aex = "neutral"; tex = "smug"
    sarms = arms_at([(0, "down"), (T("S1"), "talk"), (T("S1") + DUR["S1"], "down"), (ASK, "scared")], tt)
    zarms = arms_at([(0, "down"), (LINEUP, "hold"), (ASK, "hold")], tt)
    aarms = arms_at([(0, "down"), (T("AZ1"), "hips"), (SNORE, "down"), (ASK, "hips")], tt)
    tarms = arms_at([(0, "scared"), (ENTER, "hold"), (T("T3") + 3.0, "point"), (T("T3") + DUR["T3"] - 1.2, "hold")], tt)
    anod = 22 * ease(kk(tt, SNORE + 0.2, SNORE + 0.7)) * (1 - ease(kk(tt, SNORE + 1.2, SNORE + 1.4)))
    if tt >= ENTER:
        if in_(sk) and sk > 0: person(lay, cam, "shatta", sx_, POS["shatta"][1], POS["shatta"][2], tt, sex, 1 if tt >= T("Z1") else 0, sarms, walk=swalk)
        if in_(zk) and zk > 0: person(lay, cam, "zalata", zx_, POS["zalata"][1], POS["zalata"][2], tt, zex, 0, zarms, walk=zwalk,
                                      held="toothpaste" if tt >= LINEUP else None)
        if in_(ak) and ak > 0: person(lay, cam, "aziza", ax_, POS["aziza"][1], POS["aziza"][2], tt, aex, -1 if tt >= T("AZ1") + DUR["AZ1"] else 0, aarms,
                                      walk=awalk, held="slipper" if tt >= ASK else None, nod=anod)
        if tt >= LINEUP: drips(p, cam, tt)
    person(lay, cam, "tota", *POS["tota"], tt, tex, -1, tarms, held="torch")
    lay = tint_layer(lay, (200, 205, 240)); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    # --- torch light: a cone from Tota towards the lineup + under-chin light during her question
    d = ImageDraw.Draw(fr, "RGBA")
    hx, hy = W2S(cam, POS["tota"][0] - 70, POS["tota"][1] - 330)
    if ASK <= tt < ASK + 3.0:
        g = Image.new("L", (W, H), 0); dg = ImageDraw.Draw(g); fx_, fy_ = W2S(cam, POS["tota"][0], POS["tota"][1] - 300)
        dg.ellipse([fx_ - 260 * z / 2.5, fy_ - 300 * z / 2.5, fx_ + 260 * z / 2.5, fy_ + 260 * z / 2.5], fill=70)
        g = g.filter(ImageFilter.GaussianBlur(60)); fr = Image.composite(Image.new("RGB", (W, H), (255, 236, 170)), fr, g); d = ImageDraw.Draw(fr, "RGBA")
    elif tt >= ENTER:
        pass
    # --- number badges
    if LINEUP <= tt:
        for i, (who, col) in enumerate((("shatta", (230, 90, 40)), ("zalata", (60, 150, 80)), ("aziza", (196, 40, 96)))):
            q = W2S(cam, POS[who][0], POS[who][1] - 360 * POS[who][2] / 1.7)
            pulse = 1 + (0.12 * math.sin(tt * 8) if tt >= ASK + 3.0 else 0)
            badge(fr, q[0], q[1], str(i + 1), min(1.1, z * 0.75) * popk(tt, LINEUP + 0.15 + i * 0.25) * pulse, col)
    if SNORE + 0.5 <= tt < ASK:                                                         # Aziza snoring standing up
        q = W2S(cam, POS["aziza"][0] + 120, 560)
        for j, ch in enumerate("Zzz"):
            lzt(fr, q[0] + j * 40 * z / 2, q[1] - j * 46 * z / 2 - (tt - SNORE) * 30, ch, int((70 - j * 14) * z / 2.2), (180, 200, 255), (20, 20, 50), font=DJ)
    if tt < 3.2:
        pass
    return finish(fr, tt)

HOOK1, HOOK2 = "مين اللي في الحمّام", "الساعة 3 الفجر؟!"
def hook_banner(fr, tt):
    if tt >= 3.0: return
    a = int(255 * min(1, (3.0 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
    d.rounded_rectangle([W / 2 - 640, 30, W / 2 + 640, 160], 30, fill=(20, 12, 8, int(a * 0.8)))
    lzt(fr, W / 2, 95, HOOK1 + " " + HOOK2, 72, (255, 214, 90), alpha=a)

_render = render
def render(out_h, out_v, stills=None, t0=0.0, t1=None):
    global frame
    base_frame = frame
    def frame(tt):
        fr = base_frame(tt); hook_banner(fr, tt); return fr
    globals()["frame"] = frame
    _render(out_h, out_v, stills, t0, t1)

def vertical(fr, tt):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = ImageEnhance.Brightness(small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.35)
    bgv.paste(fr.resize((1080, 608), Image.LANCZOS), (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(255, 214, 90)); d.rectangle([0, 1168, 1080, 1171], fill=(255, 214, 90))
    if tt < ANS:
        lzt(bgv, 540, 240, HOOK1, 104, (255, 255, 255)); lzt(bgv, 540, 390, HOOK2, 120, (255, 214, 90))
    else:
        lzt(bgv, 540, 240, "حل الفزورة", 110, (255, 255, 255)); lzt(bgv, 540, 390, "اللي فاتت", 120, (255, 214, 90))
    lzt(bgv, 540, 1840, "مين الكداب؟ • قضية جديدة", 46, (255, 150, 110))
    k, _ = line_at(tt)
    if k and SUB.get(k):
        for i, l in enumerate(wrap(SUB[k])[:4]): text(bgv, 540, 1290 + i * 80, l, 60, sw=6)
    return bgv

def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(46)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 300) * 0.02, 0, 1.0)
    water = lowpass(r.normal(0, 1, int(SR * (ENTER + 0.6))).astype(np.float32), 2500) * 0.16          # shower running (stops when Tota wakes them)
    fade = np.ones_like(water); fade[-int(SR * 0.6):] = np.linspace(1, 0, int(SR * 0.6)); fade[int(SR * DOOR_END):] *= 0.45
    mix_into(buf, water * fade, 0.0, 1.0)
    for k_ in range(int(ASK / 1.0)): mix_into(buf, tone(1500, 0.04, 0.05, 50), k_ * 1.0 + 0.3, 1.0)       # wall clock ticking
    mix_into(buf, SFXF["sting"] * 0.45, 0.0, 1.0)
    mix_into(buf, SFXF["creak"] * 0.5, ENTER, 1.0)
    mix_into(buf, SFXF["steps"] * 0.35, ENTER + 0.25, 1.0)
    for i in range(3): mix_into(buf, tone(660 + i * 220, 0.18, 0.2, 12), LINEUP + 0.15 + i * 0.25, 1.0)
    for j in range(int((ASK - LINEUP) / 0.9)): mix_into(buf, tone(2400, 0.08, 0.035, 45) + tone(1700, 0.08, 0.02, 40), LINEUP + 0.4 + j * 0.9, 1.0)   # soft drips
    mix_into(buf, tone(220, 0.4, 0.3, 6) + tone(330, 0.4, 0.2, 6), PASTE + 0.1, 1.0)
    mix_into(buf, SFXF["snore"] * 0.6, SNORE + 0.3, 1.0)
    mix_into(buf, SFXF["sting"] * 0.35, ASK + 3.0, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), Q + k_ * 0.09, 1.0)
    mix_into(buf, tone(180, 0.5, 0.3, 4) + tone(120, 0.5, 0.3, 4), T("A1") + 1.5, 1.0)               # «الكداب!» stamp
    for i, t0 in enumerate((2.4, 2.9, 3.4)): mix_into(buf, tone(880 + i * 220, 0.2, 0.2, 10), T("C1") + t0, 1.0)
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 0.5: mix_into(buf, SFXF["whoosh"] * 0.25, s_["start"] - 0.1, 1.0)
    rms = lambda x: float(np.sqrt(np.mean(x ** 2))) + 1e-9; ref = []
    for st, k in lines:
        if k == "LAUGH": continue
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8; ref.append(rms(v)); mix_into(buf, v, st, 1.0)
    g = AUD["LAUGH"]; mix_into(buf, g / rms(g) * float(np.mean(ref)) * 0.9, T("LAUGH"), 1.0)
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
