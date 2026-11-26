# «مين الكداب؟» — القضية 13: «علبة عزيزة» — ACTION-CONTINUITY CUT (26/11, replaces the static ep13.py cut)
# Approved v2 voices: case13-voices-v2-raw.mp3 sliced per manifest.txt into audio/L1..L15 (lines intact, no speed change,
# no regeneration; only the pauses BETWEEN lines are re-timed so the action has room).
# Canonical places (rule 8): أوضة بندق وعزيزة = daily/bg/bandaq_room.png (under the stairs → they leave by the room door, no real stairs),
#   المدخل = s1e10/bg/morning.png (bench + mailboxes + street door), السطوح = s2e6/bg/roof_day.png. The box is drawn by code
#   (same box in the wide shot and in every close-up). Props drawn: side table + box, dough table, ball, sesame.
# Action follows the words: ring off → into the box → lid closed · «نازلين» → walk out of the room door → enter the lobby from the
#   same side → pass the doorman on his bench (Sawsan filming) → out of the street door (backs to camera) · Shatta on the roof with a
#   sesame sandwich · «الساعة ١٢ ونص» back in, lid opens → empty → two sesame seeds on the lid · everyone walks in → investigation
#   ① سوسن ② البواب ③ توتة ④ شطة → «حل القضية ١٢» → final card (the ONE ask). «خاتم» is never highlighted.
# ANSWER (start of case 14): شطة ④ — «ماشفتش أي خاتم» though nobody said ring in front of him (he was on the roof) + sesame on the lid.
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
exec(open(ROOT + "/trend/01/kit.py", encoding="utf-8").read())
from PIL import ImageFont, ImageChops
sys.path.insert(0, ROOT + "/s2"); import vnative as VN
os.chdir(ROOT + "/kaddab/13")
LZ = ROOT + "/brand/fonts/Lalezar-Regular.ttf"; DJ = ROOT + "/brand/fonts/DejaVuSans-Bold.ttf"
TXT = {1: "معلش يا خاتمي… العجينة أهم.", 2: "عجينتك أحلى يا خالتي!", 3: "أنا وتوتة نازلين لطنط فتحية نص ساعة… محدش يقرب من الأوضة!",
 4: "يا بندق، خاتمي في العلبة لحد ما أرجع… خد بالك!", 5: "وأنا صاحي أهو!", 6: "اتسرق!… اللي كان في العلبة اتاخد!",
 7: "من ١٢ لـ ١٢ ونص… كل واحد كان فين؟", 8: "أنا كنت في المدخل بصوّر لايف… وسمعت عزيزة وهي بتقول لبندق… وبعدين طلعت شقتي وما نزلتش تاني!",
 9: "أنا على الدكة من الصبح… واللي أعرفه سمعته من مراتي قدامكو… وأنا صاحي أهو!", 10: "أنا؟ أنا كنت مع خالتي عزيزة طول الوقت… من العجينة للزيارة والرجوع!",
 11: "صحيح… كانت معايا!", 12: "أنا على السطوح من ١٢… وماشفتش أي خاتم!", 13: "الدليل قدامكم… مين الكداب؟",
 14: "حل القضية ١٢: الكداب كان زلطة! قال «مختوم بالشمع»… ومحدش قالها قدامه خالص… فعرفها منين؟", 15: "مين الكداب؟ اكتب رقمه!"}
WHOL = {1: "aziza", 2: "tota", 3: "aziza", 4: "aziza", 5: "bondo2", 6: "aziza", 7: "nana", 8: "sawsan", 9: "bondo2", 10: "tota", 11: "aziza", 12: "shatta", 13: "nana", 14: "tota", 15: "tota"}
KEYS = [f"L{i}" for i in range(1, 16)]
WHO = {f"L{i}": WHOL[i] for i in TXT}
NAME = {"aziza": ("عزيزة", (255, 110, 170)), "tota": ("توتة", (255, 130, 190)), "nana": ("نعناعة", (150, 220, 190)), "sawsan": ("سوسن", (255, 170, 80)),
        "bondo2": ("البواب", (230, 170, 110)), "shatta": ("شطة", (255, 140, 80))}
EXPR = {"L1": "sad", "L2": "happy", "L3": [(0, "happy"), (2.6, "angry")], "L4": "neutral", "L5": "happy", "L6": "shock", "L7": "angry",
        "L8": "neutral", "L9": [(0, "sleepy"), (4.6, "happy")], "L10": [(0, "shock"), (0.8, "neutral")], "L11": "sad", "L12": "neutral",
        "L13": "smug", "L14": "smug", "L15": "smug"}
load_lines(KEYS)
CHV = {k: VN.chunk_times(TXT[int(k[1:])], ENV[k], FPS) for k in KEYS}          # phrase timing from the real voice envelope
VN.set_font(LZ)

ROOM = _ld(ROOT + "/daily/bg/bandaq_room.png"); LOB = _ld(ROOT + "/s1e10/bg/morning.png"); ROOF = _ld(ROOT + "/s2e6/bg/roof_day.png")
ROOM = ImageEnhance.Brightness(ROOM).enhance(1.05)
C12A = Image.open("c12a.png").convert("RGB").resize((1920, 1080)); C12B = Image.open("c12b.png").convert("RGB").resize((1920, 1080))
def W2S(cam, x, y): x0, y0, z = cam; return (x - x0) * z, (y - y0) * z
BOXP = (1515, 586)                      # the wooden box on the side table (room world coords)
SIDE = (1440, 596, 1590, 760)           # side table under the shelf
DOUGH = (700, 812, 960, 1000)           # dough table (top y 812)
DOOR = (300, 740)                       # room door (left)
FEET = 1000

# ---------------- timeline (lines intact; only the gaps between them are re-timed) ----------------
lines.clear(); shots.clear(); sfx.clear(); shakes.clear()
HOOK_END = 2.6
shot("cu", 0.0, HOOK_END, None, v=None, cu="hook")
R1 = HOOK_END                                                            # «الساعة ١٢» room
shot("room", R1, R1 + 1.2, (900, 600, 1.25), (930, 610, 1.32), v=((830, 620, 1.85), (840, 620, 1.9)), title="الساعة ١٢")
t = say(R1 + 1.15, "L1"); RINGOFF = T("L1") + 0.2
shot("room", R1 + 1.2, T("L1") + 0.85, (880, 620, 1.9), (900, 620, 2.05), v=((830, 640, 2.2), (840, 640, 2.3)))
WALK1 = (T("L1") + 0.3, T("L1") + 0.85)                                  # Aziza steps to the side table with the ring
CU1 = (T("L1") + 0.85, T("L1") + 3.0); RING_IN = CU1[0] + 0.65; LID_SHUT = CU1[0] + 1.45
shot("cu", CU1[0], CU1[1], None, v=None, cu="put")
t = say(CU1[1] + 0.05, "L2") + 0.2
shot("room", CU1[1], t, (1250, 620, 1.7), (1240, 620, 1.8), v=((1200, 640, 2.0), (1210, 640, 2.05)))
s = t; t = say(t + 0.05, "L3"); EXIT1 = (T("L3") + 1.6, T("L3") + 5.0)
shot("room", s, EXIT1[1] + 0.15, (1260, 600, 1.55), (700, 600, 1.35), v=((1300, 640, 1.9), (420, 640, 1.9)), follow=True)
L0 = EXIT1[1] + 0.15                                                      # lobby: enter from the same side they left (screen direction kept)
ENTER = (L0, L0 + 1.7)
shot("lob", L0, L0 + 1.7, (980, 600, 1.2), (900, 610, 1.25), v=((1350, 640, 1.85), (1000, 650, 1.9)), follow=True)
s = L0 + 1.7; t = say(s + 0.05, "L4") + 0.1
shot("lob", s, t, (700, 640, 1.55), (680, 640, 1.65), v=((800, 650, 1.9), (760, 650, 1.95)))
s = t; t = say(t + 0.05, "L5") + 0.2
shot("lob", s, t, (330, 600, 2.3), (330, 600, 2.45), v=((320, 610, 2.4), (320, 610, 2.5)), whip=True)
OUT = (t, t + 2.4)                                                        # out through the street door, backs to camera
shot("lob", t, OUT[1], (800, 600, 1.2), (780, 600, 1.25), v=((900, 640, 1.85), (760, 640, 1.9)), follow=True); t = OUT[1]
RF = (t, t + 2.3)                                                         # meanwhile: Shatta on the roof
shot("roof", t, RF[1], (900, 620, 1.35), (930, 640, 1.5), v=((900, 640, 1.85), (920, 640, 1.95)), whip=True); t = RF[1]
SES = (t, t + 1.3); shot("cu", t, SES[1], None, v=None, cu="sesame"); t = SES[1]
R2 = t                                                                    # «الساعة ١٢ ونص»: back in
BACK = (R2 + 0.3, R2 + 2.3)
shot("room", R2, BACK[1], (800, 600, 1.2), (1100, 600, 1.3), v=((420, 640, 1.85), (1400, 640, 1.9)), title="الساعة ١٢ ونص", whip=True, follow=True)
CU2 = (BACK[1], BACK[1] + 1.4); LID_OPEN = CU2[0] + 0.35
shot("cu", CU2[0], CU2[1], None, v=None, cu="open")
s = CU2[1]; t = say(s - 0.25, "L6") + 0.15; shakes.append((T("L6") + 0.05, 10))
shot("room", s, t, (1450, 560, 2.4), (1450, 560, 2.7), v=((1450, 600, 2.5), (1450, 600, 2.7)), crash=True)
SEEDS = (t, t + 1.6); shot("cu", t, SEEDS[1], None, v=None, cu="seeds"); t = SEEDS[1]
GATHER = (t, t + 2.2)                                                     # Nana arrives first, the others follow her in
shot("room", t, GATHER[1], (960, 600, 1.0), (960, 600, 1.05), v=((900, 640, 1.85), (700, 640, 1.85)), follow=True); t = GATHER[1]
s = t; t = say(t + 0.05, "L7") + 0.2; BADGES = t - 0.4
shot("room", s, t, (500, 640, 1.6), (520, 640, 1.7), v=((300, 650, 2.0), (310, 650, 2.05)))
INV = {"nana": (250, FEET, 1.42, 1), "sawsan": (520, FEET, 1.42, 1), "bondo2": (790, FEET, 1.42, 1), "tota": (1060, FEET, 1.42, -1),
       "shatta": (1330, FEET, 1.42, -1), "aziza": (1600, FEET, 1.45, -1)}
for k in ("L8", "L9", "L10", "L11", "L12", "L13"):
    s = t; t = say(t + 0.1, k) + 0.25; x_ = INV[WHO[k]][0]
    nb = 1 if k != "L11" else 0                                           # a neighbour stays in frame for the listener reaction
    shot("room", s, t, (x_, 640, 1.75), (x_, 640, 1.85), v=((x_, 650, 2.2), (x_, 650, 2.25)), whip=True)
SEG0 = t; s_ = say(t + 0.5, "L14"); SEG1 = s_ + 0.4
shot("c12", SEG0, SEG1, None, v=None); t = SEG1
Q = t; say(Q + 0.35, "L15"); t = Q + 0.35 + DUR["L15"] + 1.0
shot("q", Q, t, None, v=None)
TOTAL = t

def vcam(sh, tt):
    c0, c1 = sh["v"]; k = ease((tt - sh["start"]) / max(0.01, sh["end"] - sh["start"]))
    cx, cy, z = [a_ + (b_ - a_) * k for a_, b_ in zip(c0, c1)]; z = max(z, 1920 / 1080)
    if sh.get("follow"):                                                  # walking shots: the camera follows the walkers
        xs = [p[1] for p in cast_at(sh["set"], tt) if p[0] in ("aziza", "tota", "nana")]
        if xs: cx = sum(xs) / len(xs)
    shake = 0
    for st, amp in shakes:
        if 0 <= tt - st < 0.45: shake = max(shake, amp * (1 - (tt - st) / 0.45))
    cw, ch = 1080 / z, 1920 / z
    x0 = min(max(cx - cw / 2, 0), 1920 - cw); y0 = min(max(cy - ch / 2, 0), 1080 - ch)
    if shake: x0 = min(max(x0 + rng.normal(0, shake / z), 0), 1920 - cw)
    return x0, y0, z
def hcam(sh, tt):
    c0, c1 = sh["c0"], sh["c1"]; k = ease((tt - sh["start"]) / max(0.01, sh["end"] - sh["start"]))
    cx, cy, z = [a_ + (b_ - a_) * k for a_, b_ in zip(c0, c1)]
    if sh.get("follow"):
        xs = [p[1] for p in cast_at(sh["set"], tt) if p[0] in ("aziza", "tota", "nana")]
        if xs: cx = lerp(cx, sum(xs) / len(xs), 0.6)
    cw, ch = 1920 / z, 1080 / z
    return min(max(cx - cw / 2, 0), 1920 - cw), min(max(cy - ch / 2, 0), 1080 - ch), z

# ---------------- who is where (the continuity) ----------------
def walker(p0, p1, win, tt, rate=8):
    u = ease(kk(tt, *win)); return lerp(p0[0], p1[0], u), lerp(p0[1], p1[1], u), lerp(p0[2], p1[2], u), (tt * rate if 0 < kk(tt, *win) < 1 else None)
def cast_at(set_, tt):
    """[(who, x, y, s, look, arms, held, walk, sit)]"""
    C = []
    if set_ == "room" and tt < L0:                                        # 12:00 — kneading, ring, then out of the door
        ax, ay, as_, aw = walker((640, FEET, 1.55), (1380, FEET - 10, 1.5), WALK1, tt, 9)
        tx, ty, ts, tw = 1180, FEET, 1.4, None
        if tt >= EXIT1[0]:
            ax, ay, as_, aw = walker((1380, FEET - 10, 1.5), (DOOR[0] + 40, DOOR[1] + 20, 1.05), EXIT1, tt, 9)
            tx, ty, ts, tw = walker((1180, FEET, 1.4), (DOOR[0] + 120, DOOR[1] + 30, 0.98), (EXIT1[0] + 0.3, EXIT1[1]), tt, 9)
        if tt < EXIT1[1] - 0.05:
            held = "ring" if RINGOFF <= tt < CU1[0] + 0.1 else None
            aarms = "hold" if tt < RINGOFF else ("hold" if held else "down")
            C.append(("aziza", ax, ay, as_, 1 if tt < EXIT1[0] else -1, aarms, held, aw, 0))
            C.append(("tota", tx, ty, ts, -1, "down", None, tw, 0))
    elif set_ == "lob":
        C.append(("bondo2", 300, 760, 1.3, 1, "down", None, None, 1))
        C.append(("sawsan", 520, 1020, 1.5, 1, "phone", "phone", None, 0))
        if tt < OUT[1] - 0.05:
            ax, ay, as_, aw = walker((2080, 1040, 1.6), (900, 1040, 1.6), ENTER, tt, 9)
            tx, ty, ts, tw = walker((2300, 1040, 1.45), (1150, 1040, 1.45), ENTER, tt, 9)
            if tt >= OUT[0]:
                ax, ay, as_, aw = walker((900, 1040, 1.6), (745, 640, 0.75), OUT, tt, 9)
                tx, ty, ts, tw = walker((1150, 1040, 1.45), (790, 645, 0.7), (OUT[0] + 0.25, OUT[1]), tt, 9)
            C.append(("aziza", ax, ay, as_, -1, "down", None, aw, 0)); C.append(("tota", tx, ty, ts, -1, "down", None, tw, 0))
    elif set_ == "roof":
        C.append(("shatta", 900 + 60 * math.sin((tt - RF[0]) * 2.2), 980, 1.6, 1 if math.sin((tt - RF[0]) * 2.2) > 0 else -1, "hold", "sandwich", tt * 8, 0))
    elif set_ == "room":                                                  # 12:30 — back in, then the investigation
        if tt < GATHER[0]:
            ax, ay, as_, aw = walker((DOOR[0] + 40, DOOR[1] + 20, 1.05), (1450, FEET - 10, 1.5), BACK, tt, 9)
            tx, ty, ts, tw = walker((DOOR[0] + 60, DOOR[1] + 30, 0.98), (1180, FEET, 1.4), (BACK[0] + 0.25, BACK[1]), tt, 9)
            C.append(("aziza", ax, ay, as_, 1, "point" if tt >= BACK[1] else "down", None, aw, 0)); C.append(("tota", tx, ty, ts, 1, "down", None, tw, 0))
        else:
            for i, who in enumerate(("nana", "sawsan", "bondo2", "shatta")):
                p1 = INV[who]; win = (GATHER[0] + i * 0.28, GATHER[0] + 1.3 + i * 0.28)
                x, y, s, w = walker((DOOR[0] + 40, DOOR[1] + 20, 1.0), p1[:3], win, tt, 9)
                if tt >= win[0]: C.append((who, x, y, s, 1 if w else p1[3], "down", "phone" if who == "sawsan" else None, w, 0))
            x, y, s, w = walker((1180, FEET, 1.4), INV["tota"][:3], (GATHER[0], GATHER[0] + 1.2), tt, 8); C.append(("tota", x, y, s, -1, "down", None, w, 0))
            x, y, s, w = walker((1450, FEET - 10, 1.5), INV["aziza"][:3], (GATHER[0], GATHER[0] + 1.0), tt, 8); C.append(("aziza", x, y, s, -1, "down", None, w, 0))
    return C

def draw_cast(lay, cam, set_, tt):
    k, lt = line_at(tt)
    for who, x, y, s, look, arms, held, walk, sit in cast_at(set_, tt):
        talking = k is not None and WHO.get(k) == who
        if talking: e = expr_of(k, lt)
        elif set_ == "room" and tt >= GATHER[1]: e = {"nana": "smug", "aziza": "sad"}.get(who, "scared" if k in ("L7", "L13") else "neutral")
        elif set_ == "room" and tt >= LID_OPEN: e = "shock"
        else: e = {"bondo2": "sleepy", "sawsan": "happy", "shatta": "happy"}.get(who, "happy")
        if who == "bondo2" and k == "L4": e = "neutral"
        mouth = float(ENV[k][min(int(lt * FPS) + 2, len(ENV[k]) - 1)]) if talking else 0.0
        a = arms
        if talking and arms == "down": a = "talk"
        if who == "aziza" and set_ == "room" and tt < RINGOFF and walk is None: a = "hold" if int(tt * 3) % 2 else "talk"     # kneading
        if who == "nana" and k == "L13": a = "point"
        if who == "aziza" and k == "L6": a = "up"
        X, Y_ = W2S(cam, x, y); S = s * cam[2]
        lean = 0.12 * math.sin(tt * 6) if (who == "aziza" and set_ == "room" and tt < RINGOFF) else 0.0
        draw_char(P(lay), who, X, Y_, S, e, mouth, look, ((tt + len(who) * 0.37) % 3.6) < 0.11 and e != "sleepy", a, tt, held, lean, walk, sit=sit)

# ---------------- props ----------------
def side_table(d, QW, zz):
    a, b = QW(SIDE[0], SIDE[1]), QW(SIDE[2], SIDE[3])
    d.rectangle([a[0], a[1], b[0], a[1] + 14 * zz], fill=(120, 74, 40), outline=(60, 34, 14))
    for lx in (SIDE[0] + 12, SIDE[2] - 22):
        q0, q1 = QW(lx, SIDE[1] + 14), QW(lx + 10, SIDE[3]); d.rectangle([q0[0], q0[1], q1[0], q1[1]], fill=(100, 60, 30))
def box_small(d, QW, zz, open_):
    q = QW(*BOXP); w, h = 30 * zz, 18 * zz
    d.rectangle([q[0] - w, q[1] - h, q[0] + w, q[1] + 4 * zz], fill=(140, 86, 44), outline=(60, 34, 14), width=max(1, int(2 * zz)))
    if open_: d.polygon([(q[0] - w, q[1] - h), (q[0] + w, q[1] - h), (q[0] + w * 0.8, q[1] - h * 2.6), (q[0] - w * 0.8, q[1] - h * 2.6)], fill=(156, 96, 50), outline=(60, 34, 14))
    else: d.rectangle([q[0] - w - 2 * zz, q[1] - h - 6 * zz, q[0] + w + 2 * zz, q[1] - h + 2 * zz], fill=(156, 96, 50), outline=(60, 34, 14))
def dough_table(d, QW, zz, tt):
    a, b = QW(DOUGH[0], DOUGH[1]), QW(DOUGH[2], DOUGH[3])
    for lx in (DOUGH[0] + 14, DOUGH[2] - 28):
        q0, q1 = QW(lx, DOUGH[1] + 20), QW(lx + 14, DOUGH[3]); d.rectangle([q0[0], q0[1], q1[0], q1[1]], fill=(110, 66, 34))
    d.rectangle([a[0], a[1], b[0], a[1] + 22 * zz], fill=(150, 98, 56), outline=(70, 40, 18))
    c = QW((DOUGH[0] + DOUGH[2]) / 2, DOUGH[1] - 8); sq = 1 + 0.08 * math.sin(tt * 9) if tt < RINGOFF else 1
    d.ellipse([c[0] - 62 * zz * sq, c[1] - 26 * zz / sq, c[0] + 62 * zz * sq, c[1] + 12 * zz], fill=(246, 232, 205), outline=(200, 180, 150))
def door_open(d, QW, zz, amt):
    if amt <= 0: return
    a, b = QW(190, 212), QW(420, 742)
    d.rectangle([a[0], a[1], a[0] + (b[0] - a[0]) * amt, b[1]], fill=(28, 20, 14, int(255 * min(1, amt * 1.5))))

def scene(tt, sh, cam, size):
    Wd, Hd = size; x0, y0, z = cam; set_ = sh["set"]
    src = {"room": ROOM, "lob": LOB, "roof": ROOF}[set_]
    img = src.resize((int(Wd * SS), int(Hd * SS)), Image.BICUBIC, box=(x0, y0, x0 + Wd / z, y0 + Hd / z))
    zz = z * SS; QW = lambda x, y: ((x - x0) * zz, (y - y0) * zz); d = ImageDraw.Draw(img, "RGBA")
    if set_ == "room":
        side_table(d, QW, zz); box_small(d, QW, zz, open_=(tt < LID_SHUT or tt >= LID_OPEN))
        if tt < L0: dough_table(d, QW, zz, tt)
        dopen = max(kk(tt, EXIT1[1] - 1.2, EXIT1[1] - 0.8) * (1 - kk(tt, EXIT1[1], EXIT1[1] + 0.1)) if tt < L0 else 0,
                    kk(tt, R2, R2 + 0.3) * (1 - kk(tt, BACK[0] + 1.2, BACK[0] + 1.5)) if R2 <= tt < GATHER[0] else 0,
                    kk(tt, GATHER[0] - 0.1, GATHER[0] + 0.2) * (1 - kk(tt, GATHER[0] + 2.0, GATHER[1])) if tt >= GATHER[0] else 0)
        door_open(d, QW, zz, dopen)
    if set_ == "roof":
        u = (tt - RF[0]); bx, by = 1000 + 260 * math.sin(u * 2.2), 960 - abs(math.sin(u * 5.0)) * 160; q = QW(bx, by); r = 22 * zz
        d.ellipse([q[0] - r, q[1] - r, q[0] + r, q[1] + r], fill=(250, 250, 250), outline=(30, 30, 30), width=max(1, int(2 * zz)))
        d.polygon([(q[0], q[1] - r * 0.4), (q[0] + r * 0.4, q[1]), (q[0], q[1] + r * 0.4), (q[0] - r * 0.4, q[1])], fill=(30, 30, 30))
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); draw_cast(lay, cam, set_, tt)
    lay = tint_layer(lay, (255, 240, 222)); img.paste(lay, (0, 0), lay)
    fr = img.resize((Wd, Hd), Image.LANCZOS)
    if sh.get("title"): lzt(fr, Wd / 2, Hd * (0.12 if Hd > Wd else 0.13), sh["title"], int(84 * popk(tt, sh["start"] + 0.1) * (1 - kk(tt, sh["start"] + 1.6, sh["start"] + 2.0))), (255, 230, 150))
    return fr

# ---------------- close-up inserts (same box as the wide shot) ----------------
def cu_box(tt, sh, Wd, Hd):
    kind = sh["cu"]; vert = Hd > Wd; u = tt - sh["start"]
    zc = 5.2; cw, ch = Wd / zc, Hd / zc
    cam = (BOXP[0] - cw / 2, BOXP[1] - ch * 0.6, zc)
    if kind == "sesame":
        bw_, bh_ = (380, 675) if vert else (600, 338)
        fr = ROOF.resize((Wd, Hd), Image.BICUBIC, box=(700, 1080 - bh_, 700 + bw_, 1080)).filter(ImageFilter.GaussianBlur(3))
        d = ImageDraw.Draw(fr, "RGBA"); s = (1.7 if vert else 1.25)
        cx, cy = Wd / 2 + 40 * math.sin(u * 3), Hd * 0.34
        d.ellipse([cx - 230 * s, cy - 80 * s, cx + 230 * s, cy + 80 * s], fill=(214, 160, 90), outline=(130, 80, 30), width=6)
        d.ellipse([cx - 210 * s, cy - 60 * s, cx + 210 * s, cy + 10 * s], fill=(232, 182, 110))
        d.rectangle([cx - 200 * s, cy + 10 * s, cx + 200 * s, cy + 30 * s], fill=(250, 220, 150))                      # white cheese
        d.line([(cx + 120 * s, cy + 40 * s), (Wd + 100, Hd * 0.75)], fill=(255, 140, 80), width=int(46 * s))            # Shatta's orange sleeve
        d.ellipse([cx + 80 * s, cy + 10 * s, cx + 160 * s, cy + 70 * s], fill=(240, 205, 175), outline=(60, 40, 30), width=4)
        r2 = np.random.default_rng(3)
        for i in range(26):
            sx, sy = cx + r2.uniform(-190, 190) * s, cy + r2.uniform(-55, 5) * s
            d.ellipse([sx - 7 * s, sy - 3.5 * s, sx + 7 * s, sy + 3.5 * s], fill=(250, 240, 210), outline=(170, 150, 110))
        for i in range(10):                                                                                         # seeds falling
            sx = cx + r2.uniform(-170, 170) * s; sy = cy + 60 * s + ((u * 520 + i * 90) % (Hd * 0.55))
            d.ellipse([sx - 8 * s, sy - 4 * s, sx + 8 * s, sy + 4 * s], fill=(250, 240, 210), outline=(170, 150, 110))
        return fr
    fr = ROOM.resize((Wd, Hd), Image.BICUBIC, box=(cam[0], cam[1], cam[0] + cw, cam[1] + ch))
    fr = fr.filter(ImageFilter.GaussianBlur(2.5)); d = ImageDraw.Draw(fr, "RGBA")
    if kind == "hook" or kind == "seeds": fr = ImageEnhance.Brightness(fr).enhance(0.8); d = ImageDraw.Draw(fr, "RGBA")
    s = 1.0 if not vert else 0.95; push = 1 + (0.06 * kk(u, 0, 2.6) if kind == "hook" else 0.04 * kk(u, 0, 2.0))
    if kind == "seeds": push = 1.25 + 0.15 * kk(u, 0, 1.6)
    S_ = s * push * (1.0 if not vert else 1.25)
    cx, cy = Wd / 2, Hd * (0.58 if not vert else 0.55)
    d.rectangle([0, cy + 120 * S_, Wd, Hd], fill=(110, 68, 36)); d.rectangle([0, cy + 120 * S_, Wd, cy + 140 * S_], fill=(140, 90, 50))  # table top
    bw, bh = 300 * S_, 170 * S_
    d.rectangle([cx - bw, cy - bh * 0.3, cx + bw, cy + 120 * S_], fill=(140, 86, 44), outline=(60, 34, 14), width=8)
    d.rectangle([cx - bw + 26 * S_, cy - bh * 0.3 + 16 * S_, cx + bw - 26 * S_, cy + 40 * S_], fill=(150, 20, 40))         # red velvet
    d.ellipse([cx - 34 * S_, cy - 6 * S_, cx + 34 * S_, cy + 30 * S_], fill=(120, 10, 30))                                # ring slot
    if kind == "hook": ang = kk(u, 0.15, 0.55)                     # lid flips open on frame 1
    elif kind == "put": ang = 1 - kk(u, 1.25, 1.5)
    elif kind == "open": ang = kk(u, 0.35, 0.65)
    else: ang = 1.0
    ring_in = kind == "put" and u >= 0.65
    if ring_in and ang > 0.02:
        d.ellipse([cx - 30 * S_, cy - 14 * S_, cx + 30 * S_, cy + 20 * S_], outline=(230, 185, 40), width=int(9 * S_))
        d.ellipse([cx - 9 * S_, cy - 30 * S_, cx + 9 * S_, cy - 12 * S_], fill=(210, 245, 255), outline=(130, 170, 210))
    lh = bh * 1.5 * ang                                            # lid (hinged at the back edge)
    top = cy - bh * 0.3
    if ang > 0.02:
        d.polygon([(cx - bw, top), (cx + bw, top), (cx + bw * 0.92, top - lh), (cx - bw * 0.92, top - lh)], fill=(160, 100, 52), outline=(60, 34, 14))
        d.polygon([(cx - bw * 0.85, top - 6), (cx + bw * 0.85, top - 6), (cx + bw * 0.8, top - lh * 0.9), (cx - bw * 0.8, top - lh * 0.9)], fill=(140, 18, 36))
        if kind in ("hook", "seeds", "open") and ang > 0.5:                                             # the clue: sesame on the lid
            for dx, dy in ((-0.25, 0.45), (0.12, 0.62)):
                sx, sy = cx + bw * dx, top - lh * dy; r = 9 * S_
                d.ellipse([sx - r * 1.8, sy - r, sx + r * 1.8, sy + r], fill=(250, 240, 210), outline=(150, 130, 90), width=2)
    else:
        d.rectangle([cx - bw - 8, top - 26 * S_, cx + bw + 8, top + 8], fill=(160, 100, 52), outline=(60, 34, 14), width=8)
    # hands
    if kind == "put" and u < 1.6:                                  # Aziza's hand lays the ring in, then pushes the lid shut
        k1 = kk(u, 0.0, 0.6); k2 = kk(u, 0.9, 1.3)
        hx = lerp(Wd + 60, cx + 20 * S_, ease(k1)); hy = lerp(cy - 260 * S_, cy - 40 * S_, ease(k1))
        if u > 0.8: hx = lerp(cx + 20 * S_, cx + 80 * S_, ease(k2)); hy = lerp(cy - 40 * S_, top - lh * 0.8 - 30 * S_, ease(k2))
        d.line([(Wd + 200, hy - 260 * S_), (hx, hy)], fill=(255, 110, 170), width=int(34 * S_))
        d.ellipse([hx - 30 * S_, hy - 26 * S_, hx + 30 * S_, hy + 26 * S_], fill=(240, 205, 175), outline=(60, 40, 30), width=4)
        if not ring_in:
            d.ellipse([hx - 20 * S_, hy - 40 * S_, hx + 20 * S_, hy - 6 * S_], outline=(230, 185, 40), width=int(8 * S_))
    if kind in ("hook", "open"):                                   # trembling hand on the lid
        tr = 6 * math.sin(tt * 40) if kind == "hook" else 0
        hx, hy = cx + bw * 0.7 + tr, top - lh * 0.95
        d.line([(Wd + 200, hy - 200 * S_), (hx, hy)], fill=(255, 110, 170), width=int(34 * S_))
        d.ellipse([hx - 30 * S_, hy - 26 * S_, hx + 30 * S_, hy + 26 * S_], fill=(240, 205, 175), outline=(60, 40, 30), width=4)
    if kind == "seeds":
        sx, sy = cx - bw * 0.06, top - lh * 0.55; r = 150 * S_ * popk(u, 0.2, 0.3)
        if r > 0: d.ellipse([sx - r, sy - r * 0.7, sx + r, sy + r * 0.7], outline=(255, 214, 60), width=8)
    return fr

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
    d = ImageDraw.Draw(fr, "RGBA"); r = 44 * sc
    d.ellipse([x - r, y - r, x + r, y + r], fill=col + (255,), outline=(255, 255, 255, 255), width=max(1, int(6 * sc)))
    lzt(fr, x, y + 4 * sc, n, int(66 * sc), (255, 255, 255), font=DJ)
_src = open(ROOT + "/brand/pro.py", encoding="utf-8").read()
exec(_src[_src.index("CHILI = "):_src.index("def radial")])
os.chdir(ROOT + "/kaddab/13")
NUMS = (("sawsan", (230, 120, 40)), ("bondo2", (150, 96, 50)), ("tota", (220, 80, 150)), ("shatta", (230, 90, 40)))
def add_badges(fr, tt, sh, cam):
    if sh["set"] != "room" or tt < BADGES: return
    Wd, Hd = fr.size
    for i, (who, col) in enumerate(NUMS):
        x, y, s, _ = INV[who]; S_ = s * CH[who]["scale"]; q = W2S(cam, x, y - (134 + 56) * S_ - 95 * S_)
        if -100 < q[0] < Wd + 100: badge(fr, q[0], max(q[1], 120 if Hd < Wd else 300), str(i + 1), min(1.15, cam[2] * 0.55) * popk(tt, BADGES + i * 0.12), col)

def seg12(tt, Wd, Hd):
    vert = Hd > Wd; lt = tt - T("L14"); src = C12A if lt < 4.2 else C12B
    if vert:
        cx = 1185 if src is C12A else 960; cw = 1080 * 1080 / 1920
        fr = src.resize((Wd, Hd), Image.LANCZOS, box=(cx - cw / 2, 0, cx + cw / 2, 1080))
    else: fr = src.copy()
    fr = ImageEnhance.Brightness(fr).enhance(0.85); d = ImageDraw.Draw(fr, "RGBA")
    if src is C12A and lt > 0.9:                                                         # circle the case-12 liar
        cx, cy = (Wd / 2, Hd * 0.6) if vert else (1185, 640); r = (230 if vert else 150) * popk(lt, 0.9)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(110, 220, 255), width=10)
    by = Hd * (0.06 if vert else 0.07); bh = 120 if vert else 100
    d.rectangle([0, by - bh / 2, Wd, by + bh / 2], fill=(30, 120, 60, 255)); lzt(fr, Wd / 2, by, "حل القضية ١٢", 78 if vert else 70, (255, 255, 255), (10, 40, 20))
    return fr
def q_card(tt, sh, Wd, Hd):
    vert = Hd > Wd; fr = Image.new("RGB", (Wd, Hd), (40, 12, 14)); d = ImageDraw.Draw(fr, "RGBA")
    for i in range(18):
        a0 = math.radians(i * 20 + tt * 6); b = a0 + math.radians(9); R = 3000
        d.polygon([(Wd / 2, Hd * 0.5), (Wd / 2 + R * math.cos(a0), Hd * 0.5 + R * math.sin(a0)), (Wd / 2 + R * math.cos(b), Hd * 0.5 + R * math.sin(b))], fill=(58, 18, 20))
    g = 1.25 if vert else 1.0; cy = Hd * 0.15
    d.rounded_rectangle([Wd / 2 - 210 * g, cy - 150 * g, Wd / 2 + 210 * g, cy - 70 * g], 30, fill=(200, 30, 40, 240))
    lzt(fr, Wd / 2, cy - 110 * g, "قضية ١٣", int(56 * g), (255, 255, 255), stroke=False)
    lzt(fr, Wd / 2, cy + 10 * g, "مين الكداب؟", int(120 * g * popk(tt, sh["start"] + 0.05, 0.3)), (255, 214, 90))
    lay = Image.new("RGBA", (int(Wd * SS), int(Hd * SS)), (0, 0, 0, 0)); p = P(lay)
    pos = [(Wd * (0.3 + 0.4 * (j % 2)), Hd * (0.45 + 0.31 * (j // 2))) for j in range(4)] if vert else [(Wd * (0.2 + 0.2 * j), Hd * 0.76) for j in range(4)]
    sc = 1.4 if vert else 1.6
    for (who, col), (x, y) in zip(NUMS, pos):
        if popk(tt, sh["start"] + 0.2) > 0: draw_char(p, who, x, y, sc, "neutral", 0.0, 1, False, "down", tt, None, 0.0, None)
    L = lay.resize((Wd, Hd), Image.LANCZOS); fr.paste(L, (0, 0), L)
    for i, ((who, col), (x, y)) in enumerate(zip(NUMS, pos)):
        u = popk(tt, sh["start"] + 0.2 + i * 0.12); S_ = sc * CH[who]["scale"]
        badge(fr, x, y - (134 + 56) * S_ - 90 * S_, str(i + 1), 1.0 * g * u, col)
        lzt(fr, x, y + (46 if vert else 40), NAME[who][0], int(50 * g * u), (255, 255, 255))
    lzt(fr, Wd / 2, Hd * (0.92 if vert else 0.94), "اكتب رقم الكداب", int(66 * g * popk(tt, sh["start"] + 0.6)), (255, 255, 255))
    return fr

def hook_text(fr, tt, Wd, Hd):
    if tt >= HOOK_END: return
    vert = Hd > Wd; a_ = int(255 * min(1, (HOOK_END - tt) / 0.3))
    lzt(fr, Wd / 2, Hd * (0.2 if vert else 0.16), "مين فتح العلبة؟", int((116 if vert else 100) * popk(tt, 0.5, 0.3)), (255, 214, 90), alpha=a_)
def tag(fr, Wd, Hd, tt):
    if tt >= SEG0: return
    d = ImageDraw.Draw(fr, "RGBA"); vert = Hd > Wd; x, y = (Wd / 2, 110) if vert else (Wd - 150, 60)
    d.rounded_rectangle([x - 110, y - 32, x + 110, y + 32], 26, fill=(200, 30, 40, 220)); lzt(fr, x, y, "قضية ١٣", 42, (255, 255, 255), stroke=False)

def frame(tt):
    sh = shot_at(tt)
    if sh["set"] == "c12": return finish(seg12(tt, W, H), tt)
    if sh["set"] == "q": return finish(q_card(tt, sh, W, H), tt)
    if sh["set"] == "cu": fr = cu_box(tt, sh, W, H)
    else: cam = hcam(sh, tt); fr = scene(tt, sh, cam, (W, H)); add_badges(fr, tt, sh, cam)
    hook_text(fr, tt, W, H); tag(fr, W, H, tt)
    return finish(fr, tt)
def subtitle(img, tt):
    if shot_at(tt)["set"] != "q": k, lt = line_at(tt); VN.sub_v(img, k, lt, CHV, VWHO(k), cy=H - 80, size=60)
def VWHO(k): return WHO.get(k) if k else None
VN.NAMES.update({w: NAME[w] for w in NAME})
VIGV = VIG.resize((1080, 1920))
def vertical(_base, tt):
    sh = shot_at(tt); Wd, Hd = 1080, 1920
    if sh["set"] == "c12": fr = seg12(tt, Wd, Hd)
    elif sh["set"] == "q": return q_card(tt, sh, Wd, Hd)
    elif sh["set"] == "cu": fr = cu_box(tt, sh, Wd, Hd)
    else:
        cam = vcam(sh, tt); fr = scene(tt, sh, cam, (Wd, Hd)); add_badges(fr, tt, sh, cam); fr = ImageChops.multiply(fr, VIGV)
        if sh.get("whip") and tt - sh["start"] < 0.16: fr = fr.filter(ImageFilter.BoxBlur(int(2 + 16 * (1 - (tt - sh["start"]) / 0.16))))
    hook_text(fr, tt, Wd, Hd); tag(fr, Wd, Hd, tt)
    k, lt = line_at(tt)
    cy = {"c12": 330, "cu": 1700}.get(sh["set"], 560)                         # clear of the characters: wall area above their heads
    VN.sub_v(fr, k, lt, CHV, VWHO(k), cy=cy, size=74)
    return fr

# ---------------- audio ----------------
def tone(f, dur, amp, decay=3.0):
    d_ = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * d_) * np.exp(-d_ * decay) * amp).astype(np.float32)
SFXF = {n: load_audio(ROOT + f"/trend/01/sfx/{n}.mp3") for n in ("whoosh", "stinger", "gasp")}
def build_audio(path="mix.wav"):
    n = int(TOTAL * SR) + SR * 3; buf = np.zeros(n, dtype=np.float32); r = np.random.default_rng(13)
    mix_into(buf, tone(300, 0.12, 0.25, 20), 0.15, 1.0); mix_into(buf, tone(180, 0.6, 0.15, 4), 0.15, 1.0)                    # lid snaps open, frame 1
    mix_into(buf, SFXF["stinger"] * 0.3, 0.5, 1.0)
    for f_ in (R1, R2): mix_into(buf, tone(880, 0.25, 0.1, 8), f_ + 0.15, 1.0)
    mix_into(buf, tone(2200, 0.1, 0.08, 30), CU1[0] + 0.65, 1.0); mix_into(buf, tone(260, 0.12, 0.25, 22), CU1[0] + 1.5, 1.0)   # ring clink + lid clack
    for a_, b_ in ((EXIT1[0], EXIT1[1]), (ENTER[0], ENTER[1]), (OUT[0], OUT[1]), (BACK[0], BACK[1]), (GATHER[0], GATHER[1])):
        for j in range(int((b_ - a_) / 0.32)): mix_into(buf, tone(150, 0.07, 0.08, 30), a_ + j * 0.32, 1.0)   # footsteps
    for dt in (EXIT1[1] - 1.0, R2 + 0.05, GATHER[0] - 0.05): mix_into(buf, tone(140, 0.4, 0.1, 6), dt, 1.0)  # door
    for j in range(int((RF[1] - RF[0]) / 0.45)): mix_into(buf, tone(95, 0.12, 0.18, 25), RF[0] + 0.2 + j * 0.45, 1.0)   # ball bounces
    mix_into(buf, tone(300, 0.12, 0.25, 20), LID_OPEN, 1.0); mix_into(buf, SFXF["gasp"] * 0.25, T("L6") - 0.15, 1.0)
    mix_into(buf, tone(220, 0.5, 0.14, 5), SEEDS[0] + 0.2, 1.0); mix_into(buf, tone(330, 0.5, 0.1, 5), SEEDS[0] + 0.2, 1.0)
    dr = np.arange(int((SEG0 - HOOK_END) * SR)) / SR
    mix_into(buf, ((np.sin(2 * np.pi * 55 * dr) * 0.035 + np.sin(2 * np.pi * 82.5 * dr) * 0.018)).astype(np.float32), HOOK_END, 1.0)
    for i in range(4): mix_into(buf, tone(660 + i * 165, 0.18, 0.14, 12), BADGES + i * 0.12, 1.0)
    for k_, f in enumerate((523, 659, 784)): mix_into(buf, tone(f, 0.4, 0.13, 7), SEG0 + 0.1 + k_ * 0.08, 1.0)
    for k_, f in enumerate((784, 988, 1175, 1568)): mix_into(buf, tone(f, 0.4, 0.13, 6), Q + k_ * 0.09, 1.0)
    for s_ in shots:
        if s_.get("whip"): mix_into(buf, SFXF["whoosh"] * 0.14, s_["start"] - 0.1, 1.0)
    for st_, k in lines:
        a = AUD[k]; v = a / max(1e-6, np.percentile(np.abs(a), 99.5)) * 0.8; mix_into(buf, v, st_, 1.0)
    write_wav(buf[:int(TOTAL * SR)], path)

def make_covers():
    def comp(Wd, Hd, vert):
        fr = cu_box(1.6, {"cu": "hook", "start": 0.0}, Wd, Hd); fr = ImageEnhance.Brightness(fr).enhance(0.9)
        img = fr.resize((int(Wd * SS), int(Hd * SS))); lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); p = P(lay)
        if vert: draw_char(p, "aziza", Wd * 0.3, Hd * 0.62, 3.6, "shock", 0.6, 1, False, "up", 0.0, None, 0.0, None)
        else: draw_char(p, "aziza", Wd * 0.2, Hd * 1.15, 4.2, "shock", 0.6, 1, False, "up", 0.0, None, 0.0, None)
        img.paste(lay, (0, 0), lay); fr = img.resize((Wd, Hd), Image.LANCZOS); d = ImageDraw.Draw(fr, "RGBA")
        if vert:
            d.rectangle([0, Hd * 0.66, Wd, Hd * 0.86], fill=(10, 6, 4, 170))
            lzt(fr, Wd / 2, Hd * 0.71, "مين فتح", 160, (255, 255, 255)); lzt(fr, Wd / 2, Hd * 0.8, "العلبة؟", 170, (255, 214, 60))
            for i, (who, col) in enumerate(NUMS): badge(fr, Wd * (0.17 + 0.22 * i), Hd * 0.91, str(i + 1), 1.1, col)
            bx, by = Wd / 2, 120
        else:
            d.rectangle([0, Hd * 0.78, Wd, Hd * 0.97], fill=(10, 6, 4, 170)); lzt(fr, Wd * 0.58, Hd * 0.875, "مين فتح العلبة؟", 150, (255, 214, 60)); bx, by = 1620, 90
        d = ImageDraw.Draw(fr, "RGBA"); d.rounded_rectangle([bx - 200, by - 46, bx + 200, by + 46], 34, fill=(200, 30, 40, 240))
        lzt(fr, bx, by, "مين الكداب؟ • قضية ١٣", 42, (255, 255, 255), stroke=False)
        return fr
    comp(1080, 1920, True).save(ROOT + "/publish/thumbs/kaddab_e13_cover.jpg", quality=92)
    comp(1920, 1080, False).resize((1280, 720), Image.LANCZOS).save(ROOT + "/publish/thumbs/kaddab_e13_yt.jpg", quality=92)

def contact_sheet(path="speaker_check.jpg"):
    """one frame per line (vertical + horizontal) at the middle of the line: the name tag must match the speaker on screen"""
    tiles = []
    for st_, k in lines:
        tt = st_ + DUR[k] * 0.55; v = vertical(None, tt).resize((270, 480)); h = frame(tt).copy(); subtitle(h, tt); h = h.resize((480, 270))
        tile = Image.new("RGB", (760, 520), (20, 20, 24)); tile.paste(v, (5, 35)); tile.paste(h, (275, 35))
        lzt(tile, 380, 18, f"{k} • {NAME[WHO[k]][0]} • {tt:.1f}s", 26, (255, 214, 90), stroke=False); tiles.append(tile)
    cols = 3; rows = -(-len(tiles) // cols); sheet = Image.new("RGB", (760 * cols, 520 * rows), (10, 10, 12))
    for i, t_ in enumerate(tiles): sheet.paste(t_, ((i % cols) * 760, (i // cols) * 520))
    sheet.save(path, quality=88)

if __name__ == "__main__":
    print("TOTAL", round(TOTAL, 1))
    if sys.argv[1:2] == ["stills"]: render(None, None, [float(v) for v in sys.argv[2:]])
    elif sys.argv[1:2] == ["times"]:
        for s_ in shots: print(s_["set"], round(s_["start"], 2), round(s_["end"], 2), s_.get("cu", ""))
        for st, k in lines: print(k, round(st, 2), round(DUR[k], 2))
    elif sys.argv[1:2] == ["part"]:
        i, n = int(sys.argv[2]), int(sys.argv[3]); a = round(TOTAL * i / n * FPS) / FPS; b = round(TOTAL * (i + 1) / n * FPS) / FPS
        render(f"h_{i}.mp4", f"v_{i}.mp4", None, a, b)
    elif sys.argv[1:2] == ["audio"]: build_audio()
    elif sys.argv[1:2] == ["cover"]: make_covers()
    elif sys.argv[1:2] == ["sheet"]: contact_sheet()
