import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ui import author, axis_style

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
        # align component series to df_line years
        tmp = (
            df_long[df_long["component"] == c]
            .set_index("year")
            .reindex(df_line["year"])
            .fillna(0)
        )

        v = tmp["value"].values

        ax.bar(
        df_line["year"],
        v,
        bottom=np.where(v >= 0, pos_bottom, neg_bottom),
        label=c,
        alpha=0.8,
        edgecolor="none",
        )

        pos_bottom += np.where(v >= 0, v, 0)
        neg_bottom += np.where(v < 0, v, 0)
    
    ax.plot(
        df_line["year"],
        df_line["d4_gdp"],
        color="red",
        marker="o",
        markersize=20,
        linewidth=1.8,
        label="GDP"
    )

    # --- add value inside marker ---
    for x, y in zip(df_line["year"], df_line["d4_gdp"]):
        ax.text(
            x,
            y,
            f"{y:.1f}",      # định dạng số (1 chữ số thập phân)
            ha="center",
            va="center",
            fontsize=12,
            color="white",   
            fontweight="bold",
            zorder=5,        # đảm bảo nằm trên marker
        )

    # ===============================================================================================
    # Title, legend, source
    # ===============================================================================================
    
    sub = "%, so cùng kỳ"  # đơn vị

    if q_max == 4:
        title = f"Tăng trưởng GDP theo khu vực sản xuất, {period} ({sub})"
    else: 
        m = 3 * q_max
        title = f"Tăng trưởng GDP theo khu vực sản xuất {m} tháng đầu năm, {period} ({sub})"

    source = f"Nguồn: CTK; và tính toán của {author}."
    
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.25), ncol=3, fontsize=14, frameon=False)
    fig.text(0.01, 0.02, source, ha="left", va="bottom", fontsize=14)

    axis_style(ax, fig)

    return fig, title



