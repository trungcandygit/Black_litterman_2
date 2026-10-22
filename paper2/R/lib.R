# lib.R -- core functions for the BL-KMV study (base R + quadprog/sandwich/lmtest)
suppressPackageStartupMessages({
  library(quadprog); library(sandwich); library(lmtest); library(cluster)
})

# ---------------------------------------------------------------- covariance
# Ledoit & Wolf (2004) constant-correlation shrinkage, analytic intensity
lw_cc <- function(X) {
  T <- nrow(X); n <- ncol(X)
  Xc <- scale(X, scale = FALSE)
  S <- crossprod(Xc) / T
  v <- diag(S); sdv <- sqrt(v)
  R <- S / outer(sdv, sdv)
  rbar <- (sum(R) - n) / (n * (n - 1))
  Fm <- rbar * outer(sdv, sdv); diag(Fm) <- v
  Y <- Xc^2
  PiM <- crossprod(Y) / T - S^2
  pihat <- sum(PiM)
  A <- matrix(0, n, n)           # A[i,j] = theta_{ii,ij}
  for (i in 1:n) {
    M <- Xc * Xc[, i] - matrix(S[i, ], T, n, byrow = TRUE)
    A[i, ] <- colSums((Xc[, i]^2 - S[i, i]) * M) / T
  }
  off <- 0
  for (i in 1:n) for (j in 1:n) if (i != j) off <- off + (sdv[j] / sdv[i]) * A[i, j]
  rhohat <- sum(diag(PiM)) + rbar * off
  gam <- sum((Fm - S)^2)
  kappa <- (pihat - rhohat) / gam
  delta <- max(0, min(1, kappa / T))
  list(Sigma = delta * Fm + (1 - delta) * S, delta = delta, S = S)
}

# ------------------------------------------------------------- optimizers
# long-only, sum-to-one, cap: maximise Sharpe (Cornuejols-Tutuncu QP)
max_sharpe <- function(mu_ex, Sigma, cap = 0.3) {
  n <- length(mu_ex)
  if (max(mu_ex) <= 1e-10) return(list(w = min_var(Sigma, cap), fallback = TRUE))
  sc <- 1e4
  D <- matrix(0, n + 1, n + 1); D[1:n, 1:n] <- 2 * Sigma * sc; D[n + 1, n + 1] <- 1e-8
  Aeq1 <- c(mu_ex, 0)
  Aeq2 <- c(rep(1, n), -1)
  Aineq <- cbind(rbind(diag(n), rep(0, n)),
                 rbind(-diag(n), rep(cap, n)),
                 c(rep(0, n), 1))
  Amat <- cbind(Aeq1, Aeq2, Aineq)
  bvec <- c(1, 0, rep(0, n), rep(0, n), 0)
  sol <- tryCatch(solve.QP(D, rep(0, n + 1), Amat, bvec, meq = 2), error = function(e) NULL)
  if (is.null(sol) || sol$solution[n + 1] <= 1e-10)
    return(list(w = min_var(Sigma, cap), fallback = TRUE))
  y <- pmax(sol$solution[1:n], 0)
  list(w = y / sum(y), fallback = FALSE)
}

min_var <- function(Sigma, cap = 0.3) {
  n <- nrow(Sigma); sc <- 1e4
  Amat <- cbind(rep(1, n), diag(n), -diag(n))
  bvec <- c(1, rep(0, n), rep(-cap, n))
  sol <- tryCatch(solve.QP(2 * Sigma * sc + diag(1e-8, n), rep(0, n), Amat, bvec, meq = 1),
                  error = function(e) NULL)
  if (is.null(sol)) return(rep(1 / n, n))
  w <- pmax(sol$solution, 0); w / sum(w)
}

# mean-variance utility with L1 turnover cost: max w'mu - g/2 w'Sw - c*|w-w0|_1
mv_turnover <- function(mu_ex, Sigma, gamma, cost, w0, cap = 0.3) {
  n <- length(mu_ex); sc <- 1
  D <- matrix(0, 2 * n, 2 * n); D[1:n, 1:n] <- gamma * Sigma; D[(n + 1):(2 * n), (n + 1):(2 * n)] <- diag(1e-9, n)
  D[1:n, 1:n] <- D[1:n, 1:n] + diag(1e-10, n)
  d <- c(mu_ex, rep(-cost, n))
  Aeq <- c(rep(1, n), rep(0, n))
  A1 <- cbind(-diag(n), diag(n))                 # u - w >= -w0
  A2 <- cbind(diag(n), diag(n))                  # u + w >=  w0
  A3 <- cbind(diag(n), matrix(0, n, n))          # w >= 0
  A4 <- cbind(-diag(n), matrix(0, n, n))         # -w >= -cap
  A5 <- cbind(matrix(0, n, n), diag(n))          # u >= 0
  Amat <- t(rbind(Aeq, A1, A2, A3, A4, A5))
  bvec <- c(1, -w0, w0, rep(0, n), rep(-cap, n), rep(0, n))
  sol <- tryCatch(solve.QP(D, d, Amat, bvec, meq = 1), error = function(e) NULL)
  if (is.null(sol)) return(rep(1 / n, n))
  w <- pmax(sol$solution[1:n], 0); w / sum(w)
}

erc_weights <- function(Sigma, iter = 500) {
  n <- nrow(Sigma); w <- rep(1 / n, n)
  for (k in 1:iter) {
    rc <- w * as.vector(Sigma %*% w); wn <- w * sqrt(mean(rc) / rc); wn <- wn / sum(wn)
    if (max(abs(wn - w)) < 1e-10) { w <- wn; break }; w <- wn
  }
  w
}

hrp_weights <- function(Sigma) {
  n <- nrow(Sigma); if (n < 3) return(rep(1 / n, n))
  C <- cov2cor(Sigma); d <- sqrt(0.5 * (1 - C)); diag(d) <- 0
  ord <- hclust(as.dist(d), method = "single")$order
  w <- rep(1, n); items <- list(ord)
  cvar <- function(idx) { s <- Sigma[idx, idx, drop = FALSE]; iv <- 1 / diag(s); iv <- iv / sum(iv); as.numeric(t(iv) %*% s %*% iv) }
  while (length(items)) {
    nxt <- list()
    for (it in items) if (length(it) > 1) {
      h <- floor(length(it) / 2); a <- it[1:h]; b <- it[(h + 1):length(it)]
      va <- cvar(a); vb <- cvar(b); al <- 1 - va / (va + vb)
      w[a] <- w[a] * al; w[b] <- w[b] * (1 - al); nxt <- c(nxt, list(a), list(b))
    }
    items <- nxt
  }
  w / sum(w)
}

# ---------------------------------------------------------------- features
# R: T x n matrix of simple returns (rows = months up to and including s), mkt: length-T market return
# momentum "L_m - 1": cumulative idiosyncratic return over months s-L_m..s-1 (skip month s)
feat_mom <- function(R, mkt, s, Lm = 6) {
  idx <- (s - Lm):(s - 1)
  apply(1 + R[idx, , drop = FALSE] - mkt[idx], 2, prod) - 1
}
feat_vol <- function(R, s, Lv = 12, ann = 12) {
  idx <- (s - Lv + 1):s
  apply(R[idx, , drop = FALSE], 2, sd) * sqrt(ann)
}
zs <- function(x) { s <- sd(x); if (!is.finite(s) || s < 1e-12) rep(0, length(x)) else (x - mean(x)) / s }

# ---------------------------------------------------------------- clustering
km <- function(X, k, nstart = 20) kmeans(X, centers = k, nstart = nstart, iter.max = 100)

# Hennig (2007) bootstrap cluster-wise Jaccard stability
cluster_stability <- function(X, cl, k, B = 50, nstart = 5) {
  n <- nrow(X); J <- matrix(NA_real_, B, k)
  for (b in 1:B) {
    ib <- sample.int(n, n, replace = TRUE); ub <- unique(ib)
    if (length(ub) <= k) next
    fb <- tryCatch(kmeans(X[ub, , drop = FALSE], centers = k, nstart = nstart, iter.max = 50)$cluster, error = function(e) NULL)
    if (is.null(fb)) next
    for (c in 1:k) {
      Cc <- which(cl == c); Cc_in <- intersect(Cc, ub)
      if (length(Cc_in) == 0) next
      J[b, c] <- max(sapply(1:k, function(j) {
        Dj <- ub[fb == j]; length(intersect(Cc_in, Dj)) / length(union(Cc_in, Dj)) }))
    }
  }
  s <- colMeans(J, na.rm = TRUE); s[!is.finite(s)] <- 0.5
  s
}

# ---------------------------------------------------------------- BL core
bl_posterior <- function(Pi, Sigma, tau, P, q, Omega) {
  TS <- tau * Sigma; q <- as.numeric(q)
  K <- TS %*% t(P) %*% solve(P %*% TS %*% t(P) + Omega)
  as.vector(Pi + K %*% (q - P %*% Pi))
}

implied_delta <- function(mkt_win, rf_m, lo = 0.5, hi = 10) {
  d <- (mean(mkt_win) - mean(rf_m)) / var(mkt_win)
  min(hi, max(lo, d))
}

# ---------------------------------------------------------------- metrics
ann_sharpe <- function(rex, ann = 12) mean(rex) / sd(rex) * sqrt(ann)
max_dd <- function(r) { w <- cumprod(1 + r); min(w / cummax(c(1, w))[-1] - 1) }
cvar95 <- function(r) { q <- quantile(r, 0.05); mean(r[r <= q]) }
sortino <- function(rex, ann = 12) mean(rex) / sqrt(mean(pmin(rex, 0)^2)) * sqrt(ann)
ceq <- function(r, gamma = 5, ann = 12) { # annualised certainty-equivalent of quadratic-type utility
  ann * (mean(r) - gamma / 2 * var(r)) }

# ---------------------------------------------------------------- inference
nw_cov <- function(Y, L = NULL) {                      # Bartlett-kernel HAC covariance of mean of Y (T x p)
  T <- nrow(Y); Yc <- scale(Y, scale = FALSE); if (is.null(L)) L <- floor(4 * (T / 100)^(2/9))
  G <- crossprod(Yc) / T
  if (L >= 1) for (l in 1:L) { w <- 1 - l / (L + 1); Gl <- crossprod(Yc[-(1:l), , drop = FALSE], Yc[1:(T - l), , drop = FALSE]) / T; G <- G + w * (Gl + t(Gl)) }
  G
}
sr_diff_stat <- function(r1, r2, L = NULL) {            # Sharpe difference and HAC s.e. (delta method, LW 2008 style)
  Y <- cbind(r1, r2, r1^2, r2^2); colnames(Y) <- NULL; T <- nrow(Y); m <- unname(colMeans(Y))
  f <- function(m) m[1] / sqrt(m[3] - m[1]^2) - m[2] / sqrt(m[4] - m[2]^2)
  g <- c(m[3] / (m[3] - m[1]^2)^1.5, -m[4] / (m[4] - m[2]^2)^1.5,
         -0.5 * m[1] / (m[3] - m[1]^2)^1.5, 0.5 * m[2] / (m[4] - m[2]^2)^1.5)
  V <- nw_cov(Y, L); se <- sqrt(as.numeric(t(g) %*% V %*% g) / T)
  c(diff = unname(f(unname(m))), se = se)
}
circ_block_idx <- function(T, b) { nb <- ceiling(T / b); st <- sample.int(T, nb, replace = TRUE)
  idx <- as.vector(sapply(st, function(s) ((s - 1 + 0:(b - 1)) %% T) + 1)); idx[1:T] }
# studentised circular-block bootstrap p-value for H0: SR1 = SR2 (monthly excess returns; result in annualised units)
sr_diff_test <- function(r1, r2, B = 5000, b = NULL, ann = 12) {
  T <- length(r1); if (is.null(b)) b <- max(2, round(T^(1/3)))
  o <- sr_diff_stat(r1, r2); d0 <- o["diff"]; t0 <- d0 / o["se"]
  ts <- numeric(B)
  for (i in 1:B) { ix <- circ_block_idx(T, b); a <- r1[ix]; c2 <- r2[ix]
    oo <- tryCatch(sr_diff_stat(a, c2), error = function(e) c(diff = NA, se = NA))
    ts[i] <- (oo["diff"] - d0) / oo["se"] }
  p_boot <- (1 + sum(abs(ts) >= abs(t0), na.rm = TRUE)) / (1 + sum(is.finite(ts)))
  c(diff_ann = unname(d0) * sqrt(ann), t = unname(t0), p_boot = unname(p_boot),
    p_asym = unname(2 * pnorm(-abs(t0))))
}

# Bailey & Lopez de Prado (2014): probabilistic & deflated Sharpe ratio (monthly Sharpe inputs)
psr <- function(rex, sr_star = 0) {
  T <- length(rex); sr <- mean(rex) / sd(rex)
  z <- (rex - mean(rex)) / sd(rex); g3 <- mean(z^3); g4 <- mean(z^4)
  pnorm((sr - sr_star) * sqrt(T - 1) / sqrt(1 - g3 * sr + (g4 - 1) / 4 * sr^2))
}
dsr <- function(rex, n_trials, sr_var_trials) {
  em <- 0.5772156649
  sr_star <- sqrt(sr_var_trials) * ((1 - em) * qnorm(1 - 1 / n_trials) + em * qnorm(1 - 1 / (n_trials * exp(1))))
  list(dsr = psr(rex, sr_star), sr_star_monthly = sr_star)
}

# Hansen (2005) SPA / White (2000) RC via stationary bootstrap. d: T x m performance differences (model_k - benchmark)
spa_test <- function(d, B = 5000, q = 0.1) {
  T <- nrow(d); m <- ncol(d)
  dbar <- colMeans(d)
  # long-run variance of sqrt(T)*dbar by bootstrap
  boot_idx <- function() { ix <- integer(T); ix[1] <- sample.int(T, 1)
    for (t in 2:T) ix[t] <- if (runif(1) < q) sample.int(T, 1) else (ix[t - 1] %% T) + 1; ix }
  DB <- matrix(0, B, m)
  for (b in 1:B) DB[b, ] <- colMeans(d[boot_idx(), , drop = FALSE])
  omega <- apply(DB, 2, sd) * sqrt(T); omega[omega < 1e-12] <- 1e-12
  tstat <- max(sqrt(T) * dbar / omega, 0)
  thr <- -sqrt(2 * log(log(T))) * omega / sqrt(T)
  mu_c <- dbar * (dbar >= thr); mu_l <- pmax(dbar, 0)
  stat_boot <- function(mu) apply(DB, 1, function(x) max(sqrt(T) * (x - dbar + mu) / omega, 0))
  p_rc <- mean(apply(DB, 1, function(x) max(sqrt(T) * (x - dbar) / omega, 0)) >= tstat)
  c(stat = tstat, p_SPAc = mean(stat_boot(mu_c) >= tstat), p_SPAl = mean(stat_boot(mu_l) >= tstat), p_RC = p_rc)
}

hac_alpha <- function(rex_p, rex_m, ann = 12) {
  fit <- lm(rex_p ~ rex_m); vc <- NeweyWest(fit, lag = floor(4 * (length(rex_p) / 100)^(2/9)), prewhite = FALSE)
  ct <- coeftest(fit, vcov. = vc)
  c(alpha_ann = unname(coef(fit)[1]) * ann, t_alpha = ct[1, 3], p_alpha = ct[1, 4], beta = unname(coef(fit)[2]),
    r2 = summary(fit)$r.squared)
}
