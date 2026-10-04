# 20_factorial.R -- Paper B: fully crossed factorial of Black-Litterman ingredients (anchor x view x covariance x cap)
source("/home/user/Black_litterman_2/paper2/R/02_engine.R")

ANCHORS <- c("CAP", "EW", "ERC", "SHR"); VIEWS <- c("NONE", "MOM", "LOWVOL", "COMP", "CLUSTER"); COVS <- c("SAMPLE", "LW"); CAPS <- c("capped", "nocap")
CELLS <- expand.grid(anchor = ANCHORS, view = VIEWS, cov = COVS, cap = CAPS, stringsAsFactors = FALSE)
CELLS$id <- paste(CELLS$anchor, CELLS$view, CELLS$cov, CELLS$cap, sep = "|")
cap_value <- c(capped = 0.30, nocap = 1.0)

tercile_groups <- function(z) ceiling(3 * rank(z, ties.method = "first") / length(z))

# core: one window -> weights for all cells (rows) over n eligible assets
# Rw: T x n window returns; wm: market/proxy weights; rf_win: per-period rf in window; sc: list(mom, vol, z_comp)
# lam: named annual calibrated slopes (MOM, LOWVOL, COMP); clu: list(cl, k, s) cluster view object; ann: periods per year
factorial_core <- function(Rw, wm, rf_win, sc, lam, clu, ann, tau) {
  n <- ncol(Rw)
  S_s <- ann * cov(Rw) + diag(1e-10, n); S_lw <- ann * lw_cc(Rw)$Sigma
  Sig <- list(SAMPLE = S_s, LW = S_lw)
  w_anch <- list(CAP = wm, EW = rep(1 / n, n), ERC = erc_weights(S_lw), SHR = 0.5 * wm + 0.5 / n)
  delta <- sapply(w_anch, function(w) { r <- as.vector(Rw %*% w); min(10, max(0.5, (mean(r) - mean(rf_win)) / var(r))) })
  zlist <- list(MOM = zs(sc$mom), LOWVOL = -zs(sc$vol), COMP = zs(sc$mom) - zs(sc$vol))
  W <- matrix(0, nrow(CELLS), n, dimnames = list(CELLS$id, NULL))
  for (a in ANCHORS) for (cv in COVS) {
    Sg <- Sig[[cv]]; Pi <- as.vector(delta[a] * Sg %*% w_anch[[a]])
    mu_by_view <- list(NONE = Pi)
    for (v in c("MOM", "LOWVOL", "COMP")) {
      gr <- tercile_groups(zlist[[v]]); Pm <- t(sapply(1:3, function(c) as.numeric(gr == c) / sum(gr == c)))
      zc <- tapply(zlist[[v]], gr, mean); q <- as.numeric(Pm %*% Pi) + lam[[v]] * (zc - mean(zlist[[v]]))
      Om <- diag(tau * as.vector(diag(Pm %*% Sg %*% t(Pm))), 3)
      mu_by_view[[v]] <- bl_posterior(Pi, Sg, tau, Pm, q, Om) }
    cl <- clu$cl; k <- clu$k; Pm <- t(sapply(1:k, function(c) as.numeric(cl == c) / sum(cl == c)))
    zc <- tapply(zlist$COMP, cl, mean); q <- as.numeric(Pm %*% Pi) + lam$COMP * (zc - mean(zlist$COMP))
    Om <- diag(tau * as.vector(diag(Pm %*% Sg %*% t(Pm))) / pmax(clu$s, 0.05), k)
    mu_by_view$CLUSTER <- bl_posterior(Pi, Sg, tau, Pm, q, Om)
    for (v in VIEWS) for (cp in CAPS) {
      id <- paste(a, v, cv, cp, sep = "|"); W[id, ] <- max_sharpe(mu_by_view[[v]], Sg, cap_value[[cp]])$w }
  }
  W
}

# monthly bank-panel runner -------------------------------------------------------------
calib_lambda_all <- function(P, ctx, p) {
  sl <- sapply((ctx$t - p$win + 13):(ctx$t - 1), function(s) {
    sc <- score_at(P$R, P$mkt, s, ctx$elig, p$Lm, p$Lv); y <- P$R[s + 1, ctx$elig] - P$mkt[s + 1]
    zz <- list(MOM = zs(sc$mom), LOWVOL = -zs(sc$vol), COMP = zs(sc$mom) - zs(sc$vol))
    sapply(zz, function(z) cov(z, y) / var(z)) })
  lam <- 12 * pmax(0, rowMeans(sl)); names(lam) <- c("MOM", "LOWVOL", "COMP"); as.list(lam)
}

run_factorial_monthly <- function(P, p = default_params(), refs = TRUE) {
  T <- nrow(P$R); ts <- p$first_t:(min(T - 1, p$last_t)); nA <- ncol(P$R)
  ids <- c(CELLS$id, if (refs) c("REF_EW", "REF_CAP", "REF_ERC", "REF_MVP", "REF_HRP"))
  Wl <- setNames(lapply(ids, function(m) matrix(0, length(ts), nA, dimnames = list(as.character(P$dates[ts + 1]), colnames(P$R)))), ids)
  for (ii in seq_along(ts)) {
    t <- ts[ii]; ctx <- make_ctx(P, t, p); el <- ctx$elig; n <- ctx$n
    sc <- score_at(P$R, P$mkt, t, el, p$Lm, p$Lv); X12 <- scale(cbind(sc$mom, sc$vol))
    set.seed(p$seed + t * 10 + 2); ks <- select_k_stability(X12, p)
    lam <- calib_lambda_all(P, ctx, p)
    W <- factorial_core(ctx$Rw, ctx$wmkt, ctx$rfm, sc, lam, list(cl = ks$sel$cl$cluster, k = ks$sel$k, s = ks$sel$s), 12, p$tau)
    for (id in CELLS$id) { v <- rep(0, nA); v[el] <- W[id, ]; Wl[[id]][ii, ] <- v }
    if (refs) { S_lw <- lw_cc(ctx$Rw)$Sigma
      put <- function(id, w) { v <- rep(0, nA); v[el] <- w; Wl[[id]][ii, ] <<- v }
      put("REF_EW", rep(1 / n, n)); put("REF_CAP", ctx$wmkt); put("REF_ERC", erc_weights(S_lw)); put("REF_MVP", min_var(S_lw, p$cap)); put("REF_HRP", hrp_weights(S_lw)) }
  }
  oos <- ts + 1; Rm <- P$R[oos, , drop = FALSE]; Rm[is.na(Rm)] <- 0
  ret <- sapply(ids, function(m) rowSums(Wl[[m]] * Rm))
  to <- sapply(ids, function(m) { w <- Wl[[m]]; tv <- rep(NA_real_, nrow(w)); for (i in 2:nrow(w)) { g <- w[i - 1, ] * (1 + Rm[i - 1, ]); g <- g / sum(g); tv[i] <- sum(abs(w[i, ] - g)) }; tv })
  maxw <- sapply(ids, function(m) apply(Wl[[m]], 1, max))
  rownames(ret) <- rownames(to) <- as.character(P$dates[oos])
  list(ids = ids, W = Wl, ret = ret, turnover = to, maxw = maxw, rf_m = P$rf_m[oos], rf_ann = P$rf_ann[oos], mkt = P$mkt[oos], dates = P$dates[oos], params = p)
}

if (sys.nframe() == 0) {
  root <- "/home/user/Black_litterman_2/paper2"; P <- readRDS(file.path(root, "output/rds/panel.rds"))
  t0 <- Sys.time(); fb <- run_factorial_monthly(P); cat("elapsed", format(Sys.time() - t0), "\n")
  saveRDS(fb, file.path(root, "output/rds/factorial_banks.rds"))
  ex <- fb$ret - fb$rf_m; sr <- apply(ex, 2, ann_sharpe); print(summary(sr[CELLS$id])); print(round(sr[c("REF_EW", "REF_CAP", "REF_ERC", "REF_MVP", "REF_HRP")], 3))
}
