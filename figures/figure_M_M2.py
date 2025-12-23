import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def make_figure_M_M2(fig_no=None, save=False):

    df = pd.read_pickle("data/M_M2.pkl")

    df["date"] = pd.to_datetime(
        dict(year=df["year"], month=df["month"], day=1)
    )

    # Tính đóng góp cho tăng trưởng M2

    components = ["M2","Firm_deposits","Household_deposits","Currency","Commercial_papers",]
    
    for c in components:
        df[f"D12_{c}"] = (df[c] - df[c].shift(12)) / df["M2"].shift(12) * 100

    df_long = df.melt(
        id_vars=["date", "year", "month", "D12_M2"],
        value_vars=["D12_Firm_deposits","D12_Household_deposits","D12_Currency","D12_Commercial_papers",],
        var_name="component",
        value_name="value",
    )

    label = {
        "D12_Firm_deposits": "Tiền gửi TCKT",
        "D12_Household_deposits": "Tiền gửi dân cư",
        "D12_Currency": "Tiền mặt lưu thông",
        "D12_Commercial_papers": "Giấy tờ có giá",
    }
    df_long["component"] = df_long["component"].map(label)

    components_order = list(label.values())

    df = df.sort_values(["year", "month"])
    y_start, m_start = 2023, 1
    y_max = df["year"].iloc[-1]
    m_max = df["month"].iloc[-1]

    period = f"{m_start}/{y_start}-{m_max}/{y_max}"
 
    sns.set_theme(style="white", font="Times New Roman")

    fig, ax = plt.subplots(figsize=(10, 6), dpi=200)

    start_date = pd.Timestamp(year=y_start, month=m_start, day=1)

    df_line = df.loc[df["date"] >= start_date, ["date", "D12_M2"]]
    df_long = df_long.loc[df_long["date"] >= start_date]

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
            alpha=0.8
        )

        pos_bottom += np.where(v >= 0, v, 0)
        neg_bottom += np.where(v < 0, v, 0)

    
    ax.plot(
        df_line["date"],
        df_line["D12_M2"],
        color="red",
        marker="o",
        linewidth=1.8,
        label="Tổng phương tiện thanh toán"
    )

    subtitle = "%, so cùng kỳ"
    ax.set_title(f"Tốc độ tăng tổng phương tiện thanh toán, {period} ({subtitle})",fontsize=14, fontweight="bold")

    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.legend(frameon=False)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(0.6)
    ax.spines["bottom"].set_linewidth(0.6)

    source = "Nguồn: CTK; và tính toán của Ban QLRRTH."
    fig.text(0.01, 0.01, source, ha="left", va="bottom", fontsize=9)

    fig.tight_layout()
    fig.subplots_adjust(bottom=0.12)

    return fig
