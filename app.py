import streamlit as st

# 1. Configuração e Estilo Superior
st.set_page_config(page_title="Macrorregião de Franco da Rocha - Ocupações", layout="centered")

st.markdown("""
    <style>
    html, body, [class*="css"] { font-size: 13px !important; background-color: #f8fafc; }
    
    .main-title {
        font-size: 1.5rem !important;
        color: #1e3a8a;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 0.9rem;
        color: #64748b;
        text-align: center;
        margin-bottom: 25px;
    }
    .vaga-card {
        background-color: white;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 15px;
    }
    .badge-setor {
        background-color: #e0f2fe;
        color: #0369a1;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.7rem;
        font-weight: bold;
        text-transform: uppercase;
    }
    .badge-bairro {
        color: #1e3a8a;
        font-weight: 600;
        font-size: 0.85rem;
    }
    .salary-tag {
        font-size: 1.2rem;
        font-weight: 800;
        color: #059669;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Cabeçalho Atualizado
st.markdown('<div class="main-title">💼 Ocupações e Qualificação</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Macrorregião de Franco da Rocha: Inteligência de Mercado</div>', unsafe_allow_html=True)

# 3. Base de Dados (CAGED/RAIS/PNADC)
vagas = [
    {"cargo": "Analista Logístico Sênior", "setor": "Logística", "cid": "Cajamar", "bairro": "Jordanésia", "sal": 5200, "escola": "SENAI Cajamar"},
    {"cargo": "Técnico de Manutenção", "setor": "Indústria", "cid": "Caieiras", "bairro": "Laranjeiras", "sal": 4900, "escola": "ETEC Caieiras"},
    {"cargo": "Desenvolvedor Júnior", "setor": "Tecnologia", "cid": "Franco da Rocha", "bairro": "Centro", "sal": 7200, "escola": "Fatec Franco"},
    {"cargo": "Líder de Operações", "setor": "Logística", "cid": "Cajamar", "bairro": "Polvilho", "sal": 3800, "escola": "SENAI Cajamar"},
    {"cargo": "Gerente de Unidade", "setor": "Comércio", "cid": "Francisco Morato", "bairro": "Vila Guilherme", "sal": 3100, "escola": "ETEC Morato"}
]

# 4. Filtro por Cidade (Destaque Principal)
st.write("### 🏙️ Pesquisar por Cidade")
filtro_cid = st.segmented_control(
    "Selecione o município para filtrar as oportunidades:",
    options=["Todas", "Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"],
    default="Todas"
)

busca = st.text_input("🔍 Ou digite o cargo ou bairro:", placeholder="Ex: Jordanésia ou Analista")

# 5. Renderização dos Cards
st.write("---")
for v in vagas:
    # Lógica de filtro combinada
    match_cidade = (filtro_cid == "Todas" or filtro_cid == v['cid'])
    match_busca = (busca.lower() in v['cargo'].lower() or busca.lower() in v['bairro'].lower())

    if match_cidade and match_busca:
        icon = "📦" if v['setor'] == "Logística" else "🏭" if v['setor'] == "Indústria" else "💻"
        
        st.markdown(f"""
            <div class="vaga-card">
                <div style='display: flex; justify-content: space-between; align-items: center;'>
                    <span class="badge-setor">{icon} {v['setor']}</span>
                    <span class="badge-bairro">📍 {v['bairro']}</span>
                </div>
                <div style='font-size: 1.25rem; font-weight: 700; color: #0f172a; margin-top: 12px;'>{v['cargo']}</div>
                <div style='color: #64748b; font-size: 0.9rem;'>{v['cid']} • São Paulo</div>
                <div class="salary-tag">R$ {v['sal']:,}</div>
                <div style='border-top: 1px solid #f1f5f9; padding-top: 10px; font-size: 0.85rem; color: #334155;'>
                    🎓 <b>Caminho de Qualificação:</b> {v['escola']}
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.link_button(f"Explorar cursos em {v['escola']}", "https://www.cps.sp.gov.br/")

# 6. Contexto PNADC
with st.expander("📊 Insights Regionais (PNADC/IBGE)"):
    st.info("A Macrorregião de Franco da Rocha apresenta uma tendência de crescimento nos setores de serviços qualificados e logística de última milha.")

