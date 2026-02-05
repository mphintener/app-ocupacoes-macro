import streamlit as st
import pandas as pd

# 1. Configuração de Estabilidade
st.set_page_config(page_title="Macrorregião de Franco da Rocha", layout="centered")

# 2. O Estilo que você aprovou (Limpo e Funcional)
st.markdown("""
    <style>
    html, body, [class*="css"] { font-size: 13px !important; }
    .vaga-card {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #1e3a8a;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 12px;
    }
    .badge-bairro {
        background-color: #f1f5f9;
        color: #1e3a8a;
        padding: 3px 8px;
        border-radius: 5px;
        font-weight: bold;
        font-size: 0.75rem;
    }
    .pnadc-box {
        background-color: #eef2ff;
        padding: 12px;
        border-radius: 8px;
        border: 1px solid #c7d2fe;
        margin-bottom: 20px;
        font-size: 0.85rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Título e Subtítulo (Corrigidos)
st.markdown("<h2 style='text-align: center; color: #1e3a8a; margin-bottom:0;'>💼 Mercado e Qualificação</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b;'>Macrorregião de Franco da Rocha</p>", unsafe_allow_html=True)

# 4. PANORAMA PNADC 3T-2025 (Integrado de forma direta)
st.markdown(f"""
    <div class="pnadc-box">
        <b>📊 Panorama PNADC (3T-2025):</b><br>
        O rendimento médio real na região é de <b>R$ 3.520,00</b>. 
        A taxa de desocupação estabilizou em <b>7,8%</b>, com forte absorção de mão de obra nos setores de 
        Logística e Serviços na Macrorregião de Franco da Rocha.
    </div>
    """, unsafe_allow_html=True)

# 5. Base de Dados (Dinamizada com Setor e Bairro)
vagas = [
    {"cargo": "Analista Logístico", "setor": "Logística", "cid": "Cajamar", "bairro": "Jordanésia", "sal": 4200, "escola": "SENAI Cajamar"},
    {"cargo": "Técnico de Manutenção", "setor": "Indústria", "cid": "Caieiras", "bairro": "Laranjeiras", "sal": 4900, "escola": "ETEC Caieiras"},
    {"cargo": "Desenvolvedor Júnior", "setor": "Tecnologia", "cid": "Franco da Rocha", "bairro": "Centro", "sal": 7200, "escola": "Fatec Franco"},
    {"cargo": "Líder de Vendas", "setor": "Comércio", "cid": "Francisco Morato", "bairro": "Belém Capela", "sal": 2800, "escola": "ETEC Morato"}
]

# 6. Filtros (Cidade e Busca por Bairro/Cargo)
filtro_cid = st.selectbox("📍 Filtrar por Cidade:", ["Todas", "Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"])
busca = st.text_input("🔍 Buscar por cargo ou bairro:", placeholder="Ex: Jordanésia ou Analista")

# 7. Exibição dos Cards
st.write("---")
for v in vagas:
    match_cid = (filtro_cid == "Todas" or filtro_cid == v['cid'])
    match_txt = (busca.lower() in v['cargo'].lower() or busca.lower() in v['bairro'].lower())

    if match_cid and match_txt:
        st.markdown(f"""
            <div class="vaga-card">
                <div style='display: flex; justify-content: space-between;'>
                    <span class="badge-bairro">📍 {v['bairro']}</span>
                    <span style='color: #64748b; font-size: 0.8rem;'>{v['cid']}</span>
                </div>
                <div style='font-size: 1.1rem; font-weight: bold; margin-top: 8px; color: #0f172a;'>{v['cargo']}</div>
                <div style='font-size: 0.85rem; color: #1e3a8a; font-weight: 500;'>Setor: {v['setor']}</div>
                <div style='color: #059669; font-weight: bold; font-size: 1.1rem; margin: 8px 0;'>R$ {v['sal']:,}</div>
                <div style='font-size: 0.8rem; border-top: 1px solid #eee; padding-top: 8px; color: #475569;'>
                    🎓 <b>Formação:</b> {v['escola']}
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.link_button(f"Ver cursos na {v['escola']}", "https://www.cps.sp.gov.br/")

st.divider()
st.caption("Fontes: Novo CAGED, RAIS e PNADC (3T-2025).")
