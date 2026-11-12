# Render ONLY the horizontal (YouTube) picture of a Season-2 episode, for the season movie.
# Usage: python render_h.py <ep> <part_i> <parts>   -> s2eN/mh_<i>.mp4   (no audio; mux mix.wav afterwards)
#        python render_h.py <ep> audio              -> s2eN/mix.wav
# The vertical stream is stubbed (black, tiny cost) so we don't pay for a picture the movie doesn't use.
import sys, os, runpy
sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file()))
from paths import ROOT, DELIVERY
ep = int(sys.argv[1]); d = f"{ROOT}/s2e{ep}"; os.chdir(d); sys.path.insert(0, d)
g = runpy.run_path(f"{d}/ep{ep}.py", run_name="movie_h")
if sys.argv[2] == "audio":
    g["build_audio"](); sys.exit()
from PIL import Image
_black = Image.new("RGB", (1080, 1920))
g["vertical"] = lambda *a, **k: _black
render = g["render"]; render.__globals__["vertical"] = g["vertical"]
i, n = int(sys.argv[2]), int(sys.argv[3]); T, FPS = g["TOTAL"], g["FPS"]
a = round(T * i / n * FPS) / FPS; b = round(T * (i + 1) / n * FPS) / FPS
render(f"mh_{i}.mp4", f"_vstub_{i}.mp4", None, a, b)
os.remove(f"_vstub_{i}.mp4")
