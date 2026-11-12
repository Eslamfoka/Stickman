# Directing rules — apply to EVERY episode of every season (user, 2026-11-09)

The user wants it to feel like a real TV series being shot: chained events, camera coverage, high-level work. Read this before writing any script.

## 1. Motivated transitions (chain of cause → effect)
- No scene starts out of nowhere. Every new scene is triggered by something in the previous one:
  a sound (car engine, knock, mail slot, phone ring, footsteps), a character calling someone, a question, a discovery, or a look toward something.
  Example: kids are busy with X → they hear a car outside → they go to look → the Pasha scene begins.
- Prefer sound bridges: the sound of the next scene starts 0.5–1 s BEFORE the cut (J-cut).
- Time jumps are shown visibly (light time-lapse, clock, window sky), never just a hard cut.

## 2. Motivated entrances & exits
- Nobody pops into frame. A character enters because they were called («يا حاجة نعناعة!»), asked about, knocked, or are on their way from A to B — and we see them walk in (door, stairs, from depth, from frame edge).
- Exits: walk out of frame or through a door; the next shot picks them up entering from the matching side (screen direction kept).
- Plant & payoff: if something matters later (a key in a pocket), show it early in an insert the audience notices.

## 3. Camera language (every scene has coverage)
- Establishing wide → medium two-shot → over-the-shoulder for dialogue → close-ups for reactions → inserts for objects (phone screen, photo, key, plate) → POV shots (peephole, window, phone camera).
- Camera moves with purpose: slow push-in on tension, whip-pan / crash zoom on a scare, follow-pan when characters walk, low angle for the villain, high angle for scared kids, Dutch tilt for unease.
- Rack-focus feel (blur background) on reveals; silhouettes and backlight for mystery.
- Shot length varies: fast cuts in action/scare, longer holds before a jump-scare.

## 4. Dialogue quality
- Zero pronunciation mistakes: numbered pronunciation test before generating, rules in `production.md`.
- Every line has a purpose (plot, character, or joke). No filler.

## 5. Thrill + comedy balance
- Each episode: hook (first 3 s) → at least 2 tension peaks (one false scare, one real) → a twist/reveal → puzzle → cliffhanger.
- At least 3–4 comedy beats per episode (character running gags: Shatta's fake bravery, Zalata's percentages, Bondo's sleeping, Abdo's fear of the dark), placed right after tension to release it.


## First frame rule (all videos, from 2026-11-11 — user request)
Viewers on TikTok/Reels/Shorts decide in the first second. Every video (H and V, every series) must:
- Start directly on action/hook (a face, a sound, movement) — NO black title card at 0s. The episode title card goes after the hook (≥ 3s) or is dropped in the vertical cut (the vertical band already shows the title).
- OR open on a 0.5s "cover frame" = the episode's designed cover (publish/thumbs/<id>_cover.jpg style: big character + huge headline) that pops into the first shot — so the first frame doubles as the TikTok/Reels cover.

## Follow CTA (all videos, from 2026-11-12 — user request)
- Right AFTER the audience puzzle (not at the start; the end card is visual only): 2–3 s, in character, with a gag, rotating characters each episode.
  e.g. Zalata «احْتِمال تِفَوِّت الحَلْقَة الجايَّة لَوْ ما عَمَلْتِش فُولُو: مِيَّة فِي المِيَّة.» / Tota «اسْمَعُوا كَلام تُوتَة... فُولُو ولايْك وشِير!» / Shatta «ثِقُوا فِيّا... اعْمِلُوا فُولُو!»
- Spoken line is the same everywhere («فولو ولايك وشير»); the picture changes per version: a drawn phone in the character's hand shows the user's REAL profile screenshot
  (`brand/follow/{yt,fb,ig,tt}.png`, made by `brand/follow/crop.py` from `raw/` — follower/video counts hidden, video grid cropped), an animated finger taps Follow/Subscribe, glow ring, click sfx, button flips to Following/Subscribed, heart pops.
  YouTube version → yt.png (+ bell); vertical TikTok cut → tt.png; Reels → ig.png / fb.png.
- End card: platform screenshot thumbnails + @shattawzalata under «الحلقة X بكرة», no voice.
