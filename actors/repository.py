import streamlit as st
import requests
from login.service import logout  # função para fazer o logout do usuário


class ActorRepository:
    def __init__(self):
        self.__base_url = "https://nataliakf.pythonanywhere.com/api/v1/"  # definindo onde vai bater a requisição
        self.__actors_url = f"{self.__base_url}actors/"  # como estamos na app actors jogando a requisição para ela
        self.__headers = {  # vendo se a pessoa têm autorização (token)
            "Authorization": f"Bearer {st.session_state.token}"  # pegando o bearer token
        }

    def get_actors(self):  # Get actors
        response = requests.get(
            self.__actors_url,
            headers=self.__headers,  # passando a autorização
        )
        if response.status_code == 200:  # se deu certo a busca
            return response.json()  # retorna a resposta da API
        if (
            response.status_code == 401
        ):  # se o token do cara expirar faz ele fazer o logout
            logout()
            return None
        raise Exception(
            f"Erro ao obter dados da API. Status code: {response.status_code}"
        )

    def create_actor(
        self, actor_data, files
    ):  # Post actors e files para pegar a imagem
        response = requests.post(
            self.__actors_url,
            headers=self.__headers,  # botando o token do cara
            data=actor_data,
            files=files,
        )
        if response.status_code == 201:  # se deu certo a criação
            return response.json()  # retorna a resposta da API
        if (
            response.status_code == 401
        ):  # se o token do cara expirar faz ele fazer o logout
            logout()
            return None
        raise Exception(
            f"Erro ao obter dados da API. Status code: {response.status_code}"
        )
