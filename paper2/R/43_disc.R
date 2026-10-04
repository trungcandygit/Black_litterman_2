# SUPERSEDED by R/47_da_response.R for all numbers in manuscript C (see Appendix B); kept for audit. Known issue: NA propagation in the market and control calculations (41), and all-stock population (44).
# 43_disc.R -- formal discontinuity comparison (limit close vs just-below-limit), tradability of the next-open rule
suppressPackageStartupMessages({library(sandwich); library(lmtest)}); od <- "/home/user/Black_litterman_2/paper2/output"
E <- readRDS(file.path(od, "rds/limit_events_full.rds"))
cmp <- function(a, b, col, label) { d <- E[E$event %in% c(a, b) & is.finite(E[[col]]), ]; d$tr <- as.numeric(d$event == a); fit <- lm(d[[col]] ~ d$tr); vc <- vcovCL(fit, cluster = d$t, type = "HC1"); ct <- coeftest(fit, vcov. = vc)
  data.frame(contrast = label, outcome = col, diff_pct = 100 * coef(fit)[2], t_cluster = ct[2, 3], n_treated = sum(d$tr), n_control = sum(1 - d$tr)) }
cmps <- list(c("ceiling", "near_up_5_6.5", "ceiling vs 5-6.5% up"), c("ceiling", "near_up_3_5", "ceiling vs 3-5% up"), c("floor", "near_dn_5_6.5", "floor vs 5-6.5% down"), c("floor", "near_dn_3_5", "floor vs 3-5% down"))
D <- do.call(rbind, lapply(cmps, function(c) do.call(rbind, lapply(c("ar_on", "ar_id", "ar_cc1", "ar_5o"), function(col) cmp(c[1], c[2], col, c[3])))))
rownames(D) <- NULL; write.csv(D, file.path(od, "tables/C8_discontinuity.csv"), row.names = FALSE); print(D, digits = 3)
# next-open rule value for a holder: sell at the next open vs hold to the next close (ceiling), cost of buying at open
ce <- E[E$event == "ceiling" & is.finite(E$ar_id), ]; cat("ceiling: mean intraday AR (hold from open to close), pct:", 100 * mean(ce$ar_id), " share of events with negative intraday AR:", mean(ce$ar_id < 0), "\n")
cat("break-even one-way cost (bps) for the intraday reversal of a short at open (not feasible: no short selling):", 1e4 * abs(mean(ce$ar_id)) / 2, "\n")
