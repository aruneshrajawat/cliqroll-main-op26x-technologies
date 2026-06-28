import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
                .stApp{
                    background: #5865F2 !important;
                }

                .stApp div[data-testid ="stColumn"]{
                    background-color:#BDB76B !important;
                    padding:2.5rem !important;
                    border-radius:5rem;
                    }
        </style>
                """
            , unsafe_allow_html=True)
    
    
def style_background_dashboard():
    st.markdown("""
        <style>
                .stApp{
                    background: #FDFBD4 !important;
                }
        </style>
                """
            , unsafe_allow_html=True)
        

        

def style_base_layout():
    st.markdown("""
        <style>
                /* Hide top tool bar of streamlit */

                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');

                #MainMenu,footer,header{
                    visibility:hidden;
                }

                /* Hide Streamlit toolbar and logo */
                [data-testid="stToolbar"] {
                    display: none !important;
                }

                [data-testid="stDecoration"] {
                    display: none !important;
                }

                [data-testid="stStatusWidget"] {
                    display: none !important;
                }

                .block-container{
                    padding-top:1.5rem !important;
                }
                .stApp{
                    background: #BAC095!important;
                }
                h1{
                    font-family: 'Climate Crisis', sans-serif !important;
                    font-size : 3.5rem !important;
                    line-height: 1.1 !important;
                    margin-bottom:0rem !important;
                    color: #2C2C2C;
                }
                h2{
                    font-family: 'Climate Crisis', sans-serif !important;
                    font-size : 2rem !important;
                    line-height: 1.1 !important;
                    margin-bottom:0rem !important;
                    color: #2C2C2C;
                }

                h3,h4,p{
                    font-family: 'Outfit', sans-serif !important;
                    color: #2C2C2C;
                }
                button[kind = "Secondary"]{
                    border-radius: 1.5rem !important;
                    background-color: #EB459E !important;
                    color: white  !important;
                    padding: 0.5rem 1.5rem !important;
                    border: none !important;
                    font-size: 1rem !important;
                    transition: transform 0.3s ease in out !important;
                    }

                button[kind = "Tertiary"]{
                    border-radius: 1.5rem !important;
                    background-color: #5865F2 !important;
                    color: white  !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    font-size: 1rem !important;
                    transition: transform 0.3s ease in out !important;
                    }
                button{
                    border-radius: 1.5rem !important;
                    background-color: #FDFBD4 !important;
                    color: black  !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    font-size: 1rem !important;
                    transition: transform 0.3s ease in out !important;
                    }
                button:hover{
                    transform: scale(1.05) !important;
                }
                div[role="dialog"],
                div[data-testid="stDialog"],
                div[data-testid*="Dialog"] {
                    background-color: #FDFBD4 !important;
                }
                div[role="dialog"] *,
                div[data-testid="stDialog"] *,
                div[data-testid*="Dialog"] * {
                    color: #2C2C2C !important;
                }
                div[data-testid="stToast"] {
                    background-color: #FDFBD4 !important;
                }
                div[data-testid="stToast"] * {
                    color: #2C2C2C !important;
                }
                div[role="dialog"] svg,
                div[data-testid="stDialog"] svg,
                div[data-testid*="Dialog"] svg {
                    fill: #2C2C2C !important;
                    color: #2C2C2C !important;
                }
                
        </style>
                """
            , unsafe_allow_html=True)
        
