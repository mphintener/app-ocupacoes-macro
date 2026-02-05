import streamlit as st
import pandas as pd

# 1. CSS de Alta Fidelidade (Fundo Cinza Neutro + Cards Brancos)
st.set_page_config(page_title="Macrorregião de Franco da Rocha", layout="centered")

st.markdown("""
    <style>
    /* Fundo da página em cinza claro para destacar os cards brancos */
    .stApp { background-color: #f1f5f9; }
    
    html, body, [class*="css"] { font-size: 13px !important; color: #1e293b; }
    
    /* Panorama Superior Estilizado */
    .panorama-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        border-top: 4px solid #1e3a8a;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 25px;
    }

    /* Card de Ocupação com profundidade e cores por setor */
    .vaga-container {
        background-color: #ffffff;
        padding: 18px;
        border-radius: 10px;
        margin-bottom: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border-right: 4px solid #cbd5e1; /* Borda padrão */
    }
    .setor-logistica { border-right: 6px solid #1e3a8a; }
    .setor-industria { border-right: 6px solid #059669; }
    .setor-servicos { border-right: 6px solid #d97706; }
    .setor-comercio { border-right: 6px solid #7c3aed; }

    .job-title { font-size: 1.15rem; font-weight: 800; color: #0f172a; margin-bottom: 5px; }
    .label-setor { font-size: 0.75rem; font-weight: bold; text-transform: uppercase; color: #64748b; }
    .salary-value { font-size: 1.1rem; font-weight: bold; color: #059669; }
    
    /* Tabela de BI */
    .styled-table {
        width: 100%; border-collapse: collapse; background: white;
        border-radius: 8px; overflow: hidden;
    }
    .styled-table th { background: #1e3a8a; color: white; padding: 12px; text-align: left; }
    .styled-table td { padding: 12px; border-bottom: 1px solid #e2e8f0; }
    </style>
    """, unsafe_allow_html=True)

# 2. Título e Panorama PNADC (Conforme Roteiro)
st.markdown("<h2 style='color: #1e3a8a; text-align:center;'>💼 Inteligência de Mercado</h2>", unsafe_allow_html=True)

st.markdown("""
    <div class="panorama-card">
        <div style='color: #64748b; font-weight: bold; font-size: 0.8rem; margin-bottom: 8px;'>MACRORREGIÃO DE FRANCO DA ROCHA</div>
        <div style='display: flex; justify-content: space-between; align-items: center;'>
            <div>
                <small>Microdados PNADC 3T de 2025</small><br>
                <b>Renda Média: R$ 3.520,00</b>
            </div>
            <div style='text-align: right;'>
                <small>Taxa de Desemprego</small><br>
                <b style='color: #ef4444;'>7,8%</b>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 3. Base de Dados Consolidada (Cajamar, Caieiras, Franco, Morato)
vagas = [
    {"cid": "Cajamar", "ocup": "Analista de Logística", "set": "Logística", "css": "setor-logistica", "sal": 4200, "esc": "Superior", "bai": "Jordanésia", "link": "https://cajamar.sp.senai.br/"},
    {"cid": "Cajamar", "ocup": "Auxiliar de Operações", "set": "Logística", "css": "setor-logistica", "sal": 2150, "esc": "Médio", "bai": "Polvilho", "link": "https://cajamar.sp.senai.br/"},
    {"cid": "Caieiras", "ocup": "Operador de Produção", "set": "Indústria", "css": "setor-industria", "sal": 2800, "esc": "Médio", "bai": "Laranjeiras", "link": "https://www.cps.sp.gov.br/"},
    {"cid": "Franco da Rocha", "ocup": "Enfermeiro", "set": "Serviços", "css": "setor-servicos", "sal": 4800, "esc": "Superior", "bai": "Centro", "link": "https://www.fatecfrancodarocha.edu.br/"},
    {"cid": "Francisco Morato", "ocup": "Gerente de Loja", "set": "Comércio", "css": "setor-comercio", "sal": 3800, "esc": "Médio", "bai": "Centro", "link": "http://etecfranciscomorato.com.br/"}
    # (Adicionar as outras para completar o Top 5 por cidade conforme seu dado real)
]

# 4. Pesquisa por Cidade
cidade_sel = st.selectbox("🔍 Selecione o Município:", ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"])

st.markdown(f"### Top Ocupações em {cidade_sel}")

# Filtro e Loop de Cards
for v in [x for x in vagas if x['cid'] == cidade_sel]:
    st.markdown(f"""
        <div class="vaga-container {v['css']}">
            <div class="label-setor">{v['set']}</div>
            <div class="job-title">{v['ocup']}</div>
            <div style='margin-bottom: 10px;'>
                📍 Bairro: <b>{v['bai']}</b> | 🎓 Nível: <b>{v['esc']}</b>
            </div>
            <div class="salary-value">R$ {v['sal']:,}</div>
        </div>
        """, unsafe_allow_html=True)
    st.link_button(f"🔗 Qualificação Sugerida", v['link'], use_container_width=True)

# 5. Tabela de Saldos Regionais (Formatada em HTML para controle de cor)
st.divider()
st.markdown("### 📈 Panorama de Saldos e Renda")

html_table = """
<table class="styled-table">
    <thead><tr><th>Ocupação</th><th>Cidade</th><th>Salário</th></tr></thead>
    <tbody>
"""
for v in vagas:
    html_table += f"<tr><td><b>{v['ocup']}</b></td><td>{v['cid']}</td><td>R$ {v['sal']:,}</td></tr>"
html_table += "</tbody></table>"

st.markdown(html_table, unsafe_allow_html=True)

# 6. Nota Técnica
st.markdown("---")
st.caption("""
**Nota:** Dados baseados nos Microdados PNADC 3T de 2025 (IBGE) e Novo CAGED. 
O saldo representa a movimentação líquida de postos formais por unidade produtiva empregadora.
""")

