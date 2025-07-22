import streamlit as st
import plotly.express as px
from movies.service import MovieService

def show_home():
    st.header("Estatísticas de Filmes")
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()

    if movie_stats.get('movies_by_genre'):
        st.subheader('Filmes por Gênero')
        fig = px.pie(
            movie_stats['movies_by_genre'],
            values='count',
            names='genre__name',
            title='Filmes por Gênero',
        )
        st.plotly_chart(fig)

    st.subheader("Total de filmes cadastrados")
    st.write(movie_stats.get("total_movies", 0))

    st.subheader('Quantidade de filmes por Gênero')
    for genre in movie_stats.get('movies_by_genre', []):
        st.write(f"{genre['genre__name']}: {genre['count']}")

    st.subheader("Total de Avaliações Cadastradas")
    st.write(movie_stats.get("total_reviews", 0))

    st.subheader("Média Geral de Estrelas nas Avaliações")
    st.write(movie_stats.get("avarage_stars", 0))
