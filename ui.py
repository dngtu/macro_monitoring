import streamlit as st

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

# ui/styles.py

def figure_style(
    fig,
    *,
    source=None,
    note=None,
    source_pos=(0.01, 0.02),
    fontsize=14,
    top=0.8,
    bottom=0.12
):
    if source:
        fig.text(
            source_pos[0],
            source_pos[1],
            source,
            ha="left",
            va="bottom",
            fontsize=fontsize
        )

    if note:
        fig.text(
            source_pos[0],
            source_pos[1] - 0.035,
            note,
            ha="left",
            va="bottom",
            fontsize=fontsize
        )

    fig.tight_layout()
    fig.subplots_adjust(top=top, bottom=bottom)

def axis_style(
    ax,
    fig=None,
    *,
    tick_size=14,
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
        fig.subplots_adjust(top=top, bottom=bottom)






