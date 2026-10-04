# 40_zoo.R -- Paper C: pre-registered characteristic zoo (22 tests) + price-limit events (4 tests), 347 HOSE stocks, weekly cross-sections
source("/home/user/Black_litterman_2/paper2/R/lib.R")
root <- "/home/user/Black_litterman_2"; od <- file.path(root, "paper2/output"); set.seed(20261004)
fl <- list.files(file.path(root, "data/raw"), full.names = TRUE)
dat <- lapply(fl, function(f) { d <- read.csv(f); d$sym <- sub("\\.csv$", "", basename(f)); d })
all_dates <- sort(unique(unlist(lapply(dat, `[[`, "time")))); all_dates <- all_dates[all_dates >= "2024-08-21"]
mat <- function(col) { M <- matrix(NA_real_, length(all_dates), length(dat), dimnames = list(all_dates, sapply(dat, function(d) d$sym[1])))
  for (j in seq_along(dat)) { mi <- match(dat[[j]]$time, all_dates); okm <- !is.na(mi); M[mi[okm], j] <- dat[[j]][[col]][okm] }; M }
Cc <- mat("close"); Oo <- mat("open"); Hh <- mat("high"); Ll <- mat("low"); Vv <- mat("volume")
keep <- which(colMeans(!is.na(Cc)) >= 0.95); Cc <- Cc[, keep]; Oo <- Oo[, keep]; Hh <- Hh[, keep]; Ll <- Ll[, keep]; Vv <- Vv[, keep]
nd <- nrow(Cc); ns <- ncol(Cc)
la <- Sys.getenv("ZOO_LA"); if (nzchar(la)) { cut <- as.integer(la); set.seed(5); k <- (cut + 1):nd; for (nm in c("Cc", "Oo", "Hh", "Ll")) { M <- get(nm); M[k, ] <- M[k, ] * exp(matrix(rnorm(length(k) * ns, 0, 0.05), length(k))); assign(nm, M) }; Vv[k, ] <- Vv[k, ] * runif(length(k) * ns, 0.1, 10) }
Rd <- rbind(NA, Cc[-1, ] / Cc[-nd, ] - 1); Rd[!is.finite(Rd)] <- NA; DV <- Cc * Vv
adv60 <- function(t) colMeans(DV[(t - 59):t, , drop = FALSE])
H5 <- 5; t0 <- 120; ts <- seq(t0, nd - H5, by = H5); nT <- length(ts); cat("stocks", ns, "days", nd, "cross-sections", nT, "\n")
cs_spread <- function(Hs, Ls) { n <- length(Hs); hl <- log(Hs / Ls)^2; b <- hl[-n] + hl[-1]; Hm <- pmax(Hs[-n], Hs[-1]); Lm <- pmin(Ls[-n], Ls[-1]); g <- log(Hm / Lm)^2
  k <- 3 - 2 * sqrt(2); a <- (sqrt(2 * b) - sqrt(b)) / k - sqrt(g / k); S <- 2 * (exp(a) - 1) / (1 + exp(a)); mean(pmax(S, 0), na.rm = TRUE) }
CH <- c("REV1W", "REV1M", "MOM3M", "MOM6M", "IMOM", "VOL", "IVOL", "BETA", "DOWNVOL", "RANGEVOL", "MAX", "MIN", "SKEW", "KURT", "AMIHUD", "LNDVOL", "DVOLCHG", "TURNCHG", "CSSPREAD", "OVERNIGHT", "INTRADAY", "LIMITFREQ")
rn <- function(x) { ok <- is.finite(x); r <- rep(NA_real_, length(x)); r[ok] <- qnorm((rank(x[ok]) - 0.5) / sum(ok)); r }
X <- array(NA_real_, c(nT, ns, length(CH)), dimnames = list(NULL, NULL, CH)); Y <- matrix(NA_real_, nT, ns); LIQ <- matrix(NA_real_, nT, ns)
for (ii in seq_along(ts)) {
  t <- ts[ii]; w60 <- (t - 59):t; w20 <- (t - 19):t; wL <- (t - 114):t
  ok <- which(colSums(is.na(Rd[wL, , drop = FALSE])) == 0 & colSums(is.na(Cc[wL, , drop = FALSE])) == 0 & colSums(is.na(Oo[wL, , drop = FALSE])) == 0 & colSums(Vv[w60, , drop = FALSE] > 0, na.rm = TRUE) >= 50)
  fw <- (t + 1):(t + H5); okf <- ok[colSums(is.na(Rd[fw, ok, drop = FALSE])) == 0]
  a <- adv60(t); wm <- a[okf] / sum(a[okf]); mk <- as.vector(Rd[1:t, okf, drop = FALSE][(t - 114):t, ] %*% wm)   # market proxy over lookback (day t-114..t)
  Rk <- Rd[wL, okf, drop = FALSE]; idx60 <- (nrow(Rk) - 59):nrow(Rk); idx20 <- (nrow(Rk) - 19):nrow(Rk)
  idxM3 <- (nrow(Rk) - 64):(nrow(Rk) - 5); idxM6 <- 1:(nrow(Rk) - 5)
  for (jj in seq_along(okf)) { s <- okf[jj]; r <- Rk[, jj]; r60 <- r[idx60]; m60 <- mk[idx60]
    fit <- lm.fit(cbind(1, m60), r60); res <- r60 - cbind(1, m60) %*% fit$coefficients; vv <- Vv[w60, s]; dv <- DV[w60, s]; pos <- vv > 0
    X[ii, s, "REV1W"] <- prod(1 + r[(length(r) - 4):length(r)]) - 1; X[ii, s, "REV1M"] <- prod(1 + r[idx20]) - 1
    X[ii, s, "MOM3M"] <- prod(1 + r[idxM3]) - 1; X[ii, s, "MOM6M"] <- prod(1 + r[idxM6]) - 1; X[ii, s, "IMOM"] <- prod(1 + r[idxM3] - mk[idxM3]) - 1
    X[ii, s, "VOL"] <- sd(r60); X[ii, s, "IVOL"] <- sd(res); X[ii, s, "BETA"] <- fit$coefficients[2]; X[ii, s, "DOWNVOL"] <- sqrt(mean(pmin(r60, 0)^2))
    X[ii, s, "RANGEVOL"] <- sqrt(mean(log(Hh[w60, s] / Ll[w60, s])^2, na.rm = TRUE) / (4 * log(2)))
    X[ii, s, "MAX"] <- max(r[idx20]); X[ii, s, "MIN"] <- min(r[idx20]); z <- (r60 - mean(r60)) / sd(r60); X[ii, s, "SKEW"] <- mean(z^3); X[ii, s, "KURT"] <- mean(z^4)
    X[ii, s, "AMIHUD"] <- mean(abs(r60[pos]) / dv[pos]); X[ii, s, "LNDVOL"] <- log(mean(dv)); X[ii, s, "DVOLCHG"] <- mean(DV[w20, s]) / mean(dv); X[ii, s, "TURNCHG"] <- mean(Vv[w20, s]) / mean(vv)
    X[ii, s, "CSSPREAD"] <- cs_spread(Hh[w60, s], Ll[w60, s])
    X[ii, s, "OVERNIGHT"] <- mean(Oo[w20, s] / Cc[w20 - 1, s] - 1); X[ii, s, "INTRADAY"] <- mean(Cc[w20, s] / Oo[w20, s] - 1); X[ii, s, "LIMITFREQ"] <- mean(abs(r[idx20]) >= 0.065) }
  yfw <- apply(1 + Rd[fw, okf, drop = FALSE], 2, prod) - 1; mfw <- sum(wm * yfw); Y[ii, okf] <- yfw - mfw; LIQ[ii, okf] <- a[okf]
}
saveRDS(list(X = X, Y = Y, LIQ = LIQ, ts = ts, dates = all_dates), file.path(od, if (nzchar(la)) "rds/zoo_panel_LA.rds" else "rds/zoo_panel.rds")); if (nzchar(la)) quit(save = "no")
# ---- Fama-MacBeth per characteristic
nw_t <- function(x) { x <- x[is.finite(x)]; n <- length(x); fit <- lm(x ~ 1); v <- sandwich::NeweyWest(fit, lag = 4, prewhite = FALSE)[1, 1]; c(mean = mean(x), t = mean(x) / sqrt(v), n = n) }
fm_series <- function(ch, sel = NULL) { sapply(1:nT, function(ii) { x <- rn(X[ii, , ch]); y <- Y[ii, ]; ok <- is.finite(x) & is.finite(y); if (!is.null(sel)) ok <- ok & sel[ii, ]; if (sum(ok) < 30) return(NA_real_); cov(x[ok], y[ok]) / var(x[ok]) }) }
q20 <- t(apply(LIQ, 1, function(a) a > quantile(a, 0.2, na.rm = TRUE))); q20[is.na(q20)] <- FALSE
disc <- 1:floor(nT / 2); conf <- (floor(nT / 2) + 1):nT
quint <- function(ch) { sp <- rep(NA_real_, nT); to <- rep(NA_real_, nT); prevL <- prevS <- NULL
  for (ii in 1:nT) { x <- X[ii, , ch]; y <- Y[ii, ]; ok <- is.finite(x) & is.finite(y); if (sum(ok) < 50) next; r <- rank(x[ok]) / sum(ok); L <- which(ok)[r > 0.8]; S <- which(ok)[r <= 0.2]
    sp[ii] <- mean(y[L]) - mean(y[S]); if (!is.null(prevL)) to[ii] <- (1 - length(intersect(L, prevL)) / length(L)) + (1 - length(intersect(S, prevS)) / length(S)); prevL <- L; prevS <- S }
  list(sp = sp, to = to) }
rows <- lapply(CH, function(ch) { s <- fm_series(ch); a <- nw_t(s); d <- nw_t(s[disc]); cf <- nw_t(s[conf]); l <- nw_t(fm_series(ch, q20)); q <- quint(ch); qs <- nw_t(q$sp); qn <- q$sp - 0.0025 * ifelse(is.na(q$to), 0, q$to) * 2; qnt <- nw_t(qn)
  data.frame(characteristic = ch, slope_pct_per_week = 100 * a["mean"], t_nw = a["t"], n_weeks = a["n"], t_disc = d["t"], t_conf = cf["t"], slope_disc_pct = 100 * d["mean"], slope_conf_pct = 100 * cf["mean"], t_excl_illiq = l["t"],
    quintile_spread_pct = 100 * qs["mean"], quintile_t = qs["t"], quintile_net25_pct = 100 * qnt["mean"], quintile_net_t = qnt["t"], turnover_both_legs = mean(q$to, na.rm = TRUE)) })
Z <- do.call(rbind, rows); rownames(Z) <- NULL; Z$p <- 2 * pt(-abs(Z$t_nw), df = Z$n_weeks - 1)
# ---- price-limit events
fwd1 <- function(t) Rd[t + 1, ]; evt <- list()
mk_all <- sapply(1:nd, function(t) { if (t < 61) return(NA_real_); a <- adv60(t); r <- Rd[t, ]; ok <- is.finite(r) & is.finite(a); sum(r[ok] * a[ok]) / sum(a[ok]) })
cum5 <- function(t, s) prod(1 + Rd[(t + 1):(t + 5), s]) - 1; mcum5 <- function(t) prod(1 + mk_all[(t + 1):(t + 5)]) - 1
ev <- list(ceiling = list(), floor = list())
for (t in 61:(nd - 5)) { r <- Rd[t, ]; ce <- which(is.finite(r) & r >= 0.065 & Cc[t, ] >= Hh[t, ] - 1e-9); fl <- which(is.finite(r) & r <= -0.065 & Cc[t, ] <= Ll[t, ] + 1e-9)
  for (nm in c("ceiling", "floor")) { ss <- if (nm == "ceiling") ce else fl; if (!length(ss)) next
    ss <- ss[is.finite(Rd[t + 1, ss]) & colSums(is.na(Rd[(t + 1):(t + 5), ss, drop = FALSE])) == 0]
    if (length(ss)) ev[[nm]][[length(ev[[nm]]) + 1]] <- data.frame(t = t, s = ss, ar1 = Rd[t + 1, ss] - mk_all[t + 1], ar5 = sapply(ss, function(s) cum5(t, s)) - mcum5(t)) } }
clus <- function(d, col) { a <- d[[col]]; m <- mean(a); g <- tapply(a - m, d$t, sum); se <- sqrt(sum(g^2)) / length(a); c(mean = m, se = se, t = m / se, n = length(a), n_dates = length(g)) }
EV <- do.call(rbind, lapply(c("ceiling", "floor"), function(nm) { d <- do.call(rbind, ev[[nm]]); do.call(rbind, lapply(c("ar1", "ar5"), function(col) { o <- clus(d, col); h1 <- clus(d[d$t <= median(d$t), ], col); h2 <- clus(d[d$t > median(d$t), ], col)
  data.frame(event = nm, horizon = c(ar1 = "t+1", ar5 = "t+1..t+5")[col], mean_ar_pct = 100 * o["mean"], t_cluster = o["t"], n_events = o["n"], n_dates = o["n_dates"], t_first_half = h1["t"], t_second_half = h2["t"]) })) }))
rownames(EV) <- NULL; EV$p <- 2 * pnorm(-abs(EV$t_cluster))
# baseline: unconditional mean abnormal return of all stock-days (sanity)
base <- mean(unlist(lapply(61:(nd - 5), function(t) mean(Rd[t + 1, ], na.rm = TRUE) - mk_all[t + 1])), na.rm = TRUE)
# ---- family-wide control (26 tests)
fam <- data.frame(test = c(Z$characteristic, paste(EV$event, EV$horizon)), t = c(Z$t_nw, EV$t_cluster), p = c(Z$p, EV$p), t_disc = c(Z$t_disc, EV$t_first_half), t_conf = c(Z$t_conf, EV$t_second_half),
  slope = c(Z$slope_pct_per_week, EV$mean_ar_pct))
fam$p_bh <- p.adjust(fam$p, "BH"); fam$p_holm <- p.adjust(fam$p, "holm"); fam$hlz3 <- abs(fam$t) >= 3
fam$sign_agree <- sign(fam$t_disc) == sign(fam$t_conf); fam$conf_sig <- abs(fam$t_conf) > 1.96 & fam$sign_agree
fam$survives <- fam$p_bh < 0.05 & fam$conf_sig
write.csv(Z, file.path(od, "tables/C1_characteristics_FM.csv"), row.names = FALSE); write.csv(EV, file.path(od, "tables/C2_price_limit_events.csv"), row.names = FALSE); write.csv(fam, file.path(od, "tables/C3_family_control.csv"), row.names = FALSE)
options(width = 220); print(Z[, c("characteristic", "slope_pct_per_week", "t_nw", "t_disc", "t_conf", "t_excl_illiq", "quintile_spread_pct", "quintile_t", "quintile_net25_pct", "turnover_both_legs")], digits = 3)
print(EV, digits = 3); cat("baseline mean next-day AR (pct):", 100 * base, "\n"); print(fam[order(fam$p), c("test", "t", "p_bh", "t_disc", "t_conf", "survives")], digits = 3)
