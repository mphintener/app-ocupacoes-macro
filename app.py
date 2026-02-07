import streamlit as st
import pandas as pd
import plotly.express as px

# 1. ESTILO MOBILE-FIRST REFINADO
st.set_page_config(page_title="BI Macrorregião", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117 !important; color: #ffffff !important; font-size: 0.82rem; }
    .header-dark { 
        background-color: #1a1d23; padding: 12px; border-radius: 10px; 
        border: 1px solid #334155; margin-bottom: 15px; 
    }
    .header-dark h2 { font-size: 1.05rem !important; margin: 2px 0; color: #f8fafc; }
    .card-vaga { 
        background-color: #1a1d23; padding: 10px; border-radius: 8px; 
        margin-bottom: 8px; border-left: 4px solid #3b82f6; 
    }
    .card-vaga b { font-size: 0.88rem; }
    .curso-tag { font-size: 0.72rem; color: #94a3b8; margin: 4px 0; }
    .badge-inst { background-color: #1e293b; color: #60a5fa; padding: 1px 5px; border-radius: 3px; font-weight: bold; font-size: 0.68rem; }
    .dark-table {
        width: 100%; border-collapse: collapse; font-size: 0.72rem; background-color: #111418; 
        color: white; border-radius: 8px; overflow: hidden; margin-top: 10px;
    }
    .dark-table th { background-color: #1e293b; padding: 8px; text-align: left; color: #94a3b8; }
    .dark-table td { padding: 6px 8px; border-bottom: 1px solid #1e293b; }
    .salario-bi { color: #10b981; font-weight: bold; font-size: 0.78rem; }
    </style>
    """, unsafe_allow_html=True)

# 2. EXPLICAÇÃO TÉCNICA (ATUALIZADA)
with st.expander("💡 Notas Técnicas e Abrangência"):
    st.write("""
        **Abrangência:** Dados consolidados da Macrorregião de Franco da Rocha 
        (**Cajamar, Caieiras, Francisco Morato e Franco da Rocha**).
        
        **Metodologia:** * Indicadores superiores: Médias Macrorregião baseadas na **PNADC/IBGE 3T 2025**.
        * Ocupações e Saldos: Baseados no **Novo CAGED (Jan/2026)**.
        * Salários: Referem-se ao **Salário Admissional Médio**.
    """)

# 3. INDICADORES SÍNTESE (MÉDIAS PNADC/IBGE)
st.markdown("""
    <div class="header-dark">
        <div style="font-size: 0.58rem; color: #64748b; font-weight: bold; letter-spacing: 1px;">📊 MÉDIAS MACRORREGIÃO (PNADC/IBGE)</div>
        <h2>Mercado de Trabalho e Qualificação</h2>
        <div style="margin-top: 10px; display: flex; justify-content: space-between; border-top: 1px solid #334155; padding-top: 8px;">
            <div><small style="color: #94a3b8; font-size: 0.62rem;">Renda Média Região</small><br><b style="font-size: 0.85rem;">R$ 3.520,00</b></div>
            <div style="text-align: right;"><small style="color: #94a3b8; font-size: 0.62rem;">Taxa Desocupação</small><br><b style="font-size: 0.85rem; color: #f87171;">7,8%</b></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. BASE DE DADOS INTEGRAL (EXPANDIDA)
data_base = [
    {"cid": "Cajamar", "ocup": "Auxiliar de Logística", "sld": 412, "sal": 2150, "curso": "Gestão de Estoques", "esc": "Qualifica SP"},
    {"cid": "Cajamar", "ocup": "Analista de Logística", "sld": 142, "sal": 4200, "curso": "Logística FATEC", "esc": "FATEC"},
    {"cid": "Franco da Rocha", "ocup": "Técnico de Enfermagem", "sld": 45, "sal": 3450, "curso": "Técnico em Enfermagem", "esc": "ETEC Franco"},
    {"cid": "Franco da Rocha", "ocup": "Enfermeiro", "sld": 12, "sal": 4800, "curso": "Gestão Hospitalar", "esc": "FATEC Franco"},
    {"cid": "Caieiras", "ocup": "Mecânico Industrial", "sld": 28, "sal": 4500, "curso": "Mecânica Industrial", "esc": "ETEC Caieiras"},
    {"cid": "Caieiras", "ocup": "Operador de Produção", "sld": 115, "sal": 2850, "curso": "Processos Industriais", "esc": "Qualifica SP"},
    {"cid": "Francisco Morato", "ocup": "Vendedor", "sld": 89, "sal": 2050, "curso": "Técnicas de Vendas", "esc": "Qualifica SP"},
    {"cid": "Francisco Morato", "ocup": "Gerente de Loja", "sld": 15, "sal": 3800, "curso": "Gestão Comercial", "esc": "ETEC Morato"}
]
df = pd.DataFrame(data_base)

# 5. PESQUISA POR CIDADE
st.markdown("<h4 style='font-size:0.95rem; margin-bottom:5px;'>📍 Oportunidades Locais</h4>", unsafe_allow_html=True)
cid_sel = st.selectbox("Selecione o Município:", df['cid'].unique(), label_visibility="collapsed")

for _, r in df[df['cid'] == cid_sel].iterrows():
    # Formatação do salário com ponto para milhar
    sal_formatado = f"{r['sal']:,.0f}".replace(",", ".")
    st.markdown(f"""
        <div class="card-vaga">
            <b>{r['ocup']}</b>
            <div class="curso-tag">📚 {r['curso']} (<span class="badge-inst">{r['esc']}</span>)</div>
            <div style="display: flex; justify-content: space-between; font-size: 0.72rem; margin-top:5px;">
                <span style="color:#94a3b8;">Saldo: +{r['sld']}</span>
                <span class="salario-bi">R$ {sal_formatado} (Adm.)</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# 6. GRÁFICO E TABELA (FOCO TÉCNICO)
st.markdown("<h4 style='font-size:0.95rem;'>📊 Top 5 Ocupações (Região)</h4>", unsafe_allow_html=True)
fig = px.bar(df.nlargest(5, 'sld'), x='sld', y='ocup', orientation='h', color='cid', 
             template="plotly_dark", height=220)
fig.update_layout(font=dict(size=9), margin=dict(l=0, r=0, t=0, b=0), showlegend=False)
st.plotly_chart(fig, use_container_width=True)

# TABELA BI COM TÍTULOS CORRIGIDOS
st.markdown("<h4 style='font-size:0.95rem; margin-top:10px;'>📋 Tabela BI Geral</h4>", unsafe_allow_html=True)
html_table = f"""<table class="dark-table">
    <thead>
        <tr>
            <th>Ocupação</th>
            <th>Cidade</th>
            <th>Saldo (Adm-Dem)</th>
            <th>Salário Adm.</th>
        </tr>
    </thead>
    <tbody>"""
for _, row in df.iterrows():
    sal_tab = f"{row['sal']:,.0f}".replace(",", ".")
    html_table += f"<tr><td>{row['ocup']}</td><td>{row['cid']}</td><td>+{row['sld']}</td><td class='salario-bi'>R$ {sal_tab}</td></tr>"
html_table += "</tbody></table>"
st.markdown(html_table, unsafe_allow_html=True)

st.caption("Fontes: PNADC/IBGE 3T-2025 e Novo CAGED (Jan/2026).")

