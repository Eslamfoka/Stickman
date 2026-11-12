import sys, os; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
"""Safeeh's voice = Roshdy's clone + robot filter B (user pick 2026-11-12):
robotize (afftfilt, win 1024) mixed with 25% dry, short metallic echoes 7/14 ms, light flanger, band 250–4500 Hz.
Usage: python s2/robot_fx.py <in.mp3> <out.mp3>"""
import subprocess

FC = ("[0:a]asplit=2[d][w];"
      "[w]afftfilt=real='hypot(re,im)':imag='0':win_size=1024:overlap=0.75,volume=0.75[wr];"
      "[d]volume=0.25[dr];[wr][dr]amix=inputs=2:normalize=0,"
      "aecho=0.8:0.6:7|14:0.35|0.25,flanger=delay=2:depth=2:speed=0.6,"
      "highpass=f=250,lowpass=f=4500,loudnorm=I=-16:TP=-1.5[out]")

def robot(src, out):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src, "-filter_complex", FC, "-map", "[out]", "-ar", "44100", "-b:a", "192k", out], check=True)

if __name__ == "__main__":
    robot(sys.argv[1], sys.argv[2])
