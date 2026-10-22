"""Reference metadata for the Scientific Reports version (Nature style: numbered in order of first citation).
Bibliographic facts are copied from the verified reference list of the MSJ version (manuscript_final.Rmd); nothing is added."""

R = {}
def add(key, authors, title, journal=None, vol=None, pages=None, year=None, doi=None, tail=None):
    R[key] = dict(authors=authors, title=title, journal=journal, vol=vol, pages=pages, year=year, doi=doi, tail=tail)

add("aboody", ["Aboody, D.", "Even-Tov, O.", "Lehavy, R.", "Trueman, B."], "Overnight returns and firm-specific investor sentiment", "J. Financ. Quant. Anal.", "53", "485–505", "2018")
add("akbas", ["Akbas, F.", "Boehmer, E.", "Jiang, C.", "Koch, P. D."], "Overnight returns, daytime reversals, and future stock returns", "J. Financ. Econ.", "145", "850–875", "2022", "10.1016/j.jfineco.2021.09.019")
add("bh", ["Benjamini, Y.", "Hochberg, Y."], "Controlling the false discovery rate: a practical and powerful approach to multiple testing", "J. R. Stat. Soc. Ser. B", "57", "289–300", "1995", "10.1111/j.2517-6161.1995.tb02031.x")
add("berkmanlee", ["Berkman, H.", "Lee, J. B. T."], "The effectiveness of price limits in an emerging market: evidence from the Korean Stock Exchange", "Pac.-Basin Finance J.", "10", "517–530", "2002", "10.1016/S0927-538X(02)00040-9")
add("berkman12", ["Berkman, H.", "Koch, P. D.", "Tuttle, L.", "Zhang, Y. J."], "Paying attention: overnight returns and the hidden cost of buying at the open", "J. Financ. Quant. Anal.", "47", "715–741", "2012", "10.1017/S0022109012000270")
add("bildik", ["Bildik, R.", "Gülay, G."], "Are price limits effective? Evidence from the Istanbul Stock Exchange", "J. Financ. Res.", "29", "383–403", "2006", "10.1111/j.1475-6803.2006.00185.x")
add("bogous", ["Bogousslavsky, V."], "The cross-section of intraday and overnight returns", "J. Financ. Econ.", "141", "172–194", "2021")
add("brennan", ["Brennan, M. J."], "A theory of price limits in futures markets", "J. Financ. Econ.", "16", "213–233", "1986", "10.1016/0304-405X(86)90061-9")
add("cameron", ["Cameron, A. C.", "Gelbach, J. B.", "Miller, D. L."], "Robust inference with multiway clustering", "J. Bus. Econ. Stat.", "29", "238–249", "2011", "10.1198/jbes.2010.07136")
add("chen24", ["Chen, H.", "Petukhov, A.", "Wang, J.", "Xing, H."], "The dark side of circuit breakers", "J. Finance", "79", "1405–1455", "2024", "10.1111/jofi.13310")
add("chen19", ["Chen, T.", "Gao, Z.", "He, J.", "Jiang, W.", "Xiong, W."], "Daily price limits and destructive market behavior", "J. Econom.", "208", "249–264", "2019", "10.1016/j.jeconom.2018.09.014")
add("chen93", ["Chen, Y.-M."], "Price limits and stock market volatility in Taiwan", "Pac.-Basin Finance J.", "1", "139–153", "1993", "10.1016/0927-538X(93)90005-3")
add("cho", ["Cho, D. D.", "Russell, J.", "Tiao, G. C.", "Tsay, R. S."], "The magnet effect of price limits: evidence from high-frequency data on Taiwan Stock Exchange", "J. Empir. Finance", "10", "133–168", "2003", "10.1016/S0927-5398(02)00024-5")
add("chordia", ["Chordia, T.", "Goyal, A.", "Saretto, A."], "Anomalies and false rejections", "Rev. Financ. Stud.", "33", "2134–2179", "2020")
add("deb", ["Deb, S. S.", "Kalev, P. S.", "Marisetty, V. B."], "Flexible price limits: the case of Tokyo Stock Exchange", "J. Int. Financ. Mark. Inst. Money", "24", "66–84", "2013")
add("fm", ["Fama, E. F.", "MacBeth, J. D."], "Risk, return, and equilibrium: empirical tests", "J. Polit. Econ.", "81", "607–636", "1973", "10.1086/260061")
add("farber", ["Farber, A.", "Nguyen, V. N.", "Vuong, Q. H."], "Policy impacts on Vietnam stock market: a case of anomalies and disequilibria 2000–2006", tail="CEB Working Paper No. 06/005 (Université Libre de Bruxelles, 2006). https://ideas.repec.org/p/sol/wpaper/06-005.html")
add("greenwald", ["Greenwald, B. C.", "Stein, J. C."], "Transactional risk, market crashes, and the role of circuit breakers", "J. Bus.", "64", "443–462", "1991")
add("gu", ["Gu, M.", "Hu, Y.", "Xiong, Z."], "Dissecting the lottery-like anomaly: evidence from China", "Account. Finance", "65", "883–911", "2025", "10.1111/acfi.13354")
add("gutierrez", ["Gutierrez, R. C. Jr.", "Kelley, E. K."], "The long-lasting momentum in weekly returns", "J. Finance", "63", "415–447", "2008", "10.1111/j.1540-6261.2008.01320.x")
add("harveyliu", ["Harvey, C. R.", "Liu, Y."], "False (and missed) discoveries in financial economics", "J. Finance", "75", "2503–2553", "2020", "10.1111/jofi.12951")
add("hlz", ["Harvey, C. R.", "Liu, Y.", "Zhu, H."], "…and the cross-section of expected returns", "Rev. Financ. Stud.", "29", "5–68", "2016", "10.1093/rfs/hhv059")
add("holm", ["Holm, S."], "A simple sequentially rejective multiple test procedure", "Scand. J. Stat.", "6", "65–70", "1979")
add("hou", ["Hou, K.", "Xue, C.", "Zhang, L."], "Replicating anomalies", "Rev. Financ. Stud.", "33", "2019–2133", "2020")
add("hsc", ["HSC."], "Important changes of new trading system", tail="Ho Chi Minh City Securities Corporation https://www.hsc.com.vn/en/important-changes-of-new-trading-system (2025). Accessed 5 October 2026.")
add("huangx", ["Huang, X.", "Liu, C.", "Shu, T."], "Factors and anomalies in the Vietnamese stock market", "Pac.-Basin Finance J.", "82", "102176", "2023")
add("huangy", ["Huang, Y.-S.", "Fu, T.-W.", "Ke, M.-C."], "Daily price limits and stock price behavior: evidence from the Taiwan Stock Exchange", "Int. Rev. Econ. Finance", "10", "263–288", "2001", "10.1016/S1059-0560(00)00082-4")
add("jia", ["Jia, S.", "An, Y.", "Yang, L.", "Zhou, F."], "Price limit relaxation and stock price crash risk: evidence from China", "Financ. Res. Lett.", "59", "104715", "2024", "10.1016/j.frl.2023.104715")
add("jones", ["Jones, C. M.", "Shi, D.", "Zhang, X.", "Zhang, X."], "Retail trading and return predictability in China", "J. Financ. Quant. Anal.", "60", "68–104", "2025")
add("kelly", ["Kelly, M. A.", "Clark, S. P."], "Returns in trading versus non-trading hours: the difference is day and night", "J. Asset Manag.", "12", "132–145", "2011", "10.1057/jam.2011.2")
add("kimlimp", ["Kim, K. A.", "Limpaphayom, P."], "Characteristics of stocks that frequently hit price limits: empirical evidence from Taiwan and Thailand", "J. Financ. Mark.", "3", "315–332", "2000")
add("kimrhee", ["Kim, K. A.", "Rhee, S. G."], "Price limit performance: evidence from the Tokyo Stock Exchange", "J. Finance", "52", "885–901", "1997", "10.1111/j.1540-6261.1997.tb04827.x")
add("kimjun", ["Kim, W.", "Jun, S."], "Effects of a price limit change on market stability at the intraday horizon in the Korean stock market", "Appl. Econ. Lett.", "26", "582–586", "2019")
add("kodres", ["Kodres, L. E.", "O'Brien, D. P."], "The existence of Pareto-superior price limits", "Am. Econ. Rev.", "84", "919–932", "1994")
add("le", ["Le, D. N."], "Evaluating impacts of reduction in fluctuation limit on stock price risks in Vietnam", "J. Econ. Dev. (Univ. Econ. Ho Chi Minh City)", "214", "116–128", "2012", tail="https://vjol.info.vn/ed/article/view/34298")
add("liang", ["Liang, H.", "Hu, Y."], "Stock price limit and its predictability in the Chinese stock market", "J. Forecast.", "44", "297–319", "2025", "10.1002/for.3197")
add("lien", ["Lien, D.", "Hung, P.-H.", "Zhu, J.-D.", "Chen, Y.-H."], "Price limit changes and market quality in the Taiwan Stock Exchange", "Pac.-Basin Finance J.", "55", "239–258", "2019")
add("lin", ["Lin, F.", "Qiu, Z.", "Zheng, W."], "Cranes among chickens: the general-attention-grabbing effect of daily price limits in China's stock market", "J. Bank. Finance", "150", "106818", "2023", "10.1016/j.jbankfin.2023.106818")
add("lou", ["Lou, D.", "Polk, C.", "Skouras, S."], "A tug of war: overnight versus intraday expected returns", "J. Financ. Econ.", "134", "192–213", "2019", "10.1016/j.jfineco.2019.03.011")
add("lu", ["Lu, Z.", "Malliaris, S. G.", "Qin, Z."], "Heterogeneous liquidity providers and night-minus-day return predictability", "J. Financ. Econ.", "148", "175–200", "2023")
add("nw", ["Newey, W. K.", "West, K. D."], "A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix", "Econometrica", "55", "703–708", "1987", "10.2307/1913610")
add("petersen", ["Petersen, M. A."], "Estimating standard errors in finance panel data sets: comparing approaches", "Rev. Financ. Stud.", "22", "435–480", "2009")
add("qi", ["Qi, B."], "Effectiveness of price limits: evidence from China's ChiNext market", "PLOS ONE", "18", "e0287548", "2023", "10.1371/journal.pone.0287548")
add("qiao", ["Qiao, K.", "Dam, L."], "The overnight return puzzle and the “T+1” trading rule in Chinese stock markets", "J. Financ. Mark.", "50", "100534", "2020")
add("qiu", ["Qiu, J.", "Huang, W.", "Jiang, Y."], "Day-night anomaly returns in China: the role of institutions", "Res. Int. Bus. Finance", "75", "102776", "2025")
add("subrah", ["Subrahmanyam, A."], "Circuit breakers and market volatility: a theoretical perspective", "J. Finance", "49", "237–254", "1994", "10.1111/j.1540-6261.1994.tb04427.x")
add("vnnews", ["Viet Nam News."], "KRX system officially goes live", tail="https://vietnamnews.vn/economy/1717047/krx-system-officially-goes-live.html (2025). Accessed 5 October 2026.")
add("zeng", ["Zeng, Z.", "Wang, G.", "Tang, G."], "Price limits hitting effect and cross-sectional stock returns: evidence from China", "Financ. Res. Lett.", "60", "104803", "2024", "10.1016/j.frl.2023.104803")
add("zhang", ["Zhang, X.", "Wang, Z.", "Hao, J.", "He, F."], "Price limit and stock market quality: evidence from a quasi-natural experiment in the Chinese stock market", "Pac.-Basin Finance J.", "74", "101778", "2022")
# Supplementary Information only
add("amihud", ["Amihud, Y."], "Illiquidity and stock returns: cross-section and time-series effects", "J. Financ. Mark.", "5", "31–56", "2002", "10.1016/S1386-4181(01)00024-6")
add("bali", ["Bali, T. G.", "Cakici, N.", "Whitelaw, R. F."], "Maxing out: stocks as lotteries and the cross-section of expected returns", "J. Financ. Econ.", "99", "427–446", "2011", "10.1016/j.jfineco.2010.08.014")
add("corwin", ["Corwin, S. A.", "Schultz, P."], "A simple way to estimate bid-ask spreads from daily high and low prices", "J. Finance", "67", "719–760", "2012", "10.1111/j.1540-6261.2012.01729.x")
add("parkinson", ["Parkinson, M."], "The extreme value method for estimating the variance of the rate of return", "J. Bus.", "53", "61–65", "1980", "10.1086/296071")


def fmt_authors(a):
    if len(a) >= 6:
        return a[0] + " et al."
    if len(a) == 1:
        return a[0]
    return ", ".join(a[:-1]) + " & " + a[-1]


def fmt_ref(key):
    """Markdown for one Nature-style entry: authors, title., *journal* **vol**, pages (year). doi"""
    r = R[key]
    s = fmt_authors(r["authors"]) + " " + r["title"].rstrip(".") + "."
    if r["journal"]:
        s += f" *{r['journal']}*"
        if r["vol"]:
            s += f" **{r['vol']}**,"
        if r["pages"]:
            s += f" {r['pages']}"
        if r["year"]:
            s += f" ({r['year']})"
        s += "."
    if r["doi"]:
        s += f" https://doi.org/{r['doi']}"
    if r["tail"]:
        s += " " + r["tail"]
    return s
