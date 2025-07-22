from reviews.repository import ReviewRepository
import streamlit as st


class ReviewService:  # quando chamar algum service de genres
    def __init__(self):
        self.review_repository = ReviewRepository()  # já chama os dados

    def get_reviews(self):
        if 'reviews' in st.session_state:
            return st.session_state.reviews
        reviews = self.review_repository.get_reviews()
        st.session_state.reviews = reviews
        return reviews

    def create_review(self, movie, stars, comment):
        review = dict(
            movie=movie,
            stars=float(stars),
            comment=comment,
        )
        new_review = self.review_repository.create_review(review)
        st.session_state.reviews.append(new_review)
        return new_review
