import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from movies.service import MovieService
from actors.service import ActorService
from genres.service import GenreService
from datetime import datetime

def show_movies():
    st.header("Filmes Cadastrados")
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=["actors", "genre.id", "photo"], errors="ignore")
        AgGrid(data=movies_df, reload_data=True, key="movies_grid")

        st.subheader("Posters dos Filmes")
        cols = st.columns(4)
        for idx, movie in enumerate(movies):
            with cols[idx % 4]:
                if movie.get("photo"):
                    st.image(movie["photo"], caption=movie["title"], use_container_width=True)
    else:
        st.warning("Nenhum filme encontrado!")

    st.markdown("---")
    st.header("Cadastrar novo Filme")

    with st.form("movie_form", clear_on_submit=True):
        title = st.text_input("Título do Filme")
        release_date = st.date_input("Data de Lançamento", value=datetime.today(), min_value=datetime(1800, 1, 1).date(), max_value=datetime.today(), format="DD/MM/YYYY")
        
        genre_service = GenreService()
        genres = genre_service.get_genres()
        genre_names = {genre["name"]: genre["id"] for genre in genres}
        selected_genre_name = st.selectbox("Gênero", list(genre_names.keys()))

        actor_service = ActorService()
        actors = actor_service.get_actors()
        actor_names = {actor["name"]: actor["id"] for actor in actors}
        selected_actor_names = st.multiselect("Atores/Atrizes", list(actor_names.keys()))
        selected_actors_ids = [actor_names[name] for name in selected_actor_names]

        resume = st.text_area("Resumo do Filme")
        uploaded_file = st.file_uploader("Poster do Filme", type=["jpg", "jpeg", "png"])

        submitted = st.form_submit_button("Cadastrar")
        if submitted:
            if not title.strip():
                st.warning("Por favor, preencha o título do filme.")
            elif not uploaded_file:
                st.warning("Por favor, envie o poster do filme.")
            else:
                new_movie = movie_service.create_movie(
                    title=title.strip(),
                    release_date=release_date,
                    genre=genre_names[selected_genre_name],
                    actors=selected_actors_ids,
                    resume=resume,
                    photo_file=uploaded_file,
                )
                if new_movie:
                    st.success("Filme cadastrado com sucesso!")
                    st.rerun()
                else:
                    st.error("Erro ao cadastrar um filme!")
