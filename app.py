import streamlit as st
import pandas as pd
import plotly.express as px

# 1. ESTILO MOBILE-FIRST REFINADO
st.set_page_config(page_title="BI Macrorregião", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117 !important; color: #ffffff !important; }
    .header-dark { background-color: #1a1d23; padding: 15px; border-radius: 10px; border: 1px solid #334155; margin-bottom: 15px; }
    .card-vaga { background-color: #1a1d23; padding: 15px; border-radius: 10px; margin-bottom: 12px; border-left: 5px solid #3b82f6; }
    .titulo-vaga { font-size: 1rem; font-weight: bold; color: #ffffff; }
    .curso-info { font-size: 0.85rem; color: #94a3b8; margin: 8px 0; }
    .badge-instituicao { background-color: #1e293b; color: #60a5fa; padding: 2px 8px; border-radius: 4px; font-weight: bold; }
    .salario-tag { color: #10b981; font-weight: bold; font-size: 0.95rem; }
    </style>
    """, unsafe_allow_html=True)

# 2. MENU POR ABAS
aba = st.tabs(["💼 Vagas e Cursos", "📊 Painel de Gestão"])

# 3. CARREGAMENTO DE DADOS
# Adicionei a coluna 'curso' para clareza técnica
data_base = [
    {"cid": "Cajamar", "ocup": "Auxiliar de Logística", "set": "Logística", "sld": 412, "sal": 2150, "curso": "Gestão de Estoques", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/"},
    {"cid": "Franco da Rocha", "ocup": "Técnico de Enfermagem", "set": "Saúde", "sld": 34, "sal": 3400, "curso": "Técnico em Enfermagem", "esc": "ETEC Franco", "lnk": "https://www.cps.sp.gov.br/"},
    {"cid": "Caieiras", "ocup": "Mecânico Industrial", "set": "Indústria", "sld": 28, "sal": 4500, "curso": "Mecânica de Manutenção", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/"}
]

# Tenta carregar arquivo do usuário, senão usa a base acima
uploaded_file = st.sidebar.file_uploader("Atualizar Base (Excel)", type="xlsx")
if uploaded_file:
    df = pd.read_excel(uploaded_file)
else:
    df = pd.DataFrame(data_base)

# --- ABA 1: VAGAS E QUALIFICAÇÃO ---
with aba[0]:
    st.markdown('<div class="header-dark"><h2>Oportunidades e Formação</h2></div>', unsafe_allow_html=True)
    cidades = df['cid'].unique()
    cid_sel = st.selectbox("📍 Filtrar por Cidade:", cidades)
    
    df_filtrado = df[df['cid'] == cid_sel]
    
    for _, r in df_filtrado.iterrows():
        st.markdown(f"""
            <div class="card-vaga">
                <div class="titulo-vaga">{r['ocup']}</div>
                <div class="curso-info">
                    📚 <b>Qualificação:</b> {r['curso']}<br>
                    🏫 <span class="badge-instituicao">{r['esc']}</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
                    <span style="font-size: 0.8rem; color: #64748b;">Saldo: +{r['sld']}</span>
                    <span class="salario-tag">R$ {r['sal']:,}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.link_button(f"Ver detalhes do curso em {r['esc']}", r['lnk'], use_container_width=True)

# --- ABA 2: GESTÃO (TOP 5 E SALÁRIOS) ---
with aba[1]:
    st.markdown('<div class="header-dark"><h2>Indicadores Estratégicos</h2></div>', unsafe_allow_html=True)
    
    # Ranking Top 5
    st.write("### 🏆 Top 5 Ocupações (Maior Saldo)")
    top_5 = df.nlargest(5, 'sld')
    fig_rank = px.bar(top_5, x='sld', y='ocup', orientation='h', color='cid', 
                      template="plotly_dark", height=300, labels={'sld':'Vagas', 'ocup':''})
    st.plotly_chart(fig_rank, use_container_width=True)
    
    # NOVO: Média Salarial por Cidade
    st.write("### 💰 Média Salarial Regional")
    df_salario = df.groupby('cid')['sal'].mean().reset_index().sort_values('sal', ascending=False)
    fig_sal = px.line(df_salario, x='cid', y='sal', markers=True, template="plotly_dark",
                      labels={'sal':'Salário Médio (R$)', 'cid':''})
    fig_sal.update_traces(line_color='#10b981', marker_size=10)
    st.plotly_chart(fig_sal, use_container_width=True)
