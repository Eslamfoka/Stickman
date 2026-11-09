exec(open("/home/claude/repo/Stickman/trend/01/kit.py").read())
EPT = "الحلقة 3: الدقيقة 60"
SUB = {"P303": "ماتش صعب... والنتيجة لسه صفر صفر.",
       "P304": "ارجع يا شطة!... ارجع دفاع!",
       "P305": "يا كابتن... أنا مهاجم!",
       "P300": "الدقيقة ستين... والكابتن بيغيّر... شطة طالع!",
       "P301": "أنا؟!... أنا اللي جايب الأهداف!",
       "P302": "خلاص!... أنا ماشي من المعسكر!",
       "P306": "والماتش بيخلص... صفر صفر."}
WHO = {"P303": "fahmy", "P304": "bondo2", "P305": "shatta", "P300": "fahmy", "P301": "shatta", "P302": "shatta", "P306": "fahmy"}
EXPR = {"P304": "angry", "P305": "angry", "P301": "shock", "P302": "angry"}
ARMS = {"P304": "point", "P305": "up", "P301": "scared", "P302": "point"}
load_lines(list(SUB)); load_sfx(["crowd", "kick", "final", "whoosh", "switch", "stinger", "gasp"])

GOAL = (1765, 625)
_pitch = _ld("bg/pitch.png"); _cafe = _ld("bg/cafe.png")
TV = (928, 28, 1307, 244)
_ca = np.asarray(_cafe).astype(np.int16)
TVMASK = Image.fromarray((((_ca[..., 1] > 140) & (_ca[..., 0] < 140) & (_ca[..., 2] < 150)) * 255).astype(np.uint8))
RNG = np.random.default_rng(5)
FAN_BASES = ["roshdy", "fahmy", "sawsan", "nana", "tota", "abdo"]
def rnd_col(): return tuple(int(v) for v in RNG.integers(40, 235, 3))
FANS = []
for i in range(16):
    FANS.append((extra(FAN_BASES[i % 6], rnd_col(), rnd_col()), 650 + i * 30 + RNG.uniform(-8, 8), 600 - (i % 3) * 22, 0.36, ["eg", "ps", None, None][i % 4]))
for i in range(10):
    FANS.append((extra(FAN_BASES[(i + 2) % 6], rnd_col(), rnd_col()), 70 + (i % 5) * 95, 205 + (i // 5) * 120, 0.26, ["eg", None, "ps"][i % 3]))
for i in range(10):
    FANS.append((extra(FAN_BASES[(i + 4) % 6], rnd_col(), rnd_col()), 1460 + (i % 5) * 92, 190 + (i // 5) * 125, 0.26, ["ps", None, "eg"][i % 3]))
def crowd_bg(var, quiet=False):
    img = _pitch.resize((SSW, SSH), Image.BICUBIC)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    for j, (who, x, y, s, fl) in enumerate(FANS):
        hop = 0 if quiet else abs(math.sin(var * 1.57 + j)) * 10 * s
        arms = "hips" if quiet and j % 3 == 0 else ("up" if (j + var) % 3 == 0 and not quiet else "down")
        draw_char(p, who, x, y - hop, s, "sad" if quiet else "neutral", 0, 0, False, arms, var * 0.3, None, 0, None)
        if fl and not quiet: flag(p, x + 30 * s, y - hop - 60 * s, s * 1.4, fl, var * 0.5, j)
    lay = tint_layer(lay, (230, 225, 240), 0.95)
    img.paste(lay, (0, 0), lay); return img
CROWD = [crowd_bg(v) for v in range(4)]
QUIET = [crowd_bg(v, True) for v in range(2)]
PATRONS = [(extra("roshdy", rnd_col(), rnd_col()), 520, 1000, 1.7), (extra("fahmy", rnd_col(), rnd_col()), 860, 960, 1.45),
           (extra("abdo", rnd_col(), rnd_col()), 1240, 990, 1.6), (extra("nana", rnd_col(), rnd_col()), 1560, 1010, 1.7),
           (extra("roshdy", rnd_col(), rnd_col()), 230, 1040, 1.95)]
_XC = {}
def xc(key, base, col):
    if key not in _XC: _XC[key] = extra(base, col, (40, 30, 22))
    return _XC[key]
SIDE = (300, 990, 1.85); SHP = (1180, 760, 1.05); OFFI = (520, 900, 1.5)

def CU(who, pos, z=2.2):
    x, y, s = pos; S = s * CH[who]["scale"]; hy = y - 190 * S
    return (x, hy + H / (2 * z) - 1.45 * 46 * S - 25, z)

t = 0.0
fx(0, "crowd", 0.4)
shot("pitch", 0, 2.4, CU("shatta", SHP, 3.0), CU("shatta", SHP, 3.4), tin="flash", hook=True); t = 2.4
shot("title", t, t + 2.0, None, tin="fade"); fx(t, "whoosh", 0.5); TITLE = t; t += 2.0
s = t; t = say(t + 0.4, "P303") + 0.4; WIDE = s
shot("pitch", s, t, (960, 560, 1.0), (1000, 600, 1.2), tin="fade", score=True)
s = t; t = say(t, "P304") + 0.1; SHOUT = s
shot("pitch", s, t, CU("bondo2", SIDE, 1.8), CU("bondo2", SIDE, 2.1), tin="whipl", score=True)
s = t; t = say(t + 0.1, "P305") + 0.3
shot("pitch", s, t, CU("shatta", SHP, 2.4), CU("shatta", SHP, 2.6), tin="whip", score=True)
CAFE1 = (t, t + 2.4); fx(t, "crowd", 0.3)
shot("cafe", t, CAFE1[1], (960, 600, 1.05), (960, 570, 1.12), tin="whip"); t = CAFE1[1]
CLOCK = (t, t + 2.2); fx(t + 1.6, "switch", 0.8)
shot("clock", t, CLOCK[1], None, tin="zoom"); t = CLOCK[1]
BOARD = t
s = t; t = say(t + 0.3, "P300") + 0.2
shot("pitch", s, t, (560, 760, 1.6), (520, 740, 1.9), score=True, board=True)
fx(t, "gasp", 0.9)
s = t; t = say(t + 0.2, "P301") + 0.3; SHOCK = s
shot("pitch", s, t, CU("shatta", SHP, 2.0), CU("shatta", SHP, 2.6), ease="crash", tin="zoom", orbit=True, score=True)
WALK = (t, t + 4.4); THROW = t + 2.2
s = t; say(t + 1.0, "P302"); t = WALK[1]
shot("pitch", s, THROW, (1050, 720, 1.5), (760, 760, 1.4), score=True)
shot("pitch", THROW, t, (700, 860, 2.2), (680, 880, 2.6), slow=True, score=True)
SILENT = (t, t + 2.6)
shot("pitch", t, SILENT[1], (900, 560, 1.05), (900, 560, 1.12), quiet=True, score=True, tin="fade"); t = SILENT[1]
FINAL = t; fx(t, "final", 0.7)
s = t; t = say(t + 0.4, "P306") + 0.4
shot("pitch", s, t, (960, 560, 1.0), (960, 540, 1.08), quiet=True, score=True)
CAFE2 = (t, t + 2.6); TVOFF = t + 1.6; fx(TVOFF, "switch", 0.9)
shot("cafe", t, CAFE2[1], (960, 600, 1.05), (1000, 420, 1.5), tin="whip", sad=True); t = CAFE2[1]
shot("tbc", t, t + 2.6, None, tin="fade"); t += 2.6
TOTAL = t

def players(tt, sh):
    A = []
    Y = YELLOW_KIT
    if tt < FINAL:
        sha = A_("shatta", SHP, look=-1, kit=RED_KIT, num=10, expr="neutral")
        if tt < WIDE: sha["expr"] = "flat"
        if SHOUT <= tt < BOARD: sha["look"] = -1; sha["expr"] = "angry"
        if tt >= SHOCK: sha["expr"] = "shock"
        if tt >= WALK[0]:
            k = walk_to(sha, SHP, (620, 930, 1.75), (WALK[0], THROW + 0.6), tt, 7); sha["look"] = -1; sha["expr"] = "angry"
            if tt >= THROW - 0.3: sha["kit"] = None; sha["num"] = None; sha["arms"] = "up" if tt < THROW + 0.3 else "down"
            if tt >= THROW + 0.6:
                walk_to(sha, (620, 930, 1.75), (-200, 1000, 1.9), (THROW + 0.6, WALK[1] + 0.8), tt, 7)
        A.append(sha)
        for i, (k_, base, col, pos, n) in enumerate([("r2", "fahmy", RED_KIT, (800, 820, 1.25), 8), ("ko", None, RED_KIT, (980, 880, 1.4), 7),
                                                      ("y1", "abdo", Y, (1350, 780, 1.1), 3), ("y2", "roshdy", Y, (1500, 720, 0.95), 5),
                                                      ("gk", "roshdy", (40, 160, 90), (1700, 650, 0.85), 1)]):
            who = "koko" if k_ == "ko" else xc(k_, base, col)
            a = A_(who, pos, look=-1 if col == Y else 1, kit=col if k_ != "gk" else (40, 160, 90), num=n)
            if tt >= SHOCK: a["expr"] = "shock"
            A.append(a)
        bo = A_("bondo2", SIDE, look=1, expr="angry", whistle=True, arms="point")
        if tt >= SILENT[0]: bo["arms"] = "hips"; bo["expr"] = "flat"
        A.append(bo)
        if BOARD <= tt < SHOCK + 3:
            of = A_(xc("off", "roshdy", (30, 30, 30)), OFFI, look=1, arms="up", expr="flat")
            A.append(of)
    return A

def board(img, cam, tt):
    x0, y0, z = cam; S = SS * z; d = ImageDraw.Draw(img, "RGBA")
    X, Y = (OFFI[0] - x0) * S, (OFFI[1] - 1.5 * 200 - y0) * S
    w, h = 170 * S, 90 * S
    d.rectangle([X - w / 2, Y - h, X + w / 2, Y], fill=(15, 15, 15, 255), outline=(200, 200, 200, 255), width=max(1, int(4 * S)))
    on = int(tt * 4) % 2 == 0
    ltr(img, X - w / 4, Y - h / 2, "10", int(54 * S), (255, 40, 40) if on else (120, 20, 20), sw=0)
    ltr(img, X + w / 4, Y - h / 2, "14", int(54 * S), (60, 255, 90), sw=0)

JERSEY = None
def frame(tt):
    sh = shot_at(tt); set_ = sh["set"]
    if set_ == "title": return finish(title_card(tt, sh, SERIES, EPT), tt)
    if set_ == "tbc": return finish(title_card(tt, sh, "يتبع...", "الحلقة 4: قهوة الشارع"), tt)
    if set_ == "clock":
        u = kk(tt, sh["start"], sh["end"])
        fr = bg_crop(CROWD[0], (1100, 280, 2.6)).resize((W, H)).filter(ImageFilter.GaussianBlur(10))
        fr = ImageEnhance.Brightness(fr).enhance(0.5)
        sec = 3598 + int(u * 2.9); sec = min(sec, 3600)
        ltr(fr, W / 2, H / 2, f"{sec // 60:02d}:{sec % 60:02d}", 220, (255, 60, 60) if sec >= 3600 else (255, 255, 255), (0, 0, 0), 8)
        return finish(fr, tt)
    cam = cam_at(sh, tt)
    if sh.get("orbit"):   # fake orbit: lateral slide against the zoom
        u = kk(tt, sh["start"], sh["end"]); cam = (cam[0] + math.sin(u * math.pi) * 120 / cam[2], cam[1], cam[2])
    x0, y0, z = cam
    if set_ == "pitch":
        src = QUIET[int(tt * 4) % 2] if sh.get("quiet") else CROWD[int(tt * 8) % 4]
        img = bg_crop(src, cam)
    else:
        img = bg_crop(_cafe, cam)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0))
    if set_ == "pitch":
        draw_people(lay, set_, tt, cam, sh, players(tt, sh))
        p = P(lay)
        if tt < SHOCK:   # ball in play
            bx = 1000 + math.sin(tt * 1.3) * 300; by = 780 + math.cos(tt * 0.9) * 60
            ball(p, (bx - x0) * z, (by - y0) * z, 13 * z)
        if THROW <= tt < FINAL:   # the thrown jersey
            u = ease(kk(tt, THROW, THROW + 1.2)); jx = lerp(640, 720, u); jy = lerp(700, 960, u) - math.sin(u * math.pi) * 80
            X, Y_ = (jx - x0) * z, (jy - y0) * z; r = 34 * z; ang = u * 2.4
            pts = [(-1, -0.7), (1, -0.7), (1.2, -0.2), (0.7, 0), (0.7, 0.8), (-0.7, 0.8), (-0.7, 0), (-1.2, -0.2)]
            ca, sa_ = math.cos(ang), math.sin(ang)
            p.poly([(X + (px * ca - py * sa_) * r, Y_ + (px * sa_ + py * ca) * r) for px, py in pts], RED_KIT + (255,), INK, 2 * z)
        lay = tint_layer(lay, (230, 228, 245))
    else:
        mood = "sad" if sh.get("sad") else "flat"
        ppl = [A_(w_, (x_, y_, s_), look=0 if i % 2 else 1, expr=mood, arms="hips" if i % 2 else "down") for i, (w_, x_, y_, s_) in enumerate(PATRONS)]
        if sh.get("sad"): ppl[2]["arms"] = "point"
        draw_people(lay, set_, tt, cam, sh, ppl)
        lay = tint_layer(lay, (255, 238, 210))
        if sh.get("sad") and tt >= TVOFF: feed = Image.new("RGB", (TV[2] - TV[0], TV[3] - TV[1]), (8, 8, 10))
        else:
            feed = bg_crop(CROWD[int(tt * 8) % 4], (700, 300, 2.0)).resize((TV[2] - TV[0], TV[3] - TV[1]))
            ltr(feed, 70, 20, "0 - 0", 26, (255, 214, 90), sw=2)
        full = Image.new("RGB", (W, H)); full.paste(feed, (TV[0], TV[1]))
        img.paste(bg_crop(full, cam, False), (0, 0), bg_crop(TVMASK.convert("RGB"), cam, False).convert("L"))
    img.paste(lay, (0, 0), lay)
    if sh.get("board"): board(img, cam, tt)
    fr = img.resize((W, H), Image.LANCZOS)
    if sh.get("slow"): fr = ImageEnhance.Color(fr).enhance(0.8)
    if sh.get("quiet"): fr = ImageEnhance.Color(fr).enhance(0.75)
    if sh.get("score"):
        d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([40, 36, 720, 104], 14, fill=(15, 15, 25, 220)); d.rectangle([690, 36, 720, 104], fill=RED_KIT + (255,))
        text(fr, 565, 70, "منتخب العمارة", 32, (255, 255, 255), sw=0); ltr(fr, 400, 70, "0 - 0", 40, (255, 214, 90), sw=0)
        text(fr, 225, 70, "فريق الشارع", 32, (255, 255, 255), sw=0)
        m = 52 + int((tt - WIDE) * 0.8) if tt < BOARD else (60 if tt < FINAL else 90)
        ltr(fr, 790, 70, f"{min(m, 90):02d}:{int(tt * 13) % 60:02d}", 30, (255, 255, 255), sw=2)
    return finish(fr, tt)

def build_audio(path):
    buf = np.zeros(int(TOTAL * SR) + SR * 3, dtype=np.float32)
    for t0, nme, g in sfx:
        if nme in SFXF: mix_into(buf, SFXF[nme], t0, g)
    r = np.random.default_rng(9)
    n = int(TOTAL * SR); bed = lowpass(r.normal(0, 1, n).astype(np.float32), 600) * 0.05
    e = np.ones(n, np.float32); e[int(SILENT[0] * SR):] = 0.35
    mix_into(buf, bed * e, 0, 1.0)
    for i in range(3):   # clock ticks
        ts = np.arange(int(SR * 0.08)) / SR
        mix_into(buf, np.sin(2 * np.pi * 1800 * ts) * np.exp(-ts * 60) * 0.5, CLOCK[0] + 0.3 + i * 0.6, 1.0)
    for t_ in (BOARD + 0.2, SHOCK + 0.1):
        ts = np.arange(int(SR * 1.4)) / SR
        mix_into(buf, (np.sin(2 * np.pi * 55 * ts) + 0.5 * np.sin(2 * np.pi * 82 * ts)) * np.exp(-ts * 2.5) * 0.45, t_, 1.0)
    # sad wind
    ts = np.arange(int((FINAL - SILENT[0]) * SR)); wind = lowpass(r.normal(0, 1, len(ts)).astype(np.float32), 300) * 0.06
    mix_into(buf, wind, SILENT[0], 1.0)
    mix_lines(buf)
    write_wav(buf[:int(TOTAL * SR)], path)

if __name__ == "__main__": main("p3")
