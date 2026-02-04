import streamlit as st
import pandas as pd

# 1. SETUP
st.set_page_config(page_title="App Ocupações Macro", layout="wide")

# 2. BANCO DE DADOS DETALHADO (Cidades, Bairros e Setores)
dados_lista = [
    # CAJAMAR
    {"cidade": "Cajamar", "local": "Jordanésia (Polo Logístico)", "setor": "Logística", "vagas": 182, "cargo": "Auxiliar de Logística"},
    {"cidade": "Cajamar", "local": "Polvilho", "setor": "Comércio", "vagas": 45, "cargo": "Vendedor Lojista"},
    {"cidade": "Cajamar", "local": "Distrito Industrial", "setor": "Transporte", "vagas": 28, "cargo": "Motorista (Cat. D/E)"},
    
    # CAIEIRAS
    {"cidade": "Caieiras", "local": "Laranjeiras", "setor": "Indústria", "vagas": 64, "cargo": "Ajudante de Produção"},
    {"cidade": "Caieiras", "local": "Centro", "setor": "Administração", "vagas": 35, "cargo": "Assistente Administrativo"},
    {"cidade": "Caieiras", "local": "Melhoramentos", "setor": "Indústria", "vagas": 12, "cargo": "Técnico em Manutenção"},
    
    # FRANCO DA ROCHA
    {"cidade": "Franco da Rocha", "local": "Centro (Comércio)", "setor": "Serviços", "vagas": 58, "cargo": "Atendente de SAC"},
    {"cidade": "Franco da Rocha", "local": "Pq. Munhoz", "setor": "Saúde", "vagas": 22, "cargo": "Técnico de Enfermagem"},
    {"cidade": "Franco da Rocha", "local": "Vila Rosalina", "setor": "Tecnologia", "vagas": 15, "cargo": "Suporte de TI"},
    
    # FRANCISCO MORATO
    {"cidade": "Francisco Morato", "local": "Belas Águas", "setor": "Comércio", "vagas": 72, "cargo": "Operador de Caixa"},
    {"cidade": "Francisco Morato", "local": "Jd. Alegria", "setor": "Educação", "vagas": 18, "cargo": "Auxiliar Escolar"},
    {"cidade": "Francisco Morato", "local": "Centro", "setor": "Serviços", "vagas": 40, "cargo": "Vendedor"}
]
df_vagas = pd.DataFrame(dados_lista)

# 3. INTERFACE
st.title("📍 Conexão Ocupações: Macrorregião")
st.markdown("---")

# Painel PNADC (Contexto Macro)
st.subheader("📊 Panorama Regional (PNADC)")
st.caption("📅 Ref: Out-Dez/2025 | Fonte: IBGE")
c1, c2, c3 = st.columns(3)
c1.metric("Desemprego", "8.1%", "-0.4%")
c2.metric("Renda Média", "R$ 3.240", "+1.2%")
c3.metric("Informalidade", "38.5%", "Estável")

st.divider()

# 4. FILTRO LATERAL
cidade_sel = st.sidebar.selectbox("Selecione a Cidade:", ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"])

# 5. EXIBIÇÃO DAS VAGAS COM BAIRRO E QUALIFICAÇÃO
st.header(f"Oportunidades em {cidade_sel}")
st.caption("📅 Ref: Novo CAGED (Dezembro/2025)")

vagas_f = df_vagas[df_vagas['cidade'] == cidade_sel]

if not vagas_f.empty:
    for _, linha in vagas_f.iterrows():
        with st.container():
            st.info(f"💼 **{linha['cargo']}**")
            # Concatenação de Bairro e Unidade
            st.write(f"📍 **Localização:** {linha['local']}")
            st.write(f"🏢 **Setor:** {linha['setor']} | 📈 **Vagas:** {linha['vagas']}")
            
            # Link de Qualificação recuperado
            st.markdown(f"🔗 [**Qualificar-se para {linha['setor']} (ETEC/FATEC)**](https://www.vestibulinhoetec.com.br/)")
            st.write("---")
else:
    st.warning("Selecione uma cidade para carregar os dados.")

# 6. GRÁFICO DE TENDÊNCIA (Versão Blindada)
st.markdown("---")
st.subheader("📈 Evolução Mensal de Vagas")

# Criando os dados de forma que o Streamlit não tenha dúvidas
dados_grafico = pd.DataFrame({
    'Meses': ['Out', 'Nov', 'Dez', 'Jan'],
    'Vagas': [120, 150, -30, 85]
})

# Forçamos o gráfico a usar a coluna 'Meses' no eixo X
st.line_chart(data=dados_grafico, x='Meses', y='Vagas', color="#2ecc71")

st.caption("Tendência do saldo líquido mensal na Macrorregião (Fonte: Novo CAGED).")

