# «يوميات شطة وزلطة» — الخبر الوحش  (H 1920x1080 + V 1080x1920 in one pass) — Hook rule + real seated poses
# Dr. Zalata (white coat) behind his desk, Bandaq on the patient chair — both in ONE frame (user ref 2026-11-15)
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/daily/10")
SERIES = "يوميات شطة وزلطة"; EPT = "الخبر الوحش"
HOOK_TEXT = "الدكتور: عندي خبر وحش عن مراتك… 😳"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"; DJ = ROOT + "/brand/fonts/DejaVuSans-Bold.ttf"
SFXF = {"whoosh": load_audio(ROOT + "/trend/01/sfx/whoosh.mp3")}

DRZ = "drzalata"; CH[DRZ] = dict(CH["zalata"]); CH[DRZ].update(shirt=(242, 244, 248), coat=True); BASE[DRZ] = "zalata"
SUB = {"Z1": "أنا آسف يا عم بندق... بس عندي خبر وحش.", "B1": "خير يا دكتور؟... طمّنّي!",
       "Z2": "مراتك عزيزة... مش هتقدر تتكلم تاني.", "B3": "بس برضه ما قولتليش... إيه الخبر الوحش يا دكتور؟", "GROUP": ""}
WHO = {"Z1": DRZ, "Z2": DRZ, "B1": "bondo2", "B3": "bondo2", "GROUP": "-"}
EXPR = {"Z1": "sad", "Z2": "sad", "B1": "scared", "B3": "neutral", "GROUP": "laugh"}
load_lines(list(SUB))
CLINIC = _ld(ROOT + "/daily/bg/clinic.png")        # NEW canonical location «العيادة» (docs/locations.md)

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
TWO = (965, 665, 1.8)
t = say(0.1, "Z1") + 0.0
shot("clinic", 0.0, t, (940, 650, 1.95), (965, 660, 1.85))                    # opens on the line (Hook rule)
s = t; t = say(t + 0.05, "B1") + 0.05; shot("clinic", s, t, TWO, (985, 660, 1.9))
s = t; t = say(t + 0.1, "Z2") - 0.25; shot("clinic", s, t, (780, 610, 2.0), (700, 585, 2.45))   # slow push-in on the doctor
NOD = (t, t + 0.55)                                                             # Bandaq nods (< 1 s), then asks right away
s = t; t = say(t + 0.6, "B3") - 0.3; shot("clinic", s, t, (1130, 625, 2.0), (1170, 615, 2.2), tin="whipl")
GASP = t; shakes.append((GASP, 18))
shot("clinic", GASP, GASP + 0.7, (630, 575, 2.6), (630, 570, 2.95), ease="crash")   # doctor's jaw drops
LAUGH = GASP + 0.55; say(LAUGH, "GROUP"); LU = DUR["GROUP"]
shot("clinic", GASP + 0.7, LAUGH + LU, TWO, (965, 670, 1.72))
t = LAUGH + LU; FREEZE = t - 0.2
shot("end", t, t + 2.4, None); t += 2.4
TOTAL = t

# ---------------- staging (world = clinic 1920x1080, floor line y≈660) ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
DOC = (620, 800, 1.8); PAT = (1290, 800, 1.8)          # (x, hip-on-seat y, scale)
DESK = (330, 960, 792, 945)                          # x0, x1, top y, bottom y

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

WOOD = (150, 98, 52, 255); WOOD_D = (110, 68, 34, 255); WOOD_L = (176, 120, 70, 255)
def desk(p, cam, tt):
    z = cam[2]; x0, x1, ty, by = DESK
    a = W2S(cam, x0 - 20, ty - 18); b = W2S(cam, x1 + 20, ty)
    p.rect(a[0], a[1], b[0], b[1], WOOD_L, INK, 3 * z, 3 * z)                                     # top
    a = W2S(cam, x0, ty); b = W2S(cam, x1, by); p.rect(a[0], a[1], b[0], b[1], WOOD, INK, 3 * z, 2 * z)   # front panel
    for xx in (x0 + 40, x1 - 220):
        q = W2S(cam, xx, ty + 40); q2 = W2S(cam, xx + 180, by - 40); p.rect(q[0], q[1], q2[0], q2[1], WOOD_D, INK, 2 * z, 3 * z)
    # props on the desk: pen cup, files, nameplate «د. زلطة» (drawn as text later)
    q = W2S(cam, 420, ty - 18); p.rect(q[0], q[1] - 46 * z, q[0] + 36 * z, q[1], (60, 70, 90, 255), INK, 2 * z, 3 * z)
    for i, c in enumerate(((220, 60, 50), (40, 90, 200), (30, 30, 30))):
        p.line([(q[0] + (9 + 9 * i) * z, q[1] - 46 * z), (q[0] + (6 + 12 * i) * z, q[1] - 70 * z)], c + (255,), 4 * z)
    q = W2S(cam, 460, ty - 18); p.rect(q[0], q[1] - 16 * z, q[0] + 120 * z, q[1], (60, 120, 190, 255), INK, 2 * z, 2 * z)
    p.rect(q[0] + 6 * z, q[1] - 28 * z, q[0] + 116 * z, q[1] - 16 * z, (90, 160, 90, 255), INK, 2 * z, 2 * z)
    q = W2S(cam, 760, ty - 18); p.rect(q[0], q[1] - 44 * z, q[0] + 210 * z, q[1], (90, 56, 30, 255), INK, 2.5 * z, 4 * z)
def nameplate(fr, cam):
    z = cam[2]; q = W2S(cam, 865, DESK[2] - 40); lzt(fr, q[0], q[1], "د. زلطة", int(34 * z), (240, 200, 90), (40, 20, 6))
def chair(p, cam, back):
    z = cam[2]; x, y = PAT[0], PAT[1]
    if back:   # backrest behind Bandaq (he faces left → back on the right)
        a = W2S(cam, x + 20, y - 190); b = W2S(cam, x + 44, y + 6); p.rect(a[0], a[1], b[0], b[1], (50, 54, 62, 255), INK, 2.5 * z, 6 * z)
        return
    a = W2S(cam, x - 70, y - 4); b = W2S(cam, x + 50, y + 18); p.rect(a[0], a[1], b[0], b[1], (50, 54, 62, 255), INK, 2.5 * z, 5 * z)
    for xx in (x - 58, x + 36):
        q = W2S(cam, xx, y + 18); q2 = W2S(cam, xx, y + 140); p.line([q, q2], (120, 124, 132, 255), 6 * z)

def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255, font=None):
    if size < 4: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(font or LZ, size)
    kw = dict(font=f, anchor="mm", direction="rtl", language="ar") if font is None else dict(font=f, anchor="mm")
    d.text((x, y), s, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), **kw)
    d.text((x, y), s, fill=fill + (alpha,), **kw); img.paste(lay, (0, 0), lay)
def popk(tt, t0, d=0.22):
    u = kk(tt, t0, t0 + d); return 0 if u <= 0 else (1 + 0.25 * math.sin(u * math.pi)) if u < 1 else 1

_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/daily/10")
_FC = {}
def frame_cache(t_):
    if t_ not in _FC: _FC[t_] = frame(t_)
    return _FC[t_]
def endcard(tt, sh):
    k = kk(tt, sh["start"], sh["start"] + 0.4)
    fr = ImageEnhance.Brightness(frame_cache(FREEZE)).enhance(1 - 0.55 * k).filter(ImageFilter.GaussianBlur(6 * k)).convert("RGBA")
    sc = popk(tt, sh["start"] + 0.1, 0.3)
    if sc > 0:
        lzt(fr, W / 2, 400, "منشن صاحبك اللي هيرد كده!", int(96 * sc), (255, 214, 90))
    if tt >= sh["start"] + 0.5:
        logo(fr, W / 2, 680, 130); text(fr, W / 2, 830, "@shattawzalata", 52, (255, 214, 90))
    return fr.convert("RGB")

def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "end": return finish(endcard(tt, sh), tt)
    cam = cam_at(sh, tt); z = cam[2]
    img = bg_crop(CLINIC, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    gasp = tt >= GASP
    # ---- doctor (behind the desk, facing right)
    dex = "gasp" if gasp else ("flat" if tt >= T("B3") else "sad")
    darms = arms_at([(0, "hold"), (T("Z2"), "talk"), (T("Z2") + DUR["Z2"] - 0.3, "hold"), (GASP, "scared")], tt, 0.18)
    person(lay, cam, DRZ, *DOC, tt, dex, 1, darms, 0.0, "notebook" if not gasp else None, sit=1)
    desk(p, cam, tt)
    if gasp:                                                                    # the pen falls on the desk
        u = kk(tt, GASP, GASP + 0.35); q = W2S(cam, 700 + 30 * u, DESK[2] - 150 + 128 * ease(u))
        p.line([(q[0], q[1]), (q[0] + 34 * z, q[1] + (8 - 30 * u) * z)], (40, 90, 200, 255), 5 * z)
    # ---- Bandaq (patient chair, facing left)
    chair(p, cam, True)
    bex = "scared" if tt < T("Z2") else "flat"
    if NOD[0] <= tt < T("B3"): bex = "neutral"
    if tt >= T("B3"): bex = "neutral"
    if tt >= LAUGH + 0.4: bex = "happy"
    nod = 0.0
    if NOD[0] <= tt < NOD[1]: nod = math.sin((tt - NOD[0]) / (NOD[1] - NOD[0]) * 2 * math.pi) * 8      # one quick yes-nod
    barms = arms_at([(0, "clap"), (T("B1") + DUR["B1"], "down"), (T("B3"), "talk"), (GASP + 0.3, "down")], tt)
    blean = -0.25 if T("B3") <= tt < GASP + 0.5 else 0.0                       # leans in toward the doctor to ask
    person(lay, cam, "bondo2", *PAT, tt, bex, -1, barms, blean, None, sit=-1, nod=nod)
    chair(p, cam, False)
    lay = tint_layer(lay, (255, 238, 214)); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    nameplate(fr, cam)
    if gasp and tt < GASP + 0.7:
        lzt(fr, W * 0.66, H * 0.22, "!!!", int(170 * popk(tt, GASP, 0.2)), (255, 80, 60))
    if tt >= LAUGH:
        # (user 2026-11-15: no «ههههه» text — the audience laugh is sound only)
        if tt >= FREEZE: fr = Image.blend(fr, Image.new("RGB", fr.size, (255, 255, 255)), 0.6 * (1 - kk(tt, FREEZE, FREEZE + 0.2)))
    if tt < 3.2:                                                                # hook banner (H)
        a = int(255 * min(1, (3.2 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([W / 2 - 680, 40, W / 2 + 680, 150], 30, fill=(20, 12, 8, int(a * 0.8)))
        lzt(fr, W / 2, 95, "الدكتور: عندي خبر وحش عن مراتك!", 72, (255, 214, 90), alpha=a)
    return finish(fr, tt)

def vertical(fr, tt):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = ImageEnhance.Brightness(small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.35)
    bgv.paste(fr.resize((1080, 608), Image.LANCZOS), (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(255, 214, 90)); d.rectangle([0, 1168, 1080, 1171], fill=(255, 214, 90))
    lzt(bgv, 540, 250, "الدكتور: عندي خبر وحش", 92, (255, 255, 255))
    lzt(bgv, 540, 395, "عن مراتك!", 124, (255, 214, 90))
    lzt(bgv, 540, 1840, SERIES, 44, (255, 150, 110))
    k, _ = line_at(tt)
    if k and SUB.get(k):
        for i, l in enumerate(wrap(SUB[k])[:4]): text(bgv, 540, 1290 + i * 80, l, 60, sw=6)
    return bgv

def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(46)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 300) * 0.02, 0, 1.0)
    for k_ in range(int(TOTAL / 1.0)):                                          # wall clock ticking (louder in the pause)
        mix_into(buf, tone(1500, 0.04, 0.05 if not (NOD[0] - 0.4 <= k_ <= NOD[1]) else 0.12, 50), k_ * 1.0 + 0.5, 1.0)
    mix_into(buf, tone(180, 0.5, 0.25, 4) + tone(120, 0.5, 0.25, 4), T("Z2") + DUR["Z2"] - 0.4, 1.0)   # low "dun" after the news
    mix_into(buf, tone(2600, 0.5, 0.18, 7) + tone(3900, 0.5, 0.08, 9), GASP + 0.3, 1.0)                 # pen «تِن»
    mix_into(buf, tone(220, 0.3, 0.35, 12) + tone(440, 0.3, 0.2, 14), GASP, 1.0)
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
