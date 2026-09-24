# FTSE2 revision round 2 (Stage 4'): analyses requested in ars/stage3prime_review/99_verification_review_report.md
# R2-M1 ITT event study; R2-M2/M3 symmetric windows and CAR estimation windows excluding earlier event windows;
# matched estimates with MatchIt weights; post-announcement drift test; sector-composition check; BSR venue check.
eval(parse(text = readLines("/Users/nguyenvantrung/Downloads/Python for Algorithmic Trading/NCKH/BAI FTSE2/FTSE2_new/code/analysis_revision.R")))
dir.create("output/revision2", showWarnings = FALSE)
tidy2 <- function(m, tag) { ct <- coeftable(m); data.table(spec = tag, term = rownames(ct), est = ct[, 1], se = ct[, 2], p = ct[, ncol(ct)], n = nobs(m)) }

# ---------------------------------------------------------------- ITT event study (pure controls) for the manuscript
fwrite(itt_es_tab, "output/revision2/t_itt_event_study.csv")

# ---------------------------------------------------------------- matched estimates with MatchIt weights
mw <- as.data.table(match.data(m))[, .(symbol, w = weights)]
cm <- merge(clean[symbol %in% matched_syms], mw, by = "symbol")
mw_models <- rbindlist(lapply(c("lamihud", "lval", "cs"), function(y)
  tidy2(feols(as.formula(paste(y, "~", fe3("treated"), "| symbol + week")), data = cm, weights = ~w, cluster = ~symbol), paste0("matched_weighted_", y))))
mw_trend <- tidy2(feols(as.formula(paste("lamihud ~", fe3("treated"), "+ treated:tindex | symbol + week")), data = cm, weights = ~w, cluster = ~symbol), "matched_weighted_trend")
fwrite(rbind(mw_models, mw_trend), "output/revision2/t_matched_weighted.csv")

# ---------------------------------------------------------------- post-announcement drift test (SR3)
clean[, tpost := pmax(0, as.numeric(week - D_ANN) / 7)]
drift <- feols(as.formula(paste("lamihud ~", fe3("treated"), "+ treated:tpost | symbol + week")), data = clean, cluster = ~symbol)
b <- coef(drift); V <- vcov(drift); nm <- paste0("treated:P", 1:3)
drift_steps <- rbindlist(lapply(list(c(2, 1), c(3, 2)), function(ij) { a <- nm[ij[1]]; c0 <- nm[ij[2]]
  d <- b[a] - b[c0]; s <- sqrt(V[a, a] + V[c0, c0] - 2 * V[a, c0]); data.table(contrast = paste(a, "-", c0), diff = d, se = s, p = 2 * pnorm(-abs(d / s))) }))
fwrite(rbind(cbind(part = "coef", tidy2(drift, "post_drift")[, .(term, est, se, p)]), cbind(part = "step", drift_steps[, .(term = contrast, est = diff, se, p)])),
       "output/revision2/t_post_drift.csv")

# ---------------------------------------------------------------- sector composition (SR6): drop bank and broker constituents / ITT members
banks <- c("VCB","BID","VPB","HDB","STB","SHB","SSB","MSB","EIB")
brokers <- c("SSI","VCI","VIX","VND","HCM")
finx <- c(banks, brokers)
sec <- rbind(
  tidy2(feols(as.formula(paste("lamihud ~", fe3("treated"), "| symbol + week")), data = clean[!(treated == 1 & symbol %in% finx)], cluster = ~symbol), "constituents_ex_fin"),
  tidy2(feols(as.formula(paste("lamihud ~", fe3("itt"), "| symbol + week")), data = wk[(itt == 1 | never == 1) & !(itt == 1 & symbol %in% finx)], cluster = ~symbol), "itt_ex_fin"))
fwrite(sec, "output/revision2/t_sector.csv")
cat("Constituents ex fin:", sum(!(intersect(treated27, in_s) %in% finx)), " ITT ex fin:", sum(!(itt_syms %in% finx)), "\n")

# ---------------------------------------------------------------- BSR venue check (named-excluded without BSR)
nb <- feols(as.formula(paste("lamihud ~", fe3("treated"), "+", fe3("named"), "| symbol + week")), data = wk[symbol != "BSR"], cluster = ~symbol)
fwrite(tidy2(nb, "named_ex_BSR"), "output/revision2/t_named_ex_bsr.csv")
bsr_first <- dt[symbol == "BSR", .(first = min(date), n_pre = sum(date < D_ANN), gap = max(diff(as.integer(date))))]
fwrite(bsr_first, "output/revision2/t_bsr_dates.csv")

# ---------------------------------------------------------------- CARs with estimation windows excluding earlier event windows
w_bench <- rd[symbol %in% match_ctrl][mw, on = "symbol", nomatch = 0][, .(matched_w = sum(w * ret, na.rm = TRUE) / sum(w[!is.na(ret)])), by = date]
rd2 <- merge(rd, w_bench, by = "date"); setkey(rd2, symbol, date)
ev_idx <- sapply(events$d, function(d) match(min(tdays[tdays >= d]), tdays))
excl_days <- function(e) { if (e == 1) return(as.IDate(character(0)))
  unlist(lapply(1:(e - 1), function(j) as.character(tdays[max(1, ev_idx[j] - 1):min(length(tdays), ev_idx[j] + 20)]))) }
car_port2 <- function(gsyms, bmk) {
  rbindlist(lapply(seq_len(nrow(events)), function(e) {
    i0 <- ev_idx[e]
    est_days <- setdiff(as.character(tdays[max(1, i0 - 130):(i0 - 11)]), excl_days(e))
    est_days <- as.IDate(est_days)
    x <- rd2[symbol %in% gsyms & date %in% tdays[max(1, i0 - 160):min(length(tdays), i0 + 20)]]
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
      data.table(event = events$event[e], window = sprintf("[%d,%d]", w[1], w[2]), benchmark = bmk, est_days = length(est_days),
                 car = sum(p[date %in% wd]$ar), t_portfolio = sum(p[date %in% wd]$ar) / (s_est * sqrt(L)),
                 t_cross = mean(cs$car) / (sd(cs$car) / sqrt(nrow(cs))), n = nrow(cs))
    }))
  }))
}
b4 <- c("ew", "matched_w", "topsize", "market_model")
car2 <- rbind(
  cbind(group = "constituent", rbindlist(lapply(b4, function(b) car_port2(treated27, b)))),
  cbind(group = "itt_nov_list", rbindlist(lapply(b4, function(b) car_port2(itt_syms, b)))),
  cbind(group = "named_excluded", rbindlist(lapply(b4, function(b) car_port2(named_excl, b)))))
fwrite(car2, "output/revision2/t3_car_portfolio_clean_est.csv")

sink("output/revision2/run_summary_revision2.txt")
cat("ITT event study:\n"); print(itt_es_tab); cat("\nPretrend:\n"); print(pre_w)
cat("\nMatched weighted:\n"); print(rbind(mw_models, mw_trend)); cat("\nPost drift:\n"); print(drift_steps); print(tidy2(drift, "post_drift"))
cat("\nSector:\n"); print(sec); cat("\nNamed ex BSR:\n"); print(tidy2(nb, "named_ex_BSR")); print(bsr_first)
cat("\nCAR clean est:\n"); print(car2)
sink()
cat("DONE2\n")
