import streamlit as st

from src.settings import Settings

settings = Settings()

st.title(':wave: About Me')

if __name__=='__main__':
    settings.site_footer()
    print('Hello world')
