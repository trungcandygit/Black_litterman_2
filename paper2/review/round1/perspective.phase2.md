contract_role: perspective
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: warn
trigger: "a welfare or regulatory reading that goes beyond what the evidence shows"

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

Reviewer stance. I read this as a behavioral-finance and research-practice reviewer. I am an outsider to HOSE microstructure and to the econometric details of the clustered standard errors, which the methodology and domain seats cover, so I take the headline estimates as given and ask three outsider questions. Can a skeptical reader verify what was fixed before the data were seen? Is the behavioral and welfare reading tested or only asserted? Can a reader reproduce the work from what the manuscript discloses? The paper is unusually candid on all three, and several of my concerns are repairable by disclosure and reframing rather than by new analysis. I score cross-disciplinary relevance as warn, not block: no central conclusion rests on an unverifiable label presented as fact. The weaker links are the practical and regulatory readings, the unverifiable pre-specification, and the thin provenance and AI disclosure.

### S1: Candid separation of pre-specified and post hoc work
The paper states that "pre-specified" means an internal log entry, lists five specification-versus-implementation deviations, and tabulates which analyses are pre-specified or post hoc. This lets an outside reader see that the novelty claims (decomposition, discontinuity, control group) are post hoc. That is better practice than most registered-report claims in finance.
**Evidence Anchor**: text: Appendix A "Overnight–intraday decomposition; next-open returns; same-date liquidity-matched control" listed as "Post hoc (A4)"

### S2: Honest handling of prior art and independence
The manuscript credits the public GitHub analysis with the close-to-close effect and mechanism and states that its own result is "not an independent replication". It also reports the estimate under the other analysis's event definition. A reader from another field can see exactly what is and is not new.
**Evidence Anchor**: text: §1 "Our result is therefore consistent with theirs but is not an independent replication"

### S3: Explicit tradability and winner's-curse framing
Section 4.6 separates a statistical association (close-to-close continuation) from what an outsider can actually capture (entry at the next open), and Sections 4.7 and 6 name the selection of this manuscript among three projects and bound it with a Bonferroni check. This separation is what makes the practical reading assessable by a non-specialist.
**Evidence Anchor**: text: §4.6 "The close-to-close continuation is not available to an outside buyer."

### W1: The pre-specification cannot be verified by an outside reader
Everything that gives the 4-of-4 survival result its pre-specified status rests on a "time-stamped internal decision log" that readers cannot inspect, and the paper says the specification is "not independent of the project's prior results". The family of 26 was also fixed by the same authors after two earlier null manuscripts on related data. A skeptical reader therefore cannot tell what was fixed before the data were seen, and the abstract's "pre-specified family" and "survive" language carries more weight than the evidence supports. Suggested remedy: deposit a hash-stamped or third-party time-stamped copy of the log and the code at the specification commit (a public repository tag or an OSF-type registry now, flagged as retrospective), and state in the abstract that the specification is internal. The headline claim should be framed as "specified in an internal log before computation" rather than as pre-registered evidence.
**Severity**: Major
**Evidence Anchor**: text: §3.1 "it is not an external registry entry"
**Confidence**: 4 - research-practice and pre-registration credibility is this seat's core competence; I have not seen the log.

### W2: AI-assisted workflow disclosure and evidence trail are too thin for independent replication
The declaration says the code, tables and draft were produced with Claude under a named workflow, but gives no model version, no description of which steps were human-verified, and no access to prompts or logs. It also says the authors "are responsible for verifying" everything "before submission", which reads as verification still pending. Reference verification, the decisions log, the devil's-advocate report and the literature log are cited only as local `process/` and `review/` paths that a reader cannot open, and the data and code statement points to a local path (`paper2/R/`) with no public archive or DOI. The vendor library (vnstock) and the unadjusted-or-adjusted status of prices are also undocumented. Suggested remedy: add a disclosure paragraph with model and version, the tasks delegated, and the human checks performed; deposit code, derived tables and the logs cited in the text in a public archive; and report a data-retrieval date and vendor version.
**Severity**: Major
**Evidence Anchor**: text: Declarations "the authors are responsible for verifying all choices, results and references before submission"
**Confidence**: 4 - based on responsible-AI reporting and replication practice; whether a journal accepts local-path references is a venue question I cannot judge.

### W3: Regulatory and investor implications go beyond an unidentified-trader association
The Discussion states what the evidence "says" for regulators and investors. The data contain no investor-type, order-book, welfare or limit-order information, and the paper itself concedes the mechanism is inferred. A regulator-facing statement that the limit "does not settle the price" and an investor-facing statement that the evidence argues against chasing limit-up stocks both use a statistical association as a welfare or policy conclusion. The tradable five-day shortfall is also benchmark-sensitive, as the manuscript notes (t = -2.7 against the market but -1.8 against controls), and the open is an auction price whose executability for a retail buyer is assumed rather than shown. Suggested remedy: recast the Implications paragraph as hypotheses for regulators with the required data named (order-level, investor-type, trading-halt or auction-rule variation), and add a plain statement that no welfare or investor-protection conclusion is drawn.
**Severity**: Major
**Evidence Anchor**: text: §5 "For investors, it argues against chasing limit-up stocks at the open"
**Confidence**: 4 - the gap between association and welfare claim is a recurring behavioral-finance review issue; the paper's hedges in Section 4.6 partly mitigate it.

### W4: The behavioral mechanism is borrowed by analogy, not tested
The abstract, keywords and Discussion lean on delayed price discovery, retail investors and attention (Berkman et al., 2012). No retail-attention, lottery-preference or participation proxy is examined, and selection of limit events on news content is acknowledged but not separated from "unfilled demand". Within the available daily data, a simple partial check would be a split by a lottery or attention proxy already in the family (for example MAX or LIMITFREQ) to see whether the gap is larger where such behavior is plausible. At minimum, drop "retail investors" from the keywords or mark it as motivation rather than finding.
**Severity**: Minor

### W5: Institutional facts about HOSE are assumed rather than sourced
The 7% band, the reference-price rule, tick sizes, the opening auction, short-selling constraints and any rule change in the window are stated as understandings from "public exchange guides" without citations. An adjacent-field reader cannot verify them, and the exact-tick definition depends on them. Citing the exchange rulebook and the dates of any regulation changes would make the institutional setting checkable.
**Severity**: Minor

### Additional perspective notes
Cross-disciplinary reading leads, none verified in this session and offered only as search leads: [UNVERIFIED] work on retail attention and overnight returns beyond Berkman et al. (2012), including the retail-trading literature on lottery preferences and limit-up salience in China and Vietnam; [UNVERIFIED] research on the credibility of internal pre-registration and registered reports in finance and economics; [UNVERIFIED] responsible-AI reporting guidance for AI-assisted empirical research. The Korean and Taiwanese limit studies the paper already cites are the most relevant parallel evidence from adjacent markets.

Questions for the authors: (1) Can the specification log be given an external time-stamp? (2) Which results were produced and checked by a human before the draft was written? (3) Is any retail-attention or participation proxy available for a heterogeneity test of the gap? (4) What does the opening auction allow an investor to buy at, and how often is a ceiling stock buyable at the open?
