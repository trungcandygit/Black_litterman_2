# 21_factorial_broad.R -- confirmation sample: the same factorial on ~100 liquid HOSE stocks, weekly rebalance
source("/home/user/Black_litterman_2/paper2/R/20_factorial.R")
cap_value <- c(capped = 0.10, nocap = 1.0)
root <- "/home/user/Black_litterman_2"; od <- file.path(root, "paper2/output")
fl <- list.files(file.path(root, "data/raw"), full.names = TRUE)
dat <- lapply(fl, function(f) { d <- read.csv(f); d$sym <- sub("\\.csv$", "", basename(f)); d })
all_dates <- sort(unique(unlist(lapply(dat, `[[`, "time")))); all_dates <- all_dates[all_dates >= "2024-08-21"]
mat <- function(col) { M <- matrix(NA_real_, length(all_dates), length(dat), dimnames = list(all_dates, sapply(dat, function(d) d$sym[1])))
  for (j in seq_along(dat)) { mi <- match(dat[[j]]$time, all_dates); okm <- !is.na(mi); M[mi[okm], j] <- dat[[j]][[col]][okm] }; M }
C <- mat("close"); V <- mat("volume"); keep <- which(colMeans(!is.na(C)) >= 0.95); C <- C[, keep]; V <- V[, keep]
nd <- nrow(C); Rd <- rbind(NA, C[-1, ] / C[-nd, ] - 1); Rd[!is.finite(Rd)] <- NA; dv <- C * V; dts <- as.Date(rownames(C))
rf_tab <- read.csv(file.path(root, "paper2/data/rf_vgb10y.csv"))
rf_ann <- rf_tab$vgb10y_pct[match(as.integer(format(dts, "%Y")), rf_tab$year)] / 100; rf_ann[is.na(rf_ann)] <- 0.0435; rf_d <- (1 + rf_ann)^(1 / 252) - 1
la <- Sys.getenv("LA_CUT"); if (nzchar(la)) { cut <- as.integer(la); set.seed(99); Rd[(cut + 1):nd, ] <- matrix(rnorm((nd - cut) * ncol(Rd), 0, 0.03), nd - cut); dv[(cut + 1):nd, ] <- dv[(cut + 1):nd, ] * runif((nd - cut) * ncol(dv), 0.2, 5) }
W <- 120; H <- 5; N_UNI <- 100; ADV_L <- 60; tau <- 1 / W
ts <- seq(W + 1, nd - H, by = H); ids <- c(CELLS$id, "REF_EW", "REF_CAP", "REF_ERC", "REF_MVP")
Wl <- setNames(lapply(ids, function(m) matrix(0, length(ts), ncol(C))), ids)
mom_f <- function(R, mk, s, Lm = 60, skip = 5) { idx <- (s - skip - Lm + 1):(s - skip); apply(1 + R[idx, , drop = FALSE] - mk[idx], 2, prod) - 1 }
vol_f <- function(R, s, Lv = 60) apply(R[(s - Lv + 1):s, , drop = FALSE], 2, sd) * sqrt(252)
for (ii in seq_along(ts)) {
  t <- ts[ii]; rows <- (t - W + 1):t
  ok <- which(colSums(is.na(Rd[rows, ])) == 0 & !is.na(dv[t, ])); adv <- colMeans(dv[(t - ADV_L + 1):t, ok, drop = FALSE])
  el <- ok[order(-adv)[1:N_UNI]]; n <- length(el); wm <- adv[match(el, ok)]; wm <- wm / sum(wm)
  Rw <- Rd[rows, el]; Rel <- Rd[1:t, el]; mk_all <- as.vector(Rel %*% wm)
  mom <- mom_f(Rel, mk_all, t); vol <- vol_f(Rel, t); sc <- list(mom = mom, vol = vol, z = zs(mom) - zs(vol)); X <- scale(cbind(mom, vol))
  set.seed(2 + t); kk <- 3:6; out <- lapply(kk, function(k) { c0 <- km(X, k); s0 <- cluster_stability(X, c0$cluster, k, 30)
    list(k = k, cl = c0$cluster, s = s0, ws = sum(s0 * tabulate(c0$cluster, k)) / n) }); ws <- sapply(out, `[[`, "ws"); ok2 <- which(ws >= 0.70)
  ks <- out[[if (length(ok2)) max(ok2) else 1]]
  sl <- sapply(seq(t - 5 - 40, t - H, by = H), function(s) { if (s - 65 < t - W) return(rep(NA_real_, 3))
    m_ <- mom_f(Rd[1:s, el], as.vector(Rd[1:s, el] %*% wm), s); v_ <- vol_f(Rd[1:s, el], s)
    y <- apply(1 + Rd[(s + 1):(s + H), el] - as.vector(Rd[(s + 1):(s + H), el] %*% wm), 2, prod) - 1
    sapply(list(MOM = zs(m_), LOWVOL = -zs(v_), COMP = zs(m_) - zs(v_)), function(z) cov(z, y) / var(z)) })
  lam <- as.list(52 * pmax(0, rowMeans(sl, na.rm = TRUE))); names(lam) <- c("MOM", "LOWVOL", "COMP")
  Wc <- factorial_core(Rw, wm, rf_d[rows], sc, lam, list(cl = ks$cl, k = ks$k, s = ks$s), 252, tau)
  for (id in CELLS$id) { v <- rep(0, ncol(C)); v[el] <- Wc[id, ]; Wl[[id]][ii, ] <- v }
  S_lw <- lw_cc(Rw)$Sigma; put <- function(id, w) { v <- rep(0, ncol(C)); v[el] <- w; Wl[[id]][ii, ] <<- v }
  put("REF_EW", rep(1 / n, n)); put("REF_CAP", wm); put("REF_ERC", erc_weights(S_lw)); put("REF_MVP", min_var(S_lw, 0.10))
}
wk_ret <- function(i) { t <- ts[i]; r <- Rd[(t + 1):(t + H), ]; r[is.na(r)] <- 0; apply(1 + r, 2, prod) - 1 }
RW <- t(sapply(seq_along(ts), wk_ret))
ret <- sapply(ids, function(m) rowSums(Wl[[m]] * RW))
to <- sapply(ids, function(m) { w <- Wl[[m]]; tv <- rep(NA_real_, nrow(w)); for (i in 2:nrow(w)) { g <- w[i - 1, ] * (1 + RW[i - 1, ]); g <- g / sum(g); tv[i] <- sum(abs(w[i, ] - g)) }; tv })
rfw <- sapply(ts, function(t) prod(1 + rf_d[(t + 1):(t + H)]) - 1); dd <- dts[ts + H]
saveRDS(Wl, file.path(od, if (nzchar(la)) "rds/broad_weights_LA.rds" else "rds/broad_weights.rds")); if (nzchar(la)) quit(save = "no")
saveRDS(list(ids = ids, ret = ret, turnover = to, rf_m = rfw, dates = dd, n_stocks = ncol(C), n_universe = N_UNI, ann = 52), file.path(od, "rds/factorial_broad.rds"))
ex <- ret - rfw; sr <- apply(ex, 2, ann_sharpe, ann = 52); cat("OOS weeks", length(ts), "\n"); print(summary(sr[CELLS$id])); print(round(sr[c("REF_EW", "REF_CAP", "REF_ERC", "REF_MVP")], 3))
