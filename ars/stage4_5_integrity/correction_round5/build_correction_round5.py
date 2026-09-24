"""Integrity-correction round 5 (v8 -> v9) (ARS #390 integrity variant): proofreading + stop-slop
findings and the author's round-4 requests (short table notes, table lead-ins, compact
tables, ~20% shorter text, literature comparisons from the existing reference list, more
method equations), applied to the anchored manuscript_v8.md.

The target text is v9_target.md (assembled by assemble_v9.py; written by v9_edits.py). This script derives the
patch ops from it: changed blocks -> replace_block (new blocks that follow a kept block are
folded into its new_text), removed blocks -> delete_block, unchanged blocks with new
followers -> insert_after. It also writes the integrity-correction list and the author input.
"""
import hashlib
import json
import re
from pathlib import Path

from assemble_v9 import target_seq, v7_blocks

HERE = Path(__file__).resolve().parent
BASE = HERE / "manuscript_v8.md"
raw = BASE.read_bytes()
manifest = json.loads((HERE / "manuscript_v8.md.block-manifest.json").read_text())
old_hash = {b["block_id"]: b["old_hash"] for b in manifest["blocks"]}
v7 = dict(v7_blocks())
v7_order = [b for b, _ in v7_blocks()]

# ------------------------------------------------------------------ derive ops from the target
seq = target_seq()
groups = []  # (anchor_id, own_text, [follower texts])
for bid, text, _ in seq:
    if bid == "NEW":
        groups[-1][2].append(text)
    else:
        groups.append((bid, text, []))
kept = {g[0] for g in groups}
# kept blocks must stay in v7 order (no reordering in this round)
assert [g[0] for g in groups] == [b for b in v7_order if b in kept], "reordered blocks"

op_kind = {}
new_text = {}
for bid, text, followers in groups:
    if followers and text == v7[bid]:
        op_kind[bid] = "insert_after"
        new_text[bid] = "\n\n".join(followers)
    elif text != v7[bid] or followers:
        op_kind[bid] = "replace_block"
        new_text[bid] = "\n\n".join([text] + followers)
for bid in v7_order:
    if bid not in kept:
        op_kind[bid] = "delete_block"

# ------------------------------------------------------------------ issue list
CHANGED = sorted(op_kind)
ISSUES = [
    ("IL-MEDIUM-1", "Stage 4.5 re-verification round 4 (reverify_round4.md) IL-MEDIUM-1 and ADV-E6-3: B0013 attached the discrete confirmation step to the ITT group; restored the constituent subject and the 'beyond a gradual post-announcement drift' qualifier.", ["B0013"]),
    ("IL-MEDIUM-2", "reverify_round4.md IL-MEDIUM-2: B0018 said all FTSE screens use the investability weight; restored 'in the liquidity test' and the '(10% of 49%)' arithmetic marker.", ["B0018"]),
    ("IL-MINOR-1", "reverify_round4.md IL-MINOR-1..7 and E6 rows ADV-E6-1..7: Harris & Gurel and Burnham wording restored to the verified source content (B0094, B0024); benchmark tercile base restated (B0203); log offset 1e-6 stated in Eqs. (4) and (9) (B0200, B0208); ITT row caveat (B0112); Table 7 headers (B0107); upward-drift wording reverted to the v7 rung ('had to buy', three-stock caveat, 'under three of four benchmarks', 'treat neither as a bound', Dong scope caveat) in B0003, B0060, B0098, B0135, B0132, B0024.", ["B0003", "B0024", "B0060", "B0094", "B0098", "B0107", "B0112", "B0132", "B0135", "B0200", "B0203", "B0208"]),
    ("IL-MINOR-2", "Final proofreading report (ars/stage5b_proofread/round2/proofreading_report_v8.md): undefined symbols in Eqs. (2)-(3), (6), (8), (9) defined; CS letters renamed (phi, psi, eta) to avoid clashing with alpha_i and beta_k; Eq. (9) uses the day index t; event-day index s in Eq. (6); range of m stated; overflowing Eqs. (4), (6), (9) split with aligned; 'liquidity decline' -> 'illiquidity decline'; 'listed stocks' -> 'stocks on the preliminary list'; ambiguous 'whose', 'persistent effect', 'is the 27 stocks'; screening windows renamed S1-S3 and defined; 'three trading days follow the effective date' corrected to two sessions; figure file references; notes self-contained.", CHANGED),
    ("IL-MINOR-3", "Final stop-slop audit (ars/stage5b_proofread/round2/stop_slop_audit_v8.md) F-1..F-33 and O-1..O-8 applied under ARS precedence: long compaction sentences split, repeated citation templates and repeated facts removed, wrong Panel B lead-in fixed, rung observations O-1..O-4, O-6, O-7 moved down to the evidence ('improved from the announcement onward', 'came with', 'were to buy', 'no reliable change', 'could have diluted').", CHANGED),
    ("IL-MINOR-4", "Author requests AUTHOR-EVENT-r5-notes and AUTHOR-EVENT-r5-venue: every table and figure note reduced to one sentence plus 'Source: Authors' calculations.'; tables made more compact (shorter titles, row and column labels; Table 3 observations column dropped; details moved to Sections 3.3 and 5.1); venue rule that tables are numbered in order of first citation: table references removed from the introduction and appendix tables renumbered (A.1 lists, A.2 balance).", CHANGED),
]
issue_ids_for_block = {}
for cid, _, targets in ISSUES:
    for tb in targets:
        if tb in op_kind:
            issue_ids_for_block.setdefault(tb, []).append(cid)

ops = []
for bid in v7_order:
    if bid not in op_kind:
        continue
    ids = sorted(set(issue_ids_for_block[bid]))
    op = {"op": op_kind[bid], "block_id": bid, "old_hash": old_hash[bid]}
    if op_kind[bid] != "delete_block":
        op["new_text"] = new_text[bid]
    op.update({"roadmap_item_ids": ids, "claim_strength_changes": [], "collateral_authorization_ids": []})
    ops.append(op)

base_sha = hashlib.sha256(raw).hexdigest()
issue_list = {
    "schema_version": "integrity-correction-list/1.0",
    "revision_round": 7,
    "base_draft_sha256": base_sha,
    "issues": [{"correction_id": c, "description": d,
                "proposed_targets": [{"block_id": tb, "allowed_operations": [op_kind[tb]]}
                                     for tb in sorted(t for t in ts if t in op_kind)]}
               for c, d, ts in ISSUES],
}
(HERE / "integrity_correction_list_round5.json").write_text(json.dumps(issue_list, indent=1, ensure_ascii=False) + "\n")
issue_list_sha = hashlib.sha256((HERE / "integrity_correction_list_round5.json").read_bytes()).hexdigest()
patch = {
    "patch_format_version": "1.1",
    "authorization_context": "integrity_correction",
    "revision_round": 7,
    "base_draft_hash": manifest["base_draft_hash"],
    "issue_list_sha256": issue_list_sha,
    "emitted_by": "draft_writer_agent",
    "ops": ops,
}
(HERE / "integrity_patch_round5.json").write_text(json.dumps(patch, indent=1, ensure_ascii=False) + "\n")
patch_sha = hashlib.sha256((HERE / "integrity_patch_round5.json").read_bytes()).hexdigest()

# ------------------------------------------------------------------ author input (explicit session messages)
ev_text = (HERE / "author_events_round5.md").read_text()
events = {m.group(1): m.group(2).strip() for m in re.finditer(r"## (AUTHOR-EVENT-[\w-]+)\n(.*?)(?=\n## |\Z)", ev_text, re.S)}
EVENT_FOR = {"IL-MEDIUM-1": "AUTHOR-EVENT-r5-final", "IL-MEDIUM-2": "AUTHOR-EVENT-r5-final",
             "IL-MINOR-1": "AUTHOR-EVENT-r5-final", "IL-MINOR-2": "AUTHOR-EVENT-r5-final",
             "IL-MINOR-3": "AUTHOR-EVENT-r5-final", "IL-MINOR-4": "AUTHOR-EVENT-r5-notes"}
author_input = {
    "schema_version": "integrity-correction-authorization-input/1.0",
    "revision_patch_sha256": patch_sha,
    "author_events": [{"event_id": e, "source": "explicit_session_user_message", "actor_role": "author",
                       "input_sha256": hashlib.sha256(events[e].encode()).hexdigest()}
                      for e in sorted(set(EVENT_FOR.values()))],
    "author_decisions": [{"correction_id": c, "author_event_id": EVENT_FOR[c], "decision": "authorize",
                          "authorized_targets": iss["proposed_targets"]}
                         for c, iss in zip([i[0] for i in ISSUES], issue_list["issues"])],
}
(HERE / "integrity_author_input_round5.json").write_text(json.dumps(author_input, indent=1, ensure_ascii=False) + "\n")
print("ops", len(ops), {k: sum(1 for o in ops if o["op"] == k) for k in ("replace_block", "insert_after", "delete_block")})
print("issue_list_sha256", issue_list_sha)
print("patch_sha256", patch_sha)
