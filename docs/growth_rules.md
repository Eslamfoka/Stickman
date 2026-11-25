# Growth rules — FIXED by the user 2026-11-21 («ثبت كله») after the 28-day stats review
Stats that triggered this (Oct 23 – Nov 19): IG 47.3K views / 32.9K reach / 841 interactions / 60 followers ·
FB 18.6K views but only 4.9K 3-second views (26%) / 35 follows · YT 19.7K views last 7 days, all Shorts; long videos 8–67 views ·
Audience: KSA 17% · EG 15% · IQ 11%; 25–44 = 66%; male 57%. Best: couple comedy (FB «متجوز عليكي!» 6.2K), «مين الكداب؟»
(most interactions, «مين صوّرني؟» 134), «مين شبهك؟» (most follows, 22). Diagnosis: day-1 test batch scrolls away (static
silent cover in the first 0.5 s + tiny picture in the vertical) and almost no shares/follows → distribution stops after day 1.

## A. The video
1. Reels start with motion + sound on frame 1 — NO static cover in the first 0.5 s (fix publish/tiktok_cut.py; set the cover via «Edit cover» only).
2. Vertical = a real 9:16 framing: characters fill the screen; no small strip in the middle with blurred bars.
3. Every case ends with «الحل بكره… تابع عشان ما يفوتكش».
4. Every sketch ends with a share line («منشن أخوك / ابعتها لمراتك / منشن جوزك»).
5. YouTube = Shorts focus; long-form only for season movies.
## B. On-screen text
6. Big top title only the first 3 s, then a small tag («قضية 7 🕵️»).
7. Subtitles max 1–2 lines, phrase-by-phrase in sync with speech.
8. Key word in the subtitle colored yellow.
9. In cases: each speaker's name in his own color before his line.
10. Safe zones: no text in the bottom ~20% or the right-side button column; drop the bottom series line.
## C. Reel cover
11. Big face (~half the cover) with one clear emotion.
12. An object from the story on the cover (envelope / umbrella / foam…).
13. Title 2–3 words with a question, centered (IG grid crops the sides).
14. Case covers: «قضية N» + the 3 suspects with badges 1-2-3.
## D. Caption & comments
15. Caption = 3 lines: hook question (<80 chars) → ONE clear ask → 4–5 hashtags.
16. No links in IG/TikTok captions.
17. Pinned comment = discussion bait, not a copy of the caption.
18. Reply to comments in the first hour.
## E. Content mix
19. More couple comedy (بندق وعزيزة).
20. Character-intro videos like «مين شبهك؟» (top follow driver).
21. Run all of this for 1 week, then compare with the old numbers.
## F. Thumbnails
22. YT thumbnail = same rules as the cover: big face, story object, ≤3 bold high-contrast words.
23. Small fixed series badge in a corner («عمارة نعناعة • الحلقة 3» / «قضية 7»).
24. Thumbnail ≠ title: the title tells the story, the thumbnail tells the emotion.
25. Long videos: use YouTube's thumbnail test (2–3 designs per season movie).
26. Shorts: design one "cover-worthy" frame inside every episode (big face + hook text) for the user to pick as the Shorts thumbnail.

## How it's implemented (first: daily/16 «راجل البيت», 21/11)
- Item flag `growth=True` in publish/build.py → 3-line caption (`hook` ≤80 / `cta` / ≤5 tags), no links, pinned = `bait`; build.py does NOT draw thumbs for it.
- Episode makes its own cover + YT thumbnail: `python ep.py cover` (big faces composition + story object + 2-word question + badge).
- Native vertical: `vertical()` re-draws the scene with its own camera (`v=(c0,c1)` per shot, `vcam`), phrase subtitles `CHUNKS` with a yellow key word (`sub_chunk`), hook 3 s only. See daily/16/ep.py as the template.
- publish/tiktok_cut.py no longer prepends the cover (only with `--cover-first`).

---
## قواعد 23/11 (بعد مراجعة الإنستجرام — المستخدم طلب تثبيتها)
27. **الأماكن ثابتة** (القاعدة 8 في CLAUDE.md): نفس الشكل في كل الحلقات، اللي يتغير الإضاءة بس.
28. حلقات «عمارة نعناعة» تبدأ بحل لغز الحلقة اللي فاتت. في «مين الكداب؟» الحل بيتحط في **آخر** الفيديو عشان الناس تكمل.
29. **الطولي بتاع عمارة نعناعة يتعمل طولي من الأول** (مش شريط أفقي جوه فيديو طولي)، والعنوان في أول 3 ثواني بس.
30. **كل ريل ينتهي بطلب واحد بس:** القضية ← «اكتب رقم الكداب» · اليوميات ← «تابع بندق وعزيزة» (أو الشخصيات اللي في الاسكتش). مفيش لايك+فولو+شير+حلقة سابقة مع بعض.
31. حل القضية السابقة = **فقرة مفصولة بعنوان «حل القضية السابقة»**، ومن غير «شوفوا الحلقة اللي فاتت».
32. **فتّح الخلفية حوالين الشخصيات** (إضاءة/تخفيف تفاصيل) من غير ما تغير المكان.

### تجارب (اختبار بالأرقام، مش قواعد نهائية)
- القضية 45–55 ثانية.
- حلقة المسلسل تتقسم أجزاء ≤ 60 ثانية بقفلة على الريلز/تيك توك، والكاملة على يوتيوب.
- **تغيير واحد بس في المرة**، وتسجيل الأرقام بعد 48 ساعة من نزول كل ريل في `publish/metrics/instagram.csv`.

---
## تحديث 25/11 — خطة الاكتشاف + اختبار الافتتاحية + القياس (طلب المستخدم بعد مراجعة إنستجرام 25/11 الصبح)
**الدليل (لقطة واحدة، أعمار الريلز مختلفة — وصف بس، مش مقارنة مضبوطة ولا دليل إن القواعد نفعت أو ضرت أو إن التقسيم سبب ضعف):**
القضية 11 ≈1,329 مشاهدة / 14 ث متوسط / 4 متابعين · القضية 10 1,579 / 16 ث / 4 · يوميات حديثة 1,622 / 16 ث / 3 · جزئين من م2 ح1: 243 و384 / 6 و7 ث.
ممنوع: متوسطات من ريلز بأعمار مختلفة، أو مجاميع يومية من الداشبورد، كدليل على اتجاه.

33. **أدوات الاكتشاف الأساسية دلوقتي = «مين الكداب؟» + اليوميات.** القضية تفضل 45–55 ث، والطلب الواحد زي ما هو (قاعدة 30). مفيش زيادة في عدد البوستات ولا تنازل عن الجودة عشان ننشر أكتر.
34. **«عمارة نعناعة» مكملة** بنفس الاستمرارية؛ الحلقة الكاملة على يوتيوب. على إنستجرام/تيك توك: كل جزء يتقيّم لوحده — هل ينفع كريل قصير قوي لوحده (هوك في أول 2–3 ث + قفلة)؟ التقطيع مش علاج تلقائي للوصول. **أي تغيير في خطة النشر بيتعرض على المستخدم الأول قبل التنفيذ.**
35. **اختبار الافتتاحية:** متغير واحد بس = أول 2–3 ثواني في القضية. كل الباقي ثابت قدر الإمكان (المدة 45–55 ث، الساعة 20:00 الكويت، نوع الغلاف، الكابشن 3 سطور، الطلب الواحد، فقرة «حل القضية السابقة»، عدالة الأدلة، الأصوات). التبديل A/B/A/B على كذا قضية متتالية قبل أي توصية. النشر العضوي مش A/B عشوائي → النتيجة ممكن تطلع «غير حاسمة» ومفيش فائز مضمون من عينة صغيرة.
36. **القياس:** الجدول `publish/metrics/measurements.csv` — الهدف قراءة كل ريل عند **48 ساعة**؛ نسجل العمر الحقيقي وقت القراءة، وأي رقم مش متاح يتكتب `unavailable`. ممنوع اختراع أرقام 48 ساعة قديمة أو استبدالها بأرقام النهارده.
37. **الحكم على التقدم:** المتابعين (attributed follows) + المشاهدات + متوسط وقت المشاهدة (+ نسبة غير المتابعين لما تكون متاحة)، ومقارنة نفس النوع في نفس العمر بس.

**تعارضات محتاجة قرار المستخدم (مااتغيرتش):**
- قاعدة 28 بتقول حل القضية في **آخر** الفيديو، بس القضايا 10 و11 (بطلب المستخدم) بتبدأ بفقرة «حل القضية السابقة» في **أول** الفيديو. الممارسة الحالية = أول الفيديو.
- قاعدة 3 («الحل بكره… تابع عشان ما يفوتكش») بتتعارض مع قاعدة 30 (طلب واحد: «اكتب رقم الكداب»). الشغل الحالي ماشي على 30.
- سطر التجارب «حلقة المسلسل تتقسم أجزاء ≤ 60 ث» — المستخدم قال 24/11 «مش هقطع حلقات»، والمراجعة فيها جزئين من م2 ح1. محتاج يتحدد: إيه اللي بيتنشر على إنستجرام/تيك توك من الحلقات.
