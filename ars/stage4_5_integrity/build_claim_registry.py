"""E1 claim registry (claim-registry/1.0) for an exact clean draft: every body sentence carrying a number, citation, trend or causal verb."""
import hashlib, json, re, sys
p, out = sys.argv[1], sys.argv[2]
raw = open(p, 'rb').read(); t = raw.decode()
body_end = t.index('## References'); claims = []; sec = None; pos = 0
causal = re.compile(r"\b(caus|drove|drive|led to|leads to|because|explain|reflect|due to|raised|brought)", re.I)
trend = re.compile(r"\b(rose|fell|rise|fall|declin|increas|decreas|grew|widen|narrow|surge)", re.I)
for line in t[:body_end].split('\n'):
    start = pos; pos += len(line.encode()) + 1
    if line.startswith('#'): sec = line.strip('# ').strip(); continue
    if not line.strip() or line.startswith('|') or line.startswith('!['): continue
    off = 0
    for s in re.split(r'(?<!et al)(?<!e\.g)(?<=[.!?])\s+(?=[A-Z*(])', line):
        i = line.index(s, off); off = i + len(s); st = s.strip()
        if len(st) < 3: continue
        lead = len(s) - len(s.lstrip()); bs = start + len(line[:i + lead].encode()); be = bs + len(st.encode())
        assert raw[bs:be].decode() == st
        kinds = [k for k, c in [('quantitative', re.search(r'\d', st)), ('causal', causal.search(st)), ('trend', trend.search(st))] if c]
        refs = sorted(set(f"{a}_{y}" for a, y in re.findall(r"([A-Z][\w'ń\-]+(?: [A-Z][\w\-]+)?)(?: et al\.)?(?:,| and [A-Z][\w\-]+,?| & [A-Z][\w\-]+,)? \(?((?:19|20)\d\d[ab]?|n\.d\.)[\),;]", st) if not re.match(r'(January|April|August|October|September|December|November|March|June|Dec|Nov|Apr|Oct|Named|Added|Dropping|Beyond|The Amihud|The Corwin)', a)))
        if not kinds and not refs: continue
        kinds = kinds or ['other_factual']
        hib = (['numerical'] if 'quantitative' in kinds else []) + (['causal'] if 'causal' in kinds else []) + (['headline_conclusion'] if sec in ('Abstract', '1. Introduction', '6. Discussion and conclusion') else []) + (['methods_critical'] if sec and sec.startswith('3') else [])
        c = dict(claim_id=f"C{len(claims)+1:03d}", claim_text=st, draft_span=dict(start_byte=bs, end_byte=be), claim_kinds=kinds, ref_slugs=refs, writer_anchors=[], paper_section=sec, selection_tier='ALL')
        if hib: c['high_impact_basis'] = hib
        claims.append(c)
json.dump(dict(schema_version='claim-registry/1.0', draft_raw_sha256=hashlib.sha256(raw).hexdigest(), claims=claims), open(out, 'w'), indent=1, ensure_ascii=False)
print(len(claims))
