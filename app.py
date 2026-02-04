import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO
st.set_page_config(page_title="App Ocupações Macro", layout="wide")

# 2. BANCO DE DADOS (Clusters e Salários)
dados_lista = [
    {"cidade": "Cajamar", "local": "Jordanésia (Polo Logístico)", "setor": "Logística", "vagas": 182, "cargo": "Auxiliar de Logística", "salario": 1850.00},
    {"cidade": "Cajamar", "local": "Polvilho (Comércio)", "setor": "Comércio", "vagas": 45, "cargo": "Vendedor Lojista", "salario": 1720.00},
    {"cidade": "Caieiras", "local": "Laranjeiras (Indústria)", "setor": "Indústria", "vagas": 64, "cargo": "Ajudante de Produção", "salario": 1980.00},
    {"cidade": "Franco da Rocha", "local": "Centro (Polo Comercial)", "setor": "Serviços", "vagas": 58, "cargo": "Atendente de SAC", "salario": 1650.00},
    {"cidade": "Francisco Morato", "local": "Belas Águas (Comércio)", "setor": "Comércio", "vagas": 72, "cargo": "Operador de Caixa", "salario": 1680.00}
]
df_vagas = pd.DataFrame(dados_lista)

# 3. CABEÇALHO COM IDENTIDADE REGIONAL
st.title("📍 Conexão Ocupações")
st.subheader("Macrorregião de Franco da Rocha")
st.caption("Integração de Dados: PNADC/IBGE e Novo CAGED/MTE")
st.markdown("---")

# 4. PANORAMA REGIONAL (Estilo Referência)
st.markdown("### 📊 Panorama Socioeconômico (Média Regional)")
c1, c2 = st.columns(2)
c1.metric("Desemprego (Grande SP)", "8.1%", "-0.4%")
c2.metric("Renda Média PNADC", "R$ 3.240", "Referência")
st.divider()

# 5. FILTRO E LISTAGEM (Salário seguindo o formato acima)
st.sidebar.header("Navegação")
cidade_sel = st.sidebar.selectbox("Escolha a Cidade:", ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"])

st.header(f"Oportunidades em {cidade_sel}")
vagas_f = df_vagas[df_vagas['cidade'] == cidade_sel]

for _, linha in vagas_f.iterrows():
    with st.expander(f"💼 {linha['cargo']}", expanded=True):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.write(f"🏢 **Unidade Produtiva:** {linha['local']}")
            st.write(f"📈 **Saldo de Vagas:** {linha['vagas']}")
            st.write(f"📁 **Setor:** {linha['setor']}")
        
        with col2:
            # PADRONIZAÇÃO VISUAL: Salário no formato da Renda Média
            st.metric("Salário Admissional", f"R$ {linha['salario']:.2f}")

        # Botão de Ação
        if linha['setor'] in ['Logística', 'Indústria', 'Tecnologia', 'Administração']:
            st.link_button("🚀 Qualificação Técnica (ETEC)", "https://www.vestibulinhoetec.com.br/", use_container_width=True)
        else:
            st.link_button("💡 Qualificação Profissional (Sebrae)", "https://www.sebrae.com.br/sites/PortalSebrae/ufs/sp?mapa=1", use_container_width=True)

# 6. GRÁFICO DE EVOLUÇÃO
st.markdown("---")
st.subheader("📈 Evolução Mensal (Saldo Macrorregião)")
df_grafico = pd.DataFrame({'Mês': ['Out', 'Nov', 'Dez', 'Jan'], 'Saldo': [120, 150, -30, 85]})
df_grafico['Mês'] = pd.Categorical(df_grafico['Mês'], categories=['Out', 'Nov', 'Dez', 'Jan'], ordered=True)
st.line_chart(data=df_grafico.sort_values('Mês'), x='Mês', y='Saldo', color="#2ecc71")

with st.expander("ℹ️ Ver Dados Tabulares"):
    st.dataframe(df_grafico, hide_index=True, use_container_width=True)
