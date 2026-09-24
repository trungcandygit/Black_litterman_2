# Extensions for revision round 2: price effects, volatility vs spreads, naming timing of near-miss stocks.
suppressPackageStartupMessages({ library(data.table); library(fixest) })
setwd("/Users/nguyenvantrung/Downloads/Python for Algorithmic Trading/NCKH/BAI FTSE2/FTSE2_new")
# rebuild daily data exactly as in analysis.R (same filters)
source_lines <- readLines("code/analysis.R")
end_prep <- grep("^# ---------------------------------------------------------------- matched control sample", source_lines)[1] - 1
eval(parse(text = source_lines[1:end_prep]))
dt[, grp := fcase(treated == 1, "included", near == 1, "nearmiss", default = "control")]

# ---- 1. price effects: market-adjusted abnormal returns (benchmark = equal-weight mean of control stocks each day)
bench <- dt[grp == "control", .(rm = mean(ret, na.rm = TRUE)), by = date]
dt <- merge(dt, bench, by = "date")
dt[, ar := ret - rm]
events <- data.table(event = c("Announcement", "Confirmation", "Constituent list", "Effective"),
                     d = as.IDate(c("2025-10-07", "2026-04-07", "2026-08-21", "2026-09-21")))
tdays <- sort(unique(dt$date))
car_one <- function(ev_d, a, b) {
  i0 <- match(min(tdays[tdays >= ev_d]), tdays)
  win <- tdays[max(1, i0 + a):min(length(tdays), i0 + b)]
  dt[date %in% win & grp != "control", .(car = sum(ar, na.rm = TRUE)), by = .(symbol, grp)]
}
car_tab <- rbindlist(lapply(seq_len(nrow(events)), function(k) rbindlist(lapply(list(c(-1, 1), c(-1, 5), c(0, 20)), function(w) {
  x <- car_one(events$d[k], w[1], w[2])
  x[, .(event = events$event[k], window = sprintf("[%d,%d]", w[1], w[2]), mean_car = mean(car), se = sd(car) / sqrt(.N), t = mean(car) / (sd(car) / sqrt(.N)), n = .N), by = grp]
}))))
car_tab <- car_tab[!(event == "Effective" & window == "[0,20]")]
fwrite(car_tab, "output/table8_car_events.csv")
# long-window cumulative abnormal return, announcement to 23 Sep 2026
long <- dt[date >= as.IDate("2025-10-07") & grp != "control", .(car = sum(ar, na.rm = TRUE)), by = .(symbol, grp)][
  , .(mean_car = mean(car), se = sd(car) / sqrt(.N), n = .N), by = grp]
fwrite(long, "output/table8b_car_long.csv")

# ---- 2. volatility and spreads
wk[, period := fcase(week < D_ANN, "P0", week < D_CONF, "P1", week < D_LIST, "P2", default = "P3")]
wk[, `:=`(P1 = as.integer(period == "P1"), P2 = as.integer(period == "P2"), P3 = as.integer(period == "P3"))]
wk[, labsret := log(absret + 1e-6)]
v1 <- feols(labsret ~ treated:P1 + treated:P2 + treated:P3 + near:P1 + near:P2 + near:P3 | symbol + week, data = wk, cluster = ~symbol)
v2 <- feols(cs ~ treated:P1 + treated:P2 + treated:P3 + near:P1 + near:P2 + near:P3 + labsret | symbol + week, data = wk, cluster = ~symbol)
v3 <- feols(lamihud ~ treated:P1 + treated:P2 + treated:P3 + near:P1 + near:P2 + near:P3 + labsret | symbol + week, data = wk, cluster = ~symbol)
vt <- rbindlist(lapply(list(abs_return = v1, cs_given_vol = v2, amihud_given_vol = v3), function(m) { ct <- coeftable(m)
  data.table(term = rownames(ct), est = ct[, 1], se = ct[, 2], p = ct[, 4], n = nobs(m)) }), idcol = "model")
fwrite(vt, "output/table9_volatility_spreads.csv")

# ---- 3. naming timing of near-miss stocks (press-reported lists: Nov 2025 list named SAB, DXG, PLX; Apr 2026 list added GEE, BSR and dropped PLX)
D_NOV <- as.IDate("2025-11-13")
wk[, `:=`(early_named = as.integer(symbol %in% c("SAB", "DXG", "PLX")), late_named = as.integer(symbol %in% c("GEE", "BSR")))]
wk[, win := fcase(week < D_ANN, "pre", week < D_NOV, "ann_to_nov", week < D_CONF, "nov_to_apr", default = "after_apr")]
for (w in c("ann_to_nov", "nov_to_apr", "after_apr")) wk[, (paste0("W_", w)) := as.integer(win == w)]
nt <- feols(lamihud ~ early_named:W_ann_to_nov + early_named:W_nov_to_apr + early_named:W_after_apr +
              late_named:W_ann_to_nov + late_named:W_nov_to_apr + late_named:W_after_apr +
              treated:P1 + treated:P2 + treated:P3 | symbol + week, data = wk, cluster = ~symbol)
ntv <- feols(lval ~ early_named:W_ann_to_nov + early_named:W_nov_to_apr + early_named:W_after_apr +
               late_named:W_ann_to_nov + late_named:W_nov_to_apr + late_named:W_after_apr +
               treated:P1 + treated:P2 + treated:P3 | symbol + week, data = wk, cluster = ~symbol)
ntt <- rbindlist(lapply(list(lamihud = nt, lval = ntv), function(m) { ct <- coeftable(m)
  data.table(term = rownames(ct), est = ct[, 1], se = ct[, 2], p = ct[, 4]) }), idcol = "outcome")
fwrite(ntt[grepl("named", term)], "output/table10_naming_timing.csv")
# per-stock near-miss paths (mean log Amihud relative to own pre-period mean, minus control-group change)
ctrl_path <- wk[treated == 0 & near == 0, .(c_l = mean(lamihud)), by = win]
per <- wk[near == 1, .(l = mean(lamihud)), by = .(symbol, win)]
per <- merge(per, ctrl_path, by = "win"); per[, rel := l - c_l]
per[, rel := rel - rel[win == "pre"], by = symbol]
fwrite(dcast(per, symbol ~ win, value.var = "rel")[, .(symbol, ann_to_nov, nov_to_apr, after_apr)], "output/table10b_nearmiss_by_stock.csv")

sink("output/run_summary_extensions.txt")
cat("CAR events:\n"); print(car_tab); cat("\nLong-window CAR:\n"); print(long)
cat("\nVolatility / spreads:\n"); etable(v1, v2, v3)
cat("\nNaming timing:\n"); print(ntt[grepl("named", term)])
cat("\nPer-stock near-miss (log Amihud change vs controls, relative to pre):\n"); print(dcast(per, symbol ~ win, value.var = "rel"))
sink()
cat("DONE\n")
