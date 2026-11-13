"""wiki/*.md + raw/sources.json -> wiki-site/*.html"""
import html, re, sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import ROOT, sources, pages

CSS = """:root{--bg:#f6f4ef;--card:#fffdf8;--ink:#1f2328;--mute:#5d6470;--line:#d9d4c7;--acc:#1f6f5c;--chip:#e8efe9}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#15181b;--card:#1d2125;--ink:#e8e6e1;--mute:#a3a9b1;--line:#343a40;--acc:#5fc2a5;--chip:#24312c}}
:root[data-theme="dark"]{--bg:#15181b;--card:#1d2125;--ink:#e8e6e1;--mute:#a3a9b1;--line:#343a40;--acc:#5fc2a5;--chip:#24312c}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"Noto Sans TC","PingFang TC","Microsoft JhengHei",system-ui,sans-serif;line-height:1.7}
main{max-width:860px;margin:0 auto;padding:24px 16px 60px}a{color:var(--acc)}code{background:var(--chip);padding:1px 5px;border-radius:4px;word-break:break-word}
table{border-collapse:collapse;width:100%}td,th{border:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}
nav{font-size:14px;color:var(--mute);border-bottom:1px solid var(--line);padding-bottom:8px;margin-bottom:16px}.cite{font-size:12px;color:var(--mute)}"""

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", s)
    s = re.sub(r"\[([^\]]+)\]\(([\w-]+)\.md\)", r'<a href="\2.html">\1</a>', s)
    s = re.sub(r"(?<![\"=])(https?://[^\s（）\[\]<]+)", r'<a href="\1">\1</a>', s)
    s = re.sub(r"\[(S\d+)\]", r'<a class="cite" href="sources.html#\1">[\1]</a>', s)
    return s

def md(body):
    out, lst = [], None
    def close():
        nonlocal lst
        if lst: out.append(f"</{lst}>"); lst = None
    rows = []
    for line in body.splitlines():
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if not set("".join(cells)) <= set("-: "): rows.append(cells)
            continue
        if rows:
            out.append("<table>" + "".join("<tr>" + "".join(f"<{'th' if i==0 else 'td'}>{inline(c)}</{'th' if i==0 else 'td'}>" for c in r) + "</tr>" for i, r in enumerate(rows)) + "</table>"); rows = []
        if m := re.match(r"(#+) (.*)", line):
            close(); n = len(m.group(1)); out.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
        elif m := re.match(r"\s*- (.*)", line):
            if lst != "ul": close(); out.append("<ul>"); lst = "ul"
            out.append(f"<li>{inline(m.group(1))}</li>")
        elif m := re.match(r"\d+\. (.*)", line):
            if lst != "ol": close(); out.append("<ol>"); lst = "ol"
            out.append(f"<li>{inline(m.group(1))}</li>")
        elif line.strip():
            close(); out.append(f"<p>{inline(line)}</p>")
        else:
            close()
    close()
    return "\n".join(out)

def page(title, content):
    return f"""<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><style>{CSS}</style></head>
<body><main><nav><a href="index.html">Wiki 索引</a> · <a href="sources.html">原始資料</a> · <a href="log.html">紀錄</a> · <a href="../slides/index.html">教學簡報</a> · <a href="../docs/loop.html">流程設計</a></nav>{content}</main></body></html>"""

def main():
    out = ROOT/"wiki-site"; out.mkdir(exist_ok=True)
    P, S = pages(), sources()
    for pid, p in P.items():
        (out/f"{pid}.html").write_text(page(p["meta"]["title"], md(p["body"])), encoding="utf-8")
    rows = "".join(f'<tr id="{s["id"]}"><td>{s["id"]}</td><td><a href="{html.escape(s["url"])}">{html.escape(s["title"])}</a><br><span class="cite">{html.escape(s["author"])}｜存取 {s["accessed"]}｜{s["type"]}</span></td><td>{html.escape(s["used_for"])}</td><td>{html.escape(s["caveat"])}</td></tr>' for s in S.values())
    (out/"sources.html").write_text(page("原始資料", f"<h1>原始資料（raw，共 {len(S)} 份）</h1><table><tr><th>ID</th><th>資料</th><th>用在哪</th><th>限制</th></tr>{rows}</table>"), encoding="utf-8")
    (ROOT/"docs/run-log.html").write_text(page("執行紀錄", md((ROOT/"docs/run-log.md").read_text(encoding="utf-8"))).replace('href="index.html"','href="../wiki-site/index.html"').replace('href="sources.html"','href="../wiki-site/sources.html"').replace('href="log.html"','href="../wiki-site/log.html"').replace('href="../docs/loop.html"','href="loop.html"').replace('href="../slides/','href="../slides/'), encoding="utf-8")
    (ROOT/"index.html").write_text(page("論文搜尋 Wiki", f"""<h1>論文搜尋 LLM Wiki</h1><p>主題：怎麼找指定領域的論文（示範：交通工程、人工智慧）。原始資料 {len(S)} 份 → Wiki {len(P)-2} 頁 → 教學簡報。</p>
<ul><li><a href="slides/index.html"><b>教學 HTML 簡報</b></a></li><li><a href="wiki-site/index.html">LLM Wiki</a>（<a href="wiki-site/sources.html">原始資料</a>）</li><li><a href="docs/loop.html">Loop / Graph 設計</a></li><li><a href="docs/run-log.html">實際執行與檢查紀錄</a></li></ul>""").replace('href="index.html">Wiki 索引','href="wiki-site/index.html">Wiki 索引').replace('href="sources.html"','href="wiki-site/sources.html"').replace('href="log.html"','href="wiki-site/log.html"').replace('href="../slides/','href="slides/').replace('href="../docs/','href="docs/'), encoding="utf-8")
    print(f"built {len(P)} pages + sources ({len(S)})")

if __name__ == "__main__": main()
