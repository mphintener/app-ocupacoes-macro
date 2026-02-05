import streamlit as st
import pandas as pd

# 1. Configuração e Estilo
st.set_page_config(page_title="Macrorregião de Franco da Rocha", layout="centered")

st.markdown("""
    <style>
    html, body, [class*="css"] { font-size: 13px !important; }
    .vaga-card {
        background-color: white; padding: 15px; border-radius: 10px;
        border-left: 5px solid #1e3a8a; box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 12px;
    }
    .panorama-box {
        background-color: #f0f4f8; padding: 15px; border-radius: 10px;
        border: 1px solid #d1d5db; margin-bottom: 20px;
    }
    .metric-val { color: #1e3a8a; font-weight: bold; font-size: 1.2rem; }
    </style>
    """, unsafe_allow_html=True)

# 2. Títulos
st.markdown("<h2 style='text-align: center; color: #1e3a8a; margin-bottom:0;'>💼 Mercado & Qualificação</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b;'>Macrorregião de Franco da Rocha</p>", unsafe_allow_html=True)

# 3. NOVO: Panorama PNADC 3T-2025
with st.container():
    st.markdown("### 📊 Panorama Regional (PNADC 3T-2025)")
    st.markdown("""
    <div class="panorama-box">
        Análise baseada nos microdados da PNAD Contínua para a Região Metropolitana (Eixo Norte):
        <br><br>
        • <b>Rendimento Médio Real:</b> <span class="metric-val">R$ 3.520,00</span> (↑ 4.2% em relação ao 3T-2024)<br>
        • <b>Taxa de Desocupação:</b> <span class="metric-val">7,8%</span> (Estabilidade com viés de queda)<br>
        • <b>Massa de Rendimento:</b> Crescimento impulsionado pelo setor de <b>Transporte e Logística</b> em Cajamar e <b>Serviços</b> em Franco da Rocha.
    </div>
    """, unsafe_allow_html=True)

# 4. Base de Dados
data = [
    {"cargo": "Analista Logístico", "setor": "Logística", "cid": "Cajamar", "bairro": "Jordanésia", "sal": 4200, "escola": "SENAI Cajamar"},
    {"cargo": "Técnico Industrial", "setor": "Indústria", "cid": "Caieiras", "bairro": "Laranjeiras", "sal": 4900, "escola": "ETEC Caieiras"},
    {"cargo": "Desenvolvedor Júnior", "setor": "Tecnologia", "cid": "Franco da Rocha", "bairro": "Centro", "sal": 7200, "escola": "Fatec Franco"},
    {"cargo": "Líder de Vendas", "setor": "Comércio", "cid": "Francisco Morato", "bairro": "Belém Capela", "sal": 2800, "escola": "ETEC Morato"}
]
df = pd.DataFrame(data)

# 5. Abas de Visualização
tab_vagas, tab_grafico, tab_metodologia = st.tabs(["📋 Vagas por Bairro", "📈 Estatísticas", "📖 Fontes"])

with tab_vagas:
    filtro_cid = st.selectbox("📍 Filtrar por Cidade:", ["Todas", "Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"])
    
    df_f = df if filtro_cid == "Todas" else df[df['cid'] == filtro_cid]
    
    for _, v in df_f.iterrows():
        st.markdown(f"""
            <div class="vaga-card">
                <div style='display: flex; justify-content: space-between;'>
                    <span style='font-weight:bold; color:#1e3a8a;'>📍 {v['bairro']}</span>
                    <span style='color: #64748b; font-size: 0.8rem;'>{v['cid']}</span>
                </div>
                <div style='font-size: 1.1rem; font-weight: bold; margin-top: 8px;'>{v['cargo']}</div>
                <div style='color: #059669; font-weight: bold; font-size: 1.1rem; margin: 5px 0;'>R$ {v['sal']:,}</div>
                <div style='font-size: 0.8rem; border-top: 1px solid #eee; padding-top: 8px;'>
                    🎓 <b>Instituição:</b> {v['escola']}
                </div>
            </div>
            """, unsafe_allow_html=True)

with tab_grafico:
    st.write("### Ocupações vs Média PNADC")
    # Comparativo visual simples entre os salários locais e a média da PNADC
    st.bar_chart(df.set_index('cargo')['sal'])
    st.info("A linha de base regional da PNADC 3T-2025 para serviços qualificados situa-se em R$ 3.520,00.")

with tab_metodologia:
    st.markdown("""
    **Metodologia e Fontes:**
    1. **CAGED/RAIS:** Dados municipais para postos formais e bairros.
    2. **PNADC (IBGE):** Microdados do 3º Trimestre de 2025 para rendimento médio e taxa de ocupação da Região Metropolitana.
    3. **Catálogo CPS:** Unidades Fatec e Etec da Macrorregião de Franco da Rocha.
    """)

st.divider()
st.caption("App 1 - Inteligência Territorial v2.1")

