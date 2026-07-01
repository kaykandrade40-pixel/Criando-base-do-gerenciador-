import streamlit as st
import pandas as pd
from datetime import datetime

st.title("Meu Gerenciador de Gastos")

# Campos de entrada
item = st.text_input("Nome do item (ex: Água, Proteína)")
valor = st.number_input("Valor", min_value=0.0, format="%.2f")

if st.button("Salvar Gasto"):
    # Criar uma linha com os dados
    novo_gasto = {
        "Data": [datetime.now().strftime("%d/%m/%Y")],
        "Item": [item],
        "Valor": [valor]
    }
    
    # Transformar em DataFrame
    df = pd.DataFrame(novo_gasto)
    
    # Salvar em um arquivo CSV (se o arquivo não existir, ele cria)
    # mode='a' significa 'append' (adicionar ao final do arquivo)
    df.to_csv("meus_gastos.csv", mode='a', index=False, header=False)
    
    st.success(f"Gasto de R$ {valor} em '{item}' salvo com sucesso!")

# Visualizar o histórico
if st.button("Ver Histórico"):
    try:
        df_historico = pd.read_csv("meus_gastos.csv", names=["Data", "Item", "Valor"])
        st.write(df_historico)
    except FileNotFoundError:
        st.warning("Nenhum gasto registrado ainda.")
