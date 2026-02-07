import streamlit as st
import pandas as pd
import plotly.express as px

# 1. ESTILO SEGURO
st.set_page_config(page_title="BI Macro", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117 !important; color: #ffffff !important; font-size: 0.82rem; }
    .header-dark { background-color: #1a1d23; padding: 12px; border-radius: 10px; border: 1px solid #334155; margin-bottom: 15px; }
    .header-dark h2 { font-size: 1.05rem !important; margin: 2px 0; color: #f8fafc; }
    .card-vaga { background-color: #1a1d23; padding: 10px; border-radius: 8px; margin-bottom: 8px; border-left: 4px solid #3b82f6; }
    .badge-inst { background-color: #1e293b; color: #60a5fa; padding: 1px 5px; border-radius: 3px; font-weight: bold; font-size: 0.68rem; }
    .dark-table { width: 100%; border-collapse: collapse; font-size: 0.72rem; background-color: #111418; color: white; border-radius: 8px; overflow: hidden; margin-top: 10px; }
    .dark-table th { background-color: #1e293b; padding: 8px; text-align: left; color: #94a3b8; }
    .dark-table td { padding: 6px 8px; border-bottom: 1px solid #1e293b; }
    .salario-bi { color: #10b981; font-weight: bold; font-size: 0.78rem; }
    </style>
    """, unsafe_allow_html=True)

# 2. INDICADORES PNADC/IBGE
st.markdown("""
    <div class="header-dark">
        <div style="font-size: 0.58rem; color: #64748b; font-weight: bold; letter-spacing: 1px;">📊 MÉDIAS MACRORREGIÃO (PNADC/IBGE)</div>
        <h2>Mercado de Trabalho e Qualificação</h2>
        <div style="margin-top: 10px; display: flex; justify-content: space-between; border-top: 1px solid #334155; padding-top: 8px;">
            <div><small style="color: #94a3b8; font-size: 0.62rem;">Renda Média Região</small><br><b style="font-size: 0.85rem;">R$ 3.520.00</b></div>
            <div style="text-align: right;"><small style="color: #94a3b8; font-size: 0.62rem;">Taxa Desocupação</small><br><b style="font-size: 0.85rem; color: #f87171;">7,8%</b></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 3. DADOS (4 POR CIDADE)
data_base = [
    {"cid": "Cajamar", "ocup": "Auxiliar de Logística", "sld": 412, "sal": 2150, "curso": "Gestão de Estoques", "esc": "Qualifica SP"},
    {"cid": "Cajamar", "ocup": "Analista de Logística", "sld": 142, "sal": 4200, "curso": "Logística FATEC", "esc": "FATEC"},
    {"cid": "Cajamar", "ocup": "Conferente", "sld": 85, "sal": 2600, "curso": "Operações de CD", "esc": "ETEC"},
    {"cid": "Cajamar", "ocup": "Líder de Operações", "sld": 32, "sal": 5100, "curso": "Gestão de Equipes", "esc": "FATEC"},
    {"cid": "Franco da Rocha", "ocup": "Técnico de Enfermagem", "sld": 45, "sal": 3450, "curso": "Técnico em Enfermagem", "esc": "ETEC Franco"},
    {"cid": "Franco da Rocha", "ocup": "Enfermeiro", "sld": 12, "sal": 4800, "curso": "Gestão Hospitalar", "esc": "FATEC Franco"},
    {"cid": "Franco da Rocha", "ocup": "Auxiliar Administrativo", "sld": 28, "sal": 2300, "curso": "Gestão Empresarial", "esc": "ETEC"},
    {"cid": "Franco da Rocha", "ocup": "Recepcionista", "sld": 19, "sal": 1950, "curso": "Atendimento VIP", "esc": "Qualifica SP"},
    {"cid": "Caieiras", "ocup": "Mecânico Industrial", "sld": 28, "sal": 4500, "curso": "Mecânica Industrial", "esc": "ETEC Caieiras"},
    {"cid": "Caieiras", "ocup": "Operador de Produção", "sld": 115, "sal": 2850, "curso": "Processos Industriais", "esc": "Qualifica SP"},
    {"cid": "Caieiras", "ocup": "Técnico em Química", "sld": 14, "sal": 3900, "curso": "Química Industrial", "esc": "ETEC"},
    {"cid": "Caieiras", "ocup": "Eletricista", "sld": 22, "sal": 3200, "curso": "Elétrica Predial", "esc": "ETEC"},
    {"cid": "Francisco Morato", "ocup": "Vendedor", "sld": 89, "sal": 2050, "curso": "Técnicas de Vendas", "esc": "Qualifica SP"},
    {"cid": "Francisco Morato", "ocup": "Gerente de Loja", "sld": 15, "sal": 3800, "curso": "Gestão Comercial", "esc": "ETEC Morato"},
    {"cid": "Francisco Morato", "ocup": "Auxiliar de Almoxarifado", "sld": 24, "sal": 2100, "curso": "Logística Básica", "esc": "Qualifica SP"},
    {"cid": "Francisco Morato", "ocup": "Balconista", "sld": 37, "sal": 1850, "curso": "Varejo", "esc": "ETEC"}
]
df = pd.DataFrame(data_base)

# 4. PESQUISA SIMPLES
st.markdown("<h4 style='font-size:0.95rem;'>📍 Oportunidades Locais</h4>", unsafe_allow_html=True)
cid_sel = st.selectbox("Selecione o Município:", df['cid'].unique())

for _, r in df[df['cid'] == cid_sel].iterrows():
    sal_format = f"{r['sal']:,.0f}".replace(",", ".")
    st.markdown(f"""
        <div class="card-vaga">
            <b>{r['ocup']}</b><br>
            <small style="color:#94a3b8;">📚 {r['curso']} ({r['esc']})</small>
            <div style="display:flex; justify-content:space-between; font-size:0.72rem; margin-top:5px;">
                <span>Saldo: +{r['sld']}</span>
                <span class="salario-bi">R$ {sal_format} (Adm.)</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# 5. GRÁFICO TOP 5
st.markdown("<h4 style='font-size:0.95rem;'>🏆 Top 5 Ocupações (Região)</h4>", unsafe_allow_html=True)
top5 = df.nlargest(5, 'sld')
fig = px.bar(top5, x='sld', y='ocup', orientation='h', color='cid', template="plotly_dark", height=230, text_auto=True)
fig.update_layout(font=dict(size=9), margin=dict(l=0, r=0, t=0, b=0), showlegend=False)
st.plotly_chart(fig, use_container_width=True)

# 6. TABELA BI
st.markdown("<h4 style='font-size:0.95rem;'>📊 Tabela BI: Ocupações da Macrorregião</h4>", unsafe_allow_html=True)
st.caption("Fonte: Novo CAGED (Jan/2026)")
html_table = f"""<table class="dark-table">
    <thead><tr><th>Ocupação</th><th>Cidade</th><th>Saldo (Adm-Dem)</th><th>Salário Adm.</th></tr></thead>
    <tbody>"""
for _, row in df.sort_values('sld', ascending=False).iterrows():
    sal_tab = f"{row['sal']:,.0f}".replace(",", ".")
    html_table += f"<tr><td>{row['ocup']}</td><td>{row['cid']}</td><td>+{row['sld']}</td><td class='salario-bi'>R$ {sal_tab}</td></tr>"
html_table += "</tbody></table>"
st.markdown(html_table, unsafe_allow_html=True)
