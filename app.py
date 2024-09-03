import streamlit as st
import pandas as pd

from src.settings import Settings
from streamlit_option_menu import option_menu
from src.side_bar import SideBar


settings = Settings()

st.set_page_config(
    page_title= 'Edgar Adrian Castro Romero',
    layout= 'wide', initial_sidebar_state= 'expanded'
 )


# Sidebar
with st.sidebar:
    
    # Instance Sidebar
    sb = SideBar()
    
    st.title('Code as a service')
    
    #Button download
    
    sb.download_cv()
    
    
    # Menu Nav
    selected = option_menu(
        menu_title= None,
        options= settings.config['styling']['pages'],
        default_index= 0
    )
    
    
    
# Selected page

# About me
if selected == settings.config['styling']['pages'][0]:
    col1, col2 = st.columns([.60, .40], gap="small",vertical_alignment="top",)
    with col1:
        sb.profile_picture()
        st.title('Edgar Castro') 
        st.write(
            """
            - 6 años de experiencia en analisis de datos
            - 
            """
        )
    with col2:
        st.title('Edgar Castro')
        st.write(
            """
                I am a software developer, with experience in data analytics,
            """
            )
# Portfolio    
elif selected == settings.config['styling']['pages'][1]:
    st.title(':book: Portfolio')

#--Add each project here below and index the numbers page in the congi.yml    



if __name__=='__main__':
    settings.site_footer()
    print('Hello world')
