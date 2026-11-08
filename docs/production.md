# Production pipeline & rules

## Per-episode pipeline
1. Write the script (Egyptian, fully diacritized, `[direction]` tags for eleven_v4). Show the user the event outline.
2. Pronunciation test of risky words (numbered, one TTS file with Shatta's voice) → wait for OK → regenerate/replace any flagged words.
3. Generate all lines (one take each) into `sSeE/audio/XNN.mp3`; send a review MP3 of all lines.
4. Generate any new backgrounds (gpt-image-2.5-sunburst, 1 image, painterly realistic, no people, no text) and SFX (eleven_text_to_sound_v2).
5. Copy the newest episode script as a template (`s1e10/ep10.py` is the most advanced), write the timeline, render stills (`python3 epN.py stills t1 t2 ...`), look at contact sheets, fix framing/lighting.
6. Full render (~20–30 min; runs both versions in one pass) → check vertical frames (subtitles ≤6 lines) → deliver with SendUserFile (<400 MB; re-encode crf 23 if larger).
7. Copy finals to `/home/claude/delivery/{yt,tt}` with names «الحلقة NN - العنوان.mp4» / «... (تيك توك).mp4».

## ElevenLabs
Flow id (original ElevenLabs account): `4HcN4LdOL5Uje0zAong1`. Model `eleven_v4`.
| Character | voice_id |
|---|---|
| شطة | PbQ7dZRV6nFXCZN9afve |
| زلطة | ZfCBnq4IBq228hplEROe |
| توتة | B4xStlwJJFNXunfEQt3b |
| البواب (عم بندق) | nCi0WTJgF6pOCdDt4vCO |
| الحاجة نعناعة | paE5P4ZVl6GdshM7URbd |
| أستاذ فهمي | afgElYGfUrmtrsvZWaTZ |
| طنط سوسن | hS1tssZiHEuMnvJwGnJk |
| mystery caller S1E4 (library) | uCAKWh24Y93ESUjKwRGP |
| عم رشدي | rc7ifJWKsgf7jZ0iZR8X (designed, preview #2) |
IDs work only on the same ElevenLabs account; otherwise clone from `voices/` samples.

### Current account (cloned from `voices/` samples, 2026-11-09) — USE THESE
The connector account is a different workspace; voices were re-created with Instant Voice Clone.
| Character | voice_id (clone) |
|---|---|
| شطة | zXvQZBuv4eRkV8iZFo0z («شطة ٢») |
| زلطة | EmD0DWTBW7PBAZ0QyuW9 («زلطة ٢») |
| توتة | 7ZCnzbMTLiWO91psJmFa («توتة ٢») |
| الحاجة نعناعة | oaufJ1LN6G5WBWO1vDqK («الحاجة نعناعة ٢») |
| البواب (عم بندق) | hX8NPPh9eZ6FnjN6Yf6E («عم بندق ٢») |
| أستاذ فهمي | NKmBoy2aHuBrwNejzeBY («فهمي ٢») |
| طنط سوسن | NoGIW3DYKxvKHQyByngV («سوسن ٢») |
| عم رشدي | LAMgzfyVhBwHnPhLqzu9 («رشدي ٢») |
| الباشا | a4BAIRarZjSOrxjZHzaG (designed, darker round preview #1 — NOT m4FMGAmuWc9V0kVoZxOF, the earlier calm one) |
| عبده | dtJ11OXpU7ePgFeAvCJr (designed; saved preview = #1 of its round — confirm with user, screenshot showed Voice 3) |
| صفيح | proposal: Roshdy's voice (LAMgzfyVhBwHnPhLqzu9) + Audio Effects robot/old_radio filter — Roshdy recorded his own voice into the robot. Account is at the 10 custom-voice limit. |

## Pronunciation rules learned (eleven_v4)
- Egyptian qaf → hamza: فُوء، آلُوا، آلْها، بَآلُه، مَأْفُول، صُنْدُوء، بِالأَلَم، يِبْأُوا، يِبْأَى، التِّئِيل، أَطَع، أَبْل، اتَّفَأْنا.
- Real qaf kept (user's choice): الحَلْقَة، اتْسَرَق، هَسْرَق، قُصَيَّر، قَفَلِتْ، قَفَل.
- مَحَدِش (no shadda). العِمارَة (kasra). شقة → «شَأْأَة» or avoid. الحَرامِيّ، بَطَّلْ، الكَشّافْ (final sukun).
- Avoid / replace: شرطة→«خَطّ»، خرج→«مِشِي»، غرض (removed)، قدامها→«عَلِيها»، اقعدوا→«اسْمَعُونِي كِوَيِّس»، الورقة (sounds artificial; show it instead)، ملك→«بِتاعِة»، الضلمة→«العَتْمَة»، أشجع (read as verb)→rephrase، بتحمينا→«بِيْحافِظ عَلِينا»، «ودَه بأَه»→«ودَه يا جَماعَة»، برة→«بَرّا».
- الشِّبْشِب: kasra on first shin, sukun on ba. سوسن = «سَوْسَن». بندق/قطة break in v4 → say «البَوَّاب»; قطة → «أُطَّة» with eleven_multilingual_v2 if needed.
- Trim breaths/noise before screams with ffmpeg.

## Engine anatomy (`s1e1/engine.py`)
W=1920 H=1080 FPS=24 SR=44100 SS=1.5. `draw_char(p, who, x, y, s, expr, mouth, look, blink, arms, t, held, lean, walk, eat)`.
- expr: neutral happy smug flat sad angry shout scared shock sleepy. arms: down talk up point hips scared hold shush.
- held: key torch paper lantern broom basket photo nbpen phone slipper tray sweet keys chipsbag chips notebook.
- Episode script pattern: SUB/WHO/EXPR/ARMS dicts → `say()`/`shot()` timeline, camera c0→c1 (ease/crash), `CU()` close-ups, `actors()` per set, `props()`, `light_map()` glows (1/8 res → multiply → brightness), silhouettes, eyes-only blackouts, grain + vignette, lip-sync envelope (+2 frame lead), footsteps synced to walk phase, synth SFX (knock, boom, sting, tock, powercut, drone), vertical layout (blurred bg, 1080×608 at y=560, gold bars, title, subtitles, puzzle box), loudnorm I=-15.
