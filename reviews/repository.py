import requests
from login.service import logout
import streamlit as st


class ReviewRepository:
    def __init__(self):
        self.__base_url = "https://nataliakf.pythonanywhere.com/api/v1/"  # definindo onde vai bater a requisição
        self.__reviews_url = f"{self.__base_url}reviews/"  # como estamos na app reviews jogando a requisição para ela
        self.__headers = {  # vendo se a pessoa têm autorização (token)
            "Authorization": f"Bearer {st.session_state.token}"  # pegando o bearer token
        }

    def get_reviews(self):
        response = requests.get(self.__reviews_url, headers=self.__headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(
            f"Erro ao obter dados da API. Status code: {response.status_code}"
        )

    def create_review(self, review):  # Post review
        response = requests.post(
            self.__reviews_url,
            headers=self.__headers,  # botando o token do cara
            data=review,
        )
        if response.status_code == 201:  # se deu certo a criação
            return response.json()  # retorna a resposta da API
        if response.status_code == 401:
            # se o token do cara expirar faz ele fazer o logout
            logout()
            return None
        raise Exception(
            f"Erro ao obter dados da API. Status code: {response.status_code}"
        )
