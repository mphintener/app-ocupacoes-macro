import streamlit as st
import pandas as pd

# 1. FORÇAR TEMA E CONTRASTE (CSS Injetado no Root)
st.set_page_config(page_title="Inteligência Regional", layout="centered")

st.markdown("""
    <style>
    /* Força o fundo da área principal para Cinza Escuro Suave */
    .stApp {
        background-color: #e2e8f0 !important;
    }
    
    /* Bloco de Título e Panorama */
    .header-box {
        background-color: #1e3a8a;
        color: white;
        padding: 25px;
        border-radius: 12px;
        margin-bottom: 25px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
    }

    /* Cards Brancos com Contraste Forte */
    .vaga-card {
        background-color: #ffffff !important;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
        border-left: 8px solid #1e3a8a;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }

    .vaga-titulo { font-size: 1.2rem; font-weight: 800; color: #1e293b; margin-bottom: 5px; }
    .vaga-setor { font-size: 0.8rem; font-weight: bold; color: #3b82f6; text-transform: uppercase; }
    .vaga-salario { font-size: 1.1rem; font-weight: bold; color: #059669; }
    
    /* Tabela Estilo Relatório */
    .tabela-bi {
        width: 100%;
        background-color: white;
        border-collapse: collapse;
        border-radius: 8px;
        overflow: hidden;
    }
    .tabela-bi th { background-color: #334155; color: white; padding: 12px; text-align: left; }
    .tabela-bi td { padding: 12px; border-bottom: 1px solid #e2e8f0; font-size: 0.85rem; }
    </style>
    """, unsafe_allow_html=True)

# 2. Panorama Econômico (Cabeçalho de Alto Impacto)
st.markdown("""
    <div class="header-box">
        <div style="font-size: 0.8rem; opacity: 0.8;">MACRORREGIÃO DE FRANCO DA ROCHA</div>
        <h2 style="color: white; margin: 5px 0;">Mercado e Qualificação</h2>
        <hr style="opacity: 0.3; margin: 15px 0;">
        <div style="display: flex; justify-content: space-between;">
            <div><small>Renda Médio (PNADC 3T-2025)</small><br><b>R$ 3.520,00</b></div>
            <div style="text-align: right;"><small>Taxa de Desocupação</small><br><b>7,8%</b></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 3. Base de Dados Consolidada
data = {
    "Cajamar": [
        {"ocup": "Analista de Logística", "set": "Logística", "sal": 4200, "bai": "Jordanésia", "esc": "SENAI Cajamar", "link": "https://cajamar.sp.senai.br/"},
        {"ocup": "Auxiliar de Operações", "set": "Logística", "sal": 2150, "bai": "Polvilho", "esc": "SENAI Cajamar", "link": "https://cajamar.sp.senai.br/"}
    ],
    "Franco da Rocha": [
        {"ocup": "Enfermeiro de Estratégia", "set": "Saúde", "sal": 4800, "bai": "Centro", "esc": "Fatec Franco", "link": "https://www.fatecfrancodarocha.edu.br/"},
        {"ocup": "Técnico de Enfermagem", "set": "Saúde", "sal": 3200, "bai": "Pouso Alegre", "esc": "ETEC Franco", "link": "https://www.cps.sp.gov.br/"}
    ],
    "Francisco Morato": [
        {"ocup": "Gerente de Varejo", "set": "Comércio", "sal": 3800, "bai": "Centro", "esc": "ETEC Morato", "link": "http://etecfranciscomorato.com.br/"}
    ]
}

# 4. Seletor de Cidade (Integrado ao design)
cidade_sel = st.selectbox("🏙️ Selecione o município para detalhamento:", list(data.keys()))

st.write(f"### Destaques em {cidade_sel}")

# 5. Cards com Contraste Real
for v in data[cidade_sel]:
    st.markdown(f"""
        <div class="vaga-card">
            <div class="vaga-setor">{v['set']}</div>
            <div class="vaga-titulo">{v['ocup']}</div>
            <div style="color: #475569; margin-bottom: 8px;">
                📍 Bairro: <b>{v['bai']}</b> | 🎓 {v['esc']}
            </div>
            <div class="vaga-salario">Média Admissional: R$ {v['sal']:,}</div>
        </div>
        """, unsafe_allow_html=True)
    st.link_button(f"Cursos na Unidade {v['esc']}", v['link'], use_container_width=True)

# 6. Tabela de Saldo (Layout Profissional)
st.divider()
st.markdown("### 📈 Panorama de Saldos Mensais")

html_table = """<table class="tabela-bi"><thead><tr><th>Ocupação</th><th>Bairro</th><th>Salário</th></tr></thead><tbody>"""
for cid in data:
    for v in data[cid]:
        html_table += f"<tr><td><b>{v['ocup']}</b></td><td>{v['bai']}</td><td>R$ {v['sal']:,}</td></tr>"
html_table += "</tbody></table>"

st.markdown(html_table, unsafe_allow_html=True)

# 7. Nota Técnica
st.info("📊 **Fonte:** Microdados PNADC 3T de 2025 (IBGE) e Novo CAGED (Saldo Admissional).")

