import streamlit as st

from src.settings import Settings
from streamlit_option_menu import option_menu
from side_bar import SideBar


settings = Settings()

st.set_page_config(
    page_title= 'Edgar Adrian Castro Romero',
    layout= 'wide', initial_sidebar_state= 'expanded'
 )

# Sidebar
with st.sidebar:
    
    # Instance Sidebar
    sb = SideBar()
    
    st.title('Edgar Developer')
    
    #Button download
    
    sb.download_cv()
    
    
    # Menu Nav
    selected = option_menu(
        menu_title= None,
        options= settings.config['styling']['pages'],
        default_index= 0
    )
    
    sb.profile_picture()
    
# Selected page

# About me
if selected == settings.config['styling']['pages'][0]:
    st.title(':wave: About Me')

# Portfolio    
elif selected == settings.config['styling']['pages'][1]:
    st.title(':book: Portfolio')

#--Add each project here below and index the numbers page in the congi.yml    



if __name__=='__main__':
    settings.site_footer()
    print('Hello world')
