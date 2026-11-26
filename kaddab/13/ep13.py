import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
import engine as ENG
os.chdir(ROOT + "/kaddab/13")
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"; DJ = ROOT + "/brand/fonts/DejaVuSans-Bold.ttf"
TXT = {1: "معلش يا خاتمي، العجينة أهم.", 2: "عجينتك أحلى يا خالتي!", 3: "أنا وتوتة نازلين لطنط فتحية نص ساعة… محدش يقرب من الأوضة!",
 4: "يا بندق، خاتمي في العلبة لحد ما أرجع… خد بالك!", 5: "وأنا صاحي أهو!", 6: "اتسرق!… اللي كان في العلبة اتاخد!",
 7: "من ١٢ لـ ١٢ ونص… كل واحد كان فين؟", 8: "أنا كنت في المدخل بصوّر لايف… وسمعت عزيزة وهي بتقول لبندق… وبعدين طلعت شقتي وما نزلتش تاني!",
 9: "أنا على الدكة من الصبح… واللي أعرفه سمعته من مراتي قدامكو… وأنا صاحي أهو!", 10: "أنا؟ أنا كنت مع خالتي عزيزة طول الوقت… من العجينة للزيارة والرجوع!",
 11: "صحيح… كانت معايا!", 12: "أنا على السطوح من ١٢… وماشفتش أي خاتم!", 13: "الدليل قدامكم… مين الكداب؟",
 14: "حل القضية ١٢: الكداب كان زلطة! قال «مختوم بالشمع»… ومحدش قالها قدامه خالص… فعرفها منين؟", 15: "مين الكداب؟ اكتب رقمه!"}
WHOL = {1:"aziza",2:"tota",3:"aziza",4:"aziza",5:"bondo2",6:"aziza",7:"nana",8:"sawsan",9:"bondo2",10:"tota",11:"aziza",12:"shatta",13:"nana",14:"tota",15:"tota"}
KEYS = [f"L{i}" for i in range(1, 16)]
WHO = {f"L{i}": WHOL[i] for i in TXT}
NAME = {"aziza": ("عزيزة", (230, 90, 140)), "tota": ("توتة", (255, 130, 190)), "nana": ("نعناعة", (120, 200, 140)), "sawsan": ("سوسن", (255, 170, 80)), "bondo2": ("البواب", (200, 170, 120)), "shatta": ("شطة", (255, 110, 70))}
EXPR = {"L1": "sad", "L2": "happy", "L3": "angry", "L4": "angry", "L5": "happy", "L6": "shock", "L7": "neutral", "L8": "scared", "L9": "scared", "L10": "scared", "L11": "sad", "L12": "scared", "L13": "angry", "L14": "happy", "L15": "happy"}
MF = [(0.00,2.34),(3.06,4.45),(5.44,10.21),(11.33,15.37),(16.16,17.27),(18.19,21.08),(22.06,25.35),(26.47,34.52),(35.50,41.27),(42.34,48.37),(48.92,50.84),(51.87,55.40),(56.42,58.89),(59.91,68.18),(69.19,71.02)]
CHUNKS = {}
for i, s in TXT.items():
    w = s.split(); n = max(1, -(-len(w) // 5)); per = -(-len(w) // n); parts = [" ".join(w[j:j + per]) for j in range(0, len(w), per)]
    tot = sum(len(p) for p in parts); acc = 0; ch = []
    for p in parts:
        ch.append((acc / tot * (MF[i-1][1] - MF[i-1][0]), p, None)); acc += len(p)
    CHUNKS[f"L{i}"] = ch
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
os.chdir(ROOT + "/kaddab/13")
load_lines(KEYS)
RAW = load_audio("audio/RAW.mp3")
OFF = 2.7
def lim(p): return Image.open(p).convert("RGB").resize((1920, 1080), Image.LANCZOS)
BG = {"room": lim("room.jpg"), "close": lim("close.jpg"), "c12a": lim("c12a.png"), "c12b": lim("c12b.png")}
W2S = lambda cam, x, y: ((x - cam[0]) * cam[2], (y - cam[1]) * cam[2])
HOOK_END = 2.5
shots.clear(); lines.clear()
ST = {i: OFF + MF[i-1][0] for i in TXT}
for i in TXT: say(ST[i], f"L{i}")
E = lambda i: ST[i] + DUR[f"L{i}"]
# cast positions (world coords 1920x1080): who -> (x, y_feet, scale, look)
ROOMCAST = {"aziza": (880, 960, 1.7, 1), "tota": (1230, 980, 1.5, -1)}
INV = {"nana": (300, 1000, 1.6, 1), "sawsan": (600, 1010, 1.6, 1), "bondo2": (900, 1010, 1.6, 1), "tota": (1200, 1020, 1.4, -1), "shatta": (1500, 1020, 1.5, -1), "aziza": (1790, 1010, 1.6, -1)}
SC = []  # (bg, start, end, cast, cam0, cam1)
SC.append(("close", 0.0, HOOK_END, {}, (960, 540, 1.0), (960, 540, 1.12)))
SC.append(("room", HOOK_END, ST[4] - 0.35, ROOMCAST, (960, 540, 1.0), (960, 560, 1.15)))
def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255, font=None, stroke=True):
    if size < 4: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(font or LZ, size)
    kw = dict(font=f, anchor="mm", direction="rtl", language="ar") if font is None else dict(font=f, anchor="mm")
    if stroke: d.text((x, y), s, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), **kw)
    d.text((x, y), s, fill=fill + (alpha,), **kw)
    img.paste(lay, (0, 0), lay)
def popk(tt, t0, d=0.22):
    u = kk(tt, t0, t0 + d); return 0 if u <= 0 else (1 + 0.25 * math.sin(u * math.pi)) if u < 1 else 1
def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def sub_chunk(img, tt, cx, cy, size):
    k, lt = line_at(tt)
    if not k or k not in CHUNKS: return
    cur = None
    for off, txt, key in CHUNKS[k]:
        if lt >= off: cur = (off, txt, key)
    if cur is None: return
    off, txt, key = cur; sc = popk(lt, off, 0.15) if lt - off < 0.15 else 1
    f = ImageFont.truetype(LZ, max(6, int(size * sc)))
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    kw = dict(font=f, direction="rtl", language="ar", stroke_width=max(4, size // 10), stroke_fill=(10, 10, 10, 255))
    if key and key in txt:
        a_, b_ = txt.split(key, 1); parts = [(a_, (255, 255, 255)), (key, (255, 214, 60)), (b_, (255, 255, 255))]
    else: parts = [(txt, (255, 255, 255))]
    widths = [d.textlength(s, font=f, direction="rtl", language="ar") if s else 0 for s, _ in parts]
    maxw = img.size[0] * 0.88
    if sum(widths) > maxw:
        f = ImageFont.truetype(LZ, max(6, int(size * sc * maxw / sum(widths)))); kw["font"] = f
        widths = [d.textlength(s, font=f, direction="rtl", language="ar") if s else 0 for s, _ in parts]
    tot = sum(widths); x = cx + tot / 2
    for (s, col), w_ in zip(parts, widths):
        if s: d.text((x - w_, cy), s, fill=col + (255,), anchor="lm", **kw)
        x -= w_
    nm, ncol = NAME[WHO[k]]; fn = ImageFont.truetype(LZ, int(size * 0.62))
    nw = d.textlength(nm, font=fn, direction="rtl", language="ar")
    nx = cx + tot / 2 - nw / 2 - 10; ny = cy - size * 0.95
    d.rounded_rectangle([nx - nw / 2 - 18, ny - size * 0.38, nx + nw / 2 + 18, ny + size * 0.38], int(size * 0.3), fill=ncol + (235,))
    d.text((nx, ny), nm, font=fn, fill=(20, 12, 8, 255), anchor="mm", direction="rtl", language="ar")
    img.paste(lay, (0, 0), lay)

BG["lobby"] = lim(ROOT + "/s1e1/bg/lobby_1080.png")
LOBBY = {"aziza": (620, 1000, 1.7, 1), "tota": (960, 1010, 1.5, 1), "bondo2": (1420, 1000, 1.6, -1), "sawsan": (1740, 1000, 1.6, -1)}
SC.append(("lobby", ST[4] - 0.35, ST[6] - 0.3, LOBBY, (1100, 540, 1.0), (1100, 560, 1.12)))
SC.append(("close", ST[6] - 0.3, ST[6] + 1.7, {}, (960, 540, 1.0), (960, 540, 1.1)))
SC.append(("room", ST[6] + 1.7, ST[7] - 0.3, ROOMCAST, (960, 560, 1.0), (960, 560, 1.12)))
bounds = [ST[7] - 0.3] + [(E(i) + ST[i + 1]) / 2 for i in range(7, 13)] + [E(13) + 0.5]
for n, i in enumerate(range(7, 14)):
    sx = INV[WHOL[i]][0]
    SC.append(("room", bounds[n], bounds[n + 1], INV, (sx, 640, 1.3), (sx, 650, 1.4)))
SC.append(("c12a", bounds[-1], ST[14] + 4.0, {}, (960, 540, 1.0), (960, 540, 1.1)))
SC.append(("c12b", ST[14] + 4.0, E(14) + 0.5, {}, (960, 540, 1.0), (960, 540, 1.1)))
SC.append(("card", E(14) + 0.5, E(15) + 1.2, {}, (960, 540, 1.0), (960, 540, 1.0)))
for sc in SC: shot(sc[0], sc[1], sc[2], sc[4], sc[5], cast=sc[3])
TOTAL = E(15) + 1.2
def hcam(sh, tt): return cam_at(sh, tt)
def vcam(sh, tt):
    k = ease((tt - sh["start"]) / max(0.01, sh["end"] - sh["start"])); c0, c1 = sh["c0"], sh["c1"]
    cx = c0[0] + (c1[0] - c0[0]) * k; z = 1920 / 1080
    kk_, _lt = line_at(tt); cast = sh["cast"]
    if kk_ and cast and WHO[kk_] in cast:
        w = WHO[kk_]
        cx = (cast["aziza"][0] + cast["tota"][0]) / 2 if (sh["set"] in ("room", "lobby") and sh["cast"] is not INV and w in ("aziza", "tota")) else cast[w][0]
    cw, ch = 1080 / z, 1920 / z
    return min(max(cx - cw / 2, 0), 1920 - cw), min(max(580 - ch / 2, 0), 1080 - ch), z
def card(fr, tt, Wd, Hd):
    d = ImageDraw.Draw(fr); fr.paste((12, 9, 16), (0, 0, Wd, Hd))
    k = lambda a: min(1, max(0, (tt - a)))
    lzt(fr, Wd / 2, Hd * 0.2, "قضية ١٣", int(Hd * 0.06 * (1 if Hd > Wd else 1.6)), (255, 214, 60))
    lzt(fr, Wd / 2, Hd * 0.32, "مين الكداب؟", int(Hd * 0.1 * (1 if Hd > Wd else 1.5)), (255, 255, 255))
    names = [("١", "سوسن"), ("٢", "البواب"), ("٣", "توتة"), ("٤", "شطة")]
    cols = [(255, 170, 80), (200, 170, 120), (255, 130, 190), (255, 110, 70)]
    if Hd > Wd: pos = [(Wd * (0.3 + 0.4 * (j % 2)), Hd * (0.48 + 0.14 * (j // 2))) for j in range(4)]; r = 70
    else: pos = [(Wd * (0.2 + 0.2 * j), Hd * 0.6) for j in range(4)]; r = 80
    for (n, nm), (x, y), c in zip(names, pos, cols):
        d.ellipse([x - r, y - r, x + r, y + r], fill=c, outline=(255, 255, 255), width=5)
        lzt(fr, x, y - 5, n, int(r * 1.1), (30, 14, 10), stroke=False); lzt(fr, x, y + r + 40, nm, int(r * 0.6), (255, 255, 255))
def room_img(tt, cam, size, sh):
    Wd, Hd = size; x0, y0, z = cam; bg = BG.get(sh["set"])
    if sh["set"] == "card":
        fr = Image.new("RGB", size); card(fr, tt, Wd, Hd); return fr
    img = bg.resize((int(Wd * SS), int(Hd * SS)), Image.BICUBIC, box=(x0, y0, x0 + Wd / z, y0 + Hd / z))
    cast = sh["cast"]
    if cast:
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); k, lt = line_at(tt)
        for who, (x, y, s, look) in cast.items():
            talking = k is not None and WHO.get(k) == who
            e = expr_of(k, lt) if talking else ("scared" if (cast is INV and who != "nana") else "neutral")
            mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
            X, Y_ = W2S(cam, x, y); S = s * cam[2]
            draw_char(P(lay), who, X * (Wd * SS / (Wd * z / z)) / 1.0 if False else X, Y_, S, e, mouth, look, ((tt + len(who) * 0.37) % 3.6) < 0.11, "talk" if talking else "down", tt, None, 0.0, None, sit=0)
        lay = tint_layer(lay, (255, 236, 215)); img.paste(lay, (0, 0), lay)
    return img.resize((Wd, Hd), Image.LANCZOS)

def hook_text(fr, tt, Wd, Hd):
    if tt < HOOK_END:
        lzt(fr, Wd / 2, Hd * (0.78 if Hd > Wd else 0.82), "مين فتح العلبة؟", int(110 * popk(tt, 0.3)), (255, 255, 255))
        lzt(fr, Wd * (0.5 if Hd > Wd else 0.86), Hd * 0.06, "قضية ١٣", 44, (255, 214, 60))
    if 0 and 0: pass
def c12_text(fr, tt, sh, Wd, Hd):
    if sh["set"] in ("c12a", "c12b"): lzt(fr, Wd / 2, Hd * (0.08 if Hd > Wd else 0.1), "حل القضية ١٢", 90 if Hd > Wd else 80, (110, 220, 255))
def frame(tt):
    sh = shot_at(tt); cam = hcam(sh, tt)
    fr = room_img(tt, cam, (W, H), sh)
    hook_text(fr, tt, W, H); c12_text(fr, tt, sh, W, H)
    return finish(fr, tt) if sh["set"] != "card" else fr
def subtitle(img, tt): sub_chunk(img, tt, W / 2, H - 80, 62)
VIGV = VIG.resize((1080, 1920))
def vertical(_base, tt):
    sh = shot_at(tt); cam = vcam(sh, tt)
    fr = room_img(tt, cam, (1080, 1920), sh)
    if sh["set"] != "card": fr = ImageChops.multiply(fr, VIGV)
    hook_text(fr, tt, 1080, 1920); c12_text(fr, tt, sh, 1080, 1920); sub_chunk(fr, tt, 540, 1700 if sh["set"] == "card" else 330, 76); return fr
def build_audio(path="mix.wav"):
    buf = np.zeros(int(TOTAL * SR) + SR, np.float32)
    mix_into(buf, RAW / max(1e-6, np.percentile(np.abs(RAW), 99.5)) * 0.8, OFF, 1.0)
    mix_into(buf, tone(180, 0.2, 0.14, 12), 0.2, 1.0)
    write_wav(buf[:int(TOTAL * SR)], path)
if __name__ == "__main__":
    print("TOTAL", round(TOTAL, 1))
    if sys.argv[1:2] == ["stills"]: render(None, None, [float(v) for v in sys.argv[2:]])
    elif sys.argv[1:2] == ["part"]:
        a, b = float(sys.argv[2]), float(sys.argv[3]); n = sys.argv[4]; render(f"h_{n}.mp4", f"v_{n}.mp4", None, a, b)
    elif sys.argv[1:2] == ["vpart"]:
        a, b = float(sys.argv[2]), float(sys.argv[3]); n = sys.argv[4]
        p = subprocess.Popen(["ffmpeg","-y","-v","error","-f","rawvideo","-pix_fmt","rgb24","-s","1080x1920","-r",str(FPS),"-i","-","-c:v","libx264","-preset","veryfast","-crf","23","-pix_fmt","yuv420p",f"v_{n}.mp4"],stdin=subprocess.PIPE)
        for i in range(int(round(a*FPS)), int(round(b*FPS))):
            tt=i/FPS; p.stdin.write(vertical(None, tt).tobytes())
        p.stdin.close(); p.wait()
    elif sys.argv[1:2] == ["audio"]: build_audio()
