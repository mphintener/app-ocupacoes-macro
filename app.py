
import streamlit as st
import pandas as pd

# 1. DADOS DA MACRORREGIÃO INTEGRADOS (Não precisa de CSV!)
dados_vagas = [
    {"cidade": "Cajamar", "setor": "Logística", "vagas": 145, "cargo": "Auxiliar Logístico"},
    {"cidade": "Cajamar", "setor": "Logística", "vagas": 30, "cargo": "Op. Empilhadeira"},
    {"cidade": "Caieiras", "setor": "Indústria", "vagas": 52, "cargo": "Ajudante de Produção"},
    {"cidade": "Franco da Rocha", "setor": "Serviços", "vagas": 40, "cargo": "Atendente"},
    {"cidade": "Francisco Morato", "setor": "Comércio", "vagas": 25, "cargo": "Vendedor"}
]
df_vagas = pd.DataFrame(dados_vagas)

# 2. INTERFACE DO APP
st.set_page_config(page_title="App Ocupações Macro", layout="wide")
st.title("📍 Conexão Ocupações Regional")

# 3. FILTROS
cidade_sel = st.sidebar.selectbox("Sua Cidade:", ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"])

# 4. EXIBIÇÃO DE VAGAS REAIS
st.header(f"Oportunidades em {cidade_sel}")

vagas_filtradas = df_vagas[df_vagas['cidade'] == cidade_sel]

if not vagas_filtradas.empty:
    for _, linha in vagas_filtradas.iterrows():
        with st.container():
            col1, col2 = st.columns([3, 1])
            col1.write(f"**{linha['cargo']}** ({linha['setor']})")
            col2.subheader(f"🔥 {linha['vagas']}")
            st.divider()
else:
    st.info("Buscando novas atualizações do CAGED para esta cidade...")

# 5. DICA DE QUALIFICAÇÃO
st.sidebar.info(f"Dica: Procure a ETEC de {cidade_sel} para cursos em {vagas_filtradas['setor'].iloc[0] if not vagas_filtradas.empty else 'Logística'}.")
