import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="App Ocupações Macro", layout="wide")

# CSS PARA FONTES ELEGANTES E MENORES
st.markdown("""
    <style>
    [data-testid="stMetricValue"] { font-size: 24px !important; }
    [data-testid="stMetricLabel"] { font-size: 14px !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. BANCO DE DADOS EXPANDIDO (Mais vagas por cidade)
dados_lista = [
    # CAJAMAR
    {"cidade": "Cajamar", "local": "Jordanésia (Logística)", "setor": "Logística", "vagas": 182, "cargo": "Auxiliar de Logística", "salario": 1850},
    {"cidade": "Cajamar", "local": "Jordanésia (Polo II)", "setor": "Logística", "vagas": 25, "cargo": "Conferente", "salario": 2100},
    {"cidade": "Cajamar", "local": "Polvilho", "setor": "Comércio", "vagas": 45, "cargo": "Vendedor Lojista", "salario": 1720},
    {"cidade": "Cajamar", "local": "Distrito Industrial", "setor": "Indústria", "vagas": 12, "cargo": "Operador de Máquina", "salario": 2300},
    
    # CAIEIRAS
    {"cidade": "Caieiras", "local": "Laranjeiras", "setor": "Indústria", "vagas": 64, "cargo": "Ajudante de Produção", "salario": 1980},
    {"cidade": "Caieiras", "local": "Laranjeiras (Metalurgia)", "setor": "Indústria", "vagas": 15, "cargo": "Soldador", "salario": 2800},
    {"cidade": "Caieiras", "local": "Centro", "setor": "Administração", "vagas": 35, "cargo": "Assistente Administrativo", "salario": 2150},
    
    # FRANCO DA ROCHA
    {"cidade": "Franco da Rocha", "local": "Centro", "setor": "Serviços", "vagas": 58, "cargo": "Atendente de SAC", "salario": 1650},
    {"cidade": "Franco da Rocha", "local": "Vila Rosalina", "setor": "Tecnologia", "vagas": 15, "cargo": "Suporte de TI", "salario": 2400},
    {"cidade": "Franco da Rocha", "local": "Pq. Munhoz", "setor": "Saúde", "vagas": 10, "cargo": "Recepcionista Hospitalar", "salario": 1750},
    
    # FRANCISCO MORATO
    {"cidade": "Francisco Morato", "local": "Belas Águas", "setor": "Comércio", "vagas": 72, "cargo": "Operador de Caixa", "salario": 1680},
    {"cidade": "Francisco Morato", "local": "Centro", "setor": "Serviços", "vagas": 40, "cargo": "Vendedor de Serviços", "salario": 1700},
    {"cidade": "Francisco Morato", "local": "Jd. Alegria", "setor": "Educação", "vagas": 8, "cargo": "Monitor Escolar", "salario": 1550}
]
df_vagas = pd.DataFrame(dados_lista)

# 3. CABEÇALHO
st.title("📍 Conexão Ocupações")
st.subheader("Macrorregião de Franco da Rocha")
st.markdown("---")

# 4. PANORAMA REGIONAL
st.markdown("### 📊 Panorama Socioeconômico Regional")
c1, c2 = st.columns(2)
c1.metric("Desemprego (Grande SP)", "8.1%", "-0.4%")
c2.metric("Renda Média PNADC", "R$ 3.240", "Referência")
st.divider()

# 5. BUSCA CENTRALIZADA
st.markdown("### 🔍 Onde você quer trabalhar?")
cidade_sel = st.selectbox(
    "Selecione sua cidade:",
    ["Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"]
)

st.markdown(f"## Oportunidades em {cidade_sel}")
vagas_f = df_vagas[df_vagas['cidade'] == cidade_sel]

# 6. LISTAGEM COM FORMATAÇÃO R$ X.XXX
for _, linha in vagas_f.iterrows():
    with st.container():
        st.subheader(f"💼 {linha['cargo']}")
        
        # Formatação Salário R$ 1.720
        sal_val = f"R$ {linha['salario']:,.0f}".replace(',', '.')
        st.metric(label="Salário Admissional Médio (CAGED)", value=sal_val)
        
        st.write(f"🏢 **Unidade/Bairro:** {linha['local']}")
        st.write(f"📈 **Saldo:** {linha['vagas']} vagas | **Setor:** {linha['setor']}")

        if linha['setor'] in ['Logística', 'Indústria', 'Tecnologia', 'Administração']:
            st.link_button(f"🚀 Ver Cursos Técnicos para {linha['setor']}", "https://www.vestibulinhoetec.com.br/", use_container_width=True)
        else:
            st.link_button(f"💡 Qualificação Profissional (Sebrae)", "https://www.sebrae.com.br/sites/PortalSebrae/ufs/sp?mapa=1", use_container_width=True)
        st.write("---")

# 7. GRÁFICO E TABELA FINAL
st.subheader("📈 Evolução de Vagas na Macrorregião")
df_grafico = pd.DataFrame({'Mês': ['Out', 'Nov', 'Dez', 'Jan'], 'Saldo': [120, 150, -30, 85]})
df_grafico['Mês'] = pd.Categorical(df_grafico['Mês'], categories=['Out', 'Nov', 'Dez', 'Jan'], ordered=True)
st.line_chart(data=df_grafico.sort_values('Mês'), x='Mês', y='Saldo', color="#2ecc71")

with st.expander("📄 Notas Metodológicas e Dados Detalhados"):
    st.markdown("**Fontes:** Novo CAGED/MTE e PNADC/IBGE.")
    st.dataframe(df_grafico, hide_index=True, use_container_width=True)
