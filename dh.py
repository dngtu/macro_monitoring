import streamlit as st
from ui import render_title

tab_gdp, tab_cpi, tab_invest, tab_money = st.tabs(["GDP", "CPI", "Investment", "Money"])

from figures.figure_GDP_P import make_figure_GDP_P
from figures.figure_IT import make_figure_IT
from figures.figure_IT_ICOR import make_figure_IT_ICOR
from figures.figure_M_M2 import make_figure_M_M2

with tab_gdp:
    st.header("GDP")
    st.write("Tổng sản phẩm quốc nội")
    tab_gdp_p, tab_gdp_e = st.tabs(["Theo sản xuất", "Theo chi tiêu"])

    with tab_gdp_p:
        fig, title = make_figure_GDP_P()
        render_title(title)
        st.pyplot(fig)

with tab_invest:
    st.header("Đầu tư")
    st.write("Vốn đầu tư phát triển toàn xã hội")
    tab_invest_q, tab_invest_a = st.tabs(["Tăng đầu tư", "Hiệu quả đầu tư"])
    
    with tab_invest_q:
        fig, title = make_figure_IT()
        render_title(title)
        st.pyplot(fig)

    with tab_invest_a:
        fig, title = make_figure_IT_ICOR()
        render_title(title)
        st.pyplot(fig)

with tab_money:  
    st.header("Cung tiền")
    
    fig, title = make_figure_M_M2()
    render_title(title)
    st.pyplot(fig)