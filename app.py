import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURAÇÃO DE ESTILO (Fontes reduzidas e Dark Mode)
st.set_page_config(page_title="Mercado de Trabalho e Qualificação", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117 !important; color: #ffffff !important; }
    
    /* Header com fontes menores */
    .header-dark { background-color: #1a1d23; padding: 20px; border-radius: 12px; border: 1px solid #334155; margin-bottom: 20px; }
    .header-dark h2 { font-size: 1.4rem !important; margin: 5px 0; }
    
    .info-box { background-color: #1e293b; padding: 15px; border-radius: 8px; border-left: 4px solid #3b82f6; margin-bottom: 20px; }

    /* Cards com títulos menores */
    .card-vaga { background-color: #1a1d23; padding: 15px; border-radius: 10px; margin-bottom: 12px; border-top: 1px solid #334155; box-shadow: 0 4px 6px rgba(0,0,0,0.4); }
    .titulo-vaga { font-size: 1.1rem !important; font-weight: bold; color: #ffffff; margin-bottom: 5px; }
    
    /* Bordas por Setor */
    .border-logistica { border-left: 5px solid #3b82f6; }
    .border-industria { border-left: 5px solid #10b981; }
    .border-servicos { border-left: 5px solid #f59e0b; }
    .border-comercio { border-left: 5px solid #8b5cf6; }
    .border-saude { border-left: 5px solid #ef4444; }

    .nivel-tag { font-size: 0.65rem; font-weight: 800; padding: 2px 6px; border-radius: 4px; text-transform: uppercase; margin-bottom: 8px; display: inline-block; background-color: #334151; color: #94a3b8; }
    .salario-valor { font-size: 1rem; font-weight: bold; color: #10b981; }

    /* Tabela BI Ajustada */
    .dark-table { width: 100%; border-collapse: collapse; font-size: 0.8rem; background-color: #111418; color: white; border-radius: 8px; overflow: hidden; }
    .dark-table th { background-color: #1e293b; padding: 10px; text-align: left; color: #94a3b8; border-bottom: 2px solid #334155; text-transform: uppercase; }
    .dark-table td { padding: 8px 10px; border-bottom: 1px solid #1e293b; }
    .pos-saldo { color: #60a5fa; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. CHAMADA EXPLICATIVA
with st.container():
    st.markdown("""
        <div class="info-box">
            <h5 style="margin:0; font-size: 1rem;">💡 Entenda este Painel</h5>
            <p style="margin:5px 0 0 0; font-size:0.85rem; color:#94a3b8;">Conectamos oportunidades reais do Novo CAGED à sua qualificação ideal.</p>
        </div>
    """, unsafe_allow_html=True)
    with st.expander("Ver Metodologia e Objetivo"):
        st.write("""
            Este aplicativo orienta cidadãos e gestores da Macrorregião de Franco da Rocha sobre as reais oportunidades de emprego formal. 
            Cruzamos dados do **Novo CAGED (Dezembro/2025)** com cursos do **Centro Paula Souza (ETECs/FATECs)** e **Qualifica SP**, 
            direcionando você para a preparação correta conforme o nível de escolaridade da vaga.
        """)

# 3. PANORAMA MACRORREGIONAL
st.markdown("""
    <div class="header-dark">
        <div style="font-size: 0.7rem; color: #64748b; letter-spacing: 1px; font-weight: bold;">📊 EIXO NORTE • INDICADORES DA MACRORREGIÃO</div>
        <h2>Mercado de Trabalho e Qualificação</h2>
        <div style="margin-top: 15px; padding-top: 12px; border-top: 1px solid #334155; display: flex; justify-content: space-between;">
            <div><small style="color: #94a3b8;">Renda Média Regional</small><br><b style="font-size: 1.1rem;">R$ 3.520,00</b></div>
            <div style="text-align: right;"><small style="color: #94a3b8;">Desocupação (PNADC 3T-2025)</small><br><b style="font-size: 1.1rem; color: #f87171;">7,8%</b></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. BASE DE DADOS (Links corrigidos por nível)
data_list = [
    # FRANCO DA ROCHA
    {"cid": "Franco da Rocha", "ocup": "Enfermeiro", "set": "Saúde", "cls": "border-saude", "sal": "4.800", "niv": "Superior", "esc": "FATEC Franco", "lnk": "https://www.fatecfrancodarocha.edu.br/", "sld": 12, "bai": "Centro"},
    {"cid": "Franco da Rocha", "ocup": "Técnico de Enfermagem", "set": "Saúde", "cls": "border-saude", "sal": "3.450", "niv": "Médio/Técnico", "esc": "ETEC Franco", "lnk": "https://www.cps.sp.gov.br/", "sld": 45, "bai": "Pouso Alegre"},
    {"cid": "Franco da Rocha", "ocup": "Vendedor", "set": "Comércio", "cls": "border-comercio", "sal": "2.050", "niv": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": 89, "bai": "Centro"},
    {"cid": "Franco da Rocha", "ocup": "Auxiliar Administrativo", "set": "Serviços", "cls": "border-servicos", "sal": "2.100", "niv": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": 34, "bai": "Centro"},
    {"cid": "Franco da Rocha", "ocup": "Auxiliar Logístico", "set": "Logística", "cls": "border-logistica", "sal": "2.100", "niv": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": 134, "bai": "Vila Rosalina"},
    
    # FRANCISCO MORATO
    {"cid": "Francisco Morato", "ocup": "Gerente de Loja", "set": "Comércio", "cls": "border-comercio", "sal": "3.800", "niv": "Médio/Técnico", "esc": "ETEC Morato", "lnk": "http://etecfranciscomorato.com.br/", "sld": 15, "bai": "Centro"},
    {"cid": "Francisco Morato", "ocup": "Vendedor Especializado", "set": "Comércio", "cls": "border-comercio", "sal": "2.200", "niv": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": 56, "bai": "Centro"},
    {"cid": "Francisco Morato", "ocup": "Operador de Caixa", "set": "Comércio", "cls": "border-comercio", "sal": "1.820", "niv": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": 112, "bai": "Belém Capela"},
    {"cid": "Francisco Morato", "ocup": "Assistente Logístico", "set": "Logística", "cls": "border-logistica", "sal": "2.450", "niv": "Médio/Técnico", "esc": "ETEC Morato", "lnk": "http://etecfranciscomorato.com.br/", "sld": 42, "bai": "Centro"},
    {"cid": "Francisco Morato", "ocup": "Estoquista", "set": "Logística", "cls": "border-logistica", "sal": "1.900", "niv": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": 78, "bai": "Nova Morato"},
    
    # CAJAMAR
    {"cid": "Cajamar", "ocup": "Analista de Logística", "set": "Logística", "cls": "border-logistica", "sal": "4.200", "niv": "Superior", "esc": "FATEC", "lnk": "https://www.fatec.sp.gov.br/", "sld": 142, "bai": "Jordanésia"},
    {"cid": "Cajamar", "ocup": "Conferente", "set": "Logística", "cls": "border-logistica", "sal": "2.600", "niv": "Médio/Técnico", "esc": "ETEC", "lnk": "https://www.cps.sp.gov.br/", "sld": 310, "bai": "Polvilho"},
    {"cid": "Cajamar", "ocup": "Auxiliar de Logística", "set": "Logística", "cls": "border-logistica", "sal": "2.150", "niv": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": 520, "bai": "Gato Preto"},
    {"cid": "Cajamar", "ocup": "Op. de Empilhadeira", "set": "Logística", "cls": "border-logistica", "sal": "2.900", "niv": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": 85, "bai": "Jordanésia"},
    {"cid": "Cajamar", "ocup": "Líder de Recebimento", "set": "Logística", "cls": "border-logistica", "sal": "3.800", "niv": "Médio/Técnico", "esc": "ETEC", "lnk": "https://www.cps.sp.gov.br/", "sld": 45, "bai": "Polvilho"},

    # CAIEIRAS
    {"cid": "Caieiras", "ocup": "Mecânico Industrial", "set": "Indústria", "cls": "border-industria", "sal": "4.500", "niv": "Médio/Técnico", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/", "sld": 28, "bai": "Vila Rosina"},
    {"cid": "Caieiras", "ocup": "Eletricista Industrial", "set": "Indústria", "cls": "border-industria", "sal": "4.200", "niv": "Médio/Técnico", "esc": "SENAI", "lnk": "https://sp.senai.br/", "sld": 19, "bai": "Laranjeiras"},
    {"cid": "Caieiras", "ocup": "Operador de Produção", "set": "Indústria", "cls": "border-industria", "sal": "2.800", "niv": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": 115, "bai": "Laranjeiras"},
    {"cid": "Caieiras", "ocup": "Ajudante de Carga", "set": "Logística", "cls": "border-logistica", "sal": "1.950", "niv": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": 204, "bai": "Centro"},
    {"cid": "Caieiras", "ocup": "Auxiliar Administrativo", "set": "Serviços", "cls": "border-servicos", "sal": "2.200", "niv": "Médio/Técnico", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/", "sld": 62, "bai": "Centro"}
]

# 5. FILTRO E GRÁFICO
cidade_sel = st.selectbox("📍 Selecione o Município:", ["Franco da Rocha", "Francisco Morato", "Cajamar", "Caieiras"])

st.markdown("### 📈 Tendência Regional: Saldo de Vagas")
df_plot = pd.DataFrame(data_list)
fig = px.bar(df_plot[df_plot['cid'] == cidade_sel], x="ocup", y="sld", labels={"sld": "Saldo", "ocup": "Ocupação"}, template="plotly_dark")
fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", height=300)
fig.update_traces(marker_color='#3b82f6')
st.plotly_chart(fig, use_container_width=True)

# 6. CARDS DINÂMICOS
st.write(f"#### Ocupações em {cidade_sel}")
for v in [x for x in data_list if x['cid'] == cidade_sel]:
    st.markdown(f"""
        <div class="card-vaga {v['cls']}">
            <div class="nivel-tag">Nível: {v['niv']}</div>
            <div class="titulo-vaga">{v['ocup']}</div>
            <div style="color:#94a3b8; font-size:0.8rem; margin-bottom:8px;">📍 Bairro: {v['bai']} | <b>Saldo: +{v['sld']} vagas</b></div>
            <div class="salario-valor">R$ {v['sal']}</div>
        </div>
        """, unsafe_allow_html=True)
    st.link_button(f"Qualificação Sugerida: {v['esc']}", v['lnk'], use_container_width=True)

# 7. TABELA GERAL AJUSTADA
st.divider()
st.markdown("### 📊 Panorama Geral (Novo CAGED Dezembro/2025)")
html_table = """<table class="dark-table"><thead><tr><th>Ocupação</th><th>Cidade</th><th>Saldo</th><th>Salário</th></tr></thead><tbody>"""
for i in data_list:
    html_table += f"<tr><td><b>{i['ocup']}</b><br><small>{i['niv']}</small></td><td>{i['cid']}</td><td class='pos-saldo'>+{i['sld']}</td><td style='color:#10b981; font-weight:bold;'>R$ {i['sal']}</td></tr>"
html_table += "</tbody></table>"
st.markdown(html_table, unsafe_allow_html=True)

# 8. NOTA TÉCNICA
st.markdown("---")
st.info("Fontes: Microdados PNADC 3T-2025 (IBGE) e Novo CAGED (Dezembro/2025).")
