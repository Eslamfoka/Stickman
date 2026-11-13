# Locations canon — ONE background per place, for the whole brand (standing rule, user 2026-11-12)

**Rule:** every place that already appeared in Season 1 or 2 must look exactly the same in every later episode
(same room, same furniture, same camera view of the background). Between episodes only the **light** may change:
day / night / dusk, lamps on/off, torch light. Never generate a new picture of an existing place.
- Day ↔ night: use the paired files below when they exist (they are edits of the same picture — only the light changed),
  otherwise grade the canonical file in code (`s1e1/locations.py → loc(name, tod)`).
- A brand-new place: generate it once, add it to this table + `LOC` in `s1e1/locations.py`, then always reuse it.
- If a place physically changes in the story (e.g. the sheet fell in the studio), the "after" picture must be an **edit** of the
  same picture (same camera/layout) and it replaces the old one from that episode on — note it here.

| place | canonical file (day) | night / other light | used in | notes |
|---|---|---|---|---|
| مدخل العمارة (lobby: bench, mailboxes, street door, stairs, basement door) | `s1e10/bg/morning.png` | graded in code (night tint) | S1E10, S2E1–E6 | S1E1–E9 used `s1e1/bg/lobby_1080.png` (older look) — from S2 on ONLY morning.png |
| السلم (stairwell) | `s1e1/bg/stairs_1080.png` | graded (warm day / blue night) | S1, S2E3–E6 | |
| الصالة (Nana's living room, 2nd floor) | `s1e1/bg/living_1080.png` | graded | S1 | |
| أوضة العيال | `s1e1/bg/bedroom_clean.png` | graded | S1 | S2E2 bedroom `s2e2/bg_bedroom.png` = same room (posters painted over) → use bg_bedroom.png from S2 on |
| باب شقة 7 | `s1e2/bg/door7.png` | — | S1E2 | |
| شقة فهمي | `s1e5/bg/fahmy_raw.png` | — | S1E5 | |
| السطوح | `s2e6/bg/roof_day.png` | `s1e6/bg/roof_raw.png` (night) | S1E6, S2E6 | day = edit of the night picture (same layout) |
| شقة الدور السابع (رشدي) | `s1e8/bg/apt7_raw.png` | — | S1E8 | |
| شباك / بير السلم / فلاش باك م1 | `s1e9/bg/window.png`, `well.png`, `flash.png` | — | S1E9 | |
| البدروم (الأوضة اللي قبل الباب الحديد) | `s2/bg/basement_day.png` | graded | S2E1, S2E5 | S1E10 `s1e10/bg/basement.png` (electric panel, night) = older look → from S2 on basement_day.png |
| نفق الحفر (ورا حيطة الاستوديو) | `s2e8/bg/tunnel.png` | (always night: lanterns) | S2E8 | dug by the Pasha's men; hole on the left = back to the studio; foundation pillar on the right |
| ممر البدروم + الباب الحديد | `s2e4/bg/corridor.png` | (always dark) | S2E4, S2E5 | |
| الاستوديو السري | `s2e5/bg/studio_nosheet.png` | dark grade (lights off) / sepia = 1958 flashback | S2E5, S2E6 | S2E4 used `s2e4/bg/studio.png` (with the sheet over Safeeh). Sheet fell in S2E5 → studio_nosheet.png from S2E5 on |
| الشارع قدام العمارة | `s2e3/bg/street_day.png` | `s2/bg/street_car.png` (night, Pasha's car) | S2E2, S2E3 | |
| الحيطة من بره + شباك البدروم | `s2e5/bg/wall.png` | graded night (S2E6) | S2E5, S2E6 | |
| عربية الباشا (من جوه) | `s2e4/bg/carin.png` (night) | `s2e6/bg/carday.png` (day = edit of carin) | S2E4, S2E6 | S2E5 used a different generated car (`s2e5/bg/carday.png`) — retired, use the carin pair from now on |
| ترند الأسبوع: الملعب، الكافيه، المؤتمر، الجيران، الأوضة، الاستوديو | `trend/01/bg/*.png` | graded | trend 01 | |
| سلم عمارة الجيران (another building: side view, terrazzo flight bottom-left → landing top-right, plaque «الدور 10» drawn in code at world (560,410)) | `daily/bg/stairs_jeeran.png` | warm morning | يوميات 01 (التلاجة) | NOT عمارة نعناعة's stairwell |
| فصل المدرسة (green chalkboard left, teacher desk, rows of old desks right; students seated behind code-drawn desks, ROWS in daily/02/ep.py; wall clock drawn in code at world (852,168), red rim — daily/03 `clock()`) | `daily/bg/classroom.png` | warm morning | يوميات «بص على رجلي»، «بابا في المستشفى» | |
