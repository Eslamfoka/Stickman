# Crops the user's profile screenshots (raw/*.png) for the follow CTA:
# hides follower counts / video counts, drops the video grid and status bar.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "s1e1")); from paths import ROOT, DELIVERY
from PIL import Image, ImageDraw
D = ROOT + "/brand/follow/"
# name: (top, bottom, [rows to cut out], [white boxes])  — original 576x1280 coords
spec = {
    "yt": (48, 565, [], [(150, 355, 330, 395)]),          # "6 videos"
    "fb": (48, 815, [(498, 538)], []),                     # followers/posts line
    "ig": (48, 465, [], [(195, 170, 576, 295)]),           # posts/followers/following
    "tt": (48, 400, [], [(0, 225, 345, 302)]),             # following/followers/likes (avatar overlaps these rows, so blank instead of cut)
}
for n, (top, bot, cuts, hides) in spec.items():
    im = Image.open(D + "raw/%s.png" % n).convert("RGB")
    d = ImageDraw.Draw(im)
    for h in hides:
        d.rectangle(h, fill=(255, 255, 255))
    keep, y = [], top
    for a, b in cuts + [(bot, bot)]:
        keep.append(im.crop((0, y, im.width, a))); y = b
    out = Image.new("RGB", (im.width, sum(k.height for k in keep)), "white")
    yy = 0
    for k in keep:
        out.paste(k, (0, yy)); yy += k.height
    out.save(D + "%s.png" % n)
    print(n, out.size)
