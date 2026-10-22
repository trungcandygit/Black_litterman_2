# 48_revision.R -- Stage 4 revision analyses answering the round-1 review panel (post hoc, labelled as such; see process/decisions.md A9)
# REV-3 dependence-robust inference for t+1..t+5; REV-1 originally specified t+2..t+5 and split; REV-8 KRX migration split; REV-4 comparison groups with close = high and news/attention proxies;
# REV-18 reference distribution; REV-19 outlier bound.
suppressPackageStartupMessages({library(sandwich)})
src <- readLines("/home/user/Black_litterman_2/paper2/R/47_da_response.R")[1:44]; eval(parse(text = src))   # data prep, AR matrices, cl2 (two-way clustered mean)
dts <- all_dates
mk_all <- sapply(1:nd, function(t) { if (t < 61) return(NA_real_); a <- colMeans(DV[(t - 59):t, , drop = FALSE]); r <- Rd[t, ]; ok <- is.finite(r) & is.finite(a); sum(r[ok] * a[ok]) / sum(a[ok]) })
cumr <- function(t, s, a, b) prod(1 + Rd[(t + a):(t + b), s]) - 1; mcum <- function(t, a, b) prod(1 + mk_all[(t + a):(t + b)]) - 1
build <- function(kind) { out <- list()
  for (t in 61:(nd - 5)) { r <- Rd[t, ]; ss <- if (kind == "ceiling") which(is.finite(r) & r >= 0.065 & Cc[t, ] >= Hh[t, ] - 1e-9) else which(is.finite(r) & r <= -0.065 & Cc[t, ] <= Ll[t, ] + 1e-9)
    if (!length(ss)) next; ss <- ss[is.finite(Rd[t + 1, ss]) & colSums(is.na(Rd[(t + 1):(t + 5), ss, drop = FALSE])) == 0]; if (!length(ss)) next
    out[[length(out) + 1]] <- data.frame(t = t, s = ss, ar1 = Rd[t + 1, ss] - mk_all[t + 1], ar5 = sapply(ss, function(s) cumr(t, s, 1, 5)) - mcum(t, 1, 5), ar25 = sapply(ss, function(s) cumr(t, s, 2, 5)) - mcum(t, 2, 5)) }
  d <- do.call(rbind, out); d$week <- format(as.Date(dts[d$t]), "%G-%V"); d$blk10 <- d$t %/% 10; d$spec_wk <- ifelse(d$t >= 120, (d$t - 120) %/% 5 + 1, NA); d }
EVD <- list(ceiling = build("ceiling"), floor = build("floor"))
cl1 <- function(d, col, by) { a <- d[[col]]; m <- mean(a); g <- tapply(a - m, d[[by]], sum); G <- length(g); se <- sqrt(G / (G - 1)) * sqrt(sum(g^2)) / length(a); c(mean = 100 * m, t = m / se, n = length(a), G = G) }
tref <- function(t, G) 2 * pt(-abs(t), df = G - 1)
rows <- list()
for (ev in names(EVD)) { d <- EVD[[ev]]; med <- median(d$t)
  for (col in c("ar1", "ar5", "ar25")) for (by in c("t", "week", "blk10")) {
    o <- cl1(d, col, by); h1 <- cl1(d[d$t <= med, ], col, by); h2 <- cl1(d[d$t > med, ], col, by)
    rows[[length(rows) + 1]] <- data.frame(event = ev, outcome = c(ar1 = "t+1", ar5 = "t+1..t+5", ar25 = "t+2..t+5")[col], cluster = c(t = "event date", week = "calendar week", blk10 = "10-day block")[by], mean_pct = o["mean"], t = o["t"], G = o["G"], n = o["n"],
      p_t_ref = tref(o["t"], o["G"]), t_first_half = h1["t"], t_second_half = h2["t"], row.names = NULL) } }
C18 <- do.call(rbind, rows); write.csv(C18, file.path(od, "tables/C18_inference_horizons.csv"), row.names = FALSE)
# specified split (weeks 1-39 discovery / 40-79 confirmation of the cross-sectional weekly grid, events from day 120) -- as written in the pre-registration
rows <- list()
for (ev in names(EVD)) { d <- EVD[[ev]]; d <- d[!is.na(d$spec_wk) & d$spec_wk <= 79, ]
  for (col in c("ar1", "ar5", "ar25")) { a <- cl1(d[d$spec_wk <= 39, ], col, "week"); b <- cl1(d[d$spec_wk >= 40, ], col, "week"); o <- cl1(d, col, "week")
    rows[[length(rows) + 1]] <- data.frame(event = ev, outcome = c(ar1 = "t+1", ar5 = "t+1..t+5", ar25 = "t+2..t+5")[col], mean_pct_all = o["mean"], t_all_week_cluster = o["t"], t_weeks_1_39 = a["t"], n_1_39 = a["n"], t_weeks_40_79 = b["t"], n_40_79 = b["n"], row.names = NULL) } }
C19 <- do.call(rbind, rows); write.csv(C19, file.path(od, "tables/C19_spec_split_weeks.csv"), row.names = FALSE)
# survival rule re-evaluated with week-clustered t, t reference, BH across the 26 tests
fam <- read.csv(file.path(od, "tables/C3_family_control.csv")); chp <- fam$p[1:22]
ev4 <- C18[C18$cluster == "calendar week" & C18$outcome %in% c("t+1", "t+1..t+5"), ]
fam2 <- data.frame(test = c(fam$test[1:22], paste(ev4$event, ev4$outcome)), p = c(chp, ev4$p_t_ref), t_conf = c(fam$t_conf[1:22], ev4$t_second_half), t_disc = c(fam$t_disc[1:22], ev4$t_first_half))
fam2$p_bh <- p.adjust(fam2$p, "BH"); fam2$conf_sig <- abs(fam2$t_conf) > 1.96 & sign(fam2$t_conf) == sign(fam2$t_disc); fam2$survives <- fam2$p_bh < 0.05 & fam2$conf_sig
write.csv(fam2, file.path(od, "tables/C20_family_control_week_cluster.csv"), row.names = FALSE)
prog <- data.frame(item = c("Largest event p, normal reference, date cluster (original)", "Largest event p, t reference, event-date cluster", "Largest event p, t reference, calendar-week cluster", "Max programme size, normal/date (original)", "Max programme size, t/date", "Max programme size, t/week"),
  value = c(max(fam$p[23:26]), max(C18$p_t_ref[C18$cluster == "event date" & C18$outcome %in% c("t+1", "t+1..t+5")]), max(ev4$p_t_ref), floor(0.05 / max(fam$p[23:26])), floor(0.05 / max(C18$p_t_ref[C18$cluster == "event date" & C18$outcome %in% c("t+1", "t+1..t+5")])), floor(0.05 / max(ev4$p_t_ref))))
write.csv(prog, file.path(od, "tables/C21_programme_t_reference.csv"), row.names = FALSE)
# ---- KRX migration (5 May 2025): split by the date of the opening that defines the gap
rc <- r_ceil; rc[is.na(rc)] <- FALSE; rf_ <- r_floor; rf_[is.na(rf_)] <- FALSE
open_date <- matrix(dts[tt + 1], nt, ns); post <- open_date >= "2025-05-05"
kr <- list()
for (ev in c("Ceiling", "Floor")) { base <- if (ev == "Ceiling") rc else rf_; for (m in c("gap_mkt", "intraday_mkt", "cc1_mkt", "f5o_mkt")) { a <- cl2(base & !post, AR[[m]]); b <- cl2(base & post, AR[[m]])
    sa <- abs(a["mean_pct"] / a["t_twoway"]); sb <- abs(b["mean_pct"] / b["t_twoway"]); kr[[length(kr) + 1]] <- data.frame(event = ev, measure = m, pre_mean = a["mean_pct"], pre_t = a["t_twoway"], pre_n = a["n"], post_mean = b["mean_pct"], post_t = b["t_twoway"], post_n = b["n"], diff = b["mean_pct"] - a["mean_pct"], diff_t = (b["mean_pct"] - a["mean_pct"]) / sqrt(sa^2 + sb^2), row.names = NULL) } }
C22 <- do.call(rbind, kr); write.csv(C22, file.path(od, "tables/C22_krx_split.csv"), row.names = FALSE)
# ---- comparison groups that also close at the day's high (REV-4 / DA M2)
hi <- !is.na(Cc[tt, ]) & Cc[tt, ] >= Hh[tt, ] - 1e-9; lo <- !is.na(Cc[tt, ]) & Cc[tt, ] <= Ll[tt, ] + 1e-9
nb_up_56 <- !is.na(R0) & R0 >= 0.05 & R0 < 0.065; nb_up_35 <- !is.na(R0) & R0 >= 0.03 & R0 < 0.05; nb_dn_56 <- !is.na(R0) & R0 <= -0.05 & R0 > -0.065; nb_dn_35 <- !is.na(R0) & R0 <= -0.03 & R0 > -0.05
dcmp <- function(sel_t, sel_c, m, label) { v <- AR[[m]]; rt <- which(sel_t & is.finite(v)); rc_ <- which(sel_c & is.finite(v)); idx <- c(rt, rc_); y <- v[idx]; d <- c(rep(1, length(rt)), rep(0, length(rc_))); dt <- row(v)[idx]
  fit <- lm(y ~ d); vc <- vcovCL(fit, cluster = dt, type = "HC1"); b <- coef(fit)[2]; data.frame(contrast = label, outcome = m, diff_pct = 100 * b, t_cluster = b / sqrt(vc[2, 2]), n_limit = length(rt), n_comparison = length(rc_), row.names = NULL) }
cmH <- list(list(rc, nb_up_56 & hi, "ceiling vs 5-6.5% up, close = high"), list(rc, nb_up_35 & hi, "ceiling vs 3-5% up, close = high"), list(rf_, nb_dn_56 & lo, "floor vs 5-6.5% down, close = low"), list(rf_, nb_dn_35 & lo, "floor vs 3-5% down, close = low"))
C23 <- do.call(rbind, lapply(cmH, function(z) do.call(rbind, lapply(c("gap_mkt", "intraday_mkt", "cc1_mkt", "f5o_mkt"), function(m) dcmp(z[[1]], z[[2]], m, z[[3]])))))
write.csv(C23, file.path(od, "tables/C23_discontinuity_close_at_extreme.csv"), row.names = FALSE)
# ---- attention / news-intensity proxies inside ceiling and floor events (no announcement data exist in the sample)
vr <- t(sapply(tt, function(t) Vv[t, ] / colMeans(Vv[(t - 60):(t - 1), , drop = FALSE]))); pr20 <- t(sapply(tt, function(t) Cc[t - 1, ] / Cc[t - 21, ] - 1))
prx <- list(); 
for (ev in c("Ceiling", "Floor")) { base <- if (ev == "Ceiling") rc else rf_
  for (pn in c("volume ratio (day t / prior 60-day mean)", "prior 20-day return (to t-1)")) { x <- if (grepl("volume", pn)) vr else pr20; ok <- base & is.finite(x); cuts <- quantile(x[ok], c(1/3, 2/3)); gp <- ifelse(x <= cuts[1], 1, ifelse(x <= cuts[2], 2, 3))
    for (k in 1:3) for (m in c("gap_mkt", "intraday_mkt", "f5o_mkt")) prx[[length(prx) + 1]] <- data.frame(event = ev, proxy = pn, tercile = k, measure = m, t(cl2(ok & gp == k, AR[[m]])), cut_low = cuts[1], cut_high = cuts[2], row.names = NULL) } }
C24 <- do.call(rbind, prx); write.csv(C24, file.path(od, "tables/C24_attention_proxies.csv"), row.names = FALSE)
# ---- outlier bound: drop events whose stock has any |return| > 8% within +-5 days (corporate-action / listing-day candidates)
big <- abs(Rd) > 0.08; big[is.na(big)] <- FALSE
near_big <- t(sapply(tt, function(t) { idx <- max(1, t - 5):min(nd, t + 5); colSums(big[idx, , drop = FALSE]) > 0 }))
ob <- list(); for (ev in c("Ceiling", "Floor")) { base <- if (ev == "Ceiling") rc else rf_; for (m in c("gap_mkt", "cc1_mkt", "f5o_mkt")) { a <- cl2(base, AR[[m]]); b <- cl2(base & !near_big, AR[[m]]); ob[[length(ob) + 1]] <- data.frame(event = ev, measure = m, all_mean = a["mean_pct"], all_t = a["t_twoway"], all_n = a["n"], excl_mean = b["mean_pct"], excl_t = b["t_twoway"], excl_n = b["n"], row.names = NULL) } }
C25 <- do.call(rbind, ob); write.csv(C25, file.path(od, "tables/C25_outlier_bound.csv"), row.names = FALSE)
options(width = 220); print(C18, digits = 3); print(C19, digits = 3); print(fam2[23:26, ], digits = 3); print(prog); print(C22, digits = 3); print(C23, digits = 3); print(C24[C24$measure == "gap_mkt", ], digits = 3); print(C25, digits = 3)
