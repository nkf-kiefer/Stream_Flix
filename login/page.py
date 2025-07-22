import streamlit as st
from login.service import login


def show_login():
    st.title("Login")

    username = st.text_input("Usuário")
    password = st.text_input(
        label="Senha",
        type="password",  # para esconder a senha
    )

    if st.button("Login"):
        login(  # passando para o service de login esses campos
            username=username, password=password
        )
