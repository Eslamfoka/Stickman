# «يوميات شطة وزلطة» — خدمة الغرف  (H 1920x1080 + V 1080x1920 in one pass) — user script 2026-11-16 22:03
# Aziza fights the hotel window (wants to jump), Bandaq calmly calls room service, Shatta = the polite receptionist.
# Ending (user 22:11): close on SHATTA'S REACTION, then the audience laugh (sound only) over it.
# NEW canonical locations: «أوضة الفندق» daily/bg/hotel_room.png · «ريسبشن الفندق» daily/bg/hotel_desk.png (desk + phone drawn in code).
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/daily/14")
SERIES = "يوميات شطة وزلطة"; EPT = "خدمة الغرف"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"
SFXF = {"whoosh": load_audio(ROOT + "/trend/01/sfx/whoosh.mp3")}

SUB = {"AZ0": "سيبني... أنا هنطّ!", "B1": "ألو... دي خدمة الغرف؟", "S1": "أيوه يا عم بندق... أساعدك إزاي؟",
       "B2": "أنا اتخانقت مع عزيزة مراتي... وهي بتحاول تنطّ من الشبّاك!", "S2": "آسف يا عم بندق... بس دي مشكلة شخصية.",
       "B3": "الشبّاك مش عايز يتفتح... ودي مشكلتك إنت!", "GROUP": ""}
REC = "shattarec"; CH[REC] = dict(CH["shatta"]); CH[REC].update(shirt=(128, 24, 36)); BASE[REC] = "shatta"     # receptionist: maroon hotel vest
WHO = {"AZ0": "aziza", "B1": "bondo2", "S1": REC, "B2": "bondo2", "S2": REC, "B3": "bondo2", "GROUP": "-"}
EXPR = {"AZ0": "shout", "B1": "flat", "S1": "happy", "B2": "flat", "S2": "sad", "B3": "flat", "GROUP": "laugh"}
load_lines(list(SUB))
ROOM = _ld(ROOT + "/daily/bg/hotel_room.png")
DESKBG = _ld(ROOT + "/daily/bg/hotel_desk.png")

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
WIDE = (960, 560, 1.12)
t = say(0.1, "AZ0"); shakes.append((0.12, 12))
shot("room", 0.0, 1.05, (1365, 560, 2.0), (1365, 570, 2.15))                          # her back: yanking the stuck window
shot("room", 1.05, t + 0.1, (1330, 580, 2.4), (1330, 570, 2.7), tin="whip", ease="crash")   # she turns: «أنا هنطّ!»
t += 0.1
DIAL = t; shot("room", t, t + 1.5, WIDE, (900, 580, 1.25), tin="whipl")              # wide: Bandaq, calm on the bed, dials
t += 1.5
RING = t; shot("desk", t, t + 1.0, (1000, 640, 1.7), (1000, 630, 1.85))              # reception: the phone rings → Shatta picks up
PICK = t + 0.55; t += 1.0
s = t; t = say(t + 0.05, "B1") + 0.1; shot("room", s, t, (620, 470, 2.3), (620, 465, 2.45), tin="whipl")
s = t; t = say(t + 0.05, "S1") + 0.1; shot("desk", s, t, (1000, 640, 2.3), (1000, 635, 2.45), tin="whip")
s = t; b2 = say(t + 0.05, "B2"); B2 = T("B2")
shot("room", s, B2 + 2.3, (620, 470, 2.3), (640, 465, 2.4), tin="whipl")
shot("room", B2 + 2.3, b2 + 0.15, (1365, 560, 2.0), (1365, 550, 2.25), tin="whip")     # «وهي بتحاول تنطّ…» → her, leg up on the sill
t = b2 + 0.15
s = t; t = say(t + 0.05, "S2") + 0.1; shot("desk", s, t, (1000, 640, 2.3), (1000, 632, 2.5), tin="whip")
s = t; t = say(t + 0.05, "B3") + 0.1; B3 = T("B3")
shot("room", s, B3 + 1.75, (620, 470, 2.3), (620, 465, 2.5), tin="whipl")
shot("room", B3 + 1.75, t, (620, 470, 2.7), (620, 466, 2.95), ease="crash")            # «ودي مشكلتك إنت!» crash-in
REACT = t; shot("desk", t, t + 1.1, (1000, 640, 2.3), (1000, 615, 2.65), tin="whip", ease="crash")   # Shatta's reaction (user: end on it)
LAUGH = t + 0.9; say(LAUGH, "GROUP"); LU = min(3.0, DUR["GROUP"])
shot("desk", t + 1.1, LAUGH + LU, (1000, 615, 2.65), (1000, 612, 2.75))               # ...and the laugh plays over his face
t = LAUGH + LU; FREEZE = t - 0.2
shot("end", t, t + 2.4, None); t += 2.4
TOTAL = t

# ---------------- staging ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
BD = (560, 700, 2.0)            # Bandaq seated on the right edge of the bed (hip on the mattress), legs to the right
AZ = (1365, 900, 1.9)           # Aziza at the window (feet)
SH = (1000, 1000, 2.2)          # Shatta behind the reception desk (feet hidden)
PHONE_ROOM = (832, 528)         # the beige rotary phone on the nightstand (in the picture)
DESK = (600, 1400, 820)         # reception desk x0, x1, top y
PHONE_DESK = (1250, 812)

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, held=None, sit=0, nod=0.0):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    blink = ((tt + len(who) * 0.37) % 3.6) < 0.11 and expr not in ("laugh", "shock", "gasp")
    if not talking: lean += math.sin(tt * 1.7 + len(who)) * 0.04
    X, Y_ = W2S(cam, x, y); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, held, lean, None, sit=sit, nod=nod)

def head_of(who, x, y, s, sit=0):
    S = s * CH[who]["scale"]
    if sit: y = y + 62 * S
    sh = y - 134 * S; return S, sh, (x, sh - 56 * S)

def handset(p, cam, hx, hy, S, z, cord_to=None, tt=0.0, ang=-0.45):
    """old phone handset held against the ear (tilted) + curly cord back to the base"""
    c, sn = math.cos(ang), math.sin(ang); k = S * z
    R = lambda dx, dy: (hx + (dx * c - dy * sn) * k, hy + (dx * sn + dy * c) * k)
    p.poly([R(-7, -34), R(7, -34), R(7, 34), R(-7, 34)], (40, 36, 34, 255), INK, 2 * z)
    for e in (-34, 34):
        q = R(-6, e); p.ell(q[0], q[1], 12 * k, 9 * k, (40, 36, 34, 255), INK, 2 * z)
    if cord_to:
        bx, by = cord_to; n = 30; pts = []; sx, sy = R(-6, 38)
        for i in range(n + 1):
            u = i / n; x_ = lerp(sx, bx, u); y_ = lerp(sy, by, u) + math.sin(u * math.pi) * 70 * z
            pts.append((x_ + math.sin(u * 70) * 5 * z, y_ + math.cos(u * 70) * 5 * z))
        p.line(pts, (40, 36, 34, 255), 2.2 * z)

def desk(p, cam, tt):
    z = cam[2]; x0, x1, ty = DESK
    a = W2S(cam, x0 - 20, ty - 22); b = W2S(cam, x1 + 20, ty); p.rect(a[0], a[1], b[0], b[1], (130, 82, 44, 255), INK, 3 * z, 3 * z)
    a = W2S(cam, x0, ty); b = W2S(cam, x1, 1100); p.rect(a[0], a[1], b[0], b[1], (96, 58, 30, 255), INK, 3 * z, 2 * z)
    for xx in range(x0 + 40, x1 - 40, 190):
        a = W2S(cam, xx, ty + 40); b = W2S(cam, xx + 150, 1060); p.rect(a[0], a[1], b[0], b[1], (82, 48, 24, 255), INK, 2 * z, 3 * z)
    a = W2S(cam, 700, ty - 22); p.rect(a[0], a[1] - 14 * z, a[0] + 150 * z, a[1], (230, 226, 210, 255), INK, 2 * z, 2 * z)   # register book
    a = W2S(cam, 880, ty - 22); p.ell(a[0], a[1] - 10 * z, 22 * z, 12 * z, (220, 180, 70, 255), INK, 2 * z)               # brass bell
    p.ell(a[0], a[1] - 22 * z, 5 * z, 5 * z, (220, 180, 70, 255), INK, 1.5 * z)

def desk_phone(p, cam, tt, on_cradle):
    z = cam[2]; x, y = PHONE_DESK; jig = math.sin(tt * 70) * 3 if RING <= tt < PICK else 0
    a = W2S(cam, x - 60 + jig, y - 40); b = W2S(cam, x + 60 + jig, y); p.rect(a[0], a[1], b[0], b[1], (150, 30, 36, 255), INK, 2.5 * z, 10 * z)
    q = W2S(cam, x + jig, y - 22); p.ell(q[0], q[1], 22 * z, 14 * z, (230, 220, 200, 255), INK, 2 * z)
    if on_cradle:
        a = W2S(cam, x - 70 + jig, y - 64); b = W2S(cam, x + 70 + jig, y - 40); p.rect(a[0], a[1], b[0], b[1], (40, 36, 34, 255), INK, 2 * z, 10 * z)
    return W2S(cam, x, y - 30)

def ring_marks(fr, cam, tt):
    if not (RING <= tt < PICK): return
    z = cam[2]; q = W2S(cam, *PHONE_DESK); d = ImageDraw.Draw(fr, "RGBA")
    for i in range(3):
        r = (30 + i * 22) * z * (0.8 + 0.2 * math.sin(tt * 30))
        d.arc([q[0] - r, q[1] - 40 * z - r, q[0] + r, q[1] - 40 * z + r], 200, 340, fill=(255, 230, 120, 230), width=int(4 * z))

def window_rattle(cam, tt):
    """the stuck window shakes while she yanks it (only the shot camera moves a little)"""
    return 0

def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255):
    if size < 4: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(LZ, size)
    d.text((x, y), s, font=f, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), anchor="mm", direction="rtl", language="ar")
    d.text((x, y), s, font=f, fill=fill + (alpha,), anchor="mm", direction="rtl", language="ar")
    img.paste(lay, (0, 0), lay)
def popk(tt, t0, d=0.22):
    u = kk(tt, t0, t0 + d); return 0 if u <= 0 else (1 + 0.25 * math.sin(u * math.pi)) if u < 1 else 1

def sweat(fr, cam, who, x, y, s, tt, t0):
    if tt < t0: return
    z = cam[2]; d = ImageDraw.Draw(fr, "RGBA"); S, sh, (hx, hy) = head_of(who, x, y, s)
    for i, (dx, ph) in enumerate(((-40, 0.0), (38, 0.5))):
        u = (tt * 0.8 + ph) % 1.0; q = W2S(cam, hx + dx * S, hy - 22 * S + u * 46 * S); r = 5 * S * z
        d.ellipse([q[0] - r, q[1] - r * 1.5, q[0] + r, q[1] + r * 1.5], fill=(190, 225, 255, int(230 * (1 - u))), outline=(60, 110, 170, int(255 * (1 - u))), width=2)

_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/daily/14")
_FC = {}
def frame_cache(t_):
    if t_ not in _FC: _FC[t_] = frame(t_)
    return _FC[t_]
def endcard(tt, sh):
    k = kk(tt, sh["start"], sh["start"] + 0.4)
    fr = ImageEnhance.Brightness(frame_cache(FREEZE)).enhance(1 - 0.55 * k).filter(ImageFilter.GaussianBlur(6 * k)).convert("RGBA")
    sc = popk(tt, sh["start"] + 0.1, 0.3)
    if sc > 0: lzt(fr, W / 2, 400, "منشن صاحبك اللي شغال خدمة عملاء!", int(92 * sc), (255, 214, 90))
    if tt >= sh["start"] + 0.5:
        logo(fr, W / 2, 680, 130); text(fr, W / 2, 830, "@shattawzalata", 52, (255, 214, 90))
    return fr.convert("RGB")

# ---------------- frames ----------------
def room_frame(tt, sh):
    cam = cam_at(sh, tt); z = cam[2]
    img = bg_crop(ROOM, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    # ---- Bandaq on the bed: receiver at the ear from the dial on; calm
    on_phone = tt >= DIAL + 0.45
    bex = "flat"
    if tt < DIAL: bex = "sleepy"
    barms = "phonesal" if on_phone else ("point" if DIAL <= tt < DIAL + 0.45 else "down")
    person(lay, cam, "bondo2", *BD, tt, bex, 0 if tt < B3 else 1, barms, 0.0, None, sit=1)
    S, shy, (hx, hy) = head_of("bondo2", *BD, sit=1)
    if on_phone:
        q = W2S(cam, hx + 44 * S, hy + 4 * S); pb = W2S(cam, *PHONE_ROOM)
        handset(p, cam, q[0], q[1], S, z, pb, tt)
    # ---- Aziza at the window: back view yanking, front view shouting on «أنا هنطّ», leg up on the sill on «بتحاول تنطّ»
    ax, ay, as_ = AZ
    yank = math.sin(tt * 26) * 7
    front = 1.05 <= tt < DIAL
    if front:
        person(lay, cam, "aziza", ax, ay, as_, tt, "shout", -1, "up", 0.0)
    else:
        X, Y_ = W2S(cam, ax + yank, ay - (34 * abs(math.sin(tt * 9)) if tt >= B2 + 2.3 else 0)); draw_back(P(lay), "aziza", X, Y_, as_ * z, tt, None, "up")
    lay = tint_layer(lay, (255, 226, 180)); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    if not front and tt < DIAL + 1.5 or (B2 + 2.3 <= tt < T("S2")):                              # rattle lines on the window frame
        d = ImageDraw.Draw(fr, "RGBA")
        for side in (-1, 1):
            q = W2S(cam, ax + side * 230, 500)
            for i in range(3):
                o = (i * 14 + 10) * z * (0.7 + 0.3 * math.sin(tt * 40 + i))
                d.line([(q[0] + side * o, q[1] - 30 * z), (q[0] + side * o, q[1] + 30 * z)], fill=(255, 255, 255, 170), width=int(3 * z))
    return fr

def desk_frame(tt, sh):
    cam = cam_at(sh, tt); z = cam[2]
    img = bg_crop(DESKBG, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    picked = tt >= PICK
    sex = "sleepy" if tt < PICK else "happy"
    if tt >= REACT: sex = "shock"
    sarms = "phonesal" if picked else "down"
    person(lay, cam, REC, *SH, tt, sex, 0, sarms, 0.0)
    S, shy, (hx, hy) = head_of(REC, *SH)
    q = W2S(cam, SH[0], shy + 4 * S); bw = 16 * S * z                                                  # bow tie
    p.poly([(q[0], q[1]), (q[0] - bw, q[1] - bw * 0.6), (q[0] - bw, q[1] + bw * 0.6)], (20, 20, 24, 255), INK, 1.5 * z)
    p.poly([(q[0], q[1]), (q[0] + bw, q[1] - bw * 0.6), (q[0] + bw, q[1] + bw * 0.6)], (20, 20, 24, 255), INK, 1.5 * z)
    desk(p, cam, tt)
    base = desk_phone(p, cam, tt, not picked)
    if picked:
        q = W2S(cam, hx + 44 * S, hy + 4 * S); handset(p, cam, q[0], q[1], S, z, base, tt)
    a = W2S(cam, SH[0] - 120, DESK[2] - 300)
    lay = tint_layer(lay, (255, 226, 180)); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    ring_marks(fr, cam, tt)
    if tt >= REACT + 0.3: sweat(fr, cam, REC, *SH, tt, REACT + 0.3)
    return fr

def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "end": return finish(endcard(tt, sh), tt)
    fr = room_frame(tt, sh) if sh["set"] == "room" else desk_frame(tt, sh)
    if tt < 3.0:
        a_ = int(255 * min(1, (3.0 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([W / 2 - 760, 40, W / 2 + 760, 150], 30, fill=(20, 12, 8, int(a_ * 0.8)))
        lzt(fr, W / 2, 95, "مراته عايزة تنطّ من الشبّاك… وهو بيكلم خدمة الغرف؟!", 66, (255, 214, 90), alpha=a_)
    return finish(fr, tt)

def vertical(fr, tt):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = ImageEnhance.Brightness(small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.35)
    bgv.paste(fr.resize((1080, 608), Image.LANCZOS), (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(255, 214, 90)); d.rectangle([0, 1168, 1080, 1171], fill=(255, 214, 90))
    lzt(bgv, 540, 250, "مراته عايزة تنطّ", 104, (255, 255, 255))
    lzt(bgv, 540, 395, "وهو بيكلم خدمة الغرف!", 96, (255, 214, 90))
    lzt(bgv, 540, 1840, SERIES, 44, (255, 150, 110))
    k, _ = line_at(tt)
    if k and SUB.get(k):
        for i, l in enumerate(wrap(SUB[k])[:4]): text(bgv, 540, 1290 + i * 80, l, 60, sw=6)
    return bgv

def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(49)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 300) * 0.02, 0, 1.0)                   # room tone + far city
    for j in range(int((DIAL + 1.5) / 0.09)):                                                             # window rattling while she yanks
        if 0.05 + j * 0.09 < DIAL + 1.5: mix_into(buf, lowpass(r.normal(0, 1, int(SR * 0.04)).astype(np.float32), 1800) * 0.12, 0.05 + j * 0.09, 1.0)
    for j in range(int((T("S2") - B2 - 2.3) / 0.1)): mix_into(buf, lowpass(r.normal(0, 1, int(SR * 0.04)).astype(np.float32), 1800) * 0.08, B2 + 2.3 + j * 0.1, 1.0)
    for j in range(6): mix_into(buf, tone(1500, 0.03, 0.12, 60), DIAL + 0.5 + j * 0.13, 1.0)              # rotary dial clicks
    for j in range(2): mix_into(buf, tone(440, 0.4, 0.12, 2) + tone(480, 0.4, 0.12, 2), DIAL + 1.25 + j * 0.0, 1.0)   # ringback (J-cut)
    for j in range(8): mix_into(buf, tone(1200 + (j % 2) * 150, 0.05, 0.16, 20), RING + j * 0.06, 1.0)      # desk phone bell
    mix_into(buf, tone(300, 0.08, 0.2, 30), PICK, 1.0)                                                     # pick-up click
    mix_into(buf, tone(160, 0.5, 0.25, 5) + tone(110, 0.5, 0.25, 5), REACT, 1.0)                          # reaction «dun»
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 0.5: mix_into(buf, SFXF["whoosh"] * 0.22, s_["start"] - 0.1, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), TOTAL - 2.3 + k_ * 0.09, 1.0)
    rms = lambda x: float(np.sqrt(np.mean(x ** 2))) + 1e-9; ref = []
    for st, k in lines:
        if k == "GROUP": continue
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8
        if WHO[k] == REC or (WHO[k] == "bondo2" and False): pass
        ref.append(rms(v)); mix_into(buf, v, st, 1.0)
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
