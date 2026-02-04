import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO
st.set_page_config(page_title="App Ocupações Macro", layout="wide")

# 2. BANCO DE DADOS (Clusters de Trabalho)
dados_lista = [
    {"cidade": "Cajamar", "local": "Jordanésia (Polo Logístico)", "setor": "Logística", "vagas": 182, "cargo": "Auxiliar de Logística"},
    {"cidade": "Cajamar", "local": "Polvilho (Comércio/Serviços)", "setor": "Comércio", "vagas": 45, "cargo": "Vendedor Lojista"},
    {"cidade": "Caieiras", "local": "Laranjeiras (Setor Industrial)", "setor": "Indústria", "vagas": 64, "cargo": "Ajudante de Produção"},
    {"cidade": "Franco da Rocha", "local": "Centro (Polo Comercial)", "setor": "Serviços", "vagas": 58, "cargo": "Atendente de SAC"},
    {"cidade": "Francisco Morato", "local": "Belas Águas (Setor Comercial)", "setor": "Comércio", "vagas": 72, "cargo": "Operador de Caixa"}
]
df_vagas = pd.DataFrame(dados_lista)

# 3. CABEÇALHO
st.title("📍 Conexão Ocupações")
st.subheader("Macrorregião de Franco da Rocha")
st.markdown("---")

# 4. PANORAMA SOCIOECONÔMICO (PNADC/IBGE)
st.markdown("### 📊 Indicadores Regionais")
c1, c2 = st.columns(2)
c1.metric("Desemprego (Grande SP)", "8.1%", "-0.4%")
c2.metric("Renda Média Real", "R$ 3.240", "+1.2%")
st.caption("**Fonte:** PNADC/IBGE (Ref: Q4 2025).")

st.divider()

# 5. FILTRO E LISTAGEM (Onde os links foram corrigidos)
st.sidebar.header("Navegação")
cidade_sel = st.sidebar.selectbox("Escolha a Cidade:", ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"])

st.header(f"Oportunidades: {cidade_sel}")
vagas_f = df_vagas[df_vagas['cidade'] == cidade_sel]

for _, linha in vagas_f.iterrows():
    st.info(f"💼 **{linha['cargo']}**")
    st.write(f"🏢 **Unidade Produtiva:** {linha['local']}")
    st.write(f"📈 **Saldo:** {linha['vagas']} vagas (Fonte: CAGED)")
    
    # Botões de Link Blindados para Mobile
    if linha['setor'] in ['Logística', 'Indústria', 'Tecnologia', 'Administração']:
        st.link_button("🚀 Ver Cursos Técnicos (ETEC)", "https://www.vestibulinhoetec.com.br/", use_container_width=True)
    else:
        # Link do Sebrae SP - Muito mais estável para telemóvel
        st.link_button("💡 Qualificação Profissional (Sebrae)", "https://www.sebrae.com.br/sites/PortalSebrae/ufs/sp?mapa=1", use_container_width=True)
    st.write("---")

# 6. GRÁFICO (Com ordem de meses protegida)
st.subheader("📈 Evolução de Vagas na Macrorregião")

df_grafico = pd.DataFrame({
    'Mês': ['Out', 'Nov', 'Dez', 'Jan'],
    'Saldo': [120, 150, -30, 85]
})

# Forçando a ordem cronológica
df_grafico['Mês'] = pd.Categorical(df_grafico['Mês'], categories=['Out', 'Nov', 'Dez', 'Jan'], ordered=True)
df_grafico = df_grafico.sort_values('Mês')

st.line_chart(data=df_grafico, x='Mês', y='Saldo', color="#2ecc71")

with st.expander("ℹ️ Notas Metodológicas"):
    st.write("Dados consolidados das unidades produtivas locais via Novo CAGED.")
    st.dataframe(df_grafico, hide_index=True, use_container_width=True)
