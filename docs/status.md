# Status — last updated 2026-11-09 (second Claude account, new ElevenLabs workspace)

## Season 2 progress
- Plan merged (record + robot «صفيح») → `docs/seasons/season2_sirr_elbadroom.md` (approved by user).
- All 8 S1 voices re-cloned + الباشا + عبده designed on the new account (IDs in `docs/production.md`). صفيح = Roshdy clone + robot filter. Account is at its 10 custom-voice limit.
- **Ep1 «باب البدروم» DONE & delivered** (2:34, 32 lines). Script `s2e1/ep1.py` (render: `python3 ep1.py part 0 2` & `part 1 2` in parallel → concat → `python3 ep1.py audio` → mux; YT file re-encoded crf 24 to stay < 400 MB). Lines/plan in `s2e1/script.md`.
- Next: Ep2 «الصوت اللي تحت الأرض» — must beat Ep1 (more lines/events). Use `s2e1/ep1.py` as template.

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
