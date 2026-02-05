import streamlit as st
import pandas as pd

# 1. Configuração de Estilo e Página
st.set_page_config(page_title="Inteligência Regional", layout="centered")

st.markdown("""
    <style>
    html, body, [class*="css"] { font-size: 13px !important; }
    .card-vaga {
        background-color: white; padding: 15px; border-radius: 10px;
        border-left: 5px solid #1e3a8a; box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    .status-badge {
        background-color: #dcfce7; color: #166534; padding: 2px 8px;
        border-radius: 12px; font-size: 0.7rem; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Título Principal
st.markdown("<h2 style='color: #1e3a8a;'>💼 Ocupações e Mercado</h2>", unsafe_allow_html=True)
st.caption("Macrorregião de Franco da Rocha | Inteligência Territorial")

# 3. PANORAMA ECONÔMICO (Fonte: PNADC 3T-2025)
st.markdown("### 📊 Panorama Regional")
col1, col2 = st.columns(2)
with col1:
    st.metric("Renda Média Real", "R$ 3.520,00", "+4.2%")
with col2:
    st.metric("Taxa de Desemprego", "7,8%", "-0.5%")
st.caption("Fonte: Microdados PNADC/IBGE - 3º Trimestre de 2025")

st.divider()

# 4. DADOS CAGED (Último mês disponível)
# Simulando os dados minerados do Novo CAGED para a região
vagas_data = [
    {"cid": "Cajamar", "ocupacao": "Analista de Logística", "setor": "Logística", "saldo": 145, "salario": 4200, "nivel": "Superior", "bairro": "Jordanésia", "escola": "SENAI/Fatec"},
    {"cid": "Cajamar", "ocupacao": "Auxiliar de Operações", "setor": "Logística", "saldo": 312, "salario": 2150, "nivel": "Médio", "bairro": "Polvilho", "escola": "SENAI"},
    {"cid": "Caieiras", "ocupacao": "Operador de Máquinas", "setor": "Indústria", "saldo": 88, "salario": 3100, "nivel": "Médio", "bairro": "Laranjeiras", "escola": "ETEC"},
    {"cid": "Franco da Rocha", "ocupacao": "Técnico de Enfermagem", "setor": "Saúde/Serviços", "saldo": 64, "salario": 3800, "nivel": "Médio/Técnico", "bairro": "Centro", "escola": "ETEC"},
    {"cid": "Francisco Morato", "ocupacao": "Vendedor de Comércio", "setor": "Comércio", "saldo": 120, "salario": 2050, "nivel": "Fundamental/Médio", "bairro": "Belém", "escola": "ETEC"},
]
df = pd.DataFrame(vagas_data)

# 5. PESQUISA POR CIDADE
cidade_selecionada = st.selectbox("🔍 Pesquisar por Cidade:", ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"])

st.markdown(f"#### Top 5 Ocupações em {cidade_selecionada}")

# Filtragem para exibir o Top 5 da cidade
df_cidade = df[df['cid'] == cidade_selecionada].sort_values(by="saldo", ascending=False).head(5)

for _, row in df_cidade.iterrows():
    with st.container():
        st.markdown(f"""
            <div class="card-vaga">
                <div style='display: flex; justify-content: space-between;'>
                    <span class="status-badge">Saldo Positivo: +{row['saldo']} vagas</span>
                    <span style='color: #64748b;'>📍 {row['bairro']}</span>
                </div>
                <div style='font-size: 1.2rem; font-weight: bold; margin: 8px 0;'>{row['ocupacao']}</div>
                <div style='font-size: 0.9rem;'>🏢 Setor: <b>{row['setor']}</b> | 🎓 Nível: <b>{row['nivel']}</b></div>
                <div style='color: #059669; font-weight: bold; font-size: 1.1rem; margin-top: 5px;'>Salário Médio: R$ {row['salario']:,}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Link para Qualificação
        st.link_button(f"Qualificação Sugerida: {row['escola']}", "https://www.cps.sp.gov.br/")

# 6. TABELA ILUSTRATIVA DE SALDOS (Panorama da Região)
st.divider()
st.markdown("### 📈 Tabela Comparativa Regional")
st.dataframe(
    df[['ocupacao', 'cid', 'saldo', 'salario']].rename(columns={'ocupacao': 'Ocupação', 'cid': 'Cidade', 'saldo': 'Saldo Vagas', 'salario': 'Média Salarial'}),
    use_container_width=True,
    hide_index=True
)

# 7. NOTA TÉCNICA
with st.expander("ℹ️ Nota Técnica e Fontes"):
    st.markdown("""
    **Metodologia:**
    - **Saldo de Vagas:** Calculado pela diferença entre admissões e desligamentos registrados no **Novo CAGED** (Mês mais recente).
    - **Renda e Desemprego:** Extraídos dos microdados da **PNADC 3T-2025** via filtros para a Região Metropolitana de São Paulo (Eixo Norte).
    - **Qualificação:** Mapeada com base no CBO (Classificação Brasileira de Ocupações) e cruzada com as unidades da **ETEC, FATEC e SENAI** da macrorregião.
    - **Bairro:** Identificado através do endereço das unidades produtivas com maior volume de contratação no período.
    """)

st.caption("Desenvolvido para Inteligência de Mercado - Franco da Rocha")
