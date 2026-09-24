"""Assemble the round-4 target (v8) from v9_target.md + anchored v7; shared by build and word counts."""
import re
from pathlib import Path
HERE = Path(__file__).resolve().parent
def v7_blocks():
    t = (HERE / "manuscript_v8.md").read_text()
    p = re.split(r"<!--block:(B\d{4})-->\n", t)
    return [(p[i], p[i + 1].rstrip("\n")) for i in range(1, len(p), 2)]
def target_seq():
    """list of (id or 'NEW', text, kept_verbatim)"""
    v7 = v7_blocks(); d = dict(v7); order = [b for b, _ in v7]
    t = (HERE / "v9_target.md").read_text()
    seq = []
    for m in re.finditer(r"<!--(keep|keeprest|block):(B\d{4}|NEW)-->\n?(.*?)(?=<!--(?:keep|keeprest|block):|\Z)", t, re.S):
        kind, bid, body = m.group(1), m.group(2), m.group(3).rstrip("\n")
        if kind == "keep":
            seq.append((bid, d[bid], True))
        elif kind == "keeprest":
            for b in order[order.index(bid):]:
                seq.append((b, d[b], True))
        else:
            seq.append((bid, body, bid != "NEW" and body == d.get(bid)))
    return seq
def clean_text(seq):
    return "\n\n".join(x for _, x, _ in seq) + "\n"
if __name__ == "__main__":
    seq = target_seq()
    ids = [b for b, _, _ in seq if b != "NEW"]
    assert len(ids) == len(set(ids)), "duplicate ids"
    txt = clean_text(seq)
    (HERE / "v9_preview.clean.md").write_text(txt)
    def wc(s):
        body = s.split("## References")[0]
        body = re.sub(r"\$\$.*?\$\$", " EQ ", body, flags=re.S)
        lines = body.splitlines()
        pr = [l for l in lines if not l.startswith("|")]; tb = [l for l in lines if l.startswith("|")]
        w = lambda ls: len(re.findall(r"\S+", " ".join(ls)))
        return w(lines), w(pr), w(tb)
    v7 = (HERE.parent / "correction_round4" / "manuscript_v8.clean.md").read_text()
    a, b = wc(v7), wc(txt)
    print("v8 total/prose/tables", a); print("v9 total/prose/tables", b)
    print("reduction %", [round(100 * (1 - y / x), 1) for x, y in zip(a, b)])
    ab = re.search(r"## Abstract\n\n(.*?)\n\n", txt, re.S).group(1); print("abstract words", len(ab.split()))
    dropped = [b for b, _ in v7_blocks() if b not in ids]; print("dropped", dropped)
