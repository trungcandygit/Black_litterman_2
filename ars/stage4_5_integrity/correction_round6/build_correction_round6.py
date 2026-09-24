"""Integrity-correction round 6 (v9 -> v10): the six IL-MINOR issues and the E6 rows of
reverify_round5.md. Exact substring replacements inside single blocks (round-3 pattern)."""
import hashlib, json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
BASE = HERE / "manuscript_v9.md"
raw = BASE.read_bytes(); text = raw.decode()
parts = re.split(r"<!--block:(B\d{4})-->\n", text)
blocks = {parts[i]: parts[i + 1].rstrip("\n") for i in range(1, len(parts), 2)}
manifest = json.loads((HERE / "manuscript_v9.md.block-manifest.json").read_text())
old_hash = {b["block_id"]: b["old_hash"] for b in manifest["blocks"]}
SRC = "Source: Authors' calculations."
EDITS = {
 "B0068": [("largest three and two months before it (0.33 and 0.23)", "significantly so three and two months before it (0.33 and 0.23)")],
 "B0136": [("prices and liquidity moved with FTSE's public statements rather than with the first-tranche rebalancing.", "prices and liquidity moved with FTSE's public statements, and the first-tranche rebalancing brought a trading surge but no reliable price effect.")],
 "B0071": [(blocks["B0071"], f"*Note*: Coefficients $\\delta_m$ of Eq. (8), estimated jointly with the same month interactions for named-but-excluded stocks, with 95% confidence intervals (panel A: log Amihud; panel B: log trading value); dashed lines mark the announcement, confirmation and list months. {SRC}")],
 "B0189": [(blocks["B0189"], f"*Note*: Eq. (8) for log Amihud with $\\mathrm{{ITT}}_i$ in place of $\\mathrm{{Constituent}}_i$, never-named, never-included controls and 95% confidence intervals; dashed lines as in Figure 1. {SRC}")],
 "B0067": [(blocks["B0067"], f"*Notes*: Log Amihud unless stated; the split rows come from one regression with never-named, never-included controls, and other details are as in Table 2. {SRC}")],
 "B0101": [(blocks["B0101"], f"*Notes*: Eq. (7) with segment-by-window interactions; the last row reports the mean (standard error), significance marks are omitted for the three-stock segments and the last row, and other details are as in Table 2. {SRC}")],
 "B0108": [(blocks["B0108"], f"*Notes*: Eq. (7), with volatility $\\mathrm{{Vol}}_{{iw}}$ from Eq. (4), spreads in decimal units (0.0010 = 0.10 percentage points) and other details as in Table 2. {SRC}")],
 "B0115": [(blocks["B0115"], f"*Notes*: Dependent variable log Amihud; the excluded stocks and the inference settings (one-sided randomization inference) are given in Sections 3.3 and 5.1, and other details are as in Table 2. {SRC}")],
 "B0131": [(blocks["B0131"], f"*Notes*: One regression per panel on all 366 stocks, relative to never-named stocks, with S1–S3 as defined in Section 5.2, point estimates only for the two-stock row and other details as in Table 2. {SRC}")],
 "B0213": [("with S1–S3 as in Table 9", "with S1–S3 as defined in Section 5.2")],
 "B0148": [(blocks["B0148"], f"*Notes*: Pre-period means (log trading value is the mean daily log of 1 plus traded value in VND billion) and standardized mean differences (SMD); log price and volatility stay above 0.10 after matching, so the matched estimates are paired with the size-by-week and trend specifications. {SRC}")],
 "B0024": [("and distinct return and trading-volume responses when a country changes class", "and returns and trading volume that respond differently when a country changes class")],
}
ISSUES = [
 ("IL-MINOR-1", "reverify_round5.md IL-MINOR-1: B0068 'largest three and two months before it' contradicts April 2025 (0.248); now 'significantly so'.", ["B0068"]),
 ("IL-MINOR-2", "reverify_round5.md IL-MINOR-2 and ADV-E6-1 (restore): B0136 'rather than with the first-tranche rebalancing' contradicted the 0.79 trading surge.", ["B0136"]),
 ("IL-MINOR-3", "reverify_round5.md IL-MINOR-3: note disclosures restored (Figure 1 named-but-excluded interactions; Figure 2 and Table 3 split rows never-named, never-included controls).", ["B0067", "B0071", "B0189"]),
 ("IL-MINOR-4", "reverify_round5.md IL-MINOR-4: Tables 6, 7, 8 notes refer significance marks to Table 2; Table 6 omission statement corrected.", ["B0101", "B0108", "B0115"]),
 ("IL-MINOR-5", "reverify_round5.md IL-MINOR-5: S1-S3 defined by pointer in Table 9 and A.3 notes; Table A.2 log trading value defined.", ["B0131", "B0148", "B0213"]),
 ("IL-MINOR-6", "reverify_round5.md IL-MINOR-6 (Phase D): Biktimirov & Afego paraphrase distance restored.", ["B0024"]),
]
ids_for = {}
for c, _, ts in ISSUES:
    for t in ts: ids_for.setdefault(t, []).append(c)
ops = []
for bid in [b for b in re.findall(r"<!--block:(B\d{4})-->", text) if b in EDITS]:
    new = blocks[bid]
    for o, r in EDITS[bid]:
        assert new.count(o) == 1, (bid, o[:40]); new = new.replace(o, r)
    ops.append({"op": "replace_block", "block_id": bid, "old_hash": old_hash[bid], "new_text": new,
                "roadmap_item_ids": ids_for[bid], "claim_strength_changes": [], "collateral_authorization_ids": []})
issue_list = {"schema_version": "integrity-correction-list/1.0", "revision_round": 8, "base_draft_sha256": hashlib.sha256(raw).hexdigest(),
              "issues": [{"correction_id": c, "description": d, "proposed_targets": [{"block_id": t, "allowed_operations": ["replace_block"]} for t in sorted(ts)]} for c, d, ts in ISSUES]}
(HERE / "integrity_correction_list_round6.json").write_text(json.dumps(issue_list, indent=1, ensure_ascii=False) + "\n")
il_sha = hashlib.sha256((HERE / "integrity_correction_list_round6.json").read_bytes()).hexdigest()
patch = {"patch_format_version": "1.1", "authorization_context": "integrity_correction", "revision_round": 8,
         "base_draft_hash": manifest["base_draft_hash"], "issue_list_sha256": il_sha, "emitted_by": "draft_writer_agent", "ops": ops}
(HERE / "integrity_patch_round6.json").write_text(json.dumps(patch, indent=1, ensure_ascii=False) + "\n")
p_sha = hashlib.sha256((HERE / "integrity_patch_round6.json").read_bytes()).hexdigest()
ev = (HERE.parent / "correction_round5" / "author_events_round5.md").read_text()
final = re.search(r"## AUTHOR-EVENT-r5-final\n(.*?)(?=\n## |\Z)", ev, re.S).group(1).strip()
author_input = {"schema_version": "integrity-correction-authorization-input/1.0", "revision_patch_sha256": p_sha,
  "author_events": [{"event_id": "AUTHOR-EVENT-r5-final", "source": "explicit_session_user_message", "actor_role": "author", "input_sha256": hashlib.sha256(final.encode()).hexdigest()}],
  "author_decisions": [{"correction_id": c, "author_event_id": "AUTHOR-EVENT-r5-final", "decision": "authorize", "authorized_targets": i["proposed_targets"]} for c, i in zip([x[0] for x in ISSUES], issue_list["issues"])]}
(HERE / "integrity_author_input_round6.json").write_text(json.dumps(author_input, indent=1, ensure_ascii=False) + "\n")
print("ops", len(ops), "patch", p_sha)
