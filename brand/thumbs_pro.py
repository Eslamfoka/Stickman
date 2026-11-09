# Pro thumbnails for the trend mini-series (uses pro.py helpers)
exec(open("/home/claude/repo/Stickman/brand/pro.py").read())
TB = "/home/claude/repo/Stickman/trend/01/bg/"
EPS = {
 1: ("pitch.png", (255, 200, 60), ["جوووون!"], [("shatta", 4.6, "happy", 0.7, -1, "up", None, RED_KIT, 10, 1420)]),
 2: ("conference.png", (230, 40, 40), ["كوكو", "خلصان؟!"], [("shatta", 2.9, "shock", 0.5, -1, "scared", None, RED_KIT, 10, 1730), ("bondo2", 4.4, "smug", 0.0, -1, "hips", None, None, None, 1330)]),
 3: ("pitch.png", (230, 40, 40), ["شطة", "طالع!"], [("shatta", 4.6, "angry", 0.6, -1, "point", None, RED_KIT, 10, 1420)]),
 4: ("studio.png", (255, 170, 40), ["لازم", "يعتذر!"], [("pasha", 3.0, "smug", 0.0, -1, "hips", None, None, None, 1720), ("abdo", 4.3, "happy", 0.5, -1, "hold", "sweet", None, None, 1330)]),
 5: ("neighbors.png", (60, 130, 240), ["مش", "راجع!"], [("zalata", 2.9, "sad", 0.2, -1, "hold", "tray", None, None, 1720), ("shatta", 4.5, "angry", 0.4, -1, "hips", None, BLUE_KIT, 10, 1330)]),
 6: ("room.png", (230, 40, 40), ["الإقالة!"], [("bondo2", 4.6, "sleepy", 0.0, -1, "down", None, None, None, 1400)]),
}
os.makedirs(f"{OUT}/thumbs", exist_ok=True)
for n, (bgf, col, words, figs) in EPS.items():
    W_, H_ = 1920, 1080
    bg = Image.open(TB + bgf).convert("RGB").resize((W_, H_), Image.LANCZOS).filter(ImageFilter.GaussianBlur(5))
    bg = ImageEnhance.Brightness(bg).enhance(0.55).convert("RGBA")
    glow = radial(W_, H_, col, (10, 6, 12), 0.72, 0.45); glow.putalpha(150); bg.alpha_composite(glow)
    bg.alpha_composite(rays((W_, H_), 1400, 420, 22, (255, 255, 255, 22)))
    vg = Image.new("RGBA", (W_, H_), (0, 0, 0, 0)); ImageDraw.Draw(vg).rectangle([0, 0, 900, H_], fill=(0, 0, 0, 70)); bg.alpha_composite(vg.filter(ImageFilter.GaussianBlur(80)))
    for who, S, ex, mo, lk, arms, held, shirt, num, x in figs:
        fg = figure(who, S, ex, mo, lk, arms, held, shirt, num)
        place(bg, fg, x, H_ + int(S * 70))
    if n == 6:
        for zx, zy, zs in ((1590, 430, 85), (1670, 345, 110), (1770, 260, 135)): lz(bg, zx, zy, "Z", zs, (255, 255, 255), ow=12, iw=1)
    # headline (left side, keeps the bottom-right timestamp area clear)
    if len(words) == 1:
        lz(bg, 500, 560, words[0], 270, GOLD if n in (1,) else (255, 255, 255), ow=30, iw=10)
    else:
        lz(bg, 470, 400, words[0], 250, (255, 255, 255), ow=26, iw=9)
        lz(bg, 470, 690, words[1], 270, GOLD, ow=28, iw=10)
    # episode badge + series tag + logo
    d = ImageDraw.Draw(bg)
    d.rounded_rectangle([60, 50, 400, 170], 30, fill=(205, 35, 45), outline=(255, 255, 255), width=6)
    lz(bg, 230, 108, f"الحلقة {n}", 78, (255, 255, 255), ow=6, iw=1, shadow=False)
    lz(bg, 470, 975, "أزمة منتخب العمارة", 72, (255, 255, 255), ow=8, iw=1)
    logo(bg, 1700, 110, 78)
    bg.convert("RGB").resize((1280, 720), Image.LANCZOS).save(f"{OUT}/thumbs/thumb_{n}.jpg", quality=93)
    print("thumb", n)
