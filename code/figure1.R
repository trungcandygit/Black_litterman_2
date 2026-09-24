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
            aes(x = relm, y = Inf, label = lab), inherit.aes = FALSE, hjust = 0, vjust = 1.5, size = 3.6, colour = "grey30") +
  geom_pointrange(aes(ymin = est - 1.96 * se, ymax = est + 1.96 * se), size = 0.4, linewidth = 0.6, position = position_dodge(width = 0.5)) +
  facet_wrap(~outcome, ncol = 1, scales = "free_y") +
  scale_colour_manual(values = c("#1b6ca8", "#d95f02")) +
  labs(x = "Months since announcement (Oct 2025 = 0; reference: Sep 2025)", y = "Coefficient, log points (95% CI)", colour = NULL, shape = NULL) +
  theme_bw(base_size = 14) + theme(legend.position = "bottom")
# Submission files for Finance Research Open: vector PDF (fonts embedded) and 600-dpi PNG at full-page width (7.5 in = 4500 px)
dir.create("output/figures", showWarnings = FALSE)
ggsave("output/figures/Figure_1.pdf", g, width = 7.5, height = 8, device = cairo_pdf)
ggsave("output/figures/Figure_1.png", g, width = 7.5, height = 8, dpi = 600)
