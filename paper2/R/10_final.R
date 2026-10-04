suppressPackageStartupMessages(library(ggplot2))
source("/home/user/Black_litterman_2/paper2/R/lib.R")
root <- "/home/user/Black_litterman_2/paper2"; od <- file.path(root, "output"); fd <- file.path(od, "figures")
res <- readRDS(file.path(od, "rds/main_engine.rds")); tr <- readRDS(file.path(od, "rds/trials.rds")); ts <- readRDS(file.path(od, "rds/trials_sens.rds"))
ex <- res$ret - res$rf_m
# DSR with the FULL trial ledger: 8 family variants + all KMV sensitivity configurations (excluding the baseline duplicate)
fam <- tr$family; sr_fam <- sapply(fam, function(m) mean(ex[, m]) / sd(ex[, m]))
sens_m <- (ts$kmv_sensitivity_sharpes[-1]) / sqrt(12)                       # annualised -> monthly
sr_all <- c(sr_fam, sens_m); n_tr <- length(sr_all)
dfull <- do.call(rbind, lapply(c("KMV", "KMV_TC", "KMV_rawq", "EW", "ERC"), function(m) { d <- dsr(ex[, m], n_tr, var(sr_all))
  data.frame(model = m, sr_ann = ann_sharpe(ex[, m]), psr0 = psr(ex[, m], 0), dsr = d$dsr, sr_star_ann = d$sr_star_monthly * sqrt(12), n_trials = n_tr) }))
write.csv(dfull, file.path(od, "tables/T3d_dsr_full_ledger.csv"), row.names = FALSE); print(dfull, digits = 3)
# distribution diagnostics (Appendix)
jb <- function(x) { n <- length(x); z <- (x - mean(x)) / sd(x) * sqrt(n / (n - 1)); s <- mean(z^3); k <- mean(z^4) - 3; stat <- n * (s^2 / 6 + k^2 / 24)
  c(skew = s, exkurt = k, jb = stat, p_jb = pchisq(stat, 2, lower.tail = FALSE)) }
A2 <- do.call(rbind, lapply(res$models, function(m) { x <- res$ret[, m]; lb <- Box.test(x, lag = 5, type = "Ljung-Box"); data.frame(model = m, t(jb(x)), lb_q5 = unname(lb$statistic), p_lb5 = lb$p.value) }))
write.csv(A2, file.path(od, "tables/T_A2_distribution.csv"), row.names = FALSE)
# fallback / constraint diagnostics: how often is the cap binding, how often min-var fallback
Wk <- res$W$KMV; cat("KMV: share of months with any weight at cap:", mean(apply(Wk, 1, max) >= 0.2999), " mean max weight:", mean(apply(Wk, 1, max)), "\n")
# simulation figure
f <- file.path(od, "tables/T8_simulation.csv")
if (file.exists(f)) {
  sm <- read.csv(f); labm <- c(MKT = "Cap-weighted", TAN_LW = "Tangency (LW)", ERC = "ERC", KIO_v1 = "Single-view BL-K_IO", KMV = "BL-KMV (main)")
  sm <- sm[sm$model != "EW", ]; sm$model <- labm[sm$model]; sm$s <- factor(sm$s, labels = c("No alpha (null)", "Moderate alpha", "Strong alpha"))
  oi <- c("#E69F00", "#56B4E9", "#009E73", "#D55E00", "#0072B2")
  th <- theme_minimal(base_size = 10) + theme(legend.position = "bottom", legend.title = element_blank(), panel.grid.minor = element_blank())
  g1 <- ggplot(sm, aes(model, mean_d_vs_EW, fill = model)) + geom_col() + facet_wrap(~s) + scale_fill_manual(values = oi) + labs(x = NULL, y = "Mean Sharpe difference vs 1/N") + th + theme(axis.text.x = element_blank())
  ggsave(file.path(fd, "F8a_sim_delta.png"), g1, width = 7, height = 3.2, dpi = 300, bg = "white")
  g2 <- ggplot(sm, aes(model, reject_pos, fill = model)) + geom_col() + facet_wrap(~s) + scale_fill_manual(values = oi) + labs(x = NULL, y = "Rate: significant (5%) and positive vs 1/N") + th + theme(axis.text.x = element_blank())
  ggsave(file.path(fd, "F8b_sim_power.png"), g2, width = 7, height = 3.2, dpi = 300, bg = "white") }
# broad figure
b <- readRDS(file.path(od, "rds/broad.rds")); wb <- do.call(rbind, lapply(colnames(b$ret), function(m) data.frame(date = b$dates, model = m, v = cumprod(1 + b$ret[, m]))))
g3 <- ggplot(wb, aes(date, v, colour = model)) + geom_line(linewidth = 0.6) + scale_colour_manual(values = c("#000000", "#E69F00", "#56B4E9", "#009E73", "#D55E00", "#0072B2", "#CC79A7")) +
  labs(x = NULL, y = "Wealth (start = 1)") + theme_minimal(base_size = 10) + theme(legend.position = "bottom", legend.title = element_blank())
ggsave(file.path(fd, "F10_broad_wealth.png"), g3, width = 7, height = 3.4, dpi = 300, bg = "white")
cat("final done\n")
# cross-sectional structure of the bank panel (for the discussion)
P <- readRDS(file.path(od, "rds/panel.rds")); Rm <- P$R[39:144, ]
cm <- cor(Rm, use = "pairwise.complete.obs"); cat("mean pairwise corr (OOS months):", mean(cm[upper.tri(cm)]), "\n")
disp <- apply(Rm, 1, sd, na.rm = TRUE); cat("mean cross-sectional sd of monthly returns:", mean(disp), "\n")
saveRDS(list(mean_corr = mean(cm[upper.tri(cm)]), mean_xs_sd = mean(disp)), file.path(od, "rds/structure.rds"))

# risk-free sensitivity: Sharpe with the rate halved and set to zero
rfs <- do.call(rbind, lapply(c(1, 0.5, 0), function(mult) { rfm2 <- ((1 + res$rf_ann * mult)^(1/12) - 1)
  data.frame(rf_multiplier = mult, model = res$models, sharpe = apply(res$ret - rfm2, 2, ann_sharpe)) }))
write.csv(rfs, file.path(od, "tables/T11_rf_sensitivity.csv"), row.names = FALSE)
rk <- sapply(c(1, 0.5, 0), function(mult) { x <- rfs$sharpe[rfs$rf_multiplier == mult]; names(x) <- rfs$model[rfs$rf_multiplier == mult]; names(sort(x, decreasing = TRUE)) })
write.csv(rk, file.path(od, "tables/T11b_rf_rankings.csv"), row.names = FALSE); print(rk[1:8, ])
