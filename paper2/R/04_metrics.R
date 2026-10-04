source("/home/user/Black_litterman_2/paper2/R/lib.R")
root <- "/home/user/Black_litterman_2/paper2"; od <- file.path(root, "output")
P <- readRDS(file.path(od, "rds/panel.rds")); res <- readRDS(file.path(od, "rds/main_engine.rds"))
set.seed(20261004)
ret <- res$ret; rfm <- res$rf_m; dts <- res$dates; ex <- ret - rfm
i2 <- which(dts >= as.Date("2022-01-01")); i1 <- setdiff(seq_along(dts), i2)
periods <- list(Full = seq_along(dts), P1 = i1, P2 = i2)
lab <- c(EW = "1/N", MKT = "Cap-weighted (MKT)", TAN = "Tangency, sample", TAN_LW = "Tangency, LW", MVP_LW = "Min-variance, LW",
         ERC = "Equal risk contribution", HRP = "Hierarchical risk parity", BL0 = "Inverse BL, no view", MOM_EW = "Top-cluster 1/N (signal only)",
         KIO_v1 = "Single-view BL-K_IO (re-implemented)", KMV = "BL-KMV (main)", KMV_k4 = "BL-KMV, k = 4", KMV_ic = "BL-KMV, k by inner IC",
         KMV_sampleS = "BL-KMV, sample covariance", KMV_single = "BL-KMV, single view", KMV_rawq = "BL-KMV, uncalibrated q",
         KMV_nostab = "BL-KMV, no stability in Omega", KMV_TC = "BL-KMV-TC (turnover-aware)")
enb <- function(W) { h <- rowSums(W^2); mean(1 / h) }
perf <- function(idx, m) {
  r <- ret[idx, m]; e <- ex[idx, m]
  c(ann_ret = mean(r) * 12, ann_vol = sd(r) * sqrt(12), sharpe = ann_sharpe(e), sortino = sortino(e), mdd = max_dd(r),
    cvar95 = cvar95(r), ceq5 = ceq(r, 5), turnover = mean(res$turnover[idx, m], na.rm = TRUE), enb = enb(res$W[[m]][idx, , drop = FALSE]),
    sr_net25 = ann_sharpe(e - 0.0025 * ifelse(is.na(res$turnover[idx, m]), 0, res$turnover[idx, m])),
    sr_net50 = ann_sharpe(e - 0.0050 * ifelse(is.na(res$turnover[idx, m]), 0, res$turnover[idx, m])))
}
T1 <- do.call(rbind, lapply(names(periods), function(pn) { M <- t(sapply(res$models, function(m) perf(periods[[pn]], m)))
  data.frame(period = pn, model = res$models, label = lab[res$models], M, row.names = NULL) }))
write.csv(T1, file.path(od, "tables/T1_performance.csv"), row.names = FALSE)

# ---- Sharpe-difference tests: main model vs each benchmark; B = 5000
bench <- c("EW", "MKT", "TAN_LW", "MVP_LW", "ERC", "HRP", "BL0", "KIO_v1")
T2 <- do.call(rbind, lapply(names(periods), function(pn) do.call(rbind, lapply(bench, function(b) {
  idx <- periods[[pn]]; o <- sr_diff_test(ex[idx, "KMV"], ex[idx, b], B = 5000)
  data.frame(period = pn, vs = b, diff_ann = o["diff_ann"], t = o["t"], p_boot = o["p_boot"], p_asym = o["p_asym"], T = length(idx)) }))))
rownames(T2) <- NULL; write.csv(T2, file.path(od, "tables/T2_sharpe_tests_KMV.csv"), row.names = FALSE)
# turnover-aware variant vs 1/N and ERC, and KIO_v1 vs EW (the earlier single-view design)
T2b <- do.call(rbind, lapply(names(periods), function(pn) do.call(rbind, lapply(list(c("KMV_TC", "EW"), c("KMV_TC", "ERC"), c("KIO_v1", "EW"), c("KMV_rawq", "EW"), c("ERC", "EW")), function(pr) {
  idx <- periods[[pn]]; o <- sr_diff_test(ex[idx, pr[1]], ex[idx, pr[2]], B = 5000)
  data.frame(period = pn, a = pr[1], b = pr[2], diff_ann = o["diff_ann"], t = o["t"], p_boot = o["p_boot"], p_asym = o["p_asym"]) }))))
rownames(T2b) <- NULL; write.csv(T2b, file.path(od, "tables/T2b_sharpe_tests_other.csv"), row.names = FALSE)

# ---- minimum detectable Sharpe difference (power): se of difference between KMV and EW
se_tab <- do.call(rbind, lapply(names(periods), function(pn) { idx <- periods[[pn]]; o <- sr_diff_stat(ex[idx, "KMV"], ex[idx, "EW"])
  data.frame(period = pn, T = length(idx), se_ann = o["se"] * sqrt(12), mde80_ann = 2.8 * o["se"] * sqrt(12)) }))
write.csv(se_tab, file.path(od, "tables/T2c_power_mde.csv"), row.names = FALSE)

# ---- multiple testing: trials ledger, DSR, SPA
fam <- c("KMV", "KMV_k4", "KMV_ic", "KMV_sampleS", "KMV_single", "KMV_rawq", "KMV_nostab", "KMV_TC")
sr_m <- sapply(fam, function(m) mean(ex[, m]) / sd(ex[, m]))
trials <- list(family = fam, n_trials = length(fam), sr_var = var(sr_m)); saveRDS(trials, file.path(od, "rds/trials.rds"))
T3 <- do.call(rbind, lapply(res$models, function(m) { d <- dsr(ex[, m], length(fam), var(sr_m))
  data.frame(model = m, sr_ann = ann_sharpe(ex[, m]), psr0 = psr(ex[, m], 0), dsr = d$dsr, sr_star_ann = d$sr_star_monthly * sqrt(12)) }))
write.csv(T3, file.path(od, "tables/T3_dsr.csv"), row.names = FALSE)
u <- function(r) r - 5 / 2 * r^2                     # quadratic utility (gamma = 5), monthly
spa_set <- setdiff(res$models, c("KMV"))
d_spa <- sapply(spa_set, function(m) u(ret[, m]) - u(ret[, "KMV"]))
spa <- do.call(rbind, lapply(names(periods), function(pn) { o <- spa_test(d_spa[periods[[pn]], , drop = FALSE], B = 5000); data.frame(period = pn, t(o)) }))
write.csv(spa, file.path(od, "tables/T3b_spa_main_vs_all.csv"), row.names = FALSE)
# SPA with benchmark EW (does any model beat 1/N?)
d_ew <- sapply(setdiff(res$models, c("EW")), function(m) u(ret[, m]) - u(ret[, "EW"]))
spa2 <- do.call(rbind, lapply(names(periods), function(pn) { o <- spa_test(d_ew[periods[[pn]], , drop = FALSE], B = 5000); data.frame(period = pn, t(o)) }))
write.csv(spa2, file.path(od, "tables/T3c_spa_vs_EW.csv"), row.names = FALSE)

# ---- alpha vs cap-weighted bank market
mk_ex <- res$mkt - rfm
T4 <- do.call(rbind, lapply(names(periods), function(pn) do.call(rbind, lapply(setdiff(res$models, "MKT"), function(m) {
  idx <- periods[[pn]]; data.frame(period = pn, model = m, t(hac_alpha(ex[idx, m], mk_ex[idx]))) }))))
write.csv(T4, file.path(od, "tables/T4_alpha.csv"), row.names = FALSE)

# ---- stress months: worst 12 market months and named episodes
worst <- order(res$mkt)[1:12]
T5 <- data.frame(model = res$models, label = lab[res$models], worst12_mean = colMeans(ret[worst, ]), mkt_worst12_mean = mean(res$mkt[worst]),
  covid_2020_03 = ret["2020-03-31", ], bond_2022_q4 = apply(ret[as.character(dts) >= "2022-10-01" & as.character(dts) <= "2022-12-31", , drop = FALSE], 2, function(x) prod(1 + x) - 1),
  down_capture = sapply(res$models, function(m) mean(ret[res$mkt < 0, m]) / mean(res$mkt[res$mkt < 0])))
write.csv(T5, file.path(od, "tables/T5_stress.csv"), row.names = FALSE)

# ---- signal diagnostics: rank IC of composite score and of cluster ordering
ic_rows <- lapply(res$diag, function(d) d$date)
sig <- do.call(rbind, lapply(seq_along(res$diag), function(i) { t <- res$diag[[i]]$t; ctx <- NULL
  el <- which(colSums(is.na(P$R[(t - 35):t, ])) == 0 & !is.na(P$MC[t, ]))
  mom <- feat_mom(P$R[1:t, el, drop = FALSE], P$mkt[1:t], t, 6); vol <- feat_vol(P$R[1:t, el, drop = FALSE], t, 12); z <- zs(mom) - zs(vol)
  y <- P$R[t + 1, el] - P$mkt[t + 1]
  data.frame(date = P$dates[t + 1], ic_z = cor(z, y, method = "spearman"), ic_mom = cor(mom, y, method = "spearman"),
    ic_vol = cor(-vol, y, method = "spearman"), n = length(el)) }))
sig$k <- sapply(res$diag, function(d) d$k_stab); sig$lambda_t <- sapply(res$diag, function(d) d$lambda_t)
saveRDS(sig, file.path(od, "rds/signal_diag.rds"))
ic_sum <- do.call(rbind, lapply(names(periods), function(pn) { s <- sig[periods[[pn]], ]
  do.call(rbind, lapply(c("ic_z", "ic_mom", "ic_vol"), function(v) { x <- s[[v]]; fit <- lm(x ~ 1); ct <- coeftest(fit, vcov. = NeweyWest(fit, lag = 3, prewhite = FALSE))
    data.frame(period = pn, signal = v, mean_ic = mean(x), t_nw = ct[1, 3], hit = mean(x > 0)) })) }))
write.csv(ic_sum, file.path(od, "tables/T6_signal_ic.csv"), row.names = FALSE)
cat("done\n"); options(width = 200)
print(T1[T1$period == "Full", c("model", "ann_ret", "ann_vol", "sharpe", "mdd", "turnover", "sr_net25")], digits = 3, row.names = FALSE)
print(T1[T1$period == "P2", c("model", "sharpe", "mdd")], digits = 3, row.names = FALSE)
print(T2, digits = 3); print(T2b, digits = 3); print(se_tab); print(spa); print(spa2); print(ic_sum, digits = 3)
print(T3[T3$model %in% fam, ], digits = 3)
