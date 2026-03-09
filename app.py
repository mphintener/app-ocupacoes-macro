import streamlit as st
import pandas as pd
import plotly.express as px

# ─────────────────────────────────────────────────────────────
# CONFIGURAÇÃO
# ─────────────────────────────────────────────────────────────
st.set_page_config(page_title="BI Macro Franco da Rocha", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117 !important; color: #ffffff !important; font-size: 0.82rem; }
    .header-dark { background-color: #1a1d23; padding: 12px; border-radius: 10px; border: 1px solid #334155; margin-bottom: 15px; }
    .header-dark h2 { font-size: 1.05rem !important; margin: 2px 0; color: #f8fafc; }
    .card-vaga { background-color: #1a1d23; padding: 10px; border-radius: 8px; margin-bottom: 8px; border-left: 4px solid #3b82f6; }
    .dark-table { width: 100%; border-collapse: collapse; font-size: 0.72rem; background-color: #111418; color: white; border-radius: 8px; overflow: hidden; margin-top: 10px; }
    .dark-table th { background-color: #1e293b; padding: 8px; text-align: left; color: #94a3b8; }
    .dark-table td { padding: 6px 8px; border-bottom: 1px solid #1e293b; }
    .salario-bi { color: #10b981; font-weight: bold; font-size: 0.78rem; }
    .badge-green  { background:#064e3b; color:#34d399; padding:3px 10px; border-radius:4px; font-size:0.72rem; font-weight:bold; }
    .badge-yellow { background:#3d2e00; color:#fbbf24; padding:3px 10px; border-radius:4px; font-size:0.72rem; font-weight:bold; }
    .instrucao { background:#1a1d23; border-left:3px solid #3b82f6; padding:10px 14px; border-radius:6px; margin:8px 0; font-size:0.78rem; color:#cbd5e1; }
    </style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# MUNICÍPIOS DA MACRORREGIÃO (códigos IBGE)
# ─────────────────────────────────────────────────────────────
MUNICIPIOS = {
    3508504: "Cajamar",
    3515145: "Caieiras",
    3515103: "Cabreúva",
    3521804: "Franco da Rocha",
    3521606: "Francisco Morato",
    3515608: "Campo Limpo Paulista",
    3556206: "Várzea Paulista",
}
CODIGOS_IBGE = list(MUNICIPIOS.keys())

# ─────────────────────────────────────────────────────────────
# DADOS ESTÁTICOS DE FALLBACK
# ─────────────────────────────────────────────────────────────
DADOS_ESTATICOS = pd.DataFrame([
    {"municipio_nome": "Cajamar",          "ocupacao": "Auxiliar de Logística",    "saldo": 412, "salario_medio": 2150, "curso": "Gestão de Estoques",    "escola": "Qualifica SP"},
    {"municipio_nome": "Cajamar",          "ocupacao": "Analista de Logística",    "saldo": 142, "salario_medio": 4200, "curso": "Logística FATEC",       "escola": "FATEC"},
    {"municipio_nome": "Cajamar",          "ocupacao": "Conferente",               "saldo": 85,  "salario_medio": 2600, "curso": "Operações de CD",       "escola": "ETEC"},
    {"municipio_nome": "Cajamar",          "ocupacao": "Líder de Operações",       "saldo": 32,  "salario_medio": 5100, "curso": "Gestão de Equipes",     "escola": "FATEC"},
    {"municipio_nome": "Franco da Rocha",  "ocupacao": "Técnico de Enfermagem",    "saldo": 45,  "salario_medio": 3450, "curso": "Técnico em Enfermagem", "escola": "ETEC Franco"},
    {"municipio_nome": "Franco da Rocha",  "ocupacao": "Enfermeiro",               "saldo": 12,  "salario_medio": 4800, "curso": "Gestão Hospitalar",     "escola": "FATEC Franco"},
    {"municipio_nome": "Franco da Rocha",  "ocupacao": "Auxiliar Administrativo",  "saldo": 28,  "salario_medio": 2300, "curso": "Gestão Empresarial",    "escola": "ETEC"},
    {"municipio_nome": "Franco da Rocha",  "ocupacao": "Recepcionista",            "saldo": 19,  "salario_medio": 1950, "curso": "Atendimento VIP",       "escola": "Qualifica SP"},
    {"municipio_nome": "Caieiras",         "ocupacao": "Mecânico Industrial",      "saldo": 28,  "salario_medio": 4500, "curso": "Mecânica Industrial",   "escola": "ETEC Caieiras"},
    {"municipio_nome": "Caieiras",         "ocupacao": "Operador de Produção",     "saldo": 115, "salario_medio": 2850, "curso": "Processos Industriais", "escola": "Qualifica SP"},
    {"municipio_nome": "Caieiras",         "ocupacao": "Técnico em Química",       "saldo": 14,  "salario_medio": 3900, "curso": "Química Industrial",    "escola": "ETEC"},
    {"municipio_nome": "Caieiras",         "ocupacao": "Eletricista",              "saldo": 22,  "salario_medio": 3200, "curso": "Elétrica Predial",      "escola": "ETEC"},
    {"municipio_nome": "Francisco Morato", "ocupacao": "Vendedor",                 "saldo": 89,  "salario_medio": 2050, "curso": "Técnicas de Vendas",    "escola": "Qualifica SP"},
    {"municipio_nome": "Francisco Morato", "ocupacao": "Gerente de Loja",          "saldo": 15,  "salario_medio": 3800, "curso": "Gestão Comercial",      "escola": "ETEC Morato"},
    {"municipio_nome": "Francisco Morato", "ocupacao": "Auxiliar de Almoxarifado", "saldo": 24,  "salario_medio": 2100, "curso": "Logística Básica",      "escola": "Qualifica SP"},
    {"municipio_nome": "Francisco Morato", "ocupacao": "Balconista",               "saldo": 37,  "salario_medio": 1850, "curso": "Varejo",                "escola": "ETEC"},
])

# ─────────────────────────────────────────────────────────────
# OPÇÃO B — BASEDOSDADOS
# ─────────────────────────────────────────────────────────────
@st.cache_data(ttl=60 * 60 * 24 * 7, show_spinner=False)
def tentar_basedosdados():
    try:
        import basedosdados as bd
        # Tenta ler billing_project_id de diferentes locais nos Secrets
        billing = ""
        try:
            billing = st.secrets["billing_project_id"]
        except Exception:
            pass
        if not billing:
            try:
                billing = st.secrets["gcp_service_account"]["project_id"]
            except Exception:
                pass
        if not billing:
            return None, "billing_project_id não configurado nos Secrets"

        codigos = ", ".join(str(c) for c in CODIGOS_IBGE)
        df = bd.read_sql(
            f"""
            SELECT id_municipio, cbo_2002 AS cbo, tipo_movimentacao, salario_mensal
            FROM `basedosdados.br_me_caged.microdados_movimentacao`
            WHERE CAST(id_municipio AS INT64) IN ({codigos})
              AND ano >= 2024
            LIMIT 500000
            """,
            billing_project_id=billing,
        )
        if df.empty:
            return None, "Nenhum dado retornado"

        df["municipio_nome"] = pd.to_numeric(df["id_municipio"], errors="coerce").map(MUNICIPIOS)
        adm = df[df["tipo_movimentacao"].astype(str) == "1"].groupby(["municipio_nome","cbo"]).agg(
            admissoes=("salario_mensal","count"), salario_medio=("salario_mensal","mean")).reset_index()
        dem = df[df["tipo_movimentacao"].astype(str) == "2"].groupby(["municipio_nome","cbo"]).agg(
            desligamentos=("salario_mensal","count")).reset_index()
        res = adm.merge(dem, on=["municipio_nome","cbo"], how="left").fillna(0)
        res["saldo"] = (res["admissoes"] - res["desligamentos"]).astype(int)
        res["salario_medio"] = res["salario_medio"].round(0).astype(int)
        res = res.rename(columns={"cbo": "ocupacao"})
        res = res[res["saldo"] > 0].sort_values("saldo", ascending=False)
        return res[["municipio_nome","ocupacao","saldo","salario_medio"]], None
    except ImportError:
        return None, "Pacote basedosdados não instalado (adicione ao requirements.txt)"
    except Exception as e:
        return None, str(e)


# ─────────────────────────────────────────────────────────────
# OPÇÃO A — PROCESSAR CSV DO GOV.BR
# ─────────────────────────────────────────────────────────────
def processar_csv_caged(arquivo):
    try:
        nome = arquivo.name.lower()
        if nome.endswith(".xlsx") or nome.endswith(".xls"):
            df_raw = pd.read_excel(arquivo, dtype=str)
        else:
            for enc in ["latin-1", "utf-8", "cp1252"]:
                try:
                    df_raw = pd.read_csv(arquivo, sep=";", encoding=enc, dtype=str)
                    arquivo.seek(0)
                    break
                except Exception:
                    arquivo.seek(0)

        df_raw.columns = [c.strip().lower().replace(" ","_") for c in df_raw.columns]

        COL_MAP = {
            "municipio": ["municipio","id_municipio","codmun","codigomunicipio"],
            "tipo_mov":  ["tipomovimentacao","tipo_movimentacao","tipomov"],
            "salario":   ["salariomensal","salario_mensal","vl_salario_mensal"],
            "cbo":       ["cbo2002ocupacao","cbo_2002_ocupacao","cbo2002","cbo"],
            "desc_cbo":  ["descricaocbo","descricao_cbo","nm_cbo"],
        }
        col = {}
        for chave, opcoes in COL_MAP.items():
            for op in opcoes:
                if op in df_raw.columns:
                    col[chave] = op
                    break

        if "municipio" not in col:
            return None, f"Coluna município não encontrada. Colunas: {list(df_raw.columns)}"
        if "tipo_mov" not in col:
            return None, f"Coluna tipo_movimentacao não encontrada. Colunas: {list(df_raw.columns)}"

        df_raw[col["municipio"]] = pd.to_numeric(df_raw[col["municipio"]], errors="coerce")
        df = df_raw[df_raw[col["municipio"]].isin(CODIGOS_IBGE)].copy()

        if df.empty:
            return None, f"Nenhum município da macrorregião encontrado. Códigos: {CODIGOS_IBGE}"

        df["is_adm"] = df[col["tipo_mov"]].astype(str).str.strip().isin(["1","Admissão"])
        df["is_dem"] = df[col["tipo_mov"]].astype(str).str.strip().isin(["2","Desligamento"])
        df["salario_num"] = pd.to_numeric(
            df[col.get("salario","")].astype(str).str.replace(",",".") if "salario" in col else "0",
            errors="coerce").fillna(0) if "salario" in col else 0

        ocup_col = col.get("desc_cbo", col.get("cbo", None))
        df["ocupacao"] = df[ocup_col].astype(str).str.strip().str.title() if ocup_col else "Não identificada"
        df["municipio_nome"] = df[col["municipio"]].map(MUNICIPIOS)

        adm = df[df["is_adm"]].groupby(["municipio_nome","ocupacao"]).agg(
            admissoes=("is_adm","sum"), salario_medio=("salario_num","mean")).reset_index()
        dem = df[df["is_dem"]].groupby(["municipio_nome","ocupacao"]).agg(
            desligamentos=("is_dem","sum")).reset_index()
        res = adm.merge(dem, on=["municipio_nome","ocupacao"], how="left").fillna(0)
        res["saldo"] = (res["admissoes"] - res["desligamentos"]).astype(int)
        res["salario_medio"] = res["salario_medio"].round(0).astype(int)
        res = res[res["saldo"] > 0].sort_values("saldo", ascending=False)

        if res.empty:
            return None, "Arquivo processado, mas saldo positivo = 0. Verifique o período."
        return res[["municipio_nome","ocupacao","saldo","salario_medio"]], None
    except Exception as e:
        return None, f"Erro: {str(e)}"


# ─────────────────────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────────────────────
st.markdown("""
    <div class="header-dark">
        <div style="font-size:0.58rem; color:#64748b; font-weight:bold; letter-spacing:1px;">📊 MÉDIAS MACRORREGIÃO (PNADC/IBGE)</div>
        <h2>Mercado de Trabalho — Macro Franco da Rocha</h2>
        <div style="margin-top:10px; display:flex; justify-content:space-between; border-top:1px solid #334155; padding-top:8px;">
            <div><small style="color:#94a3b8; font-size:0.62rem;">Renda Média Região</small><br><b style="font-size:0.85rem;">R$ 3.520,00</b></div>
            <div style="text-align:right;"><small style="color:#94a3b8; font-size:0.62rem;">Taxa Desocupação</small><br><b style="font-size:0.85rem; color:#f87171;">7,8%</b></div>
        </div>
    </div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# PAINEL DE ATUALIZAÇÃO
# ─────────────────────────────────────────────────────────────
with st.expander("🔄 Atualizar dados do CAGED", expanded=False):
    tab_csv, tab_bd = st.tabs(["📁 Opção A — Upload CSV (gov.br)", "☁️ Opção B — Basedosdados (automático)"])

    with tab_csv:
        st.markdown("""
            <div class="instrucao">
            <b>Como baixar o arquivo:</b><br>
            1. Acesse <b>portalftp.mte.gov.br</b><br>
            2. Pasta: <b>CAGED → Novo CAGED → CAGEDMOV</b><br>
            3. Baixe o <code>.txt</code> do mês desejado, extraia o .7z e faça upload aqui
            </div>
        """, unsafe_allow_html=True)

        arquivo = st.file_uploader("Arraste o arquivo aqui", type=["csv","txt","xlsx","xls"])
        if arquivo:
            with st.spinner("Processando..."):
                df_csv, erro_csv = processar_csv_caged(arquivo)
            if erro_csv:
                st.error(f"❌ {erro_csv}")
            else:
                st.success(f"✅ {len(df_csv)} ocupações carregadas!")
                st.session_state["df_ativo"] = df_csv
                st.session_state["fonte_label"] = f"Novo CAGED — {arquivo.name}"

    with tab_bd:
        st.markdown("""
            <div class="instrucao">
            <b>Para ativar atualização automática:</b><br>
            1. Acesse <b>console.cloud.google.com</b> com Gmail pessoal<br>
            2. Crie um projeto → ative o BigQuery<br>
            3. Streamlit Cloud → Settings → Secrets → adicione:<br>
            <code>billing_project_id = "seu-project-id"</code>
            </div>
        """, unsafe_allow_html=True)

        if st.button("🔍 Testar conexão com Basedosdados"):
            with st.spinner("Conectando..."):
                df_bd, erro_bd = tentar_basedosdados()
            if erro_bd:
                st.error(f"❌ {erro_bd}")
            else:
                st.success(f"✅ {len(df_bd)} ocupações carregadas!")
                st.session_state["df_ativo"] = df_bd
                st.session_state["fonte_label"] = "Novo CAGED — Basedosdados (automático)"

# ─────────────────────────────────────────────────────────────
# FONTE DE DADOS ATIVA
# ─────────────────────────────────────────────────────────────
if "df_ativo" in st.session_state:
    df = st.session_state["df_ativo"]
    fonte_label = st.session_state.get("fonte_label", "Dados carregados")
    badge = '<span class="badge-green">🟢 Dados atualizados</span>'
else:
    df = DADOS_ESTATICOS
    fonte_label = "Dados estáticos (Jan/2026) — use o painel acima para atualizar"
    badge = '<span class="badge-yellow">🟡 Dados estáticos — clique em Atualizar dados acima</span>'

st.markdown(badge, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# CARDS POR MUNICÍPIO
# ─────────────────────────────────────────────────────────────
st.markdown("<h4 style='font-size:0.95rem; margin-top:14px;'>📍 Oportunidades Locais</h4>", unsafe_allow_html=True)
cid_sel = st.selectbox("Selecione o Município:", sorted(df["municipio_nome"].dropna().unique()))

for _, r in df[df["municipio_nome"] == cid_sel].head(10).iterrows():
    sal_fmt = f"{int(r['salario_medio']):,.0f}".replace(",",".")
    curso_info = f"📚 {r['curso']} ({r['escola']})" if "curso" in r.index and pd.notna(r.get("curso")) else ""
    st.markdown(f"""
        <div class="card-vaga">
            <b>{r['ocupacao']}</b><br>
            {"<small style='color:#94a3b8;'>" + curso_info + "</small><br>" if curso_info else ""}
            <div style="display:flex; justify-content:space-between; font-size:0.72rem; margin-top:5px;">
                <span>Saldo CAGED: <b style="color:#34d399;">+{int(r['saldo'])}</b></span>
                <span class="salario-bi">R$ {sal_fmt} (médio)</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# GRÁFICO
st.markdown("<h4 style='font-size:0.95rem;'>🏆 Top 10 Ocupações (Região)</h4>", unsafe_allow_html=True)
top10 = df.nlargest(10, "saldo")
fig = px.bar(top10, x="saldo", y="ocupacao", orientation="h", color="municipio_nome",
             template="plotly_dark", height=300, text_auto=True,
             labels={"saldo":"Saldo","ocupacao":"Ocupação","municipio_nome":"Município"})
fig.update_layout(font=dict(size=9), margin=dict(l=0,r=0,t=10,b=0),
                  showlegend=True, legend=dict(font=dict(size=8)))
st.plotly_chart(fig, use_container_width=True)

# TABELA
st.markdown("<h4 style='font-size:0.95rem;'>📊 Tabela BI: Ocupações da Macrorregião</h4>", unsafe_allow_html=True)
st.caption(f"Fonte: {fonte_label}")
html_table = """<table class="dark-table">
    <thead><tr><th>Ocupação</th><th>Município</th><th>Saldo</th><th>Salário Médio</th></tr></thead><tbody>"""
for _, row in df.sort_values("saldo", ascending=False).head(50).iterrows():
    sal_tab = f"{int(row['salario_medio']):,.0f}".replace(",",".")
    html_table += f"<tr><td>{row['ocupacao']}</td><td>{row['municipio_nome']}</td><td>+{int(row['saldo'])}</td><td class='salario-bi'>R$ {sal_tab}</td></tr>"
html_table += "</tbody></table>"
st.markdown(html_table, unsafe_allow_html=True)
