## Contract Paraphrase

D1 (methodology_rigor, mandatory, methodology seat) asks whether the design, data handling, statistical reporting and reproducibility affordances reach the bar a peer-reviewed finance journal expects. From a methodology standpoint this means the inference procedure must match the dependence structure of the data, headline numbers must be traceable to a table or figure and be mutually consistent, any ex ante or hold-out label must be verifiable, and a third party must be able to rebuild the sample, event definition and tests from what is disclosed.

D2 (domain_accuracy, mandatory, owned by the domain seat) concerns whether claims agree with current domain evidence, prior work is represented correctly, and domain terminology and institutional facts are free of factual error. I do not score it. From my vantage point I only note that every institutional fact the study relies on should be marked as sourced or assumed, so the domain seat can judge it.

D3 (argumentative_coherence, mandatory, owned by the devil's advocate seat and also open to methodology) asks whether the central thesis is internally consistent, whether the evidence actually supports the claims made, and whether fallacies undermine the argument. From a methodology standpoint this is the question of whether conclusions stay within what the tests can license: absence of evidence versus evidence of absence, power behind any null claim, selection of news or events, and causal wording that exceeds the design.

D4 (cross_disciplinary_relevance, high priority, owned by the perspective seat) concerns whether framing, definitions and implications are accessible to adjacent-field readers and whether interdisciplinary claims are substantiated. It is outside my remit and I plan no score for it.

D5 (writing_and_structure, normal priority, owned by the editor-in-chief seat) concerns manuscript organisation, clarity, figure and table quality and venue conventions. It is outside my remit and I plan no score for it, although table-level inconsistencies belong to my D1 evidence.

D6 (venue_fit_and_contribution, mandatory, owned by the editor-in-chief seat) asks whether the manuscript fits the configured venue and makes an original, significant contribution. The contract gives no chosen venue and no criteria binding, so I make no venue-alignment claim, and I plan no score for this dimension.

## Scoring Plan

### D1: methodology_rigor

dimension_id: D1
what_to_look_for: Whether inference is robust to cross-sectional and serial dependence (clustering by date or event, overlapping multi-day windows, short-panel Fama-MacBeth-type tests); whether the event definition, benchmark or abnormal-return adjustment and sample construction are specified and defensible; whether every headline number carries a table or figure anchor and its clustering scheme and ties out across tables and text; whether a pre-registered or hold-out label is backed by a verifiable ex ante record and a survival rule applied uniformly to the whole test family with multiple-testing control; whether sub-sample power supports any null claim; and whether data, code and sample filters allow replication.
what_triggers_block: Headline results rest on inference that ignores obvious dependence with no robust alternative offered, or a core reported number cannot be reconciled with its own table, or the ex ante or hold-out claim is unverifiable and applied selectively so the main finding cannot be trusted as stated, in a way the authors could repair only through re-analysis.
what_triggers_warn: Dependence-robust inference, benchmark choice, event definition or split design is reported incompletely or only partly justified, minor numerical discrepancies or unexplained extreme sub-sample statistics remain, or replication details are thin, yet the main conclusions could plausibly survive a clarified or re-run analysis.
what_triggers_fatal: Evidence that the central empirical result is an artifact of the procedure itself, such as significance that vanishes under any dependence-robust treatment the data support, a registration or hold-out label that is shown to be false or misrepresented, or irreconcilable core numbers that make the reported results unreproducible, so that no revision short of a new study rescues the claim.

### D3: argumentative_coherence

dimension_id: D3
what_to_look_for: Whether stated conclusions, including headline claims in the abstract, stay within what the tests can license; whether non-significant results are separated from demonstrated absence and any null claim rests on adequate power; whether competing explanations such as delayed price discovery versus news or event selection are confronted with discriminating evidence rather than asserted away; whether causal or mechanism language matches a descriptive or associational design; and whether the narrative is consistent across abstract, results and conclusion.
what_triggers_block: A central claim contradicts or goes well beyond the paper's own evidence, for example a categorical null or causal mechanism asserted from underpowered, selected or non-discriminating tests, or the main argument depends on an unaddressed alternative explanation that would reverse the conclusion.
what_triggers_warn: Some conclusions are phrased more strongly than the evidence supports, alternative explanations are acknowledged but not tested, or small inconsistencies in wording between abstract, results and discussion remain, while the core thesis stays coherent once those statements are toned down.
what_triggers_fatal: The core thesis is internally self-defeating, so that the paper's own reported evidence entails the opposite of its main conclusion or leaves no interpretation of the results that supports the stated contribution, and no rewording or added analysis could restore coherence.

criteria_binding_unavailable

[CONTRACT-ACKNOWLEDGED]
