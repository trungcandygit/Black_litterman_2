# 47_da_response.R -- analyses answering the independent DA Checkpoint 1 report (post hoc, A5)
suppressPackageStartupMessages({library(sandwich)}); source("/home/user/Black_litterman_2/paper2/R/lib.R")
root <- "/home/user/Black_litterman_2"; od <- file.path(root, "paper2/output"); set.seed(20261004)
fl <- list.files(file.path(root, "data/raw"), full.names = TRUE)
dat <- lapply(fl, function(f) { d <- read.csv(f); d$sym <- sub("\\.csv$", "", basename(f)); d })
all_dates <- sort(unique(unlist(lapply(dat, `[[`, "time")))); all_dates <- all_dates[all_dates >= "2024-08-21"]
mat <- function(col) { M <- matrix(NA_real_, length(all_dates), length(dat), dimnames = list(all_dates, sapply(dat, function(d) d$sym[1])))
  for (j in seq_along(dat)) { mi <- match(dat[[j]]$time, all_dates); okm <- !is.na(mi); M[mi[okm], j] <- dat[[j]][[col]][okm] }; M }
Cc <- mat("close"); Oo <- mat("open"); Hh <- mat("high"); Ll <- mat("low"); Vv <- mat("volume"); n_files <- ncol(Cc); keep <- which(colMeans(!is.na(Cc)) >= 0.95)
Cc <- Cc[, keep]; Oo <- Oo[, keep]; Hh <- Hh[, keep]; Ll <- Ll[, keep]; Vv <- Vv[, keep]; nd <- nrow(Cc); ns <- ncol(Cc)
Rd <- rbind(NA, Cc[-1, ] / Cc[-nd, ] - 1); Rd[!is.finite(Rd)] <- NA; DV <- Cc * Vv
tt <- 61:(nd - 5); nt <- length(tt)
adv <- t(sapply(tt, function(t) colMeans(DV[(t - 59):t, , drop = FALSE])))
OVN <- Oo[tt + 1, ] / Cc[tt, ] - 1; INT <- Cc[tt + 1, ] / Oo[tt + 1, ] - 1; CC1 <- Cc[tt + 1, ] / Cc[tt, ] - 1; F5O <- Cc[tt + 5, ] / Oo[tt + 1, ] - 1; F5C <- Cc[tt + 5, ] / Cc[tt, ] - 1
R0 <- Rd[tt, ]
tick <- function(p) ifelse(p < 10, 0.01, ifelse(p < 50, 0.05, 0.10)); refp <- Cc[tt - 1, ]
ceil_px <- floor(refp * 1.07 / tick(refp) + 1e-9) * tick(refp); floor_px <- ceiling(refp * 0.93 / tick(refp) - 1e-9) * tick(refp)
ex_ceil <- !is.na(Cc[tt, ]) & abs(Cc[tt, ] - ceil_px) < 1e-6; ex_floor <- !is.na(Cc[tt, ]) & abs(Cc[tt, ] - floor_px) < 1e-6
r_ceil <- !is.na(R0) & R0 >= 0.065 & Cc[tt, ] >= Hh[tt, ] - 1e-9; r_floor <- !is.na(R0) & R0 <= -0.065 & Cc[tt, ] <= Ll[tt, ] + 1e-9
locked_c <- r_ceil & Oo[tt, ] >= Hh[tt, ] - 1e-9 & Hh[tt, ] <= Ll[tt, ] + 1e-9; locked_f <- r_floor & Oo[tt, ] <= Ll[tt, ] + 1e-9 & Hh[tt, ] <= Ll[tt, ] + 1e-9
ex_ceil[is.na(ex_ceil)] <- FALSE; ex_floor[is.na(ex_floor)] <- FALSE
shift1 <- function(M) { M[is.na(M)] <- FALSE; rbind(NA, M[-nrow(M), ]) }       # previous-day status; the first event-window day has no previous day (NA)
streak <- function(M) { M[is.na(M)] <- FALSE; out <- M & !(shift1(M) %in% TRUE); out[1, ] <- FALSE; matrix(out, nrow(M), ncol(M)) }   # first-day events are dropped from streak groups because their previous day is unobserved
strt_c <- streak(r_ceil); strt_f <- streak(r_floor); exs_c <- streak(ex_ceil); exs_f <- streak(ex_floor)
# benchmark matrices (market = dollar-volume weighted; EW; same-date same-liquidity-tercile non-event control; beta-adjusted)
wm <- function(M) { ok <- is.finite(M) & is.finite(adv); sapply(1:nt, function(i) sum(M[i, ok[i, ]] * adv[i, ok[i, ]]) / sum(adv[i, ok[i, ]])) }
ew <- function(M) rowMeans(M, na.rm = TRUE)
nonev <- !is.na(R0) & abs(R0) < 0.065
ctrl <- function(M) { out <- matrix(NA_real_, nt, ns); for (i in 1:nt) { ok <- which(nonev[i, ] & is.finite(M[i, ]) & is.finite(adv[i, ])); if (length(ok) < 30) next
    ter <- cut(rank(adv[i, ok]) / length(ok), c(0, 1/3, 2/3, 1), labels = FALSE); mu <- tapply(M[i, ok], ter, mean)
    allok <- which(is.finite(adv[i, ])); tq <- cut(sapply(allok, function(j) mean(adv[i, ok] <= adv[i, j])), c(-Inf, 1/3, 2/3, Inf), labels = FALSE); out[i, allok] <- mu[tq] }; out }
mk_d <- sapply(tt, function(t) { a <- colMeans(DV[(t - 59):t, , drop = FALSE]); r <- Rd[(t - 59):t, ]; w <- a / sum(a, na.rm = TRUE); as.vector(r %*% ifelse(is.na(w), 0, w)) })   # 60 x nt market daily returns
beta <- t(sapply(1:nt, function(i) { t <- tt[i]; r <- Rd[(t - 59):t, ]; m <- mk_d[, i]; apply(r, 2, function(x) { ok <- is.finite(x); if (sum(ok) < 40) NA else cov(x[ok], m[ok]) / var(m[ok]) }) }))
mkt_next <- sapply(tt, function(t) { a <- colMeans(DV[(t - 59):t, , drop = FALSE]); w <- a / sum(a, na.rm = TRUE); r <- Rd[t + 1, ]; sum(r * w, na.rm = TRUE) })
top10 <- mean(sapply(tt, function(t) { a <- colMeans(DV[(t - 59):t, , drop = FALSE]); w <- sort(a / sum(a, na.rm = TRUE), decreasing = TRUE); sum(w[1:10], na.rm = TRUE) }))
AR <- list(
  gap_mkt = OVN - wm(OVN), intraday_mkt = INT - wm(INT), cc1_mkt = CC1 - wm(CC1), f5o_mkt = F5O - wm(F5O),
  gap_ctrl = OVN - ctrl(OVN), intraday_ctrl = INT - ctrl(INT), cc1_ctrl = CC1 - ctrl(CC1), f5o_ctrl = F5O - ctrl(F5O),
  gap_ew = OVN - ew(OVN), intraday_ew = INT - ew(INT), cc1_ew = CC1 - ew(CC1), cc1_beta = CC1 - beta * mkt_next)
cl2 <- function(sel, v) { r <- which(sel & is.finite(v)); if (length(r) < 20) return(c(mean_pct = NA, t_twoway = NA, n = length(r))); ii <- row(v)[r]; jj <- col(v)[r]; a <- v[r]; m <- mean(a); e <- a - m; N <- length(a)
  se_d <- sqrt(sum(tapply(e, ii, sum)^2)) / N; se_s <- sqrt(sum(tapply(e, jj, sum)^2)) / N; se_i <- sqrt(sum(e^2)) / N; se2 <- sqrt(max(se_d^2 + se_s^2 - se_i^2, 1e-12)); c(mean_pct = 100 * m, t_twoway = m / se2, n = N) }
ge65 <- !is.na(R0) & R0 >= 0.065; comp5 <- Reduce(`&`, lapply(1:5, function(k) is.finite(Rd[tt + k, ]))); comp5[is.na(comp5)] <- FALSE
groups <- list(`Ceiling: rule-based` = r_ceil, `Ceiling: README-style (return >= 6.5%, no close = high requirement)` = ge65, `Ceiling: rule-based, complete returns t+1..t+5` = r_ceil & comp5, `Floor: rule-based, complete returns t+1..t+5` = r_floor & comp5, `Ceiling: exact tick-rule hit` = ex_ceil, `Ceiling: near-hit (rule-based, not exact)` = r_ceil & !ex_ceil, `Ceiling: locked all day` = locked_c, `Ceiling: first day of streak (rule-based)` = strt_c, `Ceiling: first day of streak (exact)` = exs_c,
  `Floor: rule-based` = r_floor, `Floor: exact tick-rule hit` = ex_floor, `Floor: near-hit (rule-based, not exact)` = r_floor & !ex_floor, `Floor: locked all day` = locked_f, `Floor: first day of streak (rule-based)` = strt_f, `Floor: first day of streak (exact)` = exs_f)
rows <- do.call(rbind, lapply(names(groups), function(g) do.call(rbind, lapply(names(AR), function(m) data.frame(group = g, measure = m, t(cl2(groups[[g]], AR[[m]])), row.names = NULL)))))
write.csv(rows, file.path(od, "tables/C11_da_response_events.csv"), row.names = FALSE)
# carry-forward sensitivity for missing post-event data: missing next-day return = 0
cf <- function(sel) { v <- CC1 - wm(CC1); v2 <- v; miss <- sel & !is.finite(CC1); v2[miss] <- 0 - wm(CC1)[row(v)[miss]]; rbind(cl2(sel, v), cl2(sel & TRUE, v2)) }
cfr <- rbind(data.frame(group = "Ceiling rule-based", variant = c("complete cases", "missing next day = 0 return"), cf(r_ceil)), data.frame(group = "Floor rule-based", variant = c("complete cases", "missing next day = 0 return"), cf(r_floor)))
cfr$n_events_total <- c(rep(sum(r_ceil, na.rm = TRUE), 2), rep(sum(r_floor, na.rm = TRUE), 2)); cfr$n_missing_next_day <- c(rep(sum(r_ceil & !is.finite(CC1), na.rm = TRUE), 2), rep(sum(r_floor & !is.finite(CC1), na.rm = TRUE), 2))
write.csv(cfr, file.path(od, "tables/C12_attrition_sensitivity.csv"), row.names = FALSE)
univ <- data.frame(step = c("Stock-days in the event window (days 61 to nd-5) with a return", "Raw files (HOSE-listed, 2024-08-21 onward)", "Kept: at least 95% non-missing close", "Stock-days (kept)", "Rule-based ceiling closes", "Rule-based floor closes", "Exact tick-rule ceilings", "Exact tick-rule floors", "Top-10 weight share of dollar-volume market (mean)"),
  value = c(sum(is.finite(R0)), n_files, ns, sum(!is.na(Rd)), sum(r_ceil, na.rm = TRUE), sum(r_floor, na.rm = TRUE), sum(ex_ceil, na.rm = TRUE), sum(ex_floor, na.rm = TRUE), top10))
write.csv(univ, file.path(od, "tables/C13_universe_counts.csv"), row.names = FALSE)
# ---- characteristics: MDE, effective number of tests, NW lag sensitivity
Z <- read.csv(file.path(od, "tables/C1_characteristics_FM.csv")); zp <- readRDS(file.path(od, "rds/zoo_panel.rds")); X <- zp$X; Y <- zp$Y
rn <- function(x) { ok <- is.finite(x); r <- rep(NA_real_, length(x)); r[ok] <- qnorm((rank(x[ok]) - 0.5) / sum(ok)); r }
CH <- dimnames(X)[[3]]; sl <- sapply(CH, function(ch) sapply(1:dim(X)[1], function(i) { x <- rn(X[i, , ch]); y <- Y[i, ]; ok <- is.finite(x) & is.finite(y); cov(x[ok], y[ok]) / var(x[ok]) }))
nwt <- function(x, lag) { fit <- lm(x ~ 1); v <- NeweyWest(fit, lag = lag, prewhite = FALSE)[1, 1]; mean(x) / sqrt(v) }
sens <- data.frame(characteristic = CH, t_lag2 = apply(sl, 2, nwt, 2), t_lag4 = apply(sl, 2, nwt, 4), t_lag8 = apply(sl, 2, nwt, 8), t_iid = apply(sl, 2, function(x) mean(x) / (sd(x) / sqrt(length(x)))))
se <- 100 * apply(sl, 2, function(x) sqrt(NeweyWest(lm(x ~ 1), lag = 4, prewhite = FALSE)[1, 1])); sens$se_pct <- se; sens$mde80_pct_per_week <- 2.8 * se
Cmean <- Reduce(`+`, lapply(1:dim(X)[1], function(i) { M <- sapply(CH, function(ch) rn(X[i, , ch])); cor(M, use = "pairwise.complete.obs") })) / dim(X)[1]
ev <- eigen(Cmean, symmetric = TRUE, only.values = TRUE)$values; meff_pr <- sum(ev)^2 / sum(ev^2); meff_lj <- sum(ev >= 1) + sum(ev - floor(ev)); 
write.csv(sens, file.path(od, "tables/C14_characteristics_power_lags.csv"), row.names = FALSE)
fam <- read.csv(file.path(od, "tables/C3_family_control.csv")); pmax_ev <- max(fam$p[23:26])
prog <- data.frame(item = c("Effective number of tests, participation ratio of the characteristic correlation matrix", "Effective number of tests, Li-Ji", "Largest event-test p-value (4 pre-registered)", "Largest programme size m for which all 4 event tests survive Bonferroni at 5%"),
  value = c(meff_pr, meff_lj, pmax_ev, floor(0.05 / pmax_ev)))
write.csv(prog, file.path(od, "tables/C15_programme_multiplicity.csv"), row.names = FALSE)
options(width = 200); print(rows[rows$measure %in% c("gap_mkt", "intraday_mkt", "cc1_mkt", "f5o_mkt", "gap_ctrl", "intraday_ctrl", "cc1_ctrl", "f5o_ctrl"), ], digits = 3, row.names = FALSE)
print(cfr, digits = 3); print(univ); print(sens, digits = 3); print(prog)

# ================= NA-safe rebuild of Tables 1, 5, 6 (response to the independent integrity report; post hoc) =================
mk_t <- sapply(tt, function(t) { a <- adv[t - 60, ]; r <- Rd[t, ]; ok <- is.finite(a) & is.finite(r); sum(r[ok] * a[ok]) / sum(a[ok]) })          # market return on day t (weights: trailing dollar volume)
ter_t <- t(sapply(1:nt, function(i) { out <- rep(NA_integer_, ns); ok <- which(is.finite(adv[i, ])); out[ok] <- cut(rank(adv[i, ok]) / length(ok), c(0, 1/3, 2/3, 1), labels = FALSE); out }))
half_c <- function(sel, first) { r <- which(sel, arr.ind = TRUE); med <- median(r[, 1]); keepm <- matrix(FALSE, nt, ns); rr <- if (first) r[r[, 1] <= med, , drop = FALSE] else r[r[, 1] > med, , drop = FALSE]; keepm[rr] <- TRUE; keepm }
crash <- matrix(mk_t < -0.02, nt, ns); crash[is.na(crash)] <- FALSE
subs <- list()
for (ev in c("Ceiling", "Floor")) { base <- if (ev == "Ceiling") r_ceil else r_floor; lk <- if (ev == "Ceiling") locked_c else locked_f; base[is.na(base)] <- FALSE
  subs[[paste(ev, "all")]] <- base; subs[[paste(ev, "first half (by event date)")]] <- half_c(base, TRUE); subs[[paste(ev, "second half (by event date)")]] <- half_c(base, FALSE)
  subs[[paste(ev, "excluding market-crash days (market < -2%)")]] <- base & !crash; subs[[paste(ev, "locked all day")]] <- base & lk; subs[[paste(ev, "not locked all day")]] <- base & !lk
  for (k in 1:3) subs[[paste(ev, "liquidity tercile", k)]] <- base & (ter_t == k) & !is.na(ter_t) }
rows16 <- do.call(rbind, lapply(names(subs), function(g) do.call(rbind, lapply(c("gap_mkt", "intraday_mkt", "cc1_mkt", "gap_ctrl", "intraday_ctrl", "cc1_ctrl", "f5o_mkt"), function(m) data.frame(sample = g, measure = m, t(cl2(subs[[g]], AR[[m]])), row.names = NULL)))))
write.csv(rows16, file.path(od, "tables/C16_subsamples_nasafe.csv"), row.names = FALSE)
# discontinuity: limit close vs just-below-limit moves (date-clustered OLS on the indicator)
dcmp <- function(sel_t, sel_c, m, label) { v <- AR[[m]]; rt <- which(sel_t & is.finite(v)); rc <- which(sel_c & is.finite(v)); idx <- c(rt, rc); y <- v[idx]; d <- c(rep(1, length(rt)), rep(0, length(rc))); dt <- row(v)[idx]
  fit <- lm(y ~ d); vc <- vcovCL(fit, cluster = dt, type = "HC1"); b <- coef(fit)[2]; data.frame(contrast = label, outcome = m, diff_pct = 100 * b, t_cluster = b / sqrt(vc[2, 2]), n_limit = length(rt), n_comparison = length(rc), row.names = NULL) }
nb_up_56 <- !is.na(R0) & R0 >= 0.05 & R0 < 0.065; nb_up_35 <- !is.na(R0) & R0 >= 0.03 & R0 < 0.05; nb_dn_56 <- !is.na(R0) & R0 <= -0.05 & R0 > -0.065; nb_dn_35 <- !is.na(R0) & R0 <= -0.03 & R0 > -0.05
rc <- r_ceil; rc[is.na(rc)] <- FALSE; rf_ <- r_floor; rf_[is.na(rf_)] <- FALSE
cm <- list(list(rc, nb_up_56, "ceiling vs 5-6.5% up"), list(rc, nb_up_35, "ceiling vs 3-5% up"), list(rf_, nb_dn_56, "floor vs 5-6.5% down"), list(rf_, nb_dn_35, "floor vs 3-5% down"))
rows17 <- do.call(rbind, lapply(cm, function(z) do.call(rbind, lapply(c("gap_mkt", "intraday_mkt", "cc1_mkt", "f5o_mkt"), function(m) dcmp(z[[1]], z[[2]], m, z[[3]])))))
write.csv(rows17, file.path(od, "tables/C17_discontinuity_nasafe.csv"), row.names = FALSE)
# pile-up on the 347 analysed stocks (both tails); returns between consecutive calendar observations
rr <- Rd[!is.na(Rd)]; brk <- c(-Inf, -0.08, -0.071, -0.069, -0.065, -0.06, 0.06, 0.065, 0.069, 0.071, 0.08, Inf)
lab <- c("< -8.0%", "-8.0% to -7.1%", "-7.1% to -6.9%", "-6.9% to -6.5%", "-6.5% to -6.0%", "-6.0% to 6.0%", "6.0% to 6.5%", "6.5% to 6.9%", "6.9% to 7.1%", "7.1% to 8.0%", "> 8.0%")
tb <- table(cut(rr, brk, labels = lab)); pile <- data.frame(range = names(tb), n = as.integer(tb), share_pct = 100 * as.numeric(tb) / length(rr)); write.csv(pile, file.path(od, "tables/C9b_pileup_347.csv"), row.names = FALSE)
cat("pile-up 347 stocks:", length(rr), "\n"); print(pile, digits = 3); print(rows17, digits = 3); print(head(rows16[rows16$measure == "gap_mkt", ], 20), digits = 3)
