# عمارة نعناعة — Brand bible & handoff for the next Claude session

You are continuing a long project with the same user (Egyptian; writes in Egyptian Arabic — always reply in Egyptian Arabic, short and friendly).
This file describes the **whole brand** (many seasons will follow), not one season.
Read in order: this file → `docs/directing.md` → `docs/brand.md` (world & characters canon) → `docs/production.md` (pipeline & rules) → `docs/status.md` (what's done / what's next) → `voices/دليل الأصوات - عمارة نعناعة.txt`.

## The idea in one paragraph
«عمارة نعناعة» is the user's own original cartoon brand: big-white-head stickman characters (style like «فشارة»), Egyptian dialect, for the whole family. Everything happens in one old popular Cairo building — «عمارة نعناعة» — and its residents. The brand is built as **seasons of short daily mystery serials**: each season has one big secret in the building, split into ~10 daily episodes (≈1.5–2.5 min each). Every episode = hook in the first 3 seconds → events → an audience puzzle («اكتبوا حلكم في الكومنتات») → a cliffhanger; the next episode opens with the puzzle answer. Tone: light family horror (darkness, whispers, shadows, knocks — never blood, never real ghosts; everything has a logical explanation at the end) always broken by comedy. Goal: go viral and monetize on YouTube, TikTok and Facebook (horizontal for YouTube, vertical cut for TikTok/Reels/Shorts, plus a full-season compilation "movie").

## Brand name = «شطة وزلطة» (channels/handles). «عمارة نعناعة» is ONE series inside it. The brand has 5 series (see `docs/series.md`, `docs/calendar.md`)
عمارة نعناعة (main mystery serial) + يوميات شطة وزلطة + لو...؟ + زلطة بيشرح + ترند الأسبوع — same trio (شطة، زلطة، توتة) everywhere. Goal: build a 1-month buffer before publishing daily.

## Who does what
Claude does everything: story, fully diacritized scripts, voices (ElevenLabs MCP connector), animation (Python/PIL engine in `engine/` → actually `s1e1/engine.py`), rendering (ffmpeg), editing and delivery. The user reviews pronunciation and gives notes.

## Non-negotiable working rules (from the user)
1. Pronunciation must be perfect. Run a **numbered pronunciation test** of risky words before generating any new dialogue; wait for the user's per-number OK. After generating, send one review MP3 of all lines in order. Fix any word he flags.
2. **One take per line** (`generations_count=1`).
3. Each episode must beat the previous one: faster rhythm, more events, more mystery/thrill, more professional animation, zero mistakes.
4. Design **brand-owned voices** (ElevenLabs Voice Design) for every recurring character — don't use other people's library voices for main characters (monetization).
5. Never accept passwords / tokens from the user.
6. **Directing rules for the whole project** in `docs/directing.md`: motivated transitions (a sound/call/discovery triggers every next scene), motivated entrances (nobody pops in), real TV-series camera coverage (wide/OTS/CU/insert/POV, purposeful moves), zero dialogue mistakes, more thrill AND keep the comedy. Read it before writing any script.

## Repo layout
- `s1e1/engine.py` — the animation engine (characters, props, audio helpers). Shared by all seasons.
- Season 1 lives in `s1e1..s1e10/`. Season 2 shared assets in `s2/` (bg); create episode folders `s2e1/ … s2e10/` (same `sSeE` naming).
- `movie/` — tools that join a season into one long video (hook + character intro + episodes).
- `promo/` — season-2 trailer work in progress.
- `voices/` — voice guide + clean samples for cloning.
- `docs/` — brand canon, production pipeline, status, season bibles.

## Quick setup in a fresh cloud session
```bash
unzip "عمارة نعناعة - المشروع كامل.zip" -d /home/claude/repo   # or git clone
bash /home/claude/repo/setup.sh       # symlinks /home/claude/s1e1.. etc. (scripts use absolute paths)
pip install numpy pillow --break-system-packages
```
Rendered MP4s are not included (too big) — re-render with `cd /home/claude/s1eN && python3 epN.py` (ep1 = `ep.py`).
