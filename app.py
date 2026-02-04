import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO
st.set_page_config(page_title="App Ocupações Macro", layout="wide")

# 2. BANCO DE DADOS ATUALIZADO (Com Salário Admissional Médio)
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

# 4. PANORAMA SOCIOECONÔMICO
st.markdown("### 📊 Indicadores Regionais (PNADC/IBGE)")
c1, c2 = st.columns(2)
c1.metric("Desemprego (Grande SP)", "8.1%", "-0.4%")
c2.metric("Renda Média Real", "R$ 3.240", "+1.2%")

st.divider()

# 5. FILTRO E LISTAGEM COM SALÁRIOS
st.sidebar.header("Navegação")
cidade_sel = st.sidebar.selectbox("Escolha a Cidade:", ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"])

st.header(f"Oportunidades: {cidade_sel}")
vagas_f = df_vagas[df_vagas['cidade'] == cidade_sel]

for _, linha in vagas_f.iterrows():
    with st.container():
        st.info(f"💼 **{linha['cargo']}**")
        
        # Colunas para organizar os dados da vaga e o salário
        col_vaga, col_sal = st.columns([2, 1])
        with col_vaga:
            st.write(f"🏢 **Unidade:** {linha['local']}")
            st.write(f"📈 **Vagas:** {linha['vagas']}")
        with col_sal:
            # Exibindo o salário com formatação de moeda
            st.metric("Salário Médio", f"R$ {linha['salario']:.2f}")
        
        # Botões de Link dinâmicos
        if linha['setor'] in ['Logística', 'Indústria', 'Tecnologia', 'Administração']:
            st.link_button("🚀 Ver Cursos Técnicos (ETEC)", "https://www.vestibulinhoetec.com.br/", use_container_width=True)
        else:
            st.link_button("💡 Qualificação Profissional (Sebrae)", "https://www.sebrae.com.br/sites/PortalSebrae/ufs/sp?mapa=1", use_container_width=True)
        st.write("---")

# 6. GRÁFICO DE EVOLUÇÃO (CAGED)
st.subheader("📈 Evolução de Vagas na Macrorregião")
df_grafico = pd.DataFrame({'Mês': ['Out', 'Nov', 'Dez', 'Jan'], 'Saldo': [120, 150, -30, 85]})
df_grafico['Mês'] = pd.Categorical(df_grafico['Mês'], categories=['Out', 'Nov', 'Dez', 'Jan'], ordered=True)
st.line_chart(data=df_grafico.sort_values('Mês'), x='Mês', y='Saldo', color="#2ecc71")

with st.expander("ℹ️ Notas Metodológicas"):
    st.write("**Salário Admissional:** Média baseada nos registros do Novo CAGED para a ocupação e região.")
    st.dataframe(df_grafico, hide_index=True, use_container_width=True)
