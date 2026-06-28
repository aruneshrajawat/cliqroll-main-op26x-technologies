import streamlit as st


def style_base_layout():
    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

    /* ------------------------- */
    /* Hide Streamlit UI         */
    /* ------------------------- */

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

    /* ------------------------- */
    /* Typography                */
    /* ------------------------- */

    h1{
        font-family:'Climate Crisis',sans-serif !important;
        font-size:3.5rem !important;
        line-height:1.1 !important;
        color:#2C2C2C;
    }

    h2{
        font-family:'Climate Crisis',sans-serif !important;
        font-size:2rem !important;
        line-height:1.1 !important;
        color:#2C2C2C;
    }

    h3,
    h4,
    p,
    label,
    span{
        font-family:'Outfit',sans-serif !important;
        color:#2C2C2C;
    }

    /* ------------------------- */
    /* ONLY Streamlit Buttons    */
    /* ------------------------- */

    div[data-testid="stButton"] button{

        background:#FDFBD4 !important;
        color:#2C2C2C !important;

        border:none !important;
        border-radius:18px !important;

        transition:.25s;
    }

    div[data-testid="stButton"] button:hover{
        transform:scale(1.03);
    }

    div[data-testid="stButton"] button[kind="secondary"]{
        background:#EB459E !important;
        color:white !important;
    }

    div[data-testid="stButton"] button[kind="tertiary"]{
        background:#5865F2 !important;
        color:white !important;
    }

    /* ------------------------- */
    /* Dialog                    */
    /* ------------------------- */

    div[role="dialog"]{

        background:#FDFBD4 !important;
        border-radius:18px !important;
    }

    div[role="dialog"] *{
        color:#2C2C2C !important;
    }

    /* Close button */

    button[aria-label="Close"]{

        background:transparent !important;

        border:none !important;

        border-radius:50% !important;

        width:40px !important;
        height:40px !important;

        display:flex !important;
        align-items:center !important;
        justify-content:center !important;
    }

    button[aria-label="Close"]:hover{

        background:#E7E2AE !important;

    }

    button[aria-label="Close"] svg{

        width:18px !important;
        height:18px !important;

        stroke:#2C2C2C !important;
        color:#2C2C2C !important;
    }

    /* ------------------------- */
    /* Toast                     */
    /* ------------------------- */

    [data-baseweb="toast"]{

        background:#FDFBD4 !important;
        color:#2C2C2C !important;

        border-radius:12px !important;

        border:1px solid #DDD7A5 !important;
    }

    [data-baseweb="toast"] *{
        color:#2C2C2C !important;
    }

    /* ------------------------- */
    /* Success Alert             */
    /* ------------------------- */

    div[data-testid="stAlert"]{

        background:#FDFBD4 !important;

        color:#2C2C2C !important;

        border-left:4px solid #5865F2 !important;

    }

    div[data-testid="stAlert"] *{

        color:#2C2C2C !important;

    }

    </style>
    """, unsafe_allow_html=True)