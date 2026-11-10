# Builds the publishing package for «شطة وزلطة»:
#   publish/schedule.json  (machine-readable manifest for the auto-publisher app)
#   publish/schedule.md    (human-readable calendar)
#   publish/thumbs/<id>_yt.jpg (1280x720) + <id>_cover.jpg (1080x1920 for TikTok/Reels/Shorts)
# Run: python3 publish/build.py            (thumbnails + manifest)
#      python3 publish/build.py --no-thumbs (manifest only)
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
import sys, os, json, datetime as dt
NO_THUMBS = "--no-thumbs" in sys.argv
PUB = ROOT + "/publish"
REPO = ROOT
if not NO_THUMBS:
    exec(open(f"{REPO}/brand/pro.py", encoding="utf-8").read())       # figure(), place(), lz(), logo(), radial(), rays(), kit colours
os.makedirs(f"{PUB}/thumbs", exist_ok=True)

HANDLE = "shattawzalata"
LINKS = {"youtube": f"https://www.youtube.com/@{HANDLE}", "tiktok": f"https://www.tiktok.com/@{HANDLE}",
         "instagram": f"https://www.instagram.com/{HANDLE}", "facebook": f"https://www.facebook.com/{HANDLE}"}
LINKS_BLOCK = ("تابعونا في كل مكان 👇\n"
               f"▶️ يوتيوب: {LINKS['youtube']}\n🎵 تيك توك: {LINKS['tiktok']}\n"
               f"📸 انستجرام: {LINKS['instagram']}\n👍 فيسبوك: {LINKS['facebook']}")
CAIRO = dt.timezone(dt.timedelta(hours=2))      # Egypt is UTC+2 in Nov (no DST)

SERIES = {
 "trend01": dict(name="أزمة منتخب العمارة", playlist="أزمة منتخب العمارة ⚽", glow=None,
     yt_tags=["شطة وزلطة", "أزمة منتخب العمارة", "كرتون مصري", "كرتون كوميدي", "كورة", "ترند", "انيميشن مصري", "مسلسل كرتون", "ستيك مان"],
     yt_hashtags=["#شطة_وزلطة", "#أزمة_منتخب_العمارة", "#كرتون_مصري", "#كورة", "#ترند", "#مصر", "#كوميدي", "#انيميشن"],
     tt_hashtags=["#شطة_وزلطة", "#كرتون_مصري", "#كورة", "#ترند", "#مصر", "#fyp"],
     ig_hashtags=["#شطة_وزلطة", "#كرتون_مصري", "#كورة", "#ترند", "#ريلز"],
     fb_hashtags=["#شطة_وزلطة", "#كرتون_مصري", "#كورة"],
     disclaimer="⚠️ قصة ساخرة بشخصيات خيالية من عالم «شطة وزلطة» — أي تشابه مع الواقع مقصود للضحك بس 😄"),
 "nanaa_s1": dict(name="عمارة نعناعة - الموسم 1: سر الدور السابع", playlist="عمارة نعناعة - الموسم 1: سر الدور السابع 🏚️", glow=(120, 60, 200),
     yt_tags=["شطة وزلطة", "عمارة نعناعة", "سر الدور السابع", "كرتون مصري", "غموض", "رعب كوميدي", "لغز", "مسلسل كرتون", "ستيك مان", "انيميشن مصري"],
     yt_hashtags=["#عمارة_نعناعة", "#شطة_وزلطة", "#كرتون_مصري", "#غموض", "#لغز", "#رعب_كوميدي", "#انيميشن", "#مصر"],
     tt_hashtags=["#عمارة_نعناعة", "#شطة_وزلطة", "#كرتون_مصري", "#لغز", "#غموض", "#fyp"],
     ig_hashtags=["#عمارة_نعناعة", "#شطة_وزلطة", "#كرتون_مصري", "#لغز", "#ريلز"],
     fb_hashtags=["#عمارة_نعناعة", "#شطة_وزلطة", "#كرتون_مصري"], disclaimer=None),
 "nanaa_s2": dict(name="عمارة نعناعة - الموسم 2: سر البدروم", playlist="عمارة نعناعة - الموسم 2: سر البدروم 🔦", glow=(40, 150, 120),
     yt_tags=["شطة وزلطة", "عمارة نعناعة", "سر البدروم", "الموسم التاني", "كرتون مصري", "غموض", "رعب كوميدي", "لغز", "مسلسل كرتون", "ستيك مان"],
     yt_hashtags=["#عمارة_نعناعة", "#سر_البدروم", "#شطة_وزلطة", "#كرتون_مصري", "#غموض", "#لغز", "#انيميشن", "#مصر"],
     tt_hashtags=["#عمارة_نعناعة", "#شطة_وزلطة", "#كرتون_مصري", "#لغز", "#غموض", "#fyp"],
     ig_hashtags=["#عمارة_نعناعة", "#شطة_وزلطة", "#كرتون_مصري", "#لغز", "#ريلز"],
     fb_hashtags=["#عمارة_نعناعة", "#شطة_وزلطة", "#كرتون_مصري"], disclaimer=None),
}
SERIES_DESC = {
 "trend01": "تابعوا «أزمة منتخب العمارة» — مسلسل كرتون كوميدي قصير من «شطة وزلطة» 🌶️🥗",
 "nanaa_s1": "«عمارة نعناعة» — مسلسل كرتون مصري غموض وضحك للعيلة كلها. الموسم الأول: سر الدور السابع 🏚️",
 "nanaa_s2": "«عمارة نعناعة» — الموسم التاني: سر البدروم 🔦 كرتون مصري غموض وضحك للعيلة كلها",
}

# figure spec: (who, S, expr, mouth, look, arms, held, shirt, num, x)   — x in a 1920-wide frame
T = ROOT + "/trend/01/bg/"; S1 = f"{REPO}/s1e"
ITEMS = [
 # ---------------- trend «أزمة منتخب العمارة» ----------------
 dict(id="trend01_e01", series="trend01", kind="episode", ep=1, name="كاس الشارع", date="2026-11-10", time="21:00",
      src_h="أزمة منتخب العمارة - الحلقة 1 - كاس الشارع (عرض).mp4", src_v="أزمة منتخب العمارة - الحلقة 1 - كاس الشارع (طولي).mp4",
      yt_title="كابتن بندق كسب الكاس! 🏆", hook="منتخب العمارة كسب كاس الشارع والكابتن بندق بقى بطل الحارة… بس الفرحة هتكمل؟ 🤔",
      question="تفتكروا الكابتن بندق هيفضل بطل الحارة؟ 🤔", headline=["جوووون!"], bg=T + "pitch.png", glow=(255, 200, 60),
      figs=[("shatta", 4.6, "happy", 0.7, -1, "up", None, "RED", 10, 1420)], status="youtube_scheduled_manually"),
 dict(id="trend01_e02", series="trend01", kind="episode", ep=2, name="المؤتمر الصحفي", date="2026-11-10", time="21:30",
      src_h="أزمة منتخب العمارة - الحلقة 2 - المؤتمر الصحفي (عرض).mp4", src_v="أزمة منتخب العمارة - الحلقة 2 - المؤتمر الصحفي (طولي).mp4",
      yt_title="الكابتن قال إيه في المؤتمر؟! 😱", hook="مؤتمر صحفي بعد الكاس… وسؤال واحد من توتة قلب الدنيا! 🎤",
      question="مين عنده حق: الكابتن ولا توتة؟ 🎤", headline=["كوكو", "خلصان؟!"], bg=T + "conference.png", glow=(230, 40, 40),
      figs=[("shatta", 2.9, "shock", 0.5, -1, "scared", None, "RED", 10, 1730), ("bondo2", 4.4, "smug", 0.0, -1, "hips", None, None, None, 1330)],
      status="youtube_scheduled_manually"),
 dict(id="trend01_e03", series="trend01", kind="episode", ep=3, name="الدقيقة 60", date="2026-11-11", time="21:00",
      src_h="أزمة منتخب العمارة - الحلقة 3 - الدقيقة 60 (عرض).mp4", src_v="أزمة منتخب العمارة - الحلقة 3 - الدقيقة 60 (طولي).mp4",
      yt_title="شطة طالع في الدقيقة 60؟! 😡", hook="ماتش صعب صفر صفر… والكابتن قرر يطلّع نجم الفريق! ⚽",
      question="شطة غلط ولا الكابتن هو اللي غلط؟ ⚽", headline=["شطة", "طالع!"], bg=T + "pitch.png", glow=(230, 40, 40),
      figs=[("shatta", 4.6, "angry", 0.6, -1, "point", None, "RED", 10, 1420)]),
 dict(id="trend01_e04", series="trend01", kind="episode", ep=4, name="قهوة الشارع", date="2026-11-11", time="21:30",
      src_h="أزمة منتخب العمارة - الحلقة 4 - قهوة الشارع (عرض).mp4", src_v="أزمة منتخب العمارة - الحلقة 4 - قهوة الشارع (طولي).mp4",
      yt_title="الباشا وعبده في قهوة الشارع ☕😂", hook="برنامج «قهوة الشارع» بيناقش الأزمة… والباشا رأيه واضح، وعبده رأيه في البسكوت! ☕",
      question="الكابتن لازم يعتذر ولا لأ؟ اكتبوا رأيكم 👇", headline=["لازم", "يعتذر!"], bg=T + "studio.png", glow=(255, 170, 40),
      figs=[("pasha", 3.0, "smug", 0.0, -1, "hips", None, None, None, 1720), ("abdo", 4.3, "happy", 0.5, -1, "hold", "sweet", None, None, 1330)]),
 dict(id="trend01_e05", series="trend01", kind="episode", ep=5, name="الصلح", date="2026-11-12", time="21:00",
      src_h="أزمة منتخب العمارة - الحلقة 5 - الصلح (عرض).mp4", src_v="أزمة منتخب العمارة - الحلقة 5 - الصلح (طولي).mp4",
      yt_title="شطة نقل لعمارة الجيران! 🏠", hook="النجم شطة لبس الأزرق ونقل لعمارة الجيران… وزلطة رايح بالشاي والبسكوت يصالحه 🍪",
      question="شطة هيرجع العمارة ولا لأ؟ 🏠", headline=["مش", "راجع!"], bg=T + "neighbors.png", glow=(60, 130, 240),
      figs=[("zalata", 2.9, "sad", 0.2, -1, "hold", "tray", None, None, 1720), ("shatta", 4.5, "angry", 0.4, -1, "hips", None, "BLUE", 10, 1330)]),
 dict(id="trend01_e06", series="trend01", kind="episode", ep=6, name="الإقالة", date="2026-11-12", time="21:30", last=True,
      src_h="أزمة منتخب العمارة - الحلقة 6 - الإقالة (عرض).mp4", src_v="أزمة منتخب العمارة - الحلقة 6 - الإقالة (طولي).mp4",
      yt_title="رسمياً: إقالة الكابتن بندق! 📰", hook="الجرايد كلها بتقول: إقالة الكابتن بندق… وشطة نزّل بوست قلب السوشيال! 📱",
      question="مين يستاهل يبقى المدرب الجديد؟ 😂", headline=["الإقالة!"], bg=T + "room.png", glow=(230, 40, 40), zzz=True,
      figs=[("bondo2", 4.6, "sleepy", 0.0, -1, "down", None, None, None, 1400)]),
 dict(id="trend01_movie", series="trend01", kind="movie", ep=None, name="الفيلم كامل", date="2026-11-13", time="18:00",
      src_h="أزمة منتخب العمارة - الفيلم كامل (عرض).mp4", src_v="أزمة منتخب العمارة - الفيلم كامل (طولي).mp4",
      yt_title="أزمة منتخب العمارة - الفيلم كامل ⚽🎬", hook="الحكاية كلها في فيديو واحد: من الكاس… للمؤتمر… للدقيقة 60… للإقالة! 🎬",
      question="أحلى حلقة فيهم كانت أنهي؟ 👇", headline=["الفيلم", "كامل!"], bg=T + "pitch.png", glow=(255, 200, 60),
      figs=[("shatta", 2.9, "happy", 0.5, -1, "up", None, "RED", 10, 1730), ("bondo2", 4.3, "happy", 0.4, -1, "up", None, None, None, 1330)]),
 # ---------------- «عمارة نعناعة» الموسم 1 ----------------
 *[dict(id=f"nanaa_s1_e{n:02d}", series="nanaa_s1", kind="episode", ep=n, name=nm, date=f"2026-11-{12 + n}", time="21:00",
        src_h=f"عمارة نعناعة - الحلقة {n:02d} - {nm}.mp4 (من على جهازك)", src_v=f"عمارة نعناعة - الحلقة {n:02d} - {nm} (تيك توك).mp4 (من على جهازك)",
        yt_title=tt, hook=hk, question=q, headline=hl, bg=bg, figs=fg, last=(n == 10))
   for n, nm, tt, hk, q, hl, bg, fg in [
   (1, "الصوت اللي في السقف", "صوت غريب في السقف كل ليلة الساعة 12! 😱", "شقة الدور السابع مقفولة من 30 سنة… وكل ليلة الساعة 12 بيطلع منها خبط! 😱",
    "🧩 لغز الحلقة: سمعتوا كام خبطة؟ اكتبوا حلكم 👇", ["صوت في", "السقف!"], S1 + "1/bg/living_1080.png",
    [("shatta", 4.5, "shock", 0.7, -1, "scared", None, None, None, 1380)]),
   (2, "المفتاح اللي مالوش باب", "مفتاح غامض في صندوق البوستة! 🔑", "مفتاح غريب مكتوب عليه «7-30» ظهر في صندوق البوستة… وبعدين اختفى! 🔑",
    "🧩 لغز الحلقة: «7-30» على المفتاح معناها إيه؟ 👇", ["مفتاح", "7-30"], S1 + "2/bg/door7.png",
    [("zalata", 4.4, "shock", 0.4, -1, "hold", "key", None, None, 1380)]),
   (3, "عم بندق مش بينام ليه؟", "عم بندق البواب مش بينام ليه؟ 🤔", "البواب طالع السابع بالمفتاح كل ليلة… والخبط بقى 3 سريع و3 طويل و3 سريع! 🔨",
    "🧩 لغز الحلقة: الخبط ده معناه إيه؟ (فكّروا في المورس 😉) 👇", ["البواب", "صاحي!"], S1 + "1/bg/stairs_1080.png",
    [("bondo2", 4.5, "smug", 0.0, -1, "hold", "keys", None, None, 1380)]),
   (4, "ليلة انقطاع النور", "النور قطع… ومين اللي بينادي شطة؟! 🕯️", "النور قطع في العمارة كلها… وضل طويل على الحيطة بينادي: «يا شطة…» 🕯️",
    "🧩 لغز الحلقة: إزاي الضل طويل وصاحبه قصير؟ 👇", ["مين", "بينادي؟!"], S1 + "1/bg/living_1080.png",
    [("shatta", 4.5, "scared", 0.6, -1, "hold", "torch", None, None, 1380)]),
   (5, "الجار الجديد", "الجار الجديد ظريف زيادة عن اللزوم! 🍬", "أستاذ فهمي سكن جديد ومعاه حلويات للكل… بس ليه معاه مفتاح «7-30»؟ 🍬",
    "🧩 أستاذ فهمي ده وراه إيه؟ اكتبوا توقعاتكم 👇", ["الجار", "الجديد"], S1 + "5/bg/fahmy_raw.png",
    [("fahmy", 4.4, "smug", 0.3, -1, "hips", None, None, None, 1380)]),
   (6, "رسالة بالخبط", "الخبط ده رسالة سرية! 🔨", "فيه نوعين خبط في العمارة… وتوتة اكتشفت إن الخبط بيقول اسم حد! 🔨",
    "🧩 لغز الحلقة: الخبط بيقول اسم مين؟ 👇", ["رسالة", "سرية!"], S1 + "2/bg/door7.png",
    [("tota", 4.6, "shock", 0.4, -1, "hold", "notebook", None, None, 1380)]),
   (7, "الكشكول اتسرق", "كشكول زلطة اتسرق! مين الحرامي؟ 🕵️", "كشكول زلطة اللي فيه كل الحلول اتسرق… وطابور المشتبه فيهم طويل! 🕵️",
    "🧩 لغز الحلقة: مين اللي سرق الكشكول؟ 👇", ["مين", "الحرامي؟"], S1 + "1/bg/bedroom_clean.png",
    [("zalata", 4.4, "shock", 0.5, -1, "scared", None, None, None, 1380)]),
   (8, "الدور السابع", "أخيراً دخلنا الدور السابع! 🚪", "العيال دخلوا شقة الدور السابع… وفجأة الباب اتقفل عليهم! 🚪",
    "🧩 لغز الحلقة: إيه اللي مربوط في البكرة؟ 👇", ["الدور", "السابع!"], S1 + "8/bg/apt7_raw.png",
    [("tota", 2.9, "scared", 0.3, -1, "scared", None, None, None, 1730), ("shatta", 4.4, "shock", 0.7, -1, "scared", None, None, None, 1330)]),
   (9, "اللي ورا الباب", "البواب حكى السر كله… 😨", "عم بندق فتح الباب وحكى سر رشدي… وقال: «الخبط الساعة 12 مش أنا!» 😨",
    "🧩 لو البواب مش هو اللي بيخبط الساعة 12… يبقى مين؟ 👇", ["مين", "بيخبط؟!"], S1 + "9/bg/window.png",
    [("bondo2", 4.5, "shock", 0.5, -1, "scared", None, None, None, 1380)]),
   (10, "الحقيقة", "الحقيقة كلها! (الحلقة الأخيرة) 🎬", "الحلقة الأخيرة: الخطة، لايف سوسن، والشبشب على فهمي! والسر الحقيقي في البدروم… 🎬",
    "🧩 تفتكروا إيه اللي مستني العيال في البدروم؟ 👇", ["الحقيقة!"], S1 + "10/bg/basement.png",
    [("fahmy", 2.9, "shock", 0.5, -1, "scared", None, None, None, 1730), ("nana", 4.4, "angry", 0.5, -1, "hold", "slipper", None, None, 1330)]),
 ]],
 dict(id="nanaa_s1_movie", series="nanaa_s1", kind="movie", ep=None, name="الموسم الأول كامل", date="2026-11-23", time="18:00",
      src_h="عمارة نعناعة - الفيلم الكامل (الموسم الأول).mp4 (من على جهازك)", src_v=None,
      yt_title="عمارة نعناعة: سر الدور السابع - الموسم الأول كامل 🎬", hook="الموسم الأول كله في فيلم واحد: سر الدور السابع من أول خبطة لحد الحقيقة! 🎬",
      question="مين كان أشطر واحد في حل الألغاز؟ 👇", headline=["الموسم", "كامل!"], bg=S1 + "1/bg/lobby_1080.png",
      figs=[("zalata", 3.0, "happy", 0.3, -1, "up", None, None, None, 1750), ("shatta", 4.2, "happy", 0.6, -1, "up", None, None, None, 1300)]),
 dict(id="nanaa_s2_trailer", series="nanaa_s2", kind="trailer", ep=None, name="إعلان الموسم التاني", date="2026-11-23", time="21:00",
      src_h="اعلان الموسم التاني - سر البدروم.mp4 (من على جهازك)", src_v="اعلان الموسم التاني - سر البدروم (تيك توك).mp4 (من على جهازك)",
      yt_title="الموسم التاني: سر البدروم 🔦 (الإعلان الرسمي)", hook="«افتحوا البدروم… بس ما تفتحوهوش بالليل» 🔦 الموسم التاني من عمارة نعناعة بكرة!",
      question="مستعدين للموسم التاني؟ 🔦 اكتبوا توقعاتكم 👇", headline=["الموسم", "التاني"], bg=f"{REPO}/s2/bg/basement_day.png",
      figs=[("shatta", 4.5, "scared", 0.6, -1, "hold", "torch", None, None, 1380)]),
 *[dict(id=f"nanaa_s2_e{n:02d}", series="nanaa_s2", kind="episode", ep=n, name=nm, date=f"2026-11-{23 + n}", time="21:00",
        src_h=f"عمارة نعناعة م2 - الحلقة {n:02d} - {nm}.mp4", src_v=f"عمارة نعناعة م2 - الحلقة {n:02d} - {nm} (تيك توك).mp4",
        yt_title=tt, hook=hk, question=q, headline=hl, bg=bg, figs=fg)
   for n, nm, tt, hk, q, hl, bg, fg in [
   (1, "باب البدروم", "باب البدروم المقفول من سنين! 🔒", "نعناعة قالت: «محدش هينزل البدروم!»… بس توتة لاحظت إن القفل جديد ولامع! 🔒",
    "🧩 لغز الحلقة: مين اللي غيّر القفل؟ 👇", ["محدش", "هينزل!"], f"{REPO}/s2/bg/basement_day.png",
    [("nana", 4.5, "angry", 0.6, -1, "point", None, None, None, 1380)]),
   (2, "الصوت اللي تحت الأرض", "صوت جاي من تحت الأرض! 🎙️", "من فتحة في المدخل: صوت رشدي بيقول أرقام… وعربية سودا بتقف قدام العمارة الساعة 12! 🎙️",
    "🧩 لغز الحلقة: الأرقام دي معناها إيه؟ 👇", ["تحت", "الأرض!"], S1 + "10/bg/basement.png",
    [("shatta", 4.5, "scared", 0.6, -1, "scared", None, None, None, 1380)]),
   (3, "الباشا", "مين الباشا؟! 🎩", "الباشا زار نعناعة وعايز يأجّر البدروم «مخزن»… وزلطة افتكر الكلمة دي من الموسم الأول! 🎩",
    "🧩 لغز الحلقة: سمعنا كلمة «الباشا» فين قبل كده؟ 👇", ["الباشا!"], f"{REPO}/s2/bg/street_car.png",
    [("abdo", 2.9, "flat", 0.0, -1, "hips", None, None, None, 1750), ("pasha", 4.4, "smug", 0.0, -1, "hips", None, None, None, 1330)]),
   (4, "النزول", "نزلنا البدروم… ولاقينا استوديو سري! 🔦", "بالنهار زي ما رشدي قال: نزلوا البدروم، ولاقوا باب حديد بعجلة… ووراه استوديو سري! 🔦",
    "🧩 لغز الحلقة: الساعة الواقفة في الاستوديو على كام… وليه؟ 👇", ["النزول!"], f"{REPO}/s2e4/bg/corridor.png",
    [("tota", 2.9, "scared", 0.3, -1, "scared", None, None, None, 1750), ("shatta", 4.4, "shock", 0.6, -1, "hold", "torch", None, None, 1330)]),
 ]],
]

def kit_col(k):
    return {"RED": (205, 35, 45), "BLUE": (40, 95, 205)}.get(k, k)

def badge_text(it):
    if it["kind"] == "movie": return "الفيلم"
    if it["kind"] == "trailer": return "إعلان"
    return f"الحلقة {it['ep']}"

def render_bg(it, W_, H_):
    src = Image.open(it["bg"]).convert("RGB")
    sw, sh = src.size; sc = max(W_ / sw, H_ / sh)
    src = src.resize((int(sw * sc) + 1, int(sh * sc) + 1), Image.LANCZOS)
    ox, oy = (src.size[0] - W_) // 2, (src.size[1] - H_) // 2
    bg = src.crop((ox, oy, ox + W_, oy + H_)).filter(ImageFilter.GaussianBlur(5))
    bg = ImageEnhance.Brightness(bg).enhance(0.55).convert("RGBA")
    col = it.get("glow") or SERIES[it["series"]]["glow"]
    glow = radial(W_, H_, col, (10, 6, 12), 0.72 if W_ > H_ else 0.5, 0.45); glow.putalpha(150); bg.alpha_composite(glow)
    bg.alpha_composite(rays((W_, H_), int(W_ * (0.73 if W_ > H_ else 0.5)), int(H_ * 0.4), 22, (255, 255, 255, 22)))
    return bg

def series_tag(it):
    return {"trend01": "أزمة منتخب العمارة", "nanaa_s1": "عمارة نعناعة • الموسم 1", "nanaa_s2": "عمارة نعناعة • الموسم 2"}[it["series"]]

def thumb_yt(it):
    W_, H_ = 1920, 1080
    bg = render_bg(it, W_, H_)
    vg = Image.new("RGBA", (W_, H_), (0, 0, 0, 0)); ImageDraw.Draw(vg).rectangle([0, 0, 900, H_], fill=(0, 0, 0, 70)); bg.alpha_composite(vg.filter(ImageFilter.GaussianBlur(80)))
    for who, S, ex, mo, lk, arms, held, shirt, num, x in it["figs"]:
        place(bg, figure(who, S, ex, mo, lk, arms, held, kit_col(shirt), num), x, H_ + int(S * 70))
    if it.get("zzz"):
        for zx, zy, zs in ((1590, 430, 85), (1670, 345, 110), (1770, 260, 135)): lz(bg, zx, zy, "Z", zs, (255, 255, 255), ow=12, iw=1)
    hl = it["headline"]
    if len(hl) == 1: lz(bg, 500, 560, hl[0], 260, GOLD, ow=30, iw=10)
    else:
        lz(bg, 470, 400, hl[0], 240, (255, 255, 255), ow=26, iw=9); lz(bg, 470, 690, hl[1], 260, GOLD, ow=28, iw=10)
    d = ImageDraw.Draw(bg)
    d.rounded_rectangle([60, 50, 400, 170], 30, fill=(205, 35, 45), outline=(255, 255, 255), width=6)
    lz(bg, 230, 108, badge_text(it), 78, (255, 255, 255), ow=6, iw=1, shadow=False)
    lz(bg, 470, 975, series_tag(it), 64, (255, 255, 255), ow=8, iw=1)
    logo(bg, 1700, 110, 78)
    bg.convert("RGB").resize((1280, 720), Image.LANCZOS).save(f"{PUB}/thumbs/{it['id']}_yt.jpg", quality=92)

def thumb_cover(it):
    W_, H_ = 1080, 1920
    bg = render_bg(it, W_, H_)
    figs = sorted(it["figs"], key=lambda f: f[1])          # small (secondary) first, main last (front)
    for i, (who, S, ex, mo, lk, arms, held, shirt, num, x) in enumerate(figs):
        main = (i == len(figs) - 1)
        s2 = S * (1.12 if main else 0.8); cx = 540 if main else 870
        place(bg, figure(who, s2, ex, mo, 0 if main else -1, arms, held, kit_col(shirt), num), cx, H_ + int(s2 * 70) - 60)
    if it.get("zzz"):
        for zx, zy, zs in ((760, 820, 80), (830, 740, 105), (920, 650, 130)): lz(bg, zx, zy, "Z", zs, (255, 255, 255), ow=12, iw=1)
    hl = it["headline"]
    top = Image.new("RGBA", (W_, H_), (0, 0, 0, 0)); ImageDraw.Draw(top).rectangle([0, 0, W_, 760], fill=(0, 0, 0, 90)); bg.alpha_composite(top.filter(ImageFilter.GaussianBlur(60)))
    if len(hl) == 1: lz(bg, 540, 500, hl[0], 230, GOLD, ow=26, iw=9)
    else:
        lz(bg, 540, 470, hl[0], 190, (255, 255, 255), ow=22, iw=8); lz(bg, 540, 680, hl[1], 210, GOLD, ow=24, iw=9)
    d = ImageDraw.Draw(bg)
    d.rounded_rectangle([360, 225, 720, 315], 30, fill=(205, 35, 45), outline=(255, 255, 255), width=6)
    lz(bg, 540, 268, badge_text(it), 64, (255, 255, 255), ow=6, iw=1, shadow=False)
    pill = Image.new("RGBA", (W_, H_), (0, 0, 0, 0)); ImageDraw.Draw(pill).rounded_rectangle([140, 1560, 940, 1660], 50, fill=(20, 10, 20, 215), outline=(255, 214, 90, 255), width=5); bg.alpha_composite(pill)
    lz(bg, 540, 1608, series_tag(it), 56, (255, 255, 255), ow=6, iw=1, shadow=False)
    logo(bg, 540, 115, 80)
    bg.convert("RGB").save(f"{PUB}/thumbs/{it['id']}_cover.jpg", quality=90)

# ---------------- text builders ----------------
def media_names(it):
    m = {"horizontal": f"media/{it['id']}_h.mp4"}
    if it.get("src_v"): m["vertical"] = f"media/{it['id']}_v.mp4"
    return m

def next_line(it):
    if it["kind"] != "episode": return None
    if it.get("last"):
        return {"trend01": "الفيلم كامل بكرة على القناة 🎬", "nanaa_s1": "الموسم التاني «سر البدروم» قريب جداً… فعّلوا الجرس 🔔",
                "nanaa_s2": None}[it["series"]]
    return "الحلقة الجاية بكرة الساعة 9 بالليل بتوقيت مصر ⏰"

def yt_title(it, shorts=False):
    s = SERIES[it["series"]]["name"].split(":")[0].split(" - ")[0]
    part = badge_text(it) if it["kind"] == "episode" else it["name"]
    t = f"{it['yt_title']} | {s} - {part} | شطة وزلطة" if it["kind"] == "episode" else f"{it['yt_title']} | شطة وزلطة"
    if shorts: t = f"{it['yt_title']} | {s} {badge_text(it)} #Shorts"
    return t[:100]

def yt_description(it):
    S = SERIES[it["series"]]
    parts = [it["hook"], SERIES_DESC[it["series"]]]
    if it["question"].startswith("🧩"):
        q = it["question"]
        parts.append(q.replace("اكتبوا حلكم 👇", "اكتبوا حلكم في الكومنتات 👇") if "اكتبوا" in q else q.replace("👇", "اكتبوا حلكم في الكومنتات 👇"))
    nl = next_line(it)
    if nl: parts.append(nl)
    if S["disclaimer"]: parts.append(S["disclaimer"])
    parts.append(LINKS_BLOCK)
    parts.append(" ".join(S["yt_hashtags"]))
    return "\n\n".join(parts)

def short_caption(it, tags):
    q = it["question"]
    return f"{it['hook']} {badge_text(it)} من «{SERIES[it['series']]['name'].split(' - ')[0].split(':')[0]}» 🎬\n{q}\n{' '.join(tags)}"

def pinned(it, platform):
    q = it["question"]
    if platform == "youtube":
        return f"{q}\n\n{LINKS_BLOCK}"
    return f"{q}\nتابعونا على يوتيوب وانستجرام وفيسبوك وتيك توك: @{HANDLE} 🌶️🥗"

def when(it, minutes=0):
    d = dt.datetime.fromisoformat(f"{it['date']}T{it['time']}:00").replace(tzinfo=CAIRO) + dt.timedelta(minutes=minutes)
    return d

def build_post(it):
    S = SERIES[it["series"]]
    t0 = when(it); m = media_names(it)
    thumbs = {"youtube": f"thumbs/{it['id']}_yt.jpg", "vertical_cover": f"thumbs/{it['id']}_cover.jpg"}
    p = {"id": it["id"], "series": it["series"], "series_name": S["name"], "kind": it["kind"], "episode": it["ep"], "episode_name": it["name"],
         "publish_at_cairo": t0.isoformat(), "publish_at_utc": t0.astimezone(dt.timezone.utc).isoformat().replace("+00:00", "Z"),
         "status": it.get("status", "pending"),
         "media": m, "source_file_names": {"horizontal": it["src_h"], "vertical": it.get("src_v")},
         "thumbnails": thumbs, "platforms": {}}
    p["platforms"]["youtube"] = {
        "video": m["horizontal"], "title": yt_title(it), "description": yt_description(it), "tags": S["yt_tags"],
        "thumbnail": thumbs["youtube"], "playlist": S["playlist"], "category_id": "24", "default_language": "ar",
        "made_for_kids": False, "privacy": "public", "publish_at_utc": p["publish_at_utc"], "pinned_comment": pinned(it, "youtube")}
    if "vertical" in m:
        ts = when(it, 60)
        p["platforms"]["youtube_shorts"] = {
            "video": m["vertical"], "title": yt_title(it, shorts=True), "description": f"{it['hook']}\n\n{LINKS_BLOCK}\n\n{' '.join(S['yt_hashtags'][:5])} #Shorts",
            "tags": S["yt_tags"], "playlist": S["playlist"], "category_id": "24", "made_for_kids": False, "privacy": "public",
            "publish_at_utc": ts.astimezone(dt.timezone.utc).isoformat().replace("+00:00", "Z"), "pinned_comment": pinned(it, "youtube"),
            "note": "يتنشر بعد الحلقة العرض بساعة (لو المدة أكتر من 3 دقايق يوتيوب مش هيعتبره Short)"}
        p["platforms"]["tiktok"] = {
            "video": m["vertical"], "caption": short_caption(it, S["tt_hashtags"]), "cover_image": thumbs["vertical_cover"],
            "cover_timestamp_ms": 1000, "privacy": "PUBLIC_TO_EVERYONE", "allow_comments": True, "allow_duet": True, "allow_stitch": True,
            "publish_at_utc": p["publish_at_utc"], "pinned_comment": pinned(it, "tiktok"),
            "note": "لو الأداة مش بتقبل صورة غلاف، استخدم cover_timestamp_ms أو اختار الغلاف يدوي من التطبيق"}
        p["platforms"]["instagram_reel"] = {
            "video": m["vertical"], "caption": short_caption(it, S["ig_hashtags"]), "cover_image": thumbs["vertical_cover"],
            "share_to_facebook": True, "publish_at_utc": p["publish_at_utc"], "pinned_comment": pinned(it, "instagram")}
        p["platforms"]["facebook_reel"] = {
            "via": "instagram_reel.share_to_facebook", "caption": short_caption(it, S["fb_hashtags"]),
            "note": "مش محتاج رفع منفصل لو انستجرام بيعمل share لفيسبوك", "pinned_comment": pinned(it, "facebook")}
    if it["kind"] == "movie":
        p["platforms"]["facebook_video"] = {
            "video": m["horizontal"], "title": it["yt_title"], "description": yt_description(it), "thumbnail": thumbs["youtube"],
            "publish_at_utc": p["publish_at_utc"], "pinned_comment": pinned(it, "facebook")}
    return p

posts = [build_post(it) for it in ITEMS]
manifest = {
    "brand": "شطة وزلطة", "handle": HANDLE, "links": LINKS, "timezone_note": "كل المواعيد بتوقيت القاهرة (UTC+2 في نوفمبر). 9 بالليل القاهرة = 10 بالليل الكويت.",
    "media_folder": "publish/media/ (مش على الريبو — حط فيه الفيديوهات بالأسماء المكتوبة في media، والأسامي الأصلية في source_file_names)",
    "generated": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "posts": posts}
json.dump(manifest, open(f"{PUB}/schedule.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# human-readable calendar
L = ["# جدول النشر — «شطة وزلطة»", "", "كل المواعيد **بتوقيت القاهرة** (9 بالليل القاهرة = 10 بالليل الكويت). التفاصيل الكاملة لكل بوست في `schedule.json`.", "",
     "| التاريخ | الساعة | المحتوى | يوتيوب | تيك توك | انستجرام + فيسبوك | الحالة |", "|---|---|---|---|---|---|---|"]
for it, p in zip(ITEMS, posts):
    has_v = "vertical" in p["media"]
    L.append(f"| {it['date']} | {it['time']} | {SERIES[it['series']]['name'].split(':')[0]} — {badge_text(it)}: {it['name']} | ✅ عرض" + (" + Short" if has_v else "") +
             f" | {'✅' if has_v else '—'} | {'✅ ريل' if has_v else ('✅ فيديو فيسبوك' if it['kind']=='movie' else '—')} | {p['status']} |")
L += ["", "## تفاصيل كل بوست", ""]
for it, p in zip(ITEMS, posts):
    yt = p["platforms"]["youtube"]
    L += [f"### {it['date']} {it['time']} — {p['series_name']} — {badge_text(it)}: {it['name']}", "",
          f"- **الملفات:** `{p['media'].get('horizontal')}`" + (f" + `{p['media']['vertical']}`" if 'vertical' in p['media'] else "") +
          f" (الأصل: {it['src_h']})", f"- **الصور:** `{p['thumbnails']['youtube']}` (يوتيوب) — `{p['thumbnails']['vertical_cover']}` (غلاف طولي)", "",
          "**عنوان يوتيوب:**", "```", yt["title"], "```", "**وصف يوتيوب:**", "```", yt["description"], "```",
          "**الكومنت المثبت (يوتيوب):**", "```", yt["pinned_comment"], "```"]
    if "tiktok" in p["platforms"]:
        L += ["**كابشن تيك توك:**", "```", p["platforms"]["tiktok"]["caption"], "```",
              "**كابشن انستجرام/فيسبوك:**", "```", p["platforms"]["instagram_reel"]["caption"], "```",
              "**الكومنت المثبت (تيك توك/انستجرام/فيسبوك):**", "```", p["platforms"]["tiktok"]["pinned_comment"], "```"]
    L.append("")
open(f"{PUB}/schedule.md", "w", encoding="utf-8").write("\n".join(L))
print("manifest ok:", len(posts), "posts")

if not NO_THUMBS:
    for it in ITEMS:
        ("--covers" in sys.argv or thumb_yt(it)); thumb_cover(it); print("thumbs", it["id"], flush=True)
