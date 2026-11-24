# Season-2 trailer «سر البدروم» re-cut under growth_rules (user 24/11 «ابعته بس بالخطة الجديدة»):
#   * NATIVE 9:16 (no letterbox, no permanent title bars): each segment is cropped from the 16:9 frame around its subject
#     (only the letter keeps a blurred fill because the page is wider than a phone);
#   * series title only in the first 3 s; short phrase subtitles + speaker-name pill (s2/vnative.py);
#   * vertical-native news strip / «الإرسال اتقطع» / title card;
#   * end card = ONE ask: «الحلقة الأولى الليلة!» + «تابعنا عشان ما تفوتكش» (no «قريباً», no clock time).
# Voices, timing and the 16:9 picture are unchanged except the end card text. Run: python promo_v2.py part i n → then `join`.
import sys, os
sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
sys.path.insert(0, ROOT + "/s2")
_src = open(ROOT + "/promo/promo.py", encoding="utf-8").read()
_src = _src.replace('if __name__ == "__main__":', 'if False:')
_old = '        if k > 0.45: text(fr, W / 2, 790, "قريباً", 80, (255, 255, 255), (0, 0, 0), 4)'
assert _old in _src
_src = _src.replace(_old, '''        if k > 0.45: big_text(fr, W / 2, 790, "الحلقة الأولى الليلة!", 92, (255, 255, 255))
        if k > 0.6: big_text(fr, W / 2, 915, "تابعنا عشان ما تفوتكش", 60, (255, 214, 90))''')
exec(_src)
import vnative as VN
VN.set_font(ROOT + "/brand/fonts/Lalezar-Regular.ttf"); big_text = VN.big_text
os.chdir(ROOT + "/promo")
WHO.update({"RO1": "roshdy", "RO2": "roshdy", "RO3": "roshdy", "RO4": "roshdy", "RO5": "roshdy"})
CHV = {k: VN.chunk_times(SUB[k], ENV[k], FPS) for k in SUB if SUB[k]}

def seg_at(tt): return next((x for x in segs if x["start"] <= tt < x["end"]), segs[-1])
def focus_x(tt, s):
    n = s["name"]
    if n == "cctv1":
        if 3.4 < tt < 5.8: return 500 + 900 * kk(tt, 3.4, 5.8)
        return 960
    if n == "flash":
        u = ease(kk(tt, s["start"] + 1.0, s["end"])); rx = 980 + 450 * u
        return max((640 + rx) / 2, rx - 230)
    if n == "cctv2": return 960 if tt >= POP else 690
    return 960
def crop_v(fr, cx):
    cw = H * 1080 / 1920; x0 = min(max(cx - cw / 2, 0), W - cw)
    v = fr.resize((1080, 1920), Image.LANCZOS, box=(x0, 0, x0 + cw, H))
    return v.filter(ImageFilter.UnsharpMask(2, 60, 2))
def fit_v(fr):
    bg = ImageEnhance.Brightness(fr.resize((96, 54)).filter(ImageFilter.GaussianBlur(2)).crop((21, 0, 75, 54)).resize((1080, 1920), Image.BILINEAR)).enhance(0.45)
    sc = 1080 / 1920 * 1.35; fw, fh = int(W * sc), int(H * sc); big = fr.resize((fw, fh), Image.LANCZOS)
    bg.paste(big.crop(((fw - 1080) // 2, 0, (fw - 1080) // 2 + 1080, fh)), (0, (1920 - fh) // 2)); return bg

def v_title(tt, s):
    k = kk(tt, s["start"], s["end"]); fr = Image.new("RGB", (1080, 1920), (6, 6, 10))
    g = Image.new("L", fr.size, 0); ImageDraw.Draw(g).rectangle([140, 1640, 940, 1690], fill=255)
    fr.paste(Image.new("RGB", fr.size, (255, 180, 90)), (0, 0), g.filter(ImageFilter.GaussianBlur(60)))
    a = min(1, k * 5)
    big_text(fr, 540, 420, "عمارة نعناعة", 140, (255, 214, 90), (40, 10, 10), int(255 * a))
    big_text(fr, 540, 590, "الموسم التاني", 84, (235, 235, 235), (0, 0, 0), int(255 * a))
    if k > 0.18:
        sc = 1 + 0.5 * max(0, 1 - (k - 0.18) * 8); big_text(fr, 540, 820, "سر البدروم", int(190 * sc), (230, 60, 50), (20, 0, 0))
    if k > 0.45: big_text(fr, 540, 1080, "الحلقة الأولى الليلة!", 104, (255, 255, 255))
    if k > 0.6: big_text(fr, 540, 1230, "تابعنا عشان ما تفوتكش", 72, (255, 214, 90))
    d = ImageDraw.Draw(fr, "RGBA")
    for i in range(50):
        u = (tt * 0.05 + i * 0.137) % 1; x = (i * 211) % 1080; y = 1920 - u * 1920
        d.ellipse([x - 3, y - 3, x + 3, y + 3], fill=(255, 220, 160, int(180 * (1 - u))))
    return fr

def vertical(fr, tt):
    s = seg_at(tt); n = s["name"]
    if n == "title": return v_title(tt, s)
    if n == "letter": v = fit_v(fr)
    elif n == "lost":
        v = crop_v(fr, 960); d = ImageDraw.Draw(v, "RGBA"); d.rectangle([0, 860, 1080, 1060], fill=(0, 0, 0, 255))
        big_text(v, 540, 960, "الإرسال اتقطع", 96, (255, 255, 255))
    else:
        v = crop_v(fr, focus_x(tt, s))
        if n in ("cctv1", "cctv2"):
            v = ImageEnhance.Brightness(v).enhance(1.55)                                  # the phone crop of the CCTV was too dark
            d = ImageDraw.Draw(v, "RGBA"); d.rectangle([0, 1740, 1080, 1920], fill=(8, 10, 8, 255))   # own phone HUD (the 16:9 one is cut)
            if int(tt * 2) % 2: d.ellipse([60, 1790, 96, 1826], fill=(230, 30, 30))
            d.text((112, 1808), "REC   03:12 AM", font=ImageFont.truetype(FONT, 40), fill=(235, 235, 235), anchor="lm")
            big_text(v, 900, 1808, "كاميرا البدروم", 50, (235, 235, 235))
        if n == "news":                                                                 # vertical-native news strip over the cut 16:9 one
            d = ImageDraw.Draw(v, "RGBA"); d.rectangle([0, 1505, 1080, 1765], fill=(15, 15, 25, 255))
            d.rectangle([0, 1505, 1080, 1640], fill=(170, 20, 25, 255)); d.rectangle([800, 1505, 1080, 1640], fill=(255, 214, 60, 255))
            big_text(v, 940, 1572, "عاجل", 74, (120, 10, 10), (255, 214, 60)); big_text(v, 400, 1572, "أصوات غريبة من البدروم!", 58)
            tick = "الجيران مش نايمين  •  فهمي اتمسك امبارح  •  إيه اللي في البدروم؟  •  "
            off = (tt * 200) % 1500
            for j in range(-1, 2): big_text(v, -200 + off + j * 1500, 1702, tick, 40, (230, 230, 230))
            d.rectangle([0, 80, 1080, 210], fill=(0, 0, 0, 0)); d.rectangle([0, 70, 400, 220], fill=(30, 22, 16, 255))
            d.rounded_rectangle([40, 110, 230, 180], 14, fill=(220, 30, 40, 240)); d.ellipse([58, 130, 84, 156], fill=(255, 255, 255))
            ImageDraw.Draw(v).text((100, 145), "LIVE", font=ImageFont.truetype(FONT, 40), fill=(255, 255, 255), anchor="lm")
            big_text(v, 700, 145, "طنط سوسن لايف", 52, (255, 214, 90))
    if tt < 3.0:                                                                         # rule 29: series title in the first 3 s only
        a_ = int(255 * min(1, (3.0 - tt) / 0.35)); d = ImageDraw.Draw(v, "RGBA")
        d.rounded_rectangle([90, 230, 990, 420], 40, fill=(10, 8, 6, int(a_ * 0.75)))
        big_text(v, 540, 290, "عمارة نعناعة", 92, (255, 214, 90), (40, 10, 10), a_); big_text(v, 540, 375, "الموسم التاني: سر البدروم", 54, (235, 235, 235), (0, 0, 0), a_)
    k, lt = line_at(tt)
    if k and k in CHV: VN.sub_v(v, k, lt, CHV, WHO.get(k), cy=1500 if n != "news" else 1400, size=72)
    return v

def render_part(i, n):
    a = int(TOTAL * FPS * i / n); b = int(TOTAL * FPS * (i + 1) / n)
    mk = lambda w_, h_, o: subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w_}x{h_}", "-r", str(FPS), "-i", "-",
                                             "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", o], stdin=subprocess.PIPE)
    fh = mk(W, H, f"h2_{i}.mp4"); fv = mk(1080, 1920, f"v2_{i}.mp4")
    for f_ in range(a, b):
        tt = f_ / FPS; base = frame(tt); h = base.copy(); subtitle(h, tt)
        fh.stdin.write(h.tobytes()); fv.stdin.write(vertical(base, tt).tobytes())
    fh.stdin.close(); fv.stdin.close(); fh.wait(); fv.wait()

if __name__ == "__main__":
    print("TOTAL", round(TOTAL, 1))
    if sys.argv[1:2] == ["stills"]:
        for v_ in sys.argv[2:]:
            tt = float(v_); base = frame(tt); h = base.copy(); subtitle(h, tt); h.save(f"s2_h_{tt:.1f}.png"); vertical(base, tt).save(f"s2_v_{tt:.1f}.png")
    elif sys.argv[1:2] == ["part"]: render_part(int(sys.argv[2]), int(sys.argv[3]))
    elif sys.argv[1:2] == ["audio"]: build_audio()
