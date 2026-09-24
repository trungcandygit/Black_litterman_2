# Round 4 token-conservation dispositions (document level, v7 -> v8)

`token_conservation_round4.json`: 121 ops, 63 advisory rows. Deltas are expected for a compaction round. They were checked at the level of the whole document (numbers and author-year citations in the body, v7 clean vs v8 clean).

- **Numbers new to the text (4):** 0.15 (the standard error 0.153 from Table 5 panel B, now in the text); 0.47 and 0.69 (the matched declines -0.471 and -0.691 in Table 2, written as positive declines); 3% (Harris & Gurel's "more than 3 percent", from the abstract verified in Phase B). None is a new estimate.
- **Numbers gone from the document:** all come from content moved or merged under IL-MINOR-3. They are:
  - Table 4 panel C (named-but-excluded CARs), whose ranges stay in the text and are marked "not tabulated";
  - the cross-sectional t column, except 6.48 and 2.27, which are quoted;
  - the Table 5 panel B values, now in the text rounded (0.76, -0.28, 0.00);
  - the dropped Table 8 rows: placebo, two-way clustering, matched bootstrap and volatility control. Their results stay in the text (0.04 (0.10), "<17%", "at or below 0.003") or in Table 7;
  - the matched percentage declines (21%, 38%, 50%);
  - the sector numbers, now in Table 8;
  - the reference-session alternative (0.62, t = 3.54).

  Every one remains traceable in output/ (output/TABLE_SOURCE_MAP.md).
- **Citations:** no reference lost its last citation. All 33 references are still cited. The narrative forms "Becker-Blease and Paul (2006)", "Brown and Warner (1985)" and "Gregoriou and Nguyen (2010)" became parenthetical citations. New citation contexts (IL-MINOR-4) are listed for the Stage 4.5 re-verification: Harris & Gurel (B0083, B0094), Hegde & McDermott (B0060, B0105), Dong et al. (B0076), Burnham et al. (B0083), Biktimirov & Afego (B0013, B0083), Becker-Blease & Paul (B0132), Raddatz et al. (B0094, B0097), Chordia et al. (B0048), Amihud (B0104), Corwin & Schultz (B0043, B0105).
