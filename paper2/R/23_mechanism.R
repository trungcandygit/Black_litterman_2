# 23_mechanism.R -- why does attribution differ across universes? dispersion, correlation, signal strength; SPA of all cells vs 1/N; turnover/MDD/regime attribution
source("/home/user/Black_litterman_2/paper2/R/20_factorial.R")
root <- "/home/user/Black_litterman_2/paper2"; od <- file.path(root, "output"); set.seed(20261004)
fb <- readRDS(file.path(od, "rds/factorial_banks.rds")); fw <- readRDS(file.path(od, "rds/factorial_broad.rds"))
P <- readRDS(file.path(od, "rds/panel.rds"))
# --- mechanism: bank panel
Rb <- P$R[39:144, ]; cb <- cor(Rb, use = "pairwise.complete.obs"); bank_corr <- mean(cb[upper.tri(cb)])
bank_disp_m <- mean(apply(Rb, 1, sd, na.rm = TRUE))
sig <- readRDS(file.path(od, "rds/signal_diag.rds"))
nwt <- function(x) { fit <- lm(x ~ 1); ct <- lmtest::coeftest(fit, vcov. = sandwich::NeweyWest(fit, lag = 3, prewhite = FALSE)); c(mean = mean(x), t = ct[1, 3]) }
# --- mechanism: broad universe (re-derive weekly ICs and dispersion)
root0 <- "/home/user/Black_litterman_2"; fl <- list.files(file.path(root0, "data/raw"), full.names = TRUE)
dat <- lapply(fl, function(f) { d <- read.csv(f); d$sym <- sub("\\.csv$", "", basename(f)); d })
all_dates <- sort(unique(unlist(lapply(dat, `[[`, "time")))); all_dates <- all_dates[all_dates >= "2024-08-21"]
mat <- function(col) { M <- matrix(NA_real_, length(all_dates), length(dat), dimnames = list(all_dates, sapply(dat, function(d) d$sym[1])))
  for (j in seq_along(dat)) { mi <- match(dat[[j]]$time, all_dates); okm <- !is.na(mi); M[mi[okm], j] <- dat[[j]][[col]][okm] }; M }
C <- mat("close"); V <- mat("volume"); keep <- which(colMeans(!is.na(C)) >= 0.95); C <- C[, keep]; V <- V[, keep]
nd <- nrow(C); Rd <- rbind(NA, C[-1, ] / C[-nd, ] - 1); Rd[!is.finite(Rd)] <- NA; dv <- C * V
W <- 120; H <- 5; ts <- seq(W + 1, nd - H, by = H)
mom_f <- function(R, mk, s, Lm = 60, skip = 5) { idx <- (s - skip - Lm + 1):(s - skip); apply(1 + R[idx, , drop = FALSE] - mk[idx], 2, prod) - 1 }
vol_f <- function(R, s, Lv = 60) apply(R[(s - Lv + 1):s, , drop = FALSE], 2, sd) * sqrt(252)
icw <- do.call(rbind, lapply(ts, function(t) { rows <- (t - W + 1):t; ok <- which(colSums(is.na(Rd[rows, ])) == 0 & !is.na(dv[t, ]))
  adv <- colMeans(dv[(t - 59):t, ok, drop = FALSE]); el <- ok[order(-adv)[1:100]]; wm <- adv[match(el, ok)]; wm <- wm / sum(wm)
  Rel <- Rd[1:t, el]; mk <- as.vector(Rel %*% wm); mom <- mom_f(Rel, mk, t); vol <- vol_f(Rel, t)
  r_ <- Rd[(t + 1):(t + H), el]; r_[is.na(r_)] <- 0; y <- apply(1 + r_, 2, prod) - 1; yi <- y - sum(wm * y)
  cm <- cor(Rd[rows, el]); data.frame(ic_mom = cor(mom, yi, method = "spearman"), ic_vol = cor(-vol, yi, method = "spearman"), ic_comp = cor(zs(mom) - zs(vol), yi, method = "spearman"),
    corr = mean(cm[upper.tri(cm)]), disp = sd(y)) }))
mech <- rbind(data.frame(universe = "banks (monthly)", n_assets = "7-25", mean_pairwise_corr = bank_corr, xs_dispersion_per_period = bank_disp_m,
    ic_mom = mean(sig$ic_mom), t_mom = nwt(sig$ic_mom)["t"], ic_lowvol = mean(sig$ic_vol), t_lowvol = nwt(sig$ic_vol)["t"], ic_comp = mean(sig$ic_z), t_comp = nwt(sig$ic_z)["t"], n_periods = nrow(sig)),
  data.frame(universe = "broad (weekly)", n_assets = "100", mean_pairwise_corr = mean(icw$corr), xs_dispersion_per_period = mean(icw$disp),
    ic_mom = mean(icw$ic_mom), t_mom = nwt(icw$ic_mom)["t"], ic_lowvol = mean(icw$ic_vol), t_lowvol = nwt(icw$ic_vol)["t"], ic_comp = mean(icw$ic_comp), t_comp = nwt(icw$ic_comp)["t"], n_periods = nrow(icw)))
rownames(mech) <- NULL; write.csv(mech, file.path(od, "tables/B7_mechanism.csv"), row.names = FALSE); print(mech, digits = 3)
# --- SPA: does any of the 80 cells beat 1/N (quadratic utility, gamma = 5)?
spa_cells <- function(f, ann, label) { ids <- CELLS$id; r <- f$ret[, ids]; ew <- f$ret[, "REF_EW"]; g <- 5; u <- function(x) x - g / 2 * x^2
  d <- sapply(ids, function(i) u(r[, i]) - u(ew)); o <- spa_test(d, B = 5000); data.frame(universe = label, t(o), best_cell = ids[which.max(colMeans(d))], best_mean_util_diff = max(colMeans(d))) }
spa <- rbind(spa_cells(fb, 12, "banks"), spa_cells(fw, 52, "broad")); write.csv(spa, file.path(od, "tables/B8_spa_cells_vs_EW.csv"), row.names = FALSE); print(spa, digits = 3)
# --- attribution of other outcomes and by regime (banks)
fac <- CELLS[, c("anchor", "view", "cov", "cap")]; for (j in names(fac)) fac[[j]] <- factor(fac[[j]], levels = unique(fac[[j]]))
X <- model.matrix(~ (anchor + view + cov + cap)^2, fac); asg <- attr(X, "assign"); qrX <- qr(X); tn <- attr(terms(~ (anchor + view + cov + cap)^2), "term.labels")
shares <- function(y) { yc <- y - mean(y); eff <- qr.qty(qrX, yc); ss <- tapply(eff[1:qrX$rank]^2, asg[qrX$pivot][1:qrX$rank], sum)
  ss0 <- setNames(rep(0, length(tn)), tn); ss0[as.integer(names(ss)[names(ss) != "0"])] <- ss[names(ss) != "0"]; tot <- sum(yc^2)
  c(anchor = ss0[1] / tot, view = ss0[2] / tot, cov = ss0[3] / tot, cap = ss0[4] / tot, twoway = sum(ss0[5:length(tn)]) / tot) }
ids <- CELLS$id; dts <- fb$dates; i2 <- which(dts >= as.Date("2022-01-01")); i1 <- setdiff(seq_along(dts), i2)
cbi <- function(Tn, b) { nb <- ceiling(Tn / b); st <- sample.int(Tn, nb, replace = TRUE); (as.vector(sapply(st, function(s) ((s - 1 + 0:(b - 1)) %% Tn) + 1)))[1:Tn] }
sh_ci <- function(E, ann, B = 1000) { Tn <- nrow(E); b <- max(2, round(Tn^(1/3))); s0 <- shares(colMeans(E) / apply(E, 2, sd) * sqrt(ann))
  Sb <- t(replicate(B, { ix <- cbi(Tn, b); Eb <- E[ix, ]; shares(colMeans(Eb) / apply(Eb, 2, sd) * sqrt(ann)) }))
  data.frame(component = sub("\\..*", "", names(s0)), share = as.numeric(s0), lo = apply(Sb, 2, quantile, 0.025), hi = apply(Sb, 2, quantile, 0.975)) }
Eb <- fb$ret[, ids] - fb$rf_m
sub <- rbind(cbind(sample = "banks P1", sh_ci(Eb[i1, ], 12)), cbind(sample = "banks P2", sh_ci(Eb[i2, ], 12)))
write.csv(sub, file.path(od, "tables/B9_shares_by_regime.csv"), row.names = FALSE); print(sub, digits = 3)
oth <- do.call(rbind, lapply(list(list("banks", fb), list("broad", fw)), function(z) { f <- z[[2]]
  tv <- colMeans(ifelse(is.na(f$turnover[, ids]), 0, f$turnover[, ids])); md <- apply(f$ret[, ids], 2, max_dd)
  rbind(data.frame(universe = z[[1]], outcome = "turnover", t(shares(tv))), data.frame(universe = z[[1]], outcome = "max drawdown", t(shares(md)))) }))
write.csv(oth, file.path(od, "tables/B10_shares_other_outcomes.csv"), row.names = FALSE); print(oth, digits = 3)
