"""Integrity-correction round 4 (ARS #390 integrity variant): proofreading + stop-slop
findings and the author's round-4 requests (short table notes, table lead-ins, compact
tables, ~20% shorter text, literature comparisons from the existing reference list, more
method equations), applied to the anchored manuscript_v7.md.

The target text is v8_target.md (assembled by assemble_v8.py). This script derives the
patch ops from it: changed blocks -> replace_block (new blocks that follow a kept block are
folded into its new_text), removed blocks -> delete_block, unchanged blocks with new
followers -> insert_after. It also writes the integrity-correction list and the author input.
"""
import hashlib
import json
import re
from pathlib import Path

from assemble_v8 import target_seq, v7_blocks

HERE = Path(__file__).resolve().parent
BASE = HERE / "manuscript_v7.md"
raw = BASE.read_bytes()
manifest = json.loads((HERE / "manuscript_v7.md.block-manifest.json").read_text())
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
PR = ["B0003", "B0010", "B0012", "B0013", "B0014", "B0024", "B0028", "B0029", "B0030", "B0031", "B0034", "B0035",
      "B0038", "B0039", "B0043", "B0047", "B0048", "B0050", "B0060", "B0062", "B0063", "B0064", "B0066", "B0067",
      "B0068", "B0071", "B0072", "B0073", "B0076", "B0079", "B0081", "B0082", "B0084", "B0087", "B0090", "B0093",
      "B0096", "B0097", "B0100", "B0101", "B0105", "B0106", "B0107", "B0108", "B0112", "B0114", "B0115", "B0116",
      "B0118", "B0119", "B0120", "B0123", "B0126", "B0128", "B0131", "B0135", "B0138", "B0141", "B0144", "B0145",
      "B0147", "B0155", "B0189"]
SS = ["B0007", "B0008", "B0009", "B0011", "B0013", "B0024", "B0025", "B0060", "B0064", "B0072", "B0073", "B0074",
      "B0076", "B0083", "B0084", "B0085", "B0095", "B0098", "B0102", "B0105", "B0109", "B0112", "B0116", "B0132",
      "B0133", "B0135", "B0136", "B0137", "B0138", "B0141"]
LIT = ["B0022", "B0024", "B0048", "B0060", "B0076", "B0083", "B0094", "B0104", "B0105", "B0132", "B0136"]
EQ = ["B0041", "B0042", "B0043", "B0044", "B0047", "B0048", "B0049", "B0051", "B0054", "B0068", "B0071", "B0082",
      "B0108", "B0189"]
CLAIM = ["B0007", "B0112", "B0116", "B0135", "B0136"]
ALL = sorted(op_kind)

ISSUES = [
    ("IL-MINOR-1", "Proofreading skill report (ars/stage5b_proofread/proofreading_report.md), findings applied under ARS precedence: undefined symbols in Eq. (7) (M1), statistical symbols in italics (M2), abbreviations VND/VCI/UPCoM/CS/CAR/SMD/FE/SE (A1-A5), abstract gap sentence (S1), novelty statement and positioning moved to the introduction, hypotheses as predictions, roadmap phrase, survivorship stated in Section 3.1, comma splice, 'gives'->'yields', possessives on non-person nouns, unit consistency, significance marks defined in every table note (by reference to Table 2), table alignment (first column left, others centred), Figure 2 note (dashed lines), Table 7 title, results heading tense.", PR),
    ("IL-MINOR-2", "Stop-slop audit (ars/stage5b_proofread/stop_slop_audit.md, SS-1..SS-37 and O-1..O-4), applied under ARS precedence: the six 'Takeaway.' paragraphs removed (SS-17), cross-section repetitions removed (SS-14, SS-25, SS-26, SS-30, SS-31), announcement and throat-clearing sentences removed (SS-4, SS-5, SS-13, SS-23, SS-33, SS-34, SS-37), Wh- openers and intensifiers (SS-1, SS-2, SS-8, SS-9, SS-16), redundant 'rather than' contrasts (SS-11, SS-24, SS-29).", SS),
    ("IL-MINOR-3", "Author request (AUTHOR-EVENT-r4-tables, -r4-length, -r4-notes): table notes shortened to one or two sentences, a lead-in sentence before each table, tables made compact (redundant rows and columns moved to text; Table 4 panel C and Table 9 panel C moved out of the main text; Table 5 panel B and Table 2/7 spread columns merged), and the whole text shortened by about 20% without changing any reported estimate.", ALL),
    ("IL-MINOR-4", "Author request (AUTHOR-EVENT-r4-tables): results and discussion compared with prior studies, using only the 33 references already in the list and only content verified in Stage 4.5 Phase B (Harris & Gurel 1986; Shleifer 1986; Chen et al. 2004; Hegde & McDermott 2003; Becker-Blease & Paul 2006; Burnham et al. 2018; Dong et al. 2023; Raddatz et al. 2017; Biktimirov & Afego 2026; Chordia et al. 2000; Amihud 2002; Corwin & Schultz 2012).", LIT),
    ("IL-MINOR-5", "Author request (AUTHOR-EVENT-r4-tables): more method equations, each matching the R code: Corwin-Schultz spread (code/analysis.R lines 34-40), weekly aggregation (analysis.R weekly panel), abnormal returns, portfolio CAR and t-statistic (analysis_revision2.R car_port2), event-study specification (i(relm, treated, ref = -1)), drift term tpost (analysis_revision2.R line 20), rebalancing regression (analysis_revision.R spike()).", EQ),
    ("IL-MINOR-6", "Claim-accuracy corrections found by the proofreading and stop-slop passes: B0112 'of similar size in every specification' contradicted Table 8 (two rows about half the baseline); B0116 'the two months with the largest positive deviations' contradicted Figure 1 (April 2025 coefficient 0.248 exceeds August 2025 0.232; only July and August are significant); O-1/O-2/O-4 wording aligned with the evidence ('raised' -> 'improved', 'prices had already adjusted' and 'no price change' -> 'no reliable price effect'). Each change weakens or corrects a claim; none strengthens one.", CLAIM),
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
    "revision_round": 6,
    "base_draft_sha256": base_sha,
    "issues": [{"correction_id": c, "description": d,
                "proposed_targets": [{"block_id": tb, "allowed_operations": [op_kind[tb]]}
                                     for tb in sorted(t for t in ts if t in op_kind)]}
               for c, d, ts in ISSUES],
}
(HERE / "integrity_correction_list_round4.json").write_text(json.dumps(issue_list, indent=1, ensure_ascii=False) + "\n")
issue_list_sha = hashlib.sha256((HERE / "integrity_correction_list_round4.json").read_bytes()).hexdigest()
patch = {
    "patch_format_version": "1.1",
    "authorization_context": "integrity_correction",
    "revision_round": 6,
    "base_draft_hash": manifest["base_draft_hash"],
    "issue_list_sha256": issue_list_sha,
    "emitted_by": "draft_writer_agent",
    "ops": ops,
}
(HERE / "integrity_patch_round4.json").write_text(json.dumps(patch, indent=1, ensure_ascii=False) + "\n")
patch_sha = hashlib.sha256((HERE / "integrity_patch_round4.json").read_bytes()).hexdigest()

# ------------------------------------------------------------------ author input (explicit session messages)
ev_text = (HERE / "author_events_round4.md").read_text()
events = {m.group(1): m.group(2).strip() for m in re.finditer(r"## (AUTHOR-EVENT-[\w-]+)\n(.*?)(?=\n## |\Z)", ev_text, re.S)}
EVENT_FOR = {"IL-MINOR-1": "AUTHOR-EVENT-r4-skills", "IL-MINOR-2": "AUTHOR-EVENT-r4-skills",
             "IL-MINOR-3": "AUTHOR-EVENT-r4-length", "IL-MINOR-4": "AUTHOR-EVENT-r4-tables",
             "IL-MINOR-5": "AUTHOR-EVENT-r4-tables", "IL-MINOR-6": "AUTHOR-EVENT-r4-ars"}
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
(HERE / "integrity_author_input_round4.json").write_text(json.dumps(author_input, indent=1, ensure_ascii=False) + "\n")
print("ops", len(ops), {k: sum(1 for o in ops if o["op"] == k) for k in ("replace_block", "insert_after", "delete_block")})
print("issue_list_sha256", issue_list_sha)
print("patch_sha256", patch_sha)
