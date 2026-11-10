"""Copy the delivered videos into publish/media/ with the names schedule.json expects.

Usage (on your PC):
    python publish/prepare_media.py "D:\\path\\to\\folder\\with\\videos" ["D:\\another\\folder" ...]

It searches the given folders (recursively) for each post's original file name
(schedule.json -> source_file_names) and copies it to publish/media/<id>_h.mp4 / <id>_v.mp4.
Anything it can't find is listed at the end so you can rename it by hand.
"""
import json, os, shutil, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
MEDIA = os.path.join(HERE, "media")
os.makedirs(MEDIA, exist_ok=True)

def norm(s):
    s = unicodedata.normalize("NFC", s).lower()
    return s.split(" (من على جهازك)")[0].strip()

def index(folders):
    idx = {}
    for f in folders:
        for root, _, files in os.walk(f):
            for n in files:
                if n.lower().endswith((".mp4", ".mov")):
                    idx.setdefault(norm(n), os.path.join(root, n))
    return idx

def main():
    folders = sys.argv[1:] or ["."]
    idx = index(folders)
    plan = json.load(open(os.path.join(HERE, "schedule.json"), encoding="utf-8"))
    missing = []
    for p in plan["posts"]:
        for key, dst in p["media"].items():
            src_name = p["source_file_names"].get(key)
            if not src_name:
                continue
            target = os.path.join(HERE, dst)
            if os.path.exists(target):
                continue
            src = idx.get(norm(src_name))
            if src:
                shutil.copy2(src, target); print("✔", dst, "<-", os.path.basename(src))
            else:
                missing.append((dst, src_name))
    if missing:
        print("\nمش لاقي الملفات دي — سمّيها بإيدك وحطها في publish/media:")
        for dst, name in missing:
            print(f"  {dst}   <=   {name}")

if __name__ == "__main__":
    main()
