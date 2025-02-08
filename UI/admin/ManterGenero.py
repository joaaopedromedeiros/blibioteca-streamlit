import streamlit as st
import time

class ManterGenero:
    def Main():
        st.header("Cadastro de generos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "inserir", "Atualizar", "Excluir"])
        with tab1: pass
        with tab2: ManterGenero.Inserir()
        with tab3: ManterGenero.Atualizar()
        with tab4: ManterGenero.Excluir()

    def Listar():
        pass

    def Inserir():
        genero = st.text_input("Nome do genero")
        if st.button("Adicionar genero"):
            st.success("Genero adicionado")
            time.sleep(2)
            st.rerun()

    def Atualizar():
        generos = [1,2,3,4,5,6]
        genero = st.selectbox("Generos disponíveis", generos)
        mudanca = st.text_input("Novo nome")
        if st.button("Atualizar genero"):
            st.success("Genero Atualizado")
            time.sleep(2)
            st.rerun()

    def Excluir():
        generos = [1,2,3,4,5,6]
        genero = st.selectbox("Generos disponíveis para excluir", generos)
        if st.button("Excluir genero"):
            st.success("Genero Excluido")
            time.sleep(2)
            st.rerun()

ManterGenero.Main()