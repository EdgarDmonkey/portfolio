import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from src.utils import calcular_ira
from src.utils import calcular_ila

# -----Select
st.header("Select a project")
view_project =  st.selectbox("Project", ["Inventory", "Dashboards", "Apps", "VBA", "Others"])

#-------------------------Projects-----------------------------

# Inventory

# ** Data **

ira = {
    'Año': ['2017', '2018', '2019', '2020', '2021', '2022'],
    'Ira': [95.5, 98, 99.5, 99.80, 99.91, 99.95],
    'Desviacion': [4.5, 3, 0.5, 0.2, 0.09, 0.05]
}

# Data frame
df = pd.DataFrame(ira)

# Graph
fig = px.bar(ira,x='Año', y='Desviacion',title='Growth of inventory accuracy control')

# Customize the chart's appearance
fig.update_layout(
    title_font_size=14,      # Tamaño del título
    title_font_color="white", # Color del título
    xaxis_title="Year",       # Título del eje X
    yaxis_title="Percentage deviation (%)", # Título del eje Y
    xaxis_tickangle=-90,     # Rotación de los valores en el eje X
    plot_bgcolor=None,  # Fondo transparente
    paper_bgcolor=None, # Fondo del gráfico
    font=dict(
        family="Work Sans, sans-serif",  # Fuente de texto
        size=12,                     # Tamaño de fuente de los textos
        color="black"                # Color del texto
    )
)

# Colors bar
fig.update_traces(marker_color='aqua', marker_line_color='gray', marker_line_width=1)



# Conditional wiew

if view_project == 'Inventory':
    st.title('Inventory management')
    with st.form("IRA"):
        st.write("Inventory Accuracy")
        col5, col6 = st.columns([1, 1], gap="small")
        with col5:
            pcs_theoric = st.text_input('Enter the theoretical pieces', value="")
            pcs_physical = st.text_input('Enter the physical pieces', value="")
        with col6:
            qty_localities = st.text_input('Inventoried localities', value="")
            qty_localities_error = st.text_input('Locations inventoried with error', value="")
        submit_button = st.form_submit_button('Submit') 

 
    # Valores predeterminados para evitar errores
        ira_pcs = None
        ila_loc = None

    # # Lógica para cálculo
        if not pcs_theoric or not pcs_physical or not qty_localities or not qty_localities_error:
            st.warning("Por favor, ingresa todos los valores.")
        else:
    # Convertir valores y calcular IRA y ILA
            try:
                ira_pcs = calcular_ira(pcs_physical, pcs_theoric)  #int(pcs_physical) / int(pcs_theoric)
                ila_loc = calcular_ila(qty_localities,qty_localities_error)  #(int(qty_localities) - int(qty_localities_error)) / int(qty_localities)
            except ValueError:
                st.error("Por favor, ingresa valores numéricos válidos.")
        if ira_pcs is not None:
            st.subheader(f'IRA: {round(ira_pcs,2)}%')
        if ila_loc is not None:
            st.subheader(f'ILA: {round(ila_loc,2)}%') 
    st.subheader('Growth')    
    col3, col4 = st.columns([.40,.60], gap="small", vertical_alignment="center")
    with col3:
        st.dataframe(df)
    with col4:
        st.plotly_chart(fig) 
elif view_project == 'Dashboards':
    st.title('Dashboard development')
    video_url_bi = 'https://youtu.be/K0a4ru7Nm9M'
    st.video(video_url_bi)
elif view_project == 'Apps':
    st.title('Application development')
    # video_url_app = 'https://youtu.be/2ZdVVUmsLPA'
    # st.video(video_url_app)
elif view_project == 'VBA':
    st.title('A little bit of VBA')
    # video_url = 'https://youtu.be/M5_dguu0Qdo'
    # st.video(video_url)
elif view_project == 'Others':
    st.title('Development')





