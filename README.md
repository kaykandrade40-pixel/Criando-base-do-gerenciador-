# Criando-base-do-gerenciador-
import streamlit as st

st.title("Meu Gerenciador de Gastos")
gasto = st.number_input("Quanto você gastou hoje?")
if st.button("Salvar"):
    st.write(f"Você gastou R$ {gasto}. Registro salvo!")
