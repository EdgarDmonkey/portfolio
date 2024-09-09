import streamlit as st
import pandas as pd

from src.settings import Settings
# from streamlit_option_menu import option_menu
# from src.side_bar import SideBar


# Pages
about_me = st.Page(
    page="src/about_me.py",
    title="About Me",
    icon=None,
    default=True    
)  
page_1 = st.Page(
     page="src/portfolio.py",
     title="Portfolio",
     icon=None    
 )

 


pg = st.navigation(
    {
        "Info": [about_me],
        "Pages": [page_1]
    }
)


# side bar
st.sidebar.subheader("Code as a service")
st.sidebar.text("Made: Edgar Castro 2024")
st.logo(image='.\images\logo_streamlit.svg')

if __name__=='__main__':
    pg.run()
    print('we live!!!')
