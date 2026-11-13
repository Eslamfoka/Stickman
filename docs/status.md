# Status — last updated 2026-11-12 21:45 (S2 MOVIE delivered · new series «ميكروفون توتة» started)

## Latest (2026-11-12 evening)
- **S2 movie DELIVERED** «عمارة نعناعة م2 - سر البدروم (الفيلم كامل).mp4» (21:28, 280 MB). Pipeline `movie/s2/`:
  `bash movie/s2/render_all.sh` (horizontal-only render of every S2 ep → s2eN/movie_src.mp4, ~65 min on 2 CPUs) →
  `python movie/s2/movie.py all` (segs = titles / puzzles / follow CTAs + phone inserts / endcards / «لغز امبارح» to camera cut;
  hook 23 s; title card; assemble + `final_encode` crf 26 + DENOISE → <400 MB; writes `movie/s2/chapters.txt`).
  Ep10's season-end card «الموسم التالت قريباً» is kept as the movie ending. No character intro (S1 had one) — optional later.
  Publish item `nanaa_s2_movie` (2026-12-05 18:00, YT + FB video, chapters in the description), thumbs + captions HTML made.
- **Season 3 «ليلة التماثيل» PAUSED** (user): publish S2 first; start a second series to run alongside «عمارة نعناعة».
- **New series «ميكروفون توتة»** (user idea): Tota the reporter asks one question → flipped punchline → trademark laugh at the end
  (original laugh in the spirit of محمد ثروت, not his voice). Laugh rotation: ep1 شطة → ep2 زلطة → ep3 توتة → repeat.
  Ep1 «السجاير والعربية» (smoker = عم بندق, NOT the kids): script `mic/01/script.md`; pronunciation test sent
  (flow 9QwM1UhhHsYogaHwMAYZ, gen jwvG8E1rGMBnmzaIFjJD, 24 items, 23–24 = laugh options) → all approved after fixes; lines P01–P17 approved.
  Animation DONE: `mic/01/ep.py` (58 s; street loc with Bandaq's drawn Fiat 128 painted over the parked car, mic prop, facts chips,
  calculator cards + «1,095,000 جنيه!», dream bubble «موديل 2026», crickets beat, Shatta laugh with NEW engine expr "laugh").
  Rendered mic/01/mic01_h.mp4 + mic01_v.mp4 (+ mix.wav). Publish item `mic_e01` (24/11 15:00), thumbs + captions HTML done.
  DELIVERED 2026-11-12 23:35: delivery/mic/ YT (58 s, 29 MB) + «(تيك توك وريلز وشورتس)» cover-first vertical (11 MB) + thumbs + captions HTML.
  Laugh rotation next: ep2 = زلطة.
- **«يوميات شطة وزلطة» 01 «التلاجة» DELIVERED 2026-11-13** (38.6 s): user's own script (`daily/01/script.md`), lines Shatta/Zalata/Bandaq,
  ending = Bandaq's laugh. New canonical location «سلم عمارة الجيران» `daily/bg/stairs_jeeran.png` (side view; plaque «الدور 10» drawn in code).
  Bandaq: galabeya hem held in his teeth while climbing (NEW engine option `CH["bondo2"]["hem"]=True`), drops it to talk; he stands lower on the stairs.
  `daily/01/ep.py` → delivery/daily/ YT + cover-first vertical; publish item `daily_e01` (25/11 15:00), thumbs + captions done.
- 2026-11-13: sketch series never say «الحلقة N» (user) — mic01/daily01 re-rendered + renamed (no number). Fridge B01 → «ليكم عندي خبرين» (user).
- **يوميات «بص على رجلي» DELIVERED 2026-11-13** (36.6 s): أستاذ فهمي teacher, crowded class (Tota, Abdo, 6 generic kids `kid0-5`), reactions on every line,
  ending = stand-up style audience laugh (SFX) + Shatta/Tota/Abdo laughs. New location `daily/bg/classroom.png`; engine pose `CH[who]["legup"]`.
  `daily/02/ep.py`; publish item `daily_e02` (26/11 15:00).
- **يوميات «بابا في المستشفى» DELIVERED 2026-11-13** (~64 s): user's script (classic joke). 4 «days», each opens on a CU of a code-drawn wall clock
  racing later (8:05→8:45) + day title; knock off-screen left → class turns → Shatta walks in; two-shots Fahmy+Shatta (Zalata listening at edge);
  escalating class reactions (aww SFX → glances → groan + Zalata counting ١٢٣ «٣ أيام؟!» → frozen silence + cricket); F08 shout with shake,
  Shatta runs out back-to-camera; ending = audience group laugh (3 shots). `daily/03/ep.py`; publish item `daily_e03` (27/11 15:00).
- **يوميات «الواجب» DELIVERED 2026-11-13** (36.9 s): user's idea (classic joke). Hook = Fahmy smashes the stick on the front desk «طاخ!»;
  class panic (papers flying, Shatta proudly raises his notebook, Zalata calm); Fahmy patrols → Zalata raises his hand (NEW engine poses
  `raise`, `clap`/`clap2`); trap question in two-shots; Fahmy's speech to the class (nods, Tota claps); «أصلِ انا معملتش الواجب» + glasses glint;
  freeze + cricket, Fahmy speechless (mouth opens/closes, stick up/down, eye twitch, stammer, steam) → audience laugh 5 s (user: max 5 s, audience on top).
  Laugh mix rule (all sketches): GROUP mixed at dialogue RMS +2 dB. `daily/04/ep.py`; publish item `daily_e04` (28/11 15:00).
- **يوميات «الأرض لسه مبلولة» DELIVERED 2026-11-13** (50 s): user's script (classic joke). NEW recurring character **خالتي عزيزة** (Bandaq's wife,
  engine `aziza`: tarha + fuchsia galabeya + earrings, voice Dv1UgcydoyiSg2fH2eq8) and **الظابط** (engine `officer`: black uniform + police cap,
  voice C1WaRk8H5lP4Jvv5OfTN). Lobby (mop swipes, wet-floor shine, bucket dunk + splash, cold tint for the scary smile, slipper print «تششش!»,
  scream with radial speed lines + crash zoom + shake, Bandaq sweating) → black «تاني يوم...» → outside wall (s2e5 wall.png) Sawsan live with mic,
  LIVE badge + rising viewer count; officer glances nervously «مستنيين الأرض تنشف» → both laugh together + audience (5 s). `daily/05/ep.py`; item `daily_e05` (29/11 15:00).
  Thumb badge pill now grows with long sketch names (build.py).
- **يوميات «آخر يوم» DELIVERED 2026-11-13** (28 s): user's idea (classic joke). Lobby: Bandaq SITS on a code-drawn dikka (seat plank + legs drawn
  over him, shins below = sitting trick for galabeya characters), chin in hand, sigh «هـــه...»; Shatta comes down whistling (♪ notes, whistle cut
  when he sees him); sepia thought-bubble flashback of Aziza (arms crossed → turns her back «هِمّ!»; line reworded by user to «مش هتكلم معاك»);
  Shatta claps «أسبوعين راحة!»; Bandaq «النهارده آخر يوم!» plain sad (user: crying was over the top → calm re-take, single tear, fountain removed) → Shatta's laugh + light audience (5 s). User: no rain-cloud gag,
  no extra tag. FIX: first cut had «أسبوعين راحة من غير خناق» glued to the laugh (heard after «آخر يوم») — recut at the real gap (6.72 s). `daily/06/ep.py`; item `daily_e06` (30/11 15:00).
- **PUBLISHING (user, 2026-11-13):** the 7 sketches went out on **Facebook + Instagram only**: «السجاير والعربية» published 13/11, «التلاجة» scheduled 13/11 22:00, «بص على رجلي» → «آخر يوم» scheduled 14→18/11 at 22:00 (with the Nanaa episode). YouTube + TikTok not yet. FB/IG need new sketches from 19/11.
- Ideas bank: `docs/ideas.md` (التلاجة / أستاذ فهمي المدرس — user ideas 2026-11-12, to adapt).


## Where we stopped (2026-11-12)
- S2E5 «صفيح» DELIVERED (YT, TikTok, Reels, Shorts, thumbs, captions HTML `publish/captions/nanaa_s2_e05.html`).
- S2E6 «الأسطوانة» DELIVERED (YT, TikTok, Reels, Shorts 2:19, thumbs, captions HTML `publish/captions/nanaa_s2_e06.html`).
- S2E7 «فهمي التايب» DELIVERED (2:17; YT 50 MB, TikTok/Reels/Shorts 2:16 cover-first, thumbs, captions HTML `publish/captions/nanaa_s2_e07.html`). `s2e7/ep7.py` = found-footage phone video, thumps + crack + dutch, first audience VOTE, blackout eyes-only, torch beams, corridor POV, empty robot spot (dust-free patch + drag marks + antenna bulb), van + Pasha's cigar ember. Delivery: concat h/v parts + mix.wav → reels/shorts = phone_ig/phone_yt overlaid at the phone window (62.292–66.25) → tiktok_cut (title 6.98–8.98) → final_encode.
- S2E8 «ليلة البدروم» DELIVERED (2:10; 23 lines K01–K23 approved; YT + TikTok/Reels/Shorts cover-first + thumbs + captions `publish/captions/nanaa_s2_e08.html`). `s2e8/ep8.py`: new canonical set `s2e8/bg/tunnel.png` (`loc("tunnel")`), Shatta's crawl (mouse + Abdo torch freezes), antenna-plug insert, «رشدي؟! / أنا عبده!» gag, first chase, basement night→dawn time-lapse with the sun beam on the CRESCENT tile (Ep9 answer = الهلال), tiles insert, Pasha's ringed hand + reveal. Engine: `draw_safeeh(..., antenna=False)`, held "antenna". Safeeh voice filter now in repo: `s2/robot_fx.py`. Phone window 110.958–113.417, title 6.96–8.96.
- S2E9 «الصندوق» DELIVERED (1:59; 25 lines M01–M25, M13 = reused S2E8 K10). `s2e9/ep9.py`: car hook (box on the Pasha's lap), plan-board insert, Sawsan live POV, speaker under the seat (red LED + robot voice), heist on the night street, empty box + Season 3 tease (old photo: young Roshdy + sheet-covered figure with a pharaoh crown; key tagged «الدور الأخير» = the closed top floor, S3 «ليلة التماثيل»), Roshdy's letter voice-over, radio hint, loader cliff. Change vs the season plan (user OK): the KIDS get the box back and find it empty; the Pasha orders the loader → demolition at dawn.
- **S2E10 «أغنية العمارة» (FINALE) DELIVERED 2026-11-12 19:00** (1:56; 21 lines N01–N21; `s2e10/ep10.py`; YT 52 MB + TikTok/Reels/Shorts 1:55 cover-first + thumbs + captions `publish/captions/nanaa_s2_e10.html`; publish date 2026-12-03). SEASON 2 COMPLETE (10/10).
- NEXT (not asked yet): Season 2 movie (`movie/` pipeline like S1), Season 3 «ليلة التماثيل» script (see the decisions below), YouTube uploads backlog.
  - Season 3 decisions (user): statues stay INSIDE عمارة نعناعة in the closed «الدور الأخير»; S3 Ep1 = football flies into that floor → locked → kids remember the S2 key → take it from Nana's drawer → open → statues. See `docs/seasons/season3_tamaseel.md`.
- New standing rules today (CLAUDE.md 7–8 + docs/directing.md checklist): episode checklist applied automatically after voice approval; **locations fixed** (`docs/locations.md`, `s1e1/locations.py`); captions always as HTML with copy buttons; follow CTA after the puzzle (rotate characters: E5 زلطة, E6 شطة, E7 توتة…).
- Song «أغنية العمارة»: take 2أ chosen (`s2/music/`).
- Next episodes: E7 «فهمي التايب» → E10, each must beat the previous one.

## Season 2 — Ep5 «صفيح» (2026-11-12)
- ElevenLabs connector = the NEW paid account (workspace d59b5261…), flow `F8vbDWj8zsb2EVQ1DhIh` (all S2E5 gens in `s2e5/gens.txt`).
- Script `s2e5/script.md` (27 lines G01–G27, all approved after fixes), audio `s2e5/audio/GNN.mp3` (Safeeh = Roshdy clone YGNy… + robot filter B; G17 tape fx; G27 phone fx).
- New in `s1e1/engine.py`: `draw_safeeh()` (tin robot, eye red/green, mouth grill, chest drawer + tape, reach) and `draw_back()` (characters walking away, back of head). `brand/pro.py` figure() supports "safeeh".
- New bgs: `s2e5/bg/studio_nosheet.png` (studio with the sheet on the floor), `wall.png` (outside wall + basement window), `carday.png` (Pasha's car by day).
- `s2e5/ep5.py` (2:23): hook sheet falls → chase → clock turned to 3 = eyes red→green → «رشدي؟» scan POV → chest tape riddle → puzzle → Zalata follow CTA (phone insert with the real profile screenshot `brand/follow/*.png`, per platform: H=yt, TikTok=tt, `python ep5.py phones` → phone_ig.mp4 / phone_yt.mp4 for Reels/Shorts) → alarm → goodbye → corridor false scare (claw on Shatta's shoulder) → kids climb the stairs with their backs to camera → Safeeh under the window → Abdo's face → Abdo calls the Pasha → eyes back to RED.
- Ep5 puzzle: فزورة رشدي «أنا فوق الكل ومليان مية بس عمري ما شربت» → Ep6 answer: خزان المية على السطوح. Cliff: Pasha «يبقى هو المفتاح. هاته.» + Safeeh's eyes red.
- Publish item `nanaa_s2_e05` (2026-11-28 21:00) in `publish/build.py`, thumbs made.
- **Ep5 DELIVERED 2026-11-12**: delivery/s2/ «… الحلقة 05 - صفيح» (يوتيوب 64 MB / تيك توك / ريلز انستا وفيس / شورتس يوتيوب 2:21) + thumbs + captions txt.
  Render recipe: `python3 ep5.py audio` → `part 0 2` & `part 1 2` → concat → mux mix.wav → `python3 ep5.py phones` (phone_ig/phone_yt) → overlay those on v at the phone window → tiktok_cut --cut <title> (see the shell steps in the session; title 7.02–9.02, phone 85.21–88.79).
- Original song «أغنية العمارة» (الست بهية) via ElevenLabs Music: `s2/music/` (v1 + v2 takes أ/ب after the user's pronunciation notes; waiting for his pick). Use a snippet in Ep6 flashback, full song in Ep10.
- **Ep6 «الأسطوانة»**: script `s2e6/script.md` (23 lines, all approved), audio `s2e6/audio/HNN.mp3`; new bg `s2e6/bg/roof_day.png`. NEXT: write `s2e6/ep6.py` (template `s2e5/ep5.py`) following the Episode checklist in docs/directing.md.

---
# (older) Status — 2026-11-09 (second Claude account, new ElevenLabs workspace)

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

## PLAN — smaller files, same quality (user request 2026-11-11)
- Problem: deliveries are big (YT eps 300–400 MB, near the SendUserFile 400 MB cap; >25 MB can't go over the device bridge).
- Fix: keep the fast `-preset veryfast` for the raw part renders, then do ONE final encode per delivered file with
  `libx264 -preset slow -tune animation -crf 22 -pix_fmt yuv420p -movflags +faststart` (+ AAC 160k). Flat cartoon frames compress
  2–4× better with slow preset + animation tune at the same visual quality. Check size/quality on one episode, then make it a shared
  helper (`publish/final_encode.py`) and call it from every epN.py mux / tiktok_cut.py.
- Optional later: x265 (HEVC) copies for archive only (platforms re-encode anyway; keep H.264 for upload compatibility).
- DONE 2026-11-11: `publish/final_encode.py` (preset medium + tune animation, crf 23) → S2 ep3 YT 370 MB → 132 MB, no visible change
  (main size cause = per-frame film GRAIN in finish(); softer/static grain would shrink files further — try on the next episode).
  `publish/tiktok_cut.py <vertical> <cover> <title_start> <title_end> <out>` makes the TikTok cut (0.5 s cover, no title card), same encoder.
  Shorts > 3:00: `tiktok_cut.py <v> <cover> <out> --cut a-b --cut x-end --speed 1.02` (S2 ep3 Shorts: cut title, 160.4–165.0 dusk, end card → 2:58).
  Title times: `python epN.py times` → "title" line (S2 ep3 38.51–40.51, ep4 20.13–22.13).
- Brand intro publish pack: `publish/build.py` item `brand_intro` (thumbs/brand_intro_yt.jpg + _cover.jpg, texts in schedule.md). Sent to user 2026-11-11.
  `python publish/build.py --only <id>` = thumbs for one item.
- S2 ep3 + ep4 rendered and delivered (YT + TikTok cut) into delivery/s2/.
- 2026-11-12: S1 Shorts/Reels versions for ep1–10 made (cover 0.5 s first, title card cut, all < 3:00) → delivery/s1_shorts/, sent to user.
  Title times used (S1): e1 9.06–12.06, e2 18.96–21.56, e3 6.4–8.7, e4 10.37–12.07, e5 11.59–13.19, e6 7.3–8.9, e7 8.81–10.41, e8 3.0–4.6, e9 6.56–8.16, e10 5.48–7.18.
- RULE (user, 2026-11-12): from Season 2 on, every episode is delivered as YT horizontal + TikTok/Reels vertical + YouTube Shorts (<3:00), the vertical ones with the cover as first frame.
- 2026-11-12: S1 vertical recap reel (85 s, no final-reveal spoiler, end card «الحكاية كاملة على يوتيوب») → `python movie/recap.py` (clip list inside), cover publish/thumbs/nanaa_s1_recap_cover.jpg. For TikTok on S1 movie day instead of the full movie (user: movie render paused).

## NEXT (agreed with user 2026-11-12, end of session)
- Publishing state lives in `publish/build.py` → `STATUS` (regenerate with `python publish/build.py --no-thumbs`). As of 2026-11-12: trend everywhere; S1 ep1–10 on TikTok/FB/IG; YouTube through S1 ep6; S1 movie on FB + recap reel on TikTok/IG/FB. Missing: YouTube S1 ep7–10 (+ Shorts ep6–10, thumbnail ep6), YouTube S1 full movie (re-assemble with movie/assemble.sh steps).
- Tomorrow: FINISH SEASON 2 «سر البدروم» (ep5 «صفيح» → ep10) so it can be scheduled too (S2 ep1–4 are scheduled-ready on the calendar 24–27/11).
- Then START A NEW SERIES to run alongside «عمارة نعناعة» (decide which of docs/series.md with the user).
- STANDING DELIVERY RULE for every new video: YouTube horizontal + TikTok/Reels vertical with the COVER as first frame (no title card) + YouTube Shorts (< 3:00, cover first) + thumbnails: `publish/thumbs/<id>_yt.jpg` (1280×720) and `<id>_cover.jpg` (1080×1920) via a new item in `publish/build.py` + captions/pinned comments for YT, Shorts, TikTok, IG, FB.
  Tools: `publish/final_encode.py` (small files), `publish/tiktok_cut.py` (cover-first cut, `--cut`, `--speed`), `python publish/build.py --only <id>` (thumbs).
