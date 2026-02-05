import streamlit as st
import pandas as pd

# 1. CSS de Alta Fidelidade e Contraste
st.set_page_config(page_title="Macrorregião de Franco da Rocha", layout="centered")

st.markdown("""
    <style>
    /* Reset de fundo para evitar folha branca sobreposta */
    .stApp {
        background-color: #f8fafc !important;
    }
    
    /* Header Profissional */
    .header-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 25px;
    }

    /* Cards de Ocupação Brancos com Sombra Suave */
    .vaga-card {
        background-color: #ffffff !important;
        padding: 18px;
        border-radius: 10px;
        margin-bottom: 12px;
        border-left: 6px solid #1e3a8a;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .vaga-titulo { font-size: 1.1rem; font-weight: 800; color: #1e293b; margin: 0; }
    .vaga-sub { font-size: 0.8rem; color: #64748b; font-weight: 600; text-transform: uppercase; }
    .vaga-salario { font-size: 1rem; font-weight: bold; color: #059669; margin-top: 5px; }
    
    /* Estilo da Tabela para não ser encoberta */
    div[data-testid="stExpander"] {
        background-color: white !important;
        border-radius: 8px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Panorama Macrorregional (Clarificando que é Média da Região)
st.markdown("""
    <div class="header-box">
        <h2 style="color: #1e3a8a; margin-top: 0;">💼 Mercado e Qualificação</h2>
        <p style="color: #475569; font-size: 0.9rem; margin-bottom: 15px;">
            <b>Indicadores da Macrorregião de Franco da Rocha</b><br>
            <i>Valores médios calculados para o conjunto dos municípios da região.</i>
        </p>
        <div style="display: flex; justify-content: space-between; border-top: 1px solid #f1f5f9; padding-top: 15px;">
            <div><small>Renda Média (PNADC 3T-2025)</small><br><b style="font-size: 1.1rem;">R$ 3.520,00</b></div>
            <div style="text-align: right;"><small>Taxa de Desocupação</small><br><b style="font-size: 1.1rem; color: #ef4444;">7,8%</b></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 3. Dados (4 Cidades | 5 Ocupações)
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
        {"ocup": "Vendedor", "set": "Comércio", "sal": 1900, "bai": "Vila Guilherme", "esc": "ETEC Morato", "lnk": "http://etecfranciscomorato.com.br/"},
        {"ocup": "Assistente Logístico", "set": "Logística", "sal": 2450, "bai": "Centro", "esc": "ETEC Morato", "lnk": "http://etecfranciscomorato.com.br/"},
        {"ocup": "Estoquista", "set": "Logística", "sal": 1900, "bai": "Nova Morato", "esc": "ETEC Morato", "lnk": "http://etecfranciscomorato.com.br/"}
    ]
}

# 4. Filtro por Cidade
cidade_sel = st.selectbox("📍 Selecione a Cidade:", list(data.keys()))

st.write(f"### Top 5 Ocupações em {cidade_sel}")

# 5. Cards de Ocupação
for v in data[cidade_sel]:
    st.markdown(f"""
        <div class="vaga-card">
            <div class="vaga-sub">{v['set']} | Bairro: {v['bai']}</div>
            <div class="vaga-titulo">{v['ocup']}</div>
            <div class="vaga-salario">Média: R$ {v['sal']:,}</div>
        </div>
        """, unsafe_allow_html=True)
    st.link_button(f"Qualificação na Unidade {v['esc']}", v['lnk'], use_container_width=True)

# 6. Tabela Panorâmica (Protegida por Expander para não ficar comprida)
st.write("---")
with st.expander("📊 Ver Tabela Geral de Saldos da Região"):
    st.write("Dados consolidados por ocupação e município:")
    tabela_lista = []
    for c, lista in data.items():
        for o in lista:
            tabela_lista.append({"Ocupação": o['ocup'], "Cidade": c, "Salário": o['sal']})
    st.dataframe(pd.DataFrame(tabela_lista), use_container_width=True, hide_index=True)

# 7. Nota Técnica
st.caption("Fontes: Microdados PNADC 3T de 2025 (IBGE) e Novo CAGED.")

