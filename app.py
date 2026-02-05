import streamlit as st
import pandas as pd

# 1. CSS BLACK MODE (Elimina folha branca e restaura o visual de ontem)
st.set_page_config(page_title="Macrorregião de Franco da Rocha", layout="centered")

st.markdown("""
    <style>
    /* Força Fundo Preto em toda a aplicação */
    .stApp {
        background-color: #0e1117 !important;
        color: #ffffff !important;
    }
    
    /* Header Estilo Dashboard de Inteligência */
    .header-dark {
        background-color: #1f2937;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #374151;
        margin-bottom: 25px;
    }

    /* Cards de Ocupação - Estilo Glassmorphism */
    .card-vaga {
        background-color: #1a1d23 !important;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
        border-left: 6px solid #3b82f6;
        border-top: 1px solid #374151;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    
    .vaga-titulo { font-size: 1.2rem; font-weight: bold; color: #ffffff; margin-bottom: 5px; }
    .vaga-setor { font-size: 0.8rem; font-weight: bold; color: #60a5fa; text-transform: uppercase; }
    .vaga-salario { font-size: 1.1rem; font-weight: bold; color: #10b981; }
    
    /* Tabela Customizada para o Dark Mode */
    .dark-table {
        width: 100%;
        border-collapse: collapse;
        background-color: #1a1d23;
        color: white;
        border-radius: 8px;
        overflow: hidden;
    }
    .dark-table th { background-color: #374151; padding: 12px; text-align: left; color: #9ca3af; }
    .dark-table td { padding: 12px; border-bottom: 1px solid #374151; }
    </style>
    """, unsafe_allow_html=True)

# 2. Panorama Macrorregional (Dados PNADC 3T-2025)
st.markdown("""
    <div class="header-dark">
        <div style="font-size: 0.8rem; color: #9ca3af; letter-spacing: 1px;">MACRORREGIÃO DE FRANCO DA ROCHA</div>
        <h2 style="color: white; margin: 5px 0;">Mercado e Qualificação</h2>
        <div style="margin-top: 15px; padding-top: 15px; border-top: 1px solid #374151; display: flex; justify-content: space-between;">
            <div>
                <small style="color: #9ca3af;">Média Regional (PNADC 3T-2025)</small><br>
                <b style="font-size: 1.2rem;">R$ 3.520,00</b>
            </div>
            <div style="text-align: right;">
                <small style="color: #9ca3af;">Taxa Desocupação Regional</small><br>
                <b style="font-size: 1.2rem; color: #f87171;">7,8%</b>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 3. Base de Dados (4 Cidades | 5 Ocupações)
data = {
    "Cajamar": [
        {"ocup": "Analista de Logística", "set": "Logística", "sal": 4200, "bai": "Jordanésia", "esc": "SENAI Cajamar", "lnk": "https://cajamar.sp.senai.br/"},
        {"ocup": "Auxiliar Logístico", "set": "Logística", "sal": 2150, "bai": "Polvilho", "esc": "SENAI Cajamar", "lnk": "https://cajamar.sp.senai.br/"},
        {"ocup": "Conferente", "set": "Logística", "sal": 2600, "bai": "Gato Preto", "esc": "SENAI Cajamar", "lnk": "https://cajamar.sp.senai.br/"},
        {"ocup": "Operador de Empilhadeira", "set": "Logística", "sal": 2900, "bai": "Jordanésia", "esc": "SENAI Cajamar", "lnk": "https://cajamar.sp.senai.br/"},
        {"ocup": "Líder de Recebimento", "set": "Logística", "sal": 3800, "bai": "Polvilho", "esc": "SENAI Cajamar", "lnk": "https://cajamar.sp.senai.br/"}
    ],
    "Caieiras": [
        {"ocup": "Operador de Produção", "set": "Indústria", "sal": 2800, "bai": "Laranjeiras", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/"},
        {"ocup": "Mecânico Industrial", "set": "Indústria", "sal": 4500, "bai": "Vila Rosina", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/"},
        {"ocup": "Ajudante de Carga", "set": "Logística", "sal": 1950, "bai": "Laranjeiras", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/"},
        {"ocup": "Eletricista Industrial", "set": "Indústria", "sal": 4200, "bai": "Vila Jaguari", "esc": "SENAI", "lnk": "https://www.cps.sp.gov.br/"},
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
        {"ocup": "Vendedor de Varejo", "set": "Comércio", "sal": 1900, "bai": "Vila Guilherme", "esc": "ETEC Morato", "lnk": "http://etecfranciscomorato.com.br/"},
        {"ocup": "Assistente Logístico", "set": "Logística", "sal": 2450, "bai": "Centro", "esc": "ETEC Morato", "lnk": "http://etecfranciscomorato.com.br/"},
        {"ocup": "Estoquista", "set": "Logística", "sal": 1900, "bai": "Nova Morato", "esc": "ETEC Morato", "lnk": "http://etecfranciscomorato.com.br/"}
    ]
}

# 4. Filtro por Cidade
cidade_sel = st.selectbox("📍 Selecione o Município:", list(data.keys()))

st.markdown(f"### Top 5 Ocupações: {cidade_sel}")

# 5. Cards de Ocupação (Contraste Neon sobre Preto)
for v in data[cidade_sel]:
    st.markdown(f"""
        <div class="card-vaga">
            <div class="vaga-setor">{v['set']} | Bairro: {v['bai']}</div>
            <div class="vaga-titulo">{v['ocup']}</div>
            <div class="vaga-salario">Salário Médio: R$ {v['sal']:,}</div>
        </div>
        """, unsafe_allow_html=True)
    st.link_button(f"🔗 Qualificação: {v['esc']}", v['lnk'], use_container_width=True)

# 6. Tabela Panorâmica (Blindada contra folha branca)
st.divider()
st.markdown("### 📊 Tabela Geral de Saldos da Macrorregião")

html_table = """<table class="dark-table">
    <thead><tr><th>Ocupação</th><th>Cidade</th><th>Salário</th></tr></thead>
    <tbody>"""
for cid, lista in data.items():
    for item in lista:
        html_table += f"<tr><td><b>{item['ocup']}</b></td><td>{cid}</td><td>R$ {item['sal']:,}</td></tr>"
html_table += "</tbody></table>"

st.markdown(html_table, unsafe_allow_html=True)

# 7. Nota Técnica
st.markdown("---")
st.caption("Fontes: Microdados PNADC 3T de 2025 (IBGE) e Novo CAGED.")

