import streamlit as st
import pandas as pd

#CARGA DE DATOS
ruta = 'Datos_CDMB/Estado_ZNI.csv'
df = pd.read_csv (ruta)

#ANALISIS DE DATOS
filas = df.shape [0]
columnas = df.shape [1]


#VIZUALIZACION
st.title('Estado de la Prestación del Servicio de Energia')
st.header('Zonas no Interconectadas (ZNI)')
st.subheader('Conjunto de Datos')


col1, col2 = st.columns (2)

with col1:
    with st.container (border=True):
        st.subheader ("Número de filas")
        st.text (filas)

with col2:
    with st.container (border=True):
        st.subheader ("Número de columnas")
        st.text (columnas)

##OTRA FORMA DE VERLO

col3, col4 = st.columns (2)

with col3:
    st.metric ('Numero de Filas', filas, border=True)

with col4:
    st.metric ('Numero de columnas', columnas, border=True)




print("Hola Mundo")







