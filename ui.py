import streamlit as st

from matplotlib import font_manager
import matplotlib.pyplot as plt

font_manager.fontManager.addfont("assets/fonts/Inter-Regular.ttf")
font_manager.fontManager.addfont("assets/fonts/Inter-Bold.ttf")

plt.rcParams.update({
    "font.family": "Inter",
    "axes.unicode_minus": False,
})

author = "Đ.N.T"

def render_title(title: str):
    st.markdown(
        f"""
        <div style="
            text-align:center;
            font-size:14px;
            font-weight:700;
            font-family: 'DejaVu Sans', 'DejaVuSans', sans-serif;
            margin-bottom:8px;
        ">
            {title}
        </div>
        """,
        unsafe_allow_html=True,
    )
    
def legend(
    ax,
    ncol: int = 4,
    fontsize: int = 12,
    y: float = 1.25,
):
    ax.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, y),
        ncol=ncol,
        fontsize=fontsize,
        frameon=False,
    )

def source_note(
    fig,
    source: str,
    note: str | None = None,
    fontsize: int = 12,
):
    has_note = bool(note)

    # Điều chỉnh layout: có note thì chừa nhiều hơn
    fig.subplots_adjust(bottom=0.22 if has_note else 0.14)

    # Vị trí source (luôn gần đồ thị)
    y_source = 0.05 if has_note else 0.07

    fig.text(
        0.01,
        y_source,
        source,
        ha="left",
        va="bottom",
        fontsize=12,
    )

    # Vị trí note (chỉ vẽ khi có)
    if has_note:
        fig.text(
            0.01,
            0.04,
            note,
            ha="left",
            va="bottom",
            fontsize=12,
            wrap=True,
        )

def axis_style(
    ax,
    fig=None,
    *,
    tick_size=10,
    spine_width=0.6,
    grid_alpha=0.5,
    grid_width=0.8,
    top=0.8,
    bottom=0.12
):
    ax.tick_params(axis="x", labelsize=tick_size)
    ax.tick_params(axis="y", labelsize=tick_size)
    
    ax.set_xlabel(None)
    ax.set_ylabel(None)

    for spine in ["top", "left", "right"]:
        ax.spines[spine].set_visible(False)
        ax.spines["bottom"].set_linewidth(spine_width)
    
    ax.grid(axis="y", alpha=grid_alpha, linewidth=grid_width)

    if fig is not None:
        fig.tight_layout()
        fig.subplots_adjust(top=top, bottom=0.22)



















