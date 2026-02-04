import streamlit as st
import pandas as pd

# 1. SETUP
st.set_page_config(page_title="App Ocupações Macro", layout="wide")

# 2. BANCO DE DADOS COMPLETO (Recuperado)
dados_lista = [
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
df_vagas = pd.DataFrame(dados_lista)

hist = pd.DataFrame({'Mês': ['Out', 'Nov', 'Dez', 'Jan'], 'Saldo': [120, 150, -30, 85]}).set_index('Mês')

# 3. INTERFACE
st.title("📍 Conexão Ocupações")

# Painel PNADC (Contexto Macro)
st.subheader("📊 Panorama Regional (PNADC)")
st.caption("📅 Ref: Out-Dez/2025 | Fonte: IBGE")
c1, c2, c3 = st.columns(3)
c1.metric("Desemprego", "8.1%", "-0.4%")
c2.metric("Renda Média", "R$ 3.240", "+1.2%")
c3.metric("Informalidade", "38.5%", "Estável")

st.divider()

# 4. FILTRO E VAGAS (CAGED)
cidade_sel = st.sidebar.selectbox("Escolha a Cidade:", ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"])

st.header(f"Vagas em {cidade_sel}")
st.caption("📅 Ref: Dezembro/2025 | Fonte: Novo CAGED")

vagas_f = df_vagas[df_vagas['cidade'] == cidade_sel]

if not vagas_f.empty:
    for _, linha in vagas_f.iterrows():
        # Usando um formato simples que não quebra no celular
        st.info(f"💼 **{linha['cargo']}**")
        st.write(f"Setor: {linha['setor']} | Saldo: {linha['vagas']} vagas")
        st.markdown(f"[🔗 Ver curso técnico](https://www.vestibulinhoetec.com.br/)")
        st.write("---")
else:
    st.warning("Dados em atualização...")

# 5. GRÁFICO (A prova de falhas)
st.subheader("📈 Evolução de Vagas na Região")
st.line_chart(hist, color="#2ecc71")
st.caption("Tendência do saldo líquido mensal (CAGED).")
