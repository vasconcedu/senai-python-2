import streamlit as st
import datetime as dt
import json

########################################
# Ler e escrever estado da aplicação
########################################

# Ler arquivo de categorias de gastos (TXT)
def ler_categorias_gastos():
    with open("categorias_gastos.txt", "r") as arquivo_categorias:
        categorias_gastos = arquivo_categorias.read().splitlines()
        arquivo_categorias.close()
        return categorias_gastos

# Instancia uma data (utilizada pela funcao ler_gastos)
#   Isso eh necessario porque datetimes nao serializam, e 
#   consequentemente precisam ser serailizados como string e 
#   posteriormente reinstanciados 
def instanciar_data(string_data):
    return dt.datetime.strptime(string_data, "%Y-%m-%d").date()

# Ler arquivo de gastos cadastrados (JSON)
def ler_gastos():
    with open("gastos.json", "r") as arquivo_gastos:
        gastos = json.load(arquivo_gastos)
        for gasto in gastos:
            gasto["data"] = instanciar_data(gasto["data"])
        arquivo_gastos.close()
        return gastos

# Escrever arquivo de gastos cadastrados (JSON)
def escrever_gastos(gastos):
    arquivo_gastos = open("gastos.json", "w")
    arquivo_gastos.write(json.dumps(gastos, default=str))
    arquivo_gastos.close()

# Limpar o arquivo de gastos cadastrados (JSON)
def limpar_gastos():
    st.warning("⚠️ Função limpar_gastos não implementada")

########################################
# Paginas da aplicacao
########################################

# Pagina de cadastro de novo gasto (item de menu "Cadastrar")
def novo_gasto():
    nome = ""
    valor = ""
    data = ""
    categoria = ""
    tipo = ""
    cadastrar = False 

    with st.container():
        st.header("Cadastrar")

        nome = st.text_input("Nome")

        # Organiza os campos de entrada do cadastro em duas colunas 
        cols = st.columns(2)
        valor = cols[0].number_input("Valor", min_value=0.0)
        data = cols[1].date_input("Data", format="DD/MM/YYYY", max_value = "today")

        cols = st.columns(2)
        categoria = cols[0].selectbox("Categoria", ler_categorias_gastos())
        tipo = cols[1].radio("Tipo", ["Variavel", "Fixo"])

        # Botao "Cadastrar"
        cadastrar = st.button("Cadastrar")
    
    # Testa se o usuario preencheu todos os campos necessarios do cadastro
    #   Se sim, efetua o cadastro do novo gasto
    #   Senao, avisa o usuario que tem um erro no preenchimento 
    if cadastrar:
        if (nome == ""):
            st.error("🚨 Gasto não cadastrado: preencha o nome do gasto")
        elif (valor == 0.0):
            st.error("🚨 Gasto não cadastrado: preencha o valor do gasto")
        else:
            gastos = ler_gastos()
            gastos.append({
                "nome": nome,
                "valor": valor,
                "data": data,
                "categoria": categoria,
                "tipo": tipo
            })
            escrever_gastos(gastos)
            st.success("✅ Gasto cadastrado com sucesso")

# Pagina de listagem de gastos cadastrados 
def listar():
    with st.container():
        st.header("Listar")

        gastos = ler_gastos()

        # Se nao tiver nenhum gasto cadastrado, nao listar nada e 
        #   avisar somente "Sem gastos a listar"
        if (len(gastos) == 0):
            st.write("Sem gastos a listar")

        # Para cada gasto, criar um expander com as informacoes dele 
        for gasto in gastos:
            with st.expander("{}: {}".format(gasto["data"].strftime("%d/%m/%y"), gasto["nome"])):
                cols = st.columns(3)
                with cols[0]:
                    st.write("Valor: {}".format(gasto["valor"]))
                with cols[1]:
                    st.write("Categoria: {}".format(gasto["categoria"]))
                with cols[2]:
                    st.write("Tipo: {}".format(gasto["tipo"]))

# Pagina de limpeza dos gastos cadastrados
def limpar():
    with st.container():
        st.header("Limpar")

        # Botao "Limpar"
        limpar = st.button("Limpar")

    if limpar:
        limpar_gastos()

########################################
# Programa principal 
########################################

def main():
    # Menu lateral 
    st.sidebar.title("Meus Gastos")
    opcao = st.sidebar.radio("Navegação", ["Cadastrar", "Listar", "Limpar"])
    st.sidebar.write("Totalmente Existente Tech Software S.A.")

    # Mostrar pagina correspondente a opcao selecionada no menu lateral 
    if opcao == "Cadastrar":
        novo_gasto()
    elif opcao == "Listar":
        listar()
    elif opcao == "Limpar":
        limpar()
    else: 
        novo_gasto()

# Chamada do programa principal 
main()
