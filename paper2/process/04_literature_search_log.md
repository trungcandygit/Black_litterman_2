# Stage 1 literature search and reference verification log (Paper C)
Date: 2026-10-04. Tools: WebSearch (works), WebFetch (works for some hosts; doi.org, Crossref, OpenAlex, Wikipedia, briefs.co are blocked by the egress proxy). Verification standard: a search result returning the bibliographic record (title, authors, journal, volume, pages, year) from a publisher, RePEc/IDEAS, EconPapers, NBER, SSRN, SemanticScholar or ScienceDirect page.

## Search strategy (bounds the novelty statement)
Queries run: price-limit performance (delayed price discovery, volatility spillover, trading interference, magnet effect); price limits Vietnam / HOSE; overnight vs intraday returns; MAX/lottery; low volatility; multiple-testing and FDR; two-way clustering; regression discontinuity. Databases reached through the web search tool only (no Scopus/WoS access). The novelty statement in the manuscript is therefore bounded: "to our knowledge, among the sources found by this search".

## Prior art found that bears directly on novelty (Devil's Advocate Checkpoint 1, Major -> binding)
1. tungtran0911 (2026), GitHub repository `vn-equity-factors` (README presented as the paper; no DOI; not peer reviewed; 404 HOSE stocks, KBS data, 2016-01-04 to 2026-09-25): reports next-session abnormal return after a ceiling close of +1.694% (t = 39.47), after a 3-6.5% rise -0.388%, after a floor close -0.225% (t = -3.77); limit-up-day count priced negatively over the next month (-0.69% per month). This is a direct, longer-sample precedent for the close-to-close continuation. Consequence: no "first to document" claim; the contribution is (i) the overnight-gap versus intraday decomposition and its tradability implication, (ii) a formal discontinuity comparison at the limit with date- and stock-clustered inference, (iii) a pre-registered, FDR-controlled family showing that the standard characteristics are null in the same sample, and (iv) an independent replication on a different data feed and sample.
2. Veeraraghavan, Nguyen & Truong (2007), SSRN 1009042, "Delayed price discovery and momentum strategies: Evidence from Vietnam": momentum and price limits on the Vietnamese exchange, 2000-2006.

## Verified references (status VERIFIED = bibliographic record found in the search results listed)
| Reference | Status | Evidence source |
|---|---|---|
| Kim & Rhee (1997) JF 52(2), 885-901 | VERIFIED | Wiley Online Library record via search |
| Brennan (1986) JFE 16, 213-233 (doi 10.1016/0304-405X(86)90061-9) | VERIFIED | search results |
| Chen (1993) PBFJ 1(2), 139-153 | VERIFIED | ScienceDirect / IDEAS |
| Cho, Russell, Tiao & Tsay (2003) JEF 10(1), 133-168 | VERIFIED | Semantic Scholar / search results |
| Berkman & Lee (2002) PBFJ 10(5), 517-530 | VERIFIED | search results |
| Berkman, Koch, Tuttle & Zhang (2012) JFQA 47(4), 715-741 | VERIFIED | Missouri State repository / Cambridge Core |
| Lou, Polk & Skouras (2019) JFE 134(1), 192-213 | VERIFIED | EconPapers / HKUST portal |
| Cameron, Gelbach & Miller (2011) JBES 29(2), 238-249 | VERIFIED | IDEAS / EconPapers |
| Benjamini & Hochberg (1995) JRSSB 57(1), 289-300 | VERIFIED | Wiley / Tel Aviv University portal |
| Fama & MacBeth (1973) JPE 81(3), 607-636 | VERIFIED | IDEAS / EconPapers |
| Imbens & Lemieux (2008) J. Econometrics 142(2), 615-635 | VERIFIED | IDEAS / NBER |
| Bali, Cakici & Whitelaw (2011) JFE 99(2), 427-446 | VERIFIED | NYU Stern / SSRN-linked results |
| Corwin & Schultz (2012) JF 67(2), 719-760 | VERIFIED | Wiley / SSRN |
| Jegadeesh & Titman (1993) JF 48(1), 65-91 | VERIFIED | Wiley / EconPapers |
| Ang, Hodrick, Xing & Zhang (2006) JF 61(1), 259-299 | VERIFIED | JSTOR / Wiley / NBER |
| Veeraraghavan, Nguyen & Truong (2007) SSRN 1009042 | VERIFIED (working paper) | SSRN record via search |
| tungtran0911 (2026) vn-equity-factors | VERIFIED (grey literature, accessed 2026-10-04) | WebFetch of the repository README |
| Harvey, Liu & Zhu (2016); Ledoit & Wolf (2004, 2008); Newey & West (1987); Politis & Romano (1992, 1994); Hansen (2005); Holm (1979); Bailey & Lopez de Prado (2014) | AUTHOR-SUPPLIED or recalled; NOT re-verified in this round | author's earlier reference list (with DOIs) / memory; to be verified before submission |

## Not verified (stated without citation or marked)
HOSE trading-session times, settlement cycle and tick-size schedule were not verified (Wikipedia blocked): the manuscript does not rely on them beyond the assumed 7% daily limit, which is corroborated empirically (pile-up of returns at 6.5-7.1%; Table A1) and by the search snippets of public exchange guides.

## Update (verification round 2)
| Harvey, Liu & Zhu (2016) RFS 29(1), 5-68 | VERIFIED | IDEAS / NBER search results |
| Newey & West (1987) Econometrica 55(3), 703-708 | VERIFIED | JSTOR / EconPapers / Econometric Society search results |
Berkman, Koch, Tuttle & Zhang (2012): abstract read via the SSRN/Semantic Scholar search result: U.S. stocks, positive overnight returns followed by intraday reversals, opening price inflated among stocks that attracted retail attention, high net retail buying at the start of the day. This is the closest peer-reviewed precedent for the overnight-then-intraday signature; the manuscript now cites it in the novelty statement and the interpretation.
All 20 references cited in Paper C are VERIFIED (17 by title/abstract/record in search results; the 2 grey/working-paper items by the repository README and SSRN record).

## Update after review round 1 (4 October 2026) — references added in manuscript v7
| Reference | Verification (web search; DOI resolver and Crossref unreachable) |
|---|---|
| Subrahmanyam (1994), Journal of Finance 49(1), 237–254 | Wiley page and abstract returned by search; DOI taken from the Wiley URL |
| Bildik & Gülay (2006), Journal of Financial Research 29(3), 383–403 | Wiley page, IDEAS/RePEc and SSRN records returned; authors confirmed by search |
| Qi (2023), PLOS ONE 18(6), e0287548 | PLOS ONE and PMC pages returned; author, date and DOI from the search record |
| HSC (2025), "Important changes of new trading system" | Appeared in search results (page not fetched; egress blocked); used for the ATO/ATC priority change and the ±7% band |
| Viet Nam News (2025), "KRX system officially goes live" | Appeared in search results (page not fetched); used for the 5 May 2025 launch |
Status notes: Le (2012), Chen (1993), Berkman and Lee (2002) remain checked at abstract/bibliographic level only. Vietnamese-language journals and further Chinese A-share studies were not searched. Corrections to earlier entries: the manuscript no longer describes the study as an independent replication or as "pre-registered"; the term is "log-specified" (fixed in a version-controlled log; no external registry).
