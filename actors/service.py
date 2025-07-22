from actors.repository import ActorRepository
import streamlit as st

class ActorService:
    def __init__(self):
        self.actor_repository = ActorRepository()

    def get_actors(self):
        if 'actors' in st.session_state: #se eu já tiver dado um get em atores quando eu estive logada na aplicação
            return st.session_state.actors
        actors =  self.actor_repository.get_actors() #se nunca tiver logado na aplicação
        st.session_state.actors = actors #armazena para dá proxima vez já puxar esse get
        return actors

    def create_actor(self, name, birthday, nationality, photo_file):
        actor = {
            "name": name,
            "birthday": birthday.strftime("%Y-%m-%d"),
            "nationality": nationality,
        }
        actors_files = {"photo": (photo_file.name, photo_file, photo_file.type)}
        new_actor = self.actor_repository.create_actor(actor,actors_files) #armazenando esse novo ator 
        st.session_state.actors.append(new_actor)#adicionando ele na session state para o usuário não ficar desatualizado 
        return new_actor
