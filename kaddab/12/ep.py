# «مين الكداب؟» — القضية 12: «الجواب المختوم» (25/11, 20:00 Kuwait) — NEW STRUCTURE (growth rules 35–37):
#   new hook first → case → «حل القضية 11» titled segment (case-11 visuals only) → final card «قضية 12 — مين الكداب؟» + ONE ask (voiced ON the card).
# Canonical lobby (s1e10/bg/morning.png): mailboxes (left wall), the doorman's bench, street door, stairs.
# Mechanism: premature knowledge made hard — Sawsan (filmed it) and the doorman (posted it) know the RED WAX SEAL legitimately;
#   Zalata says «مختوم بالشمع» though nobody mentioned it to him, he claims he was at the lesson since 3 (letter came at 5) and Sawsan's video
#   never went online («النت فصل»). ANSWER (opens case 13): زلطة ③. No highlight on «الشمع» in Z2's subtitle (keep it hard).
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont, ImageChops, ImageOps
import engine as ENG
os.chdir(ROOT + "/kaddab/12")
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"; DJ = ROOT + "/brand/fonts/DejaVuSans-Bold.ttf"
SFXF = {n: load_audio(ROOT + f"/trend/01/sfx/{n}.mp3") for n in ("whoosh", "stinger", "gasp", "switch")}
SUB = {"SW1": "لايف يا جماعة! جواب من بره… للحاجة نعناعة! ومختوم بالشمع الأحمر كمان!",
       "SW2": "يوووه… النت فصل! خلاص، الفيديو هينزل بالليل.",
       "N1": "جواب رشدي!… الصندوق فاضي! مين خد الجواب؟!",
       "Z1": "فيه إيه يا حاجة؟ أنا لسه راجع من الدرس… من تلاتة وأنا هناك!",
       "N2": "جالي جواب من رشدي… واختفى!",
       "Z2": "جواب؟… لا يا حاجة، ماليش دعوة… وبعدين هاخد جواب مختوم بالشمع أعمل بيه إيه؟",
       "SW3": "أنا صورته بنفسي يا حاجة… بس ماخدتوش! ده الفيديو حتى مانزلش.",
       "B1": "وأنا اللي حاطه في الصندوق بإيدي… وقعدت هنا على الدكة… وأنا صاحي أهو!",
       "S0": "إجابة القضية حداشر: الكدابة كانت توتة! صورتها فيها الساعة تسعة إلا ربع… بس الشمس طالعة في الشباك، يعني الصورة اتصورت الصبح! والكف الأخضر اللي على الملاية… أخضر زي الماسك اللي على وشها!",
       "Q0": "مين الكداب؟ اكتب رقمه!"}
CHUNKS = {"SW1": [(0.0, "لايف يا جماعة!", "لايف"), (1.5, "جواب من بره…", "جواب"), (2.84, "للحاجة نعناعة!", "نعناعة"), (4.49, "ومختوم بالشمع الأحمر كمان!", "الشمع الأحمر")],
          "SW2": [(0.0, "يوووه… النت فصل!", "النت فصل"), (2.6, "خلاص، الفيديو هينزل بالليل.", "بالليل")],
          "N1": [(0.0, "جواب رشدي!…", "جواب رشدي"), (1.57, "الصندوق فاضي!", "فاضي"), (2.85, "مين خد الجواب؟!", "مين")],
          "Z1": [(0.0, "فيه إيه يا حاجة؟ أنا لسه راجع من الدرس…", "الدرس"), (2.83, "من تلاتة وأنا هناك!", "من تلاتة")],
          "N2": [(0.0, "جالي جواب من رشدي…", None), (1.76, "واختفى!", "اختفى")],
          "Z2": [(0.0, "جواب؟…", None), (0.98, "لا يا حاجة، ماليش دعوة…", "ماليش دعوة"), (3.27, "وبعدين هاخد جواب مختوم بالشمع أعمل بيه إيه؟", None)],
          "SW3": [(0.0, "أنا صورته بنفسي يا حاجة…", "بنفسي"), (1.81, "بس ماخدتوش!", "ماخدتوش"), (3.15, "ده الفيديو حتى مانزلش.", "مانزلش")],
          "B1": [(0.0, "وأنا اللي حاطه في الصندوق بإيدي…", "بإيدي"), (2.1, "وقعدت هنا على الدكة…", "الدكة"), (3.88, "وأنا صاحي أهو!", "صاحي")],
          "S0": [(0.0, "إجابة القضية حداشر:", "إجابة"), (1.73, "الكدابة كانت توتة!", "توتة"), (3.66, "صورتها فيها الساعة تسعة إلا ربع…", "تسعة إلا ربع"),
                 (5.82, "بس الشمس طالعة في الشباك،", "الشمس"), (7.53, "يعني الصورة اتصورت الصبح!", "الصبح"),
                 (9.75, "والكف الأخضر اللي على الملاية…", "الكف الأخضر"), (11.65, "أخضر زي الماسك اللي على وشها!", "الماسك")],
          "Q0": [(0.0, "مين الكداب؟", "الكداب"), (1.15, "اكتب رقمه!", "رقمه")]}
WHO = {"SW1": "sawsan", "SW2": "sawsan", "SW3": "sawsan", "N1": "nana", "N2": "nana", "Z1": "zalata", "Z2": "zalata", "B1": "bondo2", "S0": "shatta", "Q0": "tota"}
NAME = {"nana": ("نعناعة", (150, 220, 190)), "sawsan": ("سوسن", (255, 160, 70)), "zalata": ("زلطة", (140, 220, 120)), "bondo2": ("البواب", (230, 170, 110)),
        "shatta": ("شطة", (255, 140, 80)), "tota": ("توتة", (255, 130, 190))}
EXPR = {"SW1": [(0, "happy"), (4.4, "shock")], "SW2": [(0, "angry"), (2.6, "sad")], "N1": [(0, "shock"), (1.5, "scared"), (2.8, "angry")],
        "Z1": "neutral", "N2": "sad", "Z2": [(0, "neutral"), (3.2, "smug")], "SW3": [(0, "scared"), (1.8, "angry")], "B1": [(0, "sleepy"), (3.8, "happy")],
        "S0": "smug", "Q0": "smug"}
load_lines(list(SUB))
SW2_END = 5.42
def tinted(img, lvl, tint): return ImageChops.multiply(ImageEnhance.Brightness(img).enhance(lvl), Image.new("RGB", img.size, tint))
LOB = _ld(ROOT + "/s1e10/bg/morning.png")
LOB5 = tinted(LOB, 1.12, (255, 236, 205))                      # «الساعة ٥» — late-afternoon sun (canonical lobby, light only)
LOB6 = tinted(LOB, 0.9, (235, 200, 190))                       # «الساعة ٦» — sunset, dimmer
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
BOX = (205, 288, 272, 398)                                      # Nana's mailbox (canonical wooden boxes, left wall)
BOXC = ((BOX[0] + BOX[2]) / 2, (BOX[1] + BOX[3]) / 2)
FEET = 1040
P_BD5 = (420, FEET, 1.55); P_SW = (800, FEET, 1.55); P_NA = (470, FEET, 1.55); P_Z = (1010, FEET, 1.6); P_SWB = (1330, FEET, 1.55); P_BDB = (300, 760, 1.3)
NUMS = (("sawsan", (230, 120, 40)), ("bondo2", (150, 96, 50)), ("zalata", (60, 150, 60)))
def body(who, x, y, s):
    S = s * CH[who]["scale"]; sh = y - 134 * S; return S, sh, (x, sh - 56 * S)

# ---------------- timeline ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
HOOK_END = 2.6
shot("hook", 0.0, HOOK_END, (240, 345, 3.6), (240, 345, 4.0), v=((240, 345, 3.9), (240, 345, 4.3)))
F5 = HOOK_END                                                                         # «الساعة ٥»
POST = (F5 + 0.2, F5 + 1.3)                                                           # doorman drops the letter in the box
shot("lob5", F5, F5 + 1.6, (560, 640, 1.45), (600, 640, 1.55), tin="whip", v=((470, 650, 1.95), (520, 650, 2.0)))
t = say(F5 + 1.0, "SW1"); LIVE0 = T("SW1") + 1.4
shot("lob5", F5 + 1.6, t + 0.1, (760, 640, 2.1), (760, 640, 2.3), v=((760, 640, 2.3), (760, 640, 2.45)))
SW2_0 = t + 0.1; t = say(SW2_0, "SW2")
t = T("SW2") + SW2_END + 0.1
shot("lob5", SW2_0, t, (760, 640, 2.3), (760, 640, 2.5), v=((760, 640, 2.45), (760, 640, 2.6)))
LIVE1 = T("SW2") + 2.6
F6 = t                                                                                 # «الساعة ٦»
NANA_IN = (F6 + 0.2, F6 + 1.9)
shot("lob6", F6, F6 + 2.0, (900, 620, 1.3), (700, 640, 1.45), tin="whip", v=((1100, 640, 1.85), (600, 650, 1.95)))
s = F6 + 2.0; t = say(s + 0.05, "N1") + 0.15; OPEN = s - 0.15; shakes.append((T("N1") + 2.85, 9))
shot("lob6", s, t, (390, 620, 1.7), (400, 630, 1.85), ease="crash", v=((360, 640, 1.9), (370, 650, 2.0)))
Z_IN = (t - 0.2, t + 1.5)                                                              # Zalata walks in through the street door
shot("lob6", t, t + 1.6, (760, 600, 1.35), (760, 620, 1.45), v=((760, 640, 1.85), (900, 650, 1.95))); t += 1.6
s = t; t = say(t + 0.05, "Z1") + 0.15
shot("lob6", s, t, (1010, 700, 2.4), (1010, 690, 2.6), tin="whip", v=((1010, 700, 2.6), (1010, 690, 2.75)))
s = t; t = say(t + 0.05, "N2") + 0.15
shot("lob6", s, t, (880, 680, 1.9), (880, 680, 2.0), v=((760, 690, 2.45), (780, 690, 2.5)))
s = t; t = say(t + 0.05, "Z2") + 0.2
shot("lob6", s, t, (1010, 700, 2.4), (1010, 695, 2.55), v=((1010, 700, 2.6), (1010, 695, 2.7)))
SW_IN = (s - 2.0, s - 0.6)                                                             # Sawsan came down too (heard Nana) — on screen before SW3
s = t; t = say(t + 0.05, "SW3") + 0.15
shot("lob6", s, t, (P_SWB[0], 700, 2.4), (P_SWB[0], 695, 2.6), tin="whip", v=((P_SWB[0], 700, 2.6), (P_SWB[0], 695, 2.75)))
s = t; t = say(t + 0.05, "B1") + 0.2
shot("lob6", s, t, (270, 600, 2.3), (270, 600, 2.5), tin="whip", v=((290, 610, 2.4), (290, 610, 2.55)))
LINE = t; BADGES = t + 0.2
shot("lob6", t, t + 1.8, (820, 640, 1.3), (840, 640, 1.38), v=((700, 640, 1.85), (980, 640, 1.9))); t += 1.8
SEG0 = t; s0 = say(t + 0.55, "S0"); SEG1 = s0 + 0.5
shot("seg11", SEG0, SEG1, None, v=None); t = SEG1
Q = t; say(Q + 0.45, "Q0"); t = Q + 0.45 + DUR["Q0"] + 0.9
shot("q", Q, t, None, v=None)
TOTAL = t
def hcam(sh, tt): return cam_at(sh, tt)
def vcam(sh, tt):
    c0, c1 = sh["v"]; k = ease((tt - sh["start"]) / max(0.01, sh["end"] - sh["start"]), sh.get("ease"))
    cx, cy, z = [a_ + (b_ - a_) * k for a_, b_ in zip(c0, c1)]; z = max(z, 1920 / 1080)
    shake = 0
    for st, amp in shakes:
        if 0 <= tt - st < 0.45: shake = max(shake, amp * (1 - (tt - st) / 0.45))
    cw, ch = 1080 / z, 1920 / z
    x0 = min(max(cx - cw / 2 + math.sin(tt * 0.9) * 3, 0), 1920 - cw); y0 = min(max(cy - ch / 2 + math.sin(tt * 1.3) * 2, 0), 1080 - ch)
    if shake: x0 = min(max(x0 + rng.normal(0, shake / z), 0), 1920 - cw); y0 = min(max(y0 + rng.normal(0, shake / z), 0), 1080 - ch)
    return x0, y0, z

# ---------------- helpers ----------------
def lzt(img, x, y, s, size, fill, outer=(45, 12, 8), alpha=255, font=None, stroke=True):
    if size < 4: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = ImageFont.truetype(font or LZ, size)
    kw = dict(font=f, anchor="mm", direction="rtl", language="ar") if font is None else dict(font=f, anchor="mm")
    if stroke: d.text((x, y), s, fill=outer + (alpha,), stroke_width=max(3, size // 9), stroke_fill=outer + (alpha,), **kw)
    d.text((x, y), s, fill=fill + (alpha,), **kw)
    img.paste(lay, (0, 0), lay)
def popk(tt, t0, d=0.22):
    u = kk(tt, t0, t0 + d); return 0 if u <= 0 else (1 + 0.25 * math.sin(u * math.pi)) if u < 1 else 1
def badge(fr, x, y, n, sc, col):
    if sc <= 0: return
    d = ImageDraw.Draw(fr, "RGBA"); r = 46 * sc
    d.ellipse([x - r, y - r, x + r, y + r], fill=col + (255,), outline=(255, 255, 255, 255), width=max(1, int(6 * sc)))
    lzt(fr, x, y + 4 * sc, n, int(70 * sc), (255, 255, 255), font=DJ)
def rays(fr, Wd, Hd, col, tt, cy=0.55):
    d = ImageDraw.Draw(fr, "RGBA")
    for i in range(18):
        a0 = i * 20 + tt * 6; a_ = math.radians(a0); b = math.radians(a0 + 9); R = 3000
        d.polygon([(Wd / 2, Hd * cy), (Wd / 2 + R * math.cos(a_), Hd * cy + R * math.sin(a_)), (Wd / 2 + R * math.cos(b), Hd * cy + R * math.sin(b))], fill=col + (255,))
_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/kaddab/12")

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

# ---------------- props ----------------
def envelope(d, x, y, zz, rot=0.0, seal=True):
    w, h = 30 * zz, 19 * zz; c, s_ = math.cos(rot), math.sin(rot)
    P_ = lambda px, py: (x + px * c - py * s_, y + px * s_ + py * c)
    d.polygon([P_(-w, -h), P_(w, -h), P_(w, h), P_(-w, h)], fill=(244, 232, 200), outline=(90, 70, 40))
    d.line([P_(-w, -h), P_(0, h * 0.15), P_(w, -h)], fill=(160, 130, 90), width=max(1, int(2 * zz)))
    if seal:
        sx, sy = P_(0, h * 0.15); r = 7.5 * zz
        d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(190, 20, 24), outline=(110, 8, 10), width=max(1, int(1.5 * zz)))
        d.ellipse([sx - r * 0.45, sy - r * 0.45, sx + r * 0.45, sy + r * 0.45], outline=(240, 90, 80), width=max(1, int(1.2 * zz)))
def mailbox_overlay(d, QW, zz, tt, open_=False):
    """Nana's box: small brass name plate + the letter in the slot (while it is there) + the door open/empty at 6"""
    a, b = QW(BOX[0], BOX[1]), QW(BOX[2], BOX[3])
    pl = QW(BOXC[0], BOX[1] + 18); pw = 26 * zz
    d.rounded_rectangle([pl[0] - pw, pl[1] - 7 * zz, pl[0] + pw, pl[1] + 7 * zz], int(3 * zz), fill=(206, 168, 80), outline=(120, 90, 30))
    f = ImageFont.truetype(LZ, max(6, int(11 * zz))); d.text(pl, "نعناعة", font=f, fill=(60, 30, 10), anchor="mm", direction="rtl", language="ar")
    if open_:
        d.rectangle([a[0] + 3 * zz, a[1] + 30 * zz, b[0] - 3 * zz, b[1] - 4 * zz], fill=(26, 18, 12))
        d.polygon([(a[0], a[1] + 28 * zz), (a[0] - 34 * zz, a[1] + 40 * zz), (a[0] - 34 * zz, b[1] + 6 * zz), (a[0], b[1])], fill=(110, 70, 36), outline=(50, 30, 10))
def letter_in_box(tt):
    """True while the letter is visible sticking out of Nana's box (posted at 5, gone by 6)"""
    return POST[1] <= tt < F6

def hook_scene(tt, cam, size):
    Wd, Hd = size; x0, y0, z = cam
    img = LOB6.resize((int(Wd * SS), int(Hd * SS)), Image.BICUBIC, box=(x0, y0, x0 + Wd / z, y0 + Hd / z))
    img = ImageEnhance.Brightness(img).enhance(0.75)
    zz = z * SS; QW = lambda x, y: ((x - x0) * zz, (y - y0) * zz); d = ImageDraw.Draw(img, "RGBA")
    mailbox_overlay(d, QW, zz, tt)
    u = ease(kk(tt, 0.35, 1.7)); ex, ey = lerp(BOXC[0], BOXC[0] - 70, u), lerp(BOX[1] + 40, BOX[1] + 150, u)
    q = QW(ex, ey); envelope(d, q[0], q[1], zz * 1.15, -0.25 * u)
    hx, hy = q[0] - 22 * zz, q[1] + 6 * zz                                              # hand in shadow (no sleeve colour)
    d.line([(hx - 260 * zz, hy + 160 * zz), (hx, hy)], fill=(22, 18, 20), width=int(26 * zz))
    d.ellipse([hx - 12 * zz, hy - 10 * zz, hx + 12 * zz, hy + 10 * zz], fill=(40, 30, 28))
    fr = img.resize((Wd, Hd), Image.LANCZOS)
    if tt < 0.3: fr = Image.blend(Image.new("RGB", fr.size, (0, 0, 0)), fr, tt / 0.3)
    return fr

# ---------------- people in the lobby ----------------
def people(tt):
    """list of (who, x, y, s, expr, look, arms, held, walk, sit)"""
    k, lt = line_at(tt); P_ = []
    if tt < F6:
        u = ease(kk(tt, POST[1] + 0.3, POST[1] + 1.6))                                     # doorman: posts it, then goes back to his bench
        if u < 1: P_.append(("bondo2", lerp(P_BD5[0], 300, u), lerp(FEET, P_BDB[1] + 90, u), lerp(1.55, 1.3, u), "happy", -1 if u > 0 else -1, "down" if tt >= POST[1] else "point", None, tt * 7 if 0 < u < 1 else None, 0))
        else: P_.append(("bondo2", P_BDB[0], P_BDB[1], P_BDB[2], "sleepy", 1, "down", None, None, 1))
        P_.append(("sawsan", P_SW[0], P_SW[1], P_SW[2], "happy", -1, "phone", "phone", None, 0))
    else:
        P_.append(("bondo2", P_BDB[0], P_BDB[1], P_BDB[2], "sleepy" if tt < BADGES - 2 else "neutral", 1, "down", None, None, 1))
        u = ease(kk(tt, *NANA_IN)); nx = lerp(1350, P_NA[0], u); ny = lerp(880, FEET, u); ns = lerp(1.3, 1.55, u)
        u2 = ease(kk(tt, Z_IN[0], Z_IN[0] + 1.0)); nx = lerp(nx, 900, u2)                       # steps back toward the door when Zalata comes in
        P_.append(("nana", nx, ny, ns, "neutral", -1 if u < 1 else 1, "down", None, tt * 8 if (0 < u < 1 or 0 < u2 < 1) else None, 0))
        if tt >= Z_IN[0]:
            u = ease(kk(tt, *Z_IN)); P_.append(("zalata", lerp(745, P_Z[0], u), lerp(640, FEET, u), lerp(0.85, 1.6, u), "neutral", -1, "down", "nbpen", tt * 8 if u < 1 else None, 0))
        if tt >= SW_IN[0]:
            u = ease(kk(tt, *SW_IN)); P_.append(("sawsan", lerp(1450, P_SWB[0], u), lerp(900, FEET, u), lerp(1.3, 1.55, u), "neutral", -1, "down", "phone", tt * 8 if u < 1 else None, 0))
    return P_

def draw_people(lay, cam, tt):
    k, lt = line_at(tt)
    for who, x, y, s, ex, look, arms, held, walk, sit in people(tt):
        talking = k is not None and WHO.get(k) == who
        e = expr_of(k, lt) if talking else ex
        if not talking and tt >= T("N1") and who in ("sawsan", "bondo2", "zalata") and k in ("N1", "N2"): e = "scared" if who != "zalata" else "neutral"
        mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
        a = arms
        if talking and arms in ("down",): a = "talk"
        if who == "nana" and k == "N1" and lt < 1.6: a = "up"
        if who == "sawsan" and k in ("SW1", "SW2"): a = "phone"
        X, Y_ = W2S(cam, x, y); S = s * cam[2]
        draw_char(P(lay), who, X, Y_, S, e, mouth, look, ((tt + len(who) * 0.37) % 3.6) < 0.11 and e not in ("sleepy",), a, tt, held, 0.0, walk, sit=sit)
    # the letter in the doorman's hand while he posts it
    if POST[0] <= tt < POST[1]:
        u = ease(kk(tt, *POST)); q = W2S(cam, lerp(P_BD5[0] - 40, BOXC[0], u), lerp(820, BOXC[1] + 20, u))
        envelope(ImageDraw.Draw(lay), q[0] * SS, q[1] * SS, cam[2] * SS * 1.1, 0.0)

def scene(tt, sh, cam, size):
    Wd, Hd = size; x0, y0, z = cam; set_ = sh["set"]
    src = LOB5 if set_ == "lob5" else LOB6
    img = src.resize((int(Wd * SS), int(Hd * SS)), Image.BICUBIC, box=(x0, y0, x0 + Wd / z, y0 + Hd / z))
    if z > 2.2: img = img.filter(ImageFilter.GaussianBlur(min(1.4, (z - 2.2) * 0.7)))
    zz = z * SS; QW = lambda x, y: ((x - x0) * zz, (y - y0) * zz); d = ImageDraw.Draw(img, "RGBA")
    mailbox_overlay(d, QW, zz, tt, open_=(tt >= OPEN and set_ == "lob6"))
    if letter_in_box(tt): q = QW(BOXC[0], BOX[1] + 46); envelope(d, q[0], q[1], zz * 0.95, 0.0)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); draw_people(lay, cam, tt)
    lay = tint_layer(lay, (255, 240, 220) if set_ == "lob5" else (250, 232, 225)); img.paste(lay, (0, 0), lay)
    fr = img.resize((Wd, Hd), Image.LANCZOS)
    vert = Hd > Wd
    if sh["start"] == F5 and tt < F5 + 1.6: lzt(fr, Wd / 2, Hd * (0.2 if vert else 0.14), "الساعة ٥", int(80 * popk(tt, F5 + 0.1)), (255, 230, 150))
    if sh["start"] == F6 and tt < F6 + 1.7: lzt(fr, Wd / 2, Hd * (0.2 if vert else 0.14), "الساعة ٦", int(80 * popk(tt, F6 + 0.1)), (255, 200, 150))
    return fr

# ---------------- Sawsan's live (phone inset) ----------------
def live_inset(fr, tt, Wd, Hd):
    if not (LIVE0 <= tt < LIVE1 + 1.0): return fr
    k = ease(kk(tt, LIVE0, LIVE0 + 0.25)) * (1 - ease(kk(tt, LIVE1 + 0.75, LIVE1 + 1.0)))
    vert = Hd > Wd; ph = (Hd * 0.42 if vert else Hd * 0.62) * (0.6 + 0.4 * k); pw = ph * 0.56
    cx, cy = (Wd * 0.5, Hd * 0.33) if vert else (Wd * 0.78, Hd * 0.42)
    d = ImageDraw.Draw(fr, "RGBA"); bz = 14
    d.rounded_rectangle([cx - pw / 2 - bz, cy - ph / 2 - bz * 2, cx + pw / 2 + bz, cy + ph / 2 + bz * 2], 30, fill=(20, 20, 26, int(255 * k)))
    if k < 0.05: return fr
    if tt < T("SW2") + 1.9:                                                            # the live picture: Nana's box + the sealed letter
        zc = 5.2; cam = (BOXC[0] - pw / 2 / zc, BOXC[1] + 10 - ph / 2 / zc, zc)
        scr = LOB5.resize((int(pw), int(ph)), Image.BICUBIC, box=(cam[0], cam[1], cam[0] + pw / zc, cam[1] + ph / zc))
        sd = ImageDraw.Draw(scr, "RGBA"); QW = lambda x, y: ((x - cam[0]) * zc, (y - cam[1]) * zc)
        mailbox_overlay(sd, QW, zc, tt); q = QW(BOXC[0], BOX[1] + 46); envelope(sd, q[0], q[1], zc * 0.95, 0.0)
        sd.rounded_rectangle([14, 14, 128, 54], 10, fill=(220, 30, 40, 240)); sd.ellipse([24, 26, 40, 42], fill=(255, 255, 255))
        sd.text((50, 34), "LIVE", font=ImageFont.truetype(DJ, 26), fill=(255, 255, 255), anchor="lm")
    else:                                                                              # «النت فصل» — no signal, video never went up
        scr = Image.new("RGB", (int(pw), int(ph)), (24, 24, 30)); sd = ImageDraw.Draw(scr, "RGBA")
        c = (pw / 2, ph * 0.42); r = pw * 0.12; a0 = tt * 360
        sd.arc([c[0] - r, c[1] - r, c[0] + r, c[1] + r], a0, a0 + 270, fill=(200, 200, 210), width=8)
        lzt(scr, pw / 2, ph * 0.62, "مفيش إنترنت", int(pw * 0.11), (255, 255, 255))
        lzt(scr, pw / 2, ph * 0.72, "الفيديو مااتنشرش", int(pw * 0.08), (255, 140, 120))
    fr.paste(scr, (int(cx - pw / 2), int(cy - ph / 2)))
    return fr

# ---------------- «حل القضية 11» (case-11 visuals only) ----------------
C11 = ROOT + "/kaddab/12/c11/"
PHOTO11 = Image.open(C11 + "photo.png").convert("RGB")
PRINT_H = Image.open(C11 + "print_h.png").convert("RGB"); PRINT_V = Image.open(C11 + "print_v.png").convert("RGB")
def seg11(tt, Wd, Hd):
    vert = Hd > Wd; lt = tt - T("S0")
    fr = Image.new("RGB", (Wd, Hd), (12, 30, 22)); rays(fr, Wd, Hd, (20, 44, 30), tt)
    if lt < 3.6:                                                                       # 1) the liar of case 11 = Tota ②
        lay = Image.new("RGBA", (int(Wd * SS), int(Hd * SS)), (0, 0, 0, 0)); p = P(lay)
        k_, lt_ = line_at(tt)
        draw_char(p, "tota", Wd * 0.5, Hd * (0.9 if vert else 1.12), 4.6 if vert else 4.2, "scared" if lt > 1.73 else "smug", 0.0, 1, False, "scared" if lt > 1.73 else "phone", tt, "phone", 0.0, None)
        L = lay.resize((Wd, Hd), Image.LANCZOS); fr.paste(L, (0, 0), L)
        if lt > 1.73:
            badge(fr, Wd * 0.5 + (230 if vert else 260), Hd * (0.44 if vert else 0.4), "2", 1.2 * popk(lt, 1.73), (220, 80, 150))
            lzt(fr, Wd / 2, Hd * (0.3 if vert else 0.27), "الكدابة: توتة", int((96 if vert else 84) * popk(lt, 1.8)), (255, 214, 90))
    elif lt < 9.6:                                                                     # 2) her «proof» selfie: 8:45 + SUN = morning
        ph = Hd * (0.56 if vert else 0.74); pw = ph * PHOTO11.size[0] / PHOTO11.size[1]
        im = PHOTO11.resize((int(pw), int(ph)), Image.LANCZOS); cx, cy = Wd / 2, Hd * (0.45 if vert else 0.52)
        d = ImageDraw.Draw(fr, "RGBA"); d.rounded_rectangle([cx - pw / 2 - 22, cy - ph / 2 - 40, cx + pw / 2 + 22, cy + ph / 2 + 40], 40, fill=(20, 20, 26))
        fr.paste(im, (int(cx - pw / 2), int(cy - ph / 2))); d = ImageDraw.Draw(fr, "RGBA")
        sx, sy = cx - pw / 2 + pw * 230 / 760, cy - ph / 2 + ph * 170 / 1080                 # sun (PHOTO coords 230,170)
        kx, ky = cx - pw / 2 + pw * 585 / 760, cy - ph / 2 + ph * 205 / 1080                 # clock (PHOTO coords 585,205)
        if lt >= 3.66: r = pw * 0.2 * popk(lt, 3.66); d.ellipse([kx - r, ky - r, kx + r, ky + r], outline=(255, 214, 60), width=8)
        if lt >= 5.82: r = pw * 0.2 * popk(lt, 5.82); d.ellipse([sx - r, sy - r, sx + r, sy + r], outline=(255, 80, 60), width=10)
        if lt >= 7.53: lzt(fr, cx, cy - ph / 2 - (110 if vert else 80), "اتصورت الصبح!", int((84 if vert else 70) * popk(lt, 7.53)), (255, 214, 90))
    else:                                                                              # 3) green print on the sheet ↔ her green mask
        src = PRINT_V if vert else PRINT_H; z = 1.0 + 0.05 * kk(lt, 9.6, 13.6)
        im = src.resize((int(Wd * z), int(Hd * z)), Image.LANCZOS).crop((int(Wd * (z - 1) / 2), int(Hd * (z - 1) / 2), int(Wd * (z - 1) / 2) + Wd, int(Hd * (z - 1) / 2) + Hd))
        fr = ImageEnhance.Brightness(im).enhance(1.25)
        if lt >= 11.65:                                                                # inset: her green mask from the same selfie
            face = PHOTO11.crop((250, 470, 520, 760)); fs = int((Wd * 0.42) if vert else (Hd * 0.42)); face = face.resize((fs, int(fs * 290 / 270)), Image.LANCZOS)
            fx, fy = (Wd * 0.5 - fs / 2, Hd * 0.12) if vert else (Wd * 0.7, Hd * 0.12)
            ImageDraw.Draw(fr).rounded_rectangle([fx - 10, fy - 10, fx + face.size[0] + 10, fy + face.size[1] + 10], 20, fill=(255, 255, 255))
            fr.paste(face, (int(fx), int(fy)))
            lzt(fr, fx + face.size[0] / 2, fy + face.size[1] + 50, "أخضر زي الماسك", int(52 * popk(lt, 11.65)), (140, 230, 120))
    by = Hd * (0.07 if vert else 0.08); bh = 120 if vert else 100; d = ImageDraw.Draw(fr, "RGBA")
    d.rectangle([0, by - bh / 2, Wd, by + bh / 2], fill=(30, 120, 60, 255)); lzt(fr, Wd / 2, by, "حل القضية 11", 80 if vert else 70, (255, 255, 255), (10, 40, 20))
    f = kk(tt, SEG1 - 0.3, SEG1)
    if f > 0: fr = Image.blend(fr, Image.new("RGB", fr.size, (0, 0, 0)), f)
    return fr

# ---------------- final card (the ONE ask) ----------------
def q_card(tt, sh, Wd, Hd):
    vert = Hd > Wd; fr = Image.new("RGB", (Wd, Hd), (40, 12, 14)); rays(fr, Wd, Hd, (58, 18, 20), tt, 0.5)
    g = 1.25 if vert else 1.0; cy = Hd * (0.16 if vert else 0.16)
    d = ImageDraw.Draw(fr, "RGBA"); d.rounded_rectangle([Wd / 2 - 210 * g, cy - 150 * g, Wd / 2 + 210 * g, cy - 70 * g], 30, fill=(200, 30, 40, 240))
    lzt(fr, Wd / 2, cy - 110 * g, "قضية 12", int(56 * g), (255, 255, 255), stroke=False)
    lzt(fr, Wd / 2, cy + 10 * g, "مين الكداب؟", int(120 * g * popk(tt, sh["start"] + 0.05, 0.3)), (255, 214, 90))
    lay = Image.new("RGBA", (int(Wd * SS), int(Hd * SS)), (0, 0, 0, 0)); p = P(lay)
    fy = Hd * (0.62 if vert else 0.74); sc = 2.1 if vert else 1.9
    for i, (who, col) in enumerate(NUMS):
        bx = Wd / 2 + (i - 1) * (300 if vert else 330) * (1 if vert else 1); u = popk(tt, sh["start"] + 0.2 + i * 0.15)
        if u > 0: draw_char(p, who, bx, fy, sc, "neutral", 0.0, 1 if i == 0 else -1 if i == 2 else 1, False, "down", tt, None, 0.0, None)
    L = lay.resize((Wd, Hd), Image.LANCZOS); fr.paste(L, (0, 0), L)
    for i, (who, col) in enumerate(NUMS):
        bx = Wd / 2 + (i - 1) * (300 if vert else 330); u = popk(tt, sh["start"] + 0.2 + i * 0.15)
        S_, _, (_, hy) = body(who, bx, fy, sc); badge(fr, bx, hy - 46 * S_ - 70, str(i + 1), 1.1 * g * u, col)
        lzt(fr, bx, fy + (60 if vert else 40), NAME[who][0], int(56 * g * u), (255, 255, 255))
    lzt(fr, Wd / 2, Hd * (0.82 if vert else 0.92), "اكتب رقم الكداب", int(70 * g * popk(tt, sh["start"] + 0.7)), (255, 255, 255))
    return fr

# ---------------- frames ----------------
def tag(fr, Wd, Hd, tt):
    if tt >= SEG0: return
    d = ImageDraw.Draw(fr, "RGBA"); vert = Hd > Wd; x, y = (Wd / 2, 200) if vert else (Wd - 150, 60)
    d.rounded_rectangle([x - 115, y - 32, x + 115, y + 32], 26, fill=(200, 30, 40, 220)); lzt(fr, x, y, "قضية 12", 44, (255, 255, 255), stroke=False)
def hook_text(fr, tt, Wd, Hd):
    if tt >= HOOK_END: return
    vert = Hd > Wd; a_ = int(255 * min(1, (HOOK_END - tt) / 0.3))
    lzt(fr, Wd / 2, Hd * (0.78 if vert else 0.84), "مين خد الجواب؟", int((110 if vert else 96) * popk(tt, 0.4, 0.3)), (255, 214, 90), alpha=a_)
def add_badges(fr, tt, Wd, Hd, cam):
    if tt < BADGES or shot_at(tt)["set"] != "lob6": return
    pos = {w: (x, y, s) for w, x, y, s, *_ in people(tt)}
    for i, (who, col) in enumerate(NUMS):
        if who not in pos: continue
        x, y, s = pos[who]; S_, _, (_, hy) = body(who, x, y + (62 * s if who == "bondo2" else 0), s); q = W2S(cam, x, hy - 46 * S_ - 40)
        if -120 < q[0] < Wd + 120: badge(fr, q[0], max(q[1], 110 if Hd < Wd else 330), str(i + 1), min(1.1, cam[2] * 0.6) * popk(tt, BADGES + i * 0.15), col)
def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "seg11": return finish(seg11(tt, W, H), tt)
    if sh["set"] == "q": return finish(q_card(tt, sh, W, H), tt)
    if sh["set"] == "hook": fr = hook_scene(tt, hcam(sh, tt), (W, H))
    else: cam = hcam(sh, tt); fr = scene(tt, sh, cam, (W, H)); add_badges(fr, tt, W, H, cam); fr = live_inset(fr, tt, W, H)
    hook_text(fr, tt, W, H); tag(fr, W, H, tt)
    return finish(fr, tt)
def subtitle(img, tt):
    if shot_at(tt)["set"] != "q": sub_chunk(img, tt, W / 2, H - 80, 62)
VIGV = VIG.resize((1080, 1920))
def vertical(_base, tt):
    sh = shot_at(tt); Wd, Hd = 1080, 1920
    if sh["set"] == "seg11": fr = seg11(tt, Wd, Hd); sub_chunk(fr, tt, 520, 1700, 72); return fr
    if sh["set"] == "q": fr = q_card(tt, sh, Wd, Hd); return fr
    if sh["set"] == "hook": fr = hook_scene(tt, vcam(sh, tt), (Wd, Hd))
    else:
        cam = vcam(sh, tt); fr = scene(tt, sh, cam, (Wd, Hd)); add_badges(fr, tt, Wd, Hd, cam)
        fr = ImageChops.multiply(fr, VIGV)
        u = tt - sh["start"]
        if sh.get("tin") == "whip" and u < 0.18: fr = fr.filter(ImageFilter.BoxBlur(int(2 + 18 * (1 - u / 0.18))))
        fr = live_inset(fr, tt, Wd, Hd)
    hook_text(fr, tt, Wd, Hd); tag(fr, Wd, Hd, tt); sub_chunk(fr, tt, 500, 1470, 76)
    return fr

# ---------------- audio ----------------
def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 3; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(12)
    mix_into(buf, tone(110, 0.9, 0.2, 3) + tone(165, 0.9, 0.12, 3), 0.0, 1.0)                             # frame-1 «dun»
    pap = lowpass(r.normal(0, 1, int(SR * 0.6)).astype(np.float32), 5000) * np.hanning(int(SR * 0.6)).astype(np.float32) * 0.12
    mix_into(buf, pap, 0.45, 1.0); mix_into(buf, SFXF["stinger"] * 0.3, 1.6, 1.0)
    dr = np.arange(int((SEG0 - HOOK_END) * SR)) / SR
    mix_into(buf, ((np.sin(2 * np.pi * 55 * dr) * 0.04 + np.sin(2 * np.pi * 82.5 * dr) * 0.02)).astype(np.float32), HOOK_END, 1.0)
    for f_, t_ in ((F5, 0), (F6, 0)): mix_into(buf, SFXF["whoosh"] * 0.2, f_ - 0.1, 1.0); mix_into(buf, tone(880, 0.25, 0.1, 8), f_ + 0.15, 1.0)
    mix_into(buf, pap * 0.7, POST[1] - 0.2, 1.0); mix_into(buf, tone(300, 0.08, 0.15, 30), POST[1], 1.0)        # into the slot + flap
    for j in range(3): mix_into(buf, tone(1300, 0.06, 0.06, 40), LIVE0 + j * 0.2, 1.0)                    # live «ding»
    mix_into(buf, tone(500, 0.35, 0.1, 6) + tone(380, 0.35, 0.1, 5), LIVE1, 1.0)                           # signal lost
    for j in range(5): mix_into(buf, tone(150, 0.08, 0.1, 30), NANA_IN[0] + j * 0.34, 1.0)               # steps down the stairs
    mix_into(buf, tone(260, 0.1, 0.18, 25), OPEN + 0.1, 1.0); mix_into(buf, SFXF["gasp"] * 0.25, T("N1") - 0.15, 1.0)
    mix_into(buf, tone(140, 0.12, 0.12, 20), Z_IN[0] + 0.1, 1.0)                                         # street door
    for i in range(3): mix_into(buf, tone(660 + i * 220, 0.18, 0.16, 12), BADGES + i * 0.15, 1.0)
    for k_, f in enumerate((523, 659, 784)): mix_into(buf, tone(f, 0.4, 0.14, 7), SEG0 + 0.1 + k_ * 0.08, 1.0)
    mix_into(buf, tone(1047, 0.5, 0.12, 6), T("S0") + 1.73, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.14, 6), Q + k_ * 0.09, 1.0)
    for s_ in shots:
        if s_.get("tin") == "whip": mix_into(buf, SFXF["whoosh"] * 0.15, s_["start"] - 0.1, 1.0)
    for st_, k in lines:
        a = AUD[k][:int(SR * SW2_END)] if k == "SW2" else AUD[k]
        v = a / max(1e-6, np.percentile(np.abs(a), 99.5)) * 0.8; mix_into(buf, v, st_, 1.0)
    write_wav(buf[:int(TOTAL * SR)], path)

def make_covers():
    def comp(Wd, Hd, vert):
        bg = ImageEnhance.Brightness(LOB6.crop((0, 0, 1100, 1080) if vert else (0, 0, 1920, 1080)).resize((Wd, Hd), Image.LANCZOS)).enhance(0.8)
        img = bg.resize((int(Wd * SS), int(Hd * SS))); d = ImageDraw.Draw(img, "RGBA")
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); p = P(lay)
        if vert:
            envelope(d, Wd * 0.72 * SS, Hd * 0.2 * SS, 7.5 * SS, -0.2)
            draw_char(p, "nana", Wd * 0.42, Hd * 0.98, 6.4, "shock", 0.6, 1, False, "up", 0.0, None, 0.0, None)
        else:
            envelope(d, Wd * 0.74 * SS, Hd * 0.38 * SS, 7.0 * SS, -0.2)
            draw_char(p, "nana", Wd * 0.3, Hd * 1.3, 5.0, "shock", 0.6, 1, False, "up", 0.0, None, 0.0, None)
        img.paste(lay, (0, 0), lay); fr = img.resize((Wd, Hd), Image.LANCZOS); d = ImageDraw.Draw(fr, "RGBA")
        if vert:
            d.rectangle([0, Hd * 0.535, Wd, Hd * 0.725], fill=(10, 6, 4, 160))
            lzt(fr, Wd / 2, Hd * 0.575, "مين خد", 160, (255, 255, 255)); lzt(fr, Wd / 2, Hd * 0.67, "الجواب؟", 170, (255, 214, 60))
            for i, (who, col) in enumerate(NUMS): badge(fr, Wd * (0.2 + 0.3 * i), Hd * 0.775, str(i + 1), 1.2, col)
            bx, by = Wd / 2, 130
        else:
            d.rectangle([0, Hd * 0.76, Wd, Hd * 0.97], fill=(10, 6, 4, 160)); lzt(fr, Wd * 0.58, Hd * 0.865, "مين خد الجواب؟", 150, (255, 214, 60)); bx, by = 1620, 90
        d = ImageDraw.Draw(fr, "RGBA"); d.rounded_rectangle([bx - 200, by - 46, bx + 200, by + 46], 34, fill=(200, 30, 40, 240))
        lzt(fr, bx, by, "مين الكداب؟ • قضية 12", 42, (255, 255, 255), stroke=False)
        return fr
    comp(1080, 1920, True).save(ROOT + "/publish/thumbs/kaddab_e12_cover.jpg", quality=92)
    comp(1920, 1080, False).resize((1280, 720), Image.LANCZOS).save(ROOT + "/publish/thumbs/kaddab_e12_yt.jpg", quality=92)

if __name__ == "__main__":
    print("TOTAL", round(TOTAL, 1))
    if sys.argv[1:2] == ["stills"]: render(None, None, [float(v) for v in sys.argv[2:]])
    elif sys.argv[1:2] == ["times"]:
        for s_ in shots: print(s_["set"], round(s_["start"], 2), round(s_["end"], 2), s_.get("tin", ""))
        for st, k in lines: print(k, round(st, 2))
        print("LIVE", round(LIVE0, 2), round(LIVE1, 2), "F6", round(F6, 2), "BADGES", round(BADGES, 2), "SEG", round(SEG0, 2), round(SEG1, 2))
    elif sys.argv[1:2] == ["part"]:
        i, n = int(sys.argv[2]), int(sys.argv[3]); a = round(TOTAL * i / n * FPS) / FPS; b = round(TOTAL * (i + 1) / n * FPS) / FPS
        render(f"h_{i}.mp4", f"v_{i}.mp4", None, a, b)
    elif sys.argv[1:2] == ["audio"]: build_audio()
    elif sys.argv[1:2] == ["cover"]: make_covers()
