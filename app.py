import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="App Ocupações Macro", layout="wide")

# 2. BANCO DE DADOS (Vagas + Dados PNADC)
dados_vagas = [
    {"cidade": "Cajamar", "setor": "Logística", "vagas": 182, "cargo": "Auxiliar de Logística"},
    {"cidade": "Cajamar", "setor": "Logística", "vagas": 45, "cargo": "Operador de Empilhadeira"},
    {"cidade": "Caieiras", "setor": "Indústria", "vagas": 64, "cargo": "Ajudante de Produção"},
    {"cidade": "Franco da Rocha", "setor": "Serviços", "vagas": 58, "cargo": "Atendente de SAC"},
    {"cidade": "Francisco Morato", "setor": "Comércio", "vagas": 72, "cargo": "Operador de Caixa"}
]
df_vagas = pd.DataFrame(dados_vagas)

# 3. CABEÇALHO
st.title("📍 Conexão Ocupações: Macrorregião")
st.caption("Análise integrada de empregabilidade e indicadores socioeconômicos")
st.markdown("---")

# 4. PAINEL PNADC (Indicadores de Contexto)
st.subheader("📊 Panorama do Mercado (PNADC Contínua)")
# NOTA: PNADC costuma ser trimestral
st.info("📅 **Período de Referência:** Trimestre Móvel (Out/Nov/Dez 2025)")

col1, col2, col3 = st.columns(3)
col1.metric("Taxa de Desocupação", "8.1%", "-0.4%", help="Dados IBGE para a Região Metropolitana de SP")
col2.metric("Renda Média", "R$ 3.240", "+1.2%", help="Rendimento médio real habitual")
col3.metric("Informalidade", "38.5%", "Estável", help="Trabalhadores sem carteira ou autônomos")

st.divider()

# 5. FILTRO LATERAL
st.sidebar.header("Configurações")
cidade_sel = st.sidebar.selectbox(
    "Selecione a Cidade:", 
    ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"]
)

# 6. EXIBIÇÃO DAS VAGAS (Dados CAGED)
st.header(f"Vagas em Alta: {cidade_sel}")
st.write("📅 **Base de Dados:** Novo CAGED (Dezembro/2025)")

vagas_filtradas = df_vagas[df_vagas['cidade'] == cidade_sel]

if not vagas_filtradas.empty:
    for _, linha in vagas_filtradas.iterrows():
        with st.expander(f"💼 {linha['cargo']}", expanded=True):
            c1, c2 = st.columns([2, 1])
            c1.write(f"**Setor:** {linha['setor']}")
            c2.metric("Saldo de Vagas", linha['vagas'])
            st.markdown(f"🔗 [Ver curso técnico para {linha['setor']}](https://www.vestibulinhoetec.com.br/)")
else:
    st.info("Sem dados para esta cidade no momento.")

# 7. RODAPÉ TÉCNICO
st.markdown("---")
st.caption("""
**Fontes:** - Microdados do Novo CAGED (Ministério do Trabalho e Emprego) 
- Pesquisa Nacional por Amostra de Domicílios Contínua - PNADC (IBGE)
- Processamento: Python/Streamlit
""")
