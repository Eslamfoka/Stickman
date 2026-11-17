# «يوميات شطة وزلطة» — الفطار  (H 1920x1080 + V 1080x1920 in one pass) — user script 2026-11-15, GO 2026-11-17
# Bandaq begs for breakfast; Aziza lazy in bed; «هتجوّز عليكي» → she SITS UP delighted: «يا ريت! خليها تعملنا الفطار سوا!» → his stunned face + laugh.
# Location: «أوضة بندق وعزيزة» (daily/bg/bandaq_room.png, morning light). Bed drawn in code = SAME bed as the case-3 photo
# (brown wooden headboard, pink pillows, floral pink blanket) — side view, headboard on the left.
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/daily/12")
SERIES = "يوميات شطة وزلطة"; EPT = "الفطار"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"
SFXF = {"whoosh": load_audio(ROOT + "/trend/01/sfx/whoosh.mp3"), "sting": load_audio(ROOT + "/trend/01/sfx/stinger.mp3")}

SUB = {"B1": "قومي اعمليلي فطار يا وليّة! حرام عليكي... هموت من الجوع!", "A1": "ما قلتلك مش قادرة!",
       "B2": "لو ما قمتيش... هتجوّز عليكي!", "A2": "يا ريت! خليها تعملنا الفطار سوا!", "GROUP": ""}
WHO = {"B1": "bondo2", "A1": "aziza", "B2": "bondo2", "A2": "aziza", "GROUP": "-"}
EXPR = {"B1": "sad", "A1": "sleepy", "B2": "angry", "A2": "happy", "GROUP": "laugh"}
load_lines(list(SUB))
ROOM = _ld(ROOT + "/daily/bg/bandaq_room.png")

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
TWO = (1180, 700, 1.5)
t = say(0.1, "B1"); B1 = T("B1")
shot("room", 0.0, B1 + 3.2, TWO, (1180, 700, 1.62))                                   # two-shot: he begs at her bedside
shot("room", B1 + 3.2, t + 0.1, (830, 690, 2.4), (830, 684, 2.55), tin="whipl")       # «حرام عليكي… هموت من الجوع» CU, hand on his stomach (growl)
t += 0.1
s = t; t = say(t + 0.05, "A1") + 0.15; shot("room", s, t, (1160, 740, 2.5), (1160, 736, 2.65), tin="whip")   # CU her on the pillow, eyes shut
s = t; t = say(t + 0.1, "B2"); B2 = T("B2")
shot("room", s, B2 + 1.7, (830, 690, 2.3), (830, 684, 2.6))                            # slow push-in: «لو ما قمتيش…»
shot("room", B2 + 1.7, t + 0.05, (830, 680, 2.9), (830, 676, 3.1), ease="crash")       # «هتجوّز عليكي!» crash-in + sting
t += 0.05
EYES = t; shot("room", t, t + 0.6, (1150, 740, 2.9), (1150, 736, 3.05))      # her eyes pop open
t += 0.6
UP = t; a2 = say(t + 0.25, "A2"); shot("room", t, a2 + 0.15, (1260, 700, 1.9), (1260, 690, 2.0), tin="whipl")   # she SITS UP delighted
t = a2 + 0.15
REACT = t; shot("room", t, t + 0.9, (830, 690, 2.4), (830, 680, 2.85), tin="whip", ease="crash")   # his stunned face
LAUGH = t + 0.7; say(LAUGH, "GROUP"); LU = min(3.0, DUR["GROUP"])
shot("room", t + 0.9, LAUGH + LU, (830, 680, 2.85), (830, 676, 2.95))                  # laugh over his face
t = LAUGH + LU; FREEZE = t - 0.2
shot("end", t, t + 2.4, None); t += 2.4
TOTAL = t

# ---------------- staging (world = room 1920x1080) ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
BD = (820, 1010, 1.75)                     # Bandaq standing at the bedside, facing right
BED = (1000, 1800, 780)                    # x0 (headboard), x1 (foot), mattress top y
HIP = (1360, 770)                          # Aziza's hip under the blanket
AZS = 1.7

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, held=None, nod=0.0):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    blink = ((tt + len(who) * 0.37) % 3.6) < 0.11 and expr not in ("sleepy", "laugh", "shock", "gasp")
    if not talking: lean += math.sin(tt * 1.7 + len(who)) * 0.04
    X, Y_ = W2S(cam, x, y); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, held, lean, None, nod=nod)

def aziza_angle(tt):
    """90 = lying (head on the pillow, to the left), 0 = sitting up"""
    if tt < UP: return 90.0 - (6 * math.sin(tt * 1.3) if tt < T("A1") else 0)
    return 90.0 * (1 - ease(kk(tt, UP, UP + 0.28)))

def aziza(img_lay, cam, tt):
    """draw her standing on a temp layer (feet = hip + 62S), rotate around the hip, paste"""
    z = cam[2]; S = AZS * CH["aziza"]["scale"]
    PADW, PADH = SSW // SS, SSH // SS                                     # pad the temp layer so the head is not clipped before rotating
    tmp = Image.new("RGBA", (SSW * 3, SSH * 3), (0, 0, 0, 0))
    k, lt = line_at(tt); talking = k in ("A1", "A2")
    expr = "sleepy"
    if tt >= EYES: expr = "shock"
    if tt >= UP: expr = "happy"
    if talking: expr = expr_of(k, lt)
    if tt >= REACT: expr = "happy"
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    hx, hy = W2S(cam, *HIP)
    arms = "down" if tt < UP else ("clap" if tt < UP + 2.0 else "raise")
    draw_char(P(tmp), "aziza", hx + PADW, hy + PADH + 62 * S * z, AZS * z, expr, mouth, 0, False, arms, tt, None, 0.0, None)
    ang = aziza_angle(tt)
    if ang > 0.5: tmp = tmp.rotate(ang, center=((hx + PADW) * SS, (hy + PADH) * SS), resample=Image.BICUBIC)
    img_lay.alpha_composite(tmp.crop((SSW, SSH, SSW * 2, SSH * 2)))

def bed_back(p, cam):
    z = cam[2]; x0, x1, top = BED
    a = W2S(cam, x0 - 20, top - 260); b = W2S(cam, x0 + 40, top + 180); p.rect(a[0], a[1], b[0], b[1], (122, 74, 42, 255), INK, 3 * z, 18 * z)   # headboard
    for yy in range(top - 220, top + 120, 60):
        a = W2S(cam, x0 - 6, yy); b = W2S(cam, x0 + 26, yy + 40); p.rect(a[0], a[1], b[0], b[1], (98, 58, 32, 255), None, 0, 6 * z)
    a = W2S(cam, x1 - 30, top - 110); b = W2S(cam, x1 + 20, top + 180); p.rect(a[0], a[1], b[0], b[1], (122, 74, 42, 255), INK, 3 * z, 14 * z)   # foot board
    a = W2S(cam, x0 + 30, top); b = W2S(cam, x1 - 20, top + 90); p.rect(a[0], a[1], b[0], b[1], (246, 242, 234, 255), INK, 3 * z, 10 * z)      # mattress
    a = W2S(cam, x0 + 30, top + 90); b = W2S(cam, x1 - 20, top + 150); p.rect(a[0], a[1], b[0], b[1], (122, 74, 42, 255), INK, 3 * z, 4 * z)   # frame
    for xx in (x0 + 40, x1 - 50):
        a = W2S(cam, xx, top + 150); b = W2S(cam, xx + 26, top + 220); p.rect(a[0], a[1], b[0], b[1], (98, 58, 32, 255), INK, 2 * z, 3 * z)
    a = W2S(cam, x0 + 45, top - 55); b = W2S(cam, x0 + 215, top + 10); p.rect(a[0], a[1], b[0], b[1], (255, 236, 240, 255), INK, 3 * z, 26 * z)   # her pillow

def blanket(p, cam, tt):
    """floral pink blanket — up to her shoulders while lying, slides down to her lap when she sits up"""
    z = cam[2]; x0, x1, top = BED
    u = ease(kk(tt, UP, UP + 0.35)); left = lerp(1210, 1330, u); hump = lerp(70, 40, u)
    pts = [W2S(cam, left, top - 10)]
    for i in range(1, 13):
        xx = lerp(left, x1 - 40, i / 12); bump = math.sin(min(1, (xx - left) / 380) * math.pi) * hump if xx < left + 380 else 10
        pts.append(W2S(cam, xx, top - 10 - bump))
    pts += [W2S(cam, x1 - 20, top + 110), W2S(cam, left - 20, top + 110)]
    p.poly(pts, (186, 66, 92, 255), INK, 3 * z)
    for i in range(16):
        fx = left + 40 + (i * 97) % (x1 - left - 120); fy = top + 20 + (i * 37) % 70
        q = W2S(cam, fx, fy)
        for a_ in range(5):
            r = 9 * z; p.ell(q[0] + math.cos(a_ * 1.26) * r, q[1] + math.sin(a_ * 1.26) * r, 6 * z, 6 * z, (246, 196, 206, 255), None)
        p.ell(q[0], q[1], 5 * z, 5 * z, (250, 220, 90, 255), None)

def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255):
    if size < 4: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(LZ, size)
    d.text((x, y), s, font=f, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), anchor="mm", direction="rtl", language="ar")
    d.text((x, y), s, font=f, fill=fill + (alpha,), anchor="mm", direction="rtl", language="ar")
    img.paste(lay, (0, 0), lay)
def popk(tt, t0, d=0.22):
    u = kk(tt, t0, t0 + d); return 0 if u <= 0 else (1 + 0.25 * math.sin(u * math.pi)) if u < 1 else 1

def zzz(fr, cam, tt):
    if tt >= EYES: return
    z = cam[2]; d = ImageDraw.Draw(fr, "RGBA")
    for i in range(3):
        ph = (tt * 0.6 + i / 3) % 1.0; q = W2S(cam, 1100 + ph * 120, 640 - ph * 160)
        lzt(fr, q[0], q[1], "z", int((26 + i * 10) * z / 1.5), (80, 120, 200), (255, 255, 255), alpha=int(255 * math.sin(ph * math.pi)))

def growl(fr, cam, tt):
    """stomach growl lines on «هموت من الجوع»"""
    t0 = T("B1") + 3.3
    if not (t0 <= tt < t0 + 1.4): return
    z = cam[2]; S = BD[2] * CH["bondo2"]["scale"]; q = W2S(cam, BD[0] + 10, BD[1] - 62 * S - 30 * S); d = ImageDraw.Draw(fr, "RGBA")
    for i in range(3):
        r = (30 + i * 18) * z * (0.8 + 0.2 * math.sin(tt * 30 + i))
        d.arc([q[0] - r, q[1] - r, q[0] + r, q[1] + r], 300, 60, fill=(255, 200, 90, 220), width=int(4 * z))

def hearts(fr, cam, tt):
    if not (UP <= tt < REACT + 0.9): return
    z = cam[2]; d = ImageDraw.Draw(fr, "RGBA")
    for i in range(7):
        ph = (tt * 0.5 + i / 7) % 1.0
        x, y = W2S(cam, HIP[0] - 150 + (i % 4) * 90 + math.sin(tt * 2 + i) * 20, 470 - ph * 200)
        a_ = int(220 * math.sin(ph * math.pi) * kk(tt, UP, UP + 0.3)); r = (12 + (i % 2) * 6) * z
        d.ellipse([x - 2 * r, y - r, x, y + r * 0.6], fill=(235, 60, 90, a_)); d.ellipse([x, y - r, x + 2 * r, y + r * 0.6], fill=(235, 60, 90, a_))
        d.polygon([(x - 2 * r + 1, y), (x + 2 * r - 1, y), (x, y + 2 * r)], fill=(235, 60, 90, a_))

_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/daily/12")
_FC = {}
def frame_cache(t_):
    if t_ not in _FC: _FC[t_] = frame(t_)
    return _FC[t_]
def endcard(tt, sh):
    k = kk(tt, sh["start"], sh["start"] + 0.4)
    fr = ImageEnhance.Brightness(frame_cache(FREEZE)).enhance(1 - 0.55 * k).filter(ImageFilter.GaussianBlur(6 * k)).convert("RGBA")
    sc = popk(tt, sh["start"] + 0.1, 0.3)
    if sc > 0: lzt(fr, W / 2, 400, "منشن مراتك اللي هترد كده!", int(96 * sc), (255, 214, 90))
    if tt >= sh["start"] + 0.5:
        logo(fr, W / 2, 680, 130); text(fr, W / 2, 830, "@shattawzalata", 52, (255, 214, 90))
    return fr.convert("RGB")

def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "end": return finish(endcard(tt, sh), tt)
    cam = cam_at(sh, tt); z = cam[2]
    img = bg_crop(ROOM, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    bed_back(p, cam)
    aziza(lay, cam, tt)
    p = P(lay); blanket(p, cam, tt)
    # Bandaq
    bex = "sad"
    if T("B2") <= tt < UP: bex = "angry"
    if UP <= tt < REACT: bex = "smug" if tt < UP + 0.4 else "shock"
    if tt >= REACT: bex = "shock"
    barms = "clap"
    if T("B1") + 3.2 <= tt < T("A1"): barms = "hold"
    if T("A1") <= tt < T("B2"): barms = "shush"
    if T("B2") <= tt < UP: barms = "point" if tt >= T("B2") + 1.7 else "hips"
    if tt >= UP: barms = "down"
    blean = 0.12 if T("B2") + 1.7 <= tt < UP else 0.0
    person(lay, cam, "bondo2", *BD, tt, bex, 1 if tt < REACT else 0, barms, blean)
    lay = tint_layer(lay, (255, 240, 214)); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    zzz(fr, cam, tt); growl(fr, cam, tt); hearts(fr, cam, tt)
    if tt < 3.0:
        a_ = int(255 * min(1, (3.0 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([W / 2 - 700, 40, W / 2 + 700, 150], 30, fill=(20, 12, 8, int(a_ * 0.8)))
        lzt(fr, W / 2, 95, "هددها إنه هيتجوّز عليها… ردّها؟! 😂".replace(" 😂", ""), 70, (255, 214, 90), alpha=a_)
    return finish(fr, tt)

def vertical(fr, tt):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = ImageEnhance.Brightness(small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.35)
    bgv.paste(fr.resize((1080, 608), Image.LANCZOS), (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(255, 214, 90)); d.rectangle([0, 1168, 1080, 1171], fill=(255, 214, 90))
    lzt(bgv, 540, 250, "هددها إنه هيتجوّز", 100, (255, 255, 255))
    lzt(bgv, 540, 395, "عليها… ردّها؟!", 110, (255, 214, 90))
    lzt(bgv, 540, 1840, SERIES, 44, (255, 150, 110))
    k, _ = line_at(tt)
    if k and SUB.get(k):
        for i, l in enumerate(wrap(SUB[k])[:4]): text(bgv, 540, 1290 + i * 80, l, 60, sw=6)
    return bgv

def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(52)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 300) * 0.018, 0, 1.0)
    for k_ in range(10):                                                                        # morning birds
        st = 0.5 + k_ * 2.1 + r.uniform(0, 0.8)
        if st < TOTAL - 6: mix_into(buf, tone(3300 + r.uniform(-300, 300), 0.07, 0.025, 30) + tone(3900, 0.07, 0.02, 35), st, 1.0)
    g0 = T("B1") + 3.3; d_ = np.arange(int(SR * 1.1)) / SR                                    # stomach growl
    growl_ = (np.sin(2 * np.pi * (70 + 30 * np.sin(d_ * 9)) * d_) * np.exp(-((d_ - 0.5) ** 2) * 6) * 0.35).astype(np.float32)
    mix_into(buf, growl_, g0, 1.0)
    mix_into(buf, SFXF["sting"] * 0.5, T("B2") + 1.7, 1.0)                                     # «هتجوّز عليكي!»
    mix_into(buf, tone(1600, 0.12, 0.2, 20), EYES + 0.05, 1.0)                                  # eyes «ping»
    mix_into(buf, SFXF["whoosh"] * 0.45, UP - 0.05, 1.0)                                        # she shoots up
    for k_, f in enumerate((523, 659, 784, 1047)): mix_into(buf, tone(f, 0.45, 0.07, 5), UP + 0.2 + k_ * 0.3, 1.0)   # happy harp
    mix_into(buf, tone(160, 0.5, 0.25, 5) + tone(110, 0.5, 0.25, 5), REACT, 1.0)
    for j in range(3): mix_into(buf, tone(4200, 0.05, 0.06, 30) + tone(4600, 0.05, 0.04, 30), REACT + 0.15 + j * 0.2, 1.0)  # cricket
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 0.5: mix_into(buf, SFXF["whoosh"] * 0.22, s_["start"] - 0.1, 1.0)
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
