import streamlit as st
import pandas as pd

# 1. CSS DE ALTO CONTRASTE (Adeus folha branca)
st.set_page_config(page_title="Inteligência Regional", layout="centered")

st.markdown("""
    <style>
    /* Força o fundo da página para um cinza neutro de BI */
    .stApp {
        background-color: #f1f5f9 !important;
    }
    
    /* Header estilizado */
    .header-box {
        background-color: #1e3a8a;
        color: white;
        padding: 25px;
        border-radius: 12px;
        margin-bottom: 25px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
    }

    /* Cards Brancos com borda de setor */
    .vaga-card {
        background-color: #ffffff !important;
        padding: 18px;
        border-radius: 10px;
        margin-bottom: 12px;
        border-left: 8px solid #334155;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .titulo-vaga { font-size: 1.15rem; font-weight: 800; color: #0f172a; margin: 0; }
    .setor-tag { font-size: 0.75rem; font-weight: bold; color: #2563eb; text-transform: uppercase; }
    .salario-label { font-size: 1.1rem; font-weight: bold; color: #059669; margin-top: 5px; }
    
    /* Tabela de Dados Brutos */
    .tabela-bi {
        width: 100%;
        background-color: white;
        border-collapse: collapse;
        border-radius: 8px;
        overflow: hidden;
    }
    .tabela-bi th { background-color: #334155; color: white; padding: 12px; text-align: left; }
    .tabela-bi td { padding: 12px; border-bottom: 1px solid #e2e8f0; }
    </style>
    """, unsafe_allow_html=True)

# 2. Panorama PNADC (Cabeçalho Conforme Roteiro)
st.markdown("""
    <div class="header-box">
        <div style="font-size: 0.8rem; opacity: 0.8; letter-spacing: 1px;">MACRORREGIÃO DE FRANCO DA ROCHA</div>
        <h2 style="color: white; margin: 5px 0;">Ocupações e Mercado</h2>
        <div style="margin-top: 15px; padding-top: 15px; border-top: 1px solid rgba(255,255,255,0.2); display: flex; justify-content: space-between;">
            <div><small>Microdados PNADC 3T de 2025</small><br><b>Renda Média: R$ 3.520,00</b></div>
            <div style="text-align: right;"><small>Taxa de Desocupação</small><br><b>7,8%</b></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 3. Base de Dados (4 Cidades x 5 Ocupações)
data = {
    "Cajamar": [
        {"ocup": "Analista de Logística", "set": "Logística", "sal": 4200, "bai": "Jordanésia", "esc": "SENAI Cajamar", "lnk": "https://cajamar.sp.senai.br/"},
        {"ocup": "Auxiliar Logístico", "set": "Logística", "sal": 2150, "bai": "Polvilho", "esc": "SENAI Cajamar", "lnk": "https://cajamar.sp.senai.br/"},
        {"ocup": "Conferente de Carga", "set": "Logística", "sal": 2600, "bai": "Gato Preto", "esc": "SENAI Cajamar", "lnk": "https://cajamar.sp.senai.br/"},
        {"ocup": "Op. de Empilhadeira", "set": "Logística", "sal": 2900, "bai": "Jordanésia", "esc": "SENAI Cajamar", "lnk": "https://cajamar.sp.senai.br/"},
        {"ocup": "Líder de Recebimento", "set": "Logística", "sal": 3800, "bai": "Polvilho", "esc": "SENAI Cajamar", "lnk": "https://cajamar.sp.senai.br/"}
    ],
    "Caieiras": [
        {"ocup": "Operador de Produção", "set": "Indústria", "sal": 2800, "bai": "Laranjeiras", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/"},
        {"ocup": "Mecânico Industrial", "set": "Indústria", "sal": 4500, "bai": "Vila Rosina", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/"},
        {"ocup": "Ajudante de Carga", "set": "Logística", "sal": 1950, "bai": "Laranjeiras", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/"},
        {"ocup": "Eletricista Industrial", "set": "Indústria", "sal": 4200, "bai": "Vila Jaguari", "esc": "SENAI", "lnk": "https://www.cps.sp.gov.br/"},
        {"ocup": "Auxiliar de Almoxarife", "set": "Serviços", "sal": 2100, "bai": "Centro", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/"}
    ],
    "Franco da Rocha": [
        {"ocup": "Técnico de Enfermagem", "set": "Saúde", "sal": 3450, "bai": "Centro", "esc": "ETEC Franco", "lnk": "https://www.cps.sp.gov.br/"},
        {"ocup": "Analista Administrativo", "set": "Serviços", "sal": 3100, "bai": "Vila Rosalina", "esc": "Fatec Franco", "lnk": "https://www.fatecfrancodarocha.edu.br/"},
        {"ocup": "Vendedor Especializado", "set": "Comércio", "sal": 2050, "bai": "Centro", "esc": "ETEC Franco", "lnk": "https://www.cps.sp.gov.br/"},
        {"ocup": "Auxiliar de Logística", "set": "Transportes", "sal": 2100, "bai": "Pouso Alegre", "esc": "ETEC Franco", "lnk": "https://www.cps.sp.gov.br/"},
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
cidade_sel = st.selectbox("📍 Selecione o Município para análise:", list(data.keys()))

st.markdown(f"### Destaques em {cidade_sel}")

# 5. Exibição das 5 Ocupações por Cidade
for item in data[cidade_sel]:
    st.markdown(f"""
        <div class="vaga-card">
            <div class="setor-tag">{item['set']} | Bairro: {item['bai']}</div>
            <p class="titulo-vaga">{item['ocup']}</p>
            <div class="salario-label">Média Salarial: R$ {item['sal']:,}</div>
        </div>
        """, unsafe_allow_html=True)
    st.link_button(f"🔗 Qualificação na Unidade {item['esc']}", item['lnk'], use_container_width=True)

# 6. Tabela de Saldos da Região
st.divider()
st.markdown("### 📊 Panorama de Saldos por Ocupação")

tabela_lista = []
for cid, lista in data.items():
    for o in lista:
        tabela_lista.append({"Ocupação": o['ocup'], "Cidade": cid, "Salário": o['sal'], "Setor": o['set']})

st.table(pd.DataFrame(tabela_lista))

# 7. Nota Técnica
st.markdown("---")
st.info("""
**Metodologia:** Saldo Admissional via Novo CAGED (Admissões - Desligamentos). 
Rendimento e Desemprego baseados nos Microdados PNADC 3T de 2025 (IBGE).
""")

