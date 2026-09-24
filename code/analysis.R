# FTSE2: Stock-level liquidity effects of Vietnam's FTSE Russell reclassification
# Difference-in-differences and event study on HOSE stocks, Oct 2024 - Sep 2026.
suppressPackageStartupMessages({
  library(data.table); library(fixest); library(ggplot2); library(MatchIt)
})
# Run from the project root (the folder that contains code/, data/ and output/).
dir.create("output", showWarnings = FALSE)
set.seed(20260924)

# ---------------------------------------------------------------- key dates
D_ANN  <- as.IDate("2025-10-07")  # FTSE announces upgrade to Secondary Emerging
D_CONF <- as.IDate("2026-04-07")  # FTSE confirms; effective date fixed
D_LIST <- as.IDate("2026-08-21")  # FTSE publishes the 27 constituents
D_REB  <- as.IDate("2026-09-18")  # rebalancing (last pre-effective) session
D_EFF  <- as.IDate("2026-09-21")  # effective date

treated27 <- c("VCB","VIC","VHM","BID","VPB","HPG","FPT","GEX","HDB","HCM","MCH","MSN","NVL",
               "STB","SHB","SSB","SSI","TCX","VCI","VJC","VNM","MSB","VRE","VPL","VIX","VND","VCK")
nearmiss  <- c("SAB","DXG","GEE","BSR","PLX")  # named on FTSE eligibility lists, not in final 27

# ---------------------------------------------------------------- load
files <- list.files("data/raw", pattern = "\\.csv$", full.names = TRUE)
dt <- rbindlist(lapply(files, function(f) {
  x <- fread(f); if (!nrow(x)) return(NULL)
  x[, symbol := sub("\\.csv$", "", basename(f))]; x
}), fill = TRUE)
dt[, date := as.IDate(substr(as.character(time), 1, 10))]
dt <- dt[date >= as.IDate("2024-10-01") & date <= as.IDate("2026-09-23")]
setkey(dt, symbol, date)
# vnstock prices are in thousand VND
dt[, `:=`(ret = log(close / shift(close)), prev_close = shift(close)), by = symbol]
dt[, value_bn := close * 1000 * volume / 1e9]              # trading value, VND billion
dt[, illiq := fifelse(value_bn > 0, abs(ret) / value_bn, NA_real_)]
# Corwin-Schultz (2012) two-day high-low spread
dt[, `:=`(hl = log(high / low)^2, h2 = pmax(high, shift(high)), l2 = pmin(low, shift(low))), by = symbol]
dt[, beta_cs := hl + shift(hl), by = symbol]
dt[, gamma_cs := log(h2 / l2)^2]
k <- 3 - 2 * sqrt(2)
dt[, alpha_cs := (sqrt(2 * beta_cs) - sqrt(beta_cs)) / k - sqrt(gamma_cs / k)]
dt[, cs_spread := pmax(0, 2 * (exp(alpha_cs) - 1) / (1 + exp(alpha_cs)))]
dt <- dt[!is.na(ret)]

# ---------------------------------------------------------------- sample filters
pre <- dt[date < D_ANN]
elig <- pre[, .(n_pre = .N, zero_share = mean(volume == 0), px = median(close),
                lval_pre = mean(log1p(value_bn)), vol_pre = sd(ret, na.rm = TRUE)), by = symbol]
keep <- elig[n_pre >= 200 & zero_share < 0.2 & px >= 1]$symbol
dropped_treated <- setdiff(treated27, keep)
dt <- dt[symbol %in% keep]
dt[, treated := as.integer(symbol %in% treated27)]
dt[, near := as.integer(symbol %in% nearmiss)]

# winsorize daily measures cross-sectionally at 1/99 by date
wins <- function(x, p = 0.01) { q <- quantile(x, c(p, 1 - p), na.rm = TRUE); pmin(pmax(x, q[1]), q[2]) }
dt[, `:=`(illiq_w = wins(illiq), cs_w = wins(cs_spread)), by = date]

# ---------------------------------------------------------------- weekly panel
dt[, week := as.IDate(cut(as.Date(date), "week"))]
wk <- dt[, .(amihud = mean(illiq_w, na.rm = TRUE), lval = log(sum(value_bn) + 1e-6),
             cs = mean(cs_w, na.rm = TRUE), absret = mean(abs(ret)), ndays = .N),
         by = .(symbol, week, treated, near)]
wk <- wk[ndays >= 3 & is.finite(amihud) & amihud > 0]
wk[, lamihud := log(amihud)]
wk[, period := fcase(week < D_ANN, "P0_pre",
                     week < D_CONF, "P1_announce",
                     week < D_LIST, "P2_confirm",
                     default = "P3_list_rebal")]
wk[, `:=`(P1 = as.integer(period == "P1_announce"), P2 = as.integer(period == "P2_confirm"),
          P3 = as.integer(period == "P3_list_rebal"))]
# month relative to announcement month (Oct 2025 = 0)
wk[, relm := (year(week) - 2025) * 12 + month(week) - 10]

# ---------------------------------------------------------------- matched control sample
mdat <- elig[symbol %in% keep & !(symbol %in% nearmiss)]
mdat[, treated := as.integer(symbol %in% treated27)]
m <- matchit(treated ~ lval_pre + log(px) + vol_pre, data = mdat, method = "nearest",
             ratio = 3, replace = TRUE, distance = "glm")
md <- as.data.table(match.data(m))
matched_syms <- md$symbol
bal <- summary(m)$sum.matched

# ---------------------------------------------------------------- descriptive table
desc <- wk[period == "P0_pre", .(amihud = mean(amihud), lval = mean(lval), cs = mean(cs) * 100,
                                 absret = mean(absret) * 100), by = .(group = fcase(treated == 1, "FTSE constituents",
                                                                               near == 1, "Near-miss", default = "Other HOSE"))]
nstocks <- wk[, .(n = uniqueN(symbol)), by = .(group = fcase(treated == 1, "FTSE constituents",
                                                             near == 1, "Near-miss", default = "Other HOSE"))]
desc <- merge(desc, nstocks, by = "group")
fwrite(desc, "output/table1_descriptives.csv")

# ---------------------------------------------------------------- baseline DiD
base <- wk[near == 0]
est <- function(dat, y) feols(as.formula(paste(y, "~ treated:P1 + treated:P2 + treated:P3 | symbol + week")),
                              data = dat, cluster = ~symbol)
res_full <- list(lamihud = est(base, "lamihud"), lval = est(base, "lval"), cs = est(base, "cs"))
res_match <- list(lamihud = est(base[symbol %in% matched_syms], "lamihud"),
                  lval = est(base[symbol %in% matched_syms], "lval"),
                  cs = est(base[symbol %in% matched_syms], "cs"))

tidy_res <- function(lst, sample) rbindlist(lapply(names(lst), function(y) {
  ct <- coeftable(lst[[y]])
  data.table(sample = sample, outcome = y, term = rownames(ct), est = ct[, 1], se = ct[, 2], p = ct[, 4],
             n = nobs(lst[[y]]), r2w = fitstat(lst[[y]], "wr2")[[1]])
}))
tab2 <- rbind(tidy_res(res_full, "All HOSE"), tidy_res(res_match, "Matched 3:1"))
fwrite(tab2, "output/table2_did.csv")

# ---------------------------------------------------------------- event study (monthly, ref = Sep 2025)
es_dat <- base[symbol %in% matched_syms | treated == 1]
es <- lapply(c("lamihud", "lval", "cs"), function(y)
  feols(as.formula(paste(y, "~ i(relm, treated, ref = -1) | symbol + week")), data = es_dat, cluster = ~symbol))
names(es) <- c("lamihud", "lval", "cs")
es_tab <- rbindlist(lapply(names(es), function(y) {
  ct <- coeftable(es[[y]]); data.table(outcome = y, relm = as.integer(sub(".*::(-?[0-9]+):.*", "\\1", rownames(ct))),
                                       est = ct[, 1], se = ct[, 2], p = ct[, 4])
}))
fwrite(es_tab, "output/table_event_study.csv")
pretest <- lapply(es, function(e) { w <- wald(e, keep = "relm::-[0-9]+:", print = FALSE); c(stat = w$stat, p = w$p) })
fwrite(rbindlist(lapply(names(pretest), function(y) data.table(outcome = y, F = pretest[[y]]["stat"], p = pretest[[y]]["p"]))),
       "output/table_pretrend_wald.csv")

lab <- c(lamihud = "log Amihud illiquidity", lval = "log trading value", cs = "Corwin-Schultz spread")
es_tab[, outcome_lab := lab[outcome]]
es_plot <- rbind(es_tab, data.table(outcome = names(lab), relm = -1L, est = 0, se = 0, p = NA, outcome_lab = lab), fill = TRUE)
g <- ggplot(es_plot, aes(relm, est)) +
  geom_hline(yintercept = 0, colour = "grey50") +
  geom_vline(xintercept = c(-0.5, 5.5, 9.5), linetype = "dashed", colour = "grey40") +
  geom_pointrange(aes(ymin = est - 1.96 * se, ymax = est + 1.96 * se), size = 0.25) +
  facet_wrap(~outcome_lab, ncol = 1, scales = "free_y") +
  labs(x = "Months relative to the upgrade announcement (October 2025 = 0)", y = "Coefficient (95% CI)") +
  theme_bw(base_size = 10)
ggsave("output/figure1_event_study.png", g, width = 6.5, height = 7, dpi = 300)

# ---------------------------------------------------------------- rebalancing-day volume spike (daily)
dd <- dt[symbol %in% c(matched_syms, treated27) & near == 0 & date >= D_LIST - 60]
dd[, lval_d := log(value_bn + 1e-6)]
dd[, lval_bench := mean(lval_d[date < D_LIST - 5]), by = symbol]
dd[, abn_lval := lval_d - lval_bench]
reb <- dd[date >= D_REB - 5 & date <= as.IDate("2026-09-23"),
          .(abn = mean(abn_lval), se = sd(abn_lval) / sqrt(.N), n = .N), by = .(date, treated)]
fwrite(reb, "output/table_rebalance_days.csv")
tdays <- sort(unique(dd$date)); reb_idx <- match(D_REB, tdays)
dd[, rel := match(date, tdays) - reb_idx]            # trading days relative to rebalancing session
ref_rel <- match(max(tdays[tdays < D_LIST]), tdays) - reb_idx  # last session before the list announcement
reb_reg <- feols(lval_d ~ i(rel, treated, ref = ref_rel) | symbol + date,
                 data = dd[rel >= ref_rel - 10], cluster = ~symbol)
rct <- coeftable(reb_reg); fwrite(data.table(term = rownames(rct), rct), "output/table_rebalance_reg.csv")

# ---------------------------------------------------------------- robustness
rob <- list()
# (1) size-tercile x week FE
base[, size3 := as.integer(cut(rank(ave(lval, symbol, FUN = mean)) / .N, c(0, 1/3, 2/3, 1)))]
szmap <- elig[, .(symbol, szq = cut(lval_pre, quantile(lval_pre, c(0, 1/3, 2/3, 1)), include.lowest = TRUE, labels = FALSE))]
base <- merge(base, szmap, by = "symbol")
rob$size_week_fe <- feols(lamihud ~ treated:P1 + treated:P2 + treated:P3 | symbol + week^szq, data = base, cluster = ~symbol)
# (2) two-way clustering
rob$twoway_cluster <- feols(lamihud ~ treated:P1 + treated:P2 + treated:P3 | symbol + week, data = base, cluster = ~symbol + week)
# (3) exclude banks-heavy? leave-one-out max influence: drop VIC and VHM
rob$drop_vin <- feols(lamihud ~ treated:P1 + treated:P2 + treated:P3 | symbol + week, data = base[!symbol %in% c("VIC", "VHM", "VRE", "VPL")], cluster = ~symbol)
# (4) placebo: fake announcement one year earlier (Oct 2024 not available -> use Apr 2025 within pre-period)
pl <- base[week < D_ANN]; pl[, fake := as.integer(week >= as.IDate("2025-04-07"))]
rob$placebo_apr2025 <- feols(lamihud ~ treated:fake | symbol + week, data = pl, cluster = ~symbol)
# (5) near-miss stocks as the treated group vs other HOSE
nm <- wk[treated == 0]
rob$nearmiss <- feols(lamihud ~ near:P1 + near:P2 + near:P3 | symbol + week, data = nm, cluster = ~symbol)
# (6) treated-specific linear trend (identifies deviations from the pre-existing trend)
base[, tindex := as.integer(factor(week))]
rob$treated_trend <- feols(lamihud ~ treated:P1 + treated:P2 + treated:P3 + treated:tindex | symbol + week,
                           data = base, cluster = ~symbol)
rob$treated_trend_lval <- feols(lval ~ treated:P1 + treated:P2 + treated:P3 + treated:tindex | symbol + week,
                                data = base, cluster = ~symbol)
# (7) matched sample with treated-specific trend
rob$matched_trend <- feols(lamihud ~ treated:P1 + treated:P2 + treated:P3 + treated:tindex | symbol + week,
                           data = base[symbol %in% matched_syms], cluster = ~symbol)
rob_tab <- rbindlist(lapply(names(rob), function(nm_) { ct <- coeftable(rob[[nm_]])
  data.table(spec = nm_, term = rownames(ct), est = ct[, 1], se = ct[, 2], p = ct[, 4], n = nobs(rob[[nm_]])) }))
fwrite(rob_tab, "output/table3_robustness.csv")

# ---------------------------------------------------------------- bookkeeping
sink("output/run_summary.txt")
cat("Stocks kept:", uniqueN(wk$symbol), " treated:", uniqueN(wk[treated == 1]$symbol),
    " near-miss:", uniqueN(wk[near == 1]$symbol), " matched controls:", length(setdiff(matched_syms, treated27)), "\n")
cat("Treated dropped by filters:", paste(dropped_treated, collapse = ", "), "\n")
cat("Weeks:", uniqueN(wk$week), " first:", as.character(min(wk$week)), " last:", as.character(max(wk$week)), "\n")
cat("Stock-weeks:", nrow(wk), "\n\nMatching balance (matched sample):\n"); print(round(bal[, 1:4], 3))
cat("\nBaseline DiD (All HOSE):\n"); etable(res_full)
cat("\nBaseline DiD (Matched):\n"); etable(res_match)
cat("\nPre-trend Wald tests:\n"); print(pretest)
cat("\nRobustness:\n"); etable(rob)
cat("\nRebalancing days:\n"); print(reb)
sink()
cat("DONE\n")

# ================================================================ FRAMING A: eligibility-attention (two treated groups)
# included = final FTSE constituents; nearmiss = named on FTSE eligibility lists but not included
wk2 <- copy(wk)
wk2[, grp := fcase(treated == 1, "included", near == 1, "nearmiss", default = "control")]
fa <- lapply(c("lamihud", "lval", "cs"), function(y)
  feols(as.formula(paste(y, "~ treated:P1 + treated:P2 + treated:P3 + near:P1 + near:P2 + near:P3 | symbol + week")),
        data = wk2, cluster = ~symbol))
names(fa) <- c("lamihud", "lval", "cs")
fa_tab <- rbindlist(lapply(names(fa), function(y) { ct <- coeftable(fa[[y]])
  data.table(outcome = y, term = rownames(ct), est = ct[, 1], se = ct[, 2], p = ct[, 4], n = nobs(fa[[y]])) }))
# included minus near-miss, per period (Wald on linear combination)
diffs <- rbindlist(lapply(names(fa), function(y) rbindlist(lapply(1:3, function(k) {
  b <- coef(fa[[y]]); V <- vcov(fa[[y]])
  a <- paste0("treated:P", k); n <- paste0("P", k, ":near")
  d <- b[a] - b[n]; se <- sqrt(V[a, a] + V[n, n] - 2 * V[a, n])
  data.table(outcome = y, period = paste0("P", k), included_minus_nearmiss = d, se = se, p = 2 * pnorm(-abs(d / se)))
}))))
fwrite(fa_tab, "output/table4_two_groups.csv"); fwrite(diffs, "output/table4b_included_minus_nearmiss.csv")

# near-miss on rebalancing days (falsification of price pressure: should show no spike)
dd2 <- dt[date >= D_LIST - 60]
dd2[, lval_d := log(value_bn + 1e-6)]
dd2[, lval_bench := mean(lval_d[date < D_LIST - 5]), by = symbol]
dd2[, abn_lval := lval_d - lval_bench]
dd2[, grp := fcase(treated == 1, "included", near == 1, "nearmiss", symbol %in% matched_syms, "matched_control", default = "other")]
reb2 <- dd2[date >= D_REB - 5 & grp != "other", .(abn = mean(abn_lval), se = sd(abn_lval) / sqrt(.N), n = .N), by = .(date, grp)]
fwrite(reb2[order(grp, date)], "output/table5_rebalance_by_group.csv")

# event study with both groups (monthly)
es2 <- lapply(c("lamihud", "lval"), function(y)
  feols(as.formula(paste(y, "~ i(relm, treated, ref = -1) + i(relm, near, ref = -1) | symbol + week")), data = wk2, cluster = ~symbol))
names(es2) <- c("lamihud", "lval")
es2_tab <- rbindlist(lapply(names(es2), function(y) { ct <- coeftable(es2[[y]])
  data.table(outcome = y, term = rownames(ct), est = ct[, 1], se = ct[, 2], p = ct[, 4]) }))
es2_tab[, group := fifelse(grepl(":near", term), "nearmiss", "included")]
es2_tab[, relm := as.integer(sub(".*::(-?[0-9]+):.*", "\\1", term))]
fwrite(es2_tab, "output/table_event_study_two_groups.csv")
g2 <- ggplot(rbind(es2_tab, data.table(outcome = rep(c("lamihud","lval"), 2), group = rep(c("included","nearmiss"), each = 2), relm = -1L, est = 0, se = 0), fill = TRUE),
             aes(relm, est, colour = group, shape = group)) +
  geom_hline(yintercept = 0, colour = "grey50") +
  geom_vline(xintercept = c(-0.5, 5.5, 9.5), linetype = "dashed", colour = "grey40") +
  geom_pointrange(aes(ymin = est - 1.96 * se, ymax = est + 1.96 * se), size = 0.25, position = position_dodge(width = 0.5)) +
  facet_wrap(~ factor(outcome, labels = c("log Amihud illiquidity", "log trading value")), ncol = 1, scales = "free_y") +
  scale_colour_manual(values = c(included = "#1b6ca8", nearmiss = "#d95f02")) +
  labs(x = "Months relative to the upgrade announcement (October 2025 = 0)", y = "Coefficient vs other HOSE stocks (95% CI)", colour = NULL, shape = NULL) +
  theme_bw(base_size = 10) + theme(legend.position = "bottom")
ggsave("output/figure2_event_study_two_groups.png", g2, width = 6.5, height = 7, dpi = 300)

# descriptive table by group, pre-period
desc2 <- wk2[period == "P0_pre", .(stocks = uniqueN(symbol), stock_weeks = .N, amihud = mean(amihud), lval = mean(lval),
                                   cs_pct = mean(cs) * 100, absret_pct = mean(absret) * 100), by = grp]
fwrite(desc2, "output/table1b_descriptives_by_group.csv")
sink("output/run_summary_framingA.txt")
cat("Two-group DiD (vs other HOSE):\n"); etable(fa)
cat("\nIncluded minus near-miss:\n"); print(diffs)
cat("\nRebalancing window by group:\n"); print(reb2[order(grp, date)])
cat("\nPre-period descriptives by group:\n"); print(desc2)
cat("\nNear-miss symbols present:", paste(sort(unique(wk2[near == 1]$symbol)), collapse = ", "), "\n")
sink()

# ================================================================ randomization inference (few treated clusters)
# Pseudo-treated groups drawn from control stocks in the top pre-period trading-value tercile.
set.seed(20260924)
pool <- elig[symbol %in% unique(wk2[grp == "control"]$symbol)]
pool <- pool[lval_pre >= quantile(elig[symbol %in% keep]$lval_pre, 2/3)]$symbol
ctrl_only <- wk2[grp == "control"]
ri_stat <- function(pseudo) {
  d <- copy(ctrl_only); d[, ps := as.integer(symbol %in% pseudo)]
  b <- coef(feols(lamihud ~ ps:P1 + ps:P2 + ps:P3 | symbol + week, data = d, notes = FALSE, warn = FALSE))
  unname(b)
}
R <- 500
ri5  <- t(replicate(R, ri_stat(sample(pool, 5))))
ri24 <- t(replicate(R, ri_stat(sample(pool, min(24, length(pool))))))
obs_near <- unname(coef(fa$lamihud)[c("P1:near", "P2:near", "P3:near")])
obs_inc  <- unname(coef(fa$lamihud)[c("treated:P1", "treated:P2", "treated:P3")])
ri <- data.table(group = rep(c("nearmiss (k=5)", "included (k=24)"), each = 3), period = rep(paste0("P", 1:3), 2),
                 observed = c(obs_near, obs_inc),
                 p_one_sided = c(sapply(1:3, function(j) mean(ri5[, j] <= obs_near[j])), sapply(1:3, function(j) mean(ri24[, j] <= obs_inc[j]))),
                 pseudo_mean = c(colMeans(ri5), colMeans(ri24)), pseudo_p05 = c(apply(ri5, 2, quantile, .05), apply(ri24, 2, quantile, .05)),
                 pool_size = length(pool), reps = R)
fwrite(ri, "output/table6_randomization_inference.csv"); print(ri)

# ================================================================ heterogeneity by FTSE size segment (announced 21 Aug 2026)
seg <- data.table(symbol = c("VCB","VIC","VHM","BID","VPB","HPG"), segment = c(rep("large", 3), rep("mid", 3)))
wk3 <- merge(wk2, seg, by = "symbol", all.x = TRUE)
wk3[treated == 1 & is.na(segment), segment := "small"]
for (g in c("large", "mid", "small")) wk3[, (paste0("seg_", g)) := as.integer(segment %in% g & treated == 1)]
het <- lapply(c("lamihud", "lval"), function(y) feols(as.formula(paste(y,
  "~ seg_large:P1 + seg_large:P2 + seg_large:P3 + seg_mid:P1 + seg_mid:P2 + seg_mid:P3 + seg_small:P1 + seg_small:P2 + seg_small:P3 + near:P1 + near:P2 + near:P3 | symbol + week")),
  data = wk3, cluster = ~symbol))
names(het) <- c("lamihud", "lval")
het_tab <- rbindlist(lapply(names(het), function(y) { ct <- coeftable(het[[y]])
  data.table(outcome = y, term = rownames(ct), est = ct[, 1], se = ct[, 2], p = ct[, 4]) }))
fwrite(het_tab, "output/table7_segment_heterogeneity.csv")
# rebalancing-day abnormal value by segment
dd3 <- merge(dd2, seg, by = "symbol", all.x = TRUE); dd3[treated == 1 & is.na(segment), segment := "small"]
reb3 <- dd3[date == D_REB & treated == 1, .(abn = mean(abn_lval), se = sd(abn_lval) / sqrt(.N), n = .N), by = segment]
fwrite(reb3, "output/table7b_rebalance_by_segment.csv")
# matching balance table (before and after)
bal_all <- summary(m, un = TRUE)
bal_out <- data.table(variable = rownames(bal_all$sum.all), treated_mean = bal_all$sum.all[, 1], control_mean_all = bal_all$sum.all[, 2],
                      smd_all = bal_all$sum.all[, 3], control_mean_matched = bal_all$sum.matched[, 2], smd_matched = bal_all$sum.matched[, 3])
fwrite(bal_out, "output/table_matching_balance.csv")
sink("output/run_summary_heterogeneity.txt"); etable(het); print(reb3); print(bal_out); cat("segment counts:\n"); print(unique(wk3[treated == 1, .(symbol, segment)])[, .N, by = segment]); sink()
