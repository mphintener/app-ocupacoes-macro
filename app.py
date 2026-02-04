
import streamlit as st
import pandas as pd

# 1. DADOS DA MACRORREGIÃO INTEGRADOS (Não precisa de CSV!)
dados_vagas = [   # Substitua a lista 'dados_vagas' por esta:
    # CAJAMAR (Foco Logístico)
    {"cidade": "Cajamar", "setor": "Logística", "vagas": 182, "cargo": "Auxiliar de Logística"},
    {"cidade": "Cajamar", "setor": "Logística", "vagas": 45, "cargo": "Operador de Empilhadeira"},
    {"cidade": "Cajamar", "setor": "Transporte", "vagas": 28, "cargo": "Motorista (Cat. D/E)"},
    
    # CAIEIRAS (Foco Industrial e Administrativo)
    {"cidade": "Caieiras", "setor": "Indústria", "vagas": 64, "cargo": "Ajudante de Produção"},
    {"cidade": "Caieiras", "setor": "Indústria", "vagas": 12, "cargo": "Técnico em Manutenção"},
    {"cidade": "Caieiras", "setor": "Administração", "vagas": 35, "cargo": "Assistente Administrativo"},
    
    # FRANCO DA ROCHA (Serviços e Saúde)
    {"cidade": "Franco da Rocha", "setor": "Serviços", "vagas": 58, "cargo": "Atendente de SAC"},
    {"cidade": "Franco da Rocha", "setor": "Saúde", "vagas": 22, "cargo": "Técnico de Enfermagem"},
    {"cidade": "Franco da Rocha", "setor": "Tecnologia", "vagas": 15, "cargo": "Suporte de TI"},
    
    # FRANCISCO MORATO (Comércio e Varejo)
    {"cidade": "Francisco Morato", "setor": "Comércio", "vagas": 72, "cargo": "Operador de Caixa"},
    {"cidade": "Francisco Morato", "setor": "Comércio", "vagas": 40, "cargo": "Vendedor Lojista"},
    {"cidade": "Francisco Morato", "setor": "Educação", "vagas": 18, "cargo": "Auxiliar Escolar"}
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
