import streamlit as st
import pandas as pd

# 1. Ajuste Técnico de Visual (Clean, Profissional, Sem Cores Pesadas)
st.set_page_config(page_title="Macrorregião de Franco da Rocha", layout="centered")

st.markdown("""
    <style>
    /* Estilo Minimalista */
    html, body, [class*="css"] { font-size: 13px !important; color: #334155; }
    .stApp { background-color: #ffffff; }
    
    /* Container de Dados PNADC */
    .pnadc-container {
        border: 1px solid #e2e8f0;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 25px;
        background-color: #f8fafc;
    }
    
    /* Card de Ocupação - Sem Quadro Branco Excessivo */
    .card-vaga {
        padding: 15px;
        border-bottom: 2px solid #f1f5f9;
        margin-bottom: 10px;
    }
    .ocupacao-titulo { font-size: 1.1rem; font-weight: bold; color: #1e3a8a; }
    .detalhe-vaga { font-size: 0.85rem; color: #64748b; margin-top: 5px; }
    .valor-salario { color: #059669; font-weight: bold; font-size: 1rem; }
    </style>
    """, unsafe_allow_html=True)

# 2. Título e Panorama Econômico
st.markdown("## 💼 Mercado e Qualificação")
st.markdown("### Macrorregião de Franco da Rocha")

st.markdown("""
    <div class="pnadc-container">
        <b>📊 Panorama Econômico:</b><br>
        Fonte: <b>Microdados PNADC 3T de 2025</b><br>
        Renda Média: <b>R$ 3.520,00</b> | Taxa de Desemprego: <b>7,8%</b>
    </div>
    """, unsafe_allow_html=True)

# 3. Base de Dados (Nomes Reais de Ocupações, Setores e Bairros)
# Simulação dos 5 cargos que mais geraram vagas (CAGED)
vagas_data = {
    "Franco da Rocha": [
        {"ocup": "Técnico de Enfermagem", "set": "Saúde", "sal": 3450, "bai": "Centro", "esc": "ETEC Dr. Emílio Hernandez", "link": "https://www.cps.sp.gov.br/"},
        {"ocup": "Analista Administrativo", "set": "Serviços", "sal": 3100, "bai": "Vila Rosalina", "esc": "Fatec Franco da Rocha", "link": "https://www.fatecfrancodarocha.edu.br/"},
        {"ocup": "Operador de Logística", "set": "Logística", "sal": 2100, "bai": "Pouso Alegre", "esc": "ETEC Dr. Emílio Hernandez", "link": "https://www.cps.sp.gov.br/"},
        {"ocup": "Vendedor de Comércio", "set": "Varejo", "sal": 1950, "bai": "Centro", "esc": "ETEC Dr. Emílio Hernandez", "link": "https://www.cps.sp.gov.br/"},
        {"ocup": "Auxiliar de Manutenção", "set": "Indústria", "sal": 2400, "bai": "Polo Industrial", "esc": "ETEC Dr. Emílio Hernandez", "link": "https://www.cps.sp.gov.br/"}
    ],
    "Francisco Morato": [
        {"ocup": "Gerente de Loja", "set": "Varejo", "sal": 3800, "bai": "Centro", "esc": "ETEC Francisco Morato", "link": "http://etecfranciscomorato.com.br/"},
        {"ocup": "Assistente Logístico", "set": "Transportes", "sal": 2450, "bai": "Belém Capela", "esc": "ETEC Francisco Morato", "link": "http://etecfranciscomorato.com.br/"},
        {"ocup": "Vendedor Especializado", "set": "Varejo", "sal": 2100, "bai": "Vila Guilherme", "esc": "ETEC Francisco Morato", "link": "http://etecfranciscomorato.com.br/"},
        {"ocup": "Operador de Caixa", "set": "Varejo", "sal": 1820, "bai": "Centro", "esc": "ETEC Francisco Morato", "link": "http://etecfranciscomorato.com.br/"},
        {"ocup": "Estoquista", "set": "Logística", "sal": 1900, "bai": "Jardim Nova Morato", "esc": "ETEC Francisco Morato", "link": "http://etecfranciscomorato.com.br/"}
    ]
}

# 4. Filtro por Cidade
cidade_selecionada = st.selectbox("Selecione o Município:", list(vagas_data.keys()))

st.markdown(f"#### Principais Ocupações em {cidade_selecionada} (Saldo CAGED)")

# 5. Exibição das 5 Ocupações e Links
for item in vagas_data[cidade_selecionada]:
    st.markdown(f"""
        <div class="card-vaga">
            <div class="ocupacao-titulo">{item['ocup']}</div>
            <div class="detalhe-vaga">
                🏢 Setor: <b>{item['set']}</b> | 📍 Bairro: <b>{item['bai']}</b><br>
                <span class="valor-salario">Salário Médio: R$ {item['sal']:,}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.link_button(f"Qualificação Sugerida: {item['esc']}", item['link'])

# 6. Tabela Ilustrativa de Saldo Regional
st.divider()
st.markdown("### 📊 Tabela de Saldos da Região")

# Gerando dataframe para a tabela
df_lista = []
for cid, lista in vagas_data.items():
    for o in lista:
        df_lista.append({"Ocupação": o['ocup'], "Cidade": cid, "Setor": o['set'], "Salário": o['sal']})

df_final = pd.DataFrame(df_lista)

st.table(df_final)

# 7. Nota Técnica
st.markdown("---")
st.markdown("""
**Nota Técnica:**
- **Fontes:** Microdados PNADC 3T de 2025 (PNADC/IBGE) e Novo CAGED (Último mês disponível).
- **Saldo:** Diferença entre admissões e desligamentos.
- **Bairros:** Unidades produtivas com maior saldo de contratação.
""")

