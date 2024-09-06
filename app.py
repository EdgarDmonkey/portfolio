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




# settings = Settings()

# st.set_page_config(
#     page_title= 'Edgar Adrian Castro Romero',
#     layout= 'wide', initial_sidebar_state= 'expanded'
#  )



# # Sidebar
# with st.sidebar:
  
    
    
    
#     # Instance Sidebar
#     sb = SideBar()
    
#     st.title('Code as a service')
    
#     #Button download
    
#     sb.download_cv()
    
    
#     # Menu Nav
#     selected = option_menu(
#         menu_title= None,
#         options= settings.config['styling']['pages'],
#         default_index= 0
#     )
    
#     settings.site_footer()
    
    
# # Selected page

# # About me
# if selected == settings.config['styling']['pages'][0]:

         
# # Portfolio    
# elif selected == settings.config['styling']['pages'][1]:
#     st.title(':book: Portfolio')

#--Add each project here below and index the numbers page in the congi.yml    


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
