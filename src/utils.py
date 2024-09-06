import streamlit as st

from PIL import Image
from src.settings import Settings


def calcular_ira(pcs_fisico, pcs_teorico):
    # """
    # Calcula la precisión del inventario (IRA).

    # Args:
    # pcs_fisico (int): Cantidad de piezas físicas.
    # pcs_teorico (int): Cantidad de piezas teóricas.

    # Returns:
    # float: El porcentaje de precisión del inventario (IRA).
    # """
    if pcs_teorico == 0:
        return 0
    
    # Calcular la exactitud en porcentaje
    exact = (int(pcs_fisico) / int(pcs_teorico)) * 100
    
    # Aplicar las reglas de límite
    if exact > 200:
        return 0
    elif exact > 100:
        exact = 200 - exact
    elif exact < 0:
        return 0

    return exact

def calcular_ila(qty_loc, qty_loc_error):

    if qty_loc == 0:
        return 0  # Para evitar división por cero
    exact_ila = ((int(qty_loc) - int(qty_loc_error)) / int(qty_loc))*100
    return exact_ila


# ---------- download cv --------------
settings = Settings()

class SideBar:
    
    def __init__(self):
        self.cv = settings.config['docs']['cv']
        # self.profile = Image.open(settings.config['images']['picprofile'])
        
    def profile_picture(self):
        st.image(self.profile, width=500) 
        
    def download_cv(self):
        with open(self.cv, 'rb') as file:
            #Read file
            cv = file.read()
            
            # Button download
            st.download_button(
                label= 'resume PDF',
                data= cv,
                file_name= 'CV_EdgarCastro.PDF',
                mime='application/octer-stream',
                use_container_width=True
            )
            
        # Close file
        file.close()
        