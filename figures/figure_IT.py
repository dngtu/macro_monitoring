import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import textwrap
from ui import author

def make_figure_IT(fig_no=None, save=False):
    
    # ===============================================================================================
    # Load data
    # ===============================================================================================

    df = pd.read_pickle("data/IT.pkl").sort_values(["year", "quarter"])

    y_max = df["year"].iloc[-1]
    q_max = df["quarter"].iloc[-1]
   
    # ===============================================================================================
    # Parameters & Labels
    # ===============================================================================================

    y_start = 2019
    period = f"{y_start}-{y_max}"

    # ===============================================================================================
    # Data transformation
    # ===============================================================================================   
    
    df = df.loc[(df["quarter"] == q_max) & (df["year"]>=y_start)] 
    select = ["Tổng số", "Nhà nước", "Tư nhân", "FDI"] 
    df=df.loc[df["item"].isin(select)].sort_values(["year"])

    # ===============================================================================================
    # Figure setup 
    # ===============================================================================================
    
    sns.set_theme(style="white", font="DejaVu Sans")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=200)

    # ===============================================================================================
    # Plotting 
    # ===============================================================================================

    sns.barplot(
        data=df,
        x="item", y="D4_ITN_A", hue="year",
        edgecolor="none",
        ax=ax
    )

    ymax = ax.get_ylim()[1]
    ax.set_ylim(top=ymax * 1.15)

    for container in ax.containers:
        ax.bar_label(
            container,
            labels=[f"{v.get_height():.1f}" for v in container],
            fontsize=10,
            padding=4
        )

    # ===============================================================================================
    # Title, legend, source
    # ===============================================================================================

    sub = "% tăng, so cùng kỳ"

    if q_max == 4:
        title = f"Vốn đầu tư toàn xã hội, {period} ({sub})"
    else: 
        m = 3 * q_max
        title = f"Vốn đầu tư toàn xã hội {m} tháng đầu năm, {period} ({sub})"

    source = f"Nguồn: CTK; và tính toán của {author}."
    note = (
        "Chú thích: Vốn Nhà nước gồm vốn đầu tư công "
        "(từ NSNN và tín dụng đầu tư của Nhà nước) "
        "và vốn của DNNN cùng các nguồn khác."
    )
    note_wrapped = textwrap.fill(note, width=120)
    
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.25), ncol=4, fontsize=14, frameon=False)
    fig.text(0.01, 0, f"{source}\n{note_wrapped}", ha="left", va="bottom", fontsize=14)

    # ===============================================================================================
    # Axis style
    # ===============================================================================================

    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    ax.set_xlabel(None)
    ax.set_ylabel(None)
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_linewidth(0.6)
    ax.grid(axis="y", alpha=0.5, linewidth=0.8)

    fig.tight_layout()
    fig.subplots_adjust(top=0.8, bottom=0.2)

    return fig, title


