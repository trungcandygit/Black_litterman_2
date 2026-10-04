source("/home/user/Black_litterman_2/paper2/R/02_engine.R")
root <- "/home/user/Black_litterman_2/paper2"
P <- readRDS(file.path(root, "output/rds/panel.rds"))
t0 <- Sys.time(); res <- run_engine(P, default_params()); cat("elapsed:", format(Sys.time() - t0), "\n")
saveRDS(res, file.path(root, "output/rds/main_engine.rds"))
cat("OOS steps:", nrow(res$ret), range(as.character(res$dates)), "\n")
ex <- res$ret - res$rf_m
tab <- data.frame(model = res$models, ann_ret = colMeans(res$ret) * 12, ann_vol = apply(res$ret, 2, sd) * sqrt(12),
  sharpe = apply(ex, 2, ann_sharpe), mdd = apply(res$ret, 2, max_dd), turnover = colMeans(res$turnover, na.rm = TRUE))
print(round(tab[, -1], 4), row.names = FALSE); print(tab$model)
