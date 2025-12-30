import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ui import author, source_note, axis_style

def make_figure_M_M4(fig_no=None, save=False):

    # ===============================================================================================
    # Load data
    # ===============================================================================================
    
    df = pd.read_pickle("data/M_M4.pkl").sort_values(["year", "month"])

    m_max = df["month"].iloc[-1]
    y_max = df["year"].iloc[-1]

    # ===============================================================================================
    # Parameters & Labels
    # ===============================================================================================

    m_start = 1
    y_start = 2023
    period = f"{m_start}/{y_start}-{m_max}/{y_max}"
 
    label = {
        "d12_agriculture": "Nông nghiệp",
        "d12_industry": "Công nghiệp",
        "d12_construction": "Xây dựng",
        "d12_trade": "Thương mại",
        "d12_transport": "Vận tải & viễn thông",
        "d12_service": "Dịch vụ",
    }
    
    components_order = list(label.values())
    
    # ===============================================================================================
    # Data transformation
    # ===============================================================================================
     
    df_long = df.melt(
        id_vars=["date", "year", "month", "d12_m4"],
        value_vars=["d12_agriculture","d12_industry","d12_construction","d12_trade","d12_transport","d12_service",],
        var_name="component",
        value_name="value",
    )

    df_long["component"] = df_long["component"].map(label)

    start_date = pd.Timestamp(year=y_start, month=m_start, day=1)

    df_line = df.loc[df["date"] >= start_date, ["date", "d12_m4"]]
    df_long = df_long.loc[df_long["date"] >= start_date]

    # ===============================================================================================
    # Figure setup 
    # ===============================================================================================

    sns.set_theme(style="white", font="DejaVu Sans")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=200)

    # ===============================================================================================
    # Plotting 
    # ===============================================================================================

    pos_bottom = np.zeros(len(df_line))
    neg_bottom = np.zeros(len(df_line))

    for c in components_order:
        tmp = df_long[df_long["component"] == c].sort_values("date")
        v = tmp["value"].values

        ax.bar(
            tmp["date"],
            v,
            bottom=np.where(v >= 0, pos_bottom, neg_bottom),
            width=20,
            label=c,
            alpha=0.8,
            edgecolor="none"
        )

        pos_bottom += np.where(v >= 0, v, 0)
        neg_bottom += np.where(v < 0, v, 0)

    ax.plot(
        df_line["date"],
        df_line["d12_m4"],
        color="red",
        marker="o",
        linewidth=1.8,
        label="Tổng số"
    )

    # ===============================================================================================
    # Title, legend, source
    # ===============================================================================================
    
    sub = "%, so cùng kỳ"  # đơn vị
    title = f"Tốc độ tăng dư nợ tín dụng, {period} ({sub})"
    
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.25), ncol=3, fontsize=14, frameon=False)
    
    source_note(fig, source=f"Nguồn: CTK; và tính toán của {author}.")

    axis_style(ax, fig)

    return fig, title












