import streamlit as st
import time


class ManterLivroUI:
    def Main():
        st.header("Cadastro de livros")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterLivroUI.Listar()
        with tab2: ManterLivroUI.Inserir()
        with tab3: ManterLivroUI.Atualizar()
        with tab4: ManterLivroUI.Excluir()

    def Inserir():
        livro = st.text_input("Nome do novo livro")
        autor = st.text_input("Nome do autor")
        idGenero = st.text_input("Genero do livro")
        editora = st.text_input("Editora")
        ano = st.text_input("Ano")
        quantidade = st.text_input("Quantidade")

        if st.button("Cadastrar"):
            st.success("Livro cadastrado!")
            time.sleep(2)
            st.rerun()
    
    def Listar():
        pass

    def Excluir():
        livros = [1,2,3,4,5,6]
        st.selectbox("Selecione o livro",livros)
        if st.button("Excluir Livro"):
            st.success("Livro excluido")
            time.sleep(2)
            st.rerun()

    def Atualizar():
        livros = [10,99,6,7,9,8]
        st.selectbox("Selecione o livro", livros)
        livro = st.text_input("Novo nome")
        autor = st.text_input("Novo nome do autor")
        idGenero = st.text_input("Novo genero")
        editora = st.text_input("Nova editora")
        ano = st.text_input("Novo Ano")
        quantidade = st.text_input("Nova Quantidade")

        if st.button("Atualizar cadastro"):
            st.success("Livro excluido com sucesso")
            time.sleep(2)
            st.rerun
        
        
   



ManterLivroUI.Main()
