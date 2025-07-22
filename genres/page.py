import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from genres.service import GenreService

def show_genres():
    st.header("Gêneros Cadastrados")
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        genres_df = pd.json_normalize(genres)
        AgGrid(data=genres_df, reload_data=True, key="genres_grid")
    else:
        st.warning("Nenhum gênero encontrado")

    st.markdown("---")
    st.header("Cadastrar novo Gênero")

    with st.form("genre_form", clear_on_submit=True):
        name = st.text_input("Nome do Gênero")
        submitted = st.form_submit_button("Cadastrar")

        if submitted:
            if not name.strip():
                st.warning("Por favor, preencha o nome do gênero.")
            else:
                new_genre = genre_service.create_genre(name=name.strip())
                if new_genre:
                    st.success("Gênero cadastrado com sucesso!")
                    st.rerun()
                else:
                    st.error("Erro ao cadastrar gênero. Verifique os campos")
