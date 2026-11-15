# «يوميات شطة وزلطة» — فاكر يا بندق؟  (H 1920x1080 + V 1080x1920 in one pass) — user script 2026-11-15
# Aziza + Bandaq side by side on the sofa in their room under the stairs (NEW location «أوضة بندق وعزيزة», docs/locations.md)
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/daily/11")
SERIES = "يوميات شطة وزلطة"; EPT = "فاكر يا بندق؟"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"; DJ = ROOT + "/brand/fonts/DejaVuSans-Bold.ttf"
SFXF = {"whoosh": load_audio(ROOT + "/trend/01/sfx/whoosh.mp3")}

SUB = {"A1": "طلبتني للجواز 10 مرات... وأبويا كان بيرفضك كل مرة. فاكر يا بندق؟",
       "B1": "فاكر... الله يرحمه، كان عارف مصلحتي... بس أنا اللي كنت غبي.", "GROUP": ""}
WHO = {"A1": "aziza", "B1": "bondo2", "GROUP": "-"}
EXPR = {"A1": "happy", "B1": "neutral", "GROUP": "laugh"}
load_lines(list(SUB))
ROOM = _ld(ROOT + "/daily/bg/bandaq_room.png")      # NEW canonical location «أوضة بندق وعزيزة» (under the stairs)

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
TWO = (960, 695, 1.75)
t = say(0.1, "A1")                                                                   # first word at 0.1 s (hook rule)
shot("room", 0.0, 3.3, (900, 695, 1.9), (930, 695, 1.8))                          # two-shot, she is all smiles
shot("room", 3.3, t + 0.05, (760, 655, 2.3), (740, 650, 2.45), tin="whipl")        # CU Aziza: «فاكر يا بندق؟»
t += 0.05
s = t; t = say(t + 0.25, "B1")
NOD = (s + 0.3, s + 0.85)                                                            # «فاكر...» with a slow nod
PUNCH = T("B1") + DUR["B1"] - 1.7                                                    # «بس أنا اللي كنت غبي»
shot("room", s, PUNCH, (1170, 665, 2.2), (1190, 655, 2.4), tin="whip")             # CU Bandaq, calm
shot("room", PUNCH, t + 0.1, TWO, (960, 700, 1.8), tin="whip")                     # two-shot for the punchline
t += 0.1
TURN = (t, t + 0.7)                                                                  # Aziza turns her head slowly…
shot("room", t, t + 0.75, (780, 655, 2.3), (770, 645, 2.6))
t += 0.75
SLAP = t; shakes.append((SLAP, 20))                                                  # …crash zoom: slipper up!
shot("room", t, t + 0.6, (760, 635, 2.7), (760, 630, 3.0), ease="crash")
LAUGH = SLAP + 0.35; say(LAUGH, "GROUP"); LU = DUR["GROUP"]
shot("room", SLAP + 0.6, LAUGH + LU, TWO, (960, 705, 1.7))
t = LAUGH + LU; FREEZE = t - 0.2
shot("end", t, t + 2.4, None); t += 2.4
TOTAL = t

# ---------------- staging (world = room 1920x1080) ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
AZ = (790, 800, 1.8); BD = (1140, 800, 1.8)                 # (x, hip-on-seat y, scale)
SOFA = (560, 1370, 800)                                      # x0, x1, seat-top y

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
    blink = ((tt + len(who) * 0.37) % 3.6) < 0.11 and expr not in ("sleepy", "laugh", "gasp")
    if not talking: lean += math.sin(tt * 1.7 + len(who)) * 0.05
    X, Y_ = W2S(cam, x, y); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, held, lean, None, sit=sit, nod=nod)

SOF = (150, 62, 58, 255); SOF_D = (112, 42, 40, 255); SOF_L = (178, 84, 76, 255)
def sofa_back(p, cam):
    z = cam[2]; x0, x1, sy = SOFA
    a = W2S(cam, x0, sy - 230); b = W2S(cam, x1, sy + 6); p.rect(a[0], a[1], b[0], b[1], SOF_D, INK, 3 * z, 26 * z)     # backrest
    for i in range(3):                                                                                                  # back cushions
        cx = x0 + 40 + i * (x1 - x0 - 80) / 3
        a = W2S(cam, cx + 6, sy - 205); b = W2S(cam, cx + (x1 - x0 - 80) / 3 - 6, sy - 10); p.rect(a[0], a[1], b[0], b[1], SOF, INK, 2.5 * z, 18 * z)
    a = W2S(cam, x0 - 10, sy); b = W2S(cam, x1 + 10, sy + 70); p.rect(a[0], a[1], b[0], b[1], SOF_L, INK, 3 * z, 12 * z)   # seat front (behind the legs)
    a = W2S(cam, x0 - 10, sy + 70); b = W2S(cam, x1 + 10, sy + 120); p.rect(a[0], a[1], b[0], b[1], SOF_D, INK, 3 * z, 6 * z)
def sofa_front(p, cam):
    z = cam[2]; x0, x1, sy = SOFA
    for xx in (x0 - 60, x1 - 10):                                                                                        # arms
        a = W2S(cam, xx, sy - 120); b = W2S(cam, xx + 70, sy + 120); p.rect(a[0], a[1], b[0], b[1], SOF, INK, 3 * z, 22 * z)
    for xx in (x0 + 10, x1 - 30):
        a = W2S(cam, xx, sy + 120); b = W2S(cam, xx + 20, sy + 160); p.rect(a[0], a[1], b[0], b[1], (60, 36, 20, 255), INK, 2 * z, 3 * z)

def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255, font=None):
    if size < 4: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(font or LZ, size)
    kw = dict(font=f, anchor="mm", direction="rtl", language="ar") if font is None else dict(font=f, anchor="mm")
    d.text((x, y), s, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), **kw)
    d.text((x, y), s, fill=fill + (alpha,), **kw); img.paste(lay, (0, 0), lay)
def popk(tt, t0, d=0.22):
    u = kk(tt, t0, t0 + d); return 0 if u <= 0 else (1 + 0.25 * math.sin(u * math.pi)) if u < 1 else 1

def hearts(fr, cam, tt):
    """little hearts float up around Aziza while she remembers — they POP when the punchline lands"""
    if tt >= PUNCH + 0.9: return
    z = cam[2]; d = ImageDraw.Draw(fr, "RGBA")
    for i in range(6):
        ph = (tt * 0.45 + i / 6) % 1.0
        x, y = W2S(cam, AZ[0] - 120 + (i % 3) * 120 + math.sin(tt * 2 + i) * 20, 470 - ph * 200)
        x *= W / SSW; y *= H / SSH
        a = int(220 * math.sin(ph * math.pi)); r = (12 + (i % 2) * 6) * z * W / SSW
        if tt >= PUNCH: r *= 1 + 3 * kk(tt, PUNCH, PUNCH + 0.9); a = int(a * (1 - kk(tt, PUNCH + 0.3, PUNCH + 0.9)))
        d.ellipse([x - 2 * r, y - r, x, y + r * 0.6], fill=(235, 60, 90, a)); d.ellipse([x, y - r, x + 2 * r, y + r * 0.6], fill=(235, 60, 90, a))
        d.polygon([(x - 2 * r + 1, y), (x + 2 * r - 1, y), (x, y + 2 * r)], fill=(235, 60, 90, a))

_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/daily/11")
_FC = {}
def frame_cache(t_):
    if t_ not in _FC: _FC[t_] = frame(t_)
    return _FC[t_]
def endcard(tt, sh):
    k = kk(tt, sh["start"], sh["start"] + 0.4)
    fr = ImageEnhance.Brightness(frame_cache(FREEZE)).enhance(1 - 0.55 * k).filter(ImageFilter.GaussianBlur(6 * k)).convert("RGBA")
    sc = popk(tt, sh["start"] + 0.1, 0.3)
    if sc > 0:
        lzt(fr, W / 2, 400, "منشن جوزك اللي هيرد كده! 😂".replace(" 😂", ""), int(96 * sc), (255, 214, 90))
    if tt >= sh["start"] + 0.5:
        logo(fr, W / 2, 680, 130); text(fr, W / 2, 830, "@shattawzalata", 52, (255, 214, 90))
    return fr.convert("RGB")

def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "end": return finish(endcard(tt, sh), tt)
    cam = cam_at(sh, tt); z = cam[2]
    img = bg_crop(ROOM, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    sofa_back(p, cam)
    slap = tt >= SLAP
    # ---- Aziza (left, faces Bandaq)
    aex = "happy"
    if tt >= PUNCH + 0.4: aex = "flat"
    if TURN[0] <= tt < SLAP: aex = "angry"
    if slap: aex = "angry"
    aarms = arms_at([(0, "clap"), (T("A1") + 3.4, "talk"), (T("A1") + DUR["A1"], "down"), (TURN[0] + 0.3, "hips"), (SLAP, "up")], tt, 0.18)
    alook = 1
    if TURN[0] <= tt < TURN[0] + 0.35: alook = 0                                         # the slow turn: to camera first…
    alean = 0.18 if tt < T("B1") else 0.0                                                # leans on him while remembering
    if TURN[0] + 0.35 <= tt < SLAP: alean = 0.3 * kk(tt, TURN[0] + 0.35, SLAP)         # …then toward him
    person(lay, cam, "aziza", *AZ, tt, aex, alook, aarms, alean, "slipper" if slap else None, sit=1)
    # ---- Bandaq (right, faces Aziza; calm, then scared)
    bex = "neutral"
    if NOD[0] <= tt < NOD[1]: bex = "sleepy"
    if T("B1") <= tt and tt >= PUNCH: bex = "flat"
    if TURN[0] + 0.4 <= tt: bex = "scared"
    if tt >= LAUGH + 0.8: bex = "scared"
    nod = 0.0
    if NOD[0] <= tt < NOD[1]: nod = math.sin((tt - NOD[0]) / (NOD[1] - NOD[0]) * math.pi) * 9
    barms = arms_at([(0, "down"), (T("B1") + 0.6, "talk"), (PUNCH + 1.2, "down"), (TURN[0] + 0.4, "scared")], tt)
    blean = 0.25 if tt >= SLAP else 0.0                                                   # leans away from the slipper
    person(lay, cam, "bondo2", *BD, tt, bex, -1 if tt < PUNCH else 0, barms, blean, None, sit=-1, nod=nod)
    sofa_front(p, cam)
    lay = tint_layer(lay, (255, 236, 210)); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    hearts(fr, cam, tt)
    if slap and tt < SLAP + 0.6:
        lzt(fr, W * 0.70, H * 0.22, "!!!", int(170 * popk(tt, SLAP, 0.2)), (255, 80, 60))
    if tt >= FREEZE: fr = Image.blend(fr, Image.new("RGB", fr.size, (255, 255, 255)), 0.6 * (1 - kk(tt, FREEZE, FREEZE + 0.2)))
    if tt < 3.2:                                                                          # hook banner (H)
        a = int(255 * min(1, (3.2 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([W / 2 - 700, 40, W / 2 + 700, 150], 30, fill=(20, 12, 8, int(a * 0.8)))
        lzt(fr, W / 2, 95, "طلبها للجواز 10 مرات… وأبوها رفض!", 72, (255, 214, 90), alpha=a)
    return finish(fr, tt)

def vertical(fr, tt):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = ImageEnhance.Brightness(small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.35)
    bgv.paste(fr.resize((1080, 608), Image.LANCZOS), (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(255, 214, 90)); d.rectangle([0, 1168, 1080, 1171], fill=(255, 214, 90))
    lzt(bgv, 540, 250, "طلبها للجواز 10 مرات", 96, (255, 255, 255))
    lzt(bgv, 540, 395, "وأبوها رفض… ورده؟!", 110, (255, 214, 90))
    lzt(bgv, 540, 1840, SERIES, 44, (255, 150, 110))
    k, _ = line_at(tt)
    if k and SUB.get(k):
        for i, l in enumerate(wrap(SUB[k])[:4]): text(bgv, 540, 1290 + i * 80, l, 60, sw=6)
    return bgv

def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(47)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 300) * 0.02, 0, 1.0)
    for k_, f in enumerate((523, 659, 784, 659, 523, 659, 784, 1047)):                  # sweet music box while she remembers
        if k_ * 0.55 + 0.2 < PUNCH: mix_into(buf, tone(f, 0.5, 0.06, 5), 0.2 + k_ * 0.55, 1.0)
    mix_into(buf, tone(160, 0.6, 0.22, 4) + tone(110, 0.6, 0.22, 4), TURN[0], 1.0)       # slow-turn «dun»
    mix_into(buf, tone(220, 0.3, 0.35, 12) + tone(440, 0.3, 0.2, 14), SLAP, 1.0)
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 0.5: mix_into(buf, SFXF["whoosh"] * 0.25, s_["start"] - 0.1, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), TOTAL - 2.3 + k_ * 0.09, 1.0)
    rms = lambda x: float(np.sqrt(np.mean(x ** 2))) + 1e-9; ref = []
    for st, k in lines:
        if k == "GROUP": continue
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8; ref.append(rms(v)); mix_into(buf, v, st, 1.0)
    g = AUD["GROUP"]; mix_into(buf, g / rms(g) * float(np.mean(ref)) * 1.2, LAUGH, 1.0)
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
