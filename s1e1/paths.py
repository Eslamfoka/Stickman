"""Repo-relative paths + Windows setup. Import this BEFORE PIL.

Every script finds the repo root by walking up to the folder that holds s1e1/paths.py,
so the project runs from any location (Linux cloud session or Windows PC) without symlinks.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/")
DELIVERY = os.environ.get("NANAA_DELIVERY", ROOT + "/delivery").replace("\\", "/")

if os.name == "nt":
    # Pillow on Windows needs FriBiDi (tools/win/libfribidi-0.dll) for Arabic text shaping (raqm).
    # It is loaded when PIL.ImageFont is first imported, so PATH must be set before that.
    _dll = ROOT + "/tools/win"
    if _dll not in os.environ.get("PATH", ""):
        os.environ["PATH"] = _dll + os.pathsep + os.environ.get("PATH", "")
