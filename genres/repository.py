import streamlit as st
import requests
from login.service import logout  # função para fazer o logout do usuário


class GenreRepository:
    def __init__(self):
        self.__base_url = "https://nataliakf.pythonanywhere.com/api/v1/"  # definindo onde vai bater a requisição
        self.__genres_url = f"{self.__base_url}genres/"  # como estamos na app genres jogando a requisição para ela
        self.__headers = {  # vendo se a pessoa têm autorização (token)
            "Authorization": f"Bearer {st.session_state.token}"  # pegando o bearer token
        }

    def get_genres(self):  # Get genres
        response = requests.get(
            self.__genres_url,
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

    def create_genre(self, genre):  # Post genres
        response = requests.post(
            self.__genres_url,
            headers=self.__headers,  # botando o token do cara
            data=genre,
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
