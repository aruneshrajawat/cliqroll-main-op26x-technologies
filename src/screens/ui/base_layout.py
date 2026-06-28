import streamlit as st


def style_background_home():
    st.markdown("""
    <style>
        .stApp{
            background:#5865F2 !important;
        }

        .stApp div[data-testid="stColumn"]{
            background:#BDB76B !important;
            padding:2.5rem !important;
            border-radius:5rem;
        }
    </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
    <style>
        .stApp{
            background:#FDFBD4 !important;
        }
    </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

    #MainMenu,
    header,
    footer{
        visibility:hidden;
    }

    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"]{
        display:none !important;
    }

    .block-container{
        padding-top:1.5rem !important;
    }

    .stApp{
        background:#BAC095 !important;
    }

    h1{
        font-family:'Climate Crisis',sans-serif !important;
    }

    h2{
        font-family:'Climate Crisis',sans-serif !important;
    }

    h3,h4,p,label,span{
        font-family:'Outfit',sans-serif !important;
    }

    div[data-testid="stButton"] button{
        background:#FDFBD4 !important;
        color:#2C2C2C !important;
        border:none !important;
        border-radius:18px !important;
    }

    div[data-testid="stButton"] button:hover{
        transform:scale(1.03);
    }

    div[role="dialog"]{
        background:#FDFBD4 !important;
    }

    button[aria-label="Close"]{
        background:transparent !important;
        border:none !important;
    }

    button[aria-label="Close"] svg{
        stroke:#2C2C2C !important;
    }

    [data-baseweb="toast"]{
        background:#FDFBD4 !important;
    }

    [data-baseweb="toast"] *{
        color:#2C2C2C !important;
    }

    </style>
    """, unsafe_allow_html=True)