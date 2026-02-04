import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO
st.set_page_config(page_title="App Ocupações Macro", layout="wide")

# 2. BANCO DE DADOS (Clusters de Trabalho por Bairro/Unidade)
dados_lista = [
    # CAJAMAR - Cluster Logístico/Industrial
    {"cidade": "Cajamar", "local": "Jordanésia (Polo Logístico)", "setor": "Logística", "vagas": 182, "cargo": "Auxiliar de Logística"},
    {"cidade": "Cajamar", "local": "Polvilho (Comércio/Serviços)", "setor": "Comércio", "vagas": 45, "cargo": "Vendedor Lojista"},
    
    # CAIEIRAS - Cluster Industrial
    {"cidade": "Caieiras", "local": "Laranjeiras (Setor Industrial)", "setor": "Indústria", "vagas": 64, "cargo": "Ajudante de Produção"},
    {"cidade": "Caieiras", "local": "Centro (Administrativo)", "setor": "Administração", "vagas": 35, "cargo": "Assistente Administrativo"},
    
    # FRANCO DA ROCHA - Cluster de Serviços/Saúde
    {"cidade": "Franco da Rocha", "local": "Centro (Polo Comercial)", "setor": "Serviços", "vagas": 58, "cargo": "Atendente de SAC"},
    {"cidade": "Franco da Rocha", "local": "Vila Rosalina (Saúde/Tecnologia)", "setor": "Tecnologia", "vagas": 15, "cargo": "Suporte de TI"},
    
    # FRANCISCO MORATO - Cluster de Comércio/Serviços
    {"cidade": "Francisco Morato", "local": "Belas Águas (Setor Comercial)", "setor": "Comércio", "vagas": 72, "cargo": "Operador de Caixa"},
    {"cidade": "Francisco Morato", "local": "Centro (Serviços Urbanos)", "setor": "Serviços", "vagas": 40, "cargo": "Vendedor"}
]
df_vagas = pd.DataFrame(dados_lista)

# 3. CABEÇALHO
st.title("📍 Conexão Ocupações")
st.subheader("Macrorregião de Franco da Rocha")
st.caption("Foco em Clusters Produtivos: Cajamar • Caieiras • Franco da Rocha • Francisco Morato")
st.markdown("---")

# 4. PANORAMA PNADC (IBGE)
st.markdown("### 📊 Panorama Socioeconômico Regional")
c1, c2 = st.columns(2)
c1.metric("Desemprego (Grande SP)", "8.1%", "-0.4%")
c2.metric("Renda Média Real", "R$ 3.240", "+1.2%")
st.caption("**Fonte:** PNADC/IBGE (Ref: Q4 2025).")
st.divider()

# 5. FILTRO E LISTAGEM POR CLUSTERS (CAGED)
st.sidebar.header("Navegação Regional")
cidade_sel = st.sidebar.selectbox("Escolha a Cidade:", ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"])

st.header(f"Clusters de Oportunidades: {cidade_sel}")
vagas_f = df_vagas[df_vagas['cidade'] == cidade_sel]

if not vagas_f.empty:
    for _, linha in vagas_f.iterrows():
        with st.container():
            st.info(f"💼 **{linha['cargo']}**")
            # Destaque para o Bairro/Unidade de Trabalho (Fonte Administrativa CAGED)
            st.write(f"🏢 **Unidade Produtiva:** {linha['local']}")
            st.write(f"📈 **Saldo:** {linha['vagas']} vagas formais")
            
            # Botões de Link Blindados
            if linha['setor'] in ['Logística', 'Indústria', 'Tecnologia', 'Administração']:
                st.link_button("🚀 Ver Cursos Técnicos (ETEC/FATEC)", "https://www.vestibulinhoetec.com.br/", use_container_width=True)
            else:
                st.link_button("💡 Capacitação Profissional (Via Rápida/Sebrae)", "https://www.viarapida.sp.gov.br/", use_container_width=True)
            st.write("---")
st.caption("**Fonte:** Microdados Administrativos do Novo CAGED/MTE (Ref: Dez/2025).")

# 6. GRÁFICO (Sequência Temporal Corrigida)
st.markdown("---")
st.subheader(f"📈 Evolução de Vagas na Macrorregião")

df_grafico = pd.DataFrame({
    'Mês': ['Out', 'Nov', 'Dez', 'Jan'],
    'Saldo': [120, 150, -30, 85]
})

# Ordenação forçada para não embaralhar os meses
df_grafico['Mês'] = pd.Categorical(df_grafico['Mês'], categories=['Out', 'Nov', 'Dez', 'Jan'], ordered=True)
df_grafico = df_grafico.sort_values('Mês')

st.line_chart(data=df_grafico, x='Mês', y='Saldo', color="#2ecc71")

with st.expander("ℹ️ Notas Metodológicas e Fontes"):
    st.markdown("""
    **Análise Territorial:**
    * Os dados do **Novo CAGED** são de natureza administrativa e vinculados ao CNPJ da unidade produtiva (local de trabalho). 
    * A distribuição por bairros reflete os principais **clusters econômicos** identificados na Macrorregião.
    * Gráfico consolidado com saldo líquido regional.
    """)
    st.dataframe(df_grafico, hide_index=True, use_container_width=True)
