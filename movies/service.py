from movies.repository import MovieRepository
import streamlit as st


class MovieService:
    def __init__(self):
        self.movie_repository = MovieRepository()

    def get_movies(self):
        if "movies" in st.session_state:
            return st.session_state.movies
        movies = self.movie_repository.get_movies()
        st.session_state.movies = movies
        return movies

    def create_movie(self, title, release_date, genre, actors, resume, photo_file):
        movie = dict(
            title=title,
            release_date=release_date,
            genre=genre,
            actors=actors,
            resume=resume,
        )
        movies_files = {"photo": (photo_file.name, photo_file, photo_file.type)}
        new_movie = self.movie_repository.create_movie(movie,movies_files)
        st.session_state.movies.append(new_movie)
        return new_movie
    
    def get_movie_stats(self):
        return self.movie_repository.get_movie_stats()
