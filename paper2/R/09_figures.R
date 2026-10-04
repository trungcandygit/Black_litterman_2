suppressPackageStartupMessages({library(ggplot2); library(scales)})
source("/home/user/Black_litterman_2/paper2/R/lib.R")
root <- "/home/user/Black_litterman_2/paper2"; od <- file.path(root, "output"); fd <- file.path(od, "figures")
res <- readRDS(file.path(od, "rds/main_engine.rds")); sig <- readRDS(file.path(od, "rds/signal_diag.rds"))
ret <- res$ret; dts <- res$dates; ex <- ret - res$rf_m
oi <- c("#000000", "#E69F00", "#56B4E9", "#009E73", "#D55E00", "#0072B2", "#CC79A7", "#999999")
lab <- c(EW = "1/N", MKT = "Cap-weighted", ERC = "ERC", KIO_v1 = "Single-view BL-K_IO", KMV = "BL-KMV (main)", KMV_TC = "BL-KMV-TC", MVP_LW = "Min-variance (LW)", TAN_LW = "Tangency (LW)")
th <- theme_minimal(base_size = 10) + theme(legend.position = "bottom", panel.grid.minor = element_blank(), legend.title = element_blank())
shade <- annotate("rect", xmin = as.Date("2022-01-01"), xmax = max(dts), ymin = -Inf, ymax = Inf, alpha = 0.07, fill = "grey30")
long <- function(mat, ms) do.call(rbind, lapply(ms, function(m) data.frame(date = dts, model = lab[m], v = mat[, m])))
# F1 cumulative wealth
ms <- c("EW", "MKT", "ERC", "KIO_v1", "KMV", "KMV_TC")
cw <- do.call(rbind, lapply(ms, function(m) data.frame(date = dts, model = lab[m], v = cumprod(1 + ret[, m]))))
cw$model <- factor(cw$model, levels = lab[ms])
p1 <- ggplot(cw, aes(date, v, colour = model, linetype = model)) + shade + geom_line(linewidth = 0.6) + scale_y_log10(breaks = c(1, 2, 4, 8)) +
  scale_colour_manual(values = oi[1:6]) + labs(x = NULL, y = "Wealth (log scale, start = 1)") + th
ggsave(file.path(fd, "F1_wealth.png"), p1, width = 7, height = 3.6, dpi = 300, bg = "white")
# F2 drawdowns
dd <- do.call(rbind, lapply(ms, function(m) { w <- cumprod(1 + ret[, m]); data.frame(date = dts, model = lab[m], v = w / cummax(w) - 1) })); dd$model <- factor(dd$model, levels = lab[ms])
p2 <- ggplot(dd, aes(date, v, colour = model, linetype = model)) + shade + geom_line(linewidth = 0.5) + scale_colour_manual(values = oi[1:6]) +
  scale_y_continuous(labels = percent) + labs(x = NULL, y = "Drawdown") + th
ggsave(file.path(fd, "F2_drawdown.png"), p2, width = 7, height = 3.4, dpi = 300, bg = "white")
# F3 rolling 36m Sharpe difference vs 1/N
rs <- function(m) sapply(36:nrow(ex), function(i) ann_sharpe(ex[(i - 35):i, m]))
rd <- do.call(rbind, lapply(c("KMV", "KIO_v1", "ERC"), function(m) data.frame(date = dts[36:nrow(ex)], model = lab[m], v = rs(m) - rs("EW"))))
p3 <- ggplot(rd, aes(date, v, colour = model)) + geom_hline(yintercept = 0, colour = "grey50") + geom_line(linewidth = 0.6) + scale_colour_manual(values = oi[c(5, 4, 6)]) +
  labs(x = NULL, y = "Rolling 36-month Sharpe minus 1/N Sharpe") + th
ggsave(file.path(fd, "F3_rolling_sharpe_diff.png"), p3, width = 7, height = 3.2, dpi = 300, bg = "white")
# F4 diagnostics
dg <- do.call(rbind, lapply(res$diag, function(d) data.frame(date = as.Date(d$date) , n = d$n, k = d$k_stab, ws = d$ws, lam_t = d$lambda_t, lw = d$lw_int, delta = d$delta)))
dgl <- rbind(data.frame(date = dg$date, panel = "Eligible banks (n)", v = dg$n), data.frame(date = dg$date, panel = "Selected k", v = dg$k),
  data.frame(date = dg$date, panel = "Weighted mean stability", v = dg$ws), data.frame(date = dg$date, panel = "t-stat of score slope (in-window)", v = dg$lam_t),
  data.frame(date = dg$date, panel = "Ledoit-Wolf intensity", v = dg$lw), data.frame(date = dg$date, panel = "Implied risk aversion", v = dg$delta))
p4 <- ggplot(dgl, aes(date, v)) + geom_line(linewidth = 0.5, colour = oi[6]) + facet_wrap(~panel, scales = "free_y", ncol = 2) + labs(x = NULL, y = NULL) + th
ggsave(file.path(fd, "F4_diagnostics.png"), p4, width = 7, height = 5.2, dpi = 300, bg = "white")
# F5 net Sharpe vs cost
cg <- seq(0, 0.01, by = 0.0005)
nets <- do.call(rbind, lapply(c("EW", "ERC", "KIO_v1", "KMV", "KMV_TC"), function(m) do.call(rbind, lapply(c("Full", "P2"), function(pn) {
  idx <- if (pn == "Full") seq_along(dts) else which(dts >= as.Date("2022-01-01")); tv <- ifelse(is.na(res$turnover[idx, m]), 0, res$turnover[idx, m])
  data.frame(cost_bps = cg * 1e4, model = lab[m], period = pn, sr = sapply(cg, function(c) ann_sharpe(ex[idx, m] - c * tv))) }))))
nets$model <- factor(nets$model, levels = lab[c("EW", "ERC", "KIO_v1", "KMV", "KMV_TC")]); nets$period <- ifelse(nets$period == "Full", "Full sample", "Period 2 (2022-2026)")
p5 <- ggplot(nets, aes(cost_bps, sr, colour = model, linetype = model)) + geom_line(linewidth = 0.6) + facet_wrap(~period) + scale_colour_manual(values = oi[c(1, 4, 5, 6, 7)]) +
  labs(x = "Cost per unit of traded value (bps)", y = "Annualised Sharpe ratio") + th
ggsave(file.path(fd, "F5_net_sharpe_cost.png"), p5, width = 7, height = 3.4, dpi = 300, bg = "white")
# F6 sensitivity
se <- read.csv(file.path(od, "tables/T7_sensitivity.csv")); w <- reshape(se[, c("config", "model", "sharpe")], idvar = "config", timevar = "model", direction = "wide")
w$d_ew <- w$sharpe.KMV - w$sharpe.EW; w$d_v1 <- w$sharpe.KMV - w$sharpe.KIO_v1; wl <- rbind(data.frame(config = w$config, vs = "BL-KMV minus 1/N", v = w$d_ew), data.frame(config = w$config, vs = "BL-KMV minus single-view", v = w$d_v1))
wl$config <- factor(wl$config, levels = rev(w$config))
p6 <- ggplot(wl, aes(v, config, colour = vs)) + geom_vline(xintercept = 0, colour = "grey50") + geom_point(size = 2) + scale_colour_manual(values = oi[c(5, 6)]) +
  labs(x = "Sharpe-ratio difference (annualised)", y = NULL) + th
ggsave(file.path(fd, "F6_sensitivity.png"), p6, width = 6.2, height = 4, dpi = 300, bg = "white")
# F7 rolling IC
ic <- rbind(data.frame(date = sig$date, s = "Composite score", v = sig$ic_z), data.frame(date = sig$date, s = "Idiosyncratic momentum", v = sig$ic_mom), data.frame(date = sig$date, s = "Low volatility", v = sig$ic_vol))
ic <- do.call(rbind, lapply(split(ic, ic$s), function(d) { d <- d[order(d$date), ]; d$cum <- cumsum(d$v); d }))
p7 <- ggplot(ic, aes(date, cum, colour = s)) + shade + geom_line(linewidth = 0.6) + scale_colour_manual(values = oi[c(1, 5, 4)]) + labs(x = NULL, y = "Cumulative monthly rank IC") + th
ggsave(file.path(fd, "F7_cumulative_IC.png"), p7, width = 7, height = 3.2, dpi = 300, bg = "white")
# F9 KMV weights
Wk <- res$W$KMV; top <- names(sort(colMeans(Wk), decreasing = TRUE))[1:8]; Wo <- cbind(Wk[, top], Other = rowSums(Wk[, setdiff(colnames(Wk), top)]))
wl2 <- do.call(rbind, lapply(colnames(Wo), function(b) data.frame(date = dts, bank = b, w = Wo[, b]))); wl2$bank <- factor(wl2$bank, levels = rev(colnames(Wo)))
p9 <- ggplot(wl2, aes(date, w, fill = bank)) + geom_area(colour = "white", linewidth = 0.1) + scale_fill_manual(values = c(rev(oi[1:8]), "#DDDDDD")[c(9, 1:8)][1:9]) + scale_y_continuous(labels = percent) + labs(x = NULL, y = "BL-KMV weights") + th
ggsave(file.path(fd, "F9_weights_KMV.png"), p9, width = 7, height = 3.4, dpi = 300, bg = "white")
cat("figures done\n")
