import streamlit as st

from src.screens.components.header import header_home
from src.screens.ui.base_layout import style_base_layout,style_background_home
from src.screens.components.footer import footer_home

def home_screen():
    
    header_home()
    style_background_home()
    style_base_layout()
    col1, col2 = st.columns(2)

    with col1:
        st.header("I'm Teacher")
        st.image("https://res.cloudinary.com/dt0souxst/image/upload/v1779258435/file_0000000051d07230acec9ac477901f61_zbryra.png",width = 145)
        if st.button("Teacher Portal",icon = ":material/arrow_outward:",icon_position = "right"):
            st.session_state["login_type"] = "teacher"
            st.rerun()
    with col2:
        st.header("I'm Student")
        st.image("https://res.cloudinary.com/dt0souxst/image/upload/v1779258752/file_00000000a23471fd997ccc0455bc1277_cpgda4.png",width = 145)
        if st.button("Student Portal",icon = ":material/arrow_outward:",icon_position = "right"):
            st.session_state["login_type"] = "student"
            st.rerun()

    footer_home()


