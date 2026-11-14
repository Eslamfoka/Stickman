# «مين الكداب؟» — القضية 1: الزرعة المكسورة  (H 1920x1080 + V 1080x1920 in one pass)
# render:  python ep.py audio  →  python ep.py part 0 2 & python ep.py part 1 2  →  concat  →  mux mix.wav
# Answer (open the next case with it): زلطة — the power was out all night, so the desk lamp could not be on. Shatta's mud = football (red herring).
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont
os.chdir(ROOT + "/kaddab/01")
SERIES = "مين الكداب؟"; EPT = "الزرعة المكسورة"
HOOK_TEXT = "واحد فيهم بيكدب… تعرف مين؟ 🕵️"
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"; DJ = ROOT + "/brand/fonts/DejaVuSans-Bold.ttf"
SFXP = {"whoosh": "/trend/01/sfx/whoosh.mp3", "sting": "/trend/01/sfx/stinger.mp3"}
SFXF = {n: load_audio(ROOT + p) for n, p in SFXP.items()}

SUB = {"N1": "مين اللي كسر الزرعة بتاعتي؟!", "N2": "النور كان قاطع امبارح من الساعة عشرة لحد الصبح... واللي كسرها كان في العتمة!",
       "S1": "أنا نمت بدري... وما صحيتش غير الصبح!", "Z1": "أنا فضلت بذاكر على نور الأباجورة لحد الساعة اتنين.",
       "Z2": "واحتمال إني أنا: صفر في المية.", "T1": "أنا كنت نايمة جنب تيتا... اسألوها!",
       "N3": "صح... وكانت بتشخّر في ودني كمان.", "N4": "مين فيهم الكداب؟ واحد... ولا اتنين... ولا تلاتة؟ اكتبوا في الكومنتات!"}
WHO = {"N1": "nana", "N2": "nana", "S1": "shatta", "Z1": "zalata", "Z2": "zalata", "T1": "tota", "N3": "nana", "N4": "nana"}
EXPR = {"N1": "angry", "N2": "angry", "S1": "sleepy", "Z1": "smug", "Z2": "flat", "T1": "happy", "N3": "flat", "N4": "smug"}
load_lines(list(SUB))
LOBBY = _ld(ROOT + "/s1e10/bg/morning.png")        # canonical «مدخل العمارة»

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
CRASH = 0.12
shot("lobby", 0.0, 0.6, (845, 880, 2.6), (845, 885, 2.8))                                  # the pot falls & smashes (hook)
shakes.append((CRASH, 30))
t = say(0.55, "N1") + 0.1
shot("lobby", 0.6, t, (1400, 700, 1.9), (1420, 690, 2.2), tin="whip")                         # Nana, furious
NIGHT = (t, t + DUR["N2"] + 0.3)
t = say(t + 0.15, "N2") + 0.15; shot("night", NIGHT[0], t, (1000, 640, 1.15), (1000, 700, 1.4), tin="fade")   # flash-back: dark building
LINEUP = t; shot("lobby", t, t + 1.3, (1130, 760, 1.4), (1130, 760, 1.48), tin="fade"); t += 1.3   # the 3 suspects, numbers pop
s = t; t = say(t + 0.05, "S1") + 0.1; shot("lobby", s, t - 1.4, (760, 740, 1.9), (760, 735, 2.1), tin="whipl")
MUD = t - 1.4; shot("mud", MUD, t + 0.2, (700, 1010, 4.2), (700, 1015, 4.6), ease="crash"); t += 0.2   # insert: mud on his shoe
s = t; t = say(t + 0.05, "Z1") + 0.1; LAMP = (s + 0.4, t + 0.1)
shot("lobby", s, t, (1060, 670, 1.85), (1060, 665, 1.95), tin="whip")
s = t; t = say(t + 0.05, "Z2") + 0.15; shot("lobby", s, t, (1000, 640, 2.6), (1000, 640, 2.8))     # deadpan CU
s = t; t = say(t + 0.05, "T1") + 0.1; shot("lobby", s, t, (1220, 720, 2.0), (1220, 720, 2.15), tin="whip")
s = t; t = say(t + 0.05, "N3") + 0.2; SNORE = s; shot("lobby", s, t, (1360, 700, 1.6), (1360, 700, 1.7), tin="whip")
ASK = t; t = say(t + 0.1, "N4") + 0.4
shot("lobby", ASK, ASK + 2.2, (1450, 640, 2.2), (1450, 640, 2.45), tin="whip")                   # to camera
shot("lobby", ASK + 2.2, t, (1130, 760, 1.4), (1130, 760, 1.48))                                 # back to the lineup, numbers pulse
shot("end", t, t + 3.0, None); t += 3.0
TOTAL = t

# ---------------- staging (world = lobby 1920x1080) ----------------
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
POS = {"shatta": (700, 1050, 1.75), "zalata": (980, 1050, 1.75), "tota": (1240, 1055, 1.75), "nana": (1560, 1062, 1.9)}
POT = (845, 1015)

def arms_at(sched, tt, d=0.22):
    prev = sched[0][1]
    for i, (t0, pose) in enumerate(sched):
        if tt < t0: break
        if tt < t0 + d and i > 0: return (sched[i - 1][1], pose, (tt - t0) / d)
        prev = pose
    return prev

def person(lay, cam, who, x, y, s, tt, expr, look=0, arms="down", lean=0.0, walk=None, hop=0.0, held=None):
    k, lt = line_at(tt); talking = k is not None and WHO.get(k) == who
    if talking: expr = expr_of(k, lt)
    mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
    blink = ((tt + (hash(who) % 7) * 0.37) % 3.6) < 0.11 and expr not in ("sleepy", "laugh")
    if not talking and walk is None: lean += math.sin(tt * 1.7 + len(who)) * 0.06                 # idle weight shift
    X, Y_ = W2S(cam, x, y - hop); S = s * cam[2]
    draw_char(P(lay), who, X, Y_, S, expr, mouth, look, blink, arms, tt, held, lean, walk)
    return X, Y_, S * CH[who]["scale"]

def pot(p, cam, tt):
    z = cam[2]; x, y = W2S(cam, *POT)
    if tt < CRASH:                                                                # falling (enters from the top of frame)
        yy = y - (CRASH - tt) / CRASH * 300 * z
        p.poly([(x - 34 * z, yy - 50 * z), (x + 34 * z, yy - 50 * z), (x + 24 * z, yy), (x - 24 * z, yy)], (190, 95, 55, 255), INK, 3 * z)
        for a in (-1, 0, 1): p.line([(x + a * 10 * z, yy - 50 * z), (x + a * 26 * z, yy - 110 * z)], (60, 140, 60, 255), 6 * z)
        return
    p.ell(x, y + 4 * z, 90 * z, 16 * z, (95, 62, 38, 255), None)                  # spilled soil
    for dx, dy, r in ((-60, -6, 22), (54, -2, 18), (-8, -14, 26), (88, 8, 14), (-96, 6, 12)):
        p.poly([(x + (dx - r) * z, y + dy * z), (x + dx * z, y + (dy - r) * z), (x + (dx + r) * z, y + (dy + 4) * z)], (190, 95, 55, 255), INK, 2.5 * z)
    p.line([(x - 10 * z, y - 4 * z), (x + 30 * z, y - 46 * z)], (60, 140, 60, 255), 6 * z)            # the poor plant lying down
    p.ell(x + 34 * z, y - 50 * z, 14 * z, 9 * z, (80, 170, 70, 255), INK, 2 * z)

def badge(fr, x, y, n, sc, col):
    if sc <= 0: return
    d = ImageDraw.Draw(fr, "RGBA"); r = 46 * sc
    d.ellipse([x - r, y - r, x + r, y + r], fill=col + (255,), outline=(255, 255, 255, 255), width=int(6 * sc))
    lzt(fr, x, y + 4 * sc, n, int(70 * sc), (255, 255, 255), font=DJ)

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
os.chdir(ROOT + "/kaddab/01")
_FC = {}
def frame_cache(t_):
    if t_ not in _FC: _FC[t_] = frame(t_)
    return _FC[t_]
def endcard(tt, sh):
    k = kk(tt, sh["start"], sh["start"] + 0.4)
    fr = ImageEnhance.Brightness(frame_cache(sh["start"] - 0.05)).enhance(1 - 0.55 * k).filter(ImageFilter.GaussianBlur(6 * k)).convert("RGBA")
    sc = popk(tt, sh["start"] + 0.1, 0.3)
    if sc > 0:
        lzt(fr, W / 2, 330, "اكتب رقم الكداب في الكومنتات!", int(92 * sc), (255, 214, 90))
        for i, (n, col) in enumerate((("1", (230, 90, 40)), ("2", (60, 150, 80)), ("3", (220, 80, 150)))):
            badge(fr, W / 2 + (i - 1) * 200, 470, n, 1.3 * popk(tt, sh["start"] + 0.3 + i * 0.15), col)
        d = ImageDraw.Draw(fr, "RGBA"); d.rounded_rectangle([W / 2 - 360, 580, W / 2 + 360, 660], 30, fill=(230, 120, 30, 230))
        lzt(fr, W / 2, 618, "الحل في الحلقة الجاية!", 54, (255, 255, 255))
    if tt >= sh["start"] + 0.6:
        logo(fr, W / 2, 800, 110); text(fr, W / 2, 930, "@shattawzalata", 50, (255, 214, 90))
    return fr.convert("RGB")

def lamp_bubble(fr, cam, tt):
    """thought bubble over Zalata: his desk with the lamp ON — the visual lie (the power was out!)"""
    k = ease(kk(tt, LAMP[0], LAMP[0] + 0.3)) * (1 - ease(kk(tt, LAMP[1] - 0.25, LAMP[1])))
    if k <= 0: return fr
    z = cam[2]; hx, hy = W2S(cam, POS["zalata"][0], 600); cx, cy = W2S(cam, POS["zalata"][0] + 250, 545); R = 140 * z * k
    d = ImageDraw.Draw(fr, "RGBA")
    for f, r in ((0.3, 12), (0.6, 20)):
        q = (hx + (cx - hx) * f, hy + (cy - hy) * f); d.ellipse([q[0] - r * z * k, q[1] - r * z * k, q[0] + r * z * k, q[1] + r * z * k], fill=(250, 245, 230, 255), outline=(20, 20, 20, 255), width=4)
    d.ellipse([cx - R * 1.3, cy - R, cx + R * 1.3, cy + R], fill=(30, 34, 60, 255), outline=(20, 20, 20, 255), width=6)
    if k > 0.7:
        s = R / 170
        d.rectangle([cx - 140 * s, cy + 40 * s, cx + 140 * s, cy + 56 * s], fill=(150, 98, 52, 255))                 # desk
        d.polygon([(cx + 40 * s, cy - 70 * s), (cx + 110 * s, cy - 70 * s), (cx + 130 * s, cy - 20 * s), (cx + 20 * s, cy - 20 * s)], fill=(250, 210, 60, 255), outline=(20, 20, 20, 255))  # lamp shade
        d.line([(cx + 75 * s, cy - 20 * s), (cx + 75 * s, cy + 40 * s)], fill=(30, 30, 30, 255), width=int(6 * s))
        d.polygon([(cx + 20 * s, cy - 20 * s), (cx + 130 * s, cy - 20 * s), (cx + 170 * s, cy + 40 * s), (cx - 20 * s, cy + 40 * s)], fill=(255, 235, 110, 190))   # light cone
        d.ellipse([cx + 55 * s, cy - 32 * s, cx + 95 * s, cy - 8 * s], fill=(255, 255, 220, 255))          # the bulb is ON
        d.rectangle([cx - 110 * s, cy + 18 * s, cx - 20 * s, cy + 40 * s], fill=(245, 240, 220, 255), outline=(20, 20, 20, 255))   # open book
        lzt(fr, cx - 60 * s, cy - 40 * s, "2:00", int(54 * s), (120, 255, 140), (10, 30, 10), font=DJ)
    return fr

# ---------------- frame ----------------
def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "end": return finish(endcard(tt, sh), tt)
    cam = cam_at(sh, tt); z = cam[2]
    night = sh["set"] == "night"
    img = bg_crop(LOBBY, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    if not night:
        sex = "neutral"; zex = "neutral"; tex = "neutral"; nex = "angry"
        if tt < LINEUP: sex = zex = tex = "scared"
        if T("Z1") <= tt < T("T1"): sex = "smug"
        if SNORE <= tt < ASK: tex = "shock"; sex = "laugh"; zex = "smug"
        if tt >= ASK: sex = "scared"; zex = "flat"; tex = "smug"
        sarms = arms_at([(0, "scared"), (LINEUP, "down"), (T("S1"), "talk"), (T("Z1"), "down"), (SNORE, "hips"), (ASK, "scared")], tt)
        zarms = arms_at([(0, "scared"), (LINEUP, "down"), (T("Z1"), "hold"), (T("Z2"), "down"), (ASK, "hips")], tt)
        tarms = arms_at([(0, "scared"), (LINEUP, "down"), (T("T1"), "hips"), (SNORE, "scared"), (ASK, "down")], tt)
        narms = arms_at([(0, "hips"), (T("N1"), "point"), (T("N1") + DUR["N1"], "hips"), (ASK, "point"), (ASK + 2.2, "talk")], tt)
        look_s = 1 if T("Z1") <= tt < ASK else 0
        person(lay, cam, "shatta", *POS["shatta"], tt, sex, look_s, sarms, held="notebook" if False else None)
        person(lay, cam, "zalata", *POS["zalata"], tt, zex, 0, zarms, held="notebook" if T("Z1") <= tt < T("Z2") else None)
        person(lay, cam, "tota", *POS["tota"], tt, tex, -1 if SNORE <= tt < ASK else 0, tarms)
        person(lay, cam, "nana", *POS["nana"], tt, nex, -1, narms, held="slipper" if tt >= ASK + 2.2 else None)
        if sh["set"] == "mud":                                                    # mud on Shatta's shoes (red herring)
            for dx, dy, r in ((-30, -4, 9), (-22, -14, 6), (26, -4, 8), (36, -12, 5)):
                q = W2S(cam, POS["shatta"][0] + dx * 1.5, POS["shatta"][1] + dy); p.ell(q[0], q[1], r * z, r * 0.8 * z, (110, 72, 40, 255), INK, 1.2 * z)
    if not night: pot(p, cam, tt)                                               # in the foreground, in front of the kids
    lay = tint_layer(lay, (255, 236, 210)); img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    if night:                                                                     # flash-back: the building in the dark
        a = np.asarray(fr).astype(np.float32) * np.array([0.22, 0.26, 0.42]); fr = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
        u = tt - sh["start"]
        lzt(fr, W / 2, 200, "امبارح... الساعة 10 بالليل", int(84 * popk(tt, sh["start"] + 0.2)), (220, 230, 255), (10, 10, 30))
        if int(u * 7) % 9 != 0: lzt(fr, W / 2, 330, "النور قاطع", int(70 * popk(tt, sh["start"] + 0.9)), (255, 214, 90), (40, 20, 0))
    # ---- overlays: number badges over the suspects
    if not night and LINEUP <= tt and sh["set"] != "mud":
        for i, (who, col) in enumerate((("shatta", (230, 90, 40)), ("zalata", (60, 150, 80)), ("tota", (220, 80, 150)))):
            q = W2S(cam, POS[who][0], POS[who][1] - 330 * POS[who][2])
            pulse = 1 + (0.12 * math.sin(tt * 8) if tt >= ASK + 2.2 else 0)
            badge(fr, q[0], q[1], str(i + 1), min(1.1, z * 0.75) * popk(tt, LINEUP + 0.15 + i * 0.25) * pulse, col)
    if sh["set"] == "mud":
        lzt(fr, W * 0.72, H * 0.25, "طين؟!", int(110 * popk(tt, MUD + 0.2)), (255, 214, 90))
    fr = lamp_bubble(fr, cam, tt)
    if SNORE <= tt < ASK:
        q = W2S(cam, POS["tota"][0] + 90, 520); lzt(fr, q[0], q[1], "خخخ...", int(64 * popk(tt, SNORE + 0.8)), (180, 200, 255))
    if tt < 3.2:                                                                  # hook banner (horizontal)
        a = int(255 * min(1, (3.2 - tt) / 0.3)); d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([W / 2 - 600, 40, W / 2 + 600, 150], 30, fill=(20, 12, 8, int(a * 0.8)))
        lzt(fr, W / 2, 95, "واحد فيهم بيكدب… تعرف مين؟", 74, (255, 214, 90), alpha=a)
    return finish(fr, tt)

def vertical(fr, tt):
    small = fr.resize((96, 54), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    bgv = ImageEnhance.Brightness(small.crop((30, 0, 66, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.35)
    bgv.paste(fr.resize((1080, 608), Image.LANCZOS), (0, 560))
    d = ImageDraw.Draw(bgv)
    d.rectangle([0, 556, 1080, 559], fill=(255, 214, 90)); d.rectangle([0, 1168, 1080, 1171], fill=(255, 214, 90))
    lzt(bgv, 540, 240, "واحد فيهم بيكدب…", 104, (255, 255, 255))
    lzt(bgv, 540, 390, "تعرف مين؟", 130, (255, 214, 90))
    lzt(bgv, 540, 1840, "مين الكداب؟ • القضية 1", 46, (255, 150, 110))
    k, _ = line_at(tt)
    if k and SUB.get(k):
        for i, l in enumerate(wrap(SUB[k])[:4]): text(bgv, 540, 1290 + i * 80, l, 60, sw=6)
    return bgv

def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def crash():
    r = np.random.default_rng(9); n = int(SR * 0.9); d_ = np.arange(n) / SR
    out = r.normal(0, 1, n).astype(np.float32) * np.exp(-d_ * 9) * 0.5
    for f in (2100, 2900, 3700, 1700, 4400):
        st = int(SR * r.uniform(0.02, 0.35)); tt_ = tone(f, 0.25, 0.12, 22); out[st:st + len(tt_)] += tt_[:n - st]
    return out
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 2; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(46)
    mix_into(buf, lowpass(r.normal(0, 1, n).astype(np.float32), 300) * 0.02, 0, 1.0)
    c = crash(); c[:int(SR * 0.3)] += tone(90, 0.3, 0.6, 12); mix_into(buf, c, CRASH, 1.0)
    mix_into(buf, SFXF["sting"] * 0.5, NIGHT[0], 1.0)
    for k_ in range(int((T("N2") + DUR["N2"] - NIGHT[0]) / 0.5)): mix_into(buf, tone(1200, 0.05, 0.08, 40), NIGHT[0] + k_ * 0.5, 1.0)   # clock ticks
    for i in range(3): mix_into(buf, tone(660 + i * 220, 0.18, 0.2, 12), LINEUP + 0.15 + i * 0.25, 1.0)   # badge pops
    mix_into(buf, tone(220, 0.4, 0.3, 6) + tone(330, 0.4, 0.2, 6), MUD + 0.1, 1.0)
    mix_into(buf, SFXF["sting"] * 0.35, ASK + 2.2, 1.0)
    for s_ in shots:
        if s_.get("tin") in ("whip", "whipl") and s_["start"] > 0.5: mix_into(buf, SFXF["whoosh"] * 0.25, s_["start"] - 0.1, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), TOTAL - 2.9 + k_ * 0.09, 1.0)
    for st, k in lines:
        v = AUD[k] / max(1e-6, np.percentile(np.abs(AUD[k]), 99.5)) * 0.8; mix_into(buf, v, st, 1.0)
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
