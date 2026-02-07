import streamlit as st
import pandas as pd
import plotly.express as px

# 1. ESTILO COM FONTES REDUZIDAS E CORREÇÃO TÉCNICA
st.set_page_config(page_title="BI Macrorregião", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117 !important; color: #ffffff !important; font-size: 0.85rem; }
    .header-dark { 
        background-color: #1a1d23; padding: 12px; border-radius: 10px; 
        border: 1px solid #334155; margin-bottom: 15px; 
    }
    .header-dark h2 { font-size: 1.1rem !important; margin: 2px 0; }
    .card-vaga { 
        background-color: #1a1d23; padding: 10px; border-radius: 8px; 
        margin-bottom: 8px; border-left: 4px solid #3b82f6; 
    }
    .card-vaga b { font-size: 0.9rem; }
    .curso-tag { font-size: 0.75rem; color: #94a3b8; margin: 4px 0; }
    .badge-inst { background-color: #1e293b; color: #60a5fa; padding: 1px 5px; border-radius: 3px; font-weight: bold; font-size: 0.7rem; }
    .dark-table {
        width: 100%; border-collapse: collapse; font-size: 0.75rem; background-color: #111418; 
        color: white; border-radius: 8px; overflow: hidden; margin-top: 10px;
    }
    .dark-table th { background-color: #1e293b; padding: 8px; text-align: left; color: #94a3b8; }
    .dark-table td { padding: 6px 8px; border-bottom: 1px solid #1e293b; }
    .salario-bi { color: #10b981; font-weight: bold; font-size: 0.8rem; }
    </style>
    """, unsafe_allow_html=True)

# 2. INDICADORES SÍNTESE (COM MENÇÃO À MACRORREGIÃO)
st.markdown("""
    <div class="header-dark">
        <div style="font-size: 0.6rem; color: #64748b; font-weight: bold; letter-spacing: 1px;">📊 MÉDIAS DA MACRORREGIÃO</div>
        <h2>Mercado de Trabalho e Qualificação</h2>
        <div style="margin-top: 10px; display: flex; justify-content: space-between; border-top: 1px solid #334155; padding-top: 8px;">
            <div><small style="color: #94a3b8; font-size: 0.65rem;">Renda Média Região</small><br><b style="font-size: 0.9rem;">R$ 3.520,00</b></div>
            <div style="text-align: right;"><small style="color: #94a3b8; font-size: 0.65rem;">Taxa Desocupação</small><br><b style="font-size: 0.9rem; color: #f87171;">7,8%</b></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 3. BASE DE DADOS INTEGRAL
data_base = [
    {"cid": "Cajamar", "ocup": "Auxiliar de Logística", "sld": 412, "sal": 2150, "curso": "Gestão de Estoques", "esc": "Qualifica SP"},
    {"cid": "Franco da Rocha", "ocup": "Técnico de Enfermagem", "sld": 45, "sal": 3450, "curso": "Técnico em Enfermagem", "esc": "ETEC Franco"},
    {"cid": "Caieiras", "ocup": "Mecânico Industrial", "sld": 28, "sal": 4500, "curso": "Mecânica Industrial", "esc": "ETEC Caieiras"},
    {"cid": "Francisco Morato", "ocup": "Vendedor", "sld": 89, "sal": 2050, "curso": "Técnicas de Vendas", "esc": "Qualifica SP"},
    {"cid": "Cajamar", "ocup": "Analista de Logística", "sld": 142, "sal": 4200, "curso": "Logística FATEC", "esc": "FATEC"},
    {"cid": "Francisco Morato", "ocup": "Gerente de Loja", "sld": 15, "sal": 3800, "curso": "Gestão Comercial", "esc": "ETEC Morato"},
    {"cid": "Franco da Rocha", "ocup": "Enfermeiro", "sld": 12, "sal": 4800, "curso": "Gestão Hospitalar", "esc": "FATEC Franco"}
]
df = pd.DataFrame(data_base)

# 4. PESQUISA POR CIDADE
st.markdown("<h4 style='font-size:1rem; margin-bottom:5px;'>📍 Oportunidades Locais</h4>", unsafe_allow_html=True)
cid_sel = st.selectbox("Selecione o Município:", df['cid'].unique(), label_visibility="collapsed")

for _, r in df[df['cid'] == cid_sel].iterrows():
    st.markdown(f"""
        <div class="card-vaga">
            <b>{r['ocup']}</b>
            <div class="curso-tag">📚 {r['curso']} (<span class="badge-inst">{r['esc']}</span>)</div>
            <div style="display: flex; justify-content: space-between; font-size: 0.75rem; margin-top:5px;">
                <span style="color:#94a3b8;">Saldo: +{r['sld']}</span>
                <span class="salario-bi">R$ {r['sal']:,}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# 5. GRÁFICO E TABELA REDUZIDOS
st.markdown("<h4 style='font-size:1rem;'>📊 Top 5 Ocupações (Região)</h4>", unsafe_allow_html=True)
fig = px.bar(df.nlargest(5, 'sld'), x='sld', y='ocup', orientation='h', color='cid', 
             template="plotly_dark", height=250)
fig.update_layout(font=dict(size=10), margin=dict(l=0, r=0, t=0, b=0), showlegend=False)
st.plotly_chart(fig, use_container_width=True)

st.markdown("<h4 style='font-size:1rem; margin-top:15px;'>📋 Tabela BI Geral</h4>", unsafe_allow_html=True)
html_table = f"""<table class="dark-table"><thead><tr><th>Ocupação</th><th>Cidade</th><th>Saldo</th><th>Salário</th></tr></thead><tbody>"""
for _, row in df.iterrows():
    html_table += f"<tr><td>{row['ocup']}</td><td>{row['cid']}</td><td>+{row['sld']}</td><td class='salario-bi'>R$ {row['sal']}</td></tr>"
html_table += "</tbody></table>"
st.markdown(html_table, unsafe_allow_html=True)

st.caption("Fontes: PNADC 3T-2025 e Novo CAGED (Janeiro/2026). Valores referentes à média da Macrorregião.")
