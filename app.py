import streamlit as st
import pandas as pd
import plotly.express as px

# 1. ESTILO E CONFIGURAÇÃO
st.set_page_config(page_title="BI Macrorregião", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117 !important; color: #ffffff !important; }
    .header-dark { background-color: #1a1d23; padding: 18px; border-radius: 12px; border: 1px solid #334155; margin-bottom: 20px; }
    .card-vaga { background-color: #1a1d23; padding: 15px; border-radius: 10px; margin-bottom: 12px; border-left: 5px solid #3b82f6; }
    .salario-bi { color: #10b981; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. INDICADORES E EXPLICAÇÃO (Mantidos conforme solicitado)
with st.expander("💡 Sobre este Painel"):
    st.write("Análise de empregabilidade da Macrorregião de Franco da Rocha baseada no Novo CAGED 2026.")

st.markdown("""
    <div class="header-dark">
        <div style="font-size: 0.65rem; color: #64748b; font-weight: bold;">📊 INDICADORES SÍNTESE</div>
        <h2>Mercado de Trabalho e Qualificação</h2>
        <div style="margin-top: 15px; display: flex; justify-content: space-between; border-top: 1px solid #334155; padding-top: 12px;">
            <div><small>Renda Média</small><br><b>R$ 3.520,00</b></div>
            <div style="text-align: right;"><small>Desocupação</small><br><b style="color: #f87171;">7,8%</b></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 3. DADOS (Base completa com Morato e Cursos)
data_full = [
    {"cid": "Cajamar", "ocup": "Aux. Logística", "set": "Logística", "sld": 412, "sal": 2150, "curso": "Gestão de Estoques", "esc": "Qualifica SP", "lnk": "#"},
    {"cid": "Franco da Rocha", "ocup": "Téc. Enfermagem", "set": "Saúde", "sld": 45, "sal": 3450, "curso": "Técnico em Enfermagem", "esc": "ETEC Franco", "lnk": "#"},
    {"cid": "Caieiras", "ocup": "Op. Produção", "set": "Indústria", "sld": 115, "sal": 2800, "curso": "Processos Industriais", "esc": "Qualifica SP", "lnk": "#"},
    {"cid": "Francisco Morato", "ocup": "Vendedor", "set": "Comércio", "sld": 89, "sal": 2050, "curso": "Técnicas de Vendas", "esc": "Qualifica SP", "lnk": "#"},
    {"cid": "Cajamar", "ocup": "Analista Log.", "set": "Logística", "sld": 142, "sal": 4200, "curso": "Logística FATEC", "esc": "FATEC", "lnk": "#"}
]

uploaded_file = st.sidebar.file_uploader("Upload Excel", type="xlsx")
df = pd.read_excel(uploaded_file) if uploaded_file else pd.DataFrame(data_full)

aba1, aba2 = st.tabs(["💼 Vagas e Cursos", "📊 Gestão Estratégica"])

with aba1:
    cid_sel = st.selectbox("📍 Selecione a Cidade:", df['cid'].unique())
    for _, r in df[df['cid'] == cid_sel].iterrows():
        st.markdown(f"""<div class="card-vaga"><b>{r['ocup']}</b><br><small>📚 {r['curso']} ({r['esc']})</small><br>
                    <span style="font-size:0.8rem">Saldo: +{r['sld']}</span> | <span class="salario-bi">R$ {r['sal']}</span></div>""", unsafe_allow_html=True)

with aba2:
    # Ajuste Top 5: Horizontal e Ordenado
    st.write("### 🏆 Top 5 Ocupações (Vagas)")
    top5 = df.nlargest(5, 'sld').sort_values('sld', ascending=True)
    fig1 = px.bar(top5, x='sld', y='ocup', orientation='h', 
                 text='sld', # Coloca o número dentro/fora da barra
                 template="plotly_dark", 
                 color_discrete_sequence=['#3b82f6'],
                 labels={'sld': 'Total de Vagas', 'ocup': ''})
    fig1.update_traces(textposition='outside')
    fig1.update_layout(yaxis={'categoryorder':'total ascending'}, height=350, margin=dict(l=0, r=0, t=10, b=0))
    st.plotly_chart(fig1, use_container_width=True)
    
    # Ajuste Média Salarial: Linha com Rótulos de Valor
    st.write("### 💰 Média Salarial por Município")
    df_sal = df.groupby('cid')['sal'].mean().reset_index().sort_values('sal', ascending=False)
    fig2 = px.line(df_sal, x='cid', y='sal', text='sal', markers=True,
                  template="plotly_dark",
                  labels={'sal': 'Salário Médio', 'cid': ''})
    fig2.update_traces(textposition="top center", line_color='#10b981', texttemplate='R$ %{text:.0f}')
    fig2.update_layout(height=300, yaxis={'visible': False}) # Esconde o eixo Y para limpar o visual
    st.plotly_chart(fig2, use_container_width=True)
