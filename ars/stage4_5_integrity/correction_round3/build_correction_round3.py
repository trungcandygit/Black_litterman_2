"""Stage 4.5 integrity-correction round 3 (ARS #390 integrity variant).

Builds integrity-correction-list/1.0 and a patch 1.1 (authorization_context =
integrity_correction) against the anchored manuscript_v4.md. Every edit is an
exact substring replacement asserted to match once inside its block.
"""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "manuscript_v6.md"
raw = BASE.read_bytes()
text = raw.decode("utf-8")
parts = re.split(r"<!--block:(B\d{4})-->\n", text)
blocks = {parts[i]: parts[i + 1].rstrip("\n") for i in range(1, len(parts), 2)}
manifest = json.loads((HERE / "manuscript_v6.md.block-manifest.json").read_text())
old_hash = {b["block_id"]: b["old_hash"] for b in manifest["blocks"]}

# ------------------------------------------------------------------ issue list
ISSUES = [
    ("IL-MINOR-1", "Stage 4.5 re-verification N2-1: the undated GEIS entry uses 'Retrieved ... from' while all other web references use the journal's 'Accessed [date]' form; unify.", ["B0196"]),
    ("IL-MINOR-2", "Venue/format compliance (author-flagged): table and figure notes cite internal output file paths (output/...csv) as sources; journal convention is 'Authors' calculations' with the data source. The file map moves to the replication package (output/TABLE_SOURCE_MAP.md).", ['B0039', 'B0063', 'B0067', 'B0071', 'B0082', 'B0093', 'B0101', 'B0108', 'B0115', 'B0131', 'B0145', 'B0189']),
]
EDITS = {
    'B0039': [('Source: output/revision/t1_descriptives.csv.', "Source: Authors' calculations from daily HOSE trading data (VCI, via vnstock).")],
    'B0063': [('Sources: output/revision/t2_baseline_clean.csv, output/revision2/t_matched_weighted.csv.', "Source: Authors' calculations from daily HOSE trading data (VCI, via vnstock).")],
    'B0067': [('Source: output/revision/t_itt.csv.', "Source: Authors' calculations from daily HOSE trading data (VCI, via vnstock).")],
    'B0071': [('Source: output/revision/t_event_study.csv.', "Source: Authors' calculations from daily HOSE trading data (VCI, via vnstock).")],
    'B0082': [('Source: output/revision2/t3_car_portfolio_clean_est.csv.', "Source: Authors' calculations from daily HOSE trading data (VCI, via vnstock).")],
    'B0093': [('Sources: output/revision/t4c_spike_test.csv, output/revision/t4b_rebalance_groups.csv.', "Source: Authors' calculations from daily HOSE trading data (VCI, via vnstock).")],
    'B0101': [('Sources: output/revision/t5_segments.csv, output/table7b_rebalance_by_segment.csv.', "Source: Authors' calculations from daily HOSE trading data (VCI, via vnstock).")],
    'B0108': [('Sources: output/revision/t6_volatility.csv, output/revision/t7_robustness.csv.', "Source: Authors' calculations from daily HOSE trading data (VCI, via vnstock).")],
    'B0115': [('Sources: output/revision/t7_robustness.csv, output/revision2/t_matched_weighted.csv, output/revision2/t_post_drift.csv, output/revision2/t_sector.csv, output/revision/t_wild_bootstrap.csv, output/revision/t6_randomization_inference.csv.', "Source: Authors' calculations from daily HOSE trading data (VCI, via vnstock).")],
    'B0131': [('Sources: output/revision/t8_named_excluded.csv, output/revision/t8c_named_by_stock.csv.', "Source: Authors' calculations from daily HOSE trading data (VCI, via vnstock).")],
    'B0145': [('Source: output/revision/tA1_balance.csv.', "Source: Authors' calculations from daily HOSE trading data (VCI, via vnstock).")],
    'B0189': [('Source: output/revision2/t_itt_event_study.csv.', "Source: Authors' calculations from daily HOSE trading data (VCI, via vnstock).")],
    "B0196": [("FTSE Russell. (n.d.). *FTSE Global Equity Index Series ground rules*. Retrieved 24 September 2026, from https://www.lseg.com/content/dam/ftse-russell/en_us/documents/ground-rules/ftse-global-equity-index-series-ground-rules.pdf",
               "FTSE Russell. (n.d.). *FTSE Global Equity Index Series ground rules*. https://www.lseg.com/content/dam/ftse-russell/en_us/documents/ground-rules/ftse-global-equity-index-series-ground-rules.pdf Accessed 24 September 2026.")],
}
INSERTS = {}
DELETES = []
issue_ids_for_block = {}
for cid, _, targets in ISSUES:
    for t in targets:
        issue_ids_for_block.setdefault(t, []).append(cid)

ops = []
for bid in sorted(set(EDITS) | set(INSERTS) | set(DELETES)):
    ids = issue_ids_for_block[bid]
    if bid in EDITS:
        new = blocks[bid]
        for old, rep in EDITS[bid]:
            assert new.count(old) == 1, (bid, old)
            new = new.replace(old, rep)
        ops.append({"op": "replace_block", "block_id": bid, "old_hash": old_hash[bid], "new_text": new,
                    "roadmap_item_ids": ids, "claim_strength_changes": [], "collateral_authorization_ids": []})
    elif bid in DELETES:
        ops.append({"op": "delete_block", "block_id": bid, "old_hash": old_hash[bid],
                    "roadmap_item_ids": ids, "claim_strength_changes": [], "collateral_authorization_ids": []})
    else:
        ops.append({"op": "insert_after", "block_id": bid, "old_hash": old_hash[bid], "new_text": INSERTS[bid],
                    "roadmap_item_ids": ids, "claim_strength_changes": [], "collateral_authorization_ids": []})

base_sha = hashlib.sha256(raw).hexdigest()
def op_for(bid):
    return "insert_after" if bid in INSERTS else ("delete_block" if bid in DELETES else "replace_block")
issue_list = {
    "schema_version": "integrity-correction-list/1.0",
    "revision_round": 5,
    "base_draft_sha256": base_sha,
    "issues": [{"correction_id": c, "description": d,
                "proposed_targets": [{"block_id": t, "allowed_operations": [op_for(t)]} for t in sorted(ts)]}
               for c, d, ts in ISSUES],
}
(HERE / "integrity_correction_list_round3.json").write_text(json.dumps(issue_list, indent=1, ensure_ascii=False) + "\n")
issue_list_sha = hashlib.sha256((HERE / "integrity_correction_list_round3.json").read_bytes()).hexdigest()
patch = {
    "patch_format_version": "1.1",
    "authorization_context": "integrity_correction",
    "revision_round": 5,
    "base_draft_hash": manifest["base_draft_hash"],
    "issue_list_sha256": issue_list_sha,
    "emitted_by": "draft_writer_agent",
    "ops": ops,
}
(HERE / "integrity_patch_round3.json").write_text(json.dumps(patch, indent=1, ensure_ascii=False) + "\n")
print("ops", len(ops), "issues", len(ISSUES))
print("issue_list_sha256", issue_list_sha)
print("patch_sha256", hashlib.sha256((HERE / "integrity_patch_round3.json").read_bytes()).hexdigest())
