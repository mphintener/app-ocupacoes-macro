import streamlit as st
import pandas as pd

# 1. Configuração de Estilo
st.set_page_config(page_title="Mercado de Trabalho e Qualificação", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117 !important; color: #ffffff !important; }
    
    .header-dark {
        background-color: #1a1d23;
        padding: 25px; border-radius: 12px; border: 1px solid #334155; margin-bottom: 25px;
    }

    .card-vaga {
        background-color: #1a1d23; padding: 20px; border-radius: 10px;
        margin-bottom: 12px; border-top: 1px solid #334155; box-shadow: 0 4px 6px rgba(0,0,0,0.4);
    }
    
    .border-logistica { border-left: 6px solid #3b82f6; }
    .border-industria { border-left: 6px solid #10b981; }
    .border-servicos { border-left: 6px solid #f59e0b; }
    .border-comercio { border-left: 6px solid #8b5cf6; }
    .border-saude { border-left: 6px solid #ef4444; }

    .titulo-vaga { font-size: 1.25rem; font-weight: bold; color: #ffffff; margin-bottom: 5px; }
    .nivel-tag { font-size: 0.7rem; font-weight: 800; padding: 2px 8px; border-radius: 4px; text-transform: uppercase; margin-bottom: 10px; display: inline-block; background-color: #334151; color: #94a3b8; }
    .salario-valor { font-size: 1.15rem; font-weight: bold; color: #10b981; }

    .dark-table {
        width: 100%; border-collapse: collapse; background-color: #111418; color: white; border-radius: 8px; overflow: hidden;
    }
    .dark-table th { background-color: #1e293b; padding: 12px; text-align: left; color: #94a3b8; font-size: 0.75rem; text-transform: uppercase; }
    .dark-table td { padding: 10px 12px; border-bottom: 1px solid #1e293b; font-size: 0.85rem; }
    </style>
    """, unsafe_allow_html=True)

# 2. Cabeçalho e Ajuda (O "?" para situar o público)
with st.expander("❓ Sobre este Painel (Clique para saber mais)"):
    st.write("""
        Este aplicativo foi desenvolvido para orientar cidadãos e gestores da Macrorregião de Franco da Rocha 
        sobre as reais oportunidades de emprego. Cruzamos dados de contratações do **Novo CAGED** com os 
        cursos oferecidos pelo **Centro Paula Souza (ETECs/FATECs)** e **Qualifica SP**, permitindo que você 
        encontre não apenas onde estão as vagas, mas onde se preparar para elas de acordo com seu nível de escolaridade.
    """)

st.markdown("""
    <div class="header-dark">
        <div style="font-size: 0.75rem; color: #64748b; letter-spacing: 1.5px; font-weight: bold;">📊 EIXO NORTE • MACRORREGIÃO DE FRANCO DA ROCHA</div>
        <h2 style="color: white; margin: 8px 0;">Mercado de Trabalho e Qualificação</h2>
        <div style="margin-top: 15px; padding-top: 15px; border-top: 1px solid #334155; display: flex; justify-content: space-between;">
            <div><small style="color: #94a3b8;">Renda Média Regional</small><br><b style="font-size: 1.3rem;">R$ 3.520,00</b></div>
            <div style="text-align: right;"><small style="color: #94a3b8;">Desocupação (PNADC 3T-2025)</small><br><b style="font-size: 1.3rem; color: #f87171;">7,8%</b></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 3. Base de Dados Completa (As 4 Cidades)
vagas_lista = [
    # CAJAMAR
    {"cid": "Cajamar", "ocup": "Analista de Logística", "set": "Logística", "cls": "border-logistica", "sal": "4.200", "bai": "Jordanésia", "nivel": "Superior", "esc": "FATEC", "lnk": "https://www.fatec.sp.gov.br/", "sld": "+142"},
    {"cid": "Cajamar", "ocup": "Conferente", "set": "Logística", "cls": "border-logistica", "sal": "2.600", "bai": "Polvilho", "nivel": "Médio", "esc": "ETEC", "lnk": "https://www.cps.sp.gov.br/", "sld": "+310"},
    {"cid": "Cajamar", "ocup": "Op. de Empilhadeira", "set": "Logística", "cls": "border-logistica", "sal": "2.900", "bai": "Jordanésia", "nivel": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": "+85"},
    {"cid": "Cajamar", "ocup": "Auxiliar de Logística", "set": "Logística", "cls": "border-logistica", "sal": "2.150", "bai": "Gato Preto", "nivel": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": "+520"},
    {"cid": "Cajamar", "ocup": "Líder de Recebimento", "set": "Logística", "cls": "border-logistica", "sal": "3.800", "bai": "Polvilho", "nivel": "Médio/Técnico", "esc": "ETEC", "lnk": "https://www.cps.sp.gov.br/", "sld": "+45"},
    
    # CAIEIRAS
    {"cid": "Caieiras", "ocup": "Mecânico Industrial", "set": "Indústria", "cls": "border-industria", "sal": "4.500", "bai": "Vila Rosina", "nivel": "Médio/Técnico", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/", "sld": "+28"},
    {"cid": "Caieiras", "ocup": "Eletricista Industrial", "set": "Indústria", "cls": "border-industria", "sal": "4.200", "bai": "Laranjeiras", "nivel": "Médio/Técnico", "esc": "SENAI", "lnk": "https://sp.senai.br/", "sld": "+19"},
    {"cid": "Caieiras", "ocup": "Operador de Produção", "set": "Indústria", "cls": "border-industria", "sal": "2.800", "bai": "Laranjeiras", "nivel": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": "+115"},
    {"cid": "Caieiras", "ocup": "Ajudante de Carga", "set": "Logística", "cls": "border-logistica", "sal": "1.950", "bai": "Centro", "nivel": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": "+204"},
    {"cid": "Caieiras", "ocup": "Auxiliar Administrativo", "set": "Serviços", "cls": "border-servicos", "sal": "2.200", "bai": "Centro", "nivel": "Médio", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/", "sld": "+62"},

    # FRANCO DA ROCHA
    {"cid": "Franco da Rocha", "ocup": "Enfermeiro", "set": "Saúde", "cls": "border-saude", "sal": "4.800", "bai": "Centro", "nivel": "Superior", "esc": "FATEC Franco", "lnk": "https://www.fatecfrancodarocha.edu.br/", "sld": "+12"},
    {"cid": "Franco da Rocha", "ocup": "Técnico de Enfermagem", "set": "Saúde", "cls": "border-saude", "sal": "3.450", "bai": "Pouso Alegre", "nivel": "Médio/Técnico", "esc": "ETEC Franco", "lnk": "https://www.cps.sp.gov.br/", "sld": "+45"},
    {"cid": "Franco da Rocha", "ocup": "Analista Administrativo", "set": "Serviços", "cls": "border-servicos", "sal": "3.100", "bai": "Centro", "nivel": "Superior", "esc": "FATEC Franco", "lnk": "https://www.fatecfrancodarocha.edu.br/", "sld": "+22"},
    {"cid": "Franco da Rocha", "ocup": "Vendedor", "set": "Comércio", "cls": "border-comercio", "sal": "2.050", "bai": "Centro", "nivel": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": "+89"},
    {"cid": "Franco da Rocha", "ocup": "Auxiliar Logístico", "set": "Logística", "cls": "border-logistica", "sal": "2.100", "bai": "Vila Rosalina", "nivel": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": "+134"},

    # FRANCISCO MORATO
    {"cid": "Francisco Morato", "ocup": "Gerente de Loja", "set": "Comércio", "cls": "border-comercio", "sal": "3.800", "bai": "Centro", "nivel": "Médio/Técnico", "esc": "ETEC Morato", "lnk": "http://etecfranciscomorato.com.br/", "sld": "+15"},
    {"cid": "Francisco Morato", "ocup": "Vendedor Especializado", "set": "Comércio", "cls": "border-comercio", "sal": "2.200", "bai": "Centro", "nivel": "Médio", "esc": "ETEC Morato", "lnk": "http://etecfranciscomorato.com.br/", "sld": "+56"},
    {"cid": "Francisco Morato", "ocup": "Operador de Caixa", "set": "Comércio", "cls": "border-comercio", "sal": "1.820", "bai": "Belém Capela", "nivel": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": "+112"},
    {"cid": "Francisco Morato", "ocup": "Assistente Logístico", "set": "Logística", "cls": "border-logistica", "sal": "2.450", "bai": "Nova Morato", "nivel": "Médio", "esc": "ETEC Morato", "lnk": "http://etecfranciscomorato.com.br/", "sld": "+42"},
    {"cid": "Francisco Morato", "ocup": "Estoquista", "set": "Logística", "cls": "border-logistica", "sal": "1.900", "bai": "Centro", "nivel": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/", "sld": "+78"}
]

# 4. Filtros
cidade_sel = st.selectbox("📍 Filtrar por Município:", ["Franco da Rocha", "Francisco Morato", "Cajamar", "Caieiras"])

# 5. Cards Dinâmicos
st.write(f"### Ocupações em Destaque: {cidade_sel}")
df_resumo = [v for v in vagas_lista if v['cid'] == cidade_sel]

if not df_resumo:
    st.warning("Dados desta cidade ainda não carregados.")
else:
    for v in df_resumo:
        st.markdown(f"""
            <div class="card-vaga {v['cls']}">
                <div class="nivel-tag">Nível: {v['nivel']}</div>
                <div class="titulo-vaga">{v['ocup']}</div>
                <div style="color:#94a3b8; font-size:0.85rem; margin-bottom:10px;">📍 Bairro: {v['bai']} | <b>Saldo: {v['sld']} vagas</b></div>
                <div class="salario-valor">R$ {v['sal']}</div>
            </div>
            """, unsafe_allow_html=True)
        st.link_button(f"Qualificação Sugerida: {v['esc']}", v['lnk'], use_container_width=True)

# 6. Tabela Geral de Saldos
st.divider()
st.markdown("### 📊 Panorama Geral de Saldos")
st.caption("Saldo Acumulado (Contratações - Desligamentos) | Novo CAGED Dezembro/2025")

html_table = """<table class="dark-table">
    <thead><tr><th>Ocupação</th><th>Cidade</th><th>Saldo</th><th>Salário</th></tr></thead>
    <tbody>"""
for i in vagas_lista:
    html_table += f"<tr><td><b>{i['ocup']}</b></td><td>{i['cid']}</td><td style='color:#60a5fa;'>{i['sld']}</td><td style='color:#10b981; font-weight:bold;'>R$ {i['sal']}</td></tr>"
html_table += "</tbody></table>"

st.markdown(html_table, unsafe_allow_html=True)

# 7. Nota Técnica
st.markdown("---")
st.info("Fontes: Microdados PNADC 3T de 2025 (IBGE) e Novo CAGED (Dezembro/2025).")

