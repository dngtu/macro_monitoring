import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def make_figure_IT(fig_no=None, save=False):

    df = pd.read_pickle("data/IT.pkl")

    tot_list = ["Tổng số", "Nhà nước", "Tư nhân", "FDI"]

    df = df.sort_values(["year", "quarter"])
    y_max = df["year"].iloc[-1]
    q_max = df["quarter"].iloc[-1]

    y_start = 2021
    df = df[(df["quarter"] == q_max) & (df["year"] >= y_start)]

    period = f"{y_start}-{y_max}"
    m = q_max * 3
    if q_max == 4:
        timeframe = period
    else:
        timeframe = f"{m} tháng đầu năm, {period}"

    title_core = "Vốn đầu tư toàn xã hội"
    subtitle = "% tăng, so cùng kỳ"
    full_title = f"{title_core} {timeframe} ({subtitle})"

    sns.set_theme(style="white", font="Times New Roman")

    fig, ax = plt.subplots(figsize=(10, 8), dpi=200)

    sns.barplot(
        data=df[df["item"].isin(tot_list)],
        x="item", y="D4_ITN_A", hue="year",
        palette="muted", edgecolor="none",
        ax=ax
    )

    for container in ax.containers:
        labels = [f"{v.get_height():.1f}" for v in container]
        ax.bar_label(container, labels=labels, fontsize=10, padding=5)

    ax.set_title(f"Vốn đầu tư toàn xã hội {timeframe}, ({subtitle})", fontsize=14, fontweight="bold")
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.tick_params(axis="x", labelsize=10)
    ax.tick_params(axis="y", labelsize=10)
    ax.legend(fontsize=10, loc="upper right", frameon=False)

    source_a = "Nguồn: CTK; và tính toán của Ban QLRRTH."
    note = (
        "Chú thích: Vốn Nhà nước gồm vốn đầu tư công "
        "(từ NSNN và tín dụng đầu tư của Nhà nước) "
        "và vốn của DNNN cùng các nguồn khác."
    )

    fig.text(0.01, 0.02, f"{source_a}\n{note}",
             ha="left", va="bottom", fontsize=11)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(0.6)
    ax.spines["bottom"].set_linewidth(0.6)

    fig.tight_layout()
    fig.subplots_adjust(bottom=0.12)

    plt.close(fig)
    return fig
