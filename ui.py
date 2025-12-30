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

def source_note(
    fig,
    source: str,
    note: str | None = None,
    x: float = 0.01,
    y: float = 0.02,
    fontsize: int = 14,
):
    text = source if note is None else f"{source}\nNote: {note}"
    fig.text(
        x,
        y,
        text,
        ha="left",
        va="bottom",
        fontsize=fontsize,
        wrap=True
    )

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
        fig.subplots_adjust(top=top, bottom=0.22)











