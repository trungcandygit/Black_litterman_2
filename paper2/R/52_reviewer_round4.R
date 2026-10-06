# 52_reviewer_round4.R -- analyses for the fourth set of comments (post hoc):
# C28 tick-free and alternative event definitions; C29 event-time balance by quarter; C30 placebo break dates;
# C31 difference-in-differences around the KRX change with near-limit movers as controls; C32 family-definition sensitivity.
suppressPackageStartupMessages({library(sandwich)})
src <- readLines("/home/user/Black_litterman_2/paper2/R/47_da_response.R")[1:44]; eval(parse(text = src))   # data prep, AR matrices, cl2
dts <- all_dates; open_date <- matrix(dts[tt + 1], nt, ns)
M4 <- c("gap_mkt", "intraday_mkt", "cc1_mkt", "f5o_mkt")
CH <- !is.na(Cc[tt, ]) & Cc[tt, ] >= Hh[tt, ] - 1e-9; CL <- !is.na(Cc[tt, ]) & Cc[tt, ] <= Ll[tt, ] + 1e-9
LK <- !is.na(Oo[tt, ]) & abs(Oo[tt, ] - Hh[tt, ]) < 1e-9 & abs(Hh[tt, ] - Ll[tt, ]) < 1e-9
z <- function(m) { m[is.na(m)] <- FALSE; m }
defs <- list(
  `Ceiling: return >= 6.5%, close = high (baseline)` = z(R0 >= 0.065 & CH),
  `Ceiling: return >= 6.0%, close = high` = z(R0 >= 0.060 & CH),
  `Ceiling: return >= 6.8%, close = high` = z(R0 >= 0.068 & CH),
  `Ceiling: return in [6.7%, 7.3%], close = high` = z(R0 >= 0.067 & R0 <= 0.073 & CH),
  `Ceiling: return >= 6.5%, no close condition` = z(R0 >= 0.065),
  `Ceiling: return >= 6.5%, locked open = high = low = close` = z(R0 >= 0.065 & LK),
  `Floor: return <= -6.5%, close = low (baseline)` = z(R0 <= -0.065 & CL),
  `Floor: return <= -6.0%, close = low` = z(R0 <= -0.060 & CL),
  `Floor: return <= -6.8%, close = low` = z(R0 <= -0.068 & CL),
  `Floor: return in [-7.3%, -6.7%], close = low` = z(R0 <= -0.067 & R0 >= -0.073 & CL),
  `Floor: return <= -6.5%, no close condition` = z(R0 <= -0.065),
  `Floor: return <= -6.5%, locked open = high = low = close` = z(R0 <= -0.065 & LK))
C28 <- do.call(rbind, lapply(names(defs), function(g) do.call(rbind, lapply(M4, function(m) data.frame(definition = g, measure = m, t(cl2(defs[[g]], AR[[m]])), row.names = NULL)))))
write.csv(C28, file.path(od, "tables/C28_event_definitions.csv"), row.names = FALSE)
# C29: event-time balance by calendar quarter of the opening date
rc <- defs[[1]]; rf_ <- defs[[7]]; q <- matrix(paste0(substr(open_date, 1, 4), "-Q", (as.integer(substr(open_date, 6, 7)) - 1) %/% 3 + 1), nt, ns)
qs <- sort(unique(q[rc | rf_]))
C29 <- do.call(rbind, lapply(qs, function(k) { a <- cl2(rc & q == k, AR$gap_mkt); b <- cl2(rf_ & q == k, AR$gap_mkt)
  data.frame(quarter = k, ceiling_n = sum(rc & q == k), ceiling_gap_pct = a["mean_pct"], ceiling_gap_t = a["t_twoway"], floor_n = sum(rf_ & q == k), floor_gap_pct = b["mean_pct"], floor_gap_t = b["t_twoway"], row.names = NULL) }))
write.csv(C29, file.path(od, "tables/C29_event_time_balance.csv"), row.names = FALSE)
# C30: placebo break dates (first trading day of each month); difference post minus pre with independent-period t
months <- unique(substr(dts[dts >= "2025-01-01" & dts <= "2026-04-30"], 1, 7)); brk <- sapply(months, function(mo) min(dts[substr(dts, 1, 7) == mo]))
brk <- unique(sort(c(brk, "2025-05-05")))
dfun <- function(sel, m, b) { post <- open_date >= b; a <- cl2(sel & !post, AR[[m]]); c <- cl2(sel & post, AR[[m]]); sa <- abs(a["mean_pct"] / a["t_twoway"]); sc <- abs(c["mean_pct"] / c["t_twoway"])
  c(diff = unname(c["mean_pct"] - a["mean_pct"]), t = unname((c["mean_pct"] - a["mean_pct"]) / sqrt(sa^2 + sc^2)), pre_n = unname(a["n"]), post_n = unname(c["n"])) }
C30 <- do.call(rbind, lapply(brk, function(b) { x <- dfun(rc, "gap_mkt", b); y <- dfun(rf_, "gap_mkt", b); w <- dfun(rc, "cc1_mkt", b)
  data.frame(break_date = b, krx = b == "2025-05-05", ceiling_gap_diff = x["diff"], ceiling_gap_diff_t = x["t"], ceiling_pre_n = x["pre_n"], ceiling_post_n = x["post_n"], floor_gap_diff = y["diff"], floor_gap_diff_t = y["t"], ceiling_cc1_diff = w["diff"], ceiling_cc1_diff_t = w["t"], row.names = NULL) }))
write.csv(C30, file.path(od, "tables/C30_placebo_breaks.csv"), row.names = FALSE)
# C31: difference-in-differences: limit closes vs 5-6.5% movers closing at the extreme, before and after the KRX change
did <- function(sel_t, sel_c, m, label) { v <- AR[[m]]; post <- open_date >= "2025-05-05"; rt <- which(sel_t & is.finite(v)); rc_ <- which(sel_c & is.finite(v)); idx <- c(rt, rc_)
  y <- v[idx]; D <- c(rep(1, length(rt)), rep(0, length(rc_))); P <- as.numeric(post[idx]); dt <- row(v)[idx]
  fit <- lm(y ~ D * P); vc <- vcovCL(fit, cluster = dt, type = "HC1"); b <- coef(fit); se <- sqrt(diag(vc))
  data.frame(contrast = label, outcome = m, limit_minus_control_pre_pct = 100 * b["D"], t_pre = b["D"] / se["D"], change_after_krx_pct = 100 * b["D:P"], t_change = b["D:P"] / se["D:P"], n_limit = length(rt), n_control = length(rc_), row.names = NULL) }
up56 <- z(R0 >= 0.05 & R0 < 0.065 & CH); dn56 <- z(R0 <= -0.05 & R0 > -0.065 & CL)
C31 <- rbind(did(rc, up56, "gap_mkt", "ceiling vs 5-6.5% up at high"), did(rc, up56, "cc1_mkt", "ceiling vs 5-6.5% up at high"), did(rf_, dn56, "gap_mkt", "floor vs 5-6.5% down at low"), did(rf_, dn56, "cc1_mkt", "floor vs 5-6.5% down at low"))
write.csv(C31, file.path(od, "tables/C31_krx_did.csv"), row.names = FALSE)
# C32: family-definition sensitivity for the four event tests
F3 <- read.csv(file.path(od, "tables/C3_family_control.csv")); F20 <- read.csv(file.path(od, "tables/C20_family_control_week_cluster.csv")); C18 <- read.csv(file.path(od, "tables/C18_inference_horizons.csv"))
pe <- F3$p[23:26]; pc <- F3$p[1:22]; nm <- F3$test[23:26]
p25 <- C18$p_t_ref[C18$cluster == "event date" & C18$outcome == "t+2..t+5"]
fams <- list(
  `Baseline: 22 characteristics + 4 event tests (26), BH` = list(p = c(pc, pe), idx = 23:26, method = "BH"),
  `Event tests only (4), BH` = list(p = pe, idx = 1:4, method = "BH"),
  `26 tests, Holm` = list(p = c(pc, pe), idx = 23:26, method = "holm"),
  `26 tests, Bonferroni` = list(p = c(pc, pe), idx = 23:26, method = "bonferroni"),
  `28 tests: adds days d+2 to d+5 for ceiling and floor, BH` = list(p = c(pc, pe, p25), idx = 23:26, method = "BH"),
  `26 tests, week-clustered event p-values, BH` = list(p = F20$p, idx = 23:26, method = "BH"),
  `Two families: ceiling (2) and floor (2), BH within each` = NULL)
rows <- list()
for (f in names(fams)) { if (is.null(fams[[f]])) { a <- p.adjust(pe[1:2], "BH"); b <- p.adjust(pe[3:4], "BH"); adj <- c(a, b) } else { adj <- p.adjust(fams[[f]]$p, fams[[f]]$method)[fams[[f]]$idx] }
  rows[[length(rows) + 1]] <- data.frame(family = f, test = nm, adjusted_p = adj, below_5pct = adj < 0.05, row.names = NULL) }
C32 <- do.call(rbind, rows); write.csv(C32, file.path(od, "tables/C32_family_sensitivity.csv"), row.names = FALSE)
options(width = 220); print(C28[C28$measure == "gap_mkt", ], digits = 3); print(C29, digits = 3); print(C30, digits = 3); print(C31, digits = 3); print(C32, digits = 3)
