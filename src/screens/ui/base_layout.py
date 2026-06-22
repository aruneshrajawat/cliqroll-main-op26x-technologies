import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: #5865F2 !important;
            }
            .stApp div[data-testid="stColumn"] {
                background-color: #ffffff !important;
                padding: 2.5rem !important;
                border-radius: 2rem !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #F5F6FA !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');

            #MainMenu, footer, header {
                visibility: hidden;
            }

            .block-container {
                padding-top: 1.5rem !important;
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
                color: #1A1A2E !important;
            }

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
                color: #1A1A2E !important;
            }

            h3, h4, p {
                font-family: 'Outfit', sans-serif !important;
                color: #2C2C2C !important;
            }

            button[kind="secondary"] {
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 0.5rem 1.5rem !important;
                border: none !important;
                font-size: 1rem !important;
                transition: transform 0.2s ease !important;
            }

            button[kind="tertiary"] {
                border-radius: 1.5rem !important;
                background-color: transparent !important;
                color: #5865F2 !important;
                padding: 10px 20px !important;
                border: 1px solid #5865F2 !important;
                font-size: 1rem !important;
                transition: transform 0.2s ease !important;
            }

            button {
                border-radius: 1.5rem !important;
                transition: transform 0.2s ease !important;
            }

            button:hover {
                transform: scale(1.03) !important;
            }
        </style>
    """, unsafe_allow_html=True)
