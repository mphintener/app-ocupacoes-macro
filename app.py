import streamlit as st
import pandas as pd
import plotly.express as px

# 1. BANCO DE DADOS
instituicoes_macro = [
    {"cidade": "Caieiras", "nome": "ETEC de Caieiras", "cursos": ["Administração", "Logística"]},
    {"cidade": "Franco da Rocha", "nome": "ETEC Dr. Emílio Hernandez", "cursos": ["Logística", "TI"]},
    {"cidade": "Cajamar", "nome": "ETEC Gino Rezaghi", "cursos": ["Logística", "RH"]},
    {"cidade": "Francisco Morato", "nome": "ETEC Francisco Morato", "cursos": ["Informática", "Enfermagem"]}
]

# 2. INTERFACE
st.set_page_config(page_title="App Ocupações", layout="wide")
st.title("📍 Conexão Ocupações")

# 3. FILTROS
cidade_sel = st.sidebar.selectbox("Escolha sua Cidade:", ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"])
setor_sel = st.sidebar.selectbox("Setor:", ["Logística", "Indústria", "Administração", "Tecnologia"])

# 4. EXIBIÇÃO
st.subheader(f"Onde estudar em {cidade_sel}")

escolas_locais = [e for e in instituicoes_macro if e['cidade'] == cidade_sel]

if escolas_locais:
    for escola in escolas_locais:
        # O segredo está nestes 4 espaços antes do 'with'
        with st.expander(f"🏫 {escola['nome']}"):
            st.write(f"Cursos disponíveis: {', '.join(escola['cursos'])}")
            st.info(f"Foco regional em {setor_sel}")
else:
    st.write("Nenhuma escola cadastrada para esta cidade.")

# 5. GRÁFICO SIMPLES
st.divider()
dados = pd.DataFrame({'Cidade': ["Cajamar", "Caieiras", "Franco"], 'Vagas': [150, 80, 60]})
fig = px.bar(dados, x='Cidade', y='Vagas', title="Tendência Regional")
st.plotly_chart(fig)
