# Brand intro «تعالوا نعرّفكم على عيلة شطة وزلطة» — horizontal + vertical
# python intro.py stills 2 8 30   |   python intro.py audio   |   python intro.py render h|v
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
import os, math, subprocess
_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
_helpers = _src.split("# ================= logo (transparent PNG)")[0]
_sky = "def skyline" + _src.split("def skyline")[1].split("# ================= YouTube banner")[0]
exec(_helpers); exec(_sky)
HERE = ROOT + "/brand/intro"; os.chdir(HERE)

A_ = {k: load_audio(f"audio/{k}.mp3") for k in ["I01", "I02", "I03", "I04", "I05", "I06", "I07"]}
EN = {k: envelope(v) for k, v in A_.items()}
DU = {k: len(v) / SR for k, v in A_.items()}
WH = load_audio(ROOT + "/trend/01/sfx/whoosh.mp3"); ST = load_audio(ROOT + "/trend/01/sfx/stinger.mp3")

# ---------- timeline ----------
SEG = []          # dict(kind, t0, t1, ...)
t = 0.0
SEG.append(dict(kind="open", t0=0, t1=0.6 + DU["I01"] + 0.3, line=("I01", 0.6))); t = SEG[-1]["t1"]
MAIN = [("shatta", "شطة", "I02", "happy", "up", None, (255, 120, 40)),
        ("zalata", "زلطة", "I03", "smug", "point", None, (80, 190, 90)),
        ("tota", "توتة", "I04", "happy", "point", None, (235, 90, 150)),
        ("nana", "الحاجة نعناعة", "I05", "angry", "hold", "slipper", (110, 90, 220)),
        ("sawsan", "طنط سوسن", "I06", "happy", "hold", "phone", (255, 170, 40))]
for who, nm, ln, ex, arms, held, col in MAIN:
    SEG.append(dict(kind="char", who=who, name=nm, expr=ex, arms=arms, held=held, col=col, t0=t, t1=t + 0.35 + DU[ln] + 0.45, line=(ln, t + 0.35))); t = SEG[-1]["t1"]
QUICK = [("bondo2", "الكابتن بندق", "smug", (160, 104, 58)), ("fahmy", "أستاذ فهمي", "smug", (62, 70, 92)),
         ("pasha", "الباشا", "smug", (60, 60, 70)), ("abdo", "عبده", "happy", (120, 120, 130))]
for who, nm, ex, col in QUICK:
    SEG.append(dict(kind="quick", who=who, name=nm, expr=ex, col=col, t0=t, t1=t + 0.9)); t += 0.9
SEG.append(dict(kind="end", t0=t, t1=t + 0.5 + DU["I07"] + 2.6, line=("I07", t + 0.5))); t = SEG[-1]["t1"]
TOTAL = t

def seg_at(tt):
    for s in SEG:
        if s["t0"] <= tt < s["t1"]: return s
    return SEG[-1]

def mouth_at(tt):
    for s in SEG:
        if "line" in s:
            k, st = s["line"]; i = int((tt - st) * FPS)
            if 0 <= i < len(EN[k]): return k, float(EN[k][i])
    return None, 0.0

def ease_out(x): x = max(0, min(1, x)); return 1 - (1 - x) ** 3
def back(x):
    x = max(0, min(1, x)); c = 1.7
    return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2

_BG = {}
def backdrop(Wd, Hd, col):
    key = (Wd, Hd, col)
    if key not in _BG:
        b = radial(Wd, Hd, tuple(min(255, int(c * 1.15 + 30)) for c in col), tuple(int(c * 0.35) for c in col), 0.5, 0.45)
        _BG[key] = b
    return _BG[key].copy()

def spin_rays(img, cx, cy, tt, col=(255, 255, 255, 34)):
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); R = max(img.size) * 1.6; n = 18; o = tt * 0.25
    for i in range(n):
        a0 = o + i * 2 * math.pi / n; a1 = a0 + math.pi / n
        d.polygon([(cx, cy), (cx + R * math.cos(a0), cy + R * math.sin(a0)), (cx + R * math.cos(a1), cy + R * math.sin(a1))], fill=col)
    img.alpha_composite(lay)

def confetti(img, tt, t0, n=70):
    d = ImageDraw.Draw(img, "RGBA"); r = np.random.default_rng(7); Wd, Hd = img.size
    for i in range(n):
        x0 = r.uniform(0, Wd); sp = r.uniform(250, 520); c = [(255, 90, 80), (255, 214, 90), (90, 200, 120), (90, 160, 255), (240, 120, 200)][i % 5]
        y = -40 + (tt - t0) * sp - r.uniform(0, 400); x = x0 + math.sin((tt - t0) * 3 + i) * 30
        if -20 < y < Hd: d.rectangle([x, y, x + 14, y + 22], fill=c + (230,))

def frame(tt, Wd, Hd):
    s = seg_at(tt); u = tt - s["t0"]; V = Hd > Wd
    _, m = mouth_at(tt)
    cx = Wd / 2
    if s["kind"] == "open":
        img = skyline(Wd, Hd, 3); spin_rays(img, cx, Hd * 0.42, tt)
        k = back(u / 0.6); lsz = int((150 if V else 170) * max(0.05, k))
        logo(img, cx, Hd * (0.25 if V else 0.3), max(10, lsz))
        if u < 0.25: img.alpha_composite(Image.new("RGBA", img.size, (255, 255, 255, int(255 * (1 - u / 0.25)))))
        # Shatta runs in from the left, skids to the centre
        S = 4.6 if V else 3.6
        x = -300 + (cx + 300) * ease_out((u - 0.4) / 0.6)
        fg = figure("shatta", S, "shock" if u < 1.6 else "happy", m, 1 if u < 1.0 else 0, "up", None, lean=0.25 if u < 1.0 else 0)
        place(img, fg, x, Hd + int(S * 70) - (40 if V else 0))
    elif s["kind"] == "char":
        img = backdrop(Wd, Hd, s["col"]); spin_rays(img, cx, Hd * 0.45, tt)
        k = back(u / 0.45)
        S = 5.0 if V else 4.0
        bounce = math.sin(min(1, u / 0.45) * math.pi) * 40
        x = cx + (1 - k) * Wd * 0.6
        fg = figure(s["who"], S, s["expr"], m, 0, s["arms"] if m > 0.05 or u > 0.6 else "down", s["held"])
        place(img, fg, x, Hd + int(S * 70) - bounce - (60 if V else 0))
        # name card
        kk_ = ease_out((u - 0.15) / 0.3); ny = Hd * (0.13 if V else 0.15)
        if kk_ > 0:
            sz = int((190 if V else 160) * (0.6 + 0.4 * kk_))
            lz(img, cx - (1 - kk_) * 400, ny, s["name"], sz, GOLD, ow=max(8, sz // 9), iw=max(3, sz // 22))
        if s["who"] == "shatta" and u > DU["I02"] * 0.8:       # something falls behind him
            fy = min(Hd * 0.8, -100 + (u - DU["I02"] * 0.8) * 2200)
            d = ImageDraw.Draw(img); bx = cx + (230 if not V else 180)
            d.rectangle([bx - 60, fy - 40, bx + 60, fy + 40], fill=(150, 100, 60), outline=(40, 25, 15), width=6)
    elif s["kind"] == "quick":
        img = backdrop(Wd, Hd, s["col"]); spin_rays(img, cx, Hd * 0.45, tt * 3)
        k = back(u / 0.25); S = 4.6 if V else 3.7
        fg = figure(s["who"], S, s["expr"], 0.2, 0, "hips", None)
        place(img, fg, cx, Hd + int(S * 70) - (1 - k) * -400 - (60 if V else 0))
        lz(img, cx, Hd * (0.14 if V else 0.17), s["name"], 130 if V else 115, (255, 255, 255))
    else:   # end — everyone together
        img = skyline(Wd, Hd, 5); spin_rays(img, cx, Hd * 0.4, tt)
        cast = [("bondo2", -2.6), ("fahmy", -1.9), ("nana", -1.2), ("zalata", -0.55), ("shatta", 0.0), ("tota", 0.55), ("sawsan", 1.2), ("pasha", 1.9), ("abdo", 2.6)]
        S = 2.05 if V else 2.15; gap = (Wd * (0.105 if not V else 0.112))
        order = sorted(cast, key=lambda c: abs(c[1]), reverse=True)
        for i, (who, off) in enumerate(order):
            d0 = 0.06 * i; kk_ = back((u - d0) / 0.4)
            if kk_ <= 0: continue
            mm = m if who == "shatta" else 0.0
            fg = figure(who, S * (1.15 if who == "shatta" else 1.0), "happy", mm, 0, "up", None)
            place(img, fg, cx + off * gap, Hd + int(S * 70) - (1 - kk_) * -500 - (Hd * 0.08 if V else -40))
        logo(img, cx, Hd * (0.13 if V else 0.15), 120 if V else 110)
        k2 = ease_out((u - 0.6) / 0.4)
        if k2 > 0:
            lz(img, cx, Hd * (0.26 if V else 0.3), "مين فيهم شبهك؟ 👇".replace(" 👇", ""), int((110 if V else 96) * k2) + 1, GOLD, ow=12, iw=3)
        k3 = ease_out((u - 0.5 - DU["I07"]) / 0.4)
        if k3 > 0:
            lz(img, cx, Hd * (0.34 if V else 0.42), "shattawzalata@", int(64 * k3) + 1, (255, 255, 255), ow=8, iw=1)
        confetti(img, tt, s["t0"] + 0.3)
    return img.convert("RGB")

def build_audio(path="mix.wav"):
    buf = np.zeros(int(TOTAL * SR) + SR, dtype=np.float32)
    mix_into(buf, ST, 0.0, 0.8)
    for s in SEG:
        if s["kind"] in ("char", "quick", "end"): mix_into(buf, WH, max(0, s["t0"] - 0.08), 0.6)
        if "line" in s:
            k, st = s["line"]; mix_into(buf, A_[k] / max(1e-6, np.percentile(np.abs(A_[k]), 99.5)) * 0.8, st, 1.0)
    mix_into(buf, ST, SEG[-1]["t0"] + 0.2, 0.6)
    # light bouncy bed
    tt = np.arange(len(buf)) / SR
    beat = (np.sin(2 * np.pi * 110 * tt) * np.exp(-((tt * 2.2) % 1) * 9) * 0.06 + np.sin(2 * np.pi * 220 * tt) * np.exp(-(((tt * 2.2) + 0.5) % 1) * 12) * 0.03)
    buf += beat.astype(np.float32)
    buf = np.clip(buf / max(1e-6, np.abs(buf).max()) * 0.95, -1, 1)
    import wave
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((buf * 32767).astype(np.int16).tobytes())

def render(mode):
    Wd, Hd = (1920, 1080) if mode == "h" else (1080, 1920)
    out = f"intro_{mode}_video.mp4"
    p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{Wd}x{Hd}", "-r", str(FPS), "-i", "-",
                          "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    n = int(TOTAL * FPS)
    for i in range(n):
        p.stdin.write(frame(i / FPS, Wd, Hd).tobytes())
        if i % 120 == 0: print(mode, i, n, flush=True)
    p.stdin.close(); p.wait()
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", out, "-i", "mix.wav", "-c:v", "copy", "-af", "loudnorm=I=-15:TP=-1.5",
                    "-c:a", "aac", "-b:a", "192k", "-shortest", f"intro_{mode}.mp4"], check=True)

if __name__ == "__main__":
    print("TOTAL", round(TOTAL, 2))
    a = sys.argv[1:]
    if a[:1] == ["stills"]:
        for v in a[1:]:
            frame(float(v), 1920, 1080).save(f"st_h_{v}.png"); frame(float(v), 1080, 1920).save(f"st_v_{v}.png")
    elif a[:1] == ["audio"]: build_audio()
    elif a[:1] == ["render"]: render(a[1])
