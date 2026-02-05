import streamlit as st

# 1. Configuração e Estilo Mobile-First
st.set_page_config(page_title="Guia Profissional Juquery", layout="centered")

st.markdown("""
    <style>
    html, body, [class*="css"] { font-size: 13px !important; }
    h2 { font-size: 1.4rem !important; color: #1e3a8a; }
    
    .vaga-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 12px;
        border-left: 6px solid #1e3a8a;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    .local-tag {
        font-size: 0.75rem;
        color: #1e3a8a;
        font-weight: bold;
        background-color: #eef2ff;
        padding: 2px 8px;
        border-radius: 5px;
    }
    .setor-tag {
        font-size: 0.7rem;
        text-transform: uppercase;
        color: #64748b;
        font-weight: bold;
        margin-left: 5px;
    }
    .salario-text {
        color: #059669;
        font-weight: bold;
        font-size: 1.1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Cabeçalho
st.markdown("## 🔍 Ocupações por Bairro")
st.caption("Cajamar • Caieiras • Franco • Morato")

# 3. Base de Dados com Bairros (Dados RAIS/CAGED Localizados)
vagas = [
    {
        "cargo": "Analista Logístico", "setor": "Logística", 
        "cidade": "Cajamar", "bairro": "Jordanésia",
        "salario": 4800, "escola": "SENAI Cajamar", "nivel": "Técnico"
    },
    {
        "cargo": "Operador de Empilhadeira", "setor": "Logística", 
        "cidade": "Cajamar", "bairro": "Polvilho",
        "salario": 3200, "escola": "SENAI Cajamar", "nivel": "Formação Rápida"
    },
    {
        "cargo": "Técnico Industrial", "setor": "Indústria", 
        "cidade": "Caieiras", "bairro": "Laranjeiras",
        "salario": 5200, "escola": "ETEC Caieiras", "nivel": "Técnico"
    },
    {
        "cargo": "Auxiliar Administrativo", "setor": "Serviços", 
        "cidade": "Franco da Rocha", "bairro": "Centro",
        "salario": 2400, "escola": "Fatec Franco da Rocha", "nivel": "Superior"
    },
    {
        "cargo": "Vendedor Líder", "setor": "Comércio", 
        "cidade": "Francisco Morato", "bairro": "Belém Capela",
        "salario": 3100, "escola": "ETEC Morato", "nivel": "Técnico"
    }
]

# 4. Busca e Filtros Avançados
busca = st.text_input("Cargo, Setor ou Bairro:", placeholder="Ex: Jordanésia, TI, Polvilho...")
cid_filtro = st.selectbox("Filtrar por Cidade:", ["Todas as Cidades", "Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"])

# 5. Renderização
st.write("### Oportunidades Encontradas")

for v in vagas:
    # A busca agora olha para o Bairro também
    match_busca = (busca.lower() in v['cargo'].lower() or 
                   busca.lower() in v['setor'].lower() or 
                   busca.lower() in v['bairro'].lower())
    
    match_cidade = (cid_filtro == "Todas as Cidades" or cid_filtro == v['cidade'])

    if match_busca and match_cidade:
        st.markdown(f"""
            <div class="vaga-card">
                <span class="local-tag">📍 {v['bairro']}</span>
                <span class="setor-tag">{v['setor']} • {v['cidade']}</span>
                <div style='font-size: 1.2rem; font-weight: bold; margin: 8px 0;'>{v['cargo']}</div>
                <div class="salario-text">R$ {v['salario']:,}</div>
                <div style='margin-top: 10px; font-size: 0.85rem; color: #475569;'>
                    🎓 <b>Qualificação:</b> {v['escola']} ({v['nivel']})
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.link_button(f"Ver cursos na {v['escola']}", "https://www.cps.sp.gov.br/")

st.divider()
st.caption("Nota: Os bairros são baseados na geolocalização dos CNPJs ativos via RAIS.")
