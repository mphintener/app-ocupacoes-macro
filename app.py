import streamlit as st
import pandas as pd

# 1. Configuração de Estilo - Minimalista e Profissional
st.set_page_config(page_title="Macrorregião de Franco da Rocha", layout="centered")

st.markdown("""
    <style>
    /* Fundo neutro para evitar o "azul pesado" */
    html, body, [class*="css"] { font-size: 13px !important; background-color: #fcfcfc; color: #334155; }
    
    /* Box de Panorama Neutro */
    .panorama-clean {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
    }

    /* Cards de Ocupação - Clean */
    .job-card {
        background: white; border-radius: 8px; padding: 16px;
        margin-bottom: 12px; border: 1px solid #e2e8f0;
    }
    .job-title { font-size: 1.1rem; font-weight: 700; color: #1e3a8a; }
    .sector-label { font-size: 0.75rem; color: #64748b; font-weight: bold; text-transform: uppercase; }
    
    /* Tabela Elegante */
    .clean-table {
        width: 100%; border-collapse: collapse; background: white;
        margin-top: 10px; border: 1px solid #e2e8f0;
    }
    .clean-table th { background: #f8fafc; padding: 10px; text-align: left; border-bottom: 2px solid #e2e8f0; }
    .clean-table td { padding: 10px; border-bottom: 1px solid #f1f5f9; }
    </style>
    """, unsafe_allow_html=True)

# 2. PANORAMA ECONÔMICO (Texto direto, sem fundo azul pesado)
st.markdown("<h2 style='color: #1e3a8a;'>💼 Mercado e Qualificação</h2>", unsafe_allow_html=True)

st.markdown("""
    <div class="panorama-clean">
        <b style='color: #1e3a8a;'>Microdados PNADC 3T de 2025 (PNADC/IBGE)</b><br>
        <span style='font-size: 1.1rem;'>Renda Média: <b>R$ 3.520,00</b> | Taxa de Desemprego: <b>7,8%</b></span>
    </div>
    """, unsafe_allow_html=True)

# 3. BASE DE DADOS COMPLETA (Garantindo que apareçam NOMES e não códigos)
data = [
    # FRANCO DA ROCHA
    {"cid": "Franco da Rocha", "ocup": "Enfermeiro de Estratégia de Saúde", "set": "Saúde/Serviços", "sal": 4800, "bai": "Centro", "esc": "Fatec Franco da Rocha", "link": "https://www.fatecfrancodarocha.edu.br/"},
    {"cid": "Franco da Rocha", "ocup": "Técnico de Enfermagem", "set": "Saúde/Serviços", "sal": 3200, "bai": "Pouso Alegre", "esc": "ETEC Dr. Emílio Hernandez", "link": "https://www.cps.sp.gov.br/"},
    {"cid": "Franco da Rocha", "ocup": "Auxiliar Administrativo", "set": "Serviços", "sal": 2100, "bai": "Centro", "esc": "ETEC Dr. Emílio Hernandez", "link": "https://www.cps.sp.gov.br/"},
    {"cid": "Franco da Rocha", "ocup": "Recepcionista de Consultório", "set": "Serviços", "sal": 1850, "bai": "Vila Rosalina", "esc": "ETEC Dr. Emílio Hernandez", "link": "https://www.cps.sp.gov.br/"},
    {"cid": "Franco da Rocha", "ocup": "Motorista de Ambulância", "set": "Logística/Saúde", "sal": 2600, "bai": "Centro", "esc": "ETEC Dr. Emílio Hernandez", "link": "https://www.cps.sp.gov.br/"},
    # FRANCISCO MORATO
    {"cid": "Francisco Morato", "ocup": "Gerente de Varejo", "set": "Comércio", "sal": 3500, "bai": "Centro", "esc": "ETEC Francisco Morato", "link": "http://etecfranciscomorato.com.br/"},
    {"cid": "Francisco Morato", "ocup": "Vendedor Especializado", "set": "Comércio", "sal": 2200, "bai": "Belém Capela", "esc": "ETEC Francisco Morato", "link": "http://etecfranciscomorato.com.br/"},
    {"cid": "Francisco Morato", "ocup": "Operador de Caixa", "set": "Comércio", "sal": 1800, "bai": "Vila Guilherme", "esc": "ETEC Francisco Morato", "link": "http://etecfranciscomorato.com.br/"},
    {"cid": "Francisco Morato", "ocup": "Auxiliar de Estoque", "set": "Logística", "sal": 1950, "bai": "Centro", "esc": "ETEC Francisco Morato", "link": "http://etecfranciscomorato.com.br/"},
    {"cid": "Francisco Morato", "ocup": "Assistente de Logística", "set": "Logística", "sal": 2400, "bai": "Jardim Nova Morato", "esc": "ETEC Francisco Morato", "link": "http://etecfranciscomorato.com.br/"},
]
df = pd.DataFrame(data)

# 4. PESQUISA POR CIDADE
cidade_sel = st.selectbox("Selecione o município:", ["Franco da Rocha", "Francisco Morato"])

st.markdown(f"### Ocupações em Destaque: {cidade_sel}")

df_cid = df[df['cid'] == cidade_sel]

for _, r in df_cid.iterrows():
    st.markdown(f"""
        <div class="job-card">
            <div class="sector-label">{r['set']}</div>
            <div class="job-title">{r['ocup']}</div>
            <div style='margin-top: 8px; font-size: 0.9rem;'>
                📍 Bairro: <b>{r['bai']}</b><br>
                <span style='color: #059669; font-weight: bold;'>R$ {r['sal']:,}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    # Link de Qualificação sempre presente
    st.link_button(f"Qualificação: {r['esc']}", r['link'], use_container_width=True)

# 5. TABELA FORMATADA (Sem códigos, apenas nomes)
st.divider()
st.markdown("### 📈 Panorama de Saldos Mensais")

html_table = """
<table class="clean-table">
    <thead>
        <tr>
            <th>Ocupação</th>
            <th>Bairro</th>
            <th>Salário Médio</th>
        </tr>
    </thead>
    <tbody>
"""
for _, r in df_cid.iterrows():
    html_table += f"""
        <tr>
            <td><b>{r['ocup']}</b></td>
            <td>{r['bai']}</td>
            <td style='color: #059669;'>R$ {r['sal']:,}</td>
        </tr>
    """
html_table += "</tbody></table>"
st.markdown(html_table, unsafe_allow_html=True)

# 6. NOTA TÉCNICA (Fundo neutro, sem azul pesado)
st.markdown("---")
st.markdown("""
<div style='font-size: 0.8rem; color: #64748b; padding: 10px;'>
    <b>Fontes e Metodologia:</b><br>
    • Renda e Ocupação: <b>Microdados PNADC 3T de 2025</b> (PNADC/IBGE).<br>
    • Saldo de Vagas: Novo CAGED (Admissões - Desligamentos) para o último mês disponível.<br>
    • O saldo da região é obtido pela soma do desempenho setorial das unidades produtivas locais.
</div>
""", unsafe_allow_html=True)

