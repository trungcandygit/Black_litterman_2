# 02_engine.R -- rolling-window engine: signals, views, all portfolio rules
source("/home/user/Black_litterman_2/paper2/R/lib.R")

default_params <- function() list(
  win = 36, cap = 0.30, tau = 1/36, omega_mult = 1, Lm = 6, Lv = 12, Lv_v1 = 36, Bstab = 50, stab_thr = 0.70,
  kset = 3:6, k_fixed = 4, cost_tc = 0.0025, seed = 20261004, first_t = 38, last_t = Inf,
  models = NULL)

# per-window context ---------------------------------------------------------------
make_ctx <- function(P, t, p) {
  rows <- (t - p$win + 1):t
  Rw_all <- P$R[rows, , drop = FALSE]
  elig <- which(colSums(is.na(Rw_all)) == 0 & !is.na(P$MC[t, ]))
  list(t = t, rows = rows, elig = elig, n = length(elig),
       Rw = Rw_all[, elig, drop = FALSE], mktw = P$mkt[rows],
       rfm = P$rf_m[rows], rf_ann_t = P$rf_ann[t], rf_m_t = P$rf_m[t],
       wmkt = { w <- P$MC[t, elig]; w / sum(w) })
}

# composite score at decision month s using data up to s (rows of Rfull are absolute months)
score_at <- function(Rfull, mktfull, s, elig, Lm, Lv) {
  Rs <- Rfull[1:s, elig, drop = FALSE]
  mom <- feat_mom(Rs, mktfull[1:s], s, Lm); vol <- feat_vol(Rs, s, Lv)
  list(mom = mom, vol = vol, z = zs(mom) - zs(vol))
}

# k selection ---------------------------------------------------------------------
select_k_stability <- function(X, p) {
  kmax <- max(2, floor(nrow(X) / 3)); ks <- sort(unique(c(if (kmax < 3) 2, p$kset[p$kset <= kmax])))
  out <- lapply(ks, function(k) { cl <- km(X, k); s <- cluster_stability(X, cl$cluster, k, p$Bstab)
    list(k = k, cl = cl, s = s, ws = sum(s * tabulate(cl$cluster, k)) / nrow(X)) })
  ws <- sapply(out, `[[`, "ws"); ok <- which(ws >= p$stab_thr)
  pick <- if (length(ok)) max(ok) else which(ks == min(3, max(ks)))
  list(sel = out[[pick]], ws = setNames(ws, ks))
}
select_k_ic <- function(P, ctx, p) {
  kmax <- max(2, floor(ctx$n / 3)); kk <- sort(unique(c(if (kmax < 3) 2, p$kset[p$kset <= kmax]))); 
  ic <- sapply(kk, function(k) {
    v <- sapply(max(ctx$t - 17, ctx$t - p$win + 13):(ctx$t - 1), function(s) {
      sc <- score_at(P$R, P$mkt, s, ctx$elig, p$Lm, p$Lv)
      X <- scale(cbind(sc$mom, sc$vol)); cl <- km(X, k, 10)$cluster
      rk <- rank(tapply(sc$z, cl, mean))[cl]
      y <- P$R[s + 1, ctx$elig] - P$mkt[s + 1]
      suppressWarnings(cor(rk, y, method = "spearman")) })
    mean(v, na.rm = TRUE) })
  kk[which.max(ic)]
}

# calibrated slope lambda (monthly) from in-window cross-sections
calib_lambda <- function(P, ctx, p) {
  sl <- sapply((ctx$t - p$win + 13):(ctx$t - 1), function(s) {
    sc <- score_at(P$R, P$mkt, s, ctx$elig, p$Lm, p$Lv); y <- P$R[s + 1, ctx$elig] - P$mkt[s + 1]
    cov(sc$z, y) / var(sc$z) })
  c(lambda = mean(sl), t = mean(sl) / (sd(sl) / sqrt(length(sl))))
}

# BL multi-view builder --------------------------------------------------------------
kmv_weights <- function(ctx, cl, k, s_stab, sc_t, lam_ann, Sig_ann, delta, p, mode = c("multi", "single", "rawq", "nostab")) {
  mode <- match.arg(mode); n <- ctx$n
  Pi <- as.vector(delta * Sig_ann %*% ctx$wmkt)
  zc <- tapply(sc_t$z, cl, mean); zbar <- mean(sc_t$z)
  if (mode == "single") {
    ord <- order(zc); lo <- ord[1]; hi <- ord[k]
    Pm <- matrix(0, 1, n); Pm[1, cl == hi] <- 1 / sum(cl == hi); Pm[1, cl == lo] <- -1 / sum(cl == lo)
    q <- as.numeric(Pm %*% Pi) + lam_ann * (zc[hi] - zc[lo])
    Om <- matrix(p$tau * Pm %*% Sig_ann %*% t(Pm), 1, 1)
  } else {
    Pm <- t(sapply(1:k, function(c) as.numeric(cl == c) / sum(cl == c)))
    if (mode == "rawq") {   # uncalibrated: view = cluster-mean idiosyncratic momentum spread vs universe (unit-mixing, as in naive practice)
      q <- as.numeric(Pm %*% Pi) + (tapply(sc_t$mom, cl, mean) - mean(sc_t$mom))
    } else q <- as.numeric(Pm %*% Pi) + lam_ann * (zc - zbar)
    base <- diag(p$tau * as.vector(diag(Pm %*% Sig_ann %*% t(Pm))), k)
    Om <- if (mode == "nostab") base else diag(diag(base) / pmax(s_stab, 0.05), k)
  }
  bl_posterior(Pi, Sig_ann, p$tau, Pm, q, Om * p$omega_mult)
}

# the engine ----------------------------------------------------------------------------
run_engine <- function(P, p = default_params(), verbose = FALSE) {
  T <- nrow(P$R); ts <- p$first_t:(min(T - 1, p$last_t)); nA <- ncol(P$R)
  all_models <- c("EW", "MKT", "TAN", "TAN_LW", "MVP_LW", "ERC", "HRP", "BL0", "MOM_EW", "KIO_v1",
                  "KMV", "KMV_k4", "KMV_ic", "KMV_sampleS", "KMV_single", "KMV_rawq", "KMV_nostab", "KMV_TC")
  models <- if (is.null(p$models)) all_models else p$models
  W <- setNames(lapply(models, function(m) matrix(0, length(ts), nA, dimnames = list(P$dates[ts + 1], colnames(P$R)))), models)
  diag_rows <- vector("list", length(ts)); w_prev <- setNames(lapply(models, function(m) rep(0, nA)), models)
  for (ii in seq_along(ts)) {
    t <- ts[ii]; ctx <- make_ctx(P, t, p); n <- ctx$n; el <- ctx$elig
    S_s <- cov(ctx$Rw); lw <- lw_cc(ctx$Rw); S_lw <- lw$Sigma
    delta <- implied_delta(ctx$mktw, ctx$rfm)
    sc36 <- score_at(P$R, P$mkt, t, el, p$Lm, p$Lv_v1)           # v1 features: 36-month vol
    sc12 <- score_at(P$R, P$mkt, t, el, p$Lm, p$Lv)               # new features: 12-month vol
    X36 <- scale(cbind(sc36$mom, sc36$vol)); X12 <- scale(cbind(sc12$mom, sc12$vol))
    put <- function(m, w) { if (m %in% models) { v <- rep(0, nA); v[el] <- w; W[[m]][ii, ] <<- v } }
    di <- list(t = t, date = as.character(P$dates[t]), n = n, delta = delta, lw_int = lw$delta)
    # ---- benchmarks
    put("EW", rep(1 / n, n)); put("MKT", ctx$wmkt)
    mu_h <- colMeans(ctx$Rw) - mean(ctx$rfm)
    put("TAN", max_sharpe(mu_h, S_s, p$cap)$w); put("TAN_LW", max_sharpe(mu_h, S_lw, p$cap)$w)
    put("MVP_LW", min_var(S_lw, p$cap)); put("ERC", erc_weights(S_lw)); put("HRP", hrp_weights(S_lw))
    Pi_s <- as.vector(delta * (12 * S_s) %*% ctx$wmkt)
    put("BL0", max_sharpe(Pi_s, 12 * S_s, p$cap)$w)
    # ---- v1 replication (single view, k fixed, sample covariance, 36m vol)
    if (any(c("KIO_v1", "MOM_EW") %in% models)) {
      set.seed(p$seed + t * 10 + 1); cl <- km(X36, p$k_fixed, 25)$cluster
      zc <- tapply(sc36$z, cl, mean); hi <- which.max(zc); lo <- which.min(zc)
      put("MOM_EW", as.numeric(cl == hi) / sum(cl == hi))
      Pm <- matrix(0, 1, n); Pm[1, cl == hi] <- 1 / sum(cl == hi); Pm[1, cl == lo] <- -1 / sum(cl == lo)
      q <- mean(sc36$mom[cl == hi]) - mean(sc36$mom[cl == lo])
      Sa <- 12 * S_s; Om <- matrix(p$tau * Pm %*% Sa %*% t(Pm), 1, 1) * p$omega_mult
      mu_bl <- bl_posterior(as.vector(delta * Sa %*% ctx$wmkt), Sa, p$tau, Pm, q, Om)
      put("KIO_v1", max_sharpe(mu_bl, Sa, p$cap)$w)
    }
    # ---- proposed family (12-month vol features, LW covariance)
    if (any(grepl("^KMV", models))) {
      Sa_lw <- 12 * S_lw; Sa_s <- 12 * S_s
      set.seed(p$seed + t * 10 + 2); ks <- select_k_stability(X12, p); cl <- ks$sel$cl$cluster; k <- ks$sel$k
      lam <- calib_lambda(P, ctx, p); lam_ann <- max(0, lam["lambda"]) * 12
      di <- c(di, list(k_stab = k, ws = ks$ws[as.character(k)], lambda_m = unname(lam["lambda"]), lambda_t = unname(lam["t"]),
                       stab_min = min(ks$sel$s), cl_sizes = paste(sort(tabulate(cl, k)), collapse = "/")))
      mu <- kmv_weights(ctx, cl, k, ks$sel$s, sc12, lam_ann, Sa_lw, delta, p, "multi")
      put("KMV", max_sharpe(mu, Sa_lw, p$cap)$w)
      if ("KMV_TC" %in% models) {
        wprev <- w_prev[["KMV_TC"]][el]; wprev <- if (sum(wprev) > 0) wprev / sum(wprev) else rep(1 / n, n)
        put("KMV_TC", mv_turnover(mu / 12, S_lw, delta, p$cost_tc, wprev, p$cap)) }
      if ("KMV_k4" %in% models) {
        set.seed(p$seed + t * 10 + 3); c4 <- km(X12, p$k_fixed, 20); s4 <- cluster_stability(X12, c4$cluster, p$k_fixed, p$Bstab)
        put("KMV_k4", max_sharpe(kmv_weights(ctx, c4$cluster, p$k_fixed, s4, sc12, lam_ann, Sa_lw, delta, p, "multi"), Sa_lw, p$cap)$w) }
      if ("KMV_ic" %in% models) {
        set.seed(p$seed + t * 10 + 4); kic <- select_k_ic(P, ctx, p); ci <- km(X12, kic, 20); si <- cluster_stability(X12, ci$cluster, kic, p$Bstab)
        di$k_ic <- kic
        put("KMV_ic", max_sharpe(kmv_weights(ctx, ci$cluster, kic, si, sc12, lam_ann, Sa_lw, delta, p, "multi"), Sa_lw, p$cap)$w) }
      if ("KMV_sampleS" %in% models)
        put("KMV_sampleS", max_sharpe(kmv_weights(ctx, cl, k, ks$sel$s, sc12, lam_ann, Sa_s, delta, p, "multi"), Sa_s, p$cap)$w)
      if ("KMV_single" %in% models)
        put("KMV_single", max_sharpe(kmv_weights(ctx, cl, k, ks$sel$s, sc12, lam_ann, Sa_lw, delta, p, "single"), Sa_lw, p$cap)$w)
      if ("KMV_rawq" %in% models)
        put("KMV_rawq", max_sharpe(kmv_weights(ctx, cl, k, ks$sel$s, sc12, lam_ann, Sa_lw, delta, p, "rawq"), Sa_lw, p$cap)$w)
      if ("KMV_nostab" %in% models)
        put("KMV_nostab", max_sharpe(kmv_weights(ctx, cl, k, ks$sel$s, sc12, lam_ann, Sa_lw, delta, p, "nostab"), Sa_lw, p$cap)$w)
      # keep KMV_TC previous weights drifting properly (set after realisation below)
    }
    diag_rows[[ii]] <- di
    # drift bookkeeping for turnover-aware model
    for (m in models) w_prev[[m]] <- {
      w <- W[[m]][ii, ]; r <- P$R[t + 1, ]; r[is.na(r)] <- 0; g <- w * (1 + r); if (sum(g) > 0) g / sum(g) else w }
  }
  # realised returns & turnover
  oos <- ts + 1
  Rm <- P$R[oos, , drop = FALSE]; Rm[is.na(Rm)] <- 0
  ret <- sapply(models, function(m) rowSums(W[[m]] * Rm))
  to <- sapply(models, function(m) { w <- W[[m]]; tv <- rep(NA_real_, nrow(w))
    for (i in 2:nrow(w)) { g <- w[i - 1, ] * (1 + Rm[i - 1, ]); g <- g / sum(g); tv[i] <- sum(abs(w[i, ] - g)) }; tv })
  rownames(ret) <- rownames(to) <- as.character(P$dates[oos])
  list(models = models, W = W, ret = ret, turnover = to, rf_m = P$rf_m[oos], rf_ann = P$rf_ann[oos], mkt = P$mkt[oos],
       dates = P$dates[oos], diag = diag_rows, params = p)
}
