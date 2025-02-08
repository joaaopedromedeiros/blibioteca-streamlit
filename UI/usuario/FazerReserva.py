import streamlit as st

class FazerReserva:
    def Main():
        st.header("Reserva de livros")
        livros = [1,2,3,4,5,6]
        #preciso usar pandaa pra gerar uma lista com todos livros disponíveis para reserva e gênero no lado
        #selectbox apenas para selecionar ele e pedir a reserva
        st.selectbox("Selecione os livros", livros)