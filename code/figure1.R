# Figure 1 (publication labels) from saved event-study estimates
suppressPackageStartupMessages({library(data.table); library(ggplot2)})
# Run from the project root (the folder that contains code/, data/ and output/).
e <- fread("output/revision/t_event_study.csv")
e <- rbind(e, data.table(outcome = rep(c("lamihud", "lval"), 2), group = rep(c("constituent", "named_excluded"), each = 2), relm = -1L, est = 0, se = 0), fill = TRUE)
e[, group := factor(group, levels = c("constituent", "named_excluded"), labels = c("FTSE constituents (24)", "Named on FTSE eligible lists, not included (14)"))]
e[, outcome := factor(outcome, levels = c("lamihud", "lval"), labels = c("A. log Amihud illiquidity", "B. log trading value"))]
g <- ggplot(e, aes(relm, est, colour = group, shape = group)) +
  geom_hline(yintercept = 0, colour = "grey50") +
  geom_vline(xintercept = c(-0.5, 5.5, 9.5), linetype = "dashed", colour = "grey40") +
  geom_text(data = data.frame(relm = c(-0.3, 5.7, 9.7), outcome = factor("A. log Amihud illiquidity", levels = levels(e$outcome)), lab = c("Announcement", "Confirmation", "List")),
            aes(x = relm, y = Inf, label = lab), inherit.aes = FALSE, hjust = 0, vjust = 1.5, size = 2.6, colour = "grey30") +
  geom_pointrange(aes(ymin = est - 1.96 * se, ymax = est + 1.96 * se), size = 0.25, position = position_dodge(width = 0.5)) +
  facet_wrap(~outcome, ncol = 1, scales = "free_y") +
  scale_colour_manual(values = c("#1b6ca8", "#d95f02")) +
  labs(x = "Months relative to the upgrade announcement (October 2025 = 0; reference = September 2025)", y = "Coefficient relative to never-named HOSE stocks (95% CI)", colour = NULL, shape = NULL) +
  theme_bw(base_size = 10) + theme(legend.position = "bottom")
ggsave("ars/stage2_write/figures/figure1_event_study.png", g, width = 6.5, height = 7, dpi = 300)
