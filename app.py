import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="App Ocupações Macro", layout="wide")

# 2. BANCO DE DADOS
dados_lista = [
    {"cidade": "Cajamar", "local": "Jordanésia", "setor": "Logística", "vagas": 182, "cargo": "Auxiliar de Logística"},
    {"cidade": "Cajamar", "local": "Polvilho", "setor": "Comércio", "vagas": 45, "cargo": "Vendedor Lojista"},
    {"cidade": "Caieiras", "local": "Laranjeiras", "setor": "Indústria", "vagas": 64, "cargo": "Ajudante de Produção"},
    {"cidade": "Caieiras", "local": "Centro", "setor": "Administração", "vagas": 35, "cargo": "Assistente Administrativo"},
    {"cidade": "Franco da Rocha", "local": "Centro", "setor": "Serviços", "vagas": 58, "cargo": "Atendente de SAC"},
    {"cidade": "Franco da Rocha", "local": "Vila Rosalina", "setor": "Tecnologia", "vagas": 15, "cargo": "Suporte de TI"},
    {"cidade": "Francisco Morato", "local": "Belas Águas", "setor": "Comércio", "vagas": 72, "cargo": "Operador de Caixa"},
    {"cidade": "Francisco Morato", "local": "Centro", "setor": "Serviços", "vagas": 40, "cargo": "Vendedor"}
]
df_vagas = pd.DataFrame(dados_lista)

# 3. CABEÇALHO COM IDENTIDADE REGIONAL
st.title("📍 Conexão Ocupações")
st.subheader("Macrorregião de Franco da Rocha")
st.caption("Cajamar • Caieiras • Franco da Rocha • Francisco Morato")
st.markdown("---")

# 4. PANORAMA PNADC
st.markdown("### 📊 Panorama Socioeconômico Regional")
c1, c2 = st.columns(2)
c1.metric("Desemprego (Grande SP)", "8.1%", "-0.4%")
c2.metric("Renda Média Real", "R$ 3.240", "+1.2%")
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
        
        # Lógica Inteligente de Qualificação
        if linha['setor'] in ['Logística', 'Indústria', 'Tecnologia', 'Administração']:
            st.markdown(f"🔗 [**Qualificação Técnica (ETEC/FATEC)**](https://www.vestibulinhoetec.com.br/)")
        else:
            st.markdown(f"🔗 [**Capacitação e Vendas (Sebrae/Via Rápida)**](https://www.viarapida.sp.gov.br/)")
        st.write("---")

# 6. CONSOLIDAÇÃO DOS DADOS
st.subheader(f"📈 Evolução de Vagas: Macrorregião Franco da Rocha")

dados_grafico = pd.DataFrame({
    'Mês': ['Out', 'Nov', 'Dez', 'Jan'],
    'Saldo Líquido': [120, 150, -30, 85]
})

st.line_chart(data=dados_grafico, x='Mês', y='Saldo Líquido', color="#2ecc71")

with st.expander("📄 Ver Tabela de Dados (Soma da Macrorregião)"):
    st.dataframe(dados_grafico, use_container_width=True, hide_index=True)
    st.info("Nota: Os dados acima representam a soma do saldo de vagas dos 4 municípios da Macrorregião.")
