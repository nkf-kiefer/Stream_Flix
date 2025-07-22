import streamlit as st
import requests
from login.service import logout  # função para fazer o logout do usuário


class MovieRepository:
    def __init__(self):
        self.__base_url = "https://nataliakf.pythonanywhere.com/api/v1/"  # definindo onde vai bater a requisição
        self.__movies_url = f"{self.__base_url}movies/"  # como estamos na app movies jogando a requisição para ela
        self.__headers = {  # vendo se a pessoa têm autorização (token)
            "Authorization": f"Bearer {st.session_state.token}"  # pegando o bearer token
        }

    def get_movies(self):  # Get movies
        response = requests.get(
            self.__movies_url,
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

    def create_movie(
        self, movies_data, files
    ):  # Post actors e files para pegar a imagem
        response = requests.post(
            self.__movies_url,
            headers=self.__headers,  # botando o token do cara
            data=movies_data,
            files=files,  # como têm foto do filme
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

    def get_movie_stats(self):
        response = requests.get(
            f"{self.__movies_url}stats/",
            headers=self.__headers,
        )
        if response.status_code == 200:  # se deu certo a busca
            return response.json()  # retorna a resposta da API
        if response.status_code == 401:
            logout()
            return None
