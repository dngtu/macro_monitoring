import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def make_figure_IT_ICOR(fig_no=None, save=False):

    df = pd.read_pickle("data/IT_ICOR.pkl")
    df["year"] = df["year"].astype(int)

    yy = 2018
    y = df["year"].max()
    df = df[df["year"].between(yy, y)]

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

    sns.set_theme(style="white", font="Times New Roman")

    fig, ax = plt.subplots(figsize=(10, 6), dpi=200)

    sns.barplot(
        data=df_long,
        x="year",
        y="value",
        hue="sector",
        errorbar=None,
        ax=ax
    )

    ax.set_title(f"Hiệu quả đầu tư (ICOR) theo khu vực kinh tế, {yy}-{y}",fontsize=14, fontweight="bold")

    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.legend(frameon=False)

    source_a = "Nguồn: CTK; và tính toán của Ban QLRRTH."
    note = ("Chú thích: Vốn Nhà nước gồm vốn đầu tư công "
            "(từ NSNN và tín dụng đầu tư của Nhà nước) "
            "và vốn của DNNN cùng các nguồn khác.")

    fig.text(0.01, 0.01, f"{source_a}\n{note}",
             ha="left", va="bottom", fontsize=11)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(0.6)
    ax.spines["bottom"].set_linewidth(0.6)

    fig.tight_layout()
    fig.subplots_adjust(bottom=0.12)

    plt.close(fig)
    return fig
