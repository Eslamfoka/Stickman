import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
EPT = "الحلقة 4: قهوة الشارع"
SUB = {"P401": "أهلاً بيكم في قهوة الشارع!... معانا النهارده الباشا... وعبده.",
       "P406": "يا باشا... إزاي مدرب يعمل كده في نجم الفريق؟",
       "P402": "الكابتن لازم يعتذر... الكورة أخلاق قبل ما تبقى أهداف.",
       "P407": "وانت يا عبده... رأيك إيه؟",
       "P403": "وأنا رأيي... إن البسكوت ده حلو أوي.",
       "P408": "يا عبده!... بنتكلم في الكورة!",
       "P409": "آه... لازم يعتذر... وهات بسكوتة كمان.",
       "P404": "ونروح لطنط سوسن بآخر الأخبار!",
       "P405": "عاجل!... ألف كومنت بيقول: الكابتن يعتذر!"}
WHO = {"P401": "fahmy", "P406": "fahmy", "P402": "pasha", "P407": "fahmy", "P403": "abdo", "P408": "fahmy",
       "P409": "abdo", "P404": "fahmy", "P405": "sawsan"}
EXPR = {"P401": "happy", "P406": "flat", "P402": "smug", "P407": "happy", "P403": "happy", "P408": "angry",
        "P409": "happy", "P404": "happy", "P405": "happy"}
ARMS = {"P401": "up", "P406": "point", "P402": "talk", "P407": "point", "P408": "scared", "P404": "point", "P405": "talk"}
load_lines(list(SUB)); load_sfx(["crowd", "whoosh", "switch", "stinger", "kick"])

_st = _ld("bg/studio.png"); _cafe = _ld("bg/cafe.png"); _pt = _ld("bg/pitch.png")
TV = (928, 28, 1307, 244)
_ca = np.asarray(_cafe).astype(np.int16)
TVMASK = Image.fromarray((((_ca[..., 1] > 140) & (_ca[..., 0] < 140) & (_ca[..., 2] < 150)) * 255).astype(np.uint8))
RNG = np.random.default_rng(12)
def rnd_col(): return tuple(int(v) for v in RNG.integers(40, 235, 3))
PATRONS = [(extra("roshdy", rnd_col(), rnd_col()), 520, 1000, 1.7), (extra("fahmy", rnd_col(), rnd_col()), 860, 960, 1.45),
           (extra("abdo", rnd_col(), rnd_col()), 1240, 990, 1.6), (extra("nana", rnd_col(), rnd_col()), 1560, 1010, 1.7),
           (extra("roshdy", rnd_col(), rnd_col()), 230, 1040, 1.95)]
TABLE = (731, 702, 1181, 925)          # marble table in front of the host
HOST = (940, 800, 1.45); PASHA = (565, 905, 1.5); ABDO = (1345, 905, 1.42)

def CU(who, pos, z=2.2, dx=0):
    x, y, s = pos; S = s * CH[who]["scale"]
    hy = y - 190 * S
    return (x + dx, hy + H / (2 * z) - 1.45 * 46 * S - 25, z)

t = 0.0
fx(0, "stinger", 0.9); fx(0.1, "crowd", 0.35)
shot("logo", 0, 2.6, None); t = 2.6                                   # show ident
shot("title", t, t + 2.0, None, tin="fade"); fx(t, "whoosh", 0.5); t += 2.0
s = t; fx(t, "crowd", 0.45); t = say(t + 0.9, "P401") + 0.3; OPEN = s     # crane down onto the set (applause)
shot("studio", s, t, (960, 420, 1.0), (950, 600, 1.22), tin="fade", names=True)
s = t; t = say(t + 0.1, "P406") + 0.15
shot("studio", s, t, (740, 660, 1.6), (760, 660, 1.75), tin="whipl")   # two-shot host -> Pasha
s = t; t = say(t + 0.25, "P402") + 0.4; PUFF = s
shot("studio", s, t, CU("pasha", PASHA, 2.3), CU("pasha", PASHA, 2.7), tin="whipl", smoke=True)
s = t; t = say(t + 0.1, "P407") + 0.1; TO_ABDO = s
shot("studio", s, t, (1150, 660, 1.6), (1130, 660, 1.75), tin="whip")
s = t; t = say(t + 0.4, "P403") + 0.35; MUNCH = s
shot("studio", s, t, CU("abdo", ABDO, 2.2), CU("abdo", ABDO, 2.6), tin="whip", crumbs=True)
s = t; t = say(t + 0.05, "P408") + 0.15; SNAP = s; shakes.append((s + 0.15, 9))
shot("studio", s, t, CU("fahmy", HOST, 1.8), CU("fahmy", HOST, 2.6), ease="crash", tin="zoom")
s = t; t = say(t + 0.3, "P409") + 0.5; NOD = s
shot("studio", s, t, (1140, 640, 1.45), CU("abdo", ABDO, 2.0), tin="whip", crumbs=True)
s = t; t = say(t + 0.1, "P404") + 0.2; TO_CAM = s
shot("studio", s, t, CU("fahmy", HOST, 1.7), CU("fahmy", HOST, 2.1), tin="whipl", oncam=True)
s = t; fx(s, "switch", 0.8); t = say(t + 0.35, "P405") + 0.6; LIVE1 = s
shot("live", s, t, (960, 450, 1.5), (960, 450, 1.6), tin="flash")
CAFE = (t, t + 3.4); fx(t, "crowd", 0.25)
shot("cafe", t, CAFE[1], (960, 600, 1.05), (960, 540, 1.2), tin="whip"); t = CAFE[1]
shot("tbc", t, t + 2.6, None, tin="fade"); t += 2.6
TOTAL = t

def people_studio(tt, sh):
    f = A_("fahmy", HOST, look=0, held="nbpen", arms="hold", expr="happy", noshadow=True)
    if tt >= T("P406") - 0.1: f["look"] = -1
    if tt >= TO_ABDO: f["look"] = 1
    if tt >= TO_CAM: f["look"] = 0
    if SNAP <= tt < NOD: f["expr"] = "angry"; f["held"] = None; f["arms"] = "scared"
    if T("P402") <= tt < TO_ABDO: f["expr"] = "flat"
    pa = A_("pasha", PASHA, look=1, expr="smug", arms="hips")
    if MUNCH <= tt < TO_CAM: pa["look"] = 1; pa["expr"] = "flat"
    ab = A_("abdo", ABDO, look=-1, expr="happy", arms="hold", held="sweet")
    if tt < TO_ABDO: ab["expr"] = "neutral"
    if T("P402") <= tt < TO_ABDO: ab["look"] = 1     # busy with the biscuit plate while Pasha talks
    if SNAP <= tt < NOD: ab["expr"] = "shock"
    return f, pa, ab

def smoke(fr, tt, cam, pos, t0):
    x0, y0, z = cam; x, y, s = pos; S = s * CH["pasha"]["scale"]
    hy = y - 190 * S; cx = x + (30 + 17) * S; cy = hy + 27 * S
    d = ImageDraw.Draw(fr, "RGBA")
    for i in range(7):
        u = ((tt - t0) * 0.45 + i / 7) % 1
        X = (cx + math.sin(u * 6 + i) * 14 * S + u * 20 * S - x0) * z; Y = (cy - u * 120 * S - y0) * z
        r = (5 + 16 * u) * S * z
        d.ellipse([X - r, Y - r, X + r, Y + r], fill=(220, 220, 225, int(110 * (1 - u))))

def crumbs(fr, tt, cam, pos, t0):
    x0, y0, z = cam; x, y, s = pos; S = s * CH["abdo"]["scale"]
    hy = y - 190 * S; mx, my = x - 6 * S, hy + 34 * S
    d = ImageDraw.Draw(fr, "RGBA")
    for i in range(10):
        u = ((tt - t0) * 1.3 + i / 10) % 1
        X = (mx + (i - 5) * 4 * S + math.sin(i * 3.1) * 18 * S * u - x0) * z; Y = (my + u * u * 160 * S - y0) * z
        r = 2.5 * S * z
        d.ellipse([X - r, Y - r, X + r, Y + r], fill=(205, 150, 70, int(230 * (1 - u))))

def studio_still():
    """a clean studio feed for the cafe TV (host + guests, no moves)"""
    cam = (220, 220, 1.3)
    img = bg_crop(_st, cam, False); lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0))
    draw_people(lay, "studio", -1, cam, {}, [A_("pasha", PASHA, look=1, expr="smug", arms="hips"),
                                             A_("abdo", ABDO, look=-1, expr="happy", arms="hold", held="sweet"),
                                             A_("fahmy", HOST, look=0, held="nbpen", arms="hold", expr="happy", noshadow=True)])
    img.paste(tint_layer(lay, (255, 230, 200)), (0, 0), tint_layer(lay, (255, 230, 200)))
    return img.resize((TV[2] - TV[0], TV[3] - TV[1]), Image.LANCZOS)
_FEED = None

def logo(tt, sh):
    u = tt - sh["start"]; fr = bg_crop(_st, (560, 300, 1.6), False).resize((W, H)).filter(ImageFilter.GaussianBlur(18))
    fr = ImageEnhance.Brightness(fr).enhance(0.45)
    d = ImageDraw.Draw(fr, "RGBA")
    k = ease(min(1, u / 0.6)); sc = 0.6 + 0.4 * k + 0.03 * math.sin(u * 3)
    w_, h_ = 760 * sc, 260 * sc
    d.rounded_rectangle([W / 2 - w_ / 2, H / 2 - h_ / 2, W / 2 + w_ / 2, H / 2 + h_ / 2], int(40 * sc), fill=(120, 60, 25, int(235 * k)),
                        outline=(255, 205, 110, int(255 * k)), width=max(2, int(8 * sc)))
    text(fr, W / 2, H / 2 - 20 * sc, "قهوة الشارع", int(130 * sc), (255, 225, 150), (60, 20, 5), 6)
    text(fr, W / 2, H / 2 + 85 * sc, "برنامج الكورة الشعبي", int(44 * sc), (255, 255, 255), (60, 20, 5), 3)
    for i in range(3):   # steam from a little cup icon
        v = (u * 0.8 + i / 3) % 1
        x = W / 2 + w_ / 2 - 70 * sc + math.sin(v * 7 + i) * 10; y = H / 2 - h_ / 2 - 10 - v * 120
        d.ellipse([x - 14, y - 14, x + 14, y + 14], fill=(255, 255, 255, int(120 * (1 - v) * k)))
    if u < 0.25: fr = Image.blend(fr, Image.new("RGB", fr.size, (255, 255, 255)), 0.85 * (1 - u / 0.25))
    return fr

def frame(tt):
    global _FEED
    sh = shot_at(tt); set_ = sh["set"]
    if set_ == "logo": return finish(logo(tt, sh), tt)
    if set_ == "title": return finish(title_card(tt, sh, SERIES, EPT), tt)
    if set_ == "tbc": return finish(title_card(tt, sh, "يتبع...", "الحلقة 5: الصلح"), tt)
    cam = cam_at(sh, tt); x0, y0, z = cam
    if set_ == "studio": img = bg_crop(_st, cam)
    elif set_ == "cafe": img = bg_crop(_cafe, cam)
    else: img = bg_crop(_pt, (600, 0, 1.5)).filter(ImageFilter.GaussianBlur(8 * SS))
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0))
    if set_ == "studio":
        f, pa, ab = people_studio(tt, sh)
        draw_people(lay, set_, tt, cam, sh, [f])
        lay = tint_layer(lay, (255, 230, 200)); img.paste(lay, (0, 0), lay)
        # marble table in front of the host
        bx0 = int((TABLE[0] - x0) * z * SS); by0 = int((TABLE[1] - y0) * z * SS); bx1 = int((TABLE[2] - x0) * z * SS); by1 = int((TABLE[3] - y0) * z * SS)
        bgc = bg_crop(_st, cam); bx0, by0 = max(0, bx0), max(0, by0); bx1, by1 = min(SSW, bx1), min(SSH, by1)
        if bx1 > bx0 and by1 > by0: img.paste(bgc.crop((bx0, by0, bx1, by1)), (bx0, by0))
        lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0))
        draw_people(lay, set_, tt, cam, sh, [pa, ab])
        lay = tint_layer(lay, (255, 230, 200))
    elif set_ == "cafe":
        ppl = []
        for i, (w_, x_, y_, s_) in enumerate(PATRONS):
            a = A_(w_, (x_, y_, s_), look=0 if i % 2 else 1, expr="flat" if i % 2 else "angry", arms="hips" if i % 3 == 0 else "down")
            a["lift"] = abs(math.sin((tt - CAFE[0]) * 5 + i)) * 10 * (1 if tt > CAFE[0] + 0.6 else 0)   # nodding along
            ppl.append(a)
        draw_people(lay, set_, tt, cam, sh, ppl)
        lay = tint_layer(lay, (255, 238, 210))
        if _FEED is None: _FEED = studio_still()
        feed = _FEED.copy(); fd = ImageDraw.Draw(feed); fd.rectangle([0, feed.size[1] - 40, feed.size[0], feed.size[1]], fill=(200, 20, 30))
        text(feed, feed.size[0] / 2, feed.size[1] - 20, "الكل: الكابتن لازم يعتذر!", 26, (255, 255, 255), sw=0)
        full = Image.new("RGB", (W, H)); full.paste(feed, (TV[0], TV[1]))
        img.paste(bg_crop(full, cam, False), (0, 0), bg_crop(TVMASK.convert("RGB"), cam, False).convert("L"))
    elif set_ == "live":
        draw_people(lay, set_, tt, cam, sh, [A_("sawsan", (960, 760, 1.45), held="phone", arms="hold", expr="happy")])
        lay = tint_layer(lay, (255, 240, 220))
    img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    if set_ == "studio":
        if sh.get("smoke"): smoke(fr, tt, cam, PASHA, sh["start"])
        if sh.get("crumbs") and line_at(tt)[0] in ("P403", "P409"): crumbs(fr, tt, cam, ABDO, sh["start"])
        d = ImageDraw.Draw(fr, "RGBA")
        d.rounded_rectangle([W - 380, 40, W - 40, 100], 12, fill=(120, 60, 25, 235), outline=(255, 205, 110, 255), width=3)
        text(fr, W - 210, 70, "قهوة الشارع • مباشر", 30, (255, 230, 160), sw=0)
        if sh.get("oncam") or int(tt * 2) % 2 == 0: d.ellipse([60, 52, 84, 76], fill=(230, 30, 40, 255))
        # lower thirds slide in on the opening
        if sh.get("names"):
            for i, (nm, rl, t0) in enumerate((("الباشا", "محلل كروي", OPEN + 2.6), ("عبده", "ضيف دائم", OPEN + 3.4))):
                k = ease(kk(tt, t0, t0 + 0.35)) * (1 - ease(kk(tt, sh["end"] - 0.4, sh["end"])))
                if k <= 0: continue
                x = (-260 + 540 * k) if i == 0 else (W + 260 - 540 * k)
                y = 800
                d.rectangle([x - 230, y - 44, x + 230, y + 44], fill=(120, 60, 25, 235))
                d.rectangle([x - 230, y + 44, x + 230, y + 70], fill=(255, 205, 110, 235))
                text(fr, x, y, nm, 46, (255, 255, 255), sw=0); text(fr, x, y + 57, rl, 24, (60, 20, 5), sw=0)
    if set_ == "live":
        live_ui(fr, tt, LIVE1, "عاجل", ("لازم يعتذر", "شطة نجم الفريق", "اعتذر يا كابتن", "عبده عايز بسكوت", "1000 كومنت!"))
    return finish(fr, tt)

def build_audio(path):
    buf = np.zeros(int(TOTAL * SR) + SR * 3, dtype=np.float32)
    for t0, nme, g in sfx:
        if nme in SFXF: mix_into(buf, SFXF[nme], t0, g)
    r = np.random.default_rng(14)
    n = int(TOTAL * SR); bed = lowpass(r.normal(0, 1, n).astype(np.float32), 400) * 0.025
    mix_into(buf, bed, 0, 1.0)
    ts = np.arange(int(SR * 0.9)) / SR     # comedic "bonk" on Abdo's biscuit answer and on Fahmy's snap
    for t_ in (MUNCH + DUR["P403"] - 0.2, NOD + DUR["P409"] - 0.1):
        mix_into(buf, np.sin(2 * np.pi * (520 - 300 * ts) * ts) * np.exp(-ts * 7) * 0.35, t_, 1.0)
    ts = np.arange(int(SR * 1.0)) / SR
    mix_into(buf, (np.sin(2 * np.pi * 60 * ts) + 0.5 * np.sin(2 * np.pi * 90 * ts)) * np.exp(-ts * 4) * 0.35, SNAP + 0.1, 1.0)
    mix_lines(buf)
    write_wav(buf[:int(TOTAL * SR)], path)

if __name__ == "__main__": main("p4")
