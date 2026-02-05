import streamlit as st
import pandas as pd

# 1. CSS MASTER (Dark Mode Avançado com Cores de Setor)
st.set_page_config(page_title="Inteligência Regional", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117 !important; color: #ffffff !important; }
    
    /* Header Profissional */
    .header-dark {
        background-color: #1a1d23;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #334155;
        margin-bottom: 25px;
    }

    /* Cards Estilizados por Setor */
    .card-vaga {
        background-color: #1a1d23;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 12px;
        border-top: 1px solid #334155;
        box-shadow: 0 4px 6px rgba(0,0,0,0.4);
    }
    
    /* Bordas Laterais por Setor */
    .border-logistica { border-left: 6px solid #3b82f6; }
    .border-industria { border-left: 6px solid #10b981; }
    .border-servicos { border-left: 6px solid #f59e0b; }
    .border-comercio { border-left: 6px solid #8b5cf6; }

    .titulo-vaga { font-size: 1.25rem; font-weight: bold; color: #ffffff; margin-bottom: 5px; }
    .setor-badge { font-size: 0.7rem; font-weight: 800; padding: 2px 8px; border-radius: 4px; text-transform: uppercase; margin-bottom: 10px; display: inline-block; }
    .salario-valor { font-size: 1.15rem; font-weight: bold; color: #10b981; }
    .bairro-tag { color: #94a3b8; font-size: 0.85rem; }

    /* Tabela de Dados Brutos Blindada */
    .dark-table {
        width: 100%; border-collapse: collapse; background-color: #111418; color: white; border-radius: 8px; overflow: hidden;
    }
    .dark-table th { background-color: #1e293b; padding: 12px; text-align: left; color: #94a3b8; font-size: 0.8rem; }
    .dark-table td { padding: 12px; border-bottom: 1px solid #1e293b; font-size: 0.85rem; }
    </style>
    """, unsafe_allow_html=True)

# 2. Panorama Macrorregional (Microdados PNADC 3T-2025)
st.markdown("""
    <div class="header-dark">
        <div style="font-size: 0.75rem; color: #64748b; letter-spacing: 1.5px; font-weight: bold;">📊 EIXO NORTE • MACRORREGIÃO DE FRANCO DA ROCHA</div>
        <h2 style="color: white; margin: 8px 0;">Mercado e Qualificação</h2>
        <div style="margin-top: 15px; padding-top: 15px; border-top: 1px solid #334155; display: flex; justify-content: space-between; align-items: center;">
            <div>
                <small style="color: #94a3b8;">Renda Média (Média Regional)</small><br>
                <b style="font-size: 1.3rem;">R$ 3.520,00</b>
            </div>
            <div style="text-align: right;">
                <small style="color: #94a3b8;">Taxa de Desocupação (PNADC 3T-2025)</small><br>
                <b style="font-size: 1.3rem; color: #f87171;">7,8%</b>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 3. Base de Dados Dinâmica (4 Cidades | 5 Ocupações)
vagas_lista = [
    # CAJAMAR
    {"cid": "Cajamar", "ocup": "Analista de Logística", "set": "Logística", "cls": "border-logistica", "sal": 4200, "bai": "Jordanésia", "esc": "SENAI Cajamar", "lnk": "https://cajamar.sp.senai.br/"},
    {"cid": "Cajamar", "ocup": "Auxiliar de Operações", "set": "Logística", "cls": "border-logistica", "sal": 2150, "bai": "Polvilho", "esc": "SENAI Cajamar", "lnk": "https://cajamar.sp.senai.br/"},
    {"cid": "Cajamar", "ocup": "Conferente", "set": "Logística", "cls": "border-logistica", "sal": 2600, "bai": "Gato Preto", "esc": "SENAI Cajamar", "lnk": "https://cajamar.sp.senai.br/"},
    {"cid": "Cajamar", "ocup": "Operador de Empilhadeira", "set": "Logística", "cls": "border-logistica", "sal": 2900, "bai": "Jordanésia", "esc": "SENAI Cajamar", "lnk": "https://cajamar.sp.senai.br/"},
    {"cid": "Cajamar", "ocup": "Líder de Recebimento", "set": "Logística", "cls": "border-logistica", "sal": 3800, "bai": "Polvilho", "esc": "SENAI Cajamar", "lnk": "https://cajamar.sp.senai.br/"},
    # CAIEIRAS
    {"cid": "Caieiras", "ocup": "Operador de Produção", "set": "Indústria", "cls": "border-industria", "sal": 2800, "bai": "Laranjeiras", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/"},
    {"cid": "Caieiras", "ocup": "Mecânico Industrial", "set": "Indústria", "cls": "border-industria", "sal": 4500, "bai": "Vila Rosina", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/"},
    {"cid": "Caieiras", "ocup": "Ajudante de Carga", "set": "Logística", "cls": "border-logistica", "sal": 1950, "bai": "Laranjeiras", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/"},
    {"cid": "Caieiras", "ocup": "Eletricista de Manutenção", "set": "Indústria", "cls": "border-industria", "sal": 4200, "bai": "Vila Jaguari", "esc": "SENAI", "lnk": "https://www.cps.sp.gov.br/"},
    {"cid": "Caieiras", "ocup": "Auxiliar de Almoxarife", "set": "Serviços", "cls": "border-servicos", "sal": 2200, "bai": "Centro", "esc": "ETEC Caieiras", "lnk": "https://www.cps.sp.gov.br/"},
    # FRANCO E MORATO (Adicionar os 5 de cada aqui...)
    {"cid": "Franco da Rocha", "ocup": "Técnico de Enfermagem", "set": "Serviços", "cls": "border-servicos", "sal": 3450, "bai": "Centro", "esc": "ETEC Franco", "lnk": "https://www.cps.sp.gov.br/"},
    {"cid": "Francisco Morato", "ocup": "Gerente de Varejo", "set": "Comércio", "cls": "border-comercio", "sal": 3800, "bai": "Centro", "esc": "ETEC Morato", "lnk": "http://etecfranciscomorato.com.br/"}
]

# 4. Filtros de Pesquisa
st.markdown("### 🔍 Pesquisa de Oportunidades")
col_cid, col_sal = st.columns([1, 1])

with col_cid:
    cidade_sel = st.selectbox("Cidade:", ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"])
with col_sal:
    min_sal = st.slider("Salário Mínimo (R$):", 1500, 6000, 1800)

# 5. Renderização dos Cards (Dinamizados)
st.write("---")
df_resumo = [v for v in vagas_lista if v['cid'] == cidade_sel and v['sal'] >= min_sal]

for v in df_resumo:
    # Definindo cor da badge baseada no setor
    badge_color = "#3b82f6" if v['set'] == "Logística" else "#10b981" if v['set'] == "Indústria" else "#f59e0b"
    
    st.markdown(f"""
        <div class="card-vaga {v['cls']}">
            <div class="setor-badge" style="background-color: {badge_color}22; color: {badge_color}; border: 1px solid {badge_color}55;">{v['set']}</div>
            <div class="titulo-vaga">{v['ocup']}</div>
            <div class="bairro-tag">📍 Bairro: <b>{v['bai']}</b> | Unidade: <b>{v['esc']}</b></div>
            <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-top: 15px;">
                <div class="salario-valor">R$ {v['sal']:,}</div>
                <div style="color: #10b981; font-size: 0.8rem; font-weight: bold;">📈 Saldo Positivo (CAGED)</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.link_button(f"Ver Cursos na {v['esc']}", v['lnk'], use_container_width=True)

# 6. Tabela Panorâmica Estilizada
st.divider()
st.markdown("### 📊 Panorama Geral de Saldos")

html_table = """<table class="dark-table">
    <thead><tr><th>Ocupação</th><th>Cidade</th><th>Bairro</th><th>Média Salarial</th></tr></thead>
    <tbody>"""
for item in vagas_lista:
    html_table += f"<tr><td><b>{item['ocup']}</b></td><td>{item['cid']}</td><td>{item['bai']}</td><td style='color:#10b981;'>R$ {item['sal']:,}</td></tr>"
html_table += "</tbody></table>"

st.markdown(html_table, unsafe_allow_html=True)

# 7. Nota de Rodapé
st.markdown("---")
st.caption("Fontes: Microdados PNADC 3T de 2025 (IBGE), Novo CAGED e Catálogo de Escolas Técnicas CPS/SENAI.")

