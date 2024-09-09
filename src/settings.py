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
