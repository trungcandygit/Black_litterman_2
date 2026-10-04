# 07_broad.R -- external-validity test on ~390 HOSE stocks (daily, weekly rebalance)
source("/home/user/Black_litterman_2/paper2/R/lib.R")
root <- "/home/user/Black_litterman_2"; od <- file.path(root, "paper2/output")
fl <- list.files(file.path(root, "data/raw"), full.names = TRUE)
dat <- lapply(fl, function(f) { d <- read.csv(f); d$sym <- sub("\\.csv$", "", basename(f)); d })
all_dates <- sort(unique(unlist(lapply(dat, `[[`, "time")))); all_dates <- all_dates[all_dates >= "2024-08-21"]
mat <- function(col) { M <- matrix(NA_real_, length(all_dates), length(dat), dimnames = list(all_dates, sapply(dat, function(d) d$sym[1])))
  for (j in seq_along(dat)) { mi <- match(dat[[j]]$time, all_dates); okm <- !is.na(mi); M[mi[okm], j] <- dat[[j]][[col]][okm] }; M }
C <- mat("close"); V <- mat("volume")
cover <- colMeans(!is.na(C)); keep <- which(cover >= 0.95); C <- C[, keep]; V <- V[, keep]
nd <- nrow(C); cat("days", nd, "stocks kept", ncol(C), "of", length(dat), "\n")
Rd <- rbind(NA, C[-1, ] / C[-nd, ] - 1); Rd[!is.finite(Rd)] <- NA
dv <- C * V                                                   # dollar volume (price-units x shares)
dts <- as.Date(rownames(C))
rf_tab <- read.csv(file.path(root, "paper2/data/rf_vgb10y.csv"))
rf_ann <- rf_tab$vgb10y_pct[match(as.integer(format(dts, "%Y")), rf_tab$year)] / 100; rf_ann[is.na(rf_ann)] <- 0.0435
rf_d <- (1 + rf_ann)^(1 / 252) - 1
W <- 120; H <- 5; N_UNI <- 100; CAP <- 0.10; ADV_L <- 60
ts <- seq(W + 1, nd - H, by = H)                              # decision days (index of last information day)
set.seed(20261004)
models <- c("EW", "MKT", "MVP_LW", "TAN_LW", "ERC", "KIO_v1", "KMV")
Wl <- setNames(lapply(models, function(m) matrix(0, length(ts), ncol(C))), models)
mom_f <- function(R, mk, s, Lm = 60, skip = 5) { idx <- (s - skip - Lm + 1):(s - skip); apply(1 + R[idx, , drop = FALSE] - mk[idx], 2, prod) - 1 }
vol_f <- function(R, s, Lv = 60) apply(R[(s - Lv + 1):s, , drop = FALSE], 2, sd) * sqrt(252)
diagl <- list()
for (ii in seq_along(ts)) {
  t <- ts[ii]; rows <- (t - W + 1):t
  ok <- which(colSums(is.na(Rd[rows, ])) == 0 & !is.na(dv[t, ]))
  adv <- colMeans(dv[(t - ADV_L + 1):t, ok, drop = FALSE]); el <- ok[order(-adv)[1:N_UNI]]; n <- length(el)
  wm <- adv[match(el, ok)]; wm <- wm / sum(wm)
  Rw <- Rd[rows, el]; mk_all <- as.vector(Rd[1:t, el] %*% wm)             # market proxy: ADV-weighted
  S_lw <- lw_cc(Rw)$Sigma; S_s <- cov(Rw) + diag(1e-9, n)
  delta <- min(10, max(0.5, (mean(mk_all[rows]) - mean(rf_d[rows])) / var(mk_all[rows])))
  put <- function(m, w) { v <- rep(0, ncol(C)); v[el] <- w; Wl[[m]][ii, ] <<- v }
  put("EW", rep(1 / n, n)); put("MKT", wm)
  put("MVP_LW", min_var(S_lw, CAP)); put("ERC", erc_weights(S_lw))
  mu_h <- colMeans(Rw) - mean(rf_d[rows]); put("TAN_LW", max_sharpe(mu_h, S_lw, CAP)$w)
  Rel <- Rd[1:t, el]
  mom <- mom_f(Rel, mk_all, t); vol <- vol_f(Rel, t); z <- zs(mom) - zs(vol); X <- scale(cbind(mom, vol))
  Sa <- 252 * S_lw; Pi <- as.vector(delta * Sa %*% wm); tau <- 1 / W
  # v1-style: single view, k = 4, sample covariance
  set.seed(1 + t); cl4 <- km(X, 4, 25)$cluster; zc4 <- tapply(z, cl4, mean); hi <- which.max(zc4); lo <- which.min(zc4)
  Pm <- matrix(0, 1, n); Pm[1, cl4 == hi] <- 1 / sum(cl4 == hi); Pm[1, cl4 == lo] <- -1 / sum(cl4 == lo)
  Ss <- 252 * S_s; q <- mean(mom[cl4 == hi]) - mean(mom[cl4 == lo])
  mu1 <- bl_posterior(as.vector(delta * Ss %*% wm), Ss, tau, Pm, q, matrix(tau * Pm %*% Ss %*% t(Pm), 1, 1))
  put("KIO_v1", max_sharpe(mu1, Ss, CAP)$w)
  # KMV: stability-selected k, calibrated slope, multi-view
  set.seed(2 + t); ks <- { kk <- 3:6; out <- lapply(kk, function(k) { c0 <- km(X, k); s0 <- cluster_stability(X, c0$cluster, k, 30)
      list(k = k, cl = c0$cluster, s = s0, ws = sum(s0 * tabulate(c0$cluster, k)) / n) }); ws <- sapply(out, `[[`, "ws"); ok2 <- which(ws >= 0.70)
    out[[if (length(ok2)) max(ok2) else 1]] }
  sl <- sapply(seq(t - 5 - 40, t - H, by = H), function(s) { if (s - 65 < t - W) return(NA)
      zs_ <- { m_ <- mom_f(Rd[1:s, el], as.vector(Rd[1:s, el] %*% wm), s); v_ <- vol_f(Rd[1:s, el], s); zs(m_) - zs(v_) }
      y <- apply(1 + Rd[(s + 1):(s + H), el] - as.vector(Rd[(s + 1):(s + H), el] %*% wm), 2, prod) - 1; cov(zs_, y) / var(zs_) })
  lam_w <- mean(sl, na.rm = TRUE); lam_ann <- max(0, lam_w) * 52
  k <- ks$k; cl <- ks$cl; Pk <- t(sapply(1:k, function(c) as.numeric(cl == c) / sum(cl == c)))
  zck <- tapply(z, cl, mean); qk <- as.numeric(Pk %*% Pi) + lam_ann * (zck - mean(z))
  Omk <- diag(tau * as.vector(diag(Pk %*% Sa %*% t(Pk))) / pmax(ks$s, 0.05), k)
  put("KMV", max_sharpe(bl_posterior(Pi, Sa, tau, Pk, qk, Omk), Sa, CAP)$w)
  diagl[[ii]] <- data.frame(date = as.character(dts[t]), n = n, k = k, ws = ks$ws, lam_w = lam_w, delta = delta)
}
oos_ret <- function(m) sapply(seq_along(ts), function(ii) { t <- ts[ii]; r <- Rd[(t + 1):(t + H), ]; r[is.na(r)] <- 0
  sum(Wl[[m]][ii, ] * (apply(1 + r, 2, prod) - 1)) })
ret <- sapply(models, oos_ret)
rfw <- sapply(ts, function(t) prod(1 + rf_d[(t + 1):(t + H)]) - 1)
turn <- sapply(models, function(m) { w <- Wl[[m]]; tv <- rep(NA, nrow(w)); for (i in 2:nrow(w)) { r <- Rd[(ts[i - 1] + 1):(ts[i - 1] + H), ]; r[is.na(r)] <- 0
  g <- w[i - 1, ] * apply(1 + r, 2, prod); g <- g / sum(g); tv[i] <- sum(abs(w[i, ] - g)) }; tv })
ex <- ret - rfw; dd <- dts[ts + H]
perf <- data.frame(model = models, ann_ret = colMeans(ret) * 52, ann_vol = apply(ret, 2, sd) * sqrt(52), sharpe = apply(ex, 2, ann_sharpe, ann = 52),
  mdd = apply(ret, 2, max_dd), turnover_wk = colMeans(turn, na.rm = TRUE),
  sr_net25 = apply(ex - 0.0025 * ifelse(is.na(turn), 0, turn), 2, ann_sharpe, ann = 52),
  sr_net50 = apply(ex - 0.0050 * ifelse(is.na(turn), 0, turn), 2, ann_sharpe, ann = 52))
tests <- do.call(rbind, lapply(setdiff(models, "EW"), function(m) { o <- sr_diff_test(ex[, m], ex[, "EW"], B = 3000, ann = 52); data.frame(model = m, vs = "EW", t(o)) }))
write.csv(perf, file.path(od, "tables/T9_broad_performance.csv"), row.names = FALSE); write.csv(tests, file.path(od, "tables/T9b_broad_tests.csv"), row.names = FALSE)
saveRDS(list(n_stocks = ncol(C), n_universe = N_UNI, ret = ret, ex = ex, turn = turn, dates = dd, diag = do.call(rbind, diagl), n_oos = length(ts)), file.path(od, "rds/broad.rds"))
options(width = 200); cat("OOS weeks:", length(ts), as.character(range(dd)), "\n"); print(perf, digits = 3); print(tests, digits = 3)
print(table(do.call(rbind, diagl)$k)); print(summary(do.call(rbind, diagl)$lam_w))
