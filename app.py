import streamlit as st
import pandas as pd

# 1. CSS BLINDADO (Forçando contraste e transparência de camadas brancas)
st.set_page_config(page_title="Macrorregião de Franco da Rocha", layout="centered")

st.markdown("""
    <style>
    /* Força o fundo da página e remove camadas brancas fantasmas */
    .stApp, .st-emotion-cache-16idsys, .st-emotion-cache-z5fcl4 {
        background-color: #f1f5f9 !important;
    }
    
    /* Header Azul Profundo */
    .header-box {
        background-color: #1e3a8a;
        color: white;
        padding: 25px;
        border-radius: 12px;
        margin-bottom: 25px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }

    /* Cards Brancos com Sombra */
    .vaga-card {
        background-color: #ffffff !important;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 12px;
        border-left: 8px solid #3b82f6;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .vaga-titulo { font-size: 1.2rem; font-weight: 800; color: #1e293b; margin: 0; }
    .vaga-meta { font-size: 0.8rem; font-weight: bold; color: #64748b; text-transform: uppercase; }
    .vaga-salario { font-size: 1.1rem; font-weight: bold; color: #059669; margin-top: 8px; }
    
    /* Tabela em HTML Puro para não ser encoberta */
    .html-table {
        width: 100%;
        border-collapse: collapse;
        background-color: white;
        border-radius: 8px;
        overflow: hidden;
        margin-top: 20px;
    }
    .html-table th { background-color: #334155; color: white; padding: 12px; text-align: left; }
    .html-table td { padding: 12px; border-bottom: 1px solid #e2e8f0; color: #334155; }
    </style>
    """, unsafe_allow_html=True)

# 2. Cabeçalho PNADC (3T-2025)
st.markdown("""
    <div class="header-box">
        <div style="font-size: 0.8rem; opacity: 0.8;">MACRORREGIÃO DE FRANCO DA ROCHA</div>
        <h2 style="color: white; margin: 5px 0;">Mercado e Qualificação</h2>
        <div style="margin-top: 15px; display: flex; justify-content: space-between; border-top: 1px solid rgba(255,255,255,0.2); padding-top: 15px;">
            <div><small>Renda Média (Microdados PNADC 3T-2025)</small><br><b>R$ 3.520,00</b></div>
            <div style="text-align: right;"><small>Taxa de Desocupação</small><br><b>7,8%</b></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 3. Base de Dados Completa (4 Cidades x 5 Ocupações)
data = {
    "Cajamar": [
        {"ocup": "Analista de Logística", "set": "Logística", "sal": 4200, "bai": "Jordanésia", "esc": "SENAI Cajamar", "lnk": "https://cajamar.sp.senai.br/"},
        {"ocup": "Auxiliar Logístico", "set": "Logística", "sal": 2150, "bai": "Polvilho", "esc": "SENAI Cajamar", "lnk": "https://cajamar.sp.senai.br/"},
        {"ocup": "Conferente", "set": "Logística", "sal": 2600, "bai": "Gato Preto", "esc": "SENAI Cajamar", "lnk": "https://cajamar.sp.senai.br/"},
        {"ocup": "Op. de Empilhadeira", "set": "Logística", "sal": 2900, "bai": "Jordanésia", "esc": "SENAI Cajamar", "lnk": "https://cajamar.sp.senai.br/"},
        {"ocup": "Líder de Logística", "set": "Logística", "sal": 3800, "bai": "Polvilho", "esc": "SENAI Cajamar", "lnk": "https://cajamar.sp.senai.br/"}
    ],
    "Caieiras": [
        {"ocup": "Operador de Produção", "set": "Indústria", "sal": 2800, "bai": "Laranjeiras", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/"},
        {"ocup": "Mecânico Industrial", "set": "Indústria", "sal": 4500, "bai": "Vila Rosina", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/"},
        {"ocup": "Ajudante de Carga", "set": "Logística", "sal": 1950, "bai": "Laranjeiras", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/"},
        {"ocup": "Eletricista Industrial", "set": "Indústria", "sal": 4200, "bai": "Laranjeiras", "esc": "SENAI", "lnk": "https://www.cps.sp.gov.br/"},
        {"ocup": "Auxiliar Administrativo", "set": "Serviços", "sal": 2200, "bai": "Centro", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/"}
    ],
    "Franco da Rocha": [
        {"ocup": "Técnico de Enfermagem", "set": "Saúde", "sal": 3450, "bai": "Centro", "esc": "ETEC Franco", "lnk": "https://www.cps.sp.gov.br/"},
        {"ocup": "Analista Administrativo", "set": "Serviços", "sal": 3100, "bai": "Vila Rosalina", "esc": "Fatec Franco", "lnk": "https://www.fatecfrancodarocha.edu.br/"},
        {"ocup": "Vendedor", "set": "Comércio", "sal": 2050, "bai": "Centro", "esc": "ETEC Franco", "lnk": "https://www.cps.sp.gov.br/"},
        {"ocup": "Auxiliar Logístico", "set": "Transportes", "sal": 2100, "bai": "Pouso Alegre", "esc": "ETEC Franco", "lnk": "https://www.cps.sp.gov.br/"},
        {"ocup": "Recepcionista", "set": "Serviços", "sal": 1850, "bai": "Centro", "esc": "ETEC Franco", "lnk": "https://www.cps.sp.gov.br/"}
    ],
    "Francisco Morato": [
        {"ocup": "Gerente de Loja", "set": "Comércio", "sal": 3800, "bai": "Centro", "esc": "ETEC Morato", "lnk": "http://etecfranciscomorato.com.br/"},
        {"ocup": "Operador de Caixa", "set": "Comércio", "sal": 1820, "bai": "Belém Capela", "esc": "ETEC Morato", "lnk": "http://etecfranciscomorato.com.br/"},
        {"ocup": "Vendedor", "set": "Comércio", "sal": 1900, "bai": "Vila Guilherme", "esc": "ETEC Morato", "lnk": "http://etecfranciscomorato.com.br/"},
        {"ocup": "Assistente Logístico", "set": "Logística", "sal": 2450, "bai": "Nova Morato", "esc": "ETEC Morato", "lnk": "http://etecfranciscomorato.com.br/"},
        {"ocup": "Estoquista", "set": "Logística", "sal": 1900, "bai": "Centro", "esc": "ETEC Morato", "lnk": "http://etecfranciscomorato.com.br/"}
    ]
}

# 4. Filtro e Exibição
cidade_sel = st.selectbox("📍 Selecione o Município:", list(data.keys()))

st.write(f"### Top 5 Ocupações em {cidade_sel}")

for v in data[cidade_sel]:
    st.markdown(f"""
        <div class="vaga-card">
            <div class="vaga-meta">{v['set']} | Bairro: {v['bai']}</div>
            <div class="vaga-titulo">{v['ocup']}</div>
            <div class="vaga-salario">Salário Médio: R$ {v['sal']:,}</div>
        </div>
        """, unsafe_allow_html=True)
    st.link_button(f"Qualificação Sugerida: {v['esc']}", v['lnk'], use_container_width=True)

# 5. TABELA BLINDADA (HTML Puro)
st.divider()
st.markdown("### 📊 Panorama de Saldos Mensais")

tabela_html = """<table class="html-table">
    <thead><tr><th>Ocupação</th><th>Cidade</th><th>Salário</th></tr></thead>
    <tbody>"""

# Gerando linhas para as 4 cidades
for cid, lista in data.items():
    for item in lista:
        tabela_html += f"<tr><td><b>{item['ocup']}</b></td><td>{cid}</td><td>R$ {item['sal']:,}</td></tr>"

tabela_html += "</tbody></table>"

st.markdown(tabela_html, unsafe_allow_html=True)

# 6. Rodapé Técnico
st.markdown("---")
st.caption("Fontes: Microdados PNADC 3T de 2025 (IBGE) e Novo CAGED (Mês Atual).")

