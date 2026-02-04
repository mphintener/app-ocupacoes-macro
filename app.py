import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="App Ocupações Macro", layout="wide")

# CSS PARA DIMINUIR O TAMANHO DAS FONTES DOS INDICADORES (METRICS)
st.markdown("""
    <style>
    [data-testid="stMetricValue"] {
        font-size: 22px !important;
    }
    [data-testid="stMetricLabel"] {
        font-size: 14px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. BANCO DE DADOS
dados_lista = [
    {"cidade": "Cajamar", "local": "Jordanésia (Polo Logístico)", "setor": "Logística", "vagas": 182, "cargo": "Auxiliar de Logística", "salario": 1850.00},
    {"cidade": "Cajamar", "local": "Polvilho (Comércio)", "setor": "Comércio", "vagas": 45, "cargo": "Vendedor Lojista", "salario": 1720.00},
    {"cidade": "Caieiras", "local": "Laranjeiras (Indústria)", "setor": "Indústria", "vagas": 64, "cargo": "Ajudante de Produção", "salario": 1980.00},
    {"cidade": "Franco da Rocha", "local": "Centro (Polo Comercial)", "setor": "Serviços", "vagas": 58, "cargo": "Atendente de SAC", "salario": 1650.00},
    {"cidade": "Francisco Morato", "local": "Belas Águas (Comércio)", "setor": "Comércio", "vagas": 72, "cargo": "Operador de Caixa", "salario": 1680.00}
]
df_vagas = pd.DataFrame(dados_lista)

# 3. CABEÇALHO
st.title("📍 Conexão Ocupações")
st.subheader("Macrorregião de Franco da Rocha")
st.markdown("---")

# 4. PANORAMA REGIONAL (Indicadores com fonte reduzida via CSS)
st.markdown("### 📊 Panorama Socioeconômico Regional")
c1, c2 = st.columns(2)
c1.metric("Desemprego (Grande SP)", "8.1%", "-0.4%")
c2.metric("Renda Média PNADC", "R$ 3.240", "Referência")
st.caption("**Fonte:** PNADC/IBGE (Ref: Q4 2025).")
st.divider()

# 5. BUSCA CENTRALIZADA
st.markdown("### 🔍 Onde você quer trabalhar?")
cidade_sel = st.selectbox(
    "Selecione sua cidade para filtrar as oportunidades:",
    ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"]
)

st.markdown(f"## Oportunidades em {cidade_sel}")
vagas_f = df_vagas[df_vagas['cidade'] == cidade_sel]

# 6. LISTAGEM COM SALÁRIO CORRIGIDO (MESMO ESTILO DOS INDICADORES ACIMA)
for _, linha in vagas_f.iterrows():
    with st.container():
        st.subheader(f"💼 {linha['cargo']}")
        
        # O Salário agora usa o mesmo st.metric, mas com a fonte reduzida pelo CSS no topo
        st.metric(label="Salário Admissional Médio (CAGED)", value=f"R$ {linha['salario']:.2f}")
        
        st.write(f"🏢 **Unidade Produtiva/Cluster:** {linha['local']}")
        st.write(f"📈 **Saldo de Vagas:** {linha['vagas']} | **Setor:** {linha['setor']}")

        if linha['setor'] in ['Logística', 'Indústria', 'Tecnologia', 'Administração']:
            st.link_button("🚀 Ver Cursos Técnicos (ETEC)", "https://www.vestibulinhoetec.com.br/", use_container_width=True)
        else:
            st.link_button("💡 Qualificação Profissional (Sebrae)", "https://www.sebrae.com.br/sites/PortalSebrae/ufs/sp?mapa=1", use_container_width=True)
        st.write("---")

# 7. GRÁFICO, TABELA E NOTAS
st.subheader("📈 Evolução de Vagas na Macrorregião")
df_grafico = pd.DataFrame({'Mês': ['Out', 'Nov', 'Dez', 'Jan'], 'Saldo': [120, 150, -30, 85]})
df_grafico['Mês'] = pd.Categorical(df_grafico['Mês'], categories=['Out', 'Nov', 'Dez', 'Jan'], ordered=True)
st.line_chart(data=df_grafico.sort_values('Mês'), x='Mês', y='Saldo', color="#2ecc71")

with st.expander("📄 Notas Metodológicas e Dados Detalhados"):
    st.markdown("""
    **Fontes e Metodologia:**
    * **Novo CAGED:** Dados administrativos de admissões/desligamentos.
    * **PNADC:** Renda média de todos os trabalhadores da região.
    * **Salário Admissional:** Média contratual no ato da admissão.
    """)
    st.dataframe(df_grafico, hide_index=True, use_container_width=True)
