# 22_attribution.R -- Paper B: variance attribution of Sharpe ratios across the 80-cell factorial, block-bootstrap uncertainty
suppressPackageStartupMessages(library(ggplot2))
source("/home/user/Black_litterman_2/paper2/R/20_factorial.R")
root <- "/home/user/Black_litterman_2/paper2"; od <- file.path(root, "output"); set.seed(20261004); B <- 2000; NPERM <- 5000
fac <- CELLS[, c("anchor", "view", "cov", "cap")]; for (j in names(fac)) fac[[j]] <- factor(fac[[j]], levels = unique(fac[[j]]))
X <- model.matrix(~ (anchor + view + cov + cap)^2, fac)
asg <- attr(X, "assign"); tn <- attr(terms(~ (anchor + view + cov + cap)^2), "term.labels")
qrX <- qr(X)
shares <- function(y) { yc <- y - mean(y); eff <- qr.qty(qrX, yc); ss <- tapply(eff[1:qrX$rank]^2, asg[qrX$pivot][1:qrX$rank], sum)
  ss0 <- setNames(rep(0, length(tn)), tn); ss0[as.integer(names(ss)[names(ss) != "0"])] <- ss[names(ss) != "0"]
  tot <- sum(yc^2); main <- ss0[1:4] / tot; two <- sum(ss0[5:length(tn)]) / tot
  c(setNames(main, c("anchor", "view", "cov", "cap")), twoway = two, higher = 1 - sum(main) - two) }
lev_means <- function(y) unlist(lapply(names(fac), function(f) tapply(y, fac[[f]], mean)))
contr_names <- function() unlist(lapply(names(fac), function(f) { l <- levels(fac[[f]]); if (length(l) < 2) return(NULL); cb <- combn(l, 2); paste0(f, ":", cb[2, ], " - ", cb[1, ]) }))
contr <- function(y) { lm_ <- lapply(names(fac), function(f) tapply(y, fac[[f]], mean)); unlist(lapply(lm_, function(m) { cb <- combn(names(m), 2); m[cb[2, ]] - m[cb[1, ]] })) }
cbi <- function(Tn, b) { nb <- ceiling(Tn / b); st <- sample.int(Tn, nb, replace = TRUE); (as.vector(sapply(st, function(s) ((s - 1 + 0:(b - 1)) %% Tn) + 1)))[1:Tn] }
srfun <- function(E, ann) colMeans(E) / apply(E, 2, sd) * sqrt(ann)
analyse <- function(u, rds, ann, cost = 0.0025) {
  fb <- readRDS(file.path(od, "rds", rds)); ids <- CELLS$id; E <- fb$ret[, ids] - fb$rf_m; Tn <- nrow(E); b <- max(2, round(Tn^(1/3)))
  TV <- ifelse(is.na(fb$turnover[, ids]), 0, fb$turnover[, ids]); En <- E - cost * TV
  sr <- srfun(E, ann); srn <- srfun(En, ann)
  cells <- data.frame(CELLS[, c("anchor", "view", "cov", "cap", "id")], sharpe = sr, sharpe_net25 = srn, ann_ret = colMeans(fb$ret[, ids]) * ann,
    mdd = apply(fb$ret[, ids], 2, max_dd), turnover = colMeans(TV), row.names = NULL)
  write.csv(cells, file.path(od, paste0("tables/B1_cells_", u, ".csv")), row.names = FALSE)
  s0 <- shares(sr); s0n <- shares(srn); l0 <- lev_means(sr); c0 <- contr(sr)
  Sb <- matrix(NA, B, length(s0)); Sbn <- Sb; Lb <- matrix(NA, B, length(l0)); Cb <- matrix(NA, B, length(c0))
  for (i in 1:B) { ix <- cbi(Tn, b); srb <- srfun(E[ix, ], ann); Sb[i, ] <- shares(srb); Lb[i, ] <- lev_means(srb); Cb[i, ] <- contr(srb)
    Sbn[i, ] <- shares(srfun(En[ix, ], ann)) }
  perm <- t(replicate(NPERM, shares(sample(sr))))
  sh <- data.frame(universe = u, component = names(s0), share = s0, lo = apply(Sb, 2, quantile, 0.025), hi = apply(Sb, 2, quantile, 0.975),
    perm95 = apply(perm, 2, quantile, 0.95), perm_mean = colMeans(perm), p_perm = sapply(seq_along(s0), function(j) (1 + sum(perm[, j] >= s0[j])) / (1 + NPERM)),
    share_net25 = s0n, lo_net = apply(Sbn, 2, quantile, 0.025), hi_net = apply(Sbn, 2, quantile, 0.975))
  write.csv(sh, file.path(od, paste0("tables/B2_shares_", u, ".csv")), row.names = FALSE)
  mg <- data.frame(universe = u, level = names(l0), mean_sharpe = l0, lo = apply(Lb, 2, quantile, 0.025), hi = apply(Lb, 2, quantile, 0.975))
  write.csv(mg, file.path(od, paste0("tables/B3_marginal_", u, ".csv")), row.names = FALSE)
  cn <- contr_names(); pb <- sapply(seq_along(c0), function(j) { d <- Cb[, j]; 2 * min((1 + sum(d <= 0)) / (B + 1), (1 + sum(d >= 0)) / (B + 1)) })
  ct <- data.frame(universe = u, contrast = cn, diff = c0, lo = apply(Cb, 2, quantile, 0.025), hi = apply(Cb, 2, quantile, 0.975), p_boot = pmin(1, pb))
  ct$p_holm <- p.adjust(ct$p_boot, "holm"); write.csv(ct, file.path(od, paste0("tables/B4_contrasts_", u, ".csv")), row.names = FALSE)
  # H3 equivalence: view minus NONE, 90% CI vs +-0.10
  vi <- grep("^view:.* - NONE$", cn); eq <- data.frame(universe = u, contrast = cn[vi], diff = c0[vi], lo90 = apply(Cb[, vi, drop = FALSE], 2, quantile, 0.05), hi90 = apply(Cb[, vi, drop = FALSE], 2, quantile, 0.95))
  eq$equivalent_pm0.10 <- eq$lo90 > -0.10 & eq$hi90 < 0.10; write.csv(eq, file.path(od, paste0("tables/B5_equivalence_views_", u, ".csv")), row.names = FALSE)
  refs <- grep("^REF_", fb$ids, value = TRUE); Er <- fb$ret[, refs] - fb$rf_m
  rr <- data.frame(universe = u, ref = refs, sharpe = srfun(Er, ann)); write.csv(rr, file.path(od, paste0("tables/B6_refs_", u, ".csv")), row.names = FALSE)
  list(cells = cells, shares = sh, marg = mg, contr = ct, eq = eq, refs = rr, T = Tn, b = b)
}
rb <- analyse("banks", "factorial_banks.rds", 12); rw <- analyse("broad", "factorial_broad.rds", 52)
saveRDS(list(banks = rb, broad = rw), file.path(od, "rds/attribution.rds"))
options(width = 220); for (r in list(rb, rw)) { cat("\n=== T =", r$T, "\n"); print(r$shares[, c("component", "share", "lo", "hi", "perm95", "p_perm", "share_net25")], digits = 3)
  print(r$marg, digits = 3); print(head(r$contr[order(r$contr$p_boot), ], 12), digits = 3); print(r$eq, digits = 3); print(r$refs, digits = 3) }
