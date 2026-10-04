# 01_data.R -- load, clean, validate the 25-bank monthly panel
source("/home/user/Black_litterman_2/paper2/R/lib.R")
root <- "/home/user/Black_litterman_2"
cl <- read.csv(file.path(root, "Data_fetch/bank_monthly_close (6).csv"), check.names = FALSE)
mc <- read.csv(file.path(root, "Data_fetch/bank_monthly_mktcap_bn (7).csv"), check.names = FALSE)
stopifnot(identical(cl$date, mc$date), identical(names(cl), names(mc)))
dates <- as.Date(cl$date); P <- as.matrix(cl[, -1]); MC <- as.matrix(mc[, -1])
stopifnot(all((is.na(P)) == (is.na(MC))))
R <- rbind(NA, P[-1, ] / P[-nrow(P), ] - 1); rownames(R) <- cl$date    # row t = return over month t
MCl <- rbind(NA, MC[-nrow(MC), ]); rownames(MCl) <- cl$date              # lagged cap (start-of-month)
rf_tab <- read.csv(file.path(root, "paper2/data/rf_vgb10y.csv"))
yr <- as.integer(format(dates, "%Y")); yr_use <- pmax(yr, 2015)          # 2014 months use the 2015 value (carry-back)
rf_ann <- rf_tab$vgb10y_pct[match(yr_use, rf_tab$year)] / 100
rf_m <- (1 + rf_ann)^(1 / 12) - 1
# cap-weighted bank-market return (lagged weights among stocks with a return and a lagged cap)
mkt <- sapply(seq_len(nrow(R)), function(t) { ok <- !is.na(R[t, ]) & !is.na(MCl[t, ]); if (sum(ok) == 0) NA else sum(R[t, ok] * MCl[t, ok]) / sum(MCl[t, ok]) })
ew <- rowMeans(R, na.rm = TRUE)
list_out <- list(dates = dates, R = R, MCl = MCl, MC = MC, rf_m = rf_m, rf_ann = rf_ann, mkt = mkt, ew = ew, tickers = colnames(P))
saveRDS(list_out, file.path(root, "paper2/output/rds/panel.rds"))
# data quality table
first_ret <- sapply(seq_len(ncol(R)), function(j) as.character(dates[which(!is.na(R[, j]))[1]]))
dq <- data.frame(ticker = colnames(P), first_return = first_ret, n_returns = colSums(!is.na(R)),
  mean_ann_ret = colMeans(R, na.rm = TRUE) * 12, ann_vol = apply(R, 2, sd, na.rm = TRUE) * sqrt(12),
  min_month = apply(R, 2, min, na.rm = TRUE), max_month = apply(R, 2, max, na.rm = TRUE),
  avg_cap_bn_vnd = colMeans(MC, na.rm = TRUE))
write.csv(dq, file.path(root, "paper2/output/tables/T_A1_data_summary.csv"), row.names = FALSE)
cat("panel:", dim(R), " months", format(range(dates)), "\n"); print(summary(mkt))
print(head(dq, 3))
