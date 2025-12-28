import streamlit as st

author = "Đ.N.Tú"

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




