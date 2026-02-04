import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO BÁSICA
st.set_page_config(page_title="App Ocupações", layout="wide")

# 2. DADOS (Escritos de forma ultra-simples)
dados_vagas = [
    {"cidade": "Cajamar", "vagas": 182, "cargo": "Auxiliar de Logística", "setor": "Logística"},
    {"cidade": "Cajamar", "vagas": 45, "cargo": "Operador de Empilhadeira", "setor": "Logística"},
    {"cidade": "Cajamar", "vagas": 28, "cargo": "Motorista (Cat. D/E)", "setor": "Transporte"},
    {"cidade": "Caieiras", "vagas": 64, "cargo": "Ajudante de Produção", "setor": "Indústria"},
    {"cidade": "Caieiras", "vagas": 12, "cargo": "Técnico em Manutenção", "setor": "Indústria"},
    {"cidade": "Caieiras", "vagas": 35, "cargo": "Assistente Administrativo", "setor": "Administração"},
    {"cidade": "Franco da Rocha", "vagas": 58, "cargo": "Atendente de SAC", "setor": "Serviços"},
    {"cidade": "Franco da Rocha", "vagas": 22, "cargo": "Técnico de Enfermagem", "setor": "Saúde"},
    {"cidade": "Francisco Morato", "vagas": 72, "cargo": "Operador de Caixa", "setor": "Comércio"},
    {"cidade": "Francisco Morato", "vagas": 40, "cargo": "Vendedor Lojista", "setor": "Comércio"}
]
df = pd.DataFrame(dados_vagas)

# 3. INTERFACE
st.title("📍 Conexão Ocupações")

# Painel PNADC (Top)
st.subheader("📊 Panorama Regional (PNADC)")
st.caption("Ref: Out-Dez/2025 | Fonte: IBGE")
c1, c2 = st.columns(2)
c1.metric("Desemprego", "8.1%", "-0.4%")
c2.metric("Renda Média", "R$ 3.240", "+1.2%")

st.divider()

# 4. FILTRO (Menu Lateral)
cidade_sel = st.sidebar.selectbox("Escolha a Cidade:", ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"])

# 5. EXIBIÇÃO DAS VAGAS (Lógica simplificada)
st.header(f"Vagas em {cidade_sel}")

# Aqui filtramos de forma direta e simples
vagas_f = df[df['cidade'] == cidade_sel]

if len(vagas_f) > 0:
    for i, linha in vagas_f.iterrows():
        st.info(f"💼 **{linha['cargo']}**")
        st.write(f"Setor: {linha['setor']} | Saldo: {linha['vagas']} vagas")
        st.write("---")
else:
    st.error("Erro: Não encontramos vagas para esta seleção. Verifique os nomes.")

# 6. GRÁFICO (Sempre visível no fim)
st.subheader("📈 Evolução de Vagas")
hist = pd.DataFrame({'Saldo': [120, 150, -30, 85]}, index=['Out', 'Nov', 'Dez', 'Jan'])
st.line_chart(hist, color="#2ecc71")
