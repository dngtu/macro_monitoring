import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import textwrap
from ui import author, source_note, axis_style

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
        palette="muted",
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

    note = (
        "Chú thích: Vốn Nhà nước gồm vốn đầu tư công "
        "(từ NSNN và tín dụng đầu tư của Nhà nước) "
        "và vốn của DNNN cùng các nguồn khác."
    )
    note_wrapped = textwrap.fill(note, width=120)
    
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.25), ncol=4, fontsize=14, frameon=False)
    
    source_note(fig, source=f"Nguồn: CTK; và tính toán của {author}.",note=note_wrapped)
    
    axis_style(ax, fig)

    return fig, title








