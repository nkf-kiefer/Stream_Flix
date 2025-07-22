import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from actors.service import ActorService
from datetime import datetime

def show_actors():
    st.header("Atores/Atrizes Cadastrados")
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        actors_df = pd.json_normalize(actors)
        AgGrid(data=actors_df.drop(columns=["photo"], errors="ignore"), reload_data=True, key="actors_grid")

        st.subheader("Fotos dos Atores/Atrizes")
        cols = st.columns(4)
        for idx, actor in enumerate(actors):
            with cols[idx % 4]:
                st.image(actor["photo"], caption=actor["name"], use_container_width=True)
    else:
        st.warning("Nenhum Ator/Atriz encontrado!")

    st.markdown("---")
    st.header("Cadastrar novo(a) Ator/Atriz")

    with st.form("actor_form", clear_on_submit=True):
        name = st.text_input("Nome do(a) Ator/Atriz")
        birthday = st.date_input("Data de Nascimento", value=datetime.today(), min_value=datetime(1800, 1, 1).date(), max_value=datetime.today(), format="DD/MM/YYYY")
        nationality_dropdown = [
            ("USA", "American"), ("BRA", "Brazilian"), ("PER", "Peruvian"), ("ARG", "Argentinian"),
            ("CAN", "Canadian"), ("MEX", "Mexican"), ("COL", "Colombian"), ("CHI", "Chilean"),
            ("URU", "Uruguayan"), ("PAR", "Paraguayan"), ("BOL", "Bolivian"), ("VEN", "Venezuelan"),
            ("GBR", "British"), ("FRA", "French"), ("GER", "German"), ("ITA", "Italian"),
            ("ESP", "Spanish"), ("POR", "Portuguese"), ("NLD", "Dutch"), ("BEL", "Belgian"),
            ("SWE", "Swedish"), ("NOR", "Norwegian"), ("DNK", "Danish"), ("FIN", "Finnish"),
            ("RUS", "Russian"), ("TUR", "Turkish"), ("GRC", "Greek"), ("POL", "Polish"),
            ("CZE", "Czech"), ("HUN", "Hungarian"), ("CHN", "Chinese"), ("JPN", "Japanese"),
            ("KOR", "South Korean"), ("IND", "Indian"), ("IDN", "Indonesian"), ("PAK", "Pakistani"),
            ("AUS", "Australian"), ("NZL", "New Zealander"), ("ZAF", "South African"), ("NGA", "Nigerian"),
            ("EGY", "Egyptian")
        ]
        nationality = st.selectbox("Nacionalidade", options=nationality_dropdown, format_func=lambda x: x[1])
        uploaded_file = st.file_uploader("Foto do(a) Ator/Atriz", type=["jpg", "jpeg", "png"])

        submitted = st.form_submit_button("Cadastrar")
        if submitted:
            if not uploaded_file:
                st.warning("Por favor, envie uma foto.")
            elif not name:
                st.warning("Por favor, preencha o nome.")
            else:
                try:
                    actor_service.create_actor(name, birthday, nationality[0], uploaded_file)
                    st.success(f'Ator/Atriz "{name}" cadastrado(a) com sucesso!')
                except Exception as e:
                    st.error(f"Erro ao cadastrar: {e}")
