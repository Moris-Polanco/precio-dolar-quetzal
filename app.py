import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Cargar los datos de cambio de moneda en un DataFrame
df = pd.read_csv("currency_data.csv")

# Seleccionar las columnas de entrada y la columna de salida
X = df[["fecha", "precio_dolar_hoy"]]
y = df["precio_quetzal_mañana"]

# Entrenar un modelo de random forest
model = RandomForestRegressor()
model.fit(X, y)

st.title("Predicción del precio del quetzal")

# Obtener la fecha de entrada del usuario
fecha = st.text_input("Ingrese la fecha (en formato YYYY-MM-DD):")

# Obtener el precio del dólar de hoy del usuario
precio_dolar_hoy = st.text_input("Ingrese el precio del dólar de hoy:")

# Realizar la predicción al hacer clic en el botón
if st.button("Realizar predicción"):
    prediccion = model.predict([[fecha, precio_dolar_hoy]])[0]
    st.success("El precio del quetzal mañana será de ${:.2f}".format(prediccion))
