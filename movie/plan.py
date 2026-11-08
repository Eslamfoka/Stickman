# keep = full range minus cuts (seconds)
CUTS = {
 1: [(9.1, 12.1), (60.8, 68.1), (80.8, 84.0)],
 2: [(0.0, 8.4), (19.0, 21.6), (54.3, 61.0), (90.5, 93.71)],
 3: [(6.4, 13.9), (74.1, 79.4), (89.1, 92.5)],
 4: [(0.0, 1.9), (10.4, 19.8), (59.0, 65.4), (82.5, 85.71)],
 5: [(11.6, 19.2), (52.3, 57.5), (81.9, 85.1)],
 6: [(7.3, 16.3), (60.6, 68.1), (84.8, 88.0)],
 7: [(0.0, 1.8), (8.8, 16.1), (59.8, 65.7), (77.6, 80.75)],
 8: [(3.0, 9.7), (48.9, 53.7), (72.4, 75.6)],
 9: [(6.6, 14.9), (92.0, 98.2), (110.6, 113.96)],
 10: [(5.5, 13.1), (131.2, 137.6)],
}
import json, subprocess
DUR = {n: float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f"/home/claude/s1e{n}/sirr_eldor_elsabe3_ep{n}.mp4"],capture_output=True,text=True).stdout) for n in CUTS}
segs = []
for n, cuts in CUTS.items():
    # snap cut points to shot boundaries from json
    d = json.load(open(f"/home/claude/movie/ep{n}.json"))
    t = 0.0
    for a, b in sorted(cuts):
        if a - t > 0.05: segs.append((n, t, a))
        t = b
    if DUR[n] - t > 0.05: segs.append((n, t, DUR[n]))
json.dump(segs, open("/home/claude/movie/segs.json", "w"))
tot = sum(b - a for _, a, b in segs)
print(len(segs), "segments, total", round(tot, 1), "s =", round(tot/60, 2), "min")
