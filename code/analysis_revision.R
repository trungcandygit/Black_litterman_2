# FTSE2 revision round 1 (Stage 4): analyses requested in ars/stage3_review/02_editorial_decision_and_roadmap.md
# RR1 intention-to-treat on the pre-announcement eligible list; predicted constituents
# RR2 groups rebuilt from all public FTSE lists; named-but-excluded stocks removed from controls
# RR3/RR4 portfolio (calendar-time) CAR tests under four benchmarks
# SR1 pre-window sensitivity; SR2 wild cluster bootstrap; SR3 level-shift tests; RR6 selection windows by FTSE data cut-off
src <- readLines("code/analysis.R")
cut <- grep("^# -+ matched control sample", src)[1] - 1
eval(parse(text = src[1:cut]))
dir.create("output/revision", showWarnings = FALSE)
set.seed(20260925)

# ---------------------------------------------------------------- public FTSE lists
# Nov 2025 preliminary list (screened on data as of 31 Dec 2024): The Investor, 4 Mar 2026; Viet Nam News, 13 Nov 2025
nov_list <- c("VIC","VHM","HPG","MSN","VCB","VNM","SSI","STB","VIX","VJC","VRE","VCI","SHB","VND","GEX",
              "KBC","KDH","FRT","DGC","EIB","HUT","DXG","DPM","PLX","PDR","SAB","DIG","KDC")
# Apr 2026 list (screened on data as of 31 Dec 2025): The Investor, 8 Apr 2026 = Nov list - PLX + 5 additions
apr_list <- c(setdiff(nov_list, "PLX"), "BID","FPT","NVL","GEE","BSR")
named_excl <- setdiff(union(nov_list, apr_list), treated27)
late_named <- c("GEE","BSR")
in_s <- unique(wk$symbol)
cat("Nov list in sample:", sum(nov_list %in% in_s), "of", length(nov_list), " missing:", setdiff(nov_list, in_s), "\n")
cat("Named-excluded in sample:", paste(sort(intersect(named_excl, in_s)), collapse = " "), "\n")

wk[, `:=`(named = as.integer(symbol %in% named_excl), itt = as.integer(symbol %in% nov_list))]
dt[, named := as.integer(symbol %in% named_excl)]
wk[, grp := fcase(treated == 1, "constituent", named == 1, "named_excluded", default = "control")]
dt[, grp := fcase(treated == 1, "constituent", named == 1, "named_excluded", default = "control")]
elig2 <- elig[symbol %in% keep]
elig2[, grp := fcase(symbol %in% treated27, "constituent", symbol %in% named_excl, "named_excluded", default = "control")]
cat("Group sizes:\n"); print(elig2[, .N, by = grp])

tidy <- function(m, tag) { ct <- coeftable(m); data.table(spec = tag, term = rownames(ct), est = ct[, 1], se = ct[, 2], p = ct[, ncol(ct)], n = nobs(m)) }
fe3 <- function(v) paste(paste0(v, ":P", 1:3), collapse = " + ")

# ---------------------------------------------------------------- descriptives (Table 1)
t1 <- wk[period == "P0_pre", .(stock_weeks = .N, amihud = mean(amihud), lval = mean(lval), cs_pct = mean(cs) * 100, absret_pct = mean(absret) * 100), by = grp]
t1 <- merge(wk[, .(stocks = uniqueN(symbol)), by = grp], t1, by = "grp")
fwrite(t1, "output/revision/t1_descriptives.csv")

# ---------------------------------------------------------------- clean baseline (RR2)
clean <- wk[named == 0]
base_models <- lapply(c("lamihud", "lval", "cs"), function(y) feols(as.formula(paste(y, "~", fe3("treated"), "| symbol + week")), data = clean, cluster = ~symbol))
names(base_models) <- c("lamihud", "lval", "cs")
# matched sample rebuilt from clean controls
mdat <- elig2[grp != "named_excluded"]; mdat[, treated := as.integer(grp == "constituent")]
m <- matchit(treated ~ lval_pre + log(px) + vol_pre, data = mdat, method = "nearest", ratio = 3, replace = TRUE, distance = "glm")
matched_syms <- as.data.table(match.data(m))$symbol
match_ctrl <- setdiff(matched_syms, treated27)
bal <- as.data.table(summary(m)$sum.all, keep.rownames = "variable")[, .(variable, treated_mean = `Means Treated`, control_mean_all = `Means Control`, smd_all = `Std. Mean Diff.`)]
bal <- merge(bal, as.data.table(summary(m)$sum.matched, keep.rownames = "variable")[, .(variable, control_mean_matched = `Means Control`, smd_matched = `Std. Mean Diff.`)], by = "variable")
fwrite(bal, "output/revision/tA1_balance.csv")
cat("Matched controls:", length(match_ctrl), "\n")
match_models <- lapply(c("lamihud", "lval", "cs"), function(y) feols(as.formula(paste(y, "~", fe3("treated"), "| symbol + week")), data = clean[symbol %in% matched_syms], cluster = ~symbol))
names(match_models) <- names(base_models)
t2 <- rbind(rbindlist(lapply(names(base_models), function(y) tidy(base_models[[y]], paste0("clean_", y)))),
            rbindlist(lapply(names(match_models), function(y) tidy(match_models[[y]], paste0("matched_", y)))))
fwrite(t2, "output/revision/t2_baseline_clean.csv")

# ---------------------------------------------------------------- ITT and predicted constituents (RR1)
itt_all <- lapply(c("lamihud", "lval"), function(y) feols(as.formula(paste(y, "~", fe3("itt"), "| symbol + week")), data = wk, cluster = ~symbol))
# ITT with controls restricted to stocks never named and never included
wk[, never := as.integer(itt == 0 & treated == 0 & named == 0)]
itt_pure <- lapply(c("lamihud", "lval"), function(y) feols(as.formula(paste(y, "~", fe3("itt"), "| symbol + week")), data = wk[itt == 1 | never == 1], cluster = ~symbol))
# predicted constituents: top 27 stocks by pre-announcement mean log trading value
pred_syms <- elig2[order(-lval_pre)][1:27]$symbol
wk[, pred := as.integer(symbol %in% pred_syms)]
pred_m <- lapply(c("lamihud", "lval"), function(y) feols(as.formula(paste(y, "~", fe3("pred"), "| symbol + week")), data = wk, cluster = ~symbol))
cat("Predicted constituents overlap with actual:", length(intersect(pred_syms, treated27)), "; with Nov list:", length(intersect(pred_syms, nov_list)), "\n")
t_itt <- rbind(tidy(itt_all[[1]], "itt_all_lamihud"), tidy(itt_all[[2]], "itt_all_lval"),
               tidy(itt_pure[[1]], "itt_pure_lamihud"), tidy(itt_pure[[2]], "itt_pure_lval"),
               tidy(pred_m[[1]], "pred_lamihud"), tidy(pred_m[[2]], "pred_lval"))
# ITT split: listed stocks that became constituents vs not
wk[, itt_in := as.integer(itt == 1 & treated == 1)][, itt_out := as.integer(itt == 1 & treated == 0)]
itt_split <- feols(as.formula(paste("lamihud ~", fe3("itt_in"), "+", fe3("itt_out"), "| symbol + week")), data = wk[itt == 1 | never == 1], cluster = ~symbol)
t_itt <- rbind(t_itt, tidy(itt_split, "itt_split_lamihud"))
fwrite(t_itt, "output/revision/t_itt.csv")
itt_es <- feols(lamihud ~ i(relm, itt, ref = -1) | symbol + week, data = wk[itt == 1 | never == 1], cluster = ~symbol)
w_itt <- wald(itt_es, keep = "relm::-[0-9]+:", print = FALSE)
itt_es_tab <- data.table(term = names(coef(itt_es)), est = coef(itt_es), se = se(itt_es))
itt_es_tab[, relm := as.integer(sub(".*::(-?[0-9]+):.*", "\\1", term))]
fwrite(itt_es_tab, "output/revision/t_itt_event_study.csv")

# ---------------------------------------------------------------- event study with clean controls + named-excluded (Figure 1)
es2 <- lapply(c("lamihud", "lval"), function(y) feols(as.formula(paste(y, "~ i(relm, treated, ref = -1) + i(relm, named, ref = -1) | symbol + week")), data = wk, cluster = ~symbol))
names(es2) <- c("lamihud", "lval")
es2_tab <- rbindlist(lapply(names(es2), function(y) { ct <- coeftable(es2[[y]]); data.table(outcome = y, term = rownames(ct), est = ct[, 1], se = ct[, 2], p = ct[, 4]) }))
es2_tab[, group := fifelse(grepl(":named", term), "named_excluded", "constituent")]
es2_tab[, relm := as.integer(sub(".*::(-?[0-9]+):.*", "\\1", term))]
fwrite(es2_tab, "output/revision/t_event_study.csv")
pre_w <- rbindlist(lapply(names(es2), function(y) rbindlist(lapply(c("treated", "named"), function(g) {
  w <- wald(es2[[y]], keep = paste0("relm::-[0-9]+:", g, "$"), print = FALSE); data.table(outcome = y, group = g, F = w$stat, p = w$p) }))))
pre_w <- rbind(pre_w, data.table(outcome = "lamihud", group = "itt", F = w_itt$stat, p = w_itt$p))
es_m <- lapply(c("lamihud", "lval"), function(y) feols(as.formula(paste(y, "~ i(relm, treated, ref = -1) | symbol + week")), data = clean[symbol %in% matched_syms], cluster = ~symbol))
for (j in 1:2) { w <- wald(es_m[[j]], keep = "relm::-[0-9]+:", print = FALSE); pre_w <- rbind(pre_w, data.table(outcome = c("lamihud", "lval")[j], group = "treated_matched_sample", F = w$stat, p = w$p)) }
fwrite(data.table(term = names(coef(es_m[[1]])), est = coef(es_m[[1]]), se = se(es_m[[1]])), "output/revision/t_event_study_matched.csv")
fwrite(pre_w, "output/revision/t_pretrend_wald.csv")

# ---------------------------------------------------------------- two-group model and naming timing (RR2, RR6)
two <- lapply(c("lamihud", "lval"), function(y) feols(as.formula(paste(y, "~", fe3("treated"), "+", fe3("named"), "| symbol + week")), data = wk, cluster = ~symbol))
t_two <- rbind(tidy(two[[1]], "two_lamihud"), tidy(two[[2]], "two_lval"))
# windows keyed to FTSE screening cut-offs: W1 = announcement to 31 Dec 2025 (inside the data window FTSE screened for the April list)
wk[, `:=`(W1 = as.integer(week >= D_ANN & week <= as.IDate("2025-12-31")),
          W2 = as.integer(week > as.IDate("2025-12-31") & week < D_CONF),
          W3 = as.integer(week >= D_CONF))]
wk[, `:=`(early = as.integer(named == 1 & !(symbol %in% late_named)), late = as.integer(symbol %in% late_named))]
nt <- feols(lamihud ~ treated:W1 + treated:W2 + treated:W3 + early:W1 + early:W2 + early:W3 + late:W1 + late:W2 + late:W3 | symbol + week, data = wk, cluster = ~symbol)
t_two <- rbind(t_two, tidy(nt, "naming_timing_lamihud"))
fwrite(t_two, "output/revision/t8_named_excluded.csv")
ctrl_path <- wk[grp == "control", .(c_l = mean(lamihud)), by = .(win = fcase(week < D_ANN, "pre", W1 == 1, "W1", W2 == 1, "W2", default = "W3"))]
per <- wk[named == 1, .(l = mean(lamihud)), by = .(symbol, win = fcase(week < D_ANN, "pre", W1 == 1, "W1", W2 == 1, "W2", default = "W3"))]
per <- merge(per, ctrl_path, by = "win"); per[, rel := l - c_l]; per[, rel := rel - rel[win == "pre"], by = symbol]
per_w <- dcast(per, symbol ~ win, value.var = "rel")[, .(symbol, W1, W2, W3)]
per_w[, first_named := fifelse(symbol %in% late_named, "Apr 2026", "Nov 2025")]
fwrite(per_w[order(first_named, symbol)], "output/revision/t8c_named_by_stock.csv")

# ---------------------------------------------------------------- robustness on clean sample (Table 7) + SR1, SR3
rob <- list()
szmap <- elig2[, .(symbol, szq = cut(lval_pre, quantile(lval_pre, c(0, 1/3, 2/3, 1)), include.lowest = TRUE, labels = FALSE))]
cl2 <- merge(clean, szmap, by = "symbol")
rob$size_week_fe <- feols(as.formula(paste("lamihud ~", fe3("treated"), "| symbol + szq^week")), data = cl2, cluster = ~symbol)
rob$twoway <- feols(as.formula(paste("lamihud ~", fe3("treated"), "| symbol + week")), data = clean, cluster = ~symbol + week)
rob$drop_vin <- feols(as.formula(paste("lamihud ~", fe3("treated"), "| symbol + week")), data = clean[!symbol %in% c("VIC", "VHM", "VRE", "VPL")], cluster = ~symbol)
clean[, tindex := as.numeric(week - min(week)) / 7]
rob$trend <- feols(as.formula(paste("lamihud ~", fe3("treated"), "+ treated:tindex | symbol + week")), data = clean, cluster = ~symbol)
rob$matched_trend <- feols(as.formula(paste("lamihud ~", fe3("treated"), "+ treated:tindex | symbol + week")), data = clean[symbol %in% matched_syms], cluster = ~symbol)
rob$lval_trend <- feols(as.formula(paste("lval ~", fe3("treated"), "+ treated:tindex | symbol + week")), data = clean, cluster = ~symbol)
rob$drop_julaug2025 <- feols(as.formula(paste("lamihud ~", fe3("treated"), "| symbol + week")), data = clean[!(week >= as.IDate("2025-06-30") & week < as.IDate("2025-09-01"))], cluster = ~symbol)
rob$vol_control <- feols(as.formula(paste("lamihud ~", fe3("treated"), "+ log(absret) | symbol + week")), data = clean[absret > 0], cluster = ~symbol)
pl <- clean[week < D_ANN][, fake := as.integer(week >= as.IDate("2025-04-07"))]
rob$placebo <- feols(lamihud ~ treated:fake | symbol + week, data = pl, cluster = ~symbol)
t7 <- rbindlist(lapply(names(rob), function(k) tidy(rob[[k]], k)))
fwrite(t7, "output/revision/t7_robustness.csv")
# SR3 level shifts: P2 - P1 and P3 - P2
ls_tab <- rbindlist(lapply(list(baseline = base_models$lamihud, trend = rob$trend), function(mm) {
  b <- coef(mm); V <- vcov(mm); nm <- paste0("treated:P", 1:3)
  rbindlist(lapply(list(c(2, 1), c(3, 2)), function(ij) { a <- nm[ij[1]]; c0 <- nm[ij[2]]
    d <- b[a] - b[c0]; s <- sqrt(V[a, a] + V[c0, c0] - 2 * V[a, c0]); data.table(contrast = paste(a, "-", c0), diff = d, se = s, p = 2 * pnorm(-abs(d / s))) }))
}), idcol = "spec")
fwrite(ls_tab, "output/revision/t_level_shift.csv")

# ---------------------------------------------------------------- randomization inference on clean controls
pool <- elig2[grp == "control" & lval_pre >= quantile(elig2$lval_pre, 2/3)]$symbol
cat("RI pool size:", length(pool), "\n")
obs <- coef(base_models$lamihud)[paste0("treated:P", 1:3)]
ctrl_only <- clean[treated == 0]
ri <- t(replicate(500, { s <- sample(pool, 24); d <- copy(ctrl_only); d[, ps := as.integer(symbol %in% s)]
  coef(feols(lamihud ~ ps:P1 + ps:P2 + ps:P3 | symbol + week, data = d))[paste0("ps:P", 1:3)] }))
t6 <- data.table(period = paste0("P", 1:3), observed = obs, p_one_sided = sapply(1:3, function(j) mean(ri[, j] <= obs[j])),
                 pseudo_mean = colMeans(ri), pseudo_p05 = apply(ri, 2, quantile, 0.05), pool = length(pool), reps = 500)
fwrite(t6, "output/revision/t6_randomization_inference.csv")

# ---------------------------------------------------------------- SR2 wild cluster bootstrap (WCR, Rademacher, 999 draws)
wcb <- function(dat, y, B = 999) {
  X <- as.matrix(dat[, .(treated * P1, treated * P2, treated * P3)])
  fl <- dat[, .(symbol, week)]
  Xd <- demean(X, fl); yd <- demean(dat[[y]], fl)[, 1]
  cl <- dat$symbol; G <- uniqueN(cl); gid <- match(cl, unique(cl)); N <- nrow(Xd); K <- 3
  crv <- function(Xm, u) { A <- solve(crossprod(Xm)); S <- rowsum(Xm * u, gid); c1 <- G / (G - 1) * (N - 1) / (N - K); A %*% (c1 * crossprod(S)) %*% A }
  bfull <- solve(crossprod(Xd), crossprod(Xd, yd)); ufull <- yd - Xd %*% bfull
  tobs <- as.vector(bfull) / sqrt(diag(crv(Xd, as.vector(ufull))))
  out <- sapply(1:K, function(k) {
    Xr <- Xd[, -k, drop = FALSE]; br <- solve(crossprod(Xr), crossprod(Xr, yd)); fr <- Xr %*% br; er <- as.vector(yd - fr)
    ts <- numeric(B)
    for (bb in seq(1, B, by = 111)) {
      nb <- min(111, B - bb + 1)
      W <- matrix(sample(c(-1, 1), G * nb, replace = TRUE), G, nb)[gid, , drop = FALSE]
      Ys <- as.vector(fr) + demean(W * er, fl)
      Bs <- solve(crossprod(Xd), crossprod(Xd, Ys)); U <- Ys - Xd %*% Bs
      for (j in 1:nb) ts[bb + j - 1] <- Bs[k, j] / sqrt(crv(Xd, U[, j])[k, k])
    }
    mean(abs(ts) >= abs(tobs[k]))
  })
  data.table(term = paste0("treated:P", 1:3), est = as.vector(bfull), t_crve = tobs, p_wild = out, clusters = G, draws = B)
}
t_wcb <- rbind(cbind(sample = "clean", wcb(clean, "lamihud")), cbind(sample = "matched", wcb(clean[symbol %in% matched_syms], "lamihud")))
fwrite(t_wcb, "output/revision/t_wild_bootstrap.csv")

# ---------------------------------------------------------------- segment heterogeneity (clean controls)
seg_large <- c("VCB","VIC","VHM"); seg_mid <- c("BID","VPB","HPG")
clean[, `:=`(sl = as.integer(symbol %in% seg_large), sm = as.integer(symbol %in% seg_mid), ss = as.integer(treated == 1 & !(symbol %in% c(seg_large, seg_mid))))]
seg <- lapply(c("lamihud", "lval"), function(y) feols(as.formula(paste(y, "~", fe3("sl"), "+", fe3("sm"), "+", fe3("ss"), "| symbol + week")), data = clean, cluster = ~symbol))
fwrite(rbind(tidy(seg[[1]], "seg_lamihud"), tidy(seg[[2]], "seg_lval")), "output/revision/t5_segments.csv")

# ---------------------------------------------------------------- volatility and spreads (clean controls)
vol <- list(absret = feols(as.formula(paste("log(absret) ~", fe3("treated"), "| symbol + week")), data = clean[absret > 0], cluster = ~symbol),
            cs_vol = feols(as.formula(paste("cs ~", fe3("treated"), "+ log(absret) | symbol + week")), data = clean[absret > 0], cluster = ~symbol))
fwrite(rbindlist(lapply(names(vol), function(k) tidy(vol[[k]], k))), "output/revision/t6_volatility.csv")

# ---------------------------------------------------------------- rebalancing session (matched controls rebuilt)
dd <- dt[symbol %in% c(matched_syms, treated27) & named == 0 & date >= D_LIST - 60]
dd[, lval_d := log(value_bn + 1e-6)]
dd[, lval_bench := mean(lval_d[date < D_LIST - 5]), by = symbol]
dd[, abn_lval := lval_d - lval_bench]
tdays <- sort(unique(dt$date)); reb_idx <- match(D_REB, tdays)
dd[, rel := match(date, tdays) - reb_idx]
ref_rel <- match(max(tdays[tdays < D_LIST]), tdays) - reb_idx
rr <- feols(as.formula(paste0("lval_d ~ i(rel, treated, ref = ", ref_rel, ") | symbol + date")), data = dd[rel >= ref_rel - 10], cluster = ~symbol)
rr_tab <- data.table(term = names(coef(rr)), est = coef(rr), se = se(rr)); rr_tab[, t := est / se]
fwrite(rr_tab, "output/revision/t4_rebalance_reg.csv")
dd3 <- dt[date >= D_LIST - 60]; dd3[, lval_d := log(value_bn + 1e-6)]
dd3[, lval_bench := mean(lval_d[date < D_LIST - 5]), by = symbol]; dd3[, abn := lval_d - lval_bench]
dd3[, g := fcase(grp == "constituent", "constituent", grp == "named_excluded", "named_excluded", symbol %in% match_ctrl, "matched_control", default = "other")]
fwrite(dd3[date == D_REB & g != "other", .(abn = mean(abn), se = sd(abn) / sqrt(.N), n = .N), by = g], "output/revision/t4b_rebalance_groups.csv")

# ---------------------------------------------------------------- CARs: portfolio tests under four benchmarks (RR3, RR4)
rd <- dt[, .(symbol, date, ret, grp)]
top_ctrl <- elig2[grp == "control" & lval_pre >= quantile(elig2[grp == "control"]$lval_pre, 2/3)]$symbol
bm <- rd[grp == "control", .(ew = mean(ret, na.rm = TRUE)), by = date]
bm <- merge(bm, rd[symbol %in% match_ctrl, .(matched = mean(ret, na.rm = TRUE)), by = date], by = "date")
bm <- merge(bm, rd[symbol %in% top_ctrl, .(topsize = mean(ret, na.rm = TRUE)), by = date], by = "date")
rd <- merge(rd, bm, by = "date"); setkey(rd, symbol, date)
events <- data.table(event = c("Announcement", "Confirmation", "Constituent list", "Effective date"),
                     d = as.IDate(c("2025-10-07", "2026-04-07", "2026-08-21", "2026-09-21")))
wins <- list(c(-1, 1), c(-1, 5), c(0, 20))
car_port <- function(gsyms, bmk) {
  rbindlist(lapply(seq_len(nrow(events)), function(e) {
    i0 <- match(min(tdays[tdays >= events$d[e]]), tdays)
    est_days <- tdays[max(1, i0 - 130):(i0 - 11)]
    x <- rd[symbol %in% gsyms & date %in% tdays[max(1, i0 - 130):min(length(tdays), i0 + 20)]]
    if (bmk == "market_model") {
      co <- x[date %in% est_days, { f <- lm(ret ~ ew); .(a = coef(f)[1], b = coef(f)[2]) }, by = symbol]
      x <- merge(x, co, by = "symbol"); x[, ar := ret - a - b * ew]
    } else x[, ar := ret - get(bmk)]
    p <- x[, .(ar = mean(ar, na.rm = TRUE)), by = date]
    s_est <- sd(p[date %in% est_days]$ar)
    rbindlist(lapply(wins, function(w) {
      if (i0 + w[2] > length(tdays)) return(NULL)
      wd <- tdays[(i0 + w[1]):(i0 + w[2])]; L <- length(wd)
      cs <- x[date %in% wd, .(car = sum(ar, na.rm = TRUE)), by = symbol]
      data.table(event = events$event[e], window = sprintf("[%d,%d]", w[1], w[2]), benchmark = bmk,
                 car = sum(p[date %in% wd]$ar), t_portfolio = sum(p[date %in% wd]$ar) / (s_est * sqrt(L)),
                 t_cross = mean(cs$car) / (sd(cs$car) / sqrt(nrow(cs))), n = nrow(cs))
    }))
  }))
}
itt_syms <- intersect(nov_list, in_s)
car_all <- rbind(
  cbind(group = "constituent", rbindlist(lapply(c("ew", "matched", "topsize", "market_model"), function(b) car_port(treated27, b)))),
  cbind(group = "itt_nov_list", rbindlist(lapply(c("ew", "topsize"), function(b) car_port(itt_syms, b)))),
  cbind(group = "named_excluded", rbindlist(lapply(c("ew", "topsize"), function(b) car_port(named_excl, b)))))
fwrite(car_all, "output/revision/t3_car_portfolio.csv")

sink("output/revision/run_summary_revision.txt")
cat("Groups:\n"); print(elig2[, .N, by = grp]); cat("Matched controls:", length(match_ctrl), " RI pool:", length(pool), "\n")
cat("Predicted-constituent overlap with actual:", length(intersect(pred_syms, treated27)), "\n")
cat("Pretrend Wald:\n"); print(pre_w)
cat("\nBaseline clean:\n"); print(t2); cat("\nITT:\n"); print(t_itt); cat("\nNamed-excluded:\n"); print(t_two)
cat("\nRobustness:\n"); print(t7); cat("\nLevel shifts:\n"); print(ls_tab); cat("\nRI:\n"); print(t6); cat("\nWild bootstrap:\n"); print(t_wcb)
cat("\nCAR portfolio:\n"); print(car_all)
sink()
cat("DONE\n")

# ---------------------------------------------------------------- rebalancing spike vs window baseline (reference-day free)
spike <- function(dat) { d <- copy(dat)[rel >= ref_rel - 10]; d[, `:=`(s0 = as.integer(rel == 0), s1 = as.integer(rel == 1))]
  tidy(feols(lval_d ~ treated:s0 + treated:s1 | symbol + date, data = d, cluster = ~symbol), "spike") }
dall <- dt[(treated == 1 | grp == "control") & date >= D_LIST - 60]; dall[, lval_d := log(value_bn + 1e-6)]; dall[, rel := match(date, tdays) - reb_idx]
dnm <- dt[(named == 1 | grp == "control") & date >= D_LIST - 60]; dnm[, lval_d := log(value_bn + 1e-6)]; dnm[, rel := match(date, tdays) - reb_idx]; dnm[, treated := named]
fwrite(rbind(cbind(controls = "matched", spike(dd)), cbind(controls = "all_clean", spike(dall)), cbind(controls = "named_excluded_vs_clean", spike(dnm))),
       "output/revision/t4c_spike_test.csv")
