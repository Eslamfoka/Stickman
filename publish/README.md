# publish/ — باكدج النشر لـ«شطة وزلطة»

كل اللي محتاجه عشان تنشر الحلقات الجاهزة، أو عشان تطبيق/سكريبت ينشرها بدالك.

| الملف | فيه إيه |
|---|---|
| `schedule.md` | الجدول بالعربي: كل يوم إيه بينزل، والعنوان والوصف والكابشن والكومنت المثبت جاهزين للنسخ |
| `schedule.json` | نفس البيانات بشكل يقراه البرنامج (manifest) — ده اللي التطبيق هيشتغل عليه |
| `thumbs/<id>_yt.jpg` | صورة يوتيوب 1280×720 |
| `thumbs/<id>_cover.jpg` | غلاف طولي 1080×1920 (تيك توك / ريلز / شورتس) |
| `media/` | **مش على الريبو** (الفيديوهات كبيرة). حط فيه الفيديوهات بالأسامي `<id>_h.mp4` (عرض) و`<id>_v.mp4` (طولي) |
| `prepare_media.py` | بيدوّر على الفيديوهات في فولدراتك بالأسامي الأصلية ويحطها في `media/` بالأسامي الصح |
| `build.py` | السكريبت اللي بيولّد كل ده (Claude بيستخدمه لما نضيف حلقات جديدة) |

## الجدول باختصار (بتوقيت القاهرة — 9 القاهرة = 10 الكويت)
- **10–12 نوفمبر:** «أزمة منتخب العمارة» حلقتين كل يوم (9:00 و9:30). يوتيوب الحلقة 1 و2 متجدولين خلاص.
- **13 نوفمبر:** فيلم الترند 6:00 مساءً + «عمارة نعناعة» م1 ح1 الساعة 9.
- **13–22 نوفمبر:** «عمارة نعناعة» الموسم 1، حلقة كل يوم 9:00.
- **23 نوفمبر:** فيلم الموسم 1 (6:00) + إعلان الموسم 2 (9:00).
- **24–27 نوفمبر:** الموسم 2 الحلقات 1–4.

## تجهيز الفيديوهات
1. على جهازك: `python publish/prepare_media.py "D:\ستيك مان" "C:\Users\...\Downloads"`
2. اللي مش هيلاقيه هيكتبهولك — سمّيه بإيدك. (حلقات الموسم 1 وفيلمه وإعلان الموسم 2 على جهازك من الأول.)

## لـClaude اللي هيبني تطبيق النشر (spec)
- اقرا `schedule.json` → `posts[]`. كل بوست فيه `publish_at_utc` و`status` و`platforms{}`.
- المنصات وكل الحقول جاهزة: `youtube` (title, description, tags, thumbnail, playlist, category_id=24, made_for_kids=false, publish_at_utc, pinned_comment), `youtube_shorts`, `tiktok` (caption, cover_image, cover_timestamp_ms), `instagram_reel` (caption, cover_image, share_to_facebook=true), `facebook_reel` (عن طريق مشاركة انستجرام)، و`facebook_video` للأفلام.
- كل المسارات نسبية لفولدر `publish/`.
- الأمان: كل الحسابات تتربط بـOAuth على جهاز المستخدم، والـtokens تتخزن عنده بس (مثلاً في keychain/ملف `.env` متجاهل في git). ممنوع حط أي token أو باسورد في الريبو أو في الشات.
- APIs الرسمية: YouTube Data API v3 (`videos.insert` + `status.publishAt` + `thumbnails.set` + `playlistItems.insert` + `commentThreads.insert`؛ التثبيت مش متاح من الـAPI → يتعمل يدوي)، Instagram Graph API (Reels: `media_type=REELS`, `cover_url`, `share_to_feed`)، Facebook Pages API، TikTok Content Posting API (محتاج app review من تيك توك؛ لحد ما يتوافق عليه: ارفع كـdraft أو جدول يدوي من TikTok Studio).
- بعد ما بوست يتنشر غيّر `status` لـ`published` واحفظ الـ URL.
- `trend01_e01` و`trend01_e02` على يوتيوب متجدولين يدوي بالفعل (`youtube_scheduled_manually`) → ما تعيدش رفعهم على يوتيوب.

## ملاحظات
- لينك فيسبوك في الوصف `facebook.com/shattawzalata` — اتأكد إن الصفحة أخدت الـusername ده (Page settings → Username)، ولو لأ غيّره في `build.py` وشغّله تاني.
- الكومنت المثبت على يوتيوب فيه اللينكات؛ على تيك توك/انستجرام اللينكات مش بتشتغل فبنكتب `@shattawzalata`.
- الهاشتاجات: يوتيوب 8 (أول 3 بيظهروا فوق العنوان)، تيك توك 6، انستجرام 5، فيسبوك 3.
