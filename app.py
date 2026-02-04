import streamlit as st
import pandas as pd

# 1. BANCO DE DADOS INTEGRADO (Todas as cidades da Macrorregião)
# Certifique-se de que os nomes aqui são IDÊNTICOS aos do selectbox abaixo
dados_vagas = [
    {"cidade": "Cajamar", "setor": "Logística", "vagas": 182, "cargo": "Auxiliar de Logística"},
    {"cidade": "Cajamar", "setor": "Logística", "vagas": 45, "cargo": "Operador de Empilhadeira"},
    {"cidade": "Cajamar", "setor": "Transporte", "vagas": 28, "cargo": "Motorista (Cat. D/E)"},
    
    {"cidade": "Caieiras", "setor": "Indústria", "vagas": 64, "cargo": "Ajudante de Produção"},
    {"cidade": "Caieiras", "setor": "Indústria", "vagas": 12, "cargo": "Técnico em Manutenção"},
    {"cidade": "Caieiras", "setor": "Administração", "vagas": 35, "cargo": "Assistente Administrativo"},
    
    {"cidade": "Franco da Rocha", "setor": "Serviços", "vagas": 58, "cargo": "Atendente de SAC"},
    {"cidade": "Franco da Rocha", "setor": "Saúde", "vagas": 22, "cargo": "Técnico de Enfermagem"},
    {"cidade": "Franco da Rocha", "setor": "Tecnologia", "vagas": 15, "cargo": "Suporte de TI"},
    
    {"cidade": "Francisco Morato", "setor": "Comércio", "vagas": 72, "cargo": "Operador de Caixa"},
    {"cidade": "Francisco Morato", "setor": "Comércio", "vagas": 40, "cargo": "Vendedor Lojista"},
    {"cidade": "Francisco Morato", "setor": "Educação", "vagas": 18, "cargo": "Auxiliar Escolar"}
]

df_vagas = pd.DataFrame(dados_vagas)

# 2. INTERFACE E CONFIGURAÇÃO
st.set_page_config(page_title="App Ocupações Regional", layout="wide")
st.title("📍 Conexão Ocupações")
st.markdown("---")

# 3. FILTROS (Menu Lateral)
st.sidebar.header("Filtros")
cidade_sel = st.sidebar.selectbox(
    "Selecione a Cidade:", 
    ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"]
)

# 4. EXIBIÇÃO DAS VAGAS
st.header(f"Oportunidades em {cidade_sel}")

# Lógica de match exato (ajustada para não falhar)
vagas_filtradas = df_vagas[df_vagas['cidade'] == cidade_sel]

if not vagas_filtradas.empty:
    for _, linha in vagas_filtradas.iterrows():
        with st.expander(f"💼 {linha['cargo']}", expanded=True):
            col1, col2 = st.columns([2,1])
            col1.write(f"**Setor:** {linha['setor']}")
            col2.metric("Saldo de Vagas", linha['vagas'])
            
            # Botão de ação para curso técnico
            st.markdown(f"🔗 [Qualificar-se para {linha['setor']}](https://www.vestibulinhoetec.com.br/)")
else:
    st.error("Dados não encontrados para esta seleção.")

# 5. RODAPÉ INFORMATIVO
st.sidebar.markdown("---")
st.sidebar.caption("Dados baseados em estimativas regionais do Novo CAGED para a Macrorregião de Franco da Rocha.")
