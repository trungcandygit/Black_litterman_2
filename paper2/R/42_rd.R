# 42_rd.R -- discontinuity at the price limit: next-day overnight / intraday / close-to-close abnormal returns by size of today's move; exact tick rule; two-way clustering
suppressPackageStartupMessages(library(ggplot2)); source("/home/user/Black_litterman_2/paper2/R/lib.R")
root <- "/home/user/Black_litterman_2"; od <- file.path(root, "paper2/output"); fd <- file.path(od, "figures"); set.seed(20261004)
fl <- list.files(file.path(root, "data/raw"), full.names = TRUE)
dat <- lapply(fl, function(f) { d <- read.csv(f); d$sym <- sub("\\.csv$", "", basename(f)); d })
all_dates <- sort(unique(unlist(lapply(dat, `[[`, "time")))); all_dates <- all_dates[all_dates >= "2024-08-21"]
mat <- function(col) { M <- matrix(NA_real_, length(all_dates), length(dat), dimnames = list(all_dates, sapply(dat, function(d) d$sym[1])))
  for (j in seq_along(dat)) { mi <- match(dat[[j]]$time, all_dates); okm <- !is.na(mi); M[mi[okm], j] <- dat[[j]][[col]][okm] }; M }
Cc <- mat("close"); Oo <- mat("open"); Hh <- mat("high"); Ll <- mat("low"); Vv <- mat("volume"); keep <- which(colMeans(!is.na(Cc)) >= 0.95)
Cc <- Cc[, keep]; Oo <- Oo[, keep]; Hh <- Hh[, keep]; Ll <- Ll[, keep]; Vv <- Vv[, keep]; nd <- nrow(Cc); ns <- ncol(Cc)
Rd <- rbind(NA, Cc[-1, ] / Cc[-nd, ] - 1); Rd[!is.finite(Rd)] <- NA; DV <- Cc * Vv
tt <- 61:(nd - 1); adv <- t(sapply(tt, function(t) colMeans(DV[(t - 59):t, , drop = FALSE])))
OVN <- Oo[tt + 1, ] / Cc[tt, ] - 1; INT <- Cc[tt + 1, ] / Oo[tt + 1, ] - 1; CC1 <- Cc[tt + 1, ] / Cc[tt, ] - 1; R0 <- Rd[tt, ]
mk <- function(M) { ok <- is.finite(M) & is.finite(adv); sapply(seq_along(tt), function(i) sum(M[i, ok[i, ]] * adv[i, ok[i, ]]) / sum(adv[i, ok[i, ]])) }
AOVN <- OVN - mk(OVN); AINT <- INT - mk(INT); ACC <- CC1 - mk(CC1)
atceil <- !is.na(R0) & R0 >= 0.065 & Cc[tt, ] >= Hh[tt, ] - 1e-9; atfloor <- !is.na(R0) & R0 <= -0.065 & Cc[tt, ] <= Ll[tt, ] + 1e-9
# ---- binned discontinuity plot (1pp bins), "at limit" split out
brk <- c(-0.10, seq(-0.065, 0.065, by = 0.01), 0.10); bin <- cut(R0, brk, include.lowest = TRUE)
mkgrp <- function(g) { lab <- as.character(g); lab[atceil] <- "CEIL"; lab[atfloor] <- "FLOOR"; lab }
grp <- mkgrp(bin); mid <- function(l) { if (l == "CEIL") return(0.0695); if (l == "FLOOR") return(-0.0695); b <- as.numeric(strsplit(gsub("[\\[\\]\\(\\)]", "", l, perl = TRUE), ",")[[1]]); mean(b) }
dtt <- rep(tt, times = ns)
bins <- do.call(rbind, lapply(setdiff(unique(grp[!is.na(grp)]), NA), function(l) { idx <- which(grp == l); do.call(rbind, lapply(list(c("Overnight gap", "AOVN"), c("Intraday (open to close)", "AINT"), c("Close to close", "ACC")), function(m) {
  v <- get(m[2]); r <- which(grp == l & is.finite(v)); r2 <- r; rr <- row(v)[r2]; a <- v[r2]; mm <- mean(a); g <- tapply(a - mm, rr, sum); se <- sqrt(sum(g^2)) / length(a)
  data.frame(bin = l, x = mid(l), measure = m[1], mean_pct = 100 * mm, lo = 100 * (mm - 1.96 * se), hi = 100 * (mm + 1.96 * se), n = length(a)) })) }))
bins <- bins[order(bins$measure, bins$x), ]; write.csv(bins, file.path(od, "tables/C5_rd_bins.csv"), row.names = FALSE)
oi <- c("#0072B2", "#D55E00", "#009E73")
bins$kind <- ifelse(bins$bin %in% c("CEIL", "FLOOR"), "Closed at the 7% limit", ifelse(abs(bins$x) > 0.07, "Beyond 6.5%, not at limit", "Interior bin"))
bins$x[bins$kind == "Beyond 6.5%, not at limit"] <- sign(bins$x[bins$kind == "Beyond 6.5%, not at limit"]) * 0.0825
g <- ggplot(bins[bins$kind == "Interior bin", ], aes(x * 100, mean_pct, colour = measure)) + geom_hline(yintercept = 0, colour = "grey60") + geom_pointrange(aes(ymin = lo, ymax = hi), size = 0.25) + geom_line(linewidth = 0.3) +
  geom_pointrange(data = bins[bins$kind == "Closed at the 7% limit", ], aes(ymin = lo, ymax = hi), size = 0.5, shape = 17) + geom_pointrange(data = bins[bins$kind == "Beyond 6.5%, not at limit", ], aes(ymin = lo, ymax = hi), size = 0.4, shape = 15) + facet_wrap(~measure, ncol = 1, scales = "free_y") +
  scale_colour_manual(values = oi) + labs(x = "Day-t return (%)", y = "Next-day abnormal return (%)") + theme_minimal(base_size = 10) + theme(legend.position = "none", panel.grid.minor = element_blank())
ggsave(file.path(fd, "H1_rd_bins.png"), g, width = 7, height = 7.2, dpi = 300, bg = "white")
# ---- two-way clustering (date and stock) for headline measures
cl2 <- function(sel, v) { r <- which(sel & is.finite(v)); ii <- row(v)[r]; jj <- col(v)[r]; a <- v[r]; m <- mean(a); e <- a - m; N <- length(a)
  se_d <- sqrt(sum(tapply(e, ii, sum)^2)) / N; se_s <- sqrt(sum(tapply(e, jj, sum)^2)) / N; se_i <- sqrt(sum(e^2)) / N; se2 <- sqrt(max(se_d^2 + se_s^2 - se_i^2, 1e-12))
  c(mean_pct = 100 * m, t_date = m / se_d, t_stock = m / se_s, t_twoway = m / se2, n = N, n_stocks = length(unique(jj)), n_dates = length(unique(ii))) }
tw <- do.call(rbind, lapply(list(c("ceiling", "atceil"), c("floor", "atfloor")), function(e) do.call(rbind, lapply(list(c("overnight gap", "AOVN"), c("intraday", "AINT"), c("close-to-close", "ACC")), function(m) data.frame(event = e[1], measure = m[1], t(cl2(get(e[2]), get(m[2]))), row.names = NULL)))))
write.csv(tw, file.path(od, "tables/C6_twoway_cluster.csv"), row.names = FALSE); print(tw, digits = 3)
# ---- exact tick-rule classification (prices in thousand VND): tick 0.01 (<10), 0.05 (10-49.95), 0.10 (>=50)
tick <- function(p) ifelse(p < 10, 0.01, ifelse(p < 50, 0.05, 0.10))
ref <- Cc[tt - 1 + 0, ]; ref <- Cc[tt - 0 - 0, ]; refp <- Cc[tt - 1, ]                         # reference = previous close
ceil_px <- floor(refp * 1.07 / tick(refp) + 1e-9) * tick(refp); floor_px <- ceiling(refp * 0.93 / tick(refp) - 1e-9) * tick(refp)
ex_ceil <- is.finite(Cc[tt, ]) & abs(Cc[tt, ] - ceil_px) < 1e-6; ex_floor <- is.finite(Cc[tt, ]) & abs(Cc[tt, ] - floor_px) < 1e-6
cat("exact ceilings:", sum(ex_ceil, na.rm = TRUE), " rule-based ceilings:", sum(atceil), " both:", sum(ex_ceil & atceil, na.rm = TRUE), "\n")
cat("exact floors:", sum(ex_floor, na.rm = TRUE), " rule-based floors:", sum(atfloor), " both:", sum(ex_floor & atfloor, na.rm = TRUE), "\n")
tx <- do.call(rbind, lapply(list(c("exact ceiling", "ex_ceil"), c("exact floor", "ex_floor")), function(e) do.call(rbind, lapply(list(c("overnight gap", "AOVN"), c("intraday", "AINT"), c("close-to-close", "ACC")), function(m) data.frame(event = e[1], measure = m[1], t(cl2(get(e[2]) & TRUE, get(m[2]))), row.names = NULL)))))
write.csv(tx, file.path(od, "tables/C7_exact_tick_rule.csv"), row.names = FALSE); print(tx, digits = 3)
