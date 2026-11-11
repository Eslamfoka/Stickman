import sys, os; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
"""TikTok/Reels cut of a vertical episode (docs/directing.md "First frame rule"):
first 0.5 s = the episode cover (publish/thumbs/<id>_cover.jpg), and the title card is removed.

Usage:
    python publish/tiktok_cut.py <vertical.mp4> <cover.jpg> <title_start> <title_end> <out.mp4>
title_start/end in seconds (get them with `python epN.py times` -> the "title" line).
"""
import subprocess

def main():
    src, cover, ts, te, out = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
    fc = (
        "[0:v]scale=1080:1920,setsar=1,fps=24,format=yuv420p,trim=duration=0.5,setpts=PTS-STARTPTS[cv];"
        "anullsrc=r=44100:cl=mono,atrim=duration=0.5,asetpts=PTS-STARTPTS[ca];"
        f"[1:v]trim=0:{ts},setpts=PTS-STARTPTS[v1];[1:a]atrim=0:{ts},asetpts=PTS-STARTPTS[a1];"
        f"[1:v]trim=start={te},setpts=PTS-STARTPTS[v2];[1:a]atrim=start={te},asetpts=PTS-STARTPTS[a2];"
        "[a1]aformat=channel_layouts=mono:sample_rates=44100[a1m];[a2]aformat=channel_layouts=mono:sample_rates=44100[a2m];"
        "[v1][a1m][v2][a2m]concat=n=2:v=1:a=1[vb][ab];"
        "[cv][ca][vb][ab]concat=n=2:v=1:a=1[v][a]"
    )
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-loop", "1", "-t", "1", "-i", cover, "-i", src,
                    "-filter_complex", fc, "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "veryfast",
                    "-crf", "23", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out],
                   check=True)
    print("✔", out)

if __name__ == "__main__":
    main()
