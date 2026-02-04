import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="App Ocupações Macro", layout="wide")

# 2. BANCO DE DADOS (Clusters de Trabalho e Salários)
dados_lista = [
    {"cidade": "Cajamar", "local": "Jordanésia (Polo Logístico)", "setor": "Logística", "vagas": 182, "cargo": "Auxiliar de Logística", "salario": 1850.00},
    {"cidade": "Cajamar", "local": "Polvilho (Comércio)", "setor": "Comércio", "vagas": 45, "cargo": "Vendedor Lojista", "salario": 1720.00},
    {"cidade": "Caieiras", "local": "Laranjeiras (Indústria)", "setor": "Indústria", "vagas": 64, "cargo": "Ajudante de Produção", "salario": 1980.00},
    {"cidade": "Franco da Rocha", "local": "Centro (Polo Comercial)", "setor": "Serviços", "vagas": 58, "cargo": "Atendente de SAC", "salario": 1650.00},
    {"cidade": "Francisco Morato", "local": "Belas Águas (Comércio)", "setor": "Comércio", "vagas": 72, "cargo": "Operador de Caixa", "salario": 1680.00}
]
df_vagas = pd.DataFrame(dados_lista)

# 3. CABEÇALHO E IDENTIDADE REGIONAL
st.title("📍 Conexão Ocupações")
st.subheader("Macrorregião de Franco da Rocha")
st.caption("Cajamar • Caieiras • Franco da Rocha • Francisco Morato")
st.markdown("---")

# 4. PANORAMA REGIONAL (Destaque Principal)
st.markdown("### 📊 Panorama Socioeconômico Regional")
c1, c2 = st.columns(2)
c1.metric("Desemprego (Grande SP)", "8.1%", "-0.4%")
c2.metric("Renda Média PNADC", "R$ 3.240", "Referência")
st.caption("**Fonte:** PNADC/IBGE - Pesquisa Nacional por Amostra de Domicílios Contínua (Ref: Q4 2025).")
st.divider()

# 5. BUSCA CENTRALIZADA (Melhor UX para o Cidadão)
st.markdown("### 🔍 Onde você quer trabalhar?")
cidade_sel = st.selectbox(
    "Selecione sua cidade para filtrar as oportunidades:",
    ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"]
)

st.markdown(f"## Oportunidades em {cidade_sel}")
vagas_f = df_vagas[df_vagas['cidade'] == cidade_sel]

# 6. LISTAGEM COM SALÁRIO PADRONIZADO E FONTES
for _, linha in vagas_f.iterrows():
    with st.container():
        st.subheader(f"💼 {linha['cargo']}")
        
        # VISUAL DO SALÁRIO: Padronizado com os indicadores do topo
        st.metric(label="Salário Admissional Médio", value=f"R$ {linha['salario']:.2f}")
        
        st.write(f"🏢 **Unidade Produtiva/Cluster:** {linha['local']}")
        st.write(f"📈 **Saldo de Vagas:** {linha['vagas']} | **Setor:** {linha['setor']}")

        # Botões de Qualificação com Links Reais
        if linha['setor'] in ['Logística', 'Indústria', 'Tecnologia', 'Administração']:
            st.link_button("🚀 Ver Cursos Técnicos (ETEC)", "https://www.vestibulinhoetec.com.br/", use_container_width=True)
        else:
            st.link_button("💡 Qualificação Profissional (Sebrae)", "https://www.sebrae.com.br/sites/PortalSebrae/ufs/sp?mapa=1", use_container_width=True)
        st.write("---")

st.caption("**Fonte das Ocupações:** Microdados Administrativos do Novo CAGED/MTE (Ref: Dez/2025).")

# 7. GRÁFICO, TABELA E NOTAS METODOLÓGICAS
st.markdown("---")
st.subheader("📈 Evolução de Vagas na Macrorregião")

df_grafico = pd.DataFrame({
    'Mês': ['Out', 'Nov', 'Dez', 'Jan'],
    'Saldo': [120, 150, -30, 85]
})

# Ordenação Cronológica
df_grafico['Mês'] = pd.Categorical(df_grafico['Mês'], categories=['Out', 'Nov', 'Dez', 'Jan'], ordered=True)
st.line_chart(data=df_grafico.sort_values('Mês'), x='Mês', y='Saldo', color="#2ecc71")

# EXPANDER FINAL: Tabela + Notas Metodológicas
with st.expander("📄 Notas Metodológicas e Dados Detalhados"):
    st.markdown("""
    **Fontes de Dados:**
    * **Novo CAGED (Ministério do Trabalho e Emprego):** Dados baseados nos registros administrativos de admissões e desligamentos (trabalho formal/CLT).
    * **PNADC (IBGE):** Indicadores de força de trabalho que captam a renda média real de todos os trabalhadores (formais e informais).
    
    **Conceitos:**
    * **Unidade Produtiva/Cluster:** Reflete o local administrativo onde a vaga foi gerada, permitindo identificar polos econômicos (ex: Polos Logísticos em Cajamar).
    * **Salário Admissional:** Refere-se à média de salário contratual declarada no ato da contratação.
    * **Saldo Macrorregional:** Soma aritmética do desempenho dos 4 municípios que compõem a região.
    """)
    st.write("---")
    st.write("**Tabela de Evolução Regional (Saldo Líquido):**")
    st.dataframe(df_grafico, hide_index=True, use_container_width=True)
