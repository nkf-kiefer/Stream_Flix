import streamlit as st
from api.service import Auth  # importando a autenticação da api


def login(username, password):
    auth_service = Auth()
    response = auth_service.get_token(  # pegando que foi passado pelo user na page de login e jogando na API
        username=username,
        password=password,
    )

    if response.get("error"):  # se der erro com o acesso desse usuário ou senha
        st.error(f"Falha ao realizar login: {response.get('error')}")

    else:  # Se a API liberou o usuário de consumi-lá
        st.session_state.token = response.get(
            "access"
        )  # salvando na sessão do streamlite esse token
        st.rerun()  # para recarregar as permissões e garantir que o usuário vai conseguir usar a app


def logout():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    
    st.rerun()