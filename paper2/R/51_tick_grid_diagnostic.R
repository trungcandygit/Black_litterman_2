# 51_tick_grid_diagnostic.R -- are vendor prices on the exchange tick grid? (diagnostic for the exact-hit definition; table C27)
root <- "/home/user/Black_litterman_2"; od <- file.path(root, "paper2/output")
fl <- list.files(file.path(root, "data/raw"), full.names = TRUE)
dat <- lapply(fl, function(f) { d <- read.csv(f); d$sym <- sub("\\.csv$", "", basename(f)); d })
all_dates <- sort(unique(unlist(lapply(dat, `[[`, "time")))); all_dates <- all_dates[all_dates >= "2024-08-21"]
mat <- function(col) { M <- matrix(NA_real_, length(all_dates), length(dat)); for (j in seq_along(dat)) { mi <- match(dat[[j]]$time, all_dates); ok <- !is.na(mi); M[mi[ok], j] <- dat[[j]][[col]][ok] }; M }
Cc <- mat("close"); Hh <- mat("high"); keep <- which(colMeans(!is.na(Cc)) >= 0.95); Cc <- Cc[, keep]; Hh <- Hh[, keep]; nd <- nrow(Cc)
tick <- function(p) ifelse(p < 10, 0.01, ifelse(p < 50, 0.05, 0.10))
ongrid <- function(p) { k <- p / tick(p); abs(k - round(k)) < 1e-6 }
yr <- substr(all_dates, 1, 4); G <- ongrid(Cc); P <- Cc
rows <- list()
for (y in sort(unique(yr))) for (band in c("below 10", "10 or more")) { sel <- matrix(yr == y, nd, ncol(Cc)) & !is.na(P) & (if (band == "below 10") P < 10 else P >= 10)
  rows[[length(rows) + 1]] <- data.frame(group = paste("Closes on the tick grid,", y, ", price", band), value = 100 * mean(G[sel]), n = sum(sel)) }
# events: rule-based ceilings in the event window, exact vs near hits
R <- rbind(NA, Cc[-1, ] / Cc[-nd, ] - 1); tt <- 61:(nd - 5); refp <- Cc[tt - 1, ]; R0 <- R[tt, ]
ce <- !is.na(R0) & R0 >= 0.065 & Cc[tt, ] >= Hh[tt, ] - 1e-9
cpx <- floor(refp * 1.07 / tick(refp) + 1e-9) * tick(refp); ex <- ce & abs(Cc[tt, ] - cpx) < 1e-6; nh <- ce & !ex
ex[is.na(ex)] <- FALSE; nh[is.na(nh)] <- FALSE; ce[is.na(ce)] <- FALSE
rows[[length(rows) + 1]] <- data.frame(group = c("Median day-d return, exact ceiling hits (%)", "Median day-d return, near hits (%)", "Near hits with a close off the tick grid (%)", "Near-hit share of ceiling events, reference price below 10 (%)", "Near-hit share of ceiling events, reference price 10 or more (%)"),
  value = c(100 * median(R0[ex]), 100 * median(R0[nh]), 100 * mean(!ongrid(Cc[tt, ][nh])), 100 * sum(nh & refp < 10, na.rm = TRUE) / sum(ce & refp < 10, na.rm = TRUE), 100 * sum(nh & refp >= 10, na.rm = TRUE) / sum(ce & refp >= 10, na.rm = TRUE)),
  n = c(sum(ex), sum(nh), sum(nh), sum(ce & refp < 10, na.rm = TRUE), sum(ce & refp >= 10, na.rm = TRUE)))
out <- do.call(rbind, rows); write.csv(out, file.path(od, "tables/C27_tick_grid_diagnostic.csv"), row.names = FALSE); print(out, digits = 3)
