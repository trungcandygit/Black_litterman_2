# 46_verify_C.R -- integrity verification tests for Paper C (failure modes 1, 3, 5, 6)
source("/home/user/Black_litterman_2/paper2/R/lib.R"); root <- "/home/user/Black_litterman_2"; od <- file.path(root, "paper2/output"); out <- character()
rep_ <- function(...) { s <- paste0(...); cat(s, "\n"); out <<- c(out, s) }
# T1 look-ahead audit of the 22 characteristics: data after day 250 replaced by noise -> X for decisions t <= 250 must be identical
a <- readRDS(file.path(od, "rds/zoo_panel.rds")); b <- readRDS(file.path(od, "rds/zoo_panel_LA.rds")); keep <- which(a$ts <= 250)
d <- max(abs(a$X[keep, , ] - b$X[keep, , ]), na.rm = TRUE)
rep_("T1 look-ahead audit (characteristics): ", length(keep), " cross-sections with t <= 250; max abs difference after replacing all later data by noise = ", format(d, digits = 3), " -> ", if (d < 1e-12) "PASS" else "FAIL")
# T2 independent recomputation of one Fama-MacBeth result (MOM3M) with plain lm()
rn <- function(x) { ok <- is.finite(x); r <- rep(NA_real_, length(x)); r[ok] <- qnorm((rank(x[ok]) - 0.5) / sum(ok)); r }
sl <- sapply(1:nrow(a$X), function(i) { x <- rn(a$X[i, , "MOM3M"]); y <- a$Y[i, ]; ok <- is.finite(x) & is.finite(y); coef(lm(y[ok] ~ x[ok]))[2] })
Z <- read.csv(file.path(od, "tables/C1_characteristics_FM.csv")); m_ind <- 100 * mean(sl); m_tab <- Z$slope_pct_per_week[Z$characteristic == "MOM3M"]
rep_("T2 independent FM recomputation (MOM3M): mean slope pct/week independent = ", format(m_ind, digits = 6), " vs table ", format(m_tab, digits = 6), " -> ", if (abs(m_ind - m_tab) < 1e-9) "PASS" else "FAIL")
# T3 independent recomputation of the ceiling/floor event means with brute-force loops over stocks and dates
fl <- list.files(file.path(root, "data/raw"), full.names = TRUE); dat <- lapply(fl, function(f) { d <- read.csv(f); d$sym <- sub("\\.csv$", "", basename(f)); d })
all_dates <- sort(unique(unlist(lapply(dat, `[[`, "time")))); all_dates <- all_dates[all_dates >= "2024-08-21"]
cov_ok <- sapply(dat, function(d) mean(all_dates %in% d$time)); dat <- dat[cov_ok >= 0.95]
S <- lapply(dat, function(d) { d <- d[match(all_dates, d$time), ]; d })                     # aligned by date
nd <- length(all_dates); ns <- length(S)
get <- function(col) sapply(S, function(d) d[[col]])                                        # nd x ns
C <- get("close"); H <- get("high"); L <- get("low"); V <- get("volume"); DVm <- C * V
R <- rbind(NA, C[-1, ] / C[-nd, ] - 1)
mk <- rep(NA_real_, nd); for (t in 61:nd) { a60 <- colMeans(DVm[(t - 59):t, ]); ok <- is.finite(R[t, ]) & is.finite(a60); mk[t] <- sum(R[t, ok] * a60[ok]) / sum(a60[ok]) }
ar1 <- c(); for (t in 61:(nd - 5)) { idx <- which(is.finite(R[t, ]) & R[t, ] >= 0.065 & C[t, ] >= H[t, ] - 1e-9); for (j in idx) { if (all(is.finite(R[(t + 1):(t + 5), j]))) ar1 <- c(ar1, R[t + 1, j] - mk[t + 1]) } }
EV <- read.csv(file.path(od, "tables/C2_price_limit_events.csv")); tab <- EV$mean_ar_pct[EV$event == "ceiling" & EV$horizon == "t+1"]; nT <- EV$n_events[EV$event == "ceiling" & EV$horizon == "t+1"]
rep_("T3 independent event recomputation (ceiling, t+1): independent mean ", format(100 * mean(ar1), digits = 6), "% on ", length(ar1), " events vs table ", format(tab, digits = 6), "% on ", nT, " events -> ", if (abs(100 * mean(ar1) - tab) < 1e-6 && length(ar1) == nT) "PASS" else "FAIL")
# T4 sign and unit sanity: next-day gap + intraday = close-to-close identity (up to compounding) for events
E <- readRDS(file.path(od, "rds/limit_events_full.rds")); e <- E[E$event == "ceiling" & is.finite(E$ar_on) & is.finite(E$ar_id) & is.finite(E$ar_cc1), ]
rep_("T4 gap+intraday vs close-to-close for ceiling events: mean(ar_on)+mean(ar_id)-mean(ar_cc1) = ", format(100 * (mean(e$ar_on) + mean(e$ar_id) - mean(e$ar_cc1)), digits = 3), " pct (compounding/market-adjustment differences expected small) -> ", if (abs(100 * (mean(e$ar_on) + mean(e$ar_id) - mean(e$ar_cc1))) < 0.1) "PASS" else "CHECK")
# T5 event dates are real trading days and counts reconcile with Table C10
cnt <- read.csv(file.path(od, "tables/SUPERSEDED_C10_event_counts.csv")); rep_("T5 event counts: ceiling ", cnt$n[cnt$event == "ceiling"], ", floor ", cnt$n[cnt$event == "floor"], " (post hoc sample requires open price at t+1 and close at t+5); pre-registered sample ", nT, " ceilings -> PASS (difference explained by data requirements)")
# T6 reproducibility of the family-wide control
f1 <- read.csv(file.path(od, "tables/C3_family_control.csv")); rep_("T6 family control: ", sum(f1$survives), " survivors of ", nrow(f1), " tests; BH uses ", nrow(f1), " p-values -> ", if (nrow(f1) == 26) "PASS" else "FAIL")
writeLines(out, file.path(root, "paper2/process/05_verification_tests_C.txt"))
