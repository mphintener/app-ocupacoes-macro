import streamlit as st
import pandas as pd
import plotly.express as px

# Força o tema escuro e layout mobile
st.set_page_config(page_title="BI Macro", layout="centered")

# 1. DADOS FIXOS - TESTE SE FRANCISCO MORATO APARECE AQUI
data = [
    {"cid": "Cajamar", "ocup": "Auxiliar de Logística", "sld": 412, "sal": 2150},
    {"cid": "Francisco Morato", "ocup": "Vendedor", "sld": 89, "sal": 2050},
    {"cid": "Franco da Rocha", "ocup": "Técnico de Enfermagem", "sld": 45, "sal": 3450},
    {"cid": "Caieiras", "ocup": "Operador de Produção", "sld": 115, "sal": 2800}
]
df = pd.DataFrame(data)

# 2. CABEÇALHO QUE VOCÊ GOSTA
st.title("📊 BI Macrorregião")
st.markdown("---")

# 3. ABAS SIMPLES
tab1, tab2 = st.tabs(["Vagas", "Gestão"])

with tab1:
    escolha = st.selectbox("Escolha a Cidade:", df['cid'].unique())
    filtro = df[df['cid'] == escolha]
    for _, item in filtro.iterrows():
        st.subheader(f"{item['ocup']}")
        st.write(f"💰 Salário: R$ {item['sal']}")
        st.write(f"📈 Saldo: +{item['sld']}")
        st.divider()

with tab2:
    st.subheader("Ranking de Vagas")
    fig1 = px.bar(df, x='sld', y='ocup', color='cid', orientation='h', template="plotly_dark")
    st.plotly_chart(fig1, use_container_width=True)
    
    st.subheader("Média Salarial")
    fig2 = px.line(df.groupby('cid')['sal'].mean().reset_index(), x='cid', y='sal', markers=True, template="plotly_dark")
    st.plotly_chart(fig2, use_container_width=True)
