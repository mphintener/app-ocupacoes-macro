import streamlit as st
import pandas as pd

# 1. CSS MASTER (Mantendo o visual Dark que funcionou)
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

# 2. Cabeçalho Regional
st.markdown("""
    <div class="header-dark">
        <div style="font-size: 0.75rem; color: #64748b; letter-spacing: 1.5px; font-weight: bold;">📊 EIXO NORTE • MACRORREGIÃO DE FRANCO DA ROCHA</div>
        <h2 style="color: white; margin: 8px 0;">Mercado de Trabalho e Qualificação</h2>
        <div style="margin-top: 15px; padding-top: 15px; border-top: 1px solid #334155; display: flex; justify-content: space-between;">
            <div><small style="color: #94a3b8;">Renda Média (Média Regional)</small><br><b style="font-size: 1.3rem;">R$ 3.520,00</b></div>
            <div style="text-align: right;"><small style="color: #94a3b8;">Desocupação (PNADC 3T-2025)</small><br><b style="font-size: 1.3rem; color: #f87171;">7,8%</b></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 3. Base de Dados Refinada por Nível de Ensino
vagas_lista = [
    # FRANCO DA ROCHA
    {"cid": "Franco da Rocha", "ocup": "Enfermeiro de Estratégia", "set": "Saúde", "cls": "border-saude", "sal": "4.800", "bai": "Centro", "nivel": "Superior", "esc": "FATEC Franco", "lnk": "https://www.fatecfrancodarocha.edu.br/"},
    {"cid": "Franco da Rocha", "ocup": "Técnico de Enfermagem", "set": "Saúde", "cls": "border-saude", "sal": "3.450", "bai": "Pouso Alegre", "nivel": "Médio/Técnico", "esc": "ETEC Franco", "lnk": "https://www.cps.sp.gov.br/"},
    {"cid": "Franco da Rocha", "ocup": "Auxiliar Administrativo", "set": "Serviços", "cls": "border-servicos", "sal": "2.100", "bai": "Centro", "nivel": "Médio", "esc": "ETEC Franco", "lnk": "https://www.cps.sp.gov.br/"},
    {"cid": "Franco da Rocha", "ocup": "Operador de Logística", "set": "Logística", "cls": "border-logistica", "sal": "1.950", "bai": "Polo Industrial", "nivel": "Básico/Formação Rápida", "esc": "Qualifica SP / Via Rápida", "lnk": "https://www.cursosviarapida.sp.gov.br/"},
    {"cid": "Franco da Rocha", "ocup": "Recepcionista", "set": "Serviços", "cls": "border-servicos", "sal": "1.850", "bai": "Vila Rosalina", "nivel": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/"},
    
    # FRANCISCO MORATO
    {"cid": "Francisco Morato", "ocup": "Gerente de Loja", "set": "Comércio", "cls": "border-comercio", "sal": "3.800", "bai": "Centro", "nivel": "Médio/Técnico", "esc": "ETEC Morato", "lnk": "http://etecfranciscomorato.com.br/"},
    {"cid": "Francisco Morato", "ocup": "Vendedor Especializado", "set": "Comércio", "cls": "border-comercio", "sal": "2.200", "bai": "Belém Capela", "nivel": "Médio", "esc": "ETEC Morato", "lnk": "http://etecfranciscomorato.com.br/"},
    {"cid": "Francisco Morato", "ocup": "Operador de Caixa", "set": "Comércio", "cls": "border-comercio", "sal": "1.820", "bai": "Vila Guilherme", "nivel": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/"},
    {"cid": "Francisco Morato", "ocup": "Estoquista", "set": "Logística", "cls": "border-logistica", "sal": "1.900", "bai": "Centro", "nivel": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/"},
    {"cid": "Francisco Morato", "ocup": "Auxiliar de Estoque", "set": "Logística", "cls": "border-logistica", "sal": "1.750", "bai": "Nova Morato", "nivel": "Básico", "esc": "Qualifica SP", "lnk": "https://www.qualificasp.sp.gov.br/"},
    # (Dados de Cajamar e Caieiras seguindo a mesma lógica...)
]

# 4. Filtro por Cidade
cidade_sel = st.selectbox("📍 Filtrar por Município:", ["Franco da Rocha", "Francisco Morato", "Cajamar", "Caieiras"])

# 5. Cards Dinâmicos com Nível de Ensino
st.write(f"### Ocupações em Destaque: {cidade_sel}")
df_resumo = [v for v in vagas_lista if v['cid'] == cidade_sel]

for v in df_resumo:
    st.markdown(f"""
        <div class="card-vaga {v['cls']}">
            <div class="nivel-tag">Nível: {v['nivel']}</div>
            <div class="titulo-vaga">{v['ocup']}</div>
            <div style="color:#94a3b8; font-size:0.85rem; margin-bottom:10px;">📍 Bairro: {v['bai']} | Unidade: {v['esc']}</div>
            <div class="salario-valor">R$ {v['sal']}</div>
        </div>
        """, unsafe_allow_html=True)
    st.link_button(f"Qualificação Sugerida: {v['esc']}", v['lnk'], use_container_width=True)

# 6. Tabela de BI com Referência Temporal
st.divider()
st.markdown("### 📊 Panorama Geral de Ocupações")
st.caption("Dados de saldo baseados no Novo CAGED - Dezembro/2025")

html_table = """<table class="dark-table">
    <thead><tr><th>Ocupação</th><th>Nível</th><th>Cidade</th><th>Salário</th></tr></thead>
    <tbody>"""
for i in vagas_lista:
    html_table += f"<tr><td><b>{i['ocup']}</b></td><td>{i['nivel']}</td><td>{i['cid']}</td><td style='color:#10b981; font-weight:bold;'>R$ {i['sal']}</td></tr>"
html_table += "</tbody></table>"

st.markdown(html_table, unsafe_allow_html=True)

# 7. Nota Técnica
st.markdown("---")
st.info("Fontes: Microdados PNADC 3T de 2025 (IBGE) e Novo CAGED (Dezembro/2025).")

