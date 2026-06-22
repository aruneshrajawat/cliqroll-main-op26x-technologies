import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: #BAC095 !important;
            }
            .stApp div[data-testid="stColumn"] {
                background-color: #ffffff !important;
                padding: 2.5rem !important;
                border-radius: 1.5rem !important;
                box-shadow: 0 4px 24px rgba(0,0,0,0.10) !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #D4DE95 !important;
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
                color: #000000 !important;
            }

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
                color: #000000 !important;
            }

            h3, h4, p {
                font-family: 'Outfit', sans-serif !important;
                color: #000000 !important;
            }

            button[kind="primary"] {
                border-radius: 1.5rem !important;
                background-color: #000000 !important;
                color: #ffffff !important;
                border: none !important;
                font-family: 'Outfit', sans-serif !important;
                font-size: 1rem !important;
                transition: transform 0.2s ease !important;
            }

            button[kind="primary"] p {
                color: #ffffff !important;
            }

            button[kind="secondary"] {
                border-radius: 1.5rem !important;
                background-color: #ffffff !important;
                color: #000000 !important;
                border: 1.5px solid #000000 !important;
                font-family: 'Outfit', sans-serif !important;
                font-size: 1rem !important;
                transition: transform 0.2s ease !important;
            }

            button[kind="secondary"] p {
                color: #000000 !important;
            }

            button[kind="tertiary"] {
                border-radius: 1.5rem !important;
                background-color: transparent !important;
                color: #000000 !important;
                border: 1px solid #BAC095 !important;
                font-family: 'Outfit', sans-serif !important;
                font-size: 1rem !important;
                transition: transform 0.2s ease !important;
            }

            button[kind="tertiary"] p {
                color: #000000 !important;
            }

            /* selectbox, input, text area on dark background */
            div[data-baseweb="select"] *, 
            div[data-baseweb="input"] *,
            .stTextInput input,
            .stSelectbox div {
                color: #000000 !important;
                background-color: #ffffff !important;
            }

            /* metric label and value */
            div[data-testid="stMetricLabel"] p {
                color: #000000 !important;
            }
            div[data-testid="stMetricValue"] {
                color: #000000 !important;
            }

            button:hover {
                transform: scale(1.03) !important;
                opacity: 0.9 !important;
            }

            div[data-testid="stContainer"] {
                border-color: #BAC095 !important;
            }

            div[data-testid="stMetric"] {
                background-color: #ffffff !important;
                border-radius: 0.75rem !important;
                padding: 0.5rem !important;
            }
        </style>
    """, unsafe_allow_html=True)
