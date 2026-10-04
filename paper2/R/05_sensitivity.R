source("/home/user/Black_litterman_2/paper2/R/02_engine.R"); library(parallel)
root <- "/home/user/Black_litterman_2/paper2"; od <- file.path(root, "output")
P <- readRDS(file.path(od, "rds/panel.rds"))
cfgs <- list(
  base = list(), win24 = list(win = 24, Lv_v1 = 24), win48 = list(win = 48, Lv_v1 = 48, first_t = 49),
  cap20 = list(cap = 0.20), cap40 = list(cap = 0.40), cap100 = list(cap = 1.0),
  om05 = list(omega_mult = 0.5), om20 = list(omega_mult = 2), Lm3 = list(Lm = 3), Lm12 = list(Lm = 12),
  thr60 = list(stab_thr = 0.60), thr80 = list(stab_thr = 0.80))
mods <- c("EW", "MKT", "ERC", "KIO_v1", "KMV")
runone <- function(nm) { p <- default_params(); for (k in names(cfgs[[nm]])) p[[k]] <- cfgs[[nm]][[k]]; p$models <- mods
  r <- run_engine(P, p); ex <- r$ret - r$rf_m
  data.frame(config = nm, n_oos = nrow(r$ret), model = mods, sharpe = apply(ex, 2, ann_sharpe), ann_ret = colMeans(r$ret) * 12,
             mdd = apply(r$ret, 2, max_dd), turnover = colMeans(r$turnover, na.rm = TRUE), row.names = NULL) }
out <- do.call(rbind, mclapply(names(cfgs), runone, mc.cores = 4))
write.csv(out, file.path(od, "tables/T7_sensitivity.csv"), row.names = FALSE)
w <- reshape(out[, c("config", "model", "sharpe")], idvar = "config", timevar = "model", direction = "wide")
w$KMV_minus_EW <- w$sharpe.KMV - w$sharpe.EW; w$KMV_minus_KIO <- w$sharpe.KMV - w$sharpe.KIO_v1
print(w, digits = 3)
# trials ledger (all KMV configurations evaluated)
fam8 <- readRDS(file.path(od, "rds/trials.rds"))
sr_all <- c(fam8$sr_var * 0, 0); srs <- out$sharpe[out$model == "KMV"]
ledger <- list(n_trials = 8 + (length(srs) - 1), sr_monthly_sd_hint = NULL)
saveRDS(list(kmv_sensitivity_sharpes = srs, n_sens = length(srs) - 1), file.path(od, "rds/trials_sens.rds"))
