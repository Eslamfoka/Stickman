import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
EPT = "الحلقة 2: المؤتمر الصحفي"
SUB = {"P200": "أهلاً بيكم في المؤتمر الصحفي... أول سؤال.",
       "P205": "كابتن... إحساسك إيه بعد الكاس؟",
       "P206": "إحساس تاريخي... أنا عملت اللي محدش عمله!",
       "P201": "كابتن بندق... ليه ما أخدتش كوكو في الماتش؟",
       "P202": "كوكو؟... ده لاعب خلصان!",
       "P203": "يا نهار أبيض!... كوكو صاحبي!",
       "P207": "يعني حضرتك شايف إن كوكو خلص؟",
       "P208": "السؤال اللي بعده!",
       "P204": "عاجل!... السوشيال ميديا مقلوبة على الكابتن!"}
WHO = {"P200": "zalata", "P205": "fahmy", "P206": "bondo2", "P201": "tota", "P202": "bondo2", "P203": "shatta",
       "P207": "tota", "P208": "bondo2", "P204": "sawsan"}
EXPR = {"P200": "flat", "P205": "happy", "P206": "smug", "P201": "flat", "P202": "smug", "P203": "shock", "P207": "flat",
        "P208": "angry", "P204": "happy"}
ARMS = {"P205": "point", "P206": "hips", "P201": "point", "P202": "talk", "P203": "scared", "P207": "point", "P208": "point", "P204": "talk"}
load_lines(list(SUB)); load_sfx(["press", "gasp", "whoosh", "switch", "stinger", "crowd"])

_conf = _ld("bg/conference.png"); _cafe = _ld("bg/cafe.png"); _pt = _ld("bg/pitch.png")
TV = (928, 28, 1307, 244)
_ca = np.asarray(_cafe).astype(np.int16)
TVMASK = Image.fromarray((((_ca[..., 1] > 140) & (_ca[..., 0] < 140) & (_ca[..., 2] < 150)) * 255).astype(np.uint8))
RNG = np.random.default_rng(8)
def rnd_col(): return tuple(int(v) for v in RNG.integers(40, 235, 3))
PATRONS = [(extra("roshdy", rnd_col(), rnd_col()), 520, 1000, 1.7), (extra("fahmy", rnd_col(), rnd_col()), 860, 960, 1.45),
           (extra("abdo", rnd_col(), rnd_col()), 1240, 990, 1.6), (extra("nana", rnd_col(), rnd_col()), 1560, 1010, 1.7),
           (extra("roshdy", rnd_col(), rnd_col()), 230, 1040, 1.95)]
# journalists (standing along the sides and behind the last row)
JBASE = ["roshdy", "sawsan", "fahmy", "nana", "abdo"]
JOUR = []
for i, (x, y, s) in enumerate([(330, 930, 1.7), (470, 980, 1.85), (220, 1030, 1.95), (1560, 940, 1.7), (1700, 990, 1.85),
                               (1450, 1030, 1.95), (620, 700, 1.0), (760, 690, 0.95), (1180, 690, 0.95), (1320, 700, 1.0)]):
    JOUR.append((extra(JBASE[i % 5], rnd_col(), rnd_col()), x, y, s, ["phone", "paper", None][i % 3]))
TABLE = (469, 375, 1457, 560)   # table + cloth (occludes the speakers' lower bodies)
SEAT = {"zalata": (703, 480, 1.2), "bondo2": (966, 480, 1.25), "shatta": (1209, 480, 1.2)}
AISLE_F = (990, 870, 1.45); AISLE_T = (1010, 900, 1.5)

def CU(who, pos, z=2.2):
    x, y, s = pos; S = s * CH[who]["scale"]
    if who == "tota": z *= 1.25
    hy = y - 190 * S
    return (x, hy + H / (2 * z) - 1.45 * 46 * S - 25, z)

t = 0.0
fx(0, "press", 0.9)
shot("conf", 0, 2.4, (960, 600, 1.35), (960, 560, 1.2), tin="flash", flashes=True); t = 2.4
shot("title", t, t + 2.0, None, tin="fade"); fx(t, "whoosh", 0.5); TITLE = t; t += 2.0
WIDE = (t, t + 3.0); fx(t, "press", 0.6)
shot("conf", t, WIDE[1], (960, 560, 1.0), (960, 520, 1.12), tin="fade", flashes=True); t = WIDE[1]
s = t; t = say(t, "P200") + 0.2
shot("conf", s, t, CU("zalata", SEAT["zalata"], 2.4), CU("zalata", SEAT["zalata"], 2.6), tin="whipl")
s = t; t = say(t + 0.1, "P205") + 0.1
shot("conf", s, t, CU("fahmy", AISLE_F, 1.9), CU("fahmy", AISLE_F, 2.1), tin="whip")
s = t; t = say(t, "P206") + 0.3
shot("conf", s, t, CU("bondo2", SEAT["bondo2"], 2.2), CU("bondo2", SEAT["bondo2"], 2.5), flashes=True, low=True)
s = t; t = say(t + 0.3, "P201") + 0.2; TOTA_UP = s
shot("conf", s, t, (1000, 640, 1.3), CU("tota", AISLE_T, 2.1), tin="whip")
s = t; t = say(t + 0.15, "P202") + 0.1; BOMB = s
shot("conf", s, t, CU("bondo2", SEAT["bondo2"], 2.0), CU("bondo2", SEAT["bondo2"], 3.0), ease="crash", tin="zoom")
GASP = t; fx(t, "gasp", 1.1); fx(t + 0.2, "press", 1.0)
shot("conf", t, t + 2.2, (960, 600, 1.15), (960, 560, 1.25), flashes=True, react=True); t += 2.2
CAFE = (t, t + 2.4)
shot("cafe", t, CAFE[1], (960, 600, 1.05), (960, 560, 1.15), tin="whip"); t = CAFE[1]
s = t; t = say(t + 0.1, "P203") + 0.3; SHAT = s
shot("conf", s, t, CU("shatta", SEAT["shatta"], 2.2), CU("shatta", SEAT["shatta"], 2.5), tin="whipl")
s = t; t = say(t + 0.1, "P207") + 0.2
shot("conf", s, t, CU("tota", AISLE_T, 2.0), CU("tota", AISLE_T, 2.3))
s = t; t = say(t + 0.1, "P208") + 0.2; SNAP = s; shakes.append((s + 0.2, 10))
shot("conf", s, t, CU("bondo2", SEAT["bondo2"], 2.4), CU("bondo2", SEAT["bondo2"], 2.0), tin="zoom")
LEAVE = (t, t + 2.6); fx(t + 0.2, "press", 1.0)
shot("conf", t, LEAVE[1], (960, 520, 1.3), (900, 500, 1.15), flashes=True); t = LEAVE[1]
s = t; t = say(t + 0.2, "P204") + 0.5; LIVE1 = s
shot("live", s, t, (960, 450, 1.5), (960, 450, 1.6), tin="flash")
shot("tbc", t, t + 2.6, None, tin="fade"); t += 2.6
TOTAL = t

def people_conf(tt, sh):
    A = []
    for i, (w_, x, y, s, held) in enumerate(JOUR):
        a = A_(w_, (x, y, s), look=0, held=held, arms="hold" if held else "down", expr="neutral", lockarms=True)
        if tt >= GASP: a["expr"] = "shock"
        if sh.get("react") and i % 2: a["arms"] = "scared"; a["held"] = None
        A.append(a)
    f = A_("fahmy", AISLE_F, look=0, held="nbpen", arms="hold", expr="happy")
    if tt >= GASP: f["expr"] = "shock"
    to = A_("tota", AISLE_T, look=0, held="phone", arms="hold", expr="flat")
    if TOTA_UP <= tt < BOMB + 0.5: to["arms"] = "up"; to["held"] = None
    A += [f, to]
    # speakers (behind the table)
    z_ = A_("zalata", SEAT["zalata"], look=1, held="nbpen", arms="hold", expr="flat", noshadow=True)
    b = A_("bondo2", SEAT["bondo2"], look=0, expr="smug", arms="down", noshadow=True)
    if tt >= SNAP: b["expr"] = "angry"
    sa = A_("shatta", SEAT["shatta"], look=-1, expr="happy", noshadow=True, kit=RED_KIT, num=10)
    if tt >= BOMB + 0.6: sa["expr"] = "shock"
    if tt >= SHAT + DUR["P203"]: sa["expr"] = "angry"; sa["look"] = 1
    if tt >= LEAVE[0]:
        k = walk_to(b, SEAT["bondo2"], (380, 470, 1.2), (LEAVE[0] + 0.2, LEAVE[1]), tt, 8); b["look"] = -1
        b["lift"] = 40 * ease(kk(tt, LEAVE[0], LEAVE[0] + 0.3))
        if k >= 1: b = None
    A += [z_, sa] + ([b] if b else [])
    return A

def frame(tt):
    sh = shot_at(tt); set_ = sh["set"]
    if set_ == "title": return finish(title_card(tt, sh, SERIES, EPT), tt)
    if set_ == "tbc": return finish(title_card(tt, sh, "يتبع...", "الحلقة 3: الدقيقة 60"), tt)
    cam = cam_at(sh, tt); x0, y0, z = cam
    if set_ == "conf": img = bg_crop(_conf, cam)
    elif set_ == "cafe": img = bg_crop(_cafe, cam)
    else: img = bg_crop(_ld("bg/pitch.png") if "_pt" not in globals() else _pt, (600, 0, 1.5)).filter(ImageFilter.GaussianBlur(8 * SS))
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0))
    if set_ == "conf":
        ppl = people_conf(tt, sh)
        back = [a for a in ppl if a["who"] in ("zalata", "bondo2", "shatta")]
        front = [a for a in ppl if a not in back]
        draw_people(lay, set_, tt, cam, sh, back)
        lay = tint_layer(lay, (250, 245, 240))
        img.paste(lay, (0, 0), lay)
        # the table + cloth in front of the speakers (re-paste the background there)
        bx0 = int((TABLE[0] - x0) * z * SS); by0 = int((TABLE[1] - y0) * z * SS); bx1 = int((TABLE[2] - x0) * z * SS); by1 = int((TABLE[3] - y0) * z * SS)
        bgc = bg_crop(_conf, cam)
        bx0, by0 = max(0, bx0), max(0, by0); bx1, by1 = min(SSW, bx1), min(SSH, by1)
        if bx1 > bx0 and by1 > by0: img.paste(bgc.crop((bx0, by0, bx1, by1)), (bx0, by0))
        # microphones on top of the table
        p = P(img)
        for mx in (690, 940, 990, 1190, 1230):
            X = (mx - x0) * z; Y = (378 - y0) * z
            p.line([(X, Y), (X - 6 * z, Y - 40 * z)], (30, 30, 30, 255), 3 * z); p.ell(X - 6 * z, Y - 44 * z, 7 * z, 9 * z, (50, 50, 55, 255), INK, 1.5 * z)
        lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0))
        draw_people(lay, set_, tt, cam, sh, front)
        lay = tint_layer(lay, (250, 245, 240))
    elif set_ == "cafe":
        ppl = [A_(w_, (x_, y_, s_), look=0 if i % 2 else 1, expr="shock", arms="scared" if i % 2 else "down") for i, (w_, x_, y_, s_) in enumerate(PATRONS)]
        draw_people(lay, set_, tt, cam, sh, ppl)
        lay = tint_layer(lay, (255, 238, 210))
        feed = bg_crop(_conf, (700, 200, 2.6)).resize((TV[2] - TV[0], TV[3] - TV[1]))
        fd = ImageDraw.Draw(feed); fd.rectangle([0, feed.size[1] - 40, feed.size[0], feed.size[1]], fill=(200, 20, 30))
        text(feed, feed.size[0] / 2, feed.size[1] - 20, "الكابتن: كوكو خلصان!", 26, (255, 255, 255), sw=0)
        full = Image.new("RGB", (W, H)); full.paste(feed, (TV[0], TV[1]))
        img.paste(bg_crop(full, cam, False), (0, 0), bg_crop(TVMASK.convert("RGB"), cam, False).convert("L"))
    elif set_ == "live":
        draw_people(lay, set_, tt, cam, sh, [A_("sawsan", (960, 760, 1.45), held="phone", arms="hold", expr="happy")])
        lay = tint_layer(lay, (255, 240, 220))
    img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    if sh.get("flashes"):
        d = ImageDraw.Draw(fr, "RGBA")
        for i in range(8):
            if (int(tt * 11) + i * 3) % 6 == 0:
                x = 100 + (i * 241) % (W - 200); y = 500 + (i * 137) % 450
                d.ellipse([x - 60, y - 60, x + 60, y + 60], fill=(255, 255, 255, 170))
    if set_ == "conf":   # broadcast bug
        d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([W - 330, 40, W - 40, 100], 12, fill=(200, 20, 30, 230))
        text(fr, W - 185, 70, "مباشر • المؤتمر الصحفي", 28, (255, 255, 255), sw=0)
    if set_ == "live": live_ui(fr, tt, LIVE1, "عاجل", ("الكابتن غلطان", "كوكو أسطورة", "ده كلام يتقال؟!", "اعتذر يا كابتن"))
    return finish(fr, tt)

def build_audio(path):
    buf = np.zeros(int(TOTAL * SR) + SR * 3, dtype=np.float32)
    for t0, nme, g in sfx:
        if nme in SFXF: mix_into(buf, SFXF[nme], t0, g)
    r = np.random.default_rng(9)
    n = int(TOTAL * SR); bed = lowpass(r.normal(0, 1, n).astype(np.float32), 500) * 0.035
    mix_into(buf, bed, 0, 1.0)
    for t_ in (BOMB + DUR["P202"], SNAP + 0.1):   # dramatic hits
        ts = np.arange(int(SR * 1.2)) / SR
        mix_into(buf, (np.sin(2 * np.pi * 55 * ts) + 0.5 * np.sin(2 * np.pi * 82 * ts)) * np.exp(-ts * 3) * 0.4, t_, 1.0)
    mix_lines(buf)
    write_wav(buf[:int(TOTAL * SR)], path)

if __name__ == "__main__": main("p2")
