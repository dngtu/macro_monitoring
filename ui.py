import streamlit as st

author = "Đặng Ngọc Tú"

def render_title(title: str):
    st.markdown(
        f"""
        <div style="
            text-align:center;
            font-size:16px;
            font-weight:600;
            font-family:'Times New Roman', Times, serif;
            margin-bottom:8px;
        ">
            {title}
        </div>
        """,
        unsafe_allow_html=True,
    )