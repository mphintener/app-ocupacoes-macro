import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="App Ocupações Macro", layout="wide")

# 2. BANCO DE DADOS (Vagas + Dados PNADC de Contexto)
dados_vagas = [
    {"cidade": "Cajamar", "setor": "Logística", "vagas": 182, "cargo": "Auxiliar de Logística"},
    {"cidade": "Cajamar", "setor": "Logística", "vagas": 45, "cargo": "Operador de Empilhadeira"},
    {"cidade": "Caieiras", "setor": "Indústria", "vagas": 64, "cargo": "Ajudante de Produção"},
    {"cidade": "Franco da Rocha", "setor": "Serviços", "vagas": 58, "cargo": "Atendente de SAC"},
    {"cidade": "Francisco Morato", "setor": "Comércio", "vagas": 72, "cargo": "Operador de Caixa"}
]
df_vagas = pd.DataFrame(dados_vagas)

# 3. CABEÇALHO E TÍTULO
st.title("📍 Conexão Ocupações: Macrorregião")
st.markdown("---")

# 4. PAINEL PNADC (O "Termômetro" do Mercado)
st.subheader("📊 Panorama do Mercado (PNADC vs CAGED)")
col1, col2, col3 = st.columns(3)

# Estes números você altera manualmente a cada 3 meses via SIDRA/IBGE
col1.metric("Taxa de Desemprego", "8.1%", "-0.4%", help="Recorte Grande SP (PNADC)")
col2.metric("Renda Média", "R$ 3.240", "+1.2%", help="Rendimento médio real habitual")
col3.metric("Informalidade", "38.5%", "Estável", help="Trabalhadores sem carteira ou autônomos")

st.divider()

# 5. FILTRO LATERAL
st.sidebar.header("Configurações")
cidade_sel = st.sidebar.selectbox(
    "Selecione a Cidade:", 
    ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"]
)

# 6. EXIBIÇÃO DAS VAGAS (O "Mapa" das Oportunidades)
st.header(f"Vagas em Alta: {cidade_sel}")

vagas_filtradas = df_vagas[df_vagas['cidade'] == cidade_sel]

if not vagas_filtradas.empty:
    for _, linha in vagas_filtradas.iterrows():
        with st.expander(f"💼 {linha['cargo']}", expanded=True):
            c1, c2 = st.columns([2, 1])
            c1.write(f"**Setor:** {linha['setor']}")
            c2.metric("Vagas Abertas", linha['vagas'])
            st.markdown(f"🔗 [Ver curso técnico para {linha['setor']}](https://www.vestibulinhoetec.com.br/)")
else:
    st.info("Sem dados para esta cidade no momento.")

# 7. GRÁFICO DE TENDÊNCIA
st.markdown("---")
st.write("**Histórico de Movimentação (Últimos 4 meses)**")
dados_hist = pd.DataFrame({
    'Mês': ['Out', 'Nov', 'Dez', 'Jan'],
    'Vagas Novas': [120, 150, -30, 85]
}).set_index('Mês')
st.line_chart(dados_hist)
