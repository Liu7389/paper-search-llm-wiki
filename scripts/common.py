import json, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
def sources():
    return {s["id"]: s for s in json.loads((ROOT/"raw/sources.json").read_text(encoding="utf-8"))}
def pages():
    out = {}
    for p in sorted((ROOT/"wiki").glob("*.md")):
        t = p.read_text(encoding="utf-8")
        m = re.match(r"---\n(.*?)\n---\n(.*)", t, re.S)
        meta = dict(l.split(": ", 1) for l in m.group(1).splitlines())
        meta["sources"] = re.findall(r"S\d+", meta["sources"])
        out[meta["id"]] = {"file": p.name, "meta": meta, "body": m.group(2)}
    return out
