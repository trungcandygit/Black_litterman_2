# 49_final_figures.R -- compact journal figures (Figure 1: characteristic t-statistics; Figure 2: next-day returns by day-t move)
suppressPackageStartupMessages(library(ggplot2)); od <- "/home/user/Black_litterman_2/paper2/output"; fd <- file.path(od, "figures")
oi <- c("#0072B2", "#D55E00", "#009E73"); th <- theme_minimal(base_size = 9) + theme(legend.position = "bottom", legend.title = element_blank(), panel.grid.minor = element_blank())
Z <- read.csv(file.path(od, "tables/C1_characteristics_FM.csv"))
zl <- rbind(data.frame(ch = Z$characteristic, t = Z$t_nw, s = "Full sample"), data.frame(ch = Z$characteristic, t = Z$t_disc, s = "Discovery half"), data.frame(ch = Z$characteristic, t = Z$t_conf, s = "Confirmation half"))
zl$ch <- factor(zl$ch, levels = rev(Z$characteristic[order(abs(Z$t_nw))])); zl$s <- factor(zl$s, levels = c("Full sample", "Discovery half", "Confirmation half"))
g1 <- ggplot(zl, aes(t, ch, colour = s, shape = s)) + geom_vline(xintercept = 0, colour = "grey60") + geom_vline(xintercept = c(-1.96, 1.96), linetype = "dashed", colour = "grey50") + geom_vline(xintercept = c(-3, 3), linetype = "dotted", colour = "grey50") +
  geom_point(size = 1.5) + scale_colour_manual(values = oi) + labs(x = "t-statistic", y = NULL) + th
ggsave(file.path(fd, "F1_characteristics.png"), g1, width = 6.5, height = 4.6, dpi = 300, bg = "white")
bins <- read.csv(file.path(od, "tables/C5_rd_bins.csv"))
bins$kind <- ifelse(bins$bin %in% c("CEIL", "FLOOR"), "limit", ifelse(abs(bins$x) > 0.07, "beyond", "interior"))
bins$x[bins$kind == "beyond"] <- sign(bins$x[bins$kind == "beyond"]) * 0.0825
bins$measure <- factor(sub(" \\(open to close\\)", "", bins$measure), levels = c("Overnight gap", "Intraday", "Close to close"))
g2 <- ggplot(bins[bins$kind == "interior", ], aes(x * 100, mean_pct, colour = measure)) + geom_hline(yintercept = 0, colour = "grey60") + geom_pointrange(aes(ymin = lo, ymax = hi), size = 0.2) + geom_line(linewidth = 0.3) +
  geom_pointrange(data = bins[bins$kind == "limit", ], aes(ymin = lo, ymax = hi), size = 0.4, shape = 17) + geom_pointrange(data = bins[bins$kind == "beyond", ], aes(ymin = lo, ymax = hi), size = 0.3, shape = 15) +
  facet_wrap(~measure, ncol = 3, scales = "free_y") + scale_colour_manual(values = oi) + labs(x = "Day-d return (%)", y = "Next-day abnormal return (%)") + theme_minimal(base_size = 9) + theme(legend.position = "none", panel.grid.minor = element_blank())
ggsave(file.path(fd, "F2_break_at_limit.png"), g2, width = 6.5, height = 2.8, dpi = 300, bg = "white")
