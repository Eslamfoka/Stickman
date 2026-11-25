# Metrics
- `instagram.csv` — the 23/11 IG review (ages 8–80 h, one read each). Kept as recorded.
- `measurements.csv` — from 25/11 (growth rule 36). One row per reading. Target = 48 h after posting; record the REAL age and the exact
  read time; write `unavailable` for anything the dashboard doesn't show. Never back-fill a 48 h number from a later/earlier reading.
- Compare only same format at similar age. `opening_variant`: `old structure` (cases ≤11, answer first) · `new structure` (case 12 = first example: new hook first, answer at the end) · later hook variants `H-A` / `H-B` (rule 37). Snapshot rows from 25/11 are historical, unequal ages — never 48 h results.
- Scheduled vs actual: `scheduled_*` = what the user told us he scheduled; `actual_post_time_verified` only from the platform's own post time, else `unavailable`. Never copy the schedule into the actual column.
