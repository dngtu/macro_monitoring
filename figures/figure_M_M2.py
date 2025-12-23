import pandas as pd
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

    fig, ax = plt.subplots(figsize=(10, 8), dpi=200)

    start_date = pd.Timestamp(year=y_start, month=m_start, day=1)

    df_line = df.loc[df["date"] >= start_date, ["date", "D12_M2"]]
    df_long = df_long.loc[df_long["date"] >= start_date]

    for c in components_order:
        tmp = df_long[df_long["component"] == c]
        ax.bar(
            tmp["date"],
            tmp["value"],
            width=20,
            label=c,
            alpha=0.8
        )
        
    ax.plot(
        df_line["date"],
        df_line["D12_M2"],
        color="black",
        marker="o",
        linewidth=1.8,
        label="Tổng phương tiện thanh toán"
    )
    
    subtitle = "% tăng, so cùng kỳ"
    ax.set_title(f"Tăng tổng phương tiện thanh toán theo thành phần, {period} ({subtitle})",fontsize=14, fontweight="bold")

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
