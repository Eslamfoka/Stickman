import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
EPT = "الحلقة 5: الصلح"
SUB = {"P503": "عاجل!... النجم شطة نقل لعمارة الجيران!",
       "P501": "يا شطة... باسم اتحاد العمارة... جبتلك شاي وبسكوت.",
       "P504": "ارجع يا شطة... العمارة من غيرك وحشة.",
       "P502": "مش راجع... إلا لما الكابتن يمشي!",
       "P505": "احتمال إنه يرجع: صفر في المية."}
WHO = {"P503": "sawsan", "P501": "zalata", "P504": "zalata", "P502": "shatta", "P505": "zalata"}
EXPR = {"P503": "happy", "P501": "happy", "P504": "sad", "P502": "angry", "P505": "flat"}
ARMS = {"P503": "talk", "P502": "point"}
load_lines(list(SUB)); load_sfx(["whoosh", "switch", "stinger", "kick", "gasp"])

_nb = _ld("bg/neighbors.png")
BAL = (1110, 380, 1.2)                 # Shatta on the 1st-floor balcony
RAIL = (930, 300, 1420, 398)            # balcony railing + slab (re-pasted over his legs)
DOOR_Z = (1010, 885, 1.3)               # Zalata in front of the door
START_Z = (-160, 1010, 1.5)

def CU(who, pos, z=2.2, dx=0):
    x, y, s = pos; S = s * CH[who]["scale"]
    hy = y - 190 * S
    return (x + dx, hy + H / (2 * z) - 1.45 * 46 * S - 25, z)

t = 0.0
s = t; fx(0, "switch", 0.8); t = say(0.4, "P503") + 0.5; LIVE1 = s           # hook: Sawsan breaks the news
shot("live", s, t, (960, 450, 1.5), (960, 450, 1.6), tin="flash")
shot("title", t, t + 2.0, None, tin="fade"); fx(t, "whoosh", 0.5); t += 2.0
EST = (t, t + 3.4)                                                            # the neighbors' building, push up to the balcony
shot("nb", t, EST[1], (960, 540, 1.0), (1150, 330, 1.55), tin="fade"); t = EST[1]
WALK = (t, t + 4.0)                                                           # Zalata walks in with the tea tray (tracking)
shot("nb", t, WALK[1], (380, 700, 1.45), (870, 640, 1.35), tin="whip"); t = WALK[1]
KNOCK = t                                                                     # knock knock knock (insert)
for i in range(3): fx(t + 0.25 + i * 0.32, "kick", 0.9)
shot("nb", t, t + 1.5, (1150, 700, 2.3), (1150, 690, 2.45), tin="whipl"); t += 1.5
LOOK = t                                                                      # Shatta hears it, looks down
shot("nb", t, t + 1.4, CU("shatta", BAL, 2.3), CU("shatta", BAL, 2.6)); t += 1.4
s = t; t = say(t + 0.1, "P501") + 0.2                                         # two-shot: the official offer
shot("nb", s, t, (1080, 560, 1.12), (1070, 600, 1.2), tin="whip")
s = t; t = say(t + 0.15, "P504") + 0.25; PLEAD = s
shot("nb", s, t, CU("zalata", DOOR_Z, 2.2), CU("zalata", DOOR_Z, 2.5), tin="whipl")
s = t; t = say(t + 0.25, "P502") + 0.5; NO = s                                # the refusal, turns his face away
shot("nb", s, t, CU("shatta", BAL, 2.4), CU("shatta", BAL, 2.9), ease="crash", tin="zoom")
TURN = NO + DUR["P502"] + 0.15
s = t; t = say(t + 0.3, "P505") + 1.6; DEAD = s                               # Zalata to camera + biscuit
shot("nb", s, t, CU("zalata", DOOR_Z, 2.1), CU("zalata", DOOR_Z, 2.3), tin="whip", tocam=True)
BITE = DEAD + DUR["P505"] + 0.5; fx(BITE, "kick", 0.4)
shot("tbc", t, t + 2.6, None, tin="fade"); t += 2.6
TOTAL = t

def people_nb(tt, sh):
    sa = A_("shatta", BAL, look=-1, expr="angry", arms="hips", cross=True, kit=BLUE_KIT, num=10, noshadow=True)
    if tt >= LOOK: sa["look"] = -1; sa["expr"] = "flat"
    if tt >= NO: sa["expr"] = "angry"
    if NO <= tt < NO + DUR["P502"]: sa["cross"] = False   # points while refusing
    if tt >= TURN: sa["look"] = 1; sa["cross"] = True; sa["expr"] = "smug"     # turns his face away
    z = A_("zalata", DOOR_Z, look=1, held="tray", arms="hold", expr="happy")
    if tt < WALK[0]: z = None
    elif tt < KNOCK:
        walk_to(z, START_Z, DOOR_Z, (WALK[0] + 0.1, WALK[1]), tt, 9)
    elif tt < LOOK:   # knocking with the free hand
        z["arms"] = "point" if int((tt - KNOCK) / 0.16) % 2 == 0 else "talk"; z["held"] = None
    else:
        z["look"] = 1
    if z is not None and tt >= PLEAD: z["expr"] = "sad"
    if z is not None and tt >= DEAD: z["look"] = 0; z["expr"] = "flat"
    if z is not None and tt >= BITE: z["held"] = "sweet"; z["expr"] = "happy"
    return sa, z

def frame(tt):
    sh = shot_at(tt); set_ = sh["set"]
    if set_ == "title": return finish(title_card(tt, sh, SERIES, EPT), tt)
    if set_ == "tbc": return finish(title_card(tt, sh, "يتبع...", "الحلقة 6: الإقالة"), tt)
    cam = cam_at(sh, tt); x0, y0, z = cam
    if set_ == "nb": img = bg_crop(_nb, cam)
    else: img = bg_crop(_nb, (0, 160, 1.6)).filter(ImageFilter.GaussianBlur(8 * SS))
    lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0))
    if set_ == "nb":
        sa, zl = people_nb(tt, sh)
        draw_people(lay, set_, tt, cam, sh, [sa])
        lay = tint_layer(lay, (240, 222, 200)); img.paste(lay, (0, 0), lay)
        # balcony railing in front of Shatta's legs
        bx0 = int((RAIL[0] - x0) * z * SS); by0 = int((RAIL[1] - y0) * z * SS); bx1 = int((RAIL[2] - x0) * z * SS); by1 = int((RAIL[3] - y0) * z * SS)
        bgc = bg_crop(_nb, cam); bx0, by0 = max(0, bx0), max(0, by0); bx1, by1 = min(SSW, bx1), min(SSH, by1)
        if bx1 > bx0 and by1 > by0:
            rail = bgc.crop((bx0, by0, bx1, by1))
            # keep only the dark iron bars + slab so he reads "behind the railing"
            a = np.asarray(rail.convert("L"), np.float32)
            m = Image.fromarray((np.clip((95 - a) * 6, 0, 255)).astype(np.uint8))
            slab = int((340 - RAIL[1]) * z * SS) - (by0 - int((RAIL[1] - y0) * z * SS))
            md = ImageDraw.Draw(m); md.rectangle([0, max(0, slab), m.size[0], m.size[1]], fill=255)
            img.paste(rail, (bx0, by0), m)
        # top handrail + a few bars in front of his chest
        pp = P(img); hx0, hx1 = (1040 - x0) * z, (1200 - x0) * z; hy = (243 - y0) * z
        pp.line([(hx0, hy), (hx1, hy)], (28, 26, 30, 255), 6 * z)
        for bx in range(1046, 1200, 22): pp.line([(( bx - x0) * z, hy), ((bx - x0) * z, (300 - y0) * z)], (28, 26, 30, 255), 2.2 * z)
        lay = Image.new("RGBA", (SSW, SSH), (0, 0, 0, 0))
        if zl: draw_people(lay, set_, tt, cam, sh, [zl])
        lay = tint_layer(lay, (240, 222, 200))
    elif set_ == "live":
        draw_people(lay, set_, tt, cam, sh, [A_("sawsan", (960, 760, 1.45), held="phone", arms="hold", expr="happy")])
        lay = tint_layer(lay, (255, 235, 210))
    img.paste(lay, (0, 0), lay)
    fr = img.resize((W, H), Image.LANCZOS)
    if set_ == "live":
        live_ui(fr, tt, LIVE1, "عاجل", ("شطة لابس أزرق؟!", "ارجع يا شطة", "عمارة الجيران كسبت", "الكابتن السبب"))
    if set_ == "nb" and EST[0] <= tt < EST[1]:   # location caption
        k = min(kk(tt, EST[0] + 0.4, EST[0] + 0.8), 1 - kk(tt, EST[1] - 0.4, EST[1]))
        if k > 0:
            d = ImageDraw.Draw(fr, "RGBA"); d.rectangle([60, 70, 520, 130], fill=(0, 0, 0, int(150 * k)))
            text(fr, 290, 100, "عمارة الجيران • بالليل", 36, (255, 255, 255, int(255 * k)), sw=0)
    return finish(fr, tt)

def build_audio(path):
    buf = np.zeros(int(TOTAL * SR) + SR * 3, dtype=np.float32)
    for t0, nme, g in sfx:
        if nme in SFXF: mix_into(buf, SFXF[nme], t0, g)
    r = np.random.default_rng(15)
    n = int(TOTAL * SR); bed = lowpass(r.normal(0, 1, n).astype(np.float32), 300) * 0.03
    mix_into(buf, bed, 0, 1.0)
    # crickets on the night street
    ts = np.arange(n) / SR
    cr = np.sin(2 * np.pi * 4300 * ts) * (np.sin(2 * np.pi * 28 * ts) > 0.6) * (np.sin(2 * np.pi * 0.7 * ts) > 0) * 0.012
    mix_into(buf, cr.astype(np.float32), 0, 1.0)
    # footsteps while Zalata walks
    st = np.arange(int(SR * 0.08)) / SR
    step = (r.normal(0, 1, len(st)) * np.exp(-st * 60)).astype(np.float32) * 0.25
    tt = WALK[0] + 0.15
    while tt < WALK[1] - 0.1: mix_into(buf, step, tt, 1.0); tt += 0.35
    # sting on the refusal
    ts2 = np.arange(int(SR * 1.2)) / SR
    mix_into(buf, (np.sin(2 * np.pi * 55 * ts2) + 0.5 * np.sin(2 * np.pi * 82 * ts2)) * np.exp(-ts2 * 3) * 0.4, NO + DUR["P502"], 1.0)
    mix_lines(buf)
    write_wav(buf[:int(TOTAL * SR)], path)

if __name__ == "__main__": main("p5")
