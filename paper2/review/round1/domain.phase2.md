contract_role: domain
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: warn
trigger: "institutional detail is partly sourced"

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

Overall domain view. The manuscript reports a large, carefully decomposed ceiling and floor effect on the Ho Chi Minh Stock Exchange (HOSE) and a null across 22 price and volume characteristics. The empirical core is consistent with what the price-limit and overnight-return literatures would lead one to expect, and the authors are unusually open about the overlap with a non-peer-reviewed public analysis. From a domain standpoint the problems are in what surrounds the numbers: institutional facts are assumed rather than sourced, a major exchange system change inside the sample is not mentioned, the favoured economic reading is not separated from news-based rivals, and the literature base is narrow. None of these overturns the headline estimates, so my score for D2 is warn rather than block. Methodological questions (clustering, multiplicity, the hold-out) belong to other seats and are not assessed here.

Institutional-fact ledger (the contract asks for sourced versus assumed). (1) The +/-7% daily band on HOSE: sourced by me to a brokerage transcription of the HOSE trading rules (SSI, "Transaction Regulation on HSX"); the manuscript itself treats it as an assumption. (2) Tick sizes of 10, 50 and 100 VND for prices below 10,000, from 10,000 to 49,950, and from 50,000 VND: sourced by me to the same kind of guide; they match the manuscript's tick-rule assumption of 0.01, 0.05 and 0.10 thousand VND, so that assumption looks correct, although the manuscript cites nothing for it. (3) Launch of the KRX trading system on HOSE on 5 May 2025, with ATO and ATC orders losing priority over limit orders in the periodic auctions: sourced by me to news reports (Viet Nam News, VietnamNet, Vietnam.vn); I did not consult the exchange's own circular. (4) The reference-price rule (previous close, adjusted for corporate actions), session times, settlement cycle and short-sale constraints: assumed in the manuscript; I did not independently source session times or settlement and make no claim about them. (5) The claim that a ceiling-closing stock "typically cannot be bought at that close": assumed by the manuscript, plausible, not sourced. (6) Status of references: Le (2012), Veeraraghavan et al. (2007, an SSRN working paper) and the GitHub analysis (tungtran0911, 2026) are respectively an unchecked national journal article, a non-peer-reviewed working paper and non-peer-reviewed code; I could not verify Le (2012) and have not tried to confirm every other reference. The manuscript's disclosure of the GitHub item as not peer reviewed is accurate and proportionate.

### S1: Honest bounding of the novelty claim against the public analysis
**Evidence Anchor**: text: Section 1, "We do not claim to be first to document the close-to-close ceiling effect, nor its interpretation."

The authors identify the closest prior analysis, state its sample overlap, replicate its definition (1.75% under the 6.5% rule), and say their result is not an independent replication. This is correct attribution and the contribution claim is scoped accordingly.

### S2: Overnight versus intraday decomposition tied to the right literatures
**Evidence Anchor**: text: Section 5, "Berkman et al. (2012) document, for U.S. stocks, positive overnight returns followed by intraday reversals"

Placing the gap-then-giveback pattern next to Berkman et al. (2012) and Lou et al. (2019) is accurate and gives a useful domain refinement of the Kim and Rhee (1997) delayed-discovery story: the continuation sits in the opening auction, not in later days.

### S3: Candid, itemised limitations on institutional assumptions
**Evidence Anchor**: text: Section 6 (iii), "The 7% limit is checked indirectly (Table 1) but not against exchange documents"

The authors name the reference price, tick sizes and rule changes as assumptions. The disclosure is welcome; my criticism is that the fix (reading the rulebook) is cheap and was not made.

### W1: News and overnight-information rivals are not separated from the unfilled-demand reading
**Severity**: Major
**Evidence Anchor**: text: Section 4.4, "stocks that reach the limit may differ in news content"
**Confidence**: 4 - market-microstructure literature on limit-hit stocks, which are typically selected on information arrival

The abstract and Section 5 present the pattern as consistent with demand the limit prevents from clearing. The comparison with stocks that rose 5 to 6.5% (Table 5) removes a generic reversal, but not selection on news: a stock that closes at the ceiling is disproportionately one with a firm-specific announcement or a strong afternoon news flow, so a large next-open gap can be new information, or the market's completion of an already-incorporated signal, with no mechanical unfilled queue. The magnet effect (Cho et al., 2003, cited only in the introduction), attention-driven retail buying (the manuscript's own attention reading), liquidity provision and news clustering are listed or implied but never confronted with the data. The intraday giveback of 0.5% also fits an auction overshoot and does not by itself identify "delayed price discovery". Evidence that would change my view: the gap split by presence of a same-day or next-morning announcement, by queue size at the close (order-book data if obtainable), and a placebo using stocks that rise by an equal amount on news-free days. At present the interpretation should be written as one hypothesis among several and the term "discontinuity" should not carry mechanism.

### W2: Core HOSE rules are assumed, not sourced, and several are load-bearing
**Severity**: Major
**Evidence Anchor**: text: Section 2, "(public exchange guides; we treat this as an assumption and check it against the data)"
**Confidence**: 4 - exchange rules are publicly checkable; the 7% band and tick sizes agree with the guides I found

Event identification (the exact tick-rule hit, the 1.07 multiplier) depends on the reference-price rule and the tick table, and the headline "exact ceiling" estimates (2.76% gap, 1,666 events) sit on them. The assumptions I could check appear right, but the paper offers no HOSE circular, no statement of how the reference price is adjusted on ex-rights and ex-dividend days, and no mention of the wider bands for first-day listings and resumed trading that could account for the 0.064% of stock-days beyond +/-7.1% that the authors leave "uninvestigated" (Section 2). These are inexpensive to source from HOSE documents. Norm basis for the severity: exchange rules are a checkable external fact (SSI transcription of the HOSE regulation), not my own view of best practice.

### W3: The KRX system migration inside the sample is omitted, and "single market regime" is not accurate
**Severity**: Major
**Evidence Anchor**: text: Section 6 (x), "The sample is a single market regime on one exchange."
**Confidence**: 3 - date and ATO/ATC priority change sourced to press reports, not to the exchange circular; effect on opening prices not established

HOSE moved to the KRX trading platform on 5 May 2025, which is inside the 21 August 2024 to 23 September 2026 window; reports state that ATO and ATC orders ceased to have priority over limit orders in the auctions. Both the closing price that defines the event and the opening price that defines the gap are call-auction outputs, so a change in auction priority is directly relevant to the paper's mechanism and to executability at the open. The manuscript's half-sample splits are by median event date, not at the migration date, and the text never mentions the change. The authors should state the platform history, split the gap and giveback at the migration date, and drop or qualify the single-regime statement. Whether the effect differs before and after is an empirical question I cannot answer from the paper.

### W4: Literature coverage is thin on price-limit theory, Chinese A-share and Vietnamese evidence, and the novelty claim rests on it
**Severity**: Major
**Evidence Anchor**: absence: Section 1 and References — expected price-limit theory beyond Brennan (1986), Chinese A-share price-limit studies and a fuller Vietnamese literature; checked Section 1 paragraph 1, Section 5, References list
**Confidence**: 3 - I know the strands exist but cannot verify specific titles offline

The introduction and references cover Tokyo, Taiwan and Korea plus two Vietnamese items and the GitHub analysis. Missing strands: later theoretical work on price limits in equity markets (cooling-off, information-based and microstructure models); the substantial empirical work on Chinese A-share price limits, where the +/-10% band and retail dominance make the closest institutional analogue; and further studies of the Vietnamese band changes. [UNVERIFIED] search leads only: work by Kim, Rhee and co-authors on Asian price limits beyond the 1997 paper, empirical studies of Shanghai and Shenzhen price limits, and Vietnamese-language journals on the HOSE band. Lou et al. (2019) appears only in Section 5 and the overnight-return literature is otherwise represented by one 2012 paper. The statement "no peer-reviewed study documents ... for HOSE" is bounded to the authors' search (Appendix C), which I regard as under-reached; a revised novelty paragraph should follow a broader search and a short critical synthesis, not a list. This requires rewriting and added citations, but the core survives.

### W5: The claim that a ceiling-closing stock cannot be bought at the close, and the executability of the next open, are unsourced
**Severity**: Minor
**Evidence Anchor**: text: Section 4.6, "A stock that closes at its ceiling typically cannot be bought at that close"
**Confidence**: 3 - plausible from queue mechanics, unverified for this sample

The tradable-return measure assumes a fill at the vendor's open. In an opening call auction a buyer can be rationed or locked out when the stock opens again at the limit (522 locked days are noted), and the figures are conditioned on days with a next-day price. The conclusion "gains nothing from chasing ceiling stocks at the open" is therefore a statement about the quoted open, not about achievable fills; the paper should say so.

### W6: Policy implications read the data as evidence about the limit's effectiveness
**Severity**: Minor
**Evidence Anchor**: text: Section 5, "the evidence says that the limit does not settle the price on the limit day"
**Confidence**: 4 - the paper itself disclaims causality

With no variation in the band, no pre-limit regime and no counterfactual for how prices would form without a limit, the data cannot show what the limit does to price settlement. The regulator-facing sentence should be restated as a description of what happens after limit closes, in line with the paper's own statement that it makes no causal claim.

### W7: Reference verification and status statements are uneven
**Severity**: Minor
**Evidence Anchor**: text: Appendix C, "All references were verified against records returned by web search"
**Confidence**: 3 - I did not re-verify every entry

Appendix C says no DOI or Crossref resolution was possible. Several references (Le 2012, Chen 1993, Berkman and Lee 2002) carry no DOI and I could not confirm them; the description of Chen (1993) and Berkman and Lee (2002) findings in Section 1 should be checked against the originals. Veeraraghavan et al. (2007) is correctly shown as an SSRN paper, but the text calls it a study "on the Vietnamese exchange" without saying it is a working paper.

### W8: Terminology used more strongly than the design supports
**Severity**: Minor
**Evidence Anchor**: text: Section 5, "is the main reason we describe the result as a discontinuity"
**Confidence**: 4 - the authors concede the design is not a regression discontinuity

"Discontinuity" and "pre-specified" are used for an association around a rule threshold and an internal log respectively. The authors qualify both, but the abstract and headings keep the stronger words. "Delayed price discovery" is also used for a pattern that partly reverses within the day, which sits uneasily with a permanent information reading.

Questions for the authors: (1) What does HOSE's own rule text say about the reference price on corporate-action days and about first-day and resumed-trading bands, and do any events fall under them? (2) Do the gap and giveback differ before and after 5 May 2025? (3) What fraction of ceiling events have a same-day or next-morning company announcement? (4) Which Chinese A-share and Vietnamese price-limit studies did the search in Appendix C reach, and which were excluded?
