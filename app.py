import streamlit as st
import pandas as pd

# 1. SETUP
st.set_page_config(page_title="App Ocupações", layout="wide")

# 2. DADOS (Tudo numa estrutura simples para evitar erros)
dados = pd.DataFrame([
    {"cidade": "Cajamar", "vagas": 182, "cargo": "Auxiliar de Logística"},
    {"cidade": "Caieiras", "vagas": 64, "cargo": "Ajudante de Produção"},
    {"cidade": "Franco da Rocha", "vagas": 58, "cargo": "Atendente de SAC"},
    {"cidade": "Francisco Morato", "vagas": 72, "cargo": "Operador de Caixa"}
])

hist = pd.DataFrame({'Mês': ['Nov', 'Dez', 'Jan'], 'Saldo': [150, -30, 85]}).set_index('Mês')

# 3. INTERFACE
st.title("📍 Conexão Ocupações")

# Painel PNADC (Simples)
st.subheader("📊 Panorama Regional (PNADC)")
c1, c2 = st.columns(2)
c1.metric("Desemprego", "8.1%", "Out-Dez/25")
c2.metric("Renda Média", "R$ 3.240", "IBGE")

st.divider()

# Filtro e Vagas
cidade_sel = st.sidebar.selectbox("Cidade:", ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"])

st.header(f"Vagas: {cidade_sel}")
vagas_f = dados[dados['cidade'] == cidade_sel]

for _, linha in vagas_f.iterrows():
    st.info(f"💼 **{linha['cargo']}** | Vagas: {linha['vagas']}")
    st.write("---")

# Gráfico (A prova de falhas)
st.subheader("📈 Evolução de Vagas (CAGED)")
st.line_chart(hist, color="#2ecc71")

