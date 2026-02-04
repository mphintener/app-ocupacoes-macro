import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO
st.set_page_config(page_title="App Ocupações Macro", layout="wide")

# 2. BANCO DE DADOS
dados_lista = [
    {"cidade": "Cajamar", "local": "Jordanésia", "setor": "Logística", "vagas": 182, "cargo": "Auxiliar de Logística"},
    {"cidade": "Cajamar", "local": "Polvilho", "setor": "Comércio", "vagas": 45, "cargo": "Vendedor Lojista"},
    {"cidade": "Caieiras", "local": "Laranjeiras", "setor": "Indústria", "vagas": 64, "cargo": "Ajudante de Produção"},
    {"cidade": "Franco da Rocha", "local": "Centro", "setor": "Serviços", "vagas": 58, "cargo": "Atendente de SAC"},
    {"cidade": "Francisco Morato", "local": "Belas Águas", "setor": "Comércio", "vagas": 72, "cargo": "Operador de Caixa"}
]
df_vagas = pd.DataFrame(dados_lista)

# 3. CABEÇALHO
st.title("📍 Conexão Ocupações")
st.subheader("Macrorregião de Franco da Rocha")
st.caption("Cajamar • Caieiras • Franco da Rocha • Francisco Morato")
st.markdown("---")

# 4. PANORAMA PNADC
st.markdown("### 📊 Panorama Socioeconômico Regional")
c1, c2 = st.columns(2)
c1.metric("Desemprego (Grande SP)", "8.1%", "-0.4%")
c2.metric("Renda Média Real", "R$ 3.240", "+1.2%")
st.caption("**Fonte:** PNADC/IBGE (Ref: Q4 2025).")
st.divider()

# 5. FILTRO E LISTAGEM
st.sidebar.header("Navegação Regional")
cidade_sel = st.sidebar.selectbox("Escolha a Cidade:", ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"])

st.header(f"Oportunidades em {cidade_sel}")
vagas_f = df_vagas[df_vagas['cidade'] == cidade_sel]

if not vagas_f.empty:
    for _, linha in vagas_f.iterrows():
        st.info(f"💼 **{linha['cargo']}**")
        st.write(f"📍 {linha['local']} | Setor: {linha['setor']} | Vagas: {linha['vagas']}")
        
        # LINKS FORMATADOS PARA FUNCIONAR NO MOBILE
        if linha['setor'] in ['Logística', 'Indústria', 'Tecnologia', 'Administração']:
            url = "https://www.vestibulinhoetec.com.br/"
            st.markdown(f"👉 [**CLIQUE AQUI: Ver Cursos na ETEC**]({url})")
        else:
            url = "https://www.viarapida.sp.gov.br/"
            st.markdown(f"👉 [**CLIQUE AQUI: Cursos Rápidos Sebrae/Via Rápida**]({url})")
        st.write("---")
st.caption("**Fonte:** Novo CAGED/MTE (Ref: Dez/2025).")

# 6. GRÁFICO COM MESES ORDENADOS
st.markdown("---")
st.subheader(f"📈 Evolução de Vagas: Macrorregião")

dados_grafico = pd.DataFrame({
    'Mês': ['Out', 'Nov', 'Dez', 'Jan'],
    'Saldo Líquido': [120, 150, -30, 85]
})

# Ordenação Categórica para o gráfico não "embaralhar"
dados_grafico['Mês'] = pd.Categorical(dados_grafico['Mês'], categories=['Out', 'Nov', 'Dez', 'Jan'], ordered=True)
dados_grafico = dados_grafico.sort_values('Mês')

st.line_chart(data=dados_grafico, x='Mês', y='Saldo Líquido', color="#2ecc71")

with st.expander("ℹ️ Notas Metodológicas e Fontes"):
    st.markdown("**Bases de Dados:** PNADC/IBGE e Novo CAGED/MTE.")
    st.dataframe(dados_grafico, use_container_width=True, hide_index=True)
