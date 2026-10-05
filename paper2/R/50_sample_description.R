# 50_sample_description.R -- sample construction and descriptive statistics for the 347 HOSE stocks (C26)
root <- "/home/user/Black_litterman_2"; od <- file.path(root, "paper2/output")
fl <- list.files(file.path(root, "data/raw"), full.names = TRUE)
dat <- lapply(fl, function(f) { d <- read.csv(f); d$sym <- sub("\\.csv$", "", basename(f)); d })
all_dates <- sort(unique(unlist(lapply(dat, `[[`, "time")))); all_dates <- all_dates[all_dates >= "2024-08-21"]
mat <- function(col) { M <- matrix(NA_real_, length(all_dates), length(dat), dimnames = list(all_dates, sapply(dat, function(d) d$sym[1])))
  for (j in seq_along(dat)) { mi <- match(dat[[j]]$time, all_dates); ok <- !is.na(mi); M[mi[ok], j] <- dat[[j]][[col]][ok] }; M }
Cc <- mat("close"); Vv <- mat("volume"); Hh <- mat("high"); Ll <- mat("low"); keep <- which(colMeans(!is.na(Cc)) >= 0.95)
lst <- read.csv(file.path(root, "data/hose_listing_VCI_20260924.csv")); syms <- colnames(Cc)[keep]
Cc <- Cc[, keep]; Vv <- Vv[, keep]; nd <- nrow(Cc)
Rd <- rbind(NA, Cc[-1, ] / Cc[-nd, ] - 1); Rd[!is.finite(Rd)] <- NA; DV <- Cc * Vv   # price in thousand VND, so DV is in thousand VND
r <- Rd[!is.na(Rd)]; dv <- DV[!is.na(DV)]
sec <- table(lst$icb_code2[match(syms, lst$symbol)])
out <- data.frame(item = c("Files retrieved (HOSE-listed, vnstock 4.0.4, source VCI, 24 September 2026)", "Rows in the VCI listing file (all instrument types)", "Stocks kept (at least 95% non-missing close)", "Trading days (21 Aug 2024 to 23 Sep 2026)", "Stock-days with a return", "Mean daily return (%)", "Standard deviation of daily returns (%)", "Median daily return (%)", "Median daily dollar volume (million VND)", "Mean daily dollar volume (million VND)", "Distinct two-digit ICB sector codes among kept stocks", "Share of kept stocks in the largest sector (%)"),
  value = c(length(fl), nrow(lst), length(keep), nd, length(r), 100 * mean(r), 100 * sd(r), 100 * median(r), median(dv) / 1000, mean(dv) / 1000, length(sec), 100 * max(sec) / sum(sec)))
write.csv(out, file.path(od, "tables/C26_sample_description.csv"), row.names = FALSE); print(out, digits = 4)
