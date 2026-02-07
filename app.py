import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURAÇÃO E ESTILO
st.set_page_config(page_title="BI Macrorregião", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117 !important; color: #ffffff !important; }
    .header-dark { 
        background-color: #1a1d23; padding: 18px; border-radius: 12px; 
        border: 1px solid #334155; margin-bottom: 20px; 
    }
    .header-dark h2 { font-size: 1.3rem !important; margin: 5px 0; }
    .card-vaga { 
        background-color: #1a1d23; padding: 15px; border-radius: 10px; 
        margin-bottom: 12px; border-left: 5px solid #3b82f6; 
    }
    .curso-tag { font-size: 0.85rem; color: #94a3b8; margin: 8px 0; }
    .badge-inst { background-color: #1e293b; color: #60a5fa; padding: 2px 6px; border-radius: 4px; font-weight: bold; }
    .salario-bi { color: #10b981; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. TEXTO EXPLICATIVO (RECUPERADO)
with st.expander("💡 Entenda este Painel"):
    st.write("""
        Este aplicativo orienta cidadãos e gestores da Macrorregião de Franco da Rocha 
        sobre oportunidades de emprego. Cruzamos dados do **Novo CAGED (2026)** com cursos do **Centro Paula Souza (ETECs/FATECs)** e **Qualifica SP**.
    """)

# 3. INDICADORES SÍNTESE (RECUPERADO)
st.markdown("""
    <div class="header-dark">
        <div style="font-size: 0.65rem; color: #64748b; letter-spacing: 1px; font-weight: bold;">📊 INDICADORES DA MACRORREGIÃO</div>
        <h2>Mercado de Trabalho e Qualificação</h2>
        <div style="margin-top: 15px; display: flex; justify-content: space-between; border-top: 1px solid #334155; padding-top: 12px;">
            <div><small style="color: #94a3b8;">Renda Média Regional</small><br><b style="font-size: 1rem;">R$ 3.520,00</b></div>
            <div style="text-align: right;"><small style="color: #94a3b8;">Desocupação (PNADC)</small><br><b style="font-size: 1rem; color: #f87171;">7,8%</b></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. BASE DE DATOS COMPLETA (INCLUINDO MORATO)
data_full = [
    {"cid": "Cajamar", "ocup": "Auxiliar de Logística", "set": "Logística", "sld": 412, "sal": 2150, "curso": "Gestão de Estoques", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/"},
    {"cid": "Cajamar", "ocup": "Analista de Logística", "set": "Logística", "sld": 142, "sal": 4200, "curso": "Logística Aeroportuária", "esc": "FATEC", "lnk": "https://www.fatec.sp.gov.br/"},
    {"cid": "Franco da Rocha", "ocup": "Técnico de Enfermagem", "set": "Saúde", "sld": 45, "sal": 3450, "curso": "Técnico em Enfermagem", "esc": "ETEC Franco", "lnk": "https://www.cps.sp.gov.br/"},
    {"cid": "Franco da Rocha", "ocup": "Enfermeiro", "set": "Saúde", "sld": 12, "sal": 4800, "curso": "Gestão Hospitalar", "esc": "FATEC Franco", "lnk": "https://www.fatecfrancodarocha.edu.br/"},
    {"cid": "Caieiras", "ocup": "Mecânico Industrial", "set": "Indústria", "sld": 28, "sal": 4500, "curso": "Mecânica de Manutenção", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/"},
    {"cid": "Caieiras", "ocup": "Operador de Produção", "set": "Indústria", "sld": 115, "sal": 2800, "curso": "Processos Industriais", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/"},
    {"cid": "Francisco Morato", "ocup": "Vendedor", "set": "Comércio", "sld": 89, "sal": 2050, "curso": "Técnicas de Vendas", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/"},
    {"cid": "Francisco Morato", "ocup": "Gerente de Loja", "set": "Comércio", "sld": 15, "sal": 3800, "curso": "Gestão Comercial", "esc": "ETEC Morato", "lnk": "http://etecfranciscomorato.com.br/"}
]

# UPLOAD E LÓGICA
uploaded_file = st.sidebar.file_uploader("Upload da Planilha Mestra (.xlsx)", type="xlsx")
df = pd.read_excel(uploaded_file) if uploaded_file else pd.DataFrame(data_full)

# 5. NAVEGAÇÃO POR ABAS
aba1, aba2 = st.tabs(["💼 Vagas e Cursos", "📊 Gestão Estratégica"])

with aba1:
    cid_sel = st.selectbox("📍 Selecione o Município:", df['cid'].unique())
    df_f = df[df['cid'] == cid_sel]
    
    for _, r in df_f.iterrows():
        st.markdown(f"""
            <div class="card-vaga">
                <div class="titulo-vaga">{r['ocup']}</div>
                <div class="curso-tag">
                    📚 <b>Curso:</b> {r['curso']}<br>
                    🏫 <span class="badge-inst">{r['esc']}</span>
                </div>
                <div style="display: flex; justify-content: space-between;">
                    <span style="font-size: 0.8rem; color: #64748b;">Saldo: +{r['sld']}</span>
                    <span class="salario-bi">R$ {r['sal']:,}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.link_button(f"Inscrição em {r['esc']}", r['lnk'], use_container_width=True)

with aba2:
    st.write("### 🏆 Top 5 Ocupações (Maior Saldo)")
    top5 = df.nlargest(5, 'sld')
    fig1 = px.bar(top5, x='sld', y='ocup', orientation='h', color='cid', template="plotly_dark", height=300)
    st.plotly_chart(fig1, use_container_width=True)
    
    st.write("### 💰 Média Salarial por Cidade")
    df_sal = df.groupby('cid')['sal'].mean().reset_index().sort_values('sal', ascending=False)
    fig2 = px.line(df_sal, x='cid', y='sal', markers=True, template="plotly_dark")
    fig2.update_traces(line_color='#10b981')
    st.plotly_chart(fig2, use_container_width=True)
