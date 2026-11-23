# «يوميات شطة وزلطة» — «فاكر النهارده إيه؟» (23/11) — growth_rules: native 9:16, phrase subs + yellow key word + speaker name,
#   hook 3 s, motion+sound on frame 1, ONE ask end card («تابع بندق وعزيزة»), own cover, laugh = SOUND only.
# Bandaq & Aziza on the red sofa (canonical «أوضة بندق وعزيزة»). She asks «فاكر النهارده إيه؟» — three wrong guesses
# (cake / rings / market thought bubbles, a red ✗ + buzzer each), slipper comes out… «آخر يوم ماما قاعدة عندنا» —
# he jumps with joy «ده أحلى يوم في السنة!» (confetti) → «بنـدق!!» crash zoom, slipper up, confetti dies + audience laugh.
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/daily/18")
SERIES = "يوميات شطة وزلطة"; EPT = "فاكر النهارده إيه؟"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"
SFXF = {n: load_audio(ROOT + f"/trend/01/sfx/{n}.mp3") for n in ("whoosh", "gasp")}
SUB = {"AZ1": "يا بندق… إنت فاكر النهارده إيه؟", "B1": "النهارده؟! …عيد ميلادك؟", "AZ2": "لأ!", "B2": "عيد جوازنا؟", "AZ3": "لأ!",
       "B3": "اليوم اللي شفتك فيه أول مرة في السوق؟", "AZ4": "لأ يا بندق!", "B4": "طب قوليلي إنتي… وريّحيني!",
       "AZ5": "النهارده… آخر يوم ماما قاعدة عندنا.", "B5": "بجد؟! ده أحلى يوم في السنة!", "AZ6": "بنـدق!!", "GROUP": ""}
CHUNKS = {"AZ1": [(0.0, "يا بندق…", None), (1.95, "إنت فاكر النهارده إيه؟", "فاكر")],
          "B1": [(0.0, "النهارده؟!", None), (2.45, "عيد ميلادك؟", "عيد ميلادك")],
          "AZ2": [(0.0, "لأ!", "لأ!")], "B2": [(0.0, "عيد جوازنا؟", "جوازنا")], "AZ3": [(0.0, "لأ!", "لأ!")],
          "B3": [(0.0, "اليوم اللي شفتك فيه", "شفتك"), (1.85, "أول مرة في السوق؟", "السوق")],
          "AZ4": [(0.0, "لأ يا بندق!", "لأ")],
          "B4": [(0.0, "طب قوليلي إنتي…", "قوليلي"), (1.85, "وريّحيني!", "وريّحيني")],
          "AZ5": [(0.0, "النهارده…", None), (1.62, "آخر يوم ماما قاعدة عندنا.", "آخر يوم")],
          "B5": [(0.0, "بجد؟!", "بجد"), (1.0, "ده أحلى يوم في السنة!", "أحلى يوم")],
          "AZ6": [(0.0, "بنـدق!!", "بنـدق!!")]}
WHO = {k: ("aziza" if k.startswith("AZ") else "bondo2") for k in SUB}; WHO["GROUP"] = "-"
NAME = {"bondo2": ("بندق", (230, 170, 110)), "aziza": ("عزيزة", (255, 110, 170))}
EXPR = {"AZ1": "smug", "B1": [(0, "scared"), (1.1, "flat"), (2.3, "happy")], "AZ2": "angry", "B2": "happy", "AZ3": "angry",
        "B3": [(0, "happy"), (1.8, "smug")], "AZ4": "shout", "B4": "scared", "AZ5": [(0, "sad"), (1.5, "sad")],
        "B5": [(0, "shock"), (0.9, "laugh")], "AZ6": "shout", "GROUP": "laugh"}
load_lines(list(SUB))
ROOM = _ld(ROOT + "/daily/bg/bandaq_room.png")

# ---------------- staging (world = room 1920x1080; sofa as daily/11 & 17) ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
AZ = (790, 800, 1.8); BD = (1140, 800, 1.8)
SOFA = (560, 1370, 800)

# ---------------- timeline (both always in frame — the camera breathes and punches) ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
TW_H = lambda z, cy=650, cx=965: (cx, cy, z)
TW_V = lambda z, cy=640, cx=965: (cx, cy, z)
t = say(0.15, "AZ1") + 0.05
shot("room", 0.0, t, TW_H(2.4), TW_H(2.1), ease="crash", v=(TW_V(2.05), TW_V(1.9)))         # frame 1: pull-out reveal
s = t; t = say(s + 0.05, "B1") + 0.1; GUESS1 = T("B1") + 2.4
shot("room", s, t, TW_H(2.1), TW_H(2.25, 640, 1000), v=(TW_V(1.9), TW_V(1.96, 640, 990)))     # slow push on his panic
X1 = t; t = say(t + 0.05, "AZ2") + 0.15; shakes.append((X1 + 0.05, 9))
shot("room", s if False else X1, t, TW_H(2.35, 640, 940), TW_H(2.3, 640, 945), ease="crash", v=(TW_V(2.0, 640, 940), TW_V(1.98, 640, 945)))
s = t; t = say(s + 0.05, "B2") + 0.1; GUESS2 = T("B2")
shot("room", s, t, TW_H(2.2, 645, 1000), TW_H(2.25, 640, 1000), v=(TW_V(1.94, 640, 990), TW_V(1.96, 640, 990)))
X2 = t; t = say(t + 0.05, "AZ3") + 0.15; shakes.append((X2 + 0.05, 12))
shot("room", X2, t, TW_H(2.45, 635, 940), TW_H(2.4, 635, 945), ease="crash", v=(TW_V(2.04, 635, 940), TW_V(2.02, 635, 945)))
s = t; t = say(s + 0.1, "B3") + 0.1; GUESS3 = T("B3")
shot("room", s, t, TW_H(2.15), TW_H(2.3, 640, 1000), v=(TW_V(1.9), TW_V(1.97, 640, 990)))      # dreamy push
X3 = t; t = say(t + 0.05, "AZ4") + 0.2; shakes.append((X3 + 0.05, 15)); SLIP = T("AZ4") + 0.35
shot("room", X3, t, TW_H(2.55, 625, 930), TW_H(2.5, 625, 935), ease="crash", v=(TW_V(2.1, 630, 930), TW_V(2.08, 630, 935)))
s = t; t = say(s + 0.05, "B4") + 0.15
shot("room", s, t, TW_H(2.2, 645, 1000), TW_H(2.05), v=(TW_V(1.94, 640, 990), TW_V(1.88)))
s = t; t = say(s + 0.1, "AZ5") + 0.1; MAMA = T("AZ5") + 1.62
shot("room", s, t, TW_H(2.05), TW_H(2.3, 640, 930), v=(TW_V(1.88), TW_V(1.98, 640, 935)))      # slow sad push on her
s = t; t = say(s + 0.05, "B5") + 0.05; JOY = T("B5") + 0.9
shot("room", s, JOY, TW_H(2.3, 640, 930), TW_H(2.2, 640, 1010), v=(TW_V(1.98, 640, 935), TW_V(1.94, 640, 1000)))
shot("room", JOY, t, TW_H(2.05, 620, 990), TW_H(1.95, 615, 985), ease="crash", v=(TW_V(1.86, 620, 985), TW_V(1.82, 615, 980)))   # he jumps — pull out
SHOCK = t; shakes.append((SHOCK + 0.05, 20))
t = say(SHOCK + 0.1, "AZ6")
shot("room", SHOCK, t + 0.3, TW_H(2.7, 610, 940), TW_H(2.85, 605, 945), ease="crash", v=(TW_V(2.15, 615, 945), TW_V(2.25, 610, 950)))
LAUGH = t - 0.15; say(LAUGH, "GROUP"); LU = min(2.6, DUR["GROUP"])
shot("room", t + 0.3, LAUGH + LU, TW_H(2.2), TW_H(2.0), v=(TW_V(1.9), TW_V(1.84)))
t = LAUGH + LU
shot("end", t, t + 2.6, None, v=None); t += 2.6
TOTAL = t
XS = (X1, X2, X3)

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

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, held=None, sit=0, nod=0.0, hop=0.0):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    blink = ((tt + len(who) * 0.37) % 3.6) < 0.11 and expr not in ("sleepy", "laugh", "shock", "angry", "shout")
    if not talking: lean += math.sin(tt * 1.7 + len(who)) * 0.04
    X, Y_ = W2S(cam, x, y - hop); S = s * cam[2]
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

def kk2(tt, a, b): return max(0.0, min(1.0, (tt - a) / max(1e-6, b - a)))
def popk(tt, t0, d=0.22):
    u = kk(tt, t0, t0 + d); return 0 if u <= 0 else (1 + 0.25 * math.sin(u * math.pi)) if u < 1 else 1

def heart(d, x, y, r, col):
    d.ellipse([x - 2 * r, y - r, x, y + r * 0.6], fill=col); d.ellipse([x, y - r, x + 2 * r, y + r * 0.6], fill=col)
    d.polygon([(x - 2 * r + 1, y), (x + 2 * r - 1, y), (x, y + 2 * r)], fill=col)

def thought(fr, cam, tt, t0, t1, kind):
    """thought bubble over Bandaq with the drawn guess (cake / rings / market heart) — pops in, crushed by her «لأ!»"""
    if not (t0 <= tt < t1 + 0.35): return
    z = cam[2]; S = BD[2] * CH["bondo2"]["scale"]
    sc = popk(tt, t0, 0.25) * (1 - kk2(tt, t1, t1 + 0.3)); a = int(255 * (1 - kk2(tt, t1, t1 + 0.35)))
    if sc <= 0.02: return
    hx, hy = W2S(cam, BD[0] + 10 * S, BD[1] - 250 * S)
    Wd, Hd = fr.size
    if Wd > Hd: hx, hy = hx + 90, 330; cx, cy = hx + 250, 215                       # 16:9 — up-right of his head
    else: cx, cy = Wd * 0.5, hy - 330                                              # 9:16 — above, between the two heads
    R = 92 * z / 2.2 * sc
    lay = Image.new("RGBA", fr.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for i, (dx, dy, rr) in enumerate(((0.25, 0.75, 0.12), (0.55, 0.45, 0.2))):
        px, py = hx + (cx - hx) * dx, hy + (cy - hy) * dy; r = R * rr * 1.4
        d.ellipse([px - r, py - r, px + r, py + r], fill=(255, 255, 255, a), outline=(20, 12, 8, a), width=max(2, int(3 * z)))
    d.ellipse([cx - R * 1.25, cy - R, cx + R * 1.25, cy + R], fill=(255, 255, 255, a), outline=(20, 12, 8, a), width=max(3, int(4 * z)))
    u = R / 60; w = max(2, int(3 * z))
    if kind == "cake":
        d.rectangle([cx - 34 * u, cy - 4 * u, cx + 34 * u, cy + 30 * u], fill=(240, 150, 190, a), outline=(20, 12, 8, a), width=w)
        d.rectangle([cx - 34 * u, cy - 4 * u, cx + 34 * u, cy + 6 * u], fill=(255, 250, 240, a))
        d.rectangle([cx - 3 * u, cy - 26 * u, cx + 3 * u, cy - 4 * u], fill=(90, 150, 240, a))
        fl = 1 + 0.15 * math.sin(tt * 30); d.ellipse([cx - 5 * u, cy - 40 * u * fl, cx + 5 * u, cy - 26 * u], fill=(255, 190, 40, a))
    elif kind == "rings":
        for dx in (-14, 14):
            d.ellipse([cx + dx * u - 22 * u, cy - 16 * u, cx + dx * u + 22 * u, cy + 28 * u], outline=(235, 190, 50, a), width=max(4, int(7 * u)))
        d.polygon([(cx - 14 * u, cy - 16 * u), (cx - 24 * u, cy - 30 * u), (cx - 4 * u, cy - 30 * u)], fill=(170, 230, 255, a))
    else:   # market: a fruit stall + a tiny heart
        d.rectangle([cx - 40 * u, cy + 4 * u, cx + 40 * u, cy + 30 * u], fill=(170, 110, 60, a), outline=(20, 12, 8, a), width=w)
        for i, col in enumerate(((235, 70, 50), (255, 160, 40), (120, 200, 70), (235, 70, 50))):
            d.ellipse([cx - 36 * u + i * 19 * u, cy - 12 * u, cx - 20 * u + i * 19 * u, cy + 4 * u], fill=col + (a,))
        heart(d, cx, cy - 32 * u + math.sin(tt * 4) * 3 * u, 9 * u, (235, 60, 90, a))
    fr.paste(lay, (0, 0), lay)

def red_x(fr, cam, tt):
    """a big red ✗ slams between them on every «لأ!» — and a tally of ✗ in the corner of the frame"""
    d = ImageDraw.Draw(fr, "RGBA"); z = cam[2]
    for i, xt in enumerate(XS):
        if xt <= tt < xt + 0.9:
            sc = popk(tt, xt, 0.18) * (1.0 + 0.6 * (1 - kk2(tt, xt, xt + 0.12))); a = int(255 * (1 - kk2(tt, xt + 0.6, xt + 0.9)))
            cx, cy = W2S(cam, 965, 560); r = (80 + 14 * i) * z * 0.55 * sc; w = max(8, int((20 + 5 * i) * z * 0.55 * sc))
            for s_ in (1, -1):
                d.line([(cx - r, cy - r * s_), (cx + r, cy + r * s_)], fill=(30, 8, 8, a), width=w + 8)
                d.line([(cx - r, cy - r * s_), (cx + r, cy + r * s_)], fill=(230, 40, 40, a), width=w)

def sweat(fr, cam, tt, n):
    if n <= 0: return
    d = ImageDraw.Draw(fr, "RGBA"); z = cam[2]; S = BD[2] * CH["bondo2"]["scale"]
    for i in range(n):
        u = (tt * (0.9 + 0.15 * i) + i * 0.37) % 1.0
        q = W2S(cam, BD[0] + (-50 + 100 * (i % 2) + 12 * (i // 2)) * S, BD[1] - 260 * S + u * 55 * S); r = (4.5 + i * 0.4) * S * z
        d.ellipse([q[0] - r, q[1] - r * 1.5, q[0] + r, q[1] + r * 1.5], fill=(190, 225, 255, int(230 * (1 - u))), outline=(60, 110, 170, int(255 * (1 - u))), width=2)

CONF = [(np.random.default_rng(5).uniform(-1, 1), np.random.default_rng(i).uniform(0.4, 1.4), i) for i in range(46)]
def confetti(fr, cam, tt):
    """party confetti burst from Bandaq at «أحلى يوم في السنة!» — it freezes and drops dead on «بنـدق!!»"""
    if tt < JOY or tt > SHOCK + 1.4: return
    d = ImageDraw.Draw(fr, "RGBA"); z = cam[2]; S = BD[2] * CH["bondo2"]["scale"]
    ox, oy = BD[0], BD[1] - 300 * S
    cols = ((255, 90, 90), (255, 210, 60), (90, 200, 255), (130, 230, 120), (240, 120, 230))
    tl = min(tt, SHOCK) - JOY; dead = kk2(tt, SHOCK, SHOCK + 1.2)
    for i in range(46):
        r_ = np.random.default_rng(100 + i); ang = r_.uniform(-2.6, -0.5); sp = r_.uniform(260, 620)
        x = ox + math.cos(ang) * sp * tl; y = oy + math.sin(ang) * sp * tl + 330 * tl * tl + dead * 900
        x, y = W2S(cam, x, y); a = int(255 * (1 - dead))
        rr = 7 * z * 0.6; rot = tt * 8 + i
        pts = [(x + math.cos(rot + q) * rr * (2 if q % 2 else 1), y + math.sin(rot + q) * rr) for q in (0, 1.6, 3.14, 4.7)]
        d.polygon(pts, fill=cols[i % 5] + (a,))

def scene(tt, cam, size):
    Wd, Hd = size; x0, y0, z = cam
    box = (x0, y0, x0 + Wd / z, y0 + Hd / z)
    img = ROOM.resize((int(Wd * SS), int(Hd * SS)), Image.BICUBIC, box=box)
    if z > 1.9: img = img.filter(ImageFilter.GaussianBlur(min(2.5, (z - 1.8) * 1.4)))
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); p = P(lay)
    sofa_back(p, cam)
    k, lt = line_at(tt)
    # ---- Aziza (left, faces him): sweet test → ✗ ✗ → slipper out → sad «ماما» → explodes «بنـدق!!»
    aex = "smug"
    if T("B1") <= tt < X1: aex = "smug" if k != "B1" or lt < 2.4 else "flat"
    elif X1 <= tt < X2: aex = "angry" if tt < X1 + 1.2 else "flat"
    elif X2 <= tt < X3: aex = "angry" if tt < X2 + 1.0 else ("flat" if tt < T("B3") + 1.8 else "angry")
    elif X3 <= tt < T("AZ5"): aex = "angry"
    elif T("AZ5") <= tt < JOY: aex = "sad"
    elif JOY <= tt < SHOCK: aex = "shock"
    elif tt >= SHOCK: aex = "shout" if tt < SHOCK + 1.4 else "angry"
    if k == "B4" and lt > 1.8: aex = "sad"
    held = "slipper" if SLIP <= tt < T("AZ5") + 0.3 or tt >= SHOCK else None
    aarms = arms_at([(0, "hips"), (X1, "point"), (X1 + 0.7, "hips"), (X2, "point"), (X2 + 0.7, "hips"), (SLIP - 0.2, "raise"),
                     (T("B4") + 0.6, "hold"), (T("AZ5") + 0.3, "down"), (JOY, "clap2"), (SHOCK, "raise")], tt, 0.18)
    alean = 0.05
    if X1 <= tt < X1 + 0.5 or X2 <= tt < X2 + 0.5: alean = 0.22
    if X3 <= tt < X3 + 0.8: alean = 0.3
    if T("AZ5") <= tt < JOY: alean = -0.05
    if JOY <= tt < SHOCK: alean = -0.15
    if tt >= SHOCK: alean = 0.3 * kk2(tt, SHOCK, SHOCK + 0.2)
    anod = math.sin((tt - T("AZ5")) * 3) * 2 if T("AZ5") <= tt < JOY else 0.0
    person(lay, cam, "aziza", *AZ, tt, aex, 1, aarms, alean, held, sit=1, nod=anod)
    # ---- Bandaq (right, faces her): relaxed → panic & sweat → guesses (proud each time) → begs → JUMPS → freezes
    bex = "happy" if tt < T("AZ1") + 1.9 else "scared"
    if k in ("AZ2", "AZ3") or (X1 <= tt < T("B2")) or (X2 <= tt < T("B3")): bex = "scared"
    if X3 <= tt < T("B4"): bex = "scared"
    if k == "AZ5": bex = "flat" if lt < 1.62 else ("shock" if lt < 2.4 else "happy")
    if tt >= SHOCK: bex = "scared"
    barms = arms_at([(0, "down"), (T("AZ1") + 1.9, "scared"), (T("B1") + 1.1, "talk"), (X1, "scared"), (T("B2"), "raise"),
                     (X2, "scared"), (T("B3"), "talk"), (X3, "scared"), (T("B4") + 0.1, "up"), (T("B4") + 1.85, "clap"),
                     (T("AZ5"), "down"), (JOY, "up"), (SHOCK + 0.1, "scared")], tt)
    blean = 0.0
    if k == "B1" and 1.1 <= lt < 2.4: blean = -0.08                                  # looks up, thinking
    if any(xt <= tt < xt + 0.5 for xt in XS): blean = -0.22                           # flinches back at every «لأ!»
    if k == "B4": blean = 0.2                                                         # begs, leaning in
    if tt >= SHOCK: blean = -0.3 * kk2(tt, SHOCK, SHOCK + 0.25)
    hop = 0.0
    if JOY <= tt < SHOCK: hop = abs(math.sin((tt - JOY) * 7.5)) * 40                   # bouncing on the sofa
    bnod = math.sin((tt - T("B1")) * 2.2) * 5 if k == "B1" and 1.1 <= lt < 2.4 else 0.0
    person(lay, cam, "bondo2", *BD, tt, bex, -1, barms, blean, None, sit=-1, nod=bnod, hop=hop)
    sofa_front(p, cam)
    lay = tint_layer(lay, (255, 238, 212)); img.paste(lay, (0, 0), lay)
    fr = img.resize((Wd, Hd), Image.LANCZOS)
    # ---- effects
    thought(fr, cam, tt, GUESS1 - 0.1, X1, "cake"); thought(fr, cam, tt, GUESS2 - 0.05, X2, "rings"); thought(fr, cam, tt, GUESS3 + 0.1, X3, "market")
    red_x(fr, cam, tt); confetti(fr, cam, tt)
    nsw = 0
    if tt >= T("AZ1") + 1.9: nsw = 1
    if tt >= X1: nsw = 2
    if tt >= X2: nsw = 3
    if tt >= X3: nsw = 4
    if T("AZ5") + 2.4 <= tt < SHOCK: nsw = 0
    if tt >= SHOCK + 0.6: nsw = 5
    sweat(fr, cam, tt, nsw)
    d = ImageDraw.Draw(fr, "RGBA")
    if T("AZ1") + 1.95 <= tt < T("AZ1") + 3.0:                                         # «?» pops over him on «فاكر»
        S = BD[2] * CH["bondo2"]["scale"]; c = W2S(cam, BD[0] + 10 * S, BD[1] - 360 * S)
        lzt(fr, c[0], c[1], "؟", int(80 * z / 2 * popk(tt, T("AZ1") + 1.95, 0.2)), (255, 214, 60))
    if SHOCK <= tt < SHOCK + 0.9:                                                       # anger lines around her head
        S = AZ[2] * CH["aziza"]["scale"]; c = W2S(cam, AZ[0], AZ[1] - 210 * S); u = kk(tt, SHOCK, SHOCK + 0.25)
        for i in range(12):
            a_ = i / 12 * 2 * math.pi; r0, r1 = 95 * S * z, (95 + 50 * u) * S * z
            d.line([(c[0] + math.cos(a_) * r0, c[1] + math.sin(a_) * r0), (c[0] + math.cos(a_) * r1, c[1] + math.sin(a_) * r1)],
                   fill=(255, 90, 60, int(230 * (1 - kk(tt, SHOCK + 0.5, SHOCK + 0.9)))), width=max(3, int(4 * z)))
    if SHOCK + 0.1 <= tt < SHOCK + 1.6:                                                 # «!!» over her
        S = AZ[2] * CH["aziza"]["scale"]; c = W2S(cam, AZ[0] + 60 * S, AZ[1] - 330 * S)
        lzt(fr, c[0], c[1], "!!", int(90 * z / 2 * popk(tt, SHOCK + 0.1, 0.2)), (255, 80, 60))
    if SHOCK + 0.2 <= tt:                                                               # steam puffs from her head
        S = AZ[2] * CH["aziza"]["scale"]
        for i in range(3):
            u = (tt * 1.3 + i / 3) % 1.0; q = W2S(cam, AZ[0] + (-40 + 40 * i) * S, AZ[1] - 300 * S - u * 70 * S); r = (8 + u * 14) * S * z
            d.ellipse([q[0] - r, q[1] - r, q[0] + r, q[1] + r], fill=(255, 255, 255, int(170 * (1 - u))))
    return fr

def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255, rot=0, stroke=True):
    if size < 4: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(LZ, size)
    if stroke: d.text((x, y), s, font=f, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), anchor="mm", direction="rtl", language="ar")
    d.text((x, y), s, font=f, fill=fill + (alpha,), anchor="mm", direction="rtl", language="ar")
    if rot: lay = lay.rotate(rot, center=(x, y), resample=Image.BICUBIC)
    img.paste(lay, (0, 0), lay)

def sub_chunk(img, tt, cx, cy, size, maxw=None):
    k, lt = line_at(tt)
    if not k or k not in CHUNKS: return
    cur = None
    for off, txt, key in CHUNKS[k]:
        if lt >= off: cur = (off, txt, key)
    if cur is None: return
    off, txt, key = cur; sc = popk(lt, off, 0.15) if lt - off < 0.15 else 1
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    sz = size
    if maxw:
        while sz > 30 and d.textlength(txt, font=ImageFont.truetype(LZ, sz), direction="rtl", language="ar") > maxw: sz -= 4
    f = ImageFont.truetype(LZ, max(6, int(sz * sc)))
    kw = dict(font=f, direction="rtl", language="ar", stroke_width=max(4, sz // 10), stroke_fill=(10, 10, 10, 255))
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
    """growth rule 30: ONE ask only"""
    k = kk(tt, sh["start"], sh["start"] + 0.4)
    fr = ImageEnhance.Brightness(fr).enhance(1 - 0.55 * k).filter(ImageFilter.GaussianBlur(6 * k))
    sc = popk(tt, sh["start"] + 0.1, 0.3); vert = Hd > Wd
    if sc > 0:
        lzt(fr, Wd / 2, Hd * (0.33 if vert else 0.3), "تابع بندق وعزيزة…", int((112 if vert else 110) * sc), (255, 214, 90))
        lzt(fr, Wd / 2, Hd * (0.33 if vert else 0.3) + (130 if vert else 120), "الحلقة الجاية فيها الحماة!", int(84 * sc), (255, 255, 255))
    if tt >= sh["start"] + 0.5:
        logo(fr, Wd / 2, Hd * (0.56 if vert else 0.68), 130); text(fr, Wd / 2, Hd * (0.56 if vert else 0.68) + 140, "@shattawzalata", 52, (255, 214, 90))
    return fr

_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/daily/18")

def subtitle(img, tt): sub_chunk(img, tt, W / 2, H - 85, 64)

HOOK = "فاكر النهارده إيه؟!"
_FREEZE = {}
def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "end":
        if "h" not in _FREEZE: _FREEZE["h"] = scene(sh["start"] - 0.05, cam_at(shots[-2], sh["start"] - 0.05), (W, H))
        return finish(endcard(_FREEZE["h"].copy(), tt, sh, W, H), tt)
    fr = scene(tt, cam_at(sh, tt), (W, H))
    if tt < 3.0:
        a_ = int(255 * min(1, (3.0 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([W / 2 - 480, 40, W / 2 + 480, 150], 30, fill=(20, 12, 8, int(a_ * 0.8)))
        lzt(fr, W / 2, 95, HOOK, int(76 * popk(tt, 0.0, 0.25)) or 76, (255, 214, 90), alpha=a_)
    return finish(fr, tt)

VIGV = VIG.resize((1080, 1920))
def vertical(_base, tt):
    sh = shot_at(tt)
    if sh["set"] == "end":
        if "v" not in _FREEZE: _FREEZE["v"] = scene(sh["start"] - 0.05, vcam(shots[-2], sh["start"] - 0.05), (1080, 1920))
        return endcard(_FREEZE["v"].copy(), tt, sh, 1080, 1920)
    fr = scene(tt, vcam(sh, tt), (1080, 1920))
    fr = ImageChops.multiply(fr, VIGV)
    if tt < 3.0:
        a_ = int(255 * min(1, (3.0 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([110, 240, 970, 440], 40, fill=(20, 12, 8, int(a_ * 0.75)))
        lzt(fr, 540, 340, HOOK, int(100 * popk(tt, 0.0, 0.25)) or 100, (255, 214, 90), alpha=a_)
    sub_chunk(fr, tt, 520, 1420, 76, maxw=940)
    return fr

def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def buzzer(dur=0.42, amp=0.13):
    d_ = np.arange(int(SR * dur)) / SR; w = np.sign(np.sin(2 * np.pi * 110 * d_)) + 0.5 * np.sign(np.sin(2 * np.pi * 116 * d_))
    return lowpass((w * amp * np.minimum(1, (dur - d_) * 12)).astype(np.float32), 2200)
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(18)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 300) * 0.015, 0, 1.0)
    mix_into(buf, tone(196, 0.5, 0.12, 4) + tone(147, 0.5, 0.1, 4), 0.02, 1.0)                                  # frame-1 «dun»
    for i in range(6): mix_into(buf, tone(1200 if i % 2 else 900, 0.05, 0.05, 40), T("AZ1") + 2.0 + i * 0.32, 1.0)  # tense tick-tock
    for i, xt in enumerate(XS): mix_into(buf, buzzer(0.42 + 0.08 * i, 0.12 + 0.03 * i), xt + 0.02, 1.0)        # ✗ buzzer, louder each time
    for g in (GUESS1 - 0.1, GUESS2 - 0.05, GUESS3 + 0.1): mix_into(buf, tone(1320, 0.18, 0.08, 10) + tone(1760, 0.18, 0.05, 10), g, 1.0)  # bubble «ding»
    mix_into(buf, SFXF["whoosh"] * 0.25, SLIP - 0.1, 1.0)                                                      # slipper out
    mix_into(buf, tone(160, 0.9, 0.1, 2.5) + tone(120, 0.9, 0.08, 2.5), MAMA, 1.0)                             # sad low note on «ماما»
    for k_, f in enumerate((523, 659, 784, 1047)): mix_into(buf, tone(f, 0.35, 0.12, 5), JOY + k_ * 0.07, 1.0)  # party fanfare
    mix_into(buf, lowpass(r.normal(0, 1, int(SR * 0.3)).astype(np.float32), 4000) * 0.12 * np.linspace(1, 0, int(SR * 0.3)), JOY, 1.0)  # popper
    mix_into(buf, tone(140, 0.8, 0.3, 2.5), SHOCK, 1.0); mix_into(buf, tone(95, 0.8, 0.25, 2.5), SHOCK + 0.03, 1.0)   # «DUN»
    mix_into(buf, tone(700, 0.6, 0.08, 1) * np.linspace(1, 0.2, int(SR * 0.6)).astype(np.float32), SHOCK + 0.05, 1.0)  # record-scratch-ish stop
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), TOTAL - 2.5 + k_ * 0.09, 1.0)
    rms = lambda x: float(np.sqrt(np.mean(x ** 2))) + 1e-9; ref = []
    for st, k in lines:
        if k == "GROUP": continue
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8
        ref.append(rms(v)); mix_into(buf, v, st, 1.0)
    g = AUD["GROUP"][:int(SR * LU)].copy(); g[-int(SR * 0.4):] *= np.linspace(1, 0, int(SR * 0.4))
    mix_into(buf, g / rms(g) * float(np.mean(ref)) * 1.2, LAUGH, 1.0)
    write_wav(buf[:int(TOTAL * SR)], path)

def make_covers():
    """growth rules: BIG sweaty Bandaq face + Aziza with the slipper (story object), 3-word question, series badge"""
    def comp(Wd, Hd, vert):
        bgc = ROOM.crop((400, 100, 1500, 1000)).resize((Wd, Hd), Image.LANCZOS).filter(ImageFilter.GaussianBlur(6))
        img = ImageEnhance.Brightness(bgc).enhance(0.8).resize((int(Wd * SS), int(Hd * SS)))
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); p = P(lay)
        if vert:
            draw_char(p, "aziza", Wd * 0.22, Hd * 0.58, 2.5, "angry", 0.4, 1, False, "raise", 0.0, "slipper", 0.15, None)
            draw_char(p, "bondo2", Wd * 0.6, Hd * 0.95, 5.0, "scared", 0.5, -1, False, "scared", 0.0, None, -0.05, None)
        else:
            draw_char(p, "aziza", Wd * 0.22, Hd * 1.0, 3.3, "angry", 0.4, 1, False, "raise", 0.0, "slipper", 0.15, None)
            draw_char(p, "bondo2", Wd * 0.62, Hd * 1.38, 4.8, "scared", 0.5, -1, False, "scared", 0.0, None, -0.05, None)
        img.paste(lay, (0, 0), lay); fr = img.resize((Wd, Hd), Image.LANCZOS); d = ImageDraw.Draw(fr, "RGBA")
        # sweat drops on the big face
        cx, cy, R = (Wd * 0.59, Hd * 0.455, Wd * 0.026) if vert else (Wd * 0.617, Hd * 0.53, Wd * 0.016)
        for dx, dy in ((-3.2, 0), (3.4, 0.6), (-2.6, 2.2)):
            x, y = cx + dx * R * 1.8, cy + dy * R * 1.8
            d.ellipse([x - R, y - R * 1.5, x + R, y + R * 1.5], fill=(190, 225, 255, 240), outline=(60, 110, 170, 255), width=4)
        if vert:
            d.rectangle([0, Hd * 0.69, Wd, Hd * 0.88], fill=(10, 6, 4, 150))
            lzt(fr, Wd / 2, Hd * 0.74, "فاكر النهارده", 140, (255, 255, 255)); lzt(fr, Wd / 2, Hd * 0.83, "إيه؟!", 190, (255, 214, 60))
            bx, by = Wd / 2, 130
        else:
            d.rectangle([0, Hd * 0.76, Wd, Hd * 0.97], fill=(10, 6, 4, 150)); lzt(fr, Wd * 0.5, Hd * 0.865, "فاكر النهارده إيه؟!", 150, (255, 214, 60)); bx, by = 1600, 90
        d.rounded_rectangle([bx - 175, by - 40, bx + 175, by + 40], 30, fill=(200, 30, 40, 240))
        lzt(fr, bx, by, "يوميات شطة وزلطة", 40, (255, 255, 255), stroke=False)
        return fr
    comp(1080, 1920, True).save(ROOT + "/publish/thumbs/daily_e18_cover.jpg", quality=92)
    comp(1920, 1080, False).resize((1280, 720), Image.LANCZOS).save(ROOT + "/publish/thumbs/daily_e18_yt.jpg", quality=92)

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
