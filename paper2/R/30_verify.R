# 30_verify.R -- integrity verification tests of the analysis code (AI failure mode 1, 3, 5, 6 checks)
source("/home/user/Black_litterman_2/paper2/R/20_factorial.R")
root <- "/home/user/Black_litterman_2/paper2"; od <- file.path(root, "output"); out <- character()
rep_ <- function(...) { s <- paste0(...); cat(s, "\n"); out <<- c(out, s) }
P <- readRDS(file.path(od, "rds/panel.rds")); fb <- readRDS(file.path(od, "rds/factorial_banks.rds"))
set.seed(1)
# T1: weights are valid (sum to 1, non-negative, cap respected) for all cells and steps
chk <- sapply(fb$ids, function(id) { W <- fb$W[[id]]; rs <- rowSums(W); c(sum1 = max(abs(rs - 1)), neg = min(W), over = if (grepl("capped", id)) max(W) - 0.30 else 0) })
rep_("T1 weights: max |sum-1| = ", format(max(chk["sum1", ]), digits = 3), "; min weight = ", format(min(chk["neg", ]), digits = 3), "; max cap excess (capped cells) = ", format(max(chk["over", ]), digits = 3),
     " -> ", if (max(chk["sum1", ]) < 1e-8 && min(chk["neg", ]) > -1e-8 && max(chk["over", ]) < 1e-8) "PASS" else "FAIL")
# T2: max-Sharpe QP vs an independent solver (nloptr SLSQP) on random windows
library(nloptr); worst <- 0
for (i in 1:20) { n <- sample(7:25, 1); X <- matrix(rnorm(36 * n, 0.01, 0.06), 36, n) + rnorm(36) * 0.03; S <- 12 * cov(X); mu <- rnorm(n, 0.02, 0.1) + 0.1
  w1 <- max_sharpe(mu, S, 0.3)$w; f <- function(w) -(sum(w * mu) / sqrt(as.numeric(t(w) %*% S %*% w)))
  r <- nloptr(rep(1 / n, n), f, lb = rep(0, n), ub = rep(0.3, n), eval_g_eq = function(w) sum(w) - 1, eval_jac_g_eq = function(w) rep(1, n),
              opts = list(algorithm = "NLOPT_LD_SLSQP", xtol_rel = 1e-10, maxeval = 2000), eval_grad_f = function(w) { v <- as.numeric(t(w) %*% S %*% w); s <- sqrt(v); -(mu / s - sum(w * mu) * as.vector(S %*% w) / s^3) })
  s1 <- sum(w1 * mu) / sqrt(as.numeric(t(w1) %*% S %*% w1)); s2 <- -r$objective; worst <- max(worst, s2 - s1) }
rep_("T2 QP vs SLSQP: largest Sharpe shortfall of QP vs SLSQP over 20 random problems = ", format(worst, digits = 3), " -> ", if (worst < 1e-4) "PASS" else "FAIL")
# T3: BL posterior master formula equals the precision-form Bayesian formula
n <- 8; S <- cov(matrix(rnorm(40 * n), 40, n)) * 12; Pi <- rnorm(n, 0.05, 0.02); Pm <- rbind(c(rep(1 / 4, 4), rep(0, 4)), c(rep(0, 4), rep(1 / 4, 4))); q <- c(0.08, 0.02); tau <- 1 / 36; Om <- diag(c(0.01, 0.02))
m1 <- bl_posterior(Pi, S, tau, Pm, q, Om); m2 <- as.vector(solve(solve(tau * S) + t(Pm) %*% solve(Om) %*% Pm, solve(tau * S) %*% Pi + t(Pm) %*% solve(Om) %*% q))
rep_("T3 BL posterior: max abs difference master vs precision form = ", format(max(abs(m1 - m2)), digits = 3), " -> ", if (max(abs(m1 - m2)) < 1e-10) "PASS" else "FAIL")
# T4: tau invariance when Omega proportional to tau
mA <- bl_posterior(Pi, S, 0.01, Pm, q, 0.01 * diag(c(1, 2))); mB <- bl_posterior(Pi, S, 0.5, Pm, q, 0.5 * diag(c(1, 2)))
rep_("T4 tau-invariance: max abs difference = ", format(max(abs(mA - mB)), digits = 3), " -> ", if (max(abs(mA - mB)) < 1e-10) "PASS" else "FAIL")
# T5: ANOVA shares (QR implementation) vs stats::aov
cells <- read.csv(file.path(od, "tables/B1_cells_banks.csv")); for (j in c("anchor", "view", "cov", "cap")) cells[[j]] <- factor(cells[[j]], levels = unique(cells[[j]]))
a <- anova(lm(sharpe ~ (anchor + view + cov + cap)^2, cells)); sh_aov <- a[1:4, "Sum Sq"] / sum(a[, "Sum Sq"], (sum((cells$sharpe - mean(cells$sharpe))^2) - sum(a[, "Sum Sq"])))
tot <- sum((cells$sharpe - mean(cells$sharpe))^2); sh_aov <- a[1:4, "Sum Sq"] / tot
shB <- read.csv(file.path(od, "tables/B2_shares_banks.csv")); sh_mine <- shB$share[1:4]
rep_("T5 ANOVA shares: max abs difference vs aov() = ", format(max(abs(sh_aov - sh_mine)), digits = 3), " -> ", if (max(abs(sh_aov - sh_mine)) < 1e-8) "PASS" else "FAIL")
# T6: look-ahead audit, bank pipeline. Perturb every return/cap/market row after row 49, recompute weights for decisions t <= 48
P2 <- P; set.seed(7); P2$R[50:144, ] <- matrix(rnorm(95 * 25, 0.01, 0.1), 95, 25); P2$MC[50:144, ] <- P2$MC[50:144, ] * runif(95 * 25, 0.3, 3); P2$MCl <- rbind(NA, P2$MC[-144, ])
P2$mkt[50:144] <- rnorm(95, 0.01, 0.05); p <- default_params(); p$last_t <- 48
r1 <- run_factorial_monthly(P, p, refs = FALSE); r2 <- run_factorial_monthly(P2, p, refs = FALSE)
d <- max(sapply(r1$ids, function(id) max(abs(r1$W[[id]] - r2$W[[id]]))))
rep_("T6 look-ahead audit (bank pipeline): max abs weight difference when all data after month 49 is replaced by noise = ", format(d, digits = 3), " -> ", if (d < 1e-10) "PASS" else "FAIL")
# T7: look-ahead audit, broad pipeline (weights saved by 21_factorial_broad.R, original vs data after day 300 replaced)
w0 <- readRDS(file.path(od, "rds/broad_weights.rds")); w1 <- readRDS(file.path(od, "rds/broad_weights_LA.rds"))
W <- 120; H <- 5; nd <- 519; ts <- seq(W + 1, nd - H, by = H); keep <- which(ts <= 300)
d2 <- max(sapply(names(w0), function(id) max(abs(w0[[id]][keep, ] - w1[[id]][keep, ]))))
rep_("T7 look-ahead audit (broad pipeline): decisions with t <= 300 (", length(keep), " of ", length(ts), "): max abs weight difference = ", format(d2, digits = 3), " -> ", if (d2 < 1e-10) "PASS" else "FAIL")
# T8: reproducibility -- rerun a short bank pipeline twice
p$last_t <- 44; a1 <- run_factorial_monthly(P, p, refs = FALSE); a2 <- run_factorial_monthly(P, p, refs = FALSE)
rep_("T8 reproducibility: max abs difference between two runs = ", format(max(abs(a1$ret - a2$ret)), digits = 3), " -> ", if (max(abs(a1$ret - a2$ret)) == 0) "PASS" else "FAIL")
# T9: return accounting -- recompute realised returns of one cell from saved weights and raw returns
id <- "EW|LOWVOL|LW|capped"; W <- fb$W[[id]]; oos <- match(rownames(W), as.character(P$dates)); Rm <- P$R[oos, ]; Rm[is.na(Rm)] <- 0
rep_("T9 return accounting: max abs difference for cell ", id, " = ", format(max(abs(rowSums(W * Rm) - fb$ret[, id])), digits = 3), " -> ", if (max(abs(rowSums(W * Rm) - fb$ret[, id])) < 1e-12) "PASS" else "FAIL")
# T10: suspicious-value screen (identical Sharpe, round numbers, zero variance)
sr <- cells$sharpe; rep_("T10 value screen: distinct Sharpe values among 80 cells = ", length(unique(round(sr, 6))), "; min cell s.d. of returns = ", format(min(apply(fb$ret[, cells$id], 2, sd)), digits = 3), " -> ", if (length(unique(round(sr, 6))) > 40 && min(apply(fb$ret[, cells$id], 2, sd)) > 0) "PASS (cells are not identical; some duplicates arise by construction when the cap does not bind)" else "CHECK")
writeLines(out, file.path(root, "process/02_verification_tests.txt"))
