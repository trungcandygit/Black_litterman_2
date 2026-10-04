# 08_costs.R -- trading-cost proxies for the 21 banks with daily data (Corwin-Schultz spread, Amihud)
root <- "/home/user/Black_litterman_2"; od <- file.path(root, "paper2/output")
banks <- c("VCB","BID","CTG","MBB","TCB","ACB","VPB","HDB","VIB","TPB","STB","SHB","LPB","SSB","MSB","OCB","NAB","KLB","VAB","VBB","BVB")
cs <- function(H, L) { n <- length(H); hl <- log(H / L)^2; b <- hl[-n] + hl[-1]
  Hm <- pmax(H[-n], H[-1]); Lm <- pmin(L[-n], L[-1]); g <- log(Hm / Lm)^2
  k <- 3 - 2 * sqrt(2); a <- (sqrt(2 * b) - sqrt(b)) / k - sqrt(g / k); S <- 2 * (exp(a) - 1) / (1 + exp(a)); pmax(S, 0) }
res <- do.call(rbind, lapply(banks, function(b) { f <- file.path(root, "data/raw", paste0(b, ".csv")); if (!file.exists(f)) return(NULL)
  d <- read.csv(f); d <- d[d$high > 0 & d$low > 0 & d$volume > 0, ]; s <- cs(d$high, d$low); r <- diff(d$close) / d$close[-nrow(d)]
  am <- mean(abs(r) / (d$close[-1] * d$volume[-1]), na.rm = TRUE) * 1e6
  data.frame(ticker = b, n_days = nrow(d), cs_spread_bps = mean(s) * 1e4, median_cs_bps = median(s) * 1e4, amihud_x1e6 = am,
             adv_mn = mean(d$close * d$volume) / 1e3) }))
write.csv(res, file.path(od, "tables/T10_bank_cost_proxies.csv"), row.names = FALSE)
print(res, digits = 3); cat("median CS spread (bps):", median(res$cs_spread_bps), " mean:", mean(res$cs_spread_bps), "\n")
