import sys, json, os
sys.path.insert(0, "/home/claude/s1e1")
f = sys.argv[1]
src = open(f).read().split('if __name__')[0]
g = {"__name__": "dump", "__file__": f}
exec(compile(src, f, "exec"), g)
out = dict(total=g["TOTAL"],
           shots=[dict(start=s["start"], end=s["end"], set=s.get("set", s.get("name"))) for s in g["shots"]],
           lines=[dict(start=st, key=k, dur=g["DUR"][k] if "DUR" in g else None, text=g["SUB"][k]) for st, k in g["lines"]])
json.dump(out, open(sys.argv[2], "w"), ensure_ascii=False, indent=0)
print(f, round(g["TOTAL"], 1), len(out["shots"]), len(out["lines"]))
