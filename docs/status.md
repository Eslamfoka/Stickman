# Status — last updated 2026-11-09 (second Claude account, new ElevenLabs workspace)

## Season 2 progress
- Plan merged (record + robot «صفيح») → `docs/seasons/season2_sirr_elbadroom.md` (approved by user).
- All 8 S1 voices re-cloned + الباشا + عبده designed on the new account (IDs in `docs/production.md`). صفيح = Roshdy clone + robot filter. Account is at its 10 custom-voice limit.
- **Ep1 «باب البدروم» DONE & delivered** (2:34, 32 lines). Script `s2e1/ep1.py` (render: `python3 ep1.py part 0 2` & `part 1 2` in parallel → concat → `python3 ep1.py audio` → mux; YT file re-encoded crf 24 to stay < 400 MB). Lines/plan in `s2e1/script.md`.
- **Ep2 «الصوت اللي تحت الأرض» DONE & delivered** (2:36, 29 lines). `s2e2/ep2.py` — new: one unified lobby set (morning.png) with day/night time-lapse (`tl=`), walk-ins from the street door with depth scaling (`walk_to`), exits out of frame, camera pans following kids, bedroom set `s2e2/bg_bedroom.png` (real-player/club posters painted over), window POV, street set with the Pasha silhouette (`draw_pasha`), walkie prop, headlight sweep. User feedback for all future eps: realistic continuity (nobody pops in), more thrill, fewer characters is fine.
- Ep2 puzzle: «السبعة اللي بتستنى الجوابات» → answer in Ep3: صندوق بوستة شقة 7 (glint easter egg already shown at ~29 s). Ep2 cliff: Pasha («أيوا يا عبده... الولاد ابتدوا يدوروا. لازم نسبقهم» / «هاخدها ولو بالعافية») saw Shatta at the window. Tota's phone is recording in the vent all night → Ep3 can open with what it recorded.
- **Ep3 «الباشا»** (3:12, 32 lines E01–E32, NEW ElevenLabs account) — `s2e3/ep3.py`, script+shot list `s2e3/script.md`. New: phone-playback insert (`phone_card`), old photo insert with flip (`photo_card`), POV through the street-door glass on a generated day street (`s2e3/bg/street_day.png`, `glass_frame`), phone-camera POV (`phone_ui`), Pasha full body with fedora+cigar, Abdo with bump stars, street-door leaf that opens, stairs set for entrances (`stairs_1080.png`), plant&payoff key insert, night theft, dutch angle. Follows `docs/directing.md`.
- Ep3 puzzle: «مين في الموسم الأول كان بيقول "أيوا يا باشا" في التليفون؟» → answer in Ep4: فهمي. Ep3 cliff: Abdo has the basement key (it was in the doorman's pocket all along) + red light under the basement door.
- **Ep4 «النزول»** (2:29, 26 lines F01–F26) — `s2e4/ep4.py` (built from ep3 pieces). New sets generated: `s2e4/bg/studio.png` (secret studio, clock at 12, sheet in the right corner, poster of a 1950s singer = الست بهية for Ep6), `corridor.png` (vault door with wheel), `carin.png` (Pasha's car at night; seat cushion re-pasted over the characters so they sit). New: flashlight beams (dark-set composite), slow-mo keys insert, padlock/key insert, wheel insert, lights flicker-on reveal, flashlight scan inserts, reel-to-reel spin, sheet wobble + red eyes.
- Ep4 puzzle: «الساعة الواقفة في الاستوديو على كام... وليه؟» → Ep5 answer: 12 = the timer that plays the tape every night. Cliff: صفيح under the sheet (red eyes).
- Next: Ep5 «صفيح» — design صفيح's voice (robot) + draw `safeeh` in the engine; template `s2e4/ep4.py`.

---
# (older) Status — 2026-11-08 (end of session on the first Claude account)

## Done
- Season 1, episodes 1–10: rendered and delivered (YouTube horizontal + TikTok vertical). Scripts: `s1eN/epN.py` (ep1: `s1e1/ep.py`).
- Voices guide + clone samples: `voices/` (also on the user's PC in `D:\ستيك مان\عمارة نعناعة - سر الدور السابع\الأصوات`).
- Full-season compilation «الفيلم الكامل» v1 (13 min) delivered: all episodes joined with titles/endcards/recaps/puzzles removed (`movie/plan.py` = cut list, `movie/cut_segments.py`).

## Recently finished
1. **Movie v2** — DONE and delivered (14:24). User asked: a hook (≥10 s) at the very start, then an animated character introduction (each character introduces himself + catchphrase), then the series.
   - Hook: `movie/hook.sh` (8 clips, 17.7 s) — built.
   - Title: `movie/title.py` → `movie/seg/title.mp4`.
   - Character intro: `movie/intro/intro.py` (lines in `movie/intro/audio/*.mp3`, all approved by the user; Shatta's line was re-done to «أَنا شَطَّة! مَفِيش حاجَة بِتْخَوِّفْنِي... إِلّا العَتْمَة شُوَيَّة. ثِقُوا فِيّا المَرَّة دِي!» because «أشجع» was mispronounced). Renders `intro.mp4` (~60 s): 7 character cards + Roshdy silhouette teaser + group shot.
   - Assemble: re-render all episodes (if MP4s missing), then `python3 movie/cut_segments.py`, `bash movie/hook.sh`, `python3 movie/title.py`, `cd movie/intro && python3 intro.py`, `bash movie/assemble.sh`. Order = hook → title → intro → episode segments (the old v1 put the title after ep1's cold open; v2 does not).
   - Deliver with SendUserFile (must be < 400 MB; assemble.sh caps bitrate → ~300 MB).
2. **Season-2 trailer** — DONE: `promo/promo.py` → «اعلان الموسم التاني - سر البدروم.mp4» + «(تيك توك).mp4» (~57 s).
   Structure: CCTV basement (shadow, knocks) → glitch → Sawsan «عاجل» live news (knocks behind her, she freezes) → «الإرسال اتقطع» color bars → Roshdy's letter in 5 short lines (voice rc7ifJWKsgf7jZ0iZR8X, light echo) over letter / sepia flashback / building at night / dark lobby / light under the basement door → fast CUs Nana, Shatta, Zalata with rising knocks → CCTV: basement door opens, Shatta's face pops into the lens screaming → title «عمارة نعناعة — الموسم التاني — سر البدروم — قريباً».
   Lines (all approved): SW1 «عاجِلْ... عاجِلْ يا مُتابْعِين! بَعْد ما مِسِكْنا أُسْتاذ فَهْمِي... فِيه صُوت جايّ مِن البَدْرُوم!» (NOT «خبر عاجل» — read as «خبرٌ»), SW2 «...إِيه دَه؟», RO1 «نَعْناعَة... يا أُخْتِي.», RO2 «لَوْ الجَواب دَه وِصِلِك... يِبْأَى العِيال عِرْفُوا السِّرّ.», RO3 «بَس فِيه سِرّ تانِي... أَكْبَر بِكْتِير.», RO4 «تَحْت... فِي البَدْرُوم.», RO5 «افْتَحُوه... بَس ما تِفْتَحُوهُوش بِاللِّيل.» (NOT «أوعوا»), NA1 «مَحَدِش هَيِنْزِل البَدْرُوم!», SH1 «ثِقُوا فِيّا... المَرَّة دِي بَجَد!», ZA1 «احْتِمال نِرْجَع: خَمْسِين فِي المِيَّة.»
   «الإرسال اتقطع» is on-screen text only (spoken it became «اتقطاع»).

## Next
- **Season 2 «سر البدروم»** — plan is READY in `docs/seasons/season2_sirr_elbadroom.md` (truth, villain «الباشا» + «عبده», 10-episode table, Ep1 draft script with risky-word list). Steps:
  1. Summarize the plan to the user in Egyptian Arabic, get his notes/OK.
  2. Design voices for الباشا and عبده (descriptions in the plan; 3 previews each; user picks).
  3. Ep1: pronunciation test → generate lines → animate (use `s1e10/ep10.py` as template; put files in `/home/claude/s2e1/`, backgrounds from `s2/bg` + season-1 bgs) → render → deliver.
  4. Engine already has `pasha` and `abdo` characters (`s1e1/engine.py`).

## Assets index
- Backgrounds: `s1e1/bg` (living, bedroom, lobby, stairs), `s1e2/bg/door7.png`, `s1e5/bg/fahmy_raw.png`, `s1e6/bg/roof_raw.png`, `s1e8/bg/apt7_raw.png`, `s1e9/bg` (window, flash, well), `s1e10/bg` (basement, morning).
- SFX per episode in `s1eN/sfx`. Synth SFX (knock, boom, sting, tock, powercut, drone) in engine.py.

## Trend «أزمة منتخب العمارة» — DONE (2026-11-10)
6 parts (trend/01/part1..6.py, shared kit.py with cinematic transitions) + movie (trend/01/movie.sh, 4:15). All delivered (H + V).
Next: Ep5 «صفيح» of عمارة نعناعة (design robot voice + draw `safeeh`), then other series toward the 1-month buffer.

## NEXT (2026-11-11) — Brand intro video «تعالوا نعرّفكم على عيلة شطة وزلطة» (~45s, H + V)
User approved the idea. Pin it first on every platform (YouTube channel trailer).
- 0-3s logo burst; Shatta runs in: «استنى استنى! انت لسه ما تعرفناش؟!»
- 3-4s per character, motivated entrance + big name card + one-liner:
  شطة «أنا شطة… ثقوا فيّا!» (something falls behind him) / زلطة «احتمال إنك تحبنا: مية في المية» /
  توتة «أنا أذكى واحدة هنا… بس محدش بيسمع كلامي» / نعناعة «اللي هيعمل دوشة… الشبشب جاهز» /
  quick: سوسن «عاجل!»، عم بندق، فهمي، الباشا، عبده
- End: everyone in one shot + series list «عمارة نعناعة • يوميات • ترند الأسبوع» + «تابعونا… حلقة جديدة كل يوم».
- Reuse movie/intro/intro.py as a base; brand v2 style (Lalezar logo, brand/pro.py helpers).
- Pronunciation test first (rule 1).

## Publishing status (2026-11-11)
- YouTube: trend ep1-2 published; ep3-4 scheduled Nov 11 22:00/22:30 KW (user). ep5-6, trend movie, nanaa s1 e1-2: files + text sent, user scheduling.
- FB+IG (Meta Business Suite): trend ep3-6 scheduled. TikTok: ep1 posted manually.
- Shorts series «يوميات»: user rejected first jokes (not funny). Waiting for user to send videos that make him laugh before writing new ones. Don't reuse Y101–Y303.
- Brand intro: lines I01–I07 generated → brand/intro/audio/ (review MP3 sent; waiting user OK). Next: write brand/intro/intro.py (H+V) reusing movie/intro/intro.py + brand/pro.py style.

## Update 2026-11-11 (evening)
- Brand intro video DONE: `brand/intro/intro.py` (36 s, H+V, end card «مين فيهم شبهك؟» + @shattawzalata). YouTube thumb made (thumb_intro). User publishing it (YT daily upload limit hit → needs channel Verify or wait 24h).
- TikTok cuts of trend ep3–6: first 0.5 s = episode cover (publish/thumbs/*_cover.jpg), title card removed (`ep*_vertical_tiktok.mp4`). New standing rule in docs/directing.md: first frame = hook or cover.
- Early stats (day 1): IG reels ~230–260 views with 0 followers; TikTok 30–36; YouTube long-form ~0–1 → push YouTube Shorts (vertical) for every episode.
- Meta: publish reels ONCE (Business Suite → FB+IG together); user had a duplicate FB reel to delete.
- All delivered files re-sent as 6 zips (delivery/pack/).
- Season 1 ep9–10 being re-rendered for the user (he only had 8); then season-1 movie (needs all 10 rendered → movie/assemble.sh steps above).
- Season 2: ep1–4 done; next Ep5 «صفيح».
