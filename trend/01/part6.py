exec(open("/home/claude/repo/Stickman/trend/01/kit.py").read())
EPT = "الحلقة 6: الإقالة"
SUB = {"P601": "عاجل جدًا!... رسمي: إقالة الكابتن بندق!",
       "P602": "أنا؟!... طب...",
       "P603": "حد... عايز مدرب تاريخي؟",
       "P604": "وانتو رأيكو إيه؟... اكتبوا في الكومنتات!"}
WHO = {"P601": "sawsan", "P602": "bondo2", "P603": "bondo2", "P604": "sawsan"}
EXPR = {"P601": "happy", "P602": [(0, "shock"), (0.55, "sad")], "P603": "sleepy", "P604": "happy"}
ARMS = {"P601": "talk", "P604": "point"}
load_lines(list(SUB)); load_sfx(["whoosh", "switch", "stinger", "kick", "gasp", "crowd"])

_room = _ld("bg/room.png"); _cafe = _ld("bg/cafe.png"); _nb = _ld("bg/neighbors.png")
TV = (928, 28, 1307, 244)
_ca = np.asarray(_cafe).astype(np.int16)
TVMASK = Image.fromarray((((_ca[..., 1] > 140) & (_ca[..., 0] < 140) & (_ca[..., 2] < 150)) * 255).astype(np.uint8))
RNG = np.random.default_rng(16)
def rnd_col(): return tuple(int(v) for v in RNG.integers(40, 235, 3))
PATRONS = [(extra("roshdy", rnd_col(), rnd_col()), 520, 1000, 1.7), (extra("fahmy", rnd_col(), rnd_col()), 860, 960, 1.45),
           (extra("abdo", rnd_col(), rnd_col()), 1240, 990, 1.6), (extra("nana", rnd_col(), rnd_col()), 1560, 1010, 1.7),
           (extra("roshdy", rnd_col(), rnd_col()), 230, 1040, 1.95)]
SEATB = (1085, 1075, 2.2)                 # Bondo sunk in the armchair
CUSHION = (700, 880, 1470, 1060)          # armchair front (re-pasted over his legs)

def CU(who, pos, z=2.2, dx=0):
    x, y, s = pos; S = s * CH[who]["scale"]
    hy = y - 190 * S
    return (x + dx, hy + H / (2 * z) - 1.45 * 46 * S - 25, z)

def portrait(who, expr, size, kit=None, tongue=False, bgc=(70, 80, 95), look=0):
    lay = Image.new("RGBA", (SSW, SSH), bgc + (255,))
    a = A_(who, (960, 1000, 2.2), expr=expr, look=look, arms="up" if tongue else "down", noshadow=True)
    if kit: a["kit"] = kit; a["num"] = 10
    draw_people(lay, "x", -1, (0, 0, 1.0), {}, [a])
    S = 2.2 * CH[who]["scale"]; hy = 1000 - 190 * S
    if tongue:
        p = P(lay); p.ell(966, hy + 44 * S, 10 * S, 13 * S, (230, 90, 110, 255), INK, 2 * S); p.line([(966, hy + 36 * S), (966, hy + 52 * S)], (170, 50, 70, 255), 1.5 * S)
    box = (960 - 330, hy - 240, 960 + 330, hy + 300)
    im = lay.crop(tuple(int(v * SS) for v in box)).convert("RGB")
    return im.resize(size, Image.LANCZOS)

PAPERS = [("أخبار العمارة", "رسميًا: إقالة الكابتن بندق!", (244, 236, 218)),
          ("صوت الحارة", "بندق برة... والعمارة تغلي!", (236, 240, 244)),
          ("كورة الشارع", "نهاية عصر الكابتن", (250, 232, 205))]
_PIMG = None
def paper_img(i):
    name, head, col = PAPERS[i]
    im = Image.new("RGB", (900, 620), col); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 900, 110], fill=(30, 30, 35)); text(im, 450, 55, name, 64, (255, 255, 255), sw=0)
    text(im, 450, 175, head, 56, (180, 20, 30), sw=0)
    ph = portrait("bondo2", ["sad", "shock", "sleepy"][i], (360, 300), bgc=(120, 120, 128))
    im.paste(ph, (500, 240)); d.rectangle([500, 240, 860, 540], outline=(20, 20, 20), width=4)
    for k in range(8): d.rectangle([40, 250 + k * 36, 450, 262 + k * 36], fill=(150, 150, 150))
    d.rectangle([20, 570, 880, 580], fill=(30, 30, 35))
    return im

t = 0.0
PAPER_T = []
for i in range(3):                                                    # hook: spinning newspapers
    fx(t, "whoosh", 0.9); PAPER_T.append(t); t += 1.15
shot("papers", 0, t, None); fx(t - 0.3, "stinger", 0.8)
shot("title", t, t + 2.0, None, tin="fade"); fx(t, "whoosh", 0.5); t += 2.0
s = t; fx(t, "switch", 0.8); t = say(t + 0.3, "P601") + 0.5; LIVE1 = s
shot("live", s, t, (960, 450, 1.5), (960, 450, 1.6), tin="flash")
CAFE = (t, t + 3.0); fx(t + 0.6, "gasp", 0.9)                         # the cafe reads the news
shot("cafe", t, CAFE[1], (960, 600, 1.05), (960, 520, 1.25), tin="whip"); t = CAFE[1]
ROOM = t; BUZZ = t + 1.2                                              # the coach's room... the phone buzzes
for i in range(3): fx(BUZZ + i * 0.18, "kick", 0.25)
shot("room", t, t + 2.4, (960, 540, 1.0), (1060, 600, 1.3), tin="fade"); t += 2.4
s = t; t = say(t + 0.2, "P602") + 0.6; READ = s                       # reads the phone
shot("room", s, t, CU("bondo2", SEATB, 2.2), CU("bondo2", SEATB, 2.7), ease="crash", tin="zoom")
s = t; t = say(t + 0.4, "P603") + 0.3; SLEEP = s                      # sinks into the chair
shot("room", s, t, (1060, 640, 1.45), (1080, 700, 1.65))
DOZE = (t, t + 2.4)                                                   # Zzz... wide, the old photo on the wall
shot("room", t, DOZE[1], (1080, 700, 1.65), (960, 540, 1.05)); t = DOZE[1]
POST = (t, t + 4.6); fx(t, "switch", 0.6)                             # meanwhile... Shatta posts a selfie
shot("post", t, POST[1], None, tin="whip"); t = POST[1]
s = t; t = say(t + 0.3, "P604") + 0.8; LIVE2 = s
shot("live", s, t, (960, 450, 1.5), (960, 450, 1.7), tin="flash")
shot("end", t, t + 3.0, None, tin="fade"); fx(t, "stinger", 0.7); t += 3.0
TOTAL = t

def papers(tt):
    global _PIMG
    if _PIMG is None: _PIMG = [paper_img(i) for i in range(3)]
    fr = Image.new("RGB", (W, H), (18, 14, 16)); d = ImageDraw.Draw(fr)
    for j in range(0, W, 60): d.line([(j, 0), (j - 300, H)], fill=(28, 22, 24), width=2)
    for i, t0 in enumerate(PAPER_T):
        if tt < t0: continue
        k = ease(kk(tt, t0, t0 + 0.6)); ang = (1 - k) * 720 + (i - 1) * 6
        sc = 0.05 + 0.95 * k
        im = _PIMG[i].resize((max(4, int(900 * sc * 1.25)), max(4, int(620 * sc * 1.25))), Image.BILINEAR).convert("RGBA").rotate(ang, expand=True, resample=Image.BILINEAR)
        cx, cy = W / 2 + (i - 1) * 90, H / 2 + (i - 1) * 25
        fr.paste(im, (int(cx - im.size[0] / 2), int(cy - im.size[1] / 2)), im)
    return fr

def post_ui(tt):
    u = tt - POST[0]
    fr = bg_crop(_nb, (300, 200, 1.4), False).resize((W, H)).filter(ImageFilter.GaussianBlur(20))
    fr = ImageEnhance.Brightness(fr).enhance(0.5); d = ImageDraw.Draw(fr, "RGBA")
    k = ease(min(1, u / 0.4)); y0 = int(60 + (1 - k) * 600)
    X0, X1 = 560, 1360
    d.rounded_rectangle([X0, y0, X1, y0 + 960], 30, fill=(250, 250, 252, 255))
    d.ellipse([X0 + 30, y0 + 28, X0 + 100, y0 + 98], fill=(205, 35, 45))
    text(fr, X0 + 65, y0 + 63, "10", 30, (255, 255, 255), sw=0)
    text(fr, X1 - 210, y0 + 48, "شطة • النجم", 36, (20, 20, 20), sw=0)
    text(fr, X1 - 210, y0 + 86, "منذ دقيقة", 24, (120, 120, 120), sw=0)
    text(fr, (X0 + X1) / 2, y0 + 140, "مساء الفل يا عمارة...", 40, (20, 20, 20), sw=0)
    ph = portrait("shatta", "happy", (760, 560), kit=RED_KIT, tongue=True, bgc=(90, 110, 140), look=-1)
    fr.paste(ph, (X0 + 20, y0 + 180))
    likes = int(120 + 9000 * min(1, u / 3.2) ** 1.6)
    text(fr, X1 - 160, y0 + 785, f"{likes} لايك", 36, (200, 30, 60), sw=0)
    d.ellipse([X1 - 60, y0 + 765, X1 - 22, y0 + 803], fill=(220, 40, 70))
    for i, c in enumerate(("هههههههه", "يعني رجعت ولا لأ؟", "اللسان ده لمين؟", "الكابتن شاف البوست؟")):
        st = POST[0] + 0.9 + i * 0.75
        if tt < st: continue
        a = int(240 * min(1, (tt - st) * 3)); yy_ = y0 + 850 - (len([1 for j in range(4) if POST[0] + 0.9 + j * 0.75 <= tt]) - 1 - i) * 0
        bx = X1 + 40 + (i % 2) * 30; by = 180 + i * 140
        d.rounded_rectangle([bx, by, bx + 470, by + 90], 30, fill=(255, 255, 255, a))
        text(fr, bx + 235, by + 45, c, 34, (30, 30, 30), sw=0)
    for i in range(10):     # floating hearts from the like button
        v = ((tt - POST[0]) * 0.6 + i / 10) % 1
        x = X1 - 41 + math.sin(v * 9 + i) * 30; y = y0 + 760 - v * 500
        r = 18
        d.ellipse([x - r, y - r, x, y], fill=(230, 50, 80, int(220 * (1 - v)))); d.ellipse([x, y - r, x + r, y], fill=(230, 50, 80, int(220 * (1 - v))))
        d.polygon([(x - r, y - r / 2), (x + r, y - r / 2), (x, y + r)], fill=(230, 50, 80, int(220 * (1 - v))))
    return fr

def frame(tt):
    sh = shot_at(tt); set_ = sh["set"]
    if set_ == "papers": return finish(papers(tt), tt)
    if set_ == "title": return finish(title_card(tt, sh, SERIES, EPT), tt)
    if set_ == "end": return finish(title_card(tt, sh, "النهاية", SERIES, "تابعونا... الترند الجاي عندنا!"), tt)
    if set_ == "post": return finish(post_ui(tt), tt)
    cam = cam_at(sh, tt); x0, y0, z = cam
    if set_ == "room": img = bg_crop(_room, cam)
    elif set_ == "cafe": img = bg_crop(_cafe, cam)
    else: img = bg_crop(_nb, (0, 160, 1.6)).filter(ImageFilter.GaussianBlur(8 * SS))
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0))
    if set_ == "room":
        b = A_("bondo2", SEATB, look=1, expr="neutral", arms="hold", held="phone", noshadow=True)
        if tt < BUZZ: b["held"] = None; b["arms"] = "down"; b["expr"] = "sleepy"
        if BUZZ <= tt < READ: b["expr"] = "flat"
        if tt >= SLEEP: b["expr"] = "sleepy"
        if tt >= SLEEP + DUR["P603"]: b["lean"] = -1; b["held"] = None; b["arms"] = "down"
        b["y"] += 40 * ease(kk(tt, SLEEP, SLEEP + DUR["P603"] + 0.6))    # sinks into the chair
        draw_people(lay, set_, tt, cam, sh, [b])
        lay = tint_layer(lay, (255, 225, 185)); img.paste(lay, (0, 0), lay)
        bx0 = int((CUSHION[0] - x0) * z * SS); by0 = int((CUSHION[1] - y0) * z * SS); bx1 = int((CUSHION[2] - x0) * z * SS); by1 = int((CUSHION[3] - y0) * z * SS)
        bgc = bg_crop(_room, cam); bx0, by0 = max(0, bx0), max(0, by0); bx1, by1 = min(SSW, bx1), min(SSH, by1)
        if bx1 > bx0 and by1 > by0: img.paste(bgc.crop((bx0, by0, bx1, by1)), (bx0, by0))
        lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0))
        if BUZZ <= tt < READ + 0.3:     # phone screen glow
            p = P(lay); S = SEATB[2] * CH["bondo2"]["scale"]
            gx = (SEATB[0] + 46 * S - x0) * z; gy = (SEATB[1] - 104 * S - y0) * z
            if int((tt - BUZZ) * 12) % 2 == 0: p.ell(gx, gy, 26 * z, 26 * z, (160, 210, 255, 90), None)
    elif set_ == "cafe":
        ppl = []
        for i, (w_, x_, y_, s_) in enumerate(PATRONS):
            a = A_(w_, (x_, y_, s_), look=0 if i % 2 else 1, expr="shock", arms="scared" if i % 2 else "hold", held=None if i % 2 else "paper")
            ppl.append(a)
        draw_people(lay, set_, tt, cam, sh, ppl)
        lay = tint_layer(lay, (255, 238, 210))
        feed = portrait("bondo2", "sad", (TV[2] - TV[0], TV[3] - TV[1]), bgc=(40, 60, 90))
        fd = ImageDraw.Draw(feed); fd.rectangle([0, feed.size[1] - 40, feed.size[0], feed.size[1]], fill=(200, 20, 30))
        text(feed, feed.size[0] / 2, feed.size[1] - 20, "رسميًا: إقالة الكابتن بندق", 26, (255, 255, 255), sw=0)
        full = Image.new("RGB", (W, H)); full.paste(feed, (TV[0], TV[1]))
        img.paste(bg_crop(full, cam, False), (0, 0), bg_crop(TVMASK.convert("RGB"), cam, False).convert("L"))
    elif set_ == "live":
        draw_people(lay, set_, tt, cam, sh, [A_("sawsan", (960, 760, 1.45), held="phone", arms="hold", expr="happy")])
        lay = tint_layer(lay, (255, 235, 210))
    img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    if set_ == "live":
        t0 = LIVE1 if tt < LIVE2 else LIVE2
        cm = ("يا خبر!", "مين المدرب الجديد؟", "شطة هيرجع؟", "عبده عايز يدرب") if tt < LIVE2 else ("اكتبوا رأيكم", "بندق كان مظلوم", "لا كان غلطان", "مستنيين الترند الجاي")
        live_ui(fr, tt, t0, "عاجل", cm)
    return finish(fr, tt)

def build_audio(path):
    buf = np.zeros(int(TOTAL * SR) + SR * 3, dtype=np.float32)
    for t0, nme, g in sfx:
        if nme in SFXF: mix_into(buf, SFXF[nme], t0, g)
    r = np.random.default_rng(17)
    n = int(TOTAL * SR); bed = lowpass(r.normal(0, 1, n).astype(np.float32), 350) * 0.03
    mix_into(buf, bed, 0, 1.0)
    ts = np.arange(int(SR * 1.2)) / SR
    mix_into(buf, (np.sin(2 * np.pi * 55 * ts) + 0.5 * np.sin(2 * np.pi * 82 * ts)) * np.exp(-ts * 3) * 0.4, READ + 0.25, 1.0)
    # snoring during the doze
    ts = np.arange(int(SR * 1.1)) / SR
    snore = (lowpass(r.normal(0, 1, len(ts)).astype(np.float32), 250) * np.sin(np.pi * ts / 1.1) ** 2 * 0.5).astype(np.float32)
    for k in range(2): mix_into(buf, snore, DOZE[0] + 0.1 + k * 1.2, 1.0)
    # notification pings for the post
    tp = np.arange(int(SR * 0.25)) / SR
    ping = (np.sin(2 * np.pi * 1320 * tp) * np.exp(-tp * 18) * 0.3).astype(np.float32)
    for k in range(4): mix_into(buf, ping, POST[0] + 0.9 + k * 0.75, 1.0)
    mix_lines(buf)
    write_wav(buf[:int(TOTAL * SR)], path)

if __name__ == "__main__": main("p6")
