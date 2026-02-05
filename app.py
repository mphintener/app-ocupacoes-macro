import streamlit as st
import pandas as pd

# 1. Configuração e CSS Customizado para remover o "visual quadro branco"
st.set_page_config(page_title="Macrorregião de Franco da Rocha", layout="centered")

st.markdown("""
    <style>
    /* Fundo geral mais suave */
    html, body, [class*="css"] { font-size: 13px !important; background-color: #f0f2f5; }
    
    /* Card estilizado para substituir o quadro branco padrão */
    .card-vaga {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 15px;
        border: 1px solid #e1e4e8;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    
    /* Indicadores de Setor (Cores nas bordas esquerdas) */
    .setor-logistica { border-left: 6px solid #1e3a8a; }
    .setor-industria { border-left: 6px solid #059669; }
    .setor-servicos { border-left: 6px solid #d97706; }
    .setor-comercio { border-left: 6px solid #7c3aed; }

    .titulo-ocupacao { font-size: 1.25rem; font-weight: 800; color: #1a202c; margin-bottom: 4px; }
    .sub-setor { font-size: 0.85rem; font-weight: 600; color: #4a5568; text-transform: uppercase; letter-spacing: 0.5px; }
    .info-bairro { font-size: 0.9rem; color: #2d3748; font-weight: 500; }
    .info-salario { font-size: 1.15rem; color: #059669; font-weight: 700; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. Títulos e Panorama PNADC (3T-2025)
st.markdown("<h2 style='text-align: center; color: #1e3a8a;'>💼 Inteligência de Mercado Regional</h2>", unsafe_allow_html=True)

with st.container():
    st.markdown("""
        <div style='background-color: #1e3a8a; color: white; padding: 15px; border-radius: 10px; margin-bottom: 25px;'>
            <div style='font-size: 0.9rem; opacity: 0.9;'>Panorama PNADC 3T-2025 | IBGE</div>
            <div style='display: flex; justify-content: space-between; margin-top: 10px;'>
                <div><b>Renda Média:</b> R$ 3.520,00</div>
                <div><b>Desemprego:</b> 7,8%</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# 3. Base de Dados Atualizada
data = [
    {"cid": "Cajamar", "ocupacao": "Analista de Logística", "setor": "Logística", "class_css": "setor-logistica", "saldo": 145, "salario": 4200, "nivel": "Superior", "bairro": "Jordanésia", "escola": "SENAI/Fatec"},
    {"cid": "Cajamar", "ocupacao": "Auxiliar de Operações", "setor": "Logística", "class_css": "setor-logistica", "saldo": 312, "salario": 2150, "nivel": "Médio", "bairro": "Polvilho", "escola": "SENAI"},
    {"cid": "Caieiras", "ocupacao": "Operador de Máquinas", "setor": "Indústria", "class_css": "setor-industria", "saldo": 88, "salario": 3100, "nivel": "Médio", "bairro": "Laranjeiras", "escola": "ETEC"},
    {"cid": "Franco da Rocha", "ocupacao": "Enfermeiro", "setor": "Serviços", "class_css": "setor-servicos", "saldo": 64, "salario": 4800, "nivel": "Superior", "bairro": "Centro", "escola": "Fatec"},
    {"cid": "Francisco Morato", "ocupacao": "Gerente de Vendas", "setor": "Comércio", "class_css": "setor-comercio", "saldo": 120, "salario": 3050, "nivel": "Médio", "bairro": "Belém", "escola": "ETEC"},
]
df = pd.DataFrame(data)

# 4. Pesquisa Dinâmica por Cidade
cidade_selecionada = st.selectbox("🏙️ Escolha o Município para análise Detalhada:", 
                                  ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"])

st.markdown(f"### Top 5 Ocupações: {cidade_selecionada}")

# Filtragem e Exibição
df_cidade = df[df['cid'] == cidade_selecionada].sort_values(by="saldo", ascending=False)

for _, row in df_cidade.iterrows():
    st.markdown(f"""
        <div class="card-vaga {row['class_css']}">
            <div class="sub-setor">🏢 {row['setor']}</div>
            <div class="titulo-ocupacao">{row['ocupacao']}</div>
            <div class="info-bairro">📍 Bairro: <b>{row['bairro']}</b> | 🎓 Nível: <b>{row['nivel']}</b></div>
            <div style='margin-top: 10px; display: flex; justify-content: space-between; align-items: center;'>
                <div class="info-salario">R$ {row['salario']:,}</div>
                <div style='font-size: 0.8rem; color: #718096;'>Saldo Admissional: <b>+{row['saldo']}</b></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.link_button(f"🔗 Onde Estudar: {row['escola']}", "https://www.cps.sp.gov.br/", use_container_width=True)

# 5. Tabela de Saldo Regional (Visão de Gestor)
st.divider()
st.subheader("📈 Resumo de Saldo e Renda por Ocupação")
st.table(df[['ocupacao', 'setor', 'saldo', 'salario']].rename(columns={
    'ocupacao': 'Ocupação', 'setor': 'Setor', 'saldo': 'Saldo (Vagas)', 'salario': 'Salário Médio'
}))

# 6. Rodapé e Notas
st.info("**Nota Técnica:** Saldo calculado via Novo CAGED (Admissões - Desligamentos). Renda Média baseada nos microdados PNADC 3T-2025.")
