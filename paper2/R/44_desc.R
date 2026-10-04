# SUPERSEDED by R/47_da_response.R for all numbers in manuscript C (see Appendix B); kept for audit. Known issue: NA propagation in the market and control calculations (41), and all-stock population (44).
# 44_desc.R -- descriptive evidence on the limit (pile-up near 7%) and event counts
source("/home/user/Black_litterman_2/paper2/R/lib.R"); root <- "/home/user/Black_litterman_2"; od <- file.path(root, "paper2/output")
fl <- list.files(file.path(root, "data/raw"), full.names = TRUE)
dat <- lapply(fl, function(f) { d <- read.csv(f); d <- d[d$time >= "2024-08-21", ]; d$ret <- c(NA, d$close[-1] / d$close[-nrow(d)] - 1); d })
r <- unlist(lapply(dat, `[[`, "ret")); r <- r[is.finite(r)]
brk <- c(-Inf, -0.08, -0.071, -0.069, -0.065, -0.06, 0.06, 0.065, 0.069, 0.071, 0.08, Inf)
lab <- c("< -8.0%", "-8.0% to -7.1%", "-7.1% to -6.9%", "-6.9% to -6.5%", "-6.5% to -6.0%", "-6.0% to 6.0%", "6.0% to 6.5%", "6.5% to 6.9%", "6.9% to 7.1%", "7.1% to 8.0%", "> 8.0%")
tb <- table(cut(r, brk, labels = lab)); df <- data.frame(range = names(tb), n = as.integer(tb), share_pct = 100 * as.numeric(tb) / length(r))
write.csv(df, file.path(od, "tables/SUPERSEDED_C9_pileup.csv"), row.names = FALSE); print(df, digits = 3); cat("stock-days:", length(r), " stocks:", length(dat), "\n")
E <- readRDS(file.path(od, "rds/limit_events_full.rds")); cnt <- as.data.frame(table(E$event)); names(cnt) <- c("event", "n"); write.csv(cnt, file.path(od, "tables/SUPERSEDED_C10_event_counts.csv"), row.names = FALSE); print(cnt)
