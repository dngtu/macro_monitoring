import streamlit as st

tab1, tab2, tab3, tab4 = st.tabs(["GDP", "CPI", "Investment", "Money"])

from figures.figure_IT import make_figure_IT
from figures.figure_IT_ICOR import make_figure_IT_ICOR
from figures.figure_M_M2 import make_figure_M_M2

with tab3:
    st.header("Đầu tư")
    st.write("Vốn đầu tư phát triển toàn xã hội")

    fig = make_figure_IT()
    st.pyplot(fig)

    fig = make_figure_IT_ICOR()
    st.pyplot(fig)

with tab4:  
    st.header("Cung tiền")
    st.write("Tổng phương tiện thanh toán")

    fig = make_figure_M_M2()
    st.pyplot(fig)
