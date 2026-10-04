# SUPERSEDED by R/47_da_response.R for all numbers in manuscript C (see Appendix B); kept for audit. Known issue: NA propagation in the market and control calculations (41), and all-stock population (44).
# 41_limits_robust.R -- post hoc robustness of the price-limit continuation (A4)
source("/home/user/Black_litterman_2/paper2/R/lib.R")
root <- "/home/user/Black_litterman_2"; od <- file.path(root, "paper2/output"); set.seed(20261004)
fl <- list.files(file.path(root, "data/raw"), full.names = TRUE)
dat <- lapply(fl, function(f) { d <- read.csv(f); d$sym <- sub("\\.csv$", "", basename(f)); d })
all_dates <- sort(unique(unlist(lapply(dat, `[[`, "time")))); all_dates <- all_dates[all_dates >= "2024-08-21"]
mat <- function(col) { M <- matrix(NA_real_, length(all_dates), length(dat), dimnames = list(all_dates, sapply(dat, function(d) d$sym[1])))
  for (j in seq_along(dat)) { mi <- match(dat[[j]]$time, all_dates); okm <- !is.na(mi); M[mi[okm], j] <- dat[[j]][[col]][okm] }; M }
Cc <- mat("close"); Oo <- mat("open"); Hh <- mat("high"); Ll <- mat("low"); Vv <- mat("volume")
keep <- which(colMeans(!is.na(Cc)) >= 0.95); Cc <- Cc[, keep]; Oo <- Oo[, keep]; Hh <- Hh[, keep]; Ll <- Ll[, keep]; Vv <- Vv[, keep]
nd <- nrow(Cc); ns <- ncol(Cc); Rd <- rbind(NA, Cc[-1, ] / Cc[-nd, ] - 1); Rd[!is.finite(Rd)] <- NA; DV <- Cc * Vv
cat("max/min daily return:", max(Rd, na.rm = TRUE), min(Rd, na.rm = TRUE), " share |r|>=6.5%:", mean(abs(Rd) >= 0.065, na.rm = TRUE), "\n")
adv <- function(t) colMeans(DV[(t - 59):t, , drop = FALSE])
H <- 20; rows <- list()
for (t in 61:(nd - H)) {
  r <- Rd[t, ]; a <- adv(t); okm <- is.finite(a) & is.finite(r); wm <- a / sum(a[okm])
  ce <- which(is.finite(r) & r >= 0.065 & Cc[t, ] >= Hh[t, ] - 1e-9); fl <- which(is.finite(r) & r <= -0.065 & Cc[t, ] <= Ll[t, ] + 1e-9)
  nonev <- which(is.finite(r) & abs(r) < 0.065 & is.finite(Rd[t + 1, ]))
  # market and control building blocks for this date
  fin <- function(s) is.finite(Oo[t + 1, s]) & is.finite(Cc[t + 5, s]) & colSums(is.na(Rd[(t + 1):(t + 5), s, drop = FALSE])) == 0
  fin20 <- function(s) colSums(is.na(Cc[(t + 1):(t + 20), s, drop = FALSE])) == 0
  mk_cc1 <- sum(wm[okm] * Rd[t + 1, okm]); allok <- which(okm & fin(seq_len(ns)) )
  mk_on <- sum(a[allok] * (Oo[t + 1, allok] / Cc[t, allok] - 1)) / sum(a[allok]); mk_id <- sum(a[allok] * (Cc[t + 1, allok] / Oo[t + 1, allok] - 1)) / sum(a[allok])
  mk_5o <- sum(a[allok] * (Cc[t + 5, allok] / Oo[t + 1, allok] - 1)) / sum(a[allok]); mk_5c <- sum(a[allok] * (Cc[t + 5, allok] / Cc[t, allok] - 1)) / sum(a[allok])
  ter <- cut(rank(a[nonev]) / length(nonev), c(0, 1/3, 2/3, 1), labels = FALSE)
  ctrl_cc1 <- tapply(Rd[t + 1, nonev], ter, mean); ctrl_5o <- tapply((Cc[t + 5, nonev] / Oo[t + 1, nonev] - 1), ter, mean, na.rm = TRUE)
  tert_of <- function(s) { q <- mean(a[nonev] <= a[s]); cut(q, c(-Inf, 1/3, 2/3, Inf), labels = FALSE) }
  mk_row <- function(nm, ss) { ss <- ss[fin(ss)]; if (!length(ss)) return(NULL)
    data.frame(t = t, s = ss, event = nm, ret0 = r[ss], locked = (Oo[t, ss] >= Hh[t, ss] - 1e-9 & Hh[t, ss] <= Ll[t, ss] + 1e-9 & Cc[t, ss] >= Hh[t, ss] - 1e-9) | (Oo[t, ss] <= Ll[t, ss] + 1e-9 & Hh[t, ss] <= Ll[t, ss] + 1e-9),
      ter = sapply(ss, tert_of), mktret_t = mk_cc1 * 0 + sum(wm[okm] * r[okm]),
      ar_cc1 = Rd[t + 1, ss] - mk_cc1, ar_on = Oo[t + 1, ss] / Cc[t, ss] - 1 - mk_on, ar_id = Cc[t + 1, ss] / Oo[t + 1, ss] - 1 - mk_id,
      ar_5o = Cc[t + 5, ss] / Oo[t + 1, ss] - 1 - mk_5o, ar_5c = Cc[t + 5, ss] / Cc[t, ss] - 1 - mk_5c,
      ar_cc1_ctrl = Rd[t + 1, ss] - ctrl_cc1[sapply(ss, tert_of)], ar_5o_ctrl = Cc[t + 5, ss] / Oo[t + 1, ss] - 1 - ctrl_5o[sapply(ss, tert_of)],
      ar_20c = if (t + 20 <= nd) Cc[t + 20, ss] / Cc[t, ss] - 1 - sum(a[allok] * (Cc[t + 20, allok] / Cc[t, allok] - 1), na.rm = TRUE) / sum(a[allok]) else NA, stringsAsFactors = FALSE) }
  rows[[length(rows) + 1]] <- rbind(mk_row("ceiling", ce), mk_row("floor", fl),
    mk_row("near_up_5_6.5", which(is.finite(r) & r >= 0.05 & r < 0.065)), mk_row("near_up_3_5", which(is.finite(r) & r >= 0.03 & r < 0.05)),
    mk_row("near_dn_5_6.5", which(is.finite(r) & r <= -0.05 & r > -0.065)), mk_row("near_dn_3_5", which(is.finite(r) & r <= -0.03 & r > -0.05)))
}
E <- do.call(rbind, rows); saveRDS(E, file.path(od, "rds/limit_events_full.rds"))
cl <- function(d, col) { d <- d[is.finite(d[[col]]), ]; a <- d[[col]]; m <- mean(a); g <- tapply(a - m, d$t, sum); se <- sqrt(sum(g^2)) / length(a); c(mean_pct = 100 * m, t = m / se, n = length(a)) }
summ <- function(d, label) { do.call(rbind, lapply(c("ar_cc1", "ar_on", "ar_id", "ar_5o", "ar_5c", "ar_cc1_ctrl", "ar_5o_ctrl", "ar_20c"), function(col) { o <- cl(d, col); data.frame(sample = label, measure = col, mean_pct = o["mean_pct"], t_cluster = o["t"], n = o["n"], row.names = NULL) })) }
out <- list()
for (ev in c("ceiling", "floor")) { d <- E[E$event == ev, ]; out[[length(out) + 1]] <- summ(d, paste(ev, "all"))
  out[[length(out) + 1]] <- summ(d[d$t <= median(d$t), ], paste(ev, "first half")); out[[length(out) + 1]] <- summ(d[d$t > median(d$t), ], paste(ev, "second half"))
  out[[length(out) + 1]] <- summ(d[d$mktret_t > -0.02, ], paste(ev, "excl. market-crash days (mkt < -2%)")); out[[length(out) + 1]] <- summ(d[d$locked == FALSE, ], paste(ev, "not locked all day"))
  out[[length(out) + 1]] <- summ(d[d$locked == TRUE, ], paste(ev, "locked all day (open=high=low=close)"))
  for (k in 1:3) out[[length(out) + 1]] <- summ(d[d$ter == k, ], paste(ev, "liquidity tercile", k, c("(low)", "(mid)", "(high)")[k])) }
for (ev in c("near_up_5_6.5", "near_up_3_5", "near_dn_5_6.5", "near_dn_3_5")) out[[length(out) + 1]] <- summ(E[E$event == ev, ], ev)
R41 <- do.call(rbind, out); write.csv(R41, file.path(od, "tables/SUPERSEDED_C4_limits_robustness.csv"), row.names = FALSE)
options(width = 220); sel <- R41[R41$measure %in% c("ar_cc1", "ar_on", "ar_id", "ar_5o", "ar_5c", "ar_cc1_ctrl", "ar_5o_ctrl", "ar_20c"), ]
w <- reshape(sel[, c("sample", "measure", "mean_pct")], idvar = "sample", timevar = "measure", direction = "wide"); wt <- reshape(sel[, c("sample", "measure", "t_cluster")], idvar = "sample", timevar = "measure", direction = "wide")
print(w, digits = 3, row.names = FALSE); print(wt, digits = 3, row.names = FALSE); print(table(E$event))
