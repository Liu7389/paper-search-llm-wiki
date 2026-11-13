"""Lint: wiki 來源標記、slide↔wiki↔source 對應、數字可追溯、孤兒頁。exit 1 if errors."""
import re, sys, html
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import ROOT, sources, pages
E, W = [], []
S, P = sources(), pages()
for pid, p in P.items():
    if pid in ("index", "log"): continue
    used = set()
    for n, line in enumerate(p["body"].splitlines(), 1):
        t = line.strip()
        if t.startswith("|"): used |= set(re.findall(r"\[(S\d+)\]", t)); continue
        if not t or t.startswith("#"): continue
        cites = set(re.findall(r"\[(S\d+)\]", t)); used |= cites
        if not cites and "整理" not in t and not t.startswith("見 ") and not t.endswith("："):
            E.append(f"{p['file']}:{n} 事實句沒有來源標記：{t[:40]}")
        for c in cites:
            if c not in S: E.append(f"{p['file']}:{n} 來源 {c} 不在 sources.json")
            if c not in p["meta"]["sources"]: E.append(f"{p['file']}:{n} {c} 未列在 frontmatter sources")
        if pid.startswith("demo") and re.search(r"\*[^*]+\*", t) and "http" not in t:
            E.append(f"{p['file']}:{n} 論文沒有網址：{t[:40]}")
        if "待查證" in t or "待執行" in t: W.append(f"{p['file']}:{n} 尚有待辦：{t[:40]}")
    for c in set(p["meta"]["sources"]) - used: W.append(f"{p['file']} frontmatter 列了 {c} 但內文沒用到")
idx = P["index"]["body"]
for pid in P:
    if pid not in ("index", "log") and f"({pid}.md)" not in idx: E.append(f"孤兒頁：{pid} 不在 index.md")
deck = (ROOT/"slides/index.html").read_text(encoding="utf-8")
secs = re.findall(r'<section[^>]*data-wiki="([\w-]+)" data-src="([^"]+)"[^>]*>(.*?)</section>', deck, re.S)
allbody = "".join(p["body"] for p in P.values())
for k, (wid, src, body) in enumerate(secs, 1):
    if wid not in P: E.append(f"投影片 {k}: data-wiki={wid} 不存在"); continue
    for c in src.split():
        if c not in P[wid]["meta"]["sources"]: E.append(f"投影片 {k}: 來源 {c} 不屬於 wiki 頁 {wid}")
    text = html.unescape(re.sub(r"<[^>]+>", " ", body))
    for num in set(re.findall(r"\d[\d,.]*\d|\d", text)):
        if num not in allbody and num not in ("1","2","3","4","5","6","8","9","0"):
            E.append(f"投影片 {k}: 數字「{num}」在 Wiki 找不到")
# 第二輪加入：投影片上的「N 份原始資料」「N 頁」要等於實際數量
content_pages = len([p for p in P if p not in ("index", "log")])
for k, (wid, src, body) in enumerate(secs, 1):
    for n in re.findall(r"(\d+) 份原始資料", body):
        if int(n) != len(S): E.append(f"投影片 {k}: 寫 {n} 份原始資料，實際 {len(S)}")
    for n in re.findall(r"Wiki（(\d+) 頁）", body):
        if int(n) != content_pages: E.append(f"投影片 {k}: 寫 Wiki {n} 頁，實際 {content_pages}")
print(f"pages={len(P)} sources={len(S)} slides={len(secs)}")
print("\n".join(["ERROR " + e for e in E] + ["WARN  " + w for w in W]) or "all clear")
sys.exit(1 if E else 0)
