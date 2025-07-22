import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from reviews.service import ReviewService
from movies.service import MovieService

def show_reviews():
    st.header("Avaliações Cadastradas")
    review_service = ReviewService()
    reviews = review_service.get_reviews()

    if reviews:
        reviews_df = pd.json_normalize(reviews)
        AgGrid(data=reviews_df, reload_data=True, key="reviews_grid")
    else:
        st.warning("Nenhuma avaliação encontrada")

    st.markdown("---")
    st.header("Escolha um filme para avaliar")

    movie_service = MovieService()
    movies = movie_service.get_movies()
    movies_with_photo = [m for m in movies if m.get("photo")]

    selected_movie_id = st.session_state.get("selected_movie_id")
    selected_movie_title = st.session_state.get("selected_movie_title")

    cols = st.columns(min(len(movies_with_photo), 4))
    for idx, movie in enumerate(movies_with_photo):
        with cols[idx % 4]:
            st.image(movie["photo"], caption=movie["title"], use_container_width=True)
            if st.button(f'Avaliar "{movie["title"]}"', key=f"btn_{movie["id"]}"):
                st.session_state["selected_movie_id"] = movie["id"]
                st.session_state["selected_movie_title"] = movie["title"]
                st.rerun()

    if selected_movie_id:
        st.subheader(f"Avaliando: {selected_movie_title}")
        stars = st.slider("Nota", min_value=1.0, max_value=5.0, value=3.0, step=0.5)
        comment = st.text_area("Comentário")

        if st.button("Enviar Avaliação"):
            new_review = review_service.create_review(movie=selected_movie_id, stars=stars, comment=comment)
            if new_review:
                st.success("Avaliação cadastrada com sucesso!")
                del st.session_state["selected_movie_id"]
                del st.session_state["selected_movie_title"]
                st.rerun()
            else:
                st.error("Erro ao cadastrar avaliação!")
