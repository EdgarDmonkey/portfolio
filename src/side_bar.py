import streamlit as st

from PIL import Image
from .settings import Settings

# Load project settings
settings = Settings()

class SideBar:
    
    def __init__(self):
        self.cv = settings.config['docs']['cv']
        self.profile = Image.open(settings.config['images']['picprofile'])
        
    def profile_picture(self):
        st.image(self.profile) 
        
    def download_cv(self):
        with open(self.cv, 'rb') as file:
            #Read file
            cv = file.read()
            
            # Button download
            st.download_button(
                label= 'resume PDF',
                data= cv,
                file_name= 'EdgarCastro.PDF',
                mime='application/octer-stream',
                use_container_width=True
            )
            
        # Close file
        file.close()
        