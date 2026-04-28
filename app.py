import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis de Anuncios de Venta de Coches')

st.write('Explora los datos de anuncios de venta de coches usados. '
         'Selecciona las casillas de verificación para visualizar los gráficos.')

# Casilla de verificación para el histograma
build_histogram = st.checkbox('Construir histograma')

if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig_hist = px.histogram(car_data, x='odometer')
    fig_hist.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig_scatter = px.scatter(car_data, x='odometer', y='price')
    fig_scatter.update_layout(title_text='Relación entre Odómetro y Precio')
    st.plotly_chart(fig_scatter, use_container_width=True)
