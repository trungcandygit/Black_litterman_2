# Figure 2: monthly event study for the intention-to-treat group (FTSE preliminary list screened on 2024 data)
suppressPackageStartupMessages({library(data.table); library(ggplot2)})
# Run from the project root (the folder that contains code/, data/ and output/).
e <- fread("output/revision2/t_itt_event_study.csv")
e <- rbind(e, data.table(relm = -1L, est = 0, se = 0), fill = TRUE)
# Same y-axis range as Figure 1, panel A (constituents and named-but-excluded, log Amihud)
f1 <- fread("output/revision/t_event_study.csv")[outcome == "lamihud"]
ylim_a <- range(c(0, f1$est - 1.96 * f1$se, f1$est + 1.96 * f1$se, e$est - 1.96 * e$se, e$est + 1.96 * e$se))
g <- ggplot(e, aes(relm, est)) +
  geom_hline(yintercept = 0, colour = "grey50") +
  geom_vline(xintercept = c(-0.5, 5.5, 9.5), linetype = "dashed", colour = "grey40") +
  annotate("text", x = c(-0.3, 5.7, 9.7), y = Inf, label = c("Announcement", "Confirmation", "List"), hjust = 0, vjust = 1.5, size = 3.6, colour = "grey30") +
  geom_pointrange(aes(ymin = est - 1.96 * se, ymax = est + 1.96 * se), size = 0.4, linewidth = 0.6, colour = "#009E73", shape = 15) +
  coord_cartesian(ylim = ylim_a) +
  labs(x = "Months since announcement (Oct 2025 = 0; reference: Sep 2025)",
       y = "Coefficient, log points (95% CI)") +
  theme_bw(base_size = 14)
ggsave("ars/stage2_write/figures/figure2_itt_event_study.png", g, width = 6.5, height = 4, dpi = 300)
# Submission files for Finance Research Open: vector PDF (fonts embedded) and 600-dpi PNG at full-page width (7.5 in = 4500 px)
dir.create("output/figures", showWarnings = FALSE)
ggsave("output/figures/Figure_2.pdf", g, width = 7.5, height = 4.6, device = cairo_pdf)
ggsave("output/figures/Figure_2.png", g, width = 7.5, height = 4.6, dpi = 600)
