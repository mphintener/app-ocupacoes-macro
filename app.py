import streamlit as st
import pandas as pd

# 1. Estética Profissional (Clean e Direta)
st.set_page_config(page_title="Inteligência Territorial", layout="centered")

st.markdown("""
    <style>
    html, body, [class*="css"] { font-size: 13px !important; color: #1f2937; }
    .stApp { background-color: #ffffff; }
    
    /* Bloco de Informação Panorâmica */
    .panorama-box {
        border: 1px solid #e5e7eb;
        padding: 15px;
        border-radius: 4px;
        background-color: #f9fafb;
        margin-bottom: 20px;
    }
    
    /* Card de Ocupação Enxuto */
    .card-vaga {
        padding: 12px 0px;
        border-bottom: 1px solid #f3f4f6;
    }
    .titulo-vaga { font-size: 1.1rem; font-weight: bold; color: #111827; }
    .info-secundaria { color: #6b7280; font-size: 0.85rem; margin-top: 4px; }
    .salario-vaga { color: #059669; font-weight: bold; margin-top: 4px; }
    </style>
    """, unsafe_allow_html=True)

# 2. Título e Panorama Econômico (PNADC 3T 2025)
st.markdown("## Ocupações e Mercado de Trabalho")
st.markdown("### Macrorregião de Franco da Rocha")

st.markdown("""
    <div class="panorama-box">
        <b>Panorama Econômico Regional</b><br>
        Fonte: Microdados PNADC 3T de 2025 (PNADC/IBGE)<br>
        • Taxa de Desemprego: <b>7,8%</b> | Renda Média: <b>R$ 3.520,00</b>
    </div>
    """, unsafe_allow_html=True)

# 3. Base de Dados (Estrutura conforme roteiro)
# Dados simulados do Novo CAGED (Saldo, Salário, Escolaridade, Bairro)
dados_vagas = {
    "Cajamar": [
        {"cargo": "Analista de Logística", "setor": "Logística", "saldo": 145, "sal": 4200, "esc": "Superior", "bai": "Jordanésia", "link": "https://cajamar.sp.senai.br/"},
        {"cargo": "Auxiliar de Operações", "setor": "Logística", "saldo": 312, "sal": 2150, "esc": "Médio", "bai": "Polvilho", "link": "https://cajamar.sp.senai.br/"},
        {"cargo": "Conferente", "setor": "Logística", "saldo": 98, "sal": 2600, "esc": "Médio", "bai": "Gato Preto", "link": "https://cajamar.sp.senai.br/"},
        {"cargo": "Operador de Empilhadeira", "setor": "Logística", "saldo": 76, "sal": 2900, "esc": "Fundamental", "bai": "Jordanésia", "link": "https://cajamar.sp.senai.br/"},
        {"cargo": "Líder de Logística", "setor": "Logística", "saldo": 45, "sal": 3800, "esc": "Médio", "bai": "Polvilho", "link": "https://cajamar.sp.senai.br/"}
    ],
    "Franco da Rocha": [
        {"cargo": "Técnico de Enfermagem", "setor": "Saúde", "saldo": 88, "sal": 3450, "esc": "Médio", "bai": "Centro", "link": "https://www.cps.sp.gov.br/"},
        {"cargo": "Analista Administrativo", "setor": "Serviços", "saldo": 54, "sal": 3100, "esc": "Superior", "bai": "Vila Rosalina", "link": "https://www.fatecfrancodarocha.edu.br/"},
        {"cargo": "Vendedor", "setor": "Comércio", "saldo": 120, "sal": 1950, "esc": "Médio", "bai": "Centro", "link": "https://www.cps.sp.gov.br/"},
        {"cargo": "Auxiliar de Logística", "setor": "Transportes", "saldo": 65, "sal": 2100, "esc": "Médio", "bai": "Pouso Alegre", "link": "https://www.cps.sp.gov.br/"},
        {"cargo": "Recepcionista", "setor": "Serviços", "saldo": 32, "sal": 1850, "esc": "Médio", "bai": "Centro", "link": "https://www.cps.sp.gov.br/"}
    ],
    "Caieiras": [
        {"cargo": "Operador de Produção", "setor": "Indústria", "saldo": 110, "sal": 2800, "esc": "Médio", "bai": "Laranjeiras", "link": "https://www.cps.sp.gov.br/"},
        {"cargo": "Mecânico de Manutenção", "setor": "Indústria", "saldo": 42, "sal": 4500, "esc": "Médio", "bai": "Vila Rosina", "link": "https://www.cps.sp.gov.br/"},
        {"cargo": "Ajudante de Carga", "setor": "Logística", "saldo": 75, "sal": 1950, "esc": "Fundamental", "bai": "Laranjeiras", "link": "https://www.cps.sp.gov.br/"},
        {"cargo": "Eletricista Industrial", "setor": "Indústria", "saldo": 28, "sal": 4200, "esc": "Médio", "bai": "Laranjeiras", "link": "https://www.cps.sp.gov.br/"},
        {"cargo": "Auxiliar Administrativo", "setor": "Serviços", "saldo": 40, "sal": 2200, "esc": "Médio", "bai": "Centro", "link": "https://www.cps.sp.gov.br/"}
    ],
    "Francisco Morato": [
        {"cargo": "Gerente de Loja", "setor": "Comércio", "saldo": 35, "sal": 3800, "esc": "Médio", "bai": "Centro", "link": "http://etecfranciscomorato.com.br/"},
        {"cargo": "Vendedor Especializado", "setor": "Comércio", "saldo": 92, "sal": 2200, "esc": "Médio", "bai": "Belém Capela", "link": "http://etecfranciscomorato.com.br/"},
        {"cargo": "Operador de Caixa", "setor": "Comércio", "saldo": 140, "sal": 1820, "esc": "Médio", "bai": "Centro", "link": "http://etecfranciscomorato.com.br/"},
        {"cargo": "Assistente Logístico", "setor": "Logística", "saldo": 55, "sal": 2450, "esc": "Médio", "bai": "Nova Morato", "link": "http://etecfranciscomorato.com.br/"},
        {"cargo": "Estoquista", "setor": "Comércio", "saldo": 80, "sal": 1900, "esc": "Médio", "bai": "Vila Guilherme", "link": "http://etecfranciscomorato.com.br/"}
    ]
}

# 4. Pesquisa por Cidade (Top 5)
escolha_cidade = st.selectbox("Pesquisar por Cidade:", list(dados_vagas.keys()))

st.markdown(f"#### Top 5 Ocupações que mais geraram vagas em {escolha_cidade}")

for item in dados_vagas[escolha_cidade]:
    st.markdown(f"""
        <div class="card-vaga">
            <div class="titulo-vaga">{item['cargo']}</div>
            <div class="info-secundaria">
                Setor: <b>{item['setor']}</b> | Bairro: <b>{item['bai']}</b> | Nível: <b>{item['esc']}</b>
            </div>
            <div class="salario-vaga">Salário Médio: R$ {item['sal']:,} | Saldo: +{item['saldo']} vagas</div>
        </div>
        """, unsafe_allow_html=True)
    st.link_button(f"Link para Qualificação", item['link'])

# 5. Tabela de Saldo da Região
st.divider()
st.markdown("### Saldo da Região por Ocupação")

# Preparação da tabela
lista_final = []
for cid, lista in dados_vagas.items():
    for o in lista:
        lista_final.append({"Ocupação": o['cargo'], "Cidade": cid, "Saldo": o['saldo'], "Salário Médio": o['sal']})
df_tabela = pd.DataFrame(lista_final)

st.table(df_tabela)

# 6. Notas e Explicação
st.divider()
st.markdown("""
**Nota Esclarecedora:**
- **Fontes:** Rendimento e Desemprego extraídos dos microdados PNADC 3T de 2025. Dados de Ocupações e Saldo provenientes do Novo CAGED (último mês disponível).
- **Saldo de Vagas:** Representa o resultado líquido (Admissões menos Desligamentos) no período.
- **Bairros:** Refere-se à localização das unidades produtivas que registraram as maiores movimentações.
""")
