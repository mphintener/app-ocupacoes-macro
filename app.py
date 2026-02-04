import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="App Ocupações Macro", layout="wide")

# 2. BANCO DE DADOS (Vagas + Histórico para o Gráfico)
dados_vagas = [
    {"cidade": "Cajamar", "setor": "Logística", "vagas": 182, "cargo": "Auxiliar de Logística"},
    {"cidade": "Cajamar", "setor": "Logística", "vagas": 45, "cargo": "Operador de Empilhadeira"},
    {"cidade": "Caieiras", "setor": "Indústria", "vagas": 64, "cargo": "Ajudante de Produção"},
    {"cidade": "Franco da Rocha", "setor": "Serviços", "vagas": 58, "cargo": "Atendente de SAC"},
    {"cidade": "Francisco Morato", "setor": "Comércio", "vagas": 72, "cargo": "Operador de Caixa"}
]
df_vagas = pd.DataFrame(dados_vagas)

# Dados para o Gráfico que tinha sumido
dados_historicos = pd.DataFrame({
    'Mês': ['Set', 'Out', 'Nov', 'Dez', 'Jan'],
    'Saldo de Vagas': [95, 120, 150, -30, 85]
}).set_index('Mês')

# 3. CABEÇALHO
st.title("📍 Conexão Ocupações: Macrorregião")
st.markdown("---")

# 4. PAINEL PNADC (Contexto Macro)
st.subheader("📊 Panorama do Mercado (PNADC Contínua)")
st.caption("📅 Referência: Trimestre Móvel (Out-Dez 2025) | Fonte: IBGE")

col1, col2, col3 = st.columns(3)
col1.metric("Taxa de Desocupação", "8.1%", "-0.4%")
col2.metric("Renda Média", "R$ 3.240", "+1.2%")
col3.metric("Informalidade", "38.5%", "Estável")

st.divider()

# 5. FILTRO E VAGAS (CAGED)
cidade_sel = st.sidebar.selectbox(
    "Selecione a Cidade:", 
    ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"]
)

st.header(f"Vagas em Alta: {cidade_sel}")
st.caption("📅 Referência: Novo CAGED (Dezembro 2025) | Fonte: MTE")

vagas_filtradas = df_vagas[df_vagas['cidade'] == cidade_sel]

if not vagas_filtradas.empty:
    for _, linha in vagas_filtradas.iterrows():
        with st.expander(f"💼 {linha['cargo']}", expanded=True):
            st.write(f"**Setor:** {linha['setor']} | **Vagas:** {linha['vagas']}")
            st.markdown(f"🔗 [Ver curso técnico](https://www.vestibulinhoetec.com.br/)")
else:
    st.info("A carregar dados locais...")

import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="App Ocupações Macro", layout="wide")

# 2. BANCO DE DADOS
dados_vagas = [
    {"cidade": "Cajamar", "setor": "Logística", "vagas": 182, "cargo": "Auxiliar de Logística"},
    {"cidade": "Cajamar", "setor": "Logística", "vagas": 45, "cargo": "Operador de Empilhadeira"},
    {"cidade": "Caieiras", "setor": "Indústria", "vagas": 64, "cargo": "Ajudante de Produção"},
    {"cidade": "Franco da Rocha", "setor": "Serviços", "vagas": 58, "cargo": "Atendente de SAC"},
    {"cidade": "Francisco Morato", "setor": "Comércio", "vagas": 72, "cargo": "Operador de Caixa"}
]
df_vagas = pd.DataFrame(dados_vagas)

# Dados Históricos com Cor Customizada
dados_historicos = pd.DataFrame({
    'Mês': ['Set', 'Out', 'Nov', 'Dez', 'Jan'],
    'Saldo': [95, 120, 150, -30, 85]
}).set_index('Mês')

# 3. CABEÇALHO
st.title("📍 Conexão Ocupações: Macrorregião")
st.markdown("---")

# 4. PAINEL PNADC
st.subheader("📊 Panorama do Mercado (PNADC Contínua)")
st.caption("📅 Referência: Trimestre Móvel (Out-Dez 2025) | Fonte: IBGE")

col1, col2, col3 = st.columns(3)
col1.metric("Taxa de Desocupação", "8.1%", "-0.4%")
col2.metric("Renda Média", "R$ 3.240", "+1.2%")
col3.metric("Informalidade", "38.5%", "Estável")

st.divider()

# 5. FILTRO E VAGAS (CAGED)
cidade_sel = st.sidebar.selectbox(
    "Selecione a Cidade:", 
    ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"]
)

st.header(f"Vagas em Alta: {cidade_sel}")
st.caption("📅 Referência: Novo CAGED (Dezembro 2025) | Fonte: MTE")

vagas_filtradas = df_vagas[df_vagas['cidade'] == cidade_sel]

if not vagas_filtradas.empty:
    for _, linha in vagas_filtradas.iterrows():
        with st.expander(f"💼 {linha['cargo']}", expanded=True):
            st.write(f"**Setor:** {linha['setor']} | **Vagas:** {linha['vagas']}")
            st.markdown(f"🔗 [Ver curso técnico](https://www.vestibulinhoetec.com.br/)")
else:
    st.info("A carregar dados locais...")

# 6. GRÁFICOS COM CORES CUSTOMIZADAS
st.markdown("---")
st.subheader("📈 Evolução Mensal de Contratações")

# Usando o parâmetro 'color' para destacar a linha (Verde Sucesso)
st.line_chart(dados_historicos, color="#2ecc71") 

st.caption("Gráfico de tendência baseado no saldo líquido mensal da Macrorregião (Novo CAGED).")

# 7. RODAPÉ FINAL
st.markdown("---")
st.caption("Desenvolvido para análise regional de emprego e renda.")

