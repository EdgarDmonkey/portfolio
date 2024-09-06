import os
import yaml
import streamlit as st
from streamlit import markdown


class Settings:
    def __init__(self) -> None:
        """Initialize the app's settings"""
        # Relative path to directory root
        self.ROOT = os.path.dirname(os.path.dirname(__file__))
        
        with open(os.path.join(self.ROOT,'config.yml'), 'r') as file:
            self.config = yaml.safe_load(file)
        file.close()
        
    def site_footer(self):
        # HTML string to render
        content_str = f'''
        <p style="text-align: center; font-size: 15px">
            <br>
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-c-circle" viewBox="0 0 16 16">
                <path d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0M8.146 4.992c-1.212 0-1.927.92-1.927 2.502v1.06c0 1.571.703 2.462 1.927 2.462.979 0 1.641-.586 1.729-1.418h1.295v.093c-.1 1.448-1.354 2.467-3.03 2.467-2.091 0-3.269-1.336-3.269-3.603V7.482c0-2.261 1.201-3.638 3.27-3.638 1.681 0 2.935 1.054 3.029 2.572v.088H9.875c-.088-.879-.768-1.512-1.729-1.512"/>
                </svg>
                {self.config['main']['copyright']}
            </br>
            <br>
                Build with   <a href={self.config['main']['components_repository']} style="color: white">
                    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-github" viewBox="0 0 16 16">
                    <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8"/>
                    </svg>
                </a> 
                and
                <a href={self.config['main']['streamlit']} style="color: white"> 
                    <svg width="32" height="18" fill="none" xmlns="http://www.w3.org/2000/svg" alt="Streamlit Logo. Click to go back to the home page." viewBox="0 0 301 165" class="max-h-5 w-auto"><path d="M150.731 101.547l-52.592-27.8-91.292-48.25c-.084-.083-.25-.083-.334-.083-3.333-1.584-6.75 1.75-5.5 5.083L47.53 149.139l.008.025c.05.117.092.233.142.35 1.909 4.425 6.075 7.158 10.609 8.233.383.084.657.159 1.117.251.459.102 1.1.241 1.65.283.09.008.174.008.266.016h.067c.066.009.133.009.2.017h.091c.059.008.125.008.184.008h.108c.067.009.133.009.2.009a817.728 817.728 0 00177.259 0c.708 0 1.4-.034 2.066-.1l.634-.075c.025-.009.058-.009.083-.017.142-.017.283-.042.425-.067.208-.025.417-.066.625-.108.417-.092.606-.158 1.172-.353.565-.194 1.504-.534 2.091-.817.588-.283.995-.555 1.487-.863a26.566 26.566 0 001.774-1.216c.253-.194.426-.318.609-.493l-.1-.058-99.566-52.617z" fill="#FF4B4B"></path><path d="M294.766 25.498h-.083l-91.326 48.25 50.767 75.609 46.4-118.859v-.167c1.167-3.5-2.416-6.666-5.758-4.833" fill="#7D353B"></path><path d="M155.598 2.556c-2.334-3.409-7.417-3.409-9.667 0L98.139 73.748l52.592 27.8 99.667 52.674c.626-.613 1.128-1.21 1.658-1.841a20.98 20.98 0 002.067-3.025l-50.767-75.608-47.758-71.192z" fill="#BD4043"></path></svg>
                </a>
            </br>
        </p>
        '''
        
        # Render footer str
        markdown(content_str, unsafe_allow_html=True)