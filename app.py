import streamlit as st
import pandas as pd

# 1. SETUP
st.set_page_config(page_title="App Ocupações Macro", layout="wide")

# 2. BANCO DE DADOS (Vagas)
dados_lista = [
    {"cidade": "Cajamar", "local": "Jordanésia", "setor": "Logística", "vagas": 182, "cargo": "Auxiliar de Logística"},
    {"cidade": "Cajamar", "local": "Polvilho", "setor": "Comércio", "vagas": 45, "cargo": "Vendedor Lojista"},
    {"cidade": "Caieiras", "local": "Laranjeiras", "setor": "Indústria", "vagas": 64, "cargo": "Ajudante de Produção"},
    {"cidade": "Franco da Rocha", "local": "Centro", "setor": "Serviços", "vagas": 58, "cargo": "Atendente de SAC"},
    {"cidade": "Francisco Morato", "local": "Belas Águas", "setor": "Comércio", "vagas": 72, "cargo": "Operador de Caixa"}
]
df_vagas = pd.DataFrame(dados_lista)

# 3. INTERFACE INICIAL
st.title("📍 Conexão Ocupações")
st.subheader("📊 Panorama Regional (PNADC)")
c1, c2 = st.columns(2)
c1.metric("Desemprego", "8.1%", "-0.4%")
c2.metric("Renda Média", "R$ 3.240", "+1.2%")

st.divider()

# 4. FILTRO E LISTAGEM
cidade_sel = st.sidebar.selectbox("Cidade:", ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"])
st.header(f"Oportunidades em {cidade_sel}")

vagas_f = df_vagas[df_vagas['cidade'] == cidade_sel]
for _, linha in vagas_f.iterrows():
    st.info(f"💼 **{linha['cargo']}**")
    st.write(f"📍 {linha['local']} | Setor: {linha['setor']} | Vagas: {linha['vagas']}")
    st.markdown(f"[🔗 Qualificar-se para {linha['setor']}](https://www.vestibulinhoetec.com.br/)")
    st.write("---")

# 5. GRÁFICO E TABELA DE DADOS
st.subheader("📈 Evolução Mensal de Vagas")

# Dados para o gráfico e tabela
dados_grafico = pd.DataFrame({
    'Meses': ['Out', 'Nov', 'Dez', 'Jan'],
    'Vagas': [120, 150, -30, 85]
})

# Exibição do Gráfico
st.line_chart(data=dados_grafico, x='Meses', y='Vagas', color="#2ecc71")

# Exibição da Tabela Resumo
with st.expander("📄 Ver números detalhados (Tabela)"):
    st.dataframe(dados_grafico, use_container_width=True, hide_index=True)
    st.caption("Saldo líquido mensal baseado no Novo CAGED.")
