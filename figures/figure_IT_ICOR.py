import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import textwrap
from ui import author, axis_style

def make_figure_IT_ICOR(fig_no=None, save=False):

    # ===============================================================================================
    # Load data
    # ===============================================================================================

    df = pd.read_pickle("data/IT_ICOR.pkl").sort_values(["year"])
    df["year"] = df["year"].astype(int)
    y_max = df["year"].max()

    # ===============================================================================================
    # Parameters & Labels
    # ===============================================================================================

    y_start = 2019
    period = f"{y_start}-{y_max}"

    # ===============================================================================================
    # Data transformation
    # ===============================================================================================   
    
    df = df[df["year"].between(y_start, y_max)]

    df_long = df.melt(
        id_vars="year",
        value_vars=["ICOR_STA","ICOR_NST","ICOR_FDI","ICOR"],
        var_name="sector",
        value_name="value"
    )

    sector_map = {
        "ICOR_STA": "Nhà nước",
        "ICOR_NST": "Ngoài Nhà nước",
        "ICOR_FDI": "Nước ngoài",
        "ICOR": "Tổng số"
    }
    df_long["sector"] = df_long["sector"].map(sector_map)

    # ===============================================================================================
    # Figure setup 
    # ===============================================================================================
    
    sns.set_theme(style="white", font="DejaVu Sans")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=200)

    # ===============================================================================================
    # Plotting 
    # ===============================================================================================

    sns.barplot(
        data=df_long,
        x="year", y="value", hue="sector",
        errorbar=None,
        ax=ax
    )

    # ===============================================================================================
    # Title, legend, source
    # ===============================================================================================

    sub = "% tăng, so cùng kỳ"

    title = f"Hiệu quả đầu tư (ICOR) theo khu vực kinh tế, {y_start}-{y_max} ({sub})"
    source = f"Nguồn: CTK; và tính toán của {author}."
    note = ("Chú thích: Vốn Nhà nước gồm vốn đầu tư công "
            "(từ NSNN và tín dụng đầu tư của Nhà nước) "
            "và vốn của DNNN cùng các nguồn khác.")
    note_wrapped = textwrap.fill(note, width=120)

    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.25), ncol=4, fontsize=14, frameon=False)
    fig.text(0.01, 0, f"{source}\n{note_wrapped}", ha="left", va="bottom", fontsize=14)

    axis_style(ax, fig)
   
    return fig, title




