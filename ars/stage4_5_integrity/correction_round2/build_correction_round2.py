"""Stage 4.5 integrity-correction round 2 (ARS #390 integrity variant).

Builds integrity-correction-list/1.0 and a patch 1.1 (authorization_context =
integrity_correction) against the anchored manuscript_v4.md. Every edit is an
exact substring replacement asserted to match once inside its block.
"""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "manuscript_v5.md"
raw = BASE.read_bytes()
text = raw.decode("utf-8")
parts = re.split(r"<!--block:(B\d{4})-->\n", text)
blocks = {parts[i]: parts[i + 1].rstrip("\n") for i in range(1, len(parts), 2)}
manifest = json.loads((HERE / "manuscript_v5.md.block-manifest.json").read_text())
old_hash = {b["block_id"]: b["old_hash"] for b in manifest["blocks"]}

# ------------------------------------------------------------------ issue list
ISSUES = [
    ("IL-MEDIUM-1", "Re-verification N-1: GEIS ground-rules reference names v13.4 (March 2025) with the always-current URL accessed 24 September 2026; the version served then was later. Cite as an undated, continuously updated document with retrieval date (APA n.d.), placed before dated FTSE Russell entries.", ["B0011", "B0018", "B0167", "B0195"]),
    ("IL-MEDIUM-2", "Re-verification N-2 (Phase D CLOSE_MATCH): the Burnham et al. (2018) sentence repeats 13 of 14 words of the abstract in order.", ["B0024"]),
    ("IL-MINOR-1", "Shleifer (1986) reports excess returns that persist for at least ten days; 'do not reverse' still implies permanence.", ["B0021"]),
    ("IL-MINOR-2", "FTSE FAQ reference uses the index-notice title; the PDF at the cited URL is 'Reclassification of Vietnam from Frontier to Secondary Emerging Market Status - FAQ', indexed as v1.2, April 2026.", ["B0169"]),
    ("IL-MINOR-3", "The CAR test prose can be read as (CAR/sigma) x sqrt(L); the code and Table 4 note use CAR/(sigma x sqrt(L)).", ["B0044"]),
    ("IL-MINOR-4", "Gregoriou & Nguyen (2010): the null result concerns the effect of the liquidity lost after deletion on investment, not deletion as such.", ["B0022"]),
]
EDITS = {
    "B0011": [("(FTSE Russell, 2025)", "(FTSE Russell, n.d.)")],
    "B0018": [("(FTSE Russell, 2025)", "(FTSE Russell, n.d.)")],
    "B0021": [("Shleifer (1986) interprets excess returns that do not reverse after inclusion as evidence",
               "Shleifer (1986) interprets excess returns that persist for at least ten days after inclusion as evidence")],
    "B0022": [("whereas Gregoriou and Nguyen (2010) find no significant effect of FTSE 100 deletions on investment.",
               "whereas Gregoriou and Nguyen (2010) find that the liquidity lost after FTSE 100 deletions has no significant effect on investment.")],
    "B0024": [("At the country level, prices of markets that MSCI reclassifies overshoot between the announcement and the effective date and largely revert within a year (Burnham et al., 2018).",
               "Burnham et al. (2018) show that, when MSCI moves a country to a different index family, the country's stock prices move sharply in the direction implied by the new benchmark before the change is implemented and give back most of that move in the following year.")],
    "B0044": [("the portfolio CAR is divided by the standard deviation of daily portfolio abnormal returns in an estimation window, multiplied by the square root of the number of days in the event window, which assumes independent daily abnormal returns.",
               "the test statistic divides the portfolio CAR by the product of two terms, the standard deviation of daily portfolio abnormal returns in an estimation window and the square root of the number of days in the event window, which assumes independent daily abnormal returns.")],
    "B0169": [("FTSE Russell. (2026). *Reclassification of Vietnam to secondary emerging market status: FAQ*.",
               "FTSE Russell. (2026, April). *Reclassification of Vietnam from frontier to secondary emerging market status: FAQ* (Version 1.2).")],
}
INSERTS = {
    "B0167": "FTSE Russell. (n.d.). *FTSE Global Equity Index Series ground rules*. Retrieved 24 September 2026, from https://www.lseg.com/content/dam/ftse-russell/en_us/documents/ground-rules/ftse-global-equity-index-series-ground-rules.pdf",
}
DELETES = ["B0195"]
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
    "revision_round": 4,
    "base_draft_sha256": base_sha,
    "issues": [{"correction_id": c, "description": d,
                "proposed_targets": [{"block_id": t, "allowed_operations": [op_for(t)]} for t in sorted(ts)]}
               for c, d, ts in ISSUES],
}
(HERE / "integrity_correction_list_round2.json").write_text(json.dumps(issue_list, indent=1, ensure_ascii=False) + "\n")
issue_list_sha = hashlib.sha256((HERE / "integrity_correction_list_round2.json").read_bytes()).hexdigest()
patch = {
    "patch_format_version": "1.1",
    "authorization_context": "integrity_correction",
    "revision_round": 4,
    "base_draft_hash": manifest["base_draft_hash"],
    "issue_list_sha256": issue_list_sha,
    "emitted_by": "draft_writer_agent",
    "ops": ops,
}
(HERE / "integrity_patch_round2.json").write_text(json.dumps(patch, indent=1, ensure_ascii=False) + "\n")
print("ops", len(ops), "issues", len(ISSUES))
print("issue_list_sha256", issue_list_sha)
print("patch_sha256", hashlib.sha256((HERE / "integrity_patch_round2.json").read_bytes()).hexdigest())
