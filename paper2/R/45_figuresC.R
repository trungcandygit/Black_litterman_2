suppressPackageStartupMessages(library(ggplot2)); od <- "/home/user/Black_litterman_2/paper2/output"; fd <- file.path(od, "figures")
oi <- c("#0072B2", "#D55E00", "#009E73"); th <- theme_minimal(base_size = 10) + theme(legend.position = "bottom", legend.title = element_blank(), panel.grid.minor = element_blank())
Z <- read.csv(file.path(od, "tables/C1_characteristics_FM.csv")); zl <- rbind(data.frame(ch = Z$characteristic, t = Z$t_nw, s = "Full sample"), data.frame(ch = Z$characteristic, t = Z$t_disc, s = "Discovery half"), data.frame(ch = Z$characteristic, t = Z$t_conf, s = "Confirmation half"))
zl$ch <- factor(zl$ch, levels = rev(Z$characteristic[order(abs(Z$t_nw))])); zl$s <- factor(zl$s, levels = c("Full sample", "Discovery half", "Confirmation half"))
g1 <- ggplot(zl, aes(t, ch, colour = s, shape = s)) + geom_vline(xintercept = 0, colour = "grey60") + geom_vline(xintercept = c(-1.96, 1.96), linetype = "dashed", colour = "grey50") + geom_vline(xintercept = c(-3, 3), linetype = "dotted", colour = "grey30") +
  geom_point(size = 1.8) + scale_colour_manual(values = oi) + labs(x = "Fama–MacBeth t-statistic (Newey–West, 4 lags); dashed = ±1.96, dotted = ±3.0", y = NULL) + th
ggsave(file.path(fd, "H2_zoo_tstats.png"), g1, width = 7, height = 5.6, dpi = 300, bg = "white")
tw <- read.csv(file.path(od, "tables/C6_twoway_cluster.csv")); tw$se <- abs(tw$mean_pct / tw$t_twoway); tw$measure <- factor(tw$measure, levels = c("overnight gap", "intraday", "close-to-close")); tw$event <- factor(tw$event, levels = c("ceiling", "floor"), labels = c("Closed at ceiling", "Closed at floor"))
g2 <- ggplot(tw, aes(measure, mean_pct, fill = measure)) + geom_hline(yintercept = 0, colour = "grey50") + geom_col(width = 0.6) + geom_errorbar(aes(ymin = mean_pct - 1.96 * se, ymax = mean_pct + 1.96 * se), width = 0.15) + facet_wrap(~event) +
  scale_fill_manual(values = oi) + labs(x = NULL, y = "Next-day abnormal return (%), two-way-clustered 95% interval") + th + theme(legend.position = "none")
ggsave(file.path(fd, "H3_decomposition.png"), g2, width = 7, height = 3.4, dpi = 300, bg = "white"); cat("C figures done\n")
