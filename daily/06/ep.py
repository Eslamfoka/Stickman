# «يوميات شطة وزلطة» — آخر يوم  (H 1920x1080 + V 1080x1920 in one pass)
# render:  python ep.py audio  →  python ep.py part 0 2 & python ep.py part 1 2  →  concat  →  mux mix.wav
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/daily/06")
SERIES = "يوميات شطة وزلطة"; EPT = "آخر يوم"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"
SFXP = {"whoosh": "/trend/01/sfx/whoosh.mp3", "slipper": "/s2e1/sfx/slipper.mp3", "steps": "/s2e1/sfx/footsteps.mp3"}
SFXF = {n: load_audio(ROOT + p) for n, p in SFXP.items()}

SUB = {"B0": "هـــه...", "S1": "مالك يا عم البواب؟ زعلان ليه؟", "B1": "أصل أنا اتخانقت أنا وخالتك عزيزة...",
       "A1": "مش هتكلم معاك... أسبوعين! هِمّ!", "S2": "طب ودي حاجة حلوة! أسبوعين راحة من غير خناق!",
       "B2": "أنا زعلان... عشان النهارده آخر يوم!", "GROUP": ""}
WHO = {"B0": "bondo2", "S1": "shatta", "B1": "bondo2", "A1": "aziza", "S2": "shatta", "B2": "bondo2", "GROUP": "-"}
EXPR = {"B0": "sad", "S1": "neutral", "B1": "sad", "A1": "angry", "S2": "happy", "B2": "sad", "GROUP": "laugh"}
load_lines(list(SUB))
LOBBY = _ld(ROOT + "/s1e10/bg/morning.png")        # canonical «مدخل العمارة» (docs/locations.md)

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear()
t = say(0.35, "B0") + 0.2
shot("lobby", 0.0, t, (660, 700, 2.3), (660, 720, 2.05))                                # hook: the saddest doorman in Cairo
ENTER = (t + 0.1, t + 1.7); WHISTLE = (t - 0.3, t + 1.4)
shot("lobby", t, t + 2.0, (1060, 690, 1.18), (1000, 700, 1.25), tin="whip"); t += 2.0   # Shatta comes down, whistling… stops
s = t; t = say(t + 0.05, "S1") + 0.15; shot("lobby", s, t, (880, 740, 1.5), (880, 740, 1.58))
s = t; t = say(t + 0.05, "B1") + 0.2; shot("lobby", s, t, (800, 730, 1.7), (790, 725, 1.85), tin="whipl")
BUB = t; s = t; t = say(t + 0.45, "A1") + 0.35; BUBEND = t                              # flashback bubble over his head
shot("lobby", s, t, (720, 560, 1.55), (720, 560, 1.62))
s = t; t = say(t + 0.05, "S2") + 0.2; CLAP = s; shot("lobby", s, t, (900, 740, 1.5), (900, 740, 1.6), tin="whip")
s = t; t = say(t + 0.1, "B2") + 0.2; CRY = s
shot("lobby", s, s + 1.6, (680, 720, 2.1), (680, 720, 2.3), tin="whipl")
shot("lobby", s + 1.6, t, (680, 720, 2.6), (680, 710, 2.8))                             # «…آخر يوم!» — the fountain
LAUGH = t; LU = DUR["GROUP"]; say(LAUGH, "GROUP")
shot("lobby", t, t + 2.4, (1080, 700, 2.0), (1080, 710, 1.75), tin="whip")             # Shatta explodes
shot("lobby", t + 2.4, t + LU + 0.2, (880, 720, 1.45), (880, 720, 1.35))
t += LU + 0.2; FREEZE = t - 0.25
shot("end", t, t + 2.6, None); t += 2.6
TOTAL = t

# ---------------- staging (world = 1920x1080 lobby) ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
SEAT_Y, BX, BS = 905, 640, 1.9                     # the dikka (bench) and Bandaq sitting on it
SX0, SX1, SY, SS = 2080, 1120, 1040, 1.75          # Shatta: from the stairs → stops by the bench

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, walk=None, hop=0.0):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    if talking and arms == "down": arms = "talk"
    blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11 and expr not in ("sleepy", "laugh")
    X, Y_ = W2S(cam, x, y - hop); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, None, lean, walk)
    return X, Y_, S * CH[who]["scale"]

WOOD = (150, 98, 52, 255); WOOD_D = (110, 68, 34, 255)
def bench_front(p, cam):
    """the dikka's seat plank + legs, drawn OVER the sitter so he really sits on it"""
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

def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255, font=None):
    if size < 4: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(font or LZ, size)
    kw = dict(font=f, anchor="mm", direction="rtl", language="ar")
    d.text((x, y), s, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), **kw)
    d.text((x, y), s, fill=fill + (alpha,), **kw); img.paste(lay, (0, 0), lay)
def popk(tt, t0, d=0.22):
    u = kk(tt, t0, t0 + d); return 0 if u <= 0 else (1 + 0.25 * math.sin(u * math.pi)) if u < 1 else 1
def series_tag(fr, tt, t0, t1):
    k = min(ease(kk(tt, t0, t0 + 0.35)), 1 - ease(kk(tt, t1 - 0.35, t1)))
    if k <= 0: return
    d = ImageDraw.Draw(fr, "RGBA"); x = -620 + 680 * k
    d.rounded_rectangle([x, 60, x + 620, 170], 26, fill=(230, 120, 30, 235), outline=(255, 255, 255, 255), width=4)
    lzt(fr, x + 310, 108, "يوميات شطة وزلطة", 60, (255, 255, 255))

_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/daily/06")
_FC = {}
def frame_cache(t_):
    if t_ not in _FC: _FC[t_] = frame(t_)
    return _FC[t_]
def endcard(tt, sh):
    k = kk(tt, sh["start"], sh["start"] + 0.4)
    fr = ImageEnhance.Brightness(frame_cache(FREEZE)).enhance(1 - 0.55 * k).filter(ImageFilter.GaussianBlur(6 * k)).convert("RGBA")
    sc = popk(tt, sh["start"] + 0.1, 0.3)
    if sc > 0:
        lzt(fr, W / 2, 420, "يوميات شطة وزلطة", int(140 * sc), (255, 214, 90))
        d = ImageDraw.Draw(fr, "RGBA"); d.rounded_rectangle([W / 2 - 400, 520, W / 2 + 400, 600], 30, fill=(230, 120, 30, 230))
        lzt(fr, W / 2, 558, "موقف جديد كل يوم!", 54, (255, 255, 255))
    if tt >= sh["start"] + 0.6:
        logo(fr, W / 2, 760, 120); text(fr, W / 2, 900, "@shattawzalata", 50, (255, 214, 90))
    return fr.convert("RGB")

def bubble(fr, cam, tt):
    """sepia thought bubble over Bandaq: Aziza, arms crossed, turns her face away — «هِمّ!»"""
    k = ease(kk(tt, BUB, BUB + 0.3)) * (1 - ease(kk(tt, BUBEND - 0.25, BUBEND)))
    if k <= 0: return fr
    z = cam[2]; cx, cy = W2S(cam, 1000, 480); R = 215 * z * k
    hx, hy = W2S(cam, BX, SEAT_Y - 330)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    for i, (f, r) in enumerate(((0.25, 16), (0.5, 26))):     # the little trail of circles
        p.ell(hx + (cx - hx) * f + 30 * z, hy + (cy - hy) * f, r * z * k, r * z * k, (246, 232, 200, 255), INK, 3 * z)
    p.ell(cx, cy, R * 1.25, R, (246, 232, 200, 255), INK, 4 * z)
    if k > 0.6:
        turned = tt >= T("A1") + DUR["A1"] * 0.72
        X, Y_ = cx, cy + R * 0.86; S = 1.35 * z
        k_, lt = line_at(tt); talking = k_ == "A1"
        mouth = float(ENV["A1"][min(int(lt * FPS) + 2, len(ENV["A1"]) - 1)]) if talking else 0.0
        if turned:
            draw_back(p, "aziza", X, Y_, S, tt, None, "down")
        else:
            draw_char(p, "aziza", X, Y_, S, "angry", mouth, 1, False, "clap", tt)
            p.line([(X - 40 * S, Y_ - 120 * S), (X + 40 * S, Y_ - 104 * S)], INK, 6 * S)      # crossed forearms
            p.line([(X + 40 * S, Y_ - 120 * S), (X - 40 * S, Y_ - 104 * S)], INK, 6 * S)
    lay = lay.resize((W, H), Image.LANCZOS)
    a = np.asarray(lay).astype(np.float32); g = a[..., :3].mean(axis=2, keepdims=True)
    a[..., :3] = np.clip(g * np.array([1.08, 0.95, 0.75]) + np.array([18, 8, -6]), 0, 255)  # sepia = a memory
    lay = Image.fromarray(a.astype(np.uint8), "RGBA")
    fr = fr.convert("RGBA"); fr.alpha_composite(lay); fr = fr.convert("RGB")
    if tt >= T("A1") + DUR["A1"] * 0.72: lzt(fr, cx + 210 * z, cy - 120 * z, "هِمّ!", int(80 * popk(tt, T("A1") + DUR["A1"] * 0.72)), (255, 120, 120))
    return fr

# ---------------- frame ----------------
def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "end": return finish(endcard(tt, sh), tt)
    cam = cam_at(sh, tt); z = cam[2]
    img = bg_crop(LOBBY, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    laughing = tt >= LAUGH; lu = tt - LAUGH
    bench_back(p, cam)
    # Bandaq sits, chin in his hand
    bex = "sad"; blook = 0; barms = "shush"; blean = 0.25
    if tt >= ENTER[1] - 0.3: blook = 1
    if T("S1") <= tt: barms = "down"; blean = 0.1
    if CLAP <= tt < CRY: bex = "sad"; blook = 1
    if tt >= CRY: bex = "sad"; blook = 0; barms = "scared" if tt >= CRY + 1.4 else "down"
    sag = 6 * math.sin(tt * 1.3) if tt < ENTER[0] else 0
    BXs, BYs, BSs = person(lay, cam, "bondo2", BX, SEAT_Y + 62 * BS + sag, BS, tt, bex, blook, barms, blean)
    bench_front(p, cam); shins(p, cam, BX, BS, 4 * math.sin(tt * 2) if tt >= CRY else 0)
    if tt >= CRY + 1.4:                                    # the tear fountain
        hx, hy = BXs, BYs - 190 * BSs
        for sd in (-1, 1):
            for k_ in range(9):
                u = 0.1 + 0.9 * ((tt * 1.8 + k_ / 9) % 1); ex_ = hx + sd * 15 * BSs; ey_ = hy + 2 * BSs
                px = ex_ + sd * u * 150 * BSs; py = ey_ - 70 * BSs * math.sin(u * math.pi) + u * u * 120 * BSs
                p.ell(px, py, 6 * BSs, 8 * BSs, (120, 190, 255, int(255 * (1 - u * 0.6))), INK, 1.2 * BSs)
    elif T("B1") <= tt < CRY:                             # a single tear
        u = ((tt - T("B1")) * 0.6) % 1; hx, hy = BXs, BYs - 190 * BSs
        p.ell(hx - 15 * BSs, hy + 10 * BSs + u * 40 * BSs, 4 * BSs, 6 * BSs, (120, 190, 255, int(255 * (1 - u))), INK, 1 * BSs)
    # Shatta
    if tt >= ENTER[0]:
        k = kk(tt, *ENTER); x = lerp(SX0, SX1, ease(k) * 0.35 + k * 0.65); walk = tt * 8 if k < 1 else None
        sex = "happy" if k < 1 else "neutral"; sarms = "down"; lean = 0; hop = 0; slook = -1
        if k >= 1 and tt < T("S1"): sex = "shock"
        if T("S1") <= tt < CLAP: sex = "sad" if tt >= T("B1") else "neutral"
        if BUB <= tt < BUBEND: slook = -1; sex = "shock"
        if CLAP <= tt < CRY: sex = "happy"; sarms = "clap" if int((tt - CLAP) * 7) % 2 else "clap2"; hop = abs(math.sin((tt - CLAP) * 7)) * 8
        if CRY <= tt < LAUGH: sex = "shock" if tt < CRY + 1.4 else "flat"
        if laughing:
            sex = "laugh"; sarms = "hips" if int(lu * 5) % 2 else "clap"; lean = -0.35 + math.sin(lu * 9) * 0.15
            hop = abs(math.sin(lu * 8)) * 18; slook = 0
        X, Y_, SC = person(lay, cam, "shatta", x, SY, SS, tt, sex, slook, sarms, lean, walk, hop)
        p.line([(X - 20 * SC, Y_ - 134 * SC), (X + 24 * SC, Y_ - 70 * SC)], (70, 50, 120, 255), 5 * SC)     # schoolbag strap
    lay = tint_layer(lay, (255, 236, 210)); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    # ---- overlays ----
    series_tag(fr, tt, 0.4, 3.2)
    if tt < ENTER[0] + 0.4:
        q = W2S(cam, BX + 150, SEAT_Y - 330); lzt(fr, q[0], q[1], "هـــه...", int(90 * popk(tt, 0.5)), (255, 255, 255))
    if WHISTLE[0] <= tt < WHISTLE[1]:
        for k_ in range(3):
            u = ((tt - WHISTLE[0]) * 1.2 + k_ / 3) % 1; q = W2S(cam, SX1 + 160 + u * 140, 500 - u * 120)
            lzt(fr, q[0] + math.sin(u * 9) * 18, q[1], "♪", int(70 * (1 - u * 0.4)), (255, 214, 90), font=ROOT + "/brand/fonts/DejaVuSans-Bold.ttf")
    fr = bubble(fr, cam, tt)
    if laughing:
        for k_, (dx, dy, sz) in enumerate(((-560, -300, 110), (420, -360, 96), (600, -100, 100), (60, -420, 90))):
            t0_ = LAUGH + 0.2 + k_ * 0.3
            if tt >= t0_: lzt(fr, W / 2 + dx + math.sin(tt * 6 + k_) * 10, H / 2 + dy, "ههههه", int(sz * popk(tt, t0_)), (255, 214, 90))
        if tt >= FREEZE: fr = Image.blend(fr, Image.new("RGB", fr.size, (255, 255, 255)), 0.6 * (1 - kk(tt, FREEZE, FREEZE + 0.2)))
    return finish(fr, tt)

def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def whistle():
    notes = [(1568, 0.22), (1760, 0.22), (1976, 0.3), (1760, 0.18), (2093, 0.35)]; out = []
    for f, d in notes:
        d_ = np.arange(int(SR * d)) / SR; env = np.minimum(1, d_ / 0.03) * np.minimum(1, (d - d_) / 0.05)
        out.append((np.sin(2 * np.pi * (f + 14 * np.sin(2 * np.pi * 6 * d_)) * d_) * env * 0.16).astype(np.float32))
    return np.concatenate(out)
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(46)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 300) * 0.02, 0, 1.0)
    w_ = whistle(); cut_ = int(SR * (ENTER[1] + 0.05 - WHISTLE[0])); mix_into(buf, w_[:cut_], WHISTLE[0], 1.0)   # whistle cut short when he sees him
    mix_into(buf, SFXF["steps"][:int(SR * 1.6)] * 0.5, ENTER[0], 1.0)
    for k_ in range(3): mix_into(buf, tone(880 + k_ * 220, 0.12, 0.18, 18), BUB + k_ * 0.08, 1.0)               # bubble pops
    for k_, f in enumerate((392, 370, 349, 330)): mix_into(buf, tone(f, 0.5, 0.12, 2.5), BUB + 0.1 + k_ * 0.45, 1.0)  # memory chime
    for k_ in range(int((CRY - CLAP) / 0.14)): mix_into(buf, tone(1600, 0.04, 0.22, 60) + tone(900, 0.04, 0.18, 60), CLAP + k_ * 0.14, 1.0)  # claps
    fz = lowpass(r.normal(0, 1, int(SR * (LAUGH - CRY - 1.4))).astype(np.float32), 2500) * 0.05                 # tear fountain
    mix_into(buf, fz, CRY + 1.4, 1.0)
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 0.5: mix_into(buf, SFXF["whoosh"] * 0.25, s_["start"] - 0.1, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), TOTAL - 2.4 + k_ * 0.09, 1.0)
    rms = lambda x: float(np.sqrt(np.mean(x ** 2))) + 1e-9
    ref = []
    for st, k in lines:
        if k == "GROUP": continue
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8; ref.append(rms(v)); mix_into(buf, v, st, 1.0)
    g = AUD["GROUP"]; mix_into(buf, g / rms(g) * float(np.mean(ref)) * 1.25, LAUGH, 1.0)
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
