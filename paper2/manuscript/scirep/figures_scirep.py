"""Figures for the Scientific Reports version, redrawn from the saved R outputs (no number is re-estimated).
Sans-serif lettering, white background, bold lower-case panel letters, 300 dpi PNG plus vector PDF."""
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

HERE = os.path.dirname(os.path.abspath(__file__))
TAB = os.path.join(HERE, "..", "..", "output", "tables")
OUT = os.path.join(HERE, "..", "..", "final", "SciRep")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.family": "Liberation Sans", "font.size": 9, "axes.linewidth": 0.8,
                     "pdf.fonttype": 42, "axes.spines.top": False, "axes.spines.right": False})
BLUE, ORANGE, GREEN = "#0072B2", "#D55E00", "#009E73"


def figure1():
    z = pd.read_csv(os.path.join(TAB, "C1_characteristics_FM.csv"))
    z = z.assign(a=z.t_nw.abs()).sort_values("a", ascending=True).reset_index(drop=True)
    fig, ax = plt.subplots(figsize=(5.6, 4.6))
    y = range(len(z))
    for lim, ls in ((1.96, "--"), (-1.96, "--"), (3, ":"), (-3, ":")):
        ax.axvline(lim, color="0.45", lw=0.9, ls=ls)
    ax.axvline(0, color="0.6", lw=0.9)
    ax.scatter(z.t_nw, y, marker="o", s=22, color=BLUE, label="Full sample", zorder=3)
    ax.scatter(z.t_disc, y, marker="^", s=26, color=ORANGE, label="Discovery half", zorder=3)
    ax.scatter(z.t_conf, y, marker="s", s=22, color=GREEN, label="Confirmation half", zorder=3)
    ax.set_yticks(list(y)); ax.set_yticklabels(z.characteristic, fontsize=7.5)
    ax.set_xlabel("Fama–MacBeth t-statistic"); ax.set_xlim(-3.4, 3.4)
    ax.grid(axis="y", color="0.9", lw=0.6); ax.set_axisbelow(True)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=3, frameon=False, handletextpad=0.3, columnspacing=1.2)
    fig.tight_layout()
    for ext in ("png", "pdf"):
        fig.savefig(os.path.join(OUT, f"Figure_1.{ext}"), dpi=300, facecolor="white")
    plt.close(fig)


def figure2():
    d = pd.read_csv(os.path.join(TAB, "C5_rd_bins.csv"))
    fig, axes = plt.subplots(1, 3, figsize=(7.4, 2.9))
    meas = [("Overnight gap", BLUE), ("Intraday (open to close)", ORANGE), ("Close to close", GREEN)]
    for k, (ax, (m, col)) in enumerate(zip(axes, meas)):
        s = d[d.measure == m].reset_index(drop=True)
        x = s.x * 100
        inner = ~s.bin.isin(["FLOOR", "CEIL"]) & (s.x.abs() < 0.065)
        ev = s.bin.isin(["FLOOR", "CEIL"])
        oth = ~inner & ~ev
        ax.axhline(0, color="0.6", lw=0.8)
        ax.plot(x[inner], s.mean_pct[inner], color=col, lw=0.9, zorder=2)
        for mask, mk, ms in ((inner, "o", 4), (ev, "^", 6), (oth, "s", 4.5)):
            ax.errorbar(x[mask], s.mean_pct[mask], yerr=[(s.mean_pct - s.lo)[mask], (s.hi - s.mean_pct)[mask]],
                        fmt=mk, ms=ms, color=col, elinewidth=0.8, capsize=0, zorder=3)
        ax.set_title(m.replace(' (open to close)', ''), fontsize=9)
        ax.set_xlabel("Day-d return (%)")
        if k == 0:
            ax.set_ylabel("Next-day abnormal return (%)")
        ax.text(-0.02 if k else -0.20, 1.12, "abc"[k], transform=ax.transAxes, fontsize=11, fontweight="bold", va="bottom")
    h = [Line2D([], [], marker="o", color="0.3", ls="", ms=4, label="1-point bins inside the band"),
         Line2D([], [], marker="^", color="0.3", ls="", ms=6, label="Ceiling and floor closes"),
         Line2D([], [], marker="s", color="0.3", ls="", ms=4.5, label="Other moves of 6.5% to 10%")]
    fig.legend(handles=h, loc="lower center", ncol=3, frameon=False, bbox_to_anchor=(0.5, -0.01))
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    for ext in ("png", "pdf"):
        fig.savefig(os.path.join(OUT, f"Figure_2.{ext}"), dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    figure1(); figure2()
