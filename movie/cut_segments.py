# Builds seg/sNN.mp4 = the kept parts of each episode (titles, endcards, recap & puzzle-to-camera bits removed)
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
import json, subprocess, os
os.chdir(ROOT + "/movie"); os.makedirs("seg", exist_ok=True)
exec(open("plan.py", encoding="utf-8").read().split("import json, subprocess")[0])   # CUTS dict
out = []
for n, cuts in CUTS.items():
    d = json.load(open(f"ep{n}.json", encoding="utf-8")); bounds = sorted(set([s['start'] for s in d['shots']] + [s['end'] for s in d['shots']]))
    dur = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f"{ROOT}/s1e{n}/sirr_eldor_elsabe3_ep{n}.mp4"],capture_output=True,text=True).stdout)
    snap = lambda v: (lambda c: c if abs(c - v) < 0.2 else v)(min(bounds, key=lambda b: abs(b - v)))
    t = 0.0
    for a, b in sorted(cuts):
        a2, b2 = snap(a), min(snap(b), dur)
        if a2 > 0.05 and a2 - t > 0.05: out.append((n, t, a2))
        t = b2
    if dur - t > 0.05: out.append((n, t, dur))
json.dump(out, open("segs.json", "w", encoding="utf-8"))
for i, (n, a, b) in enumerate(out):
    d = b - a
    subprocess.run(["ffmpeg","-v","error","-y","-ss",f"{a}","-t",f"{d}","-i",f"{ROOT}/s1e{n}/sirr_eldor_elsabe3_ep{n}.mp4",
                    "-af",f"afade=t=in:d=0.03,afade=t=out:st={max(0,d-0.04)}:d=0.04","-c:v","libx264","-preset","veryfast","-crf","18",
                    "-pix_fmt","yuv420p","-r","24","-c:a","aac","-b:a","192k","-ar","44100","-ac","2",f"seg/s{i:02d}.mp4"], check=True)
print(len(out), "segments")
