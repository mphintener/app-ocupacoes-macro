# Dicionário de Salários (Adicione no topo do código)
salarios_regiao = {
    "Logística": {"inicial": "1.800", "pleno": "2.600"},
    "Indústria": {"inicial": "2.100", "pleno": "3.000"},
    "Administração": {"inicial": "1.900", "pleno": "2.800"},
    "Tecnologia": {"inicial": "3.500", "pleno": "5.500"}
}

# No loop das escolas, dentro do expander:
with st.expander(f"✅ {escola['nome']}"):
    st.write(f"**Bairro:** {escola['bairro']}")
    st.write(f"**Cursos:** {', '.join(escola['cursos'])}")
    
    # Exibe a estimativa salarial do setor selecionado
    salario = salarios_regiao.get(setor_sel)
    if salario:
        st.metric(label=f"Média Salarial em {setor_sel}", value=f"R$ {salario['inicial']}", delta="Inicial")
        st.caption(f"Profissionais experientes na região chegam a R$ {salario['pleno']}")
