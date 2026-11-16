# «يوميات شطة وزلطة» — لازم جوزك يفسّحك  (H 1920x1080 + V 1080x1920 in one pass) — user script 2026-11-15, GO 2026-11-16
# Aziza comes home from the doctor (door), Bandaq on the sofa with his newspaper — same room + same code sofa as daily/11 («أوضة بندق وعزيزة»).
# Callback: thought bubble of the clinic + Dr. Zalata (daily/10 «الخبر الوحش», canonical clinic set), prescription insert.
# render:  python ep.py audio  →  python ep.py part 0 2 & python ep.py part 1 2  →  concat  →  mux mix.wav
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont, ImageOps
os.chdir(ROOT + "/daily/13")
SERIES = "يوميات شطة وزلطة"; EPT = "لازم جوزك يفسّحك"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"; DJ = ROOT + "/brand/fonts/DejaVuSans-Bold.ttf"
SFXF = {"whoosh": load_audio(ROOT + "/trend/01/sfx/whoosh.mp3"), "creak": load_audio(ROOT + "/s1e9/sfx/creak.mp3"),
        "steps": load_audio(ROOT + "/s1e10/sfx/footsteps.mp3")}

SUB = {"B1": "الدكتور قالّك إيه يا وليّة؟",
       "A1": "قالّي إني تعبانة قوي... مكتئبة... ولازم جوزك يفسّحك ويخرّجك... على الأقل أسبوع!",
       "A2": "ها... هتوديني فين بقى؟", "B2": "هوديكي عند دكتور تاني.", "GROUP": ""}
DRZ = "drzalata"; CH[DRZ] = dict(CH["zalata"]); CH[DRZ].update(shirt=(242, 244, 248), coat=True); BASE[DRZ] = "zalata"
WHO = {"B1": "bondo2", "A1": "aziza", "A2": "aziza", "B2": "bondo2", "GROUP": "-"}
EXPR = {"B1": "neutral", "A1": "sad", "A2": "happy", "B2": "flat", "GROUP": "laugh"}
load_lines(list(SUB))
ROOM = _ld(ROOT + "/daily/bg/bandaq_room.png")      # canonical «أوضة بندق وعزيزة»
CLINIC = _ld(ROOT + "/daily/bg/clinic.png")         # canonical «العيادة» (flashback bubble only)

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
TWO = (900, 690, 1.6)
t = say(0.15, "B1")                                                                   # first word at 0.15 s (hook rule) — he hears the door
shot("room", 0.0, t + 0.3, (880, 700, 1.5), TWO)                                    # two-shot: the door opens, she comes in with the prescription
t += 0.3
a = say(t + 0.15, "A1"); A1 = T("A1")
BUB = (A1 + 0.35, A1 + 3.75)                                                         # «تعبانة قوي... مكتئبة» → the clinic flashback bubble
shot("room", t, A1 + 3.75, (560, 690, 2.25), (540, 680, 2.5), tin="whipl")           # CU Aziza, hand on her forehead (slow push-in)
shot("room", A1 + 3.75, A1 + 4.75, TWO, (900, 690, 1.68), tin="whip")              # «ولازم جوزك…» she points at him
RX = A1 + 4.75; shot("rx", RX, A1 + 6.45, None, tin="zoom")                         # prescription insert «يفسّحك ويخرّجك»
shot("room", A1 + 6.45, a + 0.2, (1150, 680, 2.3), (1160, 672, 2.45), tin="whip")  # «على الأقل أسبوع!» on Bandaq's face (sweat)
t = a + 0.2
a2 = say(t, "A2"); shot("room", t, a2 + 0.35, (620, 690, 1.9), (700, 690, 2.0), tin="whipl")   # she clasps her hands, hearts
t = a2 + 0.35
b2 = say(t, "B2"); PUNCH = T("B2"); shot("room", t, b2 + 0.15, (1150, 680, 2.3), (1150, 676, 2.4), tin="whip")   # deadpan CU
t = b2 + 0.15
FREEZE0 = t; shot("room", t, t + 0.9, (560, 680, 2.5), (560, 670, 2.9), ease="crash")  # her frozen face + cricket
LAUGH = t + 0.75; say(LAUGH, "GROUP"); LU = min(3.0, DUR["GROUP"])
shot("room", t + 0.9, LAUGH + LU, TWO, (900, 700, 1.62))                           # two-shot under the laugh: newspaper back up
t = LAUGH + LU; FREEZE = t - 0.2
shot("end", t, t + 2.4, None); t += 2.4
TOTAL = t

# ---------------- staging (world = room 1920x1080) ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
AZ = (440, 1010, 1.8); BD = (1140, 800, 1.8)                  # Aziza standing (feet) | Bandaq seated (hip-on-seat)
SOFA = (560, 1370, 800)                                       # same sofa as daily/11
DOOR = (300, 770)

def arms_at(sched, tt, d=0.22):
    prev = sched[0][1]
    for i, (t0, pose) in enumerate(sched):
        if tt < t0: break
        if tt < t0 + d and i > 0: return (sched[i - 1][1], pose, (tt - t0) / d)
        prev = pose
    return prev

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, held=None, sit=0, nod=0.0, walk=None):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    blink = ((tt + len(who) * 0.37) % 3.6) < 0.11 and expr not in ("sleepy", "laugh", "gasp", "shock")
    if not talking and walk is None: lean += math.sin(tt * 1.7 + len(who)) * 0.05
    X, Y_ = W2S(cam, x, y); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, held, lean, walk, sit=sit, nod=nod)

SOF = (150, 62, 58, 255); SOF_D = (112, 42, 40, 255); SOF_L = (178, 84, 76, 255)
def sofa_back(p, cam):
    z = cam[2]; x0, x1, sy = SOFA
    a_ = W2S(cam, x0, sy - 230); b = W2S(cam, x1, sy + 6); p.rect(a_[0], a_[1], b[0], b[1], SOF_D, INK, 3 * z, 26 * z)
    for i in range(3):
        cx = x0 + 40 + i * (x1 - x0 - 80) / 3
        a_ = W2S(cam, cx + 6, sy - 205); b = W2S(cam, cx + (x1 - x0 - 80) / 3 - 6, sy - 10); p.rect(a_[0], a_[1], b[0], b[1], SOF, INK, 2.5 * z, 18 * z)
    a_ = W2S(cam, x0 - 10, sy); b = W2S(cam, x1 + 10, sy + 70); p.rect(a_[0], a_[1], b[0], b[1], SOF_L, INK, 3 * z, 12 * z)
    a_ = W2S(cam, x0 - 10, sy + 70); b = W2S(cam, x1 + 10, sy + 120); p.rect(a_[0], a_[1], b[0], b[1], SOF_D, INK, 3 * z, 6 * z)
def sofa_front(p, cam):
    z = cam[2]; x0, x1, sy = SOFA
    for xx in (x0 - 60, x1 - 10):
        a_ = W2S(cam, xx, sy - 120); b = W2S(cam, xx + 70, sy + 120); p.rect(a_[0], a_[1], b[0], b[1], SOF, INK, 3 * z, 22 * z)
    for xx in (x0 + 10, x1 - 30):
        a_ = W2S(cam, xx, sy + 120); b = W2S(cam, xx + 20, sy + 160); p.rect(a_[0], a_[1], b[0], b[1], (60, 36, 20, 255), INK, 2 * z, 3 * z)

def door_open(p, cam, tt):
    k = ease(kk(tt, 0.0, 0.3)) * (1 - ease(kk(tt, 1.9, 2.3)))
    if k <= 0: return
    a_ = W2S(cam, 215, 230); b = W2S(cam, 402, 745)
    p.rect(a_[0], a_[1], b[0], b[1], (34, 26, 20, 255), None)
    lw = (b[0] - a_[0]) * (1 - 0.82 * k)
    p.poly([(a_[0], a_[1]), (a_[0] + lw, a_[1] + 14 * k * cam[2]), (a_[0] + lw, b[1] - 14 * k * cam[2]), (a_[0], b[1])], (92, 58, 36, 255), INK, 2 * cam[2])

def newspaper(p, cam, tt, up):
    """Bandaq's newspaper: up = held in front of his face (reading), else lowered on his lap"""
    z = cam[2]; x, y, s = BD; S = s * CH["bondo2"]["scale"]; sh = y - 72 * S; hx, hy = x, sh - 56 * S
    if up > 0:
        top = lerp(y - 20 * S, hy - 60 * S, up)
        a_ = W2S(cam, hx - 82 * S, top); b = W2S(cam, hx + 38 * S, top + 118 * S)
    else:
        a_ = W2S(cam, x - 74 * S, y - 34 * S); b = W2S(cam, x + 30 * S, y + 10 * S)
    p.rect(a_[0], a_[1], b[0], b[1], (236, 232, 218, 255), INK, 2 * z, 2 * z)
    w_, h_ = b[0] - a_[0], b[1] - a_[1]
    p.rect(a_[0] + w_ * 0.08, a_[1] + h_ * 0.1, b[0] - w_ * 0.08, a_[1] + h_ * 0.24, (60, 60, 60, 255), None)        # headline bar
    p.rect(a_[0] + w_ * 0.08, a_[1] + h_ * 0.32, a_[0] + w_ * 0.45, b[1] - h_ * 0.12, (170, 170, 170, 255), None)    # photo
    for i in range(5):
        yy = a_[1] + h_ * (0.34 + i * 0.11)
        if yy < b[1] - h_ * 0.1: p.line([(a_[0] + w_ * 0.52, yy), (b[0] - w_ * 0.08, yy)], (120, 120, 120, 255), 1.5 * z)
    p.line([(a_[0] + w_ / 2, a_[1]), (a_[0] + w_ / 2, b[1])], (200, 196, 180, 255), 1.5 * z)                      # fold

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

def hearts(fr, cam, tt, t0, t1):
    """hearts float up around Aziza while she dreams of the trip — they POP on the punchline"""
    if not (t0 <= tt < t1 + 0.9): return
    z = cam[2]; d = ImageDraw.Draw(fr, "RGBA")
    for i in range(7):
        ph = (tt * 0.5 + i / 7) % 1.0
        x, y = W2S(cam, AZ[0] - 140 + (i % 4) * 95 + math.sin(tt * 2 + i) * 20, 600 - ph * 220)
        a_ = int(220 * math.sin(ph * math.pi) * kk(tt, t0, t0 + 0.3)); r = (12 + (i % 2) * 6) * z
        if tt >= t1: r *= 1 + 3 * kk(tt, t1, t1 + 0.9); a_ = int(a_ * (1 - kk(tt, t1 + 0.3, t1 + 0.9)))
        d.ellipse([x - 2 * r, y - r, x, y + r * 0.6], fill=(235, 60, 90, a_)); d.ellipse([x, y - r, x + 2 * r, y + r * 0.6], fill=(235, 60, 90, a_))
        d.polygon([(x - 2 * r + 1, y), (x + 2 * r - 1, y), (x, y + 2 * r)], fill=(235, 60, 90, a_))

def sweat(fr, cam, tt, t0):
    """Bandaq sweats when he hears «أسبوع»"""
    if tt < t0 or tt >= T("A2"): return
    z = cam[2]; d = ImageDraw.Draw(fr, "RGBA"); x, y, s = BD; S = s * CH["bondo2"]["scale"]; hy = y - 72 * S - 56 * S
    for i, (dx, ph) in enumerate(((-40, 0.0), (36, 0.5))):
        u = (tt * 0.8 + ph) % 1.0; q = W2S(cam, x + dx * S, hy - 20 * S + u * 46 * S); r = 5 * S * z
        d.ellipse([q[0] - r, q[1] - r * 1.5, q[0] + r, q[1] + r * 1.5], fill=(190, 225, 255, int(230 * (1 - u))), outline=(60, 110, 170, int(255 * (1 - u))), width=2)

_BUB = {}
def bubble(fr, cam, tt):
    """sepia thought bubble: the clinic, Dr. Zalata talking to her (callback to «الخبر الوحش»)"""
    if not (BUB[0] <= tt < BUB[1]): return
    k = popk(tt, BUB[0], 0.3) * (1 - kk(tt, BUB[1] - 0.25, BUB[1]))
    if k <= 0: return
    bw, bh = 620, 380
    f = int((tt - BUB[0]) * FPS) // 2
    if f not in _BUB:
        sc = CLINIC.crop((180, 120, 1180, 733)).resize((bw, bh), Image.LANCZOS)
        lay = Image.new("RGBA", (int(bw * SS), int(bh * SS)), (0, 0, 0, 0))
        tt_ = BUB[0] + f * 2 / FPS; m = 0.5 + 0.45 * math.sin(tt_ * 17)
        draw_char(P(lay), DRZ, 300, 560, 1.75, "flat", m, 1, False, "talk", tt_, "notebook", 0.0, None)
        lay = lay.resize((bw, bh), Image.LANCZOS); sc.paste(lay, (0, 0), lay)
        sc = ImageOps.colorize(ImageOps.grayscale(sc), (60, 40, 20), (250, 232, 196))
        lzt(sc, 470, 50, "د. زلطة", 44, (255, 240, 200), (70, 40, 15))
        _BUB[f] = sc
    sc = _BUB[f]
    w2, h2 = int(bw * k * 0.9), int(bh * k * 0.9)
    if w2 < 10: return
    img = sc.resize((w2, h2), Image.LANCZOS)
    mask = Image.new("L", (w2, h2), 0); ImageDraw.Draw(mask).ellipse([0, 0, w2 - 1, h2 - 1], fill=255)
    cx, cy = W * 0.66, H * 0.30
    d = ImageDraw.Draw(fr, "RGBA")
    d.ellipse([cx - w2 / 2 - 10, cy - h2 / 2 - 10, cx + w2 / 2 + 10, cy + h2 / 2 + 10], fill=(255, 255, 255, 255))
    fr.paste(img, (int(cx - w2 / 2), int(cy - h2 / 2)), mask)
    hx, hy = W2S(cam, AZ[0] + 60, 560)
    for i, r in enumerate((14, 22, 32)):                                                   # little cloud dots from her head to the bubble
        u = (i + 1) / 4; px = lerp(hx, cx - w2 / 2, u); py = lerp(hy, cy + h2 / 3, u)
        d.ellipse([px - r * k, py - r * k, px + r * k, py + r * k], fill=(255, 255, 255, 255), outline=(40, 30, 20, 255), width=3)

def rx_insert(tt, sh):
    """the prescription: «فُسحة… أسبوع على الأقل» signed by Dr. Zalata"""
    u = kk(tt, sh["start"], sh["end"]); zz = 1.0 + 0.10 * ease(u, "crash")
    cam = (AZ[0] - 960 / 2.4, 640 - 540 / 2.4, 2.4)
    fr = bg_crop(ROOM, (max(0, cam[0]), max(0, cam[1]), 2.4)).resize((W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(10))
    fr = ImageEnhance.Brightness(fr).enhance(0.6)
    pw, ph = int(820 * zz), int(980 * zz)
    paper = Image.new("RGB", (820, 980), (252, 250, 240)); d = ImageDraw.Draw(paper)
    d.rectangle([0, 0, 819, 979], outline=(60, 60, 60), width=6)
    d.rectangle([0, 0, 819, 150], fill=(70, 130, 190))
    lzt(paper, 410, 60, "عيادة د. زلطة", 64, (255, 255, 255), (30, 60, 100))
    lzt(paper, 410, 118, "باطنة • قلب • نفسية", 34, (220, 235, 255), (30, 60, 100))
    lzt(paper, 690, 230, "Rx", 80, (40, 40, 40), (252, 250, 240), font=DJ)
    lzt(paper, 380, 230, "الاسم: عزيزة", 48, (40, 40, 40), (252, 250, 240))
    rows = [("فُسحة", 0.9), ("خروجة", 1.3), ("أسبوع على الأقل!", 1.7)]
    for i, (s_, t0) in enumerate(rows):
        kk_ = popk(tt, sh["start"] + t0 - 0.6, 0.2)
        if kk_ > 0: lzt(paper, 420, 360 + i * 130, f"{i + 1} - {s_}", int(70 * kk_), (20, 50, 140), (252, 250, 240))
        d.line([(80, 410 + i * 130), (740, 410 + i * 130)], fill=(200, 200, 210), width=2)
    k2 = popk(tt, sh["start"] + 1.35, 0.25)                                                 # the stamp
    if k2 > 0:
        st = Image.new("RGBA", (300, 300), (0, 0, 0, 0)); ds = ImageDraw.Draw(st)
        ds.ellipse([10, 10, 290, 290], outline=(200, 30, 40, 220), width=12); ds.ellipse([40, 40, 260, 260], outline=(200, 30, 40, 200), width=5)
        lzt(st, 150, 150, "د. زلطة", 64, (200, 30, 40), (252, 250, 240))
        st = st.rotate(-14, resample=Image.BICUBIC).resize((int(300 * k2 * 0.8), int(300 * k2 * 0.8)), Image.LANCZOS)
        paper.paste(st, (int(560 - st.size[0] / 2), int(840 - st.size[1] / 2)), st)
    paper = paper.convert("RGBA").resize((pw, ph), Image.LANCZOS).rotate(4 - 3 * ease(u), expand=True, resample=Image.BICUBIC)
    fr.paste(paper, (int(W / 2 - paper.size[0] / 2), int(H / 2 - paper.size[1] / 2 + 30)), paper)
    return fr

_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/daily/13")
_FC = {}
def frame_cache(t_):
    if t_ not in _FC: _FC[t_] = frame(t_)
    return _FC[t_]
def endcard(tt, sh):
    k = kk(tt, sh["start"], sh["start"] + 0.4)
    fr = ImageEnhance.Brightness(frame_cache(FREEZE)).enhance(1 - 0.55 * k).filter(ImageFilter.GaussianBlur(6 * k)).convert("RGBA")
    sc = popk(tt, sh["start"] + 0.1, 0.3)
    if sc > 0: lzt(fr, W / 2, 400, "منشن جوزك اللي هيرد كده!", int(96 * sc), (255, 214, 90))
    if tt >= sh["start"] + 0.5:
        logo(fr, W / 2, 680, 130); text(fr, W / 2, 830, "@shattawzalata", 52, (255, 214, 90))
    return fr.convert("RGB")

def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "end": return finish(endcard(tt, sh), tt)
    if sh["set"] == "rx": return finish(rx_insert(tt, sh), tt)
    cam = cam_at(sh, tt); z = cam[2]
    img = bg_crop(ROOM, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    door_open(p, cam, tt)
    sofa_back(p, cam)
    # ---- Bandaq (seated right, faces left): newspaper up at 0, lowered on «الدكتور…», back up after the punchline
    up = 1 - ease(kk(tt, 0.05, 0.4))
    if tt >= PUNCH + DUR["B2"] - 0.3: up = ease(kk(tt, PUNCH + DUR["B2"] - 0.3, PUNCH + DUR["B2"] + 0.2))
    bex = "neutral"
    if A1 + 6.4 <= tt < T("A2"): bex = "scared"
    if T("A2") <= tt < PUNCH: bex = "flat"
    barms = "scared" if up > 0.5 else "hold"
    person(lay, cam, "bondo2", *BD, tt, bex, -1, barms, 0.0, None, sit=-1)
    newspaper(p, cam, tt, up)
    sofa_front(p, cam)
    # ---- Aziza: walks in from the door, prescription in hand
    k = kk(tt, 0.0, 1.7); e = ease(k)
    ax, ay, as_ = lerp(DOOR[0], AZ[0], e), lerp(DOOR[1] + 40, AZ[1], e), AZ[2] * lerp(0.8, 1.0, e)
    wk = tt * 8 if 0 < k < 1 else None
    aex = "neutral"
    if tt >= A1: aex = "sad"
    if T("A2") <= tt < PUNCH + 0.4: aex = "happy"
    if tt >= PUNCH + 0.4: aex = "shock"
    if tt >= LAUGH + 1.2: aex = "angry"
    aarms = arms_at([(0, "hold"), (A1, "salute"), (A1 + 3.75, "point"), (A1 + 6.45, "raise"), (T("A2"), "clap"), (PUNCH + 0.4, "down"), (LAUGH + 1.2, "hips")], tt)
    alean = 0.0
    if T("A2") <= tt < PUNCH + 0.4: alean = 0.22 * kk(tt, T("A2"), T("A2") + 0.4)
    if FREEZE0 <= tt < LAUGH + 1.2: alean = math.sin(tt * 60) * 0.02                       # frozen, tiny tremble
    person(lay, cam, "aziza", ax, ay, as_, tt, aex, 1, aarms, alean, "paper" if tt < A1 + 6.45 else None, walk=wk)
    lay = tint_layer(lay, (255, 236, 210)); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    bubble(fr, cam, tt)
    hearts(fr, cam, tt, T("A2"), PUNCH + DUR["B2"] - 0.2)
    sweat(fr, cam, tt, A1 + 6.4)
    if FREEZE0 <= tt < FREEZE0 + 0.9:                                                       # her eye twitches
        q = W2S(cam, AZ[0] + 20, AZ[1] - 330)
        if int(tt * 14) % 2: lzt(fr, q[0] + 150, q[1] - 40, "!", int(70 * z / 2.5), (255, 80, 60))
    if tt < 3.2:                                                                            # hook banner (H)
        a_ = int(255 * min(1, (3.2 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([W / 2 - 720, 40, W / 2 + 720, 150], 30, fill=(20, 12, 8, int(a_ * 0.8)))
        lzt(fr, W / 2, 95, "الدكتور قالها: جوزك لازم يفسّحك… ورده؟!", 70, (255, 214, 90), alpha=a_)
    return finish(fr, tt)

def vertical(fr, tt):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = ImageEnhance.Brightness(small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.35)
    bgv.paste(fr.resize((1080, 608), Image.LANCZOS), (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(255, 214, 90)); d.rectangle([0, 1168, 1080, 1171], fill=(255, 214, 90))
    lzt(bgv, 540, 250, "الدكتور قالها", 100, (255, 255, 255))
    lzt(bgv, 540, 395, "جوزك لازم يفسّحك!", 104, (255, 214, 90))
    lzt(bgv, 540, 1840, SERIES, 44, (255, 150, 110))
    k, _ = line_at(tt)
    if k and SUB.get(k):
        for i, l in enumerate(wrap(SUB[k])[:4]): text(bgv, 540, 1290 + i * 80, l, 60, sw=6)
    return bgv

def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(48)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 300) * 0.02, 0, 1.0)
    mix_into(buf, SFXF["creak"] * 0.5, 0.0, 1.0); mix_into(buf, SFXF["steps"] * 0.35, 0.1, 1.0)
    mix_into(buf, lowpass(r.normal(0, 1, int(SR * 0.25)).astype(np.float32), 3000) * 0.08, 0.1, 1.0)          # newspaper rustle
    for k_, f in enumerate((392, 370, 349, 330)): mix_into(buf, tone(f, 0.6, 0.05, 3), BUB[0] + k_ * 0.6, 1.0)   # sad violin-ish notes under «تعبانة»
    mix_into(buf, SFXF["whoosh"] * 0.4, RX - 0.1, 1.0)
    mix_into(buf, tone(140, 0.3, 0.3, 10) + tone(90, 0.3, 0.25, 10), RX + 1.35, 1.0)                           # stamp
    for k_, f in enumerate((523, 659, 784, 1047)): mix_into(buf, tone(f, 0.45, 0.07, 5), T("A2") + k_ * 0.35, 1.0)  # happy music box
    mix_into(buf, lowpass(r.normal(0, 1, int(SR * 0.25)).astype(np.float32), 3000) * 0.08, PUNCH + DUR["B2"] - 0.3, 1.0)
    for j in range(3): mix_into(buf, tone(4200, 0.05, 0.06, 30) + tone(4600, 0.05, 0.04, 30), FREEZE0 + 0.1 + j * 0.22, 1.0)  # cricket
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 0.5: mix_into(buf, SFXF["whoosh"] * 0.25, s_["start"] - 0.1, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), TOTAL - 2.3 + k_ * 0.09, 1.0)
    rms = lambda x: float(np.sqrt(np.mean(x ** 2))) + 1e-9; ref = []
    for st, k in lines:
        if k == "GROUP": continue
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8; ref.append(rms(v)); mix_into(buf, v, st, 1.0)
    g = AUD["GROUP"][:int(SR * LU)].copy(); g[-int(SR * 0.4):] *= np.linspace(1, 0, int(SR * 0.4))
    mix_into(buf, g / rms(g) * float(np.mean(ref)) * 1.2, LAUGH, 1.0)
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
