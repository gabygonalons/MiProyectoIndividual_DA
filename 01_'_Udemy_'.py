import streamlit as st
import pandas as pd


udemy = pd.read_csv('../PI_DA/pi_da_env/modif_udemy.csv')


st.dataframe(udemy)

if st.checkbox('Muestra dimensión del Dataframe:'):
    dim = st.radio('Mostrar Dimensiones del DataFrame:', ('Filas','Columnas'))
    if dim == 'Filas':
        st.write('Cantidad de Filas:', udemy.shape[0])
    else:
        st.write('Cantidad de Columnas:', udemy.shape[1])


