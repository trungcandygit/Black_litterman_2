suppressPackageStartupMessages(library(ggplot2))
od <- "/home/user/Black_litterman_2/paper2/output"; fd <- file.path(od, "figures")
oi <- c("#0072B2", "#D55E00", "#009E73", "#E69F00"); th <- theme_minimal(base_size = 10) + theme(legend.position = "bottom", legend.title = element_blank(), panel.grid.minor = element_blank())
sh <- rbind(read.csv(file.path(od, "tables/B2_shares_banks.csv")), read.csv(file.path(od, "tables/B2_shares_broad.csv")))
sh <- sh[sh$component %in% c("anchor", "view", "cov", "cap"), ]; sh$component <- factor(sh$component, levels = c("anchor", "view", "cov", "cap"), labels = c("Anchor", "View", "Covariance", "Cap"))
sh$universe <- factor(sh$universe, levels = c("banks", "broad"), labels = c("25 banks, monthly", "100 liquid stocks, weekly"))
g1 <- ggplot(sh, aes(component, share)) + geom_col(fill = "#56B4E9", width = 0.6) + geom_errorbar(aes(ymin = lo, ymax = hi), width = 0.15) +
  geom_point(aes(y = perm95), shape = 4, size = 2.5, colour = "#D55E00", stroke = 1) + facet_wrap(~universe) + scale_y_continuous(labels = scales::percent, limits = c(0, 1)) +
  labs(x = NULL, y = "Share of Sharpe variance (80 cells)") + th
ggsave(file.path(fd, "G1_shares.png"), g1, width = 7, height = 3.4, dpi = 300, bg = "white")
ct <- rbind(read.csv(file.path(od, "tables/B4_contrasts_banks.csv")), read.csv(file.path(od, "tables/B4_contrasts_broad.csv")))
keep <- c("view:MOM - NONE", "view:LOWVOL - NONE", "view:COMP - NONE", "view:CLUSTER - NONE", "anchor:EW - CAP", "anchor:ERC - CAP", "anchor:SHR - CAP", "cov:LW - SAMPLE", "cap:nocap - capped")
ct <- ct[ct$contrast %in% keep, ]; ct$contrast <- factor(ct$contrast, levels = rev(keep)); ct$universe <- factor(ct$universe, levels = c("banks", "broad"), labels = c("25 banks, monthly", "100 liquid stocks, weekly"))
g2 <- ggplot(ct, aes(diff, contrast)) + geom_vline(xintercept = 0, colour = "grey50") + geom_errorbarh(aes(xmin = lo, xmax = hi), height = 0.2) + geom_point(size = 2, colour = "#D55E00") +
  facet_wrap(~universe, scales = "free_x") + labs(x = "Marginal Sharpe-ratio difference (annualized), 95% block-bootstrap interval", y = NULL) + th
ggsave(file.path(fd, "G2_contrasts.png"), g2, width = 7.2, height = 3.6, dpi = 300, bg = "white")
cl <- rbind(cbind(universe = "25 banks, monthly", read.csv(file.path(od, "tables/B1_cells_banks.csv"))), cbind(universe = "100 liquid stocks, weekly", read.csv(file.path(od, "tables/B1_cells_broad.csv"))))
hm <- aggregate(sharpe ~ universe + anchor + view, cl, mean); hm$view <- factor(hm$view, levels = c("NONE", "MOM", "LOWVOL", "COMP", "CLUSTER")); hm$anchor <- factor(hm$anchor, levels = rev(c("CAP", "EW", "ERC", "SHR")))
g3 <- ggplot(hm, aes(view, anchor, fill = sharpe)) + geom_tile(colour = "white") + geom_text(aes(label = sprintf("%.2f", sharpe)), size = 3) + facet_wrap(~universe) +
  scale_fill_gradient(low = "#F0F0F0", high = "#56B4E9") + labs(x = "View", y = "Anchor", fill = "Mean Sharpe") + th
ggsave(file.path(fd, "G3_heatmap.png"), g3, width = 7.2, height = 3.2, dpi = 300, bg = "white")
cat("B figures done\n")
