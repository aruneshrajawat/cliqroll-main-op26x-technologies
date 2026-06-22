import streamlit as st

def header_home():
    logo_url = "https://res.cloudinary.com/dt0souxst/image/upload/v1779278495/file_0000000009e4722fb45e2f0f4ccdc363_z7jslu.png"
    st.markdown(f"""
    <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:0px; margin-top:0px;">
        <img src='{logo_url}' style='height:100px;'/>
        <h1 style='text-align:center; color:#000000;'>CliqRoll</h1>
    </div>
    """, unsafe_allow_html=True)


def header_dashboard():
    logo_url = "https://res.cloudinary.com/dt0souxst/image/upload/v1779278495/file_0000000009e4722fb45e2f0f4ccdc363_z7jslu.png"
    st.markdown(f"""
    <div style="display:flex; align-items:center; gap:10px;">
        <img src='{logo_url}' style='height:45px; display:block;'/>
        <span style='color:#000000; font-size:1.8rem; font-weight:bold; line-height:1; margin:0; font-family: Climate Crisis, sans-serif;'>CliqRoll</span>
    </div>
    """, unsafe_allow_html=True)
