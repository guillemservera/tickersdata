
import streamlit as st

st.set_page_config(
    page_title="Tickers Data · Small-Caps Research Made Simple",
    page_icon="📊",
    layout="wide",
)

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"]::before {
            content: "Tickers Data";
            display: block;
            font-weight: bold; /* Makes the font bold */
            margin-left: 25px;
            margin-top: 0px;
            margin-botton: 0px;
            font-size: 2em;
            position: relative;
            top: 40px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

add_logo()

# Page content
st.markdown("""
    ## Welcome to Tickers Data

    ##
    
    Feel free to share feedback and ideas.

                   
    Developed by [Guillem Servera](https://twitter.com/guillemservera)
""")

