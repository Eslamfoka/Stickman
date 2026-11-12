"""Locations canon (docs/locations.md): one background per place; only the light changes between episodes.

    from locations import loc
    img = loc("lobby", "night")      # PIL RGB 1920x1080
tod: "day" | "night" | "dusk" | "dark" (lights off) | "sepia" (flashback colour is applied later in the frame pipeline, here = day)
"""
import paths  # noqa: F401
from PIL import Image, ImageEnhance, ImageChops

R = paths.ROOT
LOC = {
    "lobby":     {"day": "/s1e10/bg/morning.png"},
    "stairs":    {"day": "/s1e1/bg/stairs_1080.png"},
    "living":    {"day": "/s1e1/bg/living_1080.png"},
    "bedroom":   {"day": "/s2e2/bg_bedroom.png"},
    "door7":     {"day": "/s1e2/bg/door7.png"},
    "fahmy_apt": {"day": "/s1e5/bg/fahmy_raw.png"},
    "roof":      {"day": "/s2e6/bg/roof_day.png", "night": "/s1e6/bg/roof_raw.png"},
    "apt7":      {"day": "/s1e8/bg/apt7_raw.png"},
    "basement":  {"day": "/s2/bg/basement_day.png"},
    "tunnel":    {"day": "/s2e8/bg/tunnel.png"},
    "corridor":  {"day": "/s2e4/bg/corridor.png"},
    "studio":    {"day": "/s2e5/bg/studio_nosheet.png"},
    "street":    {"day": "/s2e3/bg/street_day.png", "night": "/s2/bg/street_car.png"},
    "wall":      {"day": "/s2e5/bg/wall.png"},
    "car":       {"day": "/s2e6/bg/carday.png", "night": "/s2e4/bg/carin.png"},
}
GRADE = {"night": (0.62, (135, 152, 222)), "dusk": (0.85, (255, 200, 160)), "dark": (0.35, (150, 160, 200))}

def _ld(p): return Image.open(R + p).convert("RGB").resize((1920, 1080), Image.LANCZOS)

def loc(name, tod="day"):
    files = LOC[name]
    if tod in files: return _ld(files[tod])
    base = _ld(files["day"])
    if tod in ("day", "sepia"): return base
    lvl, tint = GRADE[tod]
    return ImageChops.multiply(ImageEnhance.Brightness(base).enhance(lvl), Image.new("RGB", base.size, tint))
