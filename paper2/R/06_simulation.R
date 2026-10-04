# 06_simulation.R -- Monte-Carlo size/power study of the rolling pipeline (null and persistent-alpha DGPs)
source("/home/user/Black_litterman_2/paper2/R/02_engine.R"); library(parallel)
root <- "/home/user/Black_litterman_2/paper2"; od <- file.path(root, "output")
P0 <- readRDS(file.path(od, "rds/panel.rds"))
args <- commandArgs(trailingOnly = TRUE); nrep <- if (length(args)) as.integer(args[1]) else 120
levels_s <- c(0, 1, 2)                       # alpha dispersion multiplier (sd of alpha = s * 0.4% per month)
T <- 144; N <- 25
sim_panel <- function(s, seed) {
  set.seed(seed)
  beta <- runif(N, 0.8, 1.2); sdE <- runif(N, 0.035, 0.07); alpha <- s * 0.004 * rnorm(N)
  f <- rnorm(T, 0.008, 0.055); R <- matrix(NA_real_, T, N)
  for (j in 1:N) R[, j] <- alpha[j] + beta[j] * f + rnorm(T, 0, sdE[j])
  R[1, ] <- NA
  MC <- matrix(NA_real_, T, N); MC[1, ] <- exp(rnorm(N, 0, 0.8)) * 50
  for (t in 2:T) MC[t, ] <- MC[t - 1, ] * (1 + R[t, ])
  MCl <- rbind(NA, MC[-T, ])
  mkt <- sapply(1:T, function(t) if (t == 1) NA else sum(R[t, ] * MCl[t, ]) / sum(MCl[t, ]))
  list(dates = P0$dates, R = R, MC = MC, MCl = MCl, rf_m = P0$rf_m, rf_ann = P0$rf_ann, mkt = mkt, tickers = paste0("A", 1:N))
}
mods <- c("EW", "MKT", "TAN_LW", "ERC", "KIO_v1", "KMV")
one <- function(job) {
  Ps <- sim_panel(job$s, 777000 + job$rep); p <- default_params(); p$models <- mods; p$Bstab <- 20
  r <- run_engine(Ps, p); ex <- r$ret - r$rf_m
  sr <- apply(ex, 2, ann_sharpe)
  pv <- sapply(setdiff(mods, "EW"), function(m) { o <- sr_diff_stat(ex[, m], ex[, "EW"]); 2 * pnorm(-abs(o["diff"] / o["se"])) })
  data.frame(s = job$s, rep = job$rep, model = mods, sharpe = sr, d_vs_EW = sr - sr["EW"], p_asym = c(NA, pv[mods[-1]]), row.names = NULL)
}
jobs <- expand.grid(s = levels_s, rep = 1:nrep); jobs <- lapply(seq_len(nrow(jobs)), function(i) as.list(jobs[i, ]))
t0 <- Sys.time(); out <- do.call(rbind, mclapply(jobs, one, mc.cores = 4)); cat("elapsed", format(Sys.time() - t0), "\n")
saveRDS(out, file.path(od, "rds/simulation.rds"))
sm <- do.call(rbind, lapply(split(out, list(out$s, out$model)), function(d) data.frame(s = d$s[1], model = d$model[1],
  mean_sharpe = mean(d$sharpe), mean_d_vs_EW = mean(d$d_vs_EW), sd_d = sd(d$d_vs_EW), pos_share = mean(d$d_vs_EW > 0),
  reject_5pct = mean(d$p_asym < 0.05, na.rm = TRUE), reject_pos = mean(d$p_asym < 0.05 & d$d_vs_EW > 0, na.rm = TRUE))))
rownames(sm) <- NULL; write.csv(sm, file.path(od, "tables/T8_simulation.csv"), row.names = FALSE); print(sm, digits = 3)
