import sys, os; sys.path.insert(0, next(str(p / "s1e1") for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "s1e1" / "paths.py").is_file())); from paths import ROOT, DELIVERY
"""Captions page per post: every title / description / caption / pinned comment in its own box with a one-tap «نسخ» button.
Reads publish/schedule.json (run build.py first). Writes publish/captions/<id>.html (self-contained, works offline on the phone).

Usage: python publish/captions_html.py <id> [<id> ...]      e.g. nanaa_s2_e05
"""
import json, html

PUB = ROOT + "/publish"
os.makedirs(PUB + "/captions", exist_ok=True)
M = json.load(open(PUB + "/schedule.json", encoding="utf-8"))

CSS = """
:root{--bg:#f6f2ea;--card:#fff;--ink:#1d1a16;--muted:#6d655b;--line:#e4dccf;--acc:#c8322d;--gold:#e0a82e;--ok:#2f8f46}
@media (prefers-color-scheme:dark){:root{--bg:#141210;--card:#1f1c19;--ink:#f1ece4;--muted:#a59c90;--line:#34302b;--acc:#e5534b;--gold:#f0c050;--ok:#5cc274}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 system-ui,-apple-system,"Segoe UI",Tahoma,sans-serif}
.wrap{max-width:820px;margin:0 auto;padding:16px}
header{padding:18px 4px 6px}h1{margin:0;font-size:24px}header p{margin:4px 0 0;color:var(--muted);font-size:14px}
.plat{background:var(--card);border:1px solid var(--line);border-radius:16px;margin:16px 0;padding:6px 14px 14px}
.plat h2{font-size:18px;margin:10px 0 4px;display:flex;align-items:center;gap:8px}
.dot{width:12px;height:12px;border-radius:50%}
.field{margin-top:12px}.label{display:flex;justify-content:space-between;align-items:center;font-weight:600;font-size:14px;color:var(--muted);margin-bottom:6px}
pre{margin:0;white-space:pre-wrap;word-break:break-word;background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:12px;font:15px/1.7 system-ui,Tahoma,sans-serif;direction:rtl;text-align:right;user-select:all}
button{font:inherit;font-size:14px;font-weight:700;border:0;border-radius:999px;padding:8px 18px;background:var(--acc);color:#fff;cursor:pointer;min-width:84px}
button.done{background:var(--ok)}
.files{font-size:14px;color:var(--muted)}
"""
JS = """
function copyText(id, btn){
  const t = document.getElementById(id).innerText;
  const ok = () => { btn.textContent = 'اتنسخ ✓'; btn.classList.add('done'); setTimeout(()=>{btn.textContent='نسخ'; btn.classList.remove('done')}, 1600); };
  if (navigator.clipboard && window.isSecureContext) { navigator.clipboard.writeText(t).then(ok, () => fallback(t, ok)); }
  else fallback(t, ok);
}
function fallback(t, ok){
  const ta = document.createElement('textarea'); ta.value = t; ta.style.position='fixed'; ta.style.opacity='0';
  document.body.appendChild(ta); ta.focus(); ta.select(); try { document.execCommand('copy'); ok(); } catch(e) {} ta.remove();
}
"""
PLAT = [("youtube", "يوتيوب (الحلقة العرض)", "#ff0033", [("title", "العنوان"), ("description", "الوصف"), ("tags", "التاجز"), ("pinned_comment", "الكومنت المثبت")]),
        ("youtube_shorts", "يوتيوب شورتس", "#ff0033", [("title", "العنوان"), ("description", "الوصف"), ("pinned_comment", "الكومنت المثبت")]),
        ("tiktok", "تيك توك", "#25f4ee", [("caption", "الكابشن"), ("pinned_comment", "الكومنت المثبت")]),
        ("instagram_reel", "ريلز انستجرام", "#e1306c", [("caption", "الكابشن"), ("pinned_comment", "الكومنت المثبت")]),
        ("facebook_reel", "ريلز فيسبوك", "#1877f2", [("caption", "الكابشن"), ("pinned_comment", "الكومنت المثبت")])]

def page(post):
    n = [0]
    def box(label, value):
        n[0] += 1; i = f"f{n[0]}"
        if isinstance(value, list): value = ", ".join(value)
        return (f'<div class="field"><div class="label"><span>{html.escape(label)}</span>'
                f'<button onclick="copyText(\'{i}\', this)">نسخ</button></div><pre id="{i}">{html.escape(value)}</pre></div>')
    out = [f'<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<title>كابشن {html.escape(post["episode_name"] or post["id"])}</title><style>{CSS}</style></head><body><div class="wrap">',
           f'<header><h1>{html.escape(post["series_name"])} — {html.escape(post["episode_name"] or "")}</h1>'
           f'<p>ميعاد النشر: {html.escape(post["publish_at_cairo"][:16].replace("T", " "))} بتوقيت القاهرة</p></header>']
    for key, name, col, fields in PLAT:
        p = post["platforms"].get(key)
        if not p: continue
        out.append(f'<section class="plat"><h2><span class="dot" style="background:{col}"></span>{name}</h2>')
        for f, lab in fields:
            if p.get(f): out.append(box(lab, p[f]))
        out.append("</section>")
    out.append(f"</div><script>{JS}</script></body></html>")
    return "".join(out)

if __name__ == "__main__":
    ids = sys.argv[1:]
    for post in M["posts"]:
        if post["id"] in ids:
            f = f"{PUB}/captions/{post['id']}.html"
            open(f, "w", encoding="utf-8").write(page(post)); print("✔", f)
