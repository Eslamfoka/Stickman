# S2E01 REV 23/11 (fix 1): a short, separated opening section «حل القضية السابقة» BEFORE the basement-door hook.
# Tota's line A02 («لغز امبارح: اللي خمنوا إن فهمي هو اللي ورا الخبط... برافو عليكو!») moved here from the live scene.
# Renders pre_h.mp4 (1920x1080), pre_v.mp4 (1080x1920) and pre.wav; ep1 is then concatenated after it.
import sys, os, math, subprocess, wave
sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter, ImageFont
from engine import *
sys.path.insert(0, ROOT + "/s2"); from vnative import *
set_font(ROOT + "/brand/fonts/Lalezar-Regular.ttf")
os.chdir(ROOT + "/s2e1")

A02 = load_audio("audio/A02.mp3"); ENVA = envelope(A02); DA = len(A02) / SR
T0 = 0.5                                   # line starts
TOTAL = T0 + DA + 0.6
CH_A02 = {"A02": chunk_times("لغز امبارح: اللي خمنوا إن فهمي هو اللي ورا الخبط... برافو عليكو!", ENVA, FPS)}

def pop(tt, t0, d=0.25):
    u = (tt - t0) / d; return 0.0 if u <= 0 else (1 + 0.22 * math.sin(min(1, u) * math.pi)) if u < 1 else 1.0

def draw(tt, Wd, Hd):
    vert = Hd > Wd
    fr = Image.new("RGB", (Wd, Hd), (14, 24, 18)); d = ImageDraw.Draw(fr, "RGBA")
    for i in range(16):                                                     # slow rays
        a0 = math.radians(i * 22.5 + tt * 8); a1 = a0 + math.radians(11); R = 3000; cx, cy = Wd / 2, Hd * 0.55
        d.polygon([(cx, cy), (cx + R * math.cos(a0), cy + R * math.sin(a0)), (cx + R * math.cos(a1), cy + R * math.sin(a1))], fill=(22, 40, 28, 255))
    # the title band — clearly separated from the episode
    by = Hd * (0.16 if vert else 0.14); bh = 120 if vert else 100
    d.rectangle([0, by - bh / 2, Wd, by + bh / 2], fill=(30, 120, 60, 255))
    big_text(fr, Wd / 2, by, "حل القضية السابقة", 84 if vert else 72, (255, 255, 255), (10, 40, 20))
    # Fahmy, caught, + the green check
    lay = Image.new("RGBA", (int(Wd * SS), int(Hd * SS)), (0, 0, 0, 0)); p = P(lay)
    k = min(1.0, pop(tt, 0.15, 0.35))
    fx_, fy_, fs = (Wd * 0.5, Hd * 0.86, 4.8) if vert else (Wd * 0.33, Hd * 1.05, 3.6)
    draw_char(p, "fahmy", fx_, fy_ + (1 - k) * 200, fs, "scared", 0.0, 1, ((tt + 0.2) % 3.0) < 0.1, "scared", tt, None, 0.0, None)
    L = lay.resize((Wd, Hd), Image.LANCZOS); fr.paste(L, (0, 0), L)
    k2 = pop(tt, T0 + 1.6, 0.3)
    if k2 > 0:
        cx, cy = (Wd * 0.5, Hd * 0.3) if vert else (Wd * 0.68, Hd * 0.45)
        big_text(fr, cx, cy, "أستاذ فهمي ✓".replace(" ✓", ""), int((120 if vert else 110) * k2), (140, 255, 160), (10, 40, 20))
        r = (46 if vert else 42) * k2; cx2 = cx + (0 if vert else 0); cy2 = cy + (110 if vert else 105)
        d = ImageDraw.Draw(fr, "RGBA"); d.ellipse([cx2 - r, cy2 - r, cx2 + r, cy2 + r], fill=(40, 170, 80, 255), outline=(255, 255, 255, 255), width=5)
        d.line([(cx2 - r * 0.45, cy2), (cx2 - r * 0.1, cy2 + r * 0.38), (cx2 + r * 0.5, cy2 - r * 0.35)], fill=(255, 255, 255, 255), width=max(4, int(r * 0.22)))
    k_, lt = ("A02", tt - T0) if T0 <= tt < T0 + DA else (None, 0)
    if vert: sub_v(fr, k_, lt, CH_A02, "tota", cy=1430)
    else: sub_v(fr, k_, lt, CH_A02, "tota", cy=Hd - 90, size=56)
    # fade to black into the hook
    f = min(1, max(0, (tt - (TOTAL - 0.3)) / 0.3))
    if f > 0: fr = Image.blend(fr, Image.new("RGB", fr.size, (0, 0, 0)), f)
    return fr

def render():
    mk = lambda w, h, o: subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}", "-r", str(FPS), "-i", "-",
                                           "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p", o], stdin=subprocess.PIPE)
    fh, fv = mk(W, H, "pre_h.mp4"), mk(1080, 1920, "pre_v.mp4")
    for i in range(int(round(TOTAL * FPS))):
        tt = i / FPS; fh.stdin.write(draw(tt, W, H).tobytes()); fv.stdin.write(draw(tt, 1080, 1920).tobytes())
    fh.stdin.close(); fv.stdin.close(); fh.wait(); fv.wait()
    n = int(round(TOTAL * FPS)) / FPS
    buf = np.zeros(int(n * SR), np.float32); ts = np.arange(int(SR * 0.5)) / SR
    for j, f in enumerate((523, 659, 784)): buf[int((0.1 + j * 0.08) * SR):][:len(ts)] += (np.sin(2 * np.pi * f * ts) * np.exp(-ts * 7) * 0.18)[:len(buf[int((0.1 + j * 0.08) * SR):])]
    v = A02 / max(1e-6, np.percentile(np.abs(A02), 99.5)) * 0.8; a = int(T0 * SR); buf[a:a + len(v)] += v[:len(buf) - a]
    ts = np.arange(int(SR * 0.6)) / SR; c = int((T0 + 1.6) * SR); ch = np.sin(2 * np.pi * 1047 * ts) * np.exp(-ts * 6) * 0.15; buf[c:c + len(ch)] += ch[:len(buf) - c]
    buf = np.clip(buf, -1, 1)
    with wave.open("pre.wav", "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((buf * 32767).astype(np.int16).tobytes())
    print("pre", round(n, 2))

if __name__ == "__main__":
    if sys.argv[1:2] == ["stills"]:
        for t_ in sys.argv[2:]:
            draw(float(t_), W, H).save(f"pre_h_{t_}.png"); draw(float(t_), 1080, 1920).save(f"pre_v_{t_}.png")
    else: render()
