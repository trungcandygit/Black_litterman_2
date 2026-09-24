# Figure 2: monthly event study for the intention-to-treat group (FTSE preliminary list screened on 2024 data)
suppressPackageStartupMessages({library(data.table); library(ggplot2)})
setwd("/Users/nguyenvantrung/Downloads/Python for Algorithmic Trading/NCKH/BAI FTSE2/FTSE2_new")
e <- fread("output/revision2/t_itt_event_study.csv")
e <- rbind(e, data.table(relm = -1L, est = 0, se = 0), fill = TRUE)
g <- ggplot(e, aes(relm, est)) +
  geom_hline(yintercept = 0, colour = "grey50") +
  geom_vline(xintercept = c(-0.5, 5.5, 9.5), linetype = "dashed", colour = "grey40") +
  annotate("text", x = c(-0.3, 5.7, 9.7), y = Inf, label = c("Announcement", "Confirmation", "List"), hjust = 0, vjust = 1.5, size = 2.6, colour = "grey30") +
  geom_pointrange(aes(ymin = est - 1.96 * se, ymax = est + 1.96 * se), size = 0.25, colour = "#1b6ca8") +
  labs(x = "Months relative to the upgrade announcement (October 2025 = 0; reference = September 2025)",
       y = "log Amihud illiquidity, ITT group vs never-named stocks (95% CI)") +
  theme_bw(base_size = 10)
ggsave("ars/stage2_write/figures/figure2_itt_event_study.png", g, width = 6.5, height = 3.8, dpi = 300)
