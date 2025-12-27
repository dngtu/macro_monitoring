import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ui import author

def make_figure_GDP_P(fig_no=None, save=False):

    # ===============================================================================================
    # Load data
    # ===============================================================================================
    
    df = pd.read_pickle("data/GDP_P.pkl").sort_values("year")

    q_max = df["quarter"].iloc[-1]
    y_max = df["year"].iloc[-1]
    df = df.loc[df["quarter"] == q_max]

    # ===============================================================================================
    # Parameters & Labels
    # ===============================================================================================

    y_start = 2019  # năm bắt đầu hiển thị
    period = f"{y_start}-{y_max}"
 
    label = {
        "d4_agriculture": "Nông nghiệp",
        "d4_mining": "Khai khoáng",
        "d4_manufacturing": "CN chế biến, chế tạo",
        "d4_construction": "Xây dựng",
        "d4_electricity_water": "Sản xuất điện, nước",
        "d4_service": "Dịch vụ",
        "d4_tax": "Thuế sản phẩm",
    }
    
    components_order = list(label.values())
    
    # ===============================================================================================
    # Data transformation
    # ===============================================================================================
     
    df_long = df.melt(
        id_vars=["year","d4_gdp"],
        value_vars=list(label.keys()),
        var_name="component",
        value_name="value",
    )

    df_long["component"] = df_long["component"].map(label)

    df_line = df.loc[df["year"] >= y_start, ["year", "d4_gdp"]]
    df_long = df_long.loc[df_long["year"] >= y_start]

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
            fontsize=10,
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
    fig.subplots_adjust(top=0.8, bottom=0.12)


    return fig, title



