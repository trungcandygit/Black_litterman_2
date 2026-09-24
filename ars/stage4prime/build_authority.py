"""Builds revision-roadmap/1.0 (round 2), empty claim-surface-manifest/1.0, author-adjudication input,
then patch 1.1 from round2_edits.json. Item-to-block mapping follows ars/stage3prime_review/99_verification_review_report.md."""
import hashlib, json, sys, subprocess
from pathlib import Path
ARS = Path("/Users/nguyenvantrung/academic-research-skills"); sys.path.insert(0, str(ARS))
from scripts._block_parser import parse_document, base_draft_hash
from scripts.revision_roadmap import author_decision_digest

D = Path("/Users/nguyenvantrung/Downloads/Python for Algorithmic Trading/NCKH/BAI FTSE2/FTSE2_new/ars/stage4prime")
A = D / "authority"; A.mkdir(exist_ok=True)
BASE = D / "manuscript_v3.anchored.md"; MANI = D / "manuscript_v3.anchored.md.block-manifest.json"
base_raw = BASE.read_bytes(); base = base_raw.decode(); blocks = parse_document(base).block_by_id()
def sha(b): return hashlib.sha256(b).hexdigest()
def raw(v): return (json.dumps(v, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()
def write(p, v): r = raw(v); p.write_bytes(r); return r
E = json.load(open(D / "round2_edits.json")); NEW, INS = E["new"], E["ins"]

# item: (id, seats[(seat, ordinal)], obligation, severity, description, section, cost_kind, consequence, anchor_quote, blocks)
ITEMS = [
 ("REV-R2-01", [("DA", 1), ("R1", 1)], "must_fix", "major", "RR1 residual: report the ITT event study and its joint pre-trend test, which rejects; put ITT beside constituent estimates in abstract and introduction; state the weaker ITT confirmation price response.", "Abstract; 1; 4.1; 6", "re_analysis", "evidence_gap_remains", "This last result is why we report intention-to-treat effects beside the constituent effects",
  ["B0003", "B0007", "B0013", "B0068", "B0071", "B0084", "B0135"]),
 ("REV-R2-02", [("DA", 6), ("DA", 8)], "must_fix", "major", "DA NEW-1/NEW-3: the upper/lower-bound reading and the claim that disclosure-date reactions cannot come from selection are unjustified.", "3.4; 5.2; 6", "sentence", "claim_scope_unsupported", "We therefore read the constituent estimates as upper bounds",
  ["B0057", "B0132", "B0133", "B0139"]),
 ("REV-R2-03", [("DA", 7), ("R1", 7), ("EIC", 4), ("DA", 3)], "must_fix", "major", "DA NEW-2 / R1 NEW-R1-1 / EIC NEW-1 / RR4 residual: pre-specify identical event windows, report all, base claims symmetrically, give magnitudes as ranges across benchmarks.", "3.2; 4.2", "section", "claim_scope_unsupported", "Constituents earned abnormal returns in the week around the announcement",
  ["B0012", "B0044", "B0076", "B0079", "B0080", "B0081", "B0082", "B0083", "B0084", "B0085"]),
 ("REV-R2-04", [("R1", 2)], "should_fix", "major", "RR3/RR4 residual: CAR estimation windows and market-model betas contain earlier event windows.", "3.2; Table 4", "re_analysis", "method_reproducibility_unresolved", "dividing the portfolio CAR by the standard deviation",
  ["B0044", "B0079", "B0081", "B0082"]),
 ("REV-R2-05", [("R3", 1), ("DA", 4)], "should_fix", "minor", "RR5 residual: three effective-date statements lack the first-tranche qualifier; the claim that gains preceded index trading needs the tranche qualifier.", "1; 4.3; 6", "sentence", "claim_scope_unsupported", "prices did not move",
  ["B0007", "B0013", "B0094", "B0095", "B0102", "B0135"]),
 ("REV-R2-06", [("R2", 2), ("R2", 5)], "should_fix", "minor", "RR6 residual and R2 NEW-R2-1: BSR claim overstated (decline mostly after cut-off; UPCoM to HOSE in January 2025).", "3.1; 5.2; References", "section", "claim_scope_unsupported", "BSR",
  ["B0035", "B0122", "B0123", "B0128", "B0131", "B0185"]),
 ("REV-R2-07", [("R1", 5), ("R1", 9), ("R2", 6)], "should_fix", "minor", "SR2 / R1 NEW-R1-3 / R2 NEW-R2-2: inference on three-stock segments and the two-stock group.", "4.4; 5.2", "section", "method_reproducibility_unresolved", "Large (3 stocks)",
  ["B0098", "B0100", "B0101", "B0128", "B0131"]),
 ("REV-R2-08", [("R1", 6)], "should_fix", "minor", "SR3: test the step pattern against a post-announcement drift; soften H2 for the list stage.", "4.1", "re_analysis", "claim_scope_unsupported", "The steps are significant",
  ["B0060"]),
 ("REV-R2-09", [("R2", 3)], "should_fix", "minor", "SR4: explain how investability weights set index weights and passive demand.", "2.1", "sentence", "interpretive_ambiguity_remains", "investability weight (free float)",
  ["B0018"]),
 ("REV-R2-10", [("DA", 5)], "should_fix", "minor", "SR6: discuss sector composition and the pre-funding reform.", "5.1; 6", "re_analysis", "evidence_gap_remains", "Two-way clustering by stock and week",
  ["B0114", "B0115", "B0119", "B0141"]),
 ("REV-R2-11", [("R2", 4)], "should_fix", "minor", "SR7: record the missing A-share stock-level literature as a limitation in the manuscript.", "2.3", "sentence", "reporting_requirement_unmet", "Nguyen et al. (2021)",
  ["B0025"]),
 ("REV-R2-12", [("R1", 8)], "should_fix", "minor", "R1 NEW-R1-2: matched estimates and the matched benchmark ignore MatchIt weights.", "3.3; 4.1; 5.1; Appendix", "re_analysis", "method_reproducibility_unresolved", "Matched 3:1",
  ["B0050", "B0060", "B0062", "B0063", "B0114", "B0115", "B0116", "B0119", "B0145"]),
 ("REV-R2-13", [("R3", 3), ("R3", 4), ("R3", 5), ("DA", 9), ("DA", 10)], "consider", "minor", "R3 NEW-R3-1..5, DA NEW-4/5: policy and investor-type claims outrun single-event evidence; S 4.4 takeaway contradicts non-monotone ordering.", "Abstract; 4.3; 4.4; 6", "sentence", "claim_scope_unsupported", "Index funds traded the constituents heavily",
  ["B0003", "B0094", "B0095", "B0102", "B0136", "B0137", "B0138", "B0140"]),
 ("REV-R2-14", [("EIC", 5), ("EIC", 6), ("EIC", 7), ("EIC", 8)], "consider", "minor", "EIC NEW-2..5 and EIC-W2: table reference, eligibility-pricing claim, Table 9 note, labels.", "1; 4.2; 5.2; 6", "sentence", "reader_traceability_reduced", "Tables 5",
  ["B0013", "B0084", "B0131", "B0137"]),
 ("REV-R2-15", [("R1", 10)], "consider", "minor", "R1 NEW-R1-4: method-text wording (full-sample trend; two top-tercile pools).", "3.2; 3.3; 5.1", "sentence", "reader_traceability_reduced", "pre-period trend",
  ["B0044", "B0050", "B0118"]),
 ("REV-R2-16", [("EIC", 9)], "consider", "minor", "Venue compliance (Finance Research Open guide): appendix table numbering, AI declaration wording, web reference access dates.", "Appendix; Declarations; References", "section", "editorial_conformance_unmet", "Table A1",
  ["B0018", "B0035", "B0050", "B0143", "B0146", "B0155", "B0168", "B0169", "B0176", "B0177", "B0183", "B0184", "B0185", "B0186"]),
 ("REV-R2-17", [("R1", 11)], "consider", "minor", "R1 PLO-1: disclose the rebalancing-test design change in the manuscript.", "4.3", "sentence", "reader_traceability_reduced", "Panel A: stock and date fixed effects",
  ["B0093"]),
]
def ops_for(bid):
    o = []
    if bid in NEW: o.append("replace_block")
    if bid in INS: o.append("insert_after")
    assert o, bid
    return o
items = []
for iid, seats, ob, sev, desc, sect, ck, cons, quote, bl in ITEMS:
    SO={"EIC":0,"R1":1,"R2":2,"R3":3,"DA":4}
    seats=sorted(seats,key=lambda x:(SO[x[0]],x[1]))
    items.append({"id": iid, "source_refs": [{"seat": s, "channel": "finding", "ordinal": n, "subclaim_ordinal": 0} for s, n in seats],
        "description": desc, "reviewer": ",".join(sorted({s for s, _ in seats})), "obligation_class": ob, "severity": sev,
        "evidence_anchor": {"anchor_type": "text", "locator": f"manuscript_v3 {sect}", "quote": quote},
        "confidence": 4, "competence_basis": "Stage 3' routed seat within its declared competence (ars/stage3prime_review).",
        "cost_scope": {"kind": ck, "locator": sect}, "consequence_if_unaddressed": {"code": cons, "target": {"kind": "section", "locator": sect}},
        "target_section": sect, "suggested_action": desc, "consensus_level": "SINGLE-VERIFIER" if len({s for s, _ in seats}) == 1 else "CONSENSUS-3" if len({s for s, _ in seats}) >= 3 else "SPLIT",
        "verification_criteria": "Stage 4.5 verifies the change against ars/stage3prime_review/99_verification_review_report.md.",
        "proposed_targets": [{"block_id": b, "allowed_operations": ops_for(b)} for b in bl]})
SOK={"EIC":0,"R1":1,"R2":2,"R3":3,"DA":4}
items.sort(key=lambda i:((SOK[i["source_refs"][0]["seat"]],i["source_refs"][0]["ordinal"],0,0),i["id"]))
counts = {k: sum(1 for i in items if i["obligation_class"] == k) for k in ("must_fix", "should_fix", "consider")}
roadmap = {"schema_version": "revision-roadmap/1.0", "revision_round": 2, "base_draft_sha256": sha(base_raw), "block_manifest_sha256": sha(MANI.read_bytes()),
    "items": items, "total_items": len(items), "obligation_counts": counts, "editorial_decision": "Major Revision",
    "consensus_summary": "Stage 3' (five independent seats) found RR1 partly addressed with a must_fix residual and two major regressions (bound reading, asymmetric windows).",
    "dissenting_opinions": ["R1 grades the RR1 residual should_fix; DA grades it must_fix. The stricter grade is kept."]}
roadmap_raw = write(A / "roadmap_round2.json", roadmap)
claim = {"schema_version": "claim-surface-manifest/1.0", "revision_round": 2, "roadmap_sha256": sha(roadmap_raw), "base_draft_sha256": sha(base_raw), "claim_intent_sources": [], "surfaces": []}
claim_raw = write(A / "claim_surface_round2.json", claim)
user_msg = "vậy cứ làm đi nha. Không cần hỏi tôi xem tôi có đồng ý không. phải làm cẩn thận tóot nhất theo skill . Ra bài báo tốt nhất'. tôi đi ngủ và taứt màn hình đây."
ev = "AUTHOR-EVENT-round2-standing"
choices = {"schema_version": "author-adjudication-input/1.0",
    "author_events": [{"event_id": ev, "source": "explicit_session_user_message", "actor_role": "author", "input_sha256": sha(user_msg.encode())}],
    "display_order": {"mode": "source_traceability", "item_ids": [i["id"] for i in items], "author_event_id": ev},
    "author_adjudications": [{"item_id": i["id"], "author_event_id": ev, "author_triage": "will_address", "authorized_targets": i["proposed_targets"], "claim_strength_authorizations": []} for i in items],
    "collateral_authorizations": []}
write(A / "author_choices_round2.json", choices)
(A / "author_event_round2.txt").write_text(user_msg)
print("roadmap items", len(items), counts)
