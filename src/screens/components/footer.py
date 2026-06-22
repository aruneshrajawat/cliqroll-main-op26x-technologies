import streamlit as st

def footer_home():
    logo_url = "https://res.cloudinary.com/dt0souxst/image/upload/v1779281494/file_000000003e487208bcda01a76cb05d88_vi0b9p.png"
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:5px; justify-content:center; align-items:center; color:#2B2B2B;">
            <p style="font-weight:bold; margin:0;">Created with ❤️ By</p>
            <img src="{logo_url}" style="max-height:28px; width:auto; vertical-align:middle;"/>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://res.cloudinary.com/dt0souxst/image/upload/v1779281494/file_000000003e487208bcda01a76cb05d88_vi0b9p.png"
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:5px; justify-content:center; align-items:center; color:#2B2B2B;">
            <p style="font-weight:bold; margin:0;">Created with ❤️ By</p>
            <img src="{logo_url}" style="max-height:28px; width:auto; vertical-align:middle;"/>
        </div>
    """, unsafe_allow_html=True)
