import requests


class Auth:
    def __init__(self):
        self.__base_url = (
            "https://nataliakf.pythonanywhere.com/api/v1/"  # onde a API está em deploy
        )
        self.__auth_url = (
            f"{self.__base_url}authentication/token/"  # link para pegar o token
        )

    def get_token(self, username, password):
        auth_payload = {  # coletando o que o usuário passou
            "username": username,
            "password": password,
        }
        auth_response = requests.post(  # enviando o Post para a API
            self.__auth_url, data=auth_payload
        )
        if (
            auth_response.status_code == 200
        ):  # se deu certo a autenticação retorna o acess token
            return auth_response.json()
        return {
            "error": f"Erro ao autenticar. Status code: {auth_response.status_code}"
        }  # pegando o codigo do error
