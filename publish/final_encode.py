import sys, os; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
"""Final delivery encode: same look, ~3x smaller files (docs/status.md "PLAN — smaller files").
Flat cartoon + grain compresses much better with preset medium + tune animation (veryfast is only for the raw part renders).
Tested on s2e3: 32 MB -> 9.5 MB for 15 s, no visible difference (only the film grain gets a touch softer).

Usage: python publish/final_encode.py <in.mp4> <out.mp4> [crf=23]
"""
import subprocess
VOPTS = ["-c:v", "libx264", "-preset", "medium", "-tune", "animation", "-pix_fmt", "yuv420p", "-movflags", "+faststart"]

def encode(src, out, crf=23):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src, *VOPTS, "-crf", str(crf), "-c:a", "copy", out], check=True)
    print("✔", out, round(os.path.getsize(out) / 1e6, 1), "MB")

if __name__ == "__main__":
    encode(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 23)
