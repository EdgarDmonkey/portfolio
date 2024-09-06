import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

#from src.settings import Settings
#from streamlit_option_menu import option_menu
from src.utils import SideBar


col1, col2 = st.columns([.40,.60], gap="small", vertical_alignment="center")
with col1:
        st.image("./images/pic_portfolio.png", width=350) 
with col2:
        st.title('Edgar Adrian Castro Romero', anchor=False)
        st.write('Software Developer | Data Analyst')
        st.write(
            """
                I am a software developer, with experience in data analytics,
            """
                )
        #Button download
        sb = SideBar()
        sb.download_cv()
        
        
# Sections Experience
st.write("\n")
st.subheader('Experience:')
st.write(
        """
        4e Global | Inventory manager
        
        I have been fortunate enough to have a pleasant experience working on this project, 
        helping to create work controls to increase inventory accuracy, validation processes, and information flows. 
        I have learned to lead teams by focusing the efforts and skills of each member toward a common goal.
        """
        )
st.write("\n")
st.write("Challenges:")
st.write(
        """
            - Reduction of W2W validation activity times.
            - Reduction of obsolete and non-rotating inventory.
            - Inventory connection analysis or inventory flow analysis.
            - Standardization of capture flow processes.
            - Inventory reconciliation analysis processes.
            - Personnel development and integration of position indicators.
        """
    
)

# Selected 

st.header("View results")
view_results = st.selectbox("Select", ["None", "Show"])

# Data

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

# Cambiar el color de las barras
fig.update_traces(marker_color='aqua', marker_line_color='gray', marker_line_width=1)

# Render graph

if view_results == 'Show':
    col3, col4 = st.columns([.40,.60], gap="small", vertical_alignment="center")
    with col3:
        st.dataframe(df)
    with col4:
        st.plotly_chart(fig)    
elif view_results == 'None':
    pass    



#--How did you solve it?

st.write("\n")
st.write("Solutions:")
st.write(
        """
            - Implementation of data-driven controls and validation processes, achieving a threefold reduction in validation activity time.
            - Massive analysis of historical and current transactions.
            - Clustering of materials according to their rotation classification.
            - Inventory level indicators.
            - Proper standardization of consumption flows, transfers, receipts, and all operational movements.
            - Continuous training of personnel responsible for data ingestion.
            - Cyclical validation activities and information analysis with clear accountability and prompt root-cause solutions.
            - Measurable objectives aligned with responsibilities, allowing individuals to have a metric for growth and development based on their achievements and capabilities.
        """
    
)
#--------------Second experience

# Sections Experience 2do
st.write("\n")
st.write(
        """
        AVIOR / TRAXION | Data Analyst Sr.
        
        A great experience, contributing expertise within an agile team where we constantly aimed 
        to deliver value to the business, ensuring data integrity and using the correct analysis methods to obtain 
        the clearest view of the dynamic daily operations. I was involved in activities such as indicators, applications, reports, 
        and processes, always prioritizing agile methodologies.
        """
        )
st.write("\n")
st.write("Activities:")
st.write(
        """
            - Standardization of information sources.
            - Validation controls for data integrity.
            - Continuous reconciliation of data and obtained information.
            - Development of applications in very short time frames.
            - Multiple tasks performed simultaneously.
            - Inter-departmental cooperation.
        """
)

st.write("\n")


# Sections Skills
st.write("\n")
st.subheader("Skills:")
st.write("Programming languages")
st.write(
        """
        - Dashboards en power BI (Dax)
        - Utilizando python con pandas, matplotlib, numpy.
        - Power apps
        - Power Automate
        - SQL , T-SQL

        """
        )

st.write("Platforms and tools")
st.write(
        """
        - Streamlit
        - Git
        - Power BI
        - Power apps
        - Power Automate
        - SQL Server
        - Azure
        - Excel / VBA
        - Share Point

        """
        )

st.write("Others")
st.write(
        """
        - Kanban and scrum
        - 
        """
        )