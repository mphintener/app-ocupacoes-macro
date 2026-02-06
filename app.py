import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURAÇÃO DE ESTILO (Visual Dark Mode Profissional)
st.set_page_config(page_title="Mercado de Trabalho e Qualificação", layout="centered")

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
        margin-bottom: 12px; border-top: 1px solid #334155; box-shadow: 0 4px 6px rgba(0,0,0,0.4);
    }
    
    /* Cores das Bordas por Setor */
    .border-logistica { border-left: 5px solid #3b82f6; }
    .border-industria { border-left: 5px solid #10b981; }
    .border-servicos { border-left: 5px solid #f59e0b; }
    .border-comercio { border-left: 5px solid #8b5cf6; }
    .border-saude { border-left: 5px solid #ef4444; }

    .titulo-vaga { font-size: 1rem; font-weight: bold; color: #ffffff; margin-bottom: 4px; }
    .nivel-tag { font-size: 0.6rem; font-weight: 800; padding: 2px 6px; border-radius: 4px; text-transform: uppercase; margin-bottom: 6px; display: inline-block; background-color: #334151; color: #94a3b8; }
    
    /* TABELA BI REFINADA */
    .dark-table {
        width: 100%; border-collapse: collapse; font-size: 0.75rem; background-color: #111418; 
        color: white; border-radius: 10px; overflow: hidden; margin-top: 10px;
    }
    .dark-table th { 
        background-color: #1e293b; padding: 10px; text-align: left; 
        color: #94a3b8; border-bottom: 2px solid #334155; text-transform: uppercase; letter-spacing: 0.5px;
    }
    .dark-table tr:nth-child(even) { background-color: #1a1d23; }
    .dark-table td { padding: 8px 10px; border-bottom: 1px solid #1e293b; }
    .pos-saldo { color: #60a5fa; font-weight: bold; }
    .salario-bi { color: #10b981; font-weight: bold; }
    
    .tabela-titulo { font-size: 1.1rem; font-weight: bold; color: #ffffff; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 2. CHAMADA EXPLICATIVA
with st.expander("💡 Entenda este Painel"):
    st.write("""
        Este aplicativo foi desenvolvido para orientar cidadãos e gestores da Macrorregião de Franco da Rocha 
        sobre as reais oportunidades de emprego formal. Cruzamos dados de contratações do **Novo CAGED (Dez/2025)** com cursos do **Centro Paula Souza (ETECs/FATECs)** e **Qualifica SP**.
    """)

# 3. PANORAMA MACRORREGIONAL
st.markdown("""
    <div class="header-dark">
        <div style="font-size: 0.65rem; color: #64748b; letter-spacing: 1px; font-weight: bold;">📊 INDICADORES DA MACRORREGIÃO</div>
        <h2>Mercado de Trabalho e Qualificação</h2>
        <div style="margin-top: 15px; display: flex; justify-content: space-between; border-top: 1px solid #334155; padding-top: 12px;">
            <div><small style="color: #94a3b8;">Renda Média Regional</small><br><b style="font-size: 1rem;">R$ 3.520,00</b></div>
            <div style="text-align: right;"><small style="color: #94a3b8;">Desocupação (PNADC 3T-2025)</small><br><b style="font-size: 1rem; color: #f87171;">7,8%</b></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. BASE DE DADOS INTEGRAL
data_list = [
    # CAJAMAR
    {"cid": "Cajamar", "ocup": "Analista de Logística", "set": "Logística", "cls": "border-logistica", "sal": "4.200", "niv": "Superior", "esc": "FATEC", "lnk": "https://www.fatec.sp.gov.br/", "sld": 142, "bai": "Jordanésia"},
    {"cid": "Cajamar", "ocup": "Conferente", "set": "Logística", "cls": "border-logistica", "sal": "2.600", "niv": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": 310, "bai": "Polvilho"},
    {"cid": "Cajamar", "ocup": "Auxiliar de Logística", "set": "Logística", "cls": "border-logistica", "sal": "2.150", "niv": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": 520, "bai": "Gato Preto"},
    # CAIEIRAS
    {"cid": "Caieiras", "ocup": "Mecânico Industrial", "set": "Indústria", "cls": "border-industria", "sal": "4.500", "niv": "Médio/Técnico", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/", "sld": 28, "bai": "Vila Rosina"},
    {"cid": "Caieiras", "ocup": "Operador de Produção", "set": "Indústria", "cls": "border-industria", "sal": "2.800", "niv": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": 115, "bai": "Laranjeiras"},
    # FRANCO DA ROCHA
    {"cid": "Franco da Rocha", "ocup": "Enfermeiro", "set": "Saúde", "cls": "border-saude", "sal": "4.800", "niv": "Superior", "esc": "FATEC Franco", "lnk": "https://www.fatecfrancodarocha.edu.br/", "sld": 12, "bai": "Centro"},
    {"cid": "Franco da Rocha", "ocup": "Técnico de Enfermagem", "set": "Saúde", "cls": "border-saude", "sal": "3.450", "niv": "Médio/Técnico", "esc": "ETEC Franco", "lnk": "https://www.cps.sp.gov.br/", "sld": 45, "bai": "Pouso Alegre"},
    {"cid": "Franco da Rocha", "ocup": "Vendedor", "set": "Comércio", "cls": "border-comercio", "sal": "2.050", "niv": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": 89, "bai": "Centro"},
    # FRANCISCO MORATO
    {"cid": "Francisco Morato", "ocup": "Gerente de Loja", "set": "Comércio", "cls": "border-comercio", "sal": "3.800", "niv": "Médio/Técnico", "esc": "ETEC Morato", "lnk": "http://etecfranciscomorato.com.br/", "sld": 15, "bai": "Centro"},
    {"cid": "Francisco Morato", "ocup": "Operador de Caixa", "set": "Comércio", "cls": "border-comercio", "sal": "1.820", "niv": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": 112, "bai": "Belém Capela"}
]

# 5. FILTRO E GRÁFICO DINÂMICO
df_total = pd.DataFrame(data_list)
cidade_sel = st.selectbox("📍 Selecione o Município:", df_total['cid'].unique())

st.markdown(f"#### Tendência em {cidade_sel}: Saldo de Vagas")
df_plot = df_total[df_total['cid'] == cidade_sel]
fig = px.bar(df_plot, x="ocup", y="sld", labels={"sld": "Saldo", "ocup": "Ocupação"}, template="plotly_dark")
fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", height=280)
fig.update_traces(marker_color='#3b82f6')
st.plotly_chart(fig, use_container_width=True)

# 6. CARDS DINÂMICOS
for v in data_list:
    if v['cid'] == cidade_sel:
        st.markdown(f"""
            <div class="card-vaga {v['cls']}">
                <div class="nivel-tag">Nível: {v['niv']}</div>
                <div class="titulo-vaga">{v['ocup']}</div>
                <div style="color:#94a3b8; font-size:0.75rem; margin-bottom:8px;">📍 Bairro: {v['bai']} | <b>Saldo: +{v['sld']}</b></div>
                <div style="color:#10b981; font-weight:bold; font-size: 0.9rem;">R$ {v['sal']}</div>
            </div>
            """, unsafe_allow_html=True)
        st.link_button(f"Qualificação Sugerida: {v['esc']}", v['lnk'], use_container_width=True)

# 7. TABELA GERAL REFINADA
st.divider()
st.markdown('<p class="tabela-titulo">Panorama de Saldos da Macrorregião (CAGED Dez/2025)</p>', unsafe_allow_html=True)

html_table = """<table class="dark-table"><thead><tr><th>Ocupação</th><th>Cidade</th><th>Saldo</th><th>Média Salarial</th></tr></thead><tbody>"""
for i in data_list:
    html_table += f"<tr><td><b>{i['ocup']}</b><br><small style='color:#94a3b8'>{i['niv']}</small></td><td>{i['cid']}</td><td class='pos-saldo'>+{i['sld']}</td><td class='salario-bi'>R$ {i['sal']}</td></tr>"
html_table += "</tbody></table>"
st.markdown(html_table, unsafe_allow_html=True)

st.markdown("---")
st.caption("Fontes: Microdados PNADC 3T-2025 (IBGE) e Novo CAGED (Dezembro/2025).")
