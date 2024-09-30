
import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

conn = st.connection("gsheets", type=GSheetsConnection)

existing_data = conn.read(worksheet="Hoja1", usecols=list(range(6)), ttl=5)
existing_data = existing_data.dropna(how="all")

# mostrar el dataframe con los datos
# st.dataframe(existing_data)

col_izq, col_der = st.columns(2)
with col_izq:
    st.image('./assets/brunenina.gif',)
with col_der:
    st.markdown("<h3 style='text-align: center'>Confirmar Asistencia</h3>", unsafe_allow_html=True)
    with st.form(key="Form1"):
        nombre = st.text_input("Nombre")
        apellido = st.text_input("Apellido")
        telefono = st.text_input("Telefono")
        value = [[nombre, apellido, telefono]]
        submit_button = st.form_submit_button("Enviar")
if submit_button and nombre != '' and apellido != '' and telefono != '':
    agregar_asistente = pd.DataFrame([{
        "Nombre": nombre,
        "Apellido": apellido,
        "Telefono": telefono
    }])
    update_df = pd.concat([existing_data, agregar_asistente], ignore_index=True)
    with col_der:
        left_co, cent_co,last_co = st.columns((1, 2, 1))
        with cent_co:
            st.success('Gracias por venir al cumple!')
            st.image('./assets/gifkitty.gif')
else: 
    submit_button and nombre == '' and apellido == '' and telefono == ''
    st.error("Te olvidaste de ingresar alguno de los datos")

# Update Google Sheets with the new vendor data
conn.update(worksheet="Hoja1", data=update_df)