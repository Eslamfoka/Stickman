import sys, os; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
"""TikTok/Reels/Shorts cut of a vertical episode (docs/directing.md "First frame rule"):
first 0.5 s = the episode cover (publish/thumbs/<id>_cover.jpg), and the title card is removed.

Usage:
    python publish/tiktok_cut.py <vertical.mp4> <cover.jpg> <title_start> <title_end> <out.mp4>
    python publish/tiktok_cut.py <vertical.mp4> <cover.jpg> <out.mp4> --cut 38.51-40.51 --cut 187.95-end [--speed 1.02]
title_start/end in seconds (get them with `python epN.py times` -> the "title" line).
--cut can repeat (any dead air / end card); --speed > 1 speeds up picture+sound (pitch kept) — use ≤ 1.03 so it stays invisible.
YouTube Shorts must be ≤ 3:00 → keep the result ≤ ~179.5 s.
"""
import subprocess

def probe_dur(src):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", src],
                                capture_output=True, text=True, check=True).stdout)

def run(src, cover, out, cuts, speed=1.0):
    end = probe_dur(src)
    cuts = sorted((a, end if b is None else b) for a, b in cuts)
    keep, t = [], 0.0
    for a, b in cuts:
        if a > t: keep.append((t, a))
        t = max(t, b)
    if t < end - 0.01: keep.append((t, end))
    args = ["ffmpeg", "-y", "-v", "error", "-loop", "1", "-t", "1", "-i", cover]
    fc = ["[0:v]scale=1080:1920,setsar=1,fps=24,format=yuv420p,trim=duration=0.5,setpts=PTS-STARTPTS[cv]",
          "anullsrc=r=44100:cl=mono,atrim=duration=0.5,asetpts=PTS-STARTPTS[ca]"]
    pads = "[cv][ca]"
    for i, (a, b) in enumerate(keep, 1):          # separate inputs (input seeking) → no frame buffering / no OOM
        args += ["-ss", f"{a:.3f}", "-t", f"{b - a:.3f}", "-i", src]
        fc.append(f"[{i}:v]setpts=PTS-STARTPTS[v{i}]")
        fc.append(f"[{i}:a]asetpts=PTS-STARTPTS,aformat=channel_layouts=mono:sample_rates=44100[a{i}]")
        pads += f"[v{i}][a{i}]"
    fc.append(f"{pads}concat=n={len(keep) + 1}:v=1:a=1[vc][ac]")
    if abs(speed - 1) > 1e-3:
        fc.append(f"[vc]setpts=PTS/{speed},fps=24[v]"); fc.append(f"[ac]atempo={speed}[a]")
    else:
        fc.append("[vc]null[v]"); fc.append("[ac]anull[a]")
    args += ["-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-tune", "animation",
             "-crf", "23", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out]
    subprocess.run(args, check=True)
    print("✔", out, round(probe_dur(out), 2), "s")

def main():
    a = sys.argv[1:]
    if len(a) == 5 and "--cut" not in a:                       # old form: src cover ts te out
        return run(a[0], a[1], a[4], [(float(a[2]), float(a[3]))])
    src, cover, out = a[0], a[1], a[2]
    cuts, speed, i = [], 1.0, 3
    while i < len(a):
        if a[i] == "--cut":
            x, y = a[i + 1].split("-"); cuts.append((float(x), None if y == "end" else float(y))); i += 2
        elif a[i] == "--speed":
            speed = float(a[i + 1]); i += 2
        else:
            raise SystemExit(f"unknown arg {a[i]}")
    run(src, cover, out, cuts, speed)

if __name__ == "__main__":
    main()
