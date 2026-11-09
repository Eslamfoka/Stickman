exec(open("/home/claude/repo/Stickman/trend/01/kit.py").read())
EPT = "الحلقة 1: كاس الشارع"
SUB = {"P100": "جوووون!... منتخب العمارة بيسجّل!",
       "P101": "عاجل يا جماعة!... منتخب العمارة كسب عمارة الجيران تلاتة صفر!",
       "P102": "وكمان كسب فريق الشارع اللي ورا!",
       "P103": "الكاس ده للعمارة كلها!",
       "P104": "الكابتن بندق... أحسن مدرب في الدنيا!"}
WHO = {"P100": "fahmy", "P101": "sawsan", "P102": "sawsan", "P103": "bondo2", "P104": "shatta"}
EXPR = {"P101": "happy", "P102": "happy", "P103": "happy", "P104": "happy"}
ARMS = {"P101": "talk", "P102": "point", "P103": "up", "P104": "up"}
load_lines(list(SUB)); load_sfx(["crowd", "kick", "final", "whoosh", "switch", "stinger"])

# ---------- world (pitch.png → 1920 coords) ----------
GOAL = (1765, 625)
_pitch = _ld("bg/pitch.png"); _cafe = _ld("bg/cafe.png")
TV = (928, 28, 1307, 244)
# extras
RNG = np.random.default_rng(5)
FAN_BASES = ["roshdy", "fahmy", "sawsan", "nana", "tota", "abdo"]
def rnd_col(): return tuple(int(v) for v in RNG.integers(40, 235, 3))
FANS = []   # (who, x, y, s, flag)
for i in range(16):   # bleachers
    x = 650 + i * 30 + RNG.uniform(-8, 8); y = 600 - (i % 3) * 22
    FANS.append((extra(FAN_BASES[i % 6], rnd_col(), rnd_col()), x, y, 0.36, ["eg", "ps", None, None][i % 4]))
for i in range(10):   # left balconies
    x = 70 + (i % 5) * 95; y = 205 + (i // 5) * 120
    FANS.append((extra(FAN_BASES[(i + 2) % 6], rnd_col(), rnd_col()), x, y, 0.26, ["eg", None, "ps"][i % 3]))
for i in range(10):   # right balconies
    x = 1460 + (i % 5) * 92; y = 190 + (i // 5) * 125
    FANS.append((extra(FAN_BASES[(i + 4) % 6], rnd_col(), rnd_col()), x, y, 0.26, ["ps", None, "eg"][i % 3]))

def crowd_bg(var, banner=False):
    img = _pitch.resize((SSW, SSH), Image.BICUBIC)
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    for j, (who, x, y, s, fl) in enumerate(FANS):
        hop = abs(math.sin(var * 1.57 + j)) * 14 * s
        a = A_(who, (x, y - hop, s), arms="up" if (j + var) % 2 else "down", expr="happy", noshadow=True)
        draw_char(p, who, x, y - hop, s, "happy", 0.3 if (j + var) % 3 == 0 else 0, 0, False, a["arms"], var * 0.3, None, 0, None)
        if fl: flag(p, x + 30 * s, y - hop - 60 * s, s * 1.4, fl, var * 0.5, j)
    if banner:
        p.rect(1450, 300, 1890, 360, (250, 250, 245, 255), INK, 3)
        text(lay, 1670 * SS, 330 * SS, "بنحبك يا كابتن بندق ❤", int(34 * SS), (200, 20, 30), sw=0)
    lay = tint_layer(lay, (230, 225, 240), 0.95)
    img.paste(lay, (0, 0), lay); return img
CROWD = [crowd_bg(v) for v in range(4)]
CROWD_B = [crowd_bg(v, True) for v in range(4)]

# cafe TV mask (green screen)
_ca = np.asarray(_cafe).astype(np.int16)
TVMASK = Image.fromarray((((_ca[..., 1] > 140) & (_ca[..., 0] < 140) & (_ca[..., 2] < 150)) * 255).astype(np.uint8))
PATRONS = [(extra("roshdy", rnd_col(), rnd_col()), 520, 1000, 1.7), (extra("fahmy", rnd_col(), rnd_col()), 860, 960, 1.45),
           (extra("abdo", rnd_col(), rnd_col()), 1240, 990, 1.6), (extra("nana", rnd_col(), rnd_col()), 1560, 1010, 1.7),
           (extra("roshdy", rnd_col(), rnd_col()), 230, 1040, 1.95)]

# ---------- timeline ----------
t = 0.0
HOOK = (0, 2.2)
shot("pitch", 0, 2.2, (GOAL[0] - 120, GOAL[1] - 20, 3.0), (GOAL[0] - 80, GOAL[1] - 10, 3.3), hook=True)
fx(0.0, "crowd", 0.35); t = 2.2
shot("title", t, t + 2.0, None); fx(t, "whoosh", 0.5); TITLE = t; t += 2.0
WIDE = (t, t + 3.0); fx(t, "crowd", 0.7); fx(t + 1.0, "switch", 0.3)
shot("pitch", t, WIDE[1], (960, 560, 1.0), (980, 600, 1.15), score=(0, 0)); t = WIDE[1]
RUN = (t, t + 3.4)
shot("pitch", t, RUN[1], (900, 700, 1.5), (1450, 640, 1.8), score=(0, 0)); t = RUN[1]
KICK = t; fx(KICK, "kick", 1.2)
SHOT_ = (t, t + 1.8); fx(t + 0.8, "crowd", 1.0)
shot("pitch", t, SHOT_[1], (1600, 640, 2.2), (GOAL[0] - 40, GOAL[1], 2.8), slow=True, score=(1, 0))
say(t + 0.6, "P100"); t = SHOT_[1]
CEL = (t, t + 1.6)
shot("pitch", t, CEL[1], (1520, 620, 2.2), (1500, 600, 2.4), score=(1, 0)); t = CEL[1]
CAFE1 = (t, t + 2.6); fx(t, "crowd", 0.8)
shot("cafe", t, CAFE1[1], (960, 600, 1.05), (960, 560, 1.15), tvgoal=True); t = CAFE1[1]
s = t; t = say(t + 0.2, "P101") + 0.3
shot("live", s, t, (1450, 300, 2.0), (1450, 300, 2.12)); LIVE1 = s
MONT = (t, t + 4.4); fx(t + 2.2, "kick", 1.0); fx(t + 2.9, "crowd", 0.9)
say(t + 0.3, "P102")
shot("pitch", t, MONT[1], (900, 640, 1.2), (1300, 620, 1.5), score=(1, 0), yellow=True, score2=True); t = MONT[1]
FINAL = t; fx(t, "final", 1.1)
LIFT = (t + 1.0, t + 3.4)
shot("pitch", t, LIFT[1], (700, 700, 1.25), (520, 700, 1.4), fin=True); t = LIFT[1]
CONF0 = t
s = t; t = say(t + 0.2, "P103") + 0.5
shot("pitch", s, t, (420, 640, 1.8), (420, 620, 2.0), fin=True, conf=True)
s = t; t = say(t, "P104") + 0.4
shot("pitch", s, t, (520, 700, 1.9), (520, 700, 2.1), fin=True, conf=True)
BAN = (t, t + 3.0); fx(t, "crowd", 0.8)
shot("pitch", t, BAN[1], (1500, 360, 2.0), (1600, 330, 2.3), fin=True, banner=True, flashes=True); t = BAN[1]
shot("tbc", t, t + 2.6, None); t += 2.6
TOTAL = t

# ---------- actors ----------
def score_bug(fr, a, b, tt, other="عمارة الجيران"):
    d = ImageDraw.Draw(fr, "RGBA")
    d.rounded_rectangle([40, 36, 720, 104], 14, fill=(15, 15, 25, 220))
    d.rectangle([690, 36, 720, 104], fill=RED_KIT + (255,))
    text(fr, 220, 70, "منتخب العمارة", 32, (255, 255, 255), sw=0)
    ltr(fr, 400, 70, f"{a} - {b}", 40, (255, 214, 90), sw=0)
    text(fr, 570, 70, other, 32, (255, 255, 255), sw=0)
    sec = int(tt * 9 + 1500); ltr(fr, 790, 70, f"{(sec // 60) % 90:02d}:{sec % 60:02d}", 30, (255, 255, 255), sw=2)

def players(tt, sh):
    A = []
    other = YELLOW_KIT if sh.get("yellow") else BLUE_KIT
    sl = 0.35 if sh.get("slow") else 1.0
    sha = A_("shatta", (900, 800, 1.15), look=1, kit=RED_KIT, num=10, expr="smug")
    if tt >= RUN[0] and tt < CAFE1[0]:
        walk_to(sha, (900, 800, 1.15), (1500, 690, 0.95), (RUN[0], KICK), tt, 12)
    if SHOT_[0] <= tt < CAFE1[0]: sha["x"], sha["y"], sha["s"] = 1500, 690, 0.95
    if CEL[0] <= tt < CAFE1[0]: sha["arms"] = "up"; sha["expr"] = "happy"; sha["hop"] = True
    kick_on = WIDE[0] <= tt < CAFE1[0]
    if kick_on:
        A.append(sha)
        b1 = A_(extra_cache("b1", "roshdy", other), (1100, 820, 1.2), look=-1, kit=other, num=4)
        if RUN[0] <= tt: walk_to(b1, (1100, 820, 1.2), (1250, 760, 1.05), (RUN[0], RUN[0] + 1.2), tt, 10); b1["expr"] = "shock"
        b2 = A_(extra_cache("b2", "abdo", other), (1350, 760, 1.0), look=-1, kit=other, num=5)
        if RUN[0] + 1.0 <= tt: walk_to(b2, (1350, 760, 1.0), (1420, 720, 0.98), (RUN[0] + 1.0, RUN[0] + 2.2), tt, 10); b2["expr"] = "shock"
        kp = A_(extra_cache("gk", "roshdy", (40, 40, 40)), (1700, 650, 0.85), look=-1, kit=(250, 140, 30), num=1)
        if tt >= KICK: kp["lean"] = 0.9 * ease(kk(tt, KICK + 0.2, KICK + 0.9)); kp["expr"] = "shock"
        r2 = A_(extra_cache("r2", "fahmy", RED_KIT), (700, 860, 1.3), look=1, kit=RED_KIT, num=8)
        r3 = A_("koko", (1150, 900, 1.45), look=1, kit=RED_KIT, num=7)
        if tt >= CEL[0]: r2["arms"] = r3["arms"] = "up"; r2["hop"] = r3["hop"] = True
        A += [b1, b2, kp, r2, r3]
    if MONT[0] <= tt < FINAL:
        u = tt - MONT[0]
        ko = A_("koko", (950, 820, 1.2), look=1, kit=RED_KIT, num=7, expr="happy")
        sh2 = A_("shatta", (1250, 760, 1.05), look=1, kit=RED_KIT, num=10, expr="smug")
        walk_to(sh2, (1250, 760, 1.05), (1480, 690, 0.95), (MONT[0] + 0.9, MONT[0] + 2.2), tt, 12)
        if u > 2.6: sh2["arms"] = "up"; sh2["hop"] = True; ko["arms"] = "up"; ko["hop"] = True
        y1 = A_(extra_cache("y1", "abdo", other), (1150, 860, 1.25), look=-1, kit=other, num=3)
        gk = A_(extra_cache("gk2", "roshdy", other), (1700, 650, 0.85), look=-1, kit=(40, 160, 90), num=1)
        if u > 2.2: gk["lean"] = 0.9; gk["expr"] = "shock"
        A += [ko, sh2, y1, gk]
    if tt >= FINAL:
        bo = A_("bondo2", (420, 960, 1.75), look=1, expr="happy", whistle=True)
        if tt >= LIFT[0]: bo["lift"] = 120 * ease(kk(tt, LIFT[0] + 0.6, LIFT[0] + 1.4)); bo["arms"] = "up"
        if tt >= CONF0: bo["lift"] = 0; bo["trophy"] = True; bo["arms"] = "up"
        team = [("shatta", 10, 600, 1000, 1.85), ("koko", 7, 760, 930, 1.55), (extra_cache("r2", "fahmy", RED_KIT), 8, 230, 980, 1.7),
                (extra_cache("r4", "roshdy", RED_KIT), 9, 900, 880, 1.4)]
        for i, (w_, n_, x_, y_, s_) in enumerate(team):
            a = A_(w_, (x_ + 500, y_ - 120, s_ * 0.8), look=-1, kit=RED_KIT, num=n_, expr="happy", arms="up", ph=i)
            walk_to(a, (x_ + 500, y_ - 120, s_ * 0.8), (x_, y_, s_), (FINAL + 0.1 + i * 0.15, LIFT[0] + 0.6), tt, 12)
            if tt >= LIFT[0] + 0.6: a["hop"] = True
            if tt >= CONF0: a["flag"] = ["eg", "ps", "eg", "ps"][i]
            if w_ == "shatta" and tt >= T("P104"): a["hop"] = False; a["x"] = 560; a["look"] = -1
            A.append(a)
        A.append(bo)
    return A
_XC = {}
def extra_cache(key, base, col):
    if key not in _XC: _XC[key] = extra(base, col, (40, 30, 22))
    return _XC[key]

def ball_pos(tt):
    if WIDE[0] <= tt < RUN[0]: return (930, 800, 1.15)
    if RUN[0] <= tt < KICK:
        k = ease(kk(tt, RUN[0], KICK)); x = lerp(930, 1530, k); y = lerp(800, 690, k); s = lerp(1.15, 0.95, k)
        return (x + math.sin(tt * 20) * 8, y, s)
    if KICK <= tt < SHOT_[1]:
        u = kk(tt, KICK, KICK + 1.2); x = lerp(1530, GOAL[0], u); y = lerp(690, GOAL[1] - 10, u) - math.sin(u * math.pi) * 60
        return (x, y, lerp(0.95, 0.85, u))
    if SHOT_[1] <= tt < CAFE1[0]: return (GOAL[0] + 20, GOAL[1] + 20, 0.85)
    if MONT[0] <= tt < FINAL:
        u = tt - MONT[0]
        if u < 1.0: return (lerp(980, 1260, u), lerp(820, 760, u), 1.1)
        if u < 2.2: k = (u - 1.0) / 1.2; return (lerp(1280, 1500, k), lerp(760, 690, k), 1.0)
        k = min(1, (u - 2.2) / 0.6); return (lerp(1500, GOAL[0], k), lerp(690, GOAL[1], k) - math.sin(k * math.pi) * 40, 0.9)
    return None

def frame(tt):
    sh = shot_at(tt); set_ = sh["set"]
    if set_ == "title": return finish(title_card(tt, sh, SERIES, EPT), tt)
    if set_ == "tbc": return finish(title_card(tt, sh, "يتبع...", "الحلقة 2: المؤتمر الصحفي"), tt)
    cam = cam_at(sh, tt)
    if sh.get("slow"):   # slow-motion feel: less camera drift
        pass
    if set_ in ("pitch", "live"):
        var = int(tt * 8) % 4
        src = (CROWD_B if sh.get("banner") or tt >= FINAL else CROWD)[var]
        img = bg_crop(src, cam, set_ != "live")
        if set_ == "live": img = img.filter(ImageFilter.GaussianBlur(6 * SS))
    elif set_ == "cafe":
        img = bg_crop(_cafe, cam)
    else:
        img = Image.new("RGB", (SSW, SSH))
    x0, y0, z = cam
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0)); p = P(lay)
    people = []
    if set_ == "pitch":
        people = players(tt, sh)
        bp = ball_pos(tt)
        if bp and not sh.get("hook"):
            bx, by, bs = bp; ball(p, (bx - x0) * z, (by - 14 * bs - y0) * z, 14 * bs * z)
        if sh.get("hook"):
            u = kk(tt, 0, 2.0); bx = lerp(GOAL[0] - 260, GOAL[0] - 30, u); by = GOAL[1] - 30 - math.sin(u * 3) * 20
            ball(p, (bx - x0) * z, (by - y0) * z, 18 * z)
    elif set_ == "live":
        people = [A_("sawsan", (1450, 610, 1.45), look=0, held="phone", arms="hold", expr="happy")]
    elif set_ == "cafe":
        for i, (w_, x_, y_, s_) in enumerate(PATRONS):
            a = A_(w_, (x_, y_, s_), look=0 if i % 2 else 1, expr="happy", arms="up", hop=True, ph=i)
            people.append(a)
    draw_people(lay, set_, tt, cam, sh, people)
    tint = (230, 228, 245) if set_ == "pitch" else (255, 238, 210)
    lay = tint_layer(lay, tint, 0.98)
    if set_ == "cafe":   # live TV feed on the green-screen
        feed = bg_crop(CROWD[int(tt * 8) % 4], (1085, 300, 2.3)).resize((TV[2] - TV[0], TV[3] - TV[1]))
        text(feed, feed.size[0] / 2, feed.size[1] * 0.45, "جووووون", 64, (255, 214, 90), (120, 10, 10), 5)
        full = Image.new("RGB", (W, H)); full.paste(feed, (TV[0], TV[1]))
        fullS = bg_crop(full, cam, False); maskS = bg_crop(TVMASK.convert("RGB"), cam, False).convert("L")
        img.paste(fullS, (0, 0), maskS)
    img.paste(lay, (0, 0), lay)
    if sh.get("conf"): confetti(img, tt, CONF0)
    fr = img.resize((W, H), Image.LANCZOS)
    if sh.get("flashes"):
        d = ImageDraw.Draw(fr, "RGBA")
        for i in range(6):
            if (int(tt * 9) + i * 3) % 7 == 0:
                x = (i * 331) % W; y = 120 + (i * 177) % 500
                d.ellipse([x - 40, y - 40, x + 40, y + 40], fill=(255, 255, 255, 180))
    if sh.get("slow"): fr = ImageEnhance.Color(fr).enhance(1.15)
    if "score" in sh and set_ == "pitch":
        a_, b_ = sh["score"]
        if sh.get("score2"): a_, b_ = (1 if tt - MONT[0] > 2.8 else 0), 0
        score_bug(fr, a_, b_, tt, "فريق الشارع" if sh.get("yellow") else "عمارة الجيران")
    if set_ == "live": live_ui(fr, tt, LIVE1, "عاجل", ("منتخب العمارة يا رجالة", "تلاتة صفر!!", "الكابتن بندق ❤", "إحنا الأبطال"))
    if sh.get("hook"):
        fr = ImageEnhance.Contrast(fr).enhance(1.15)
    return finish(fr, tt)

def build_audio(path):
    buf = np.zeros(int(TOTAL * SR) + SR * 3, dtype=np.float32)
    for t0, nme, g in sfx:
        if nme in SFXF: mix_into(buf, SFXF[nme], t0, g)
    r = np.random.default_rng(9)   # stadium bed
    n = int(TOTAL * SR); bed = lowpass(r.normal(0, 1, n).astype(np.float32), 700) * 0.05
    e = np.ones(n, np.float32)
    for a_, b_ in ((CAFE1[0], CAFE1[1]),): e[int(a_ * SR):int(b_ * SR)] = 0.6
    mix_into(buf, bed * e, 0, 1.0)
    # upbeat drum loop under the montage & celebration
    for a_, b_ in ((WIDE[0], CAFE1[0]), (MONT[0], BAN[1])):
        tb = a_
        while tb < b_:
            ts = np.arange(int(SR * 0.18)) / SR
            mix_into(buf, np.sin(2 * np.pi * 70 * ts) * np.exp(-ts * 22) * 0.35, tb, 1.0)
            mix_into(buf, r.normal(0, 1, len(ts)).astype(np.float32) * np.exp(-ts * 40) * 0.08, tb + 0.25, 1.0)
            tb += 0.5
    mix_lines(buf)
    write_wav(buf[:int(TOTAL * SR)], path)

if __name__ == "__main__": main("p1")
