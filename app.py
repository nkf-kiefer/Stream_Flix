import streamlit as st
from genres.page import show_genres
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviews
from login.page import show_login 
from home.page import show_home

def main (): #script para o streamlit saber qual arquivo rodar 
    if 'token' not in st.session_state: #se o usuário n tiver nenhum acesso salvo no streamlite
        show_login() #direciona para a página de login
    else:
        st.title('Flix App')

        menu_option = st.sidebar.selectbox( #fazendo um menu com as opções para o usuário clicar
            'Selecione uma opção',
            ['Início','Gêneros','Atores/atrizes','Filmes','Avaliações']
        )

        if menu_option == 'Início':
            show_home()

        if menu_option == 'Gêneros':
            show_genres()

        if menu_option == 'Atores/atrizes':
            show_actors()

        if menu_option == 'Filmes':
            show_movies()

        if menu_option == 'Avaliações':
            show_reviews()


if __name__ == '__main__': #boas práticas
     main()