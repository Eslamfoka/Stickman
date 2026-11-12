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

## Realism pass (user, 2026-11-12 — S2E5 on)
- Exits with the BACK to camera: when someone leaves the others, the camera stays and we watch him walk away from behind (back view, shrinking into depth / out the door), not a face-forward slide. Engine needs a back-view pose for characters (no face, hair/back of head, arms swinging).
- Entrances always motivated (called / knocked / heard / on the way) — unchanged, re-confirmed.
- Acting & reactions: every line gets a listener reaction (look, blink, step back, head turn), anticipation before big moves, overlap/settle after stops, weight shifts while standing — no frozen listeners.
- Camera: real coverage per scene (wide → OTS → CU → insert/POV), purposeful moves only.


## Episode checklist — run it on EVERY episode right after the voices are approved (standing rule, user 2026-11-12)
Go through each item before rendering stills, and again on the contact sheet. The user must never have to ask for these.
1. **Chain of events:** every scene starts because of something in the previous one (sound, call, discovery, look). No hard cut "out of nowhere"; J-cut sound bridges; time jumps shown (time-lapse, clock, sky).
2. **Entrances:** nobody pops in. Someone calls them, knocks, they're heard first, or we see them on their way (door, stairs, depth, frame edge).
3. **Exits:** when someone leaves, the camera stays and we watch them walk away **with their back to camera** (`draw_back`), shrinking into depth / out a door. Screen direction kept into the next shot.
4. **Camera coverage per scene:** establishing wide → two-shot → OTS → real close-ups (head & shoulders) → inserts → POV. Purposeful moves only (push-in on tension, crash zoom on scares, follow-pan on walks, low angle for villains/robot, high angle for scared kids, dutch for unease).
5. **Acting & reactions:** every line has listener reactions (look at the speaker, blink, step back, flinch, lean in); anticipation before big moves, settle after; nobody frozen; expressions change inside a line where it fits.
6. **Thrill + comedy:** hook ≤3 s, ≥2 tension peaks (one false scare, one real), a twist, puzzle, cliffhanger; 3–4 comedy beats placed right after tension.
7. **Beat the previous episode** — write down (in the episode's script.md) at least 3 concrete things that are new/better than last time: a new set or camera move, a new effect, faster rhythm, a bigger scare, a better gag.
8. **Locations:** every set comes from `docs/locations.md` (`loc(name, tod)`); the same place never changes look — only the light (day/night/lamps).
8b. **Pronunciation:** numbered test → user OK per number → one take per line → review MP3 → fix flags. Apply every rule in production.md.
9. **Delivery pack:** YouTube H + TikTok vertical (cover first frame, no title card) + Reels + Shorts (<3:00) + YT thumbnail + vertical cover + captions & pinned comments per platform as an HTML page with copy buttons (`python publish/captions_html.py <id>`, user request 2026-11-12 — not a .txt); small files via final_encode; update status.md + build.py STATUS; push after each step.
