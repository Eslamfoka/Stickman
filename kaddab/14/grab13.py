# grabs clean case-13 frames (no subtitles/tags) for the «حل القضية ١٣» segment of case 14
import sys; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
__name__ = "grab"
exec(open(ROOT + "/kaddab/13/ep.py", encoding="utf-8").read())
out = ROOT + "/kaddab/14/c13/"
for nm, tt in (("roof", 24.6), ("lob", 17.2), ("sesame", 26.4), ("seeds", 34.9)):
    sh = shot_at(tt)
    for tag_, (Wd, Hd) in (("h", (1920, 1080)), ("v", (1080, 1920))):
        if sh["set"] == "cu": fr = cu_box(tt, sh, Wd, Hd)
        else:
            cam = hcam(sh, tt) if tag_ == "h" else vcam(sh, tt); fr = scene(tt, sh, cam, (Wd, Hd))
        fr.save(out + f"{nm}_{tag_}.png"); print(nm, tag_, sh["set"])
