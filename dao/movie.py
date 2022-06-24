from dao.model.movie import Movie
from setup_db import db


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self, limit=1, offset=0):
        movies = self.session.query(Movie).limit(limit).offset(offset)
        return movies

    def get_by_one_filter(self, k_filter: list, v_filter: list):
        f_s = f'self.session.query(Movie).filter(' \
              f'Movie.{k_filter[0]} == {v_filter[0]})'
        return exec(f_s)

    def get_by_two_filter(self, k_filter: list, v_filter: list):
        f_s = f'self.session.query(Movie).filter(' \
              f'Movie.{k_filter[0]} == {v_filter[0]}, ' \
              f'Movie.{k_filter[1]} == {v_filter[1]})'
        return exec(f_s)

    def get_by_three_filter(self, k_filter: list = None, v_filter: list = None):
        f_s = f'self.session.query(Movie).filter(' \
              f'Movie.{k_filter[0]} == {v_filter[0]}, ' \
              f'Movie.{k_filter[1]} == {v_filter[1]}, ' \
              f'Movie.{k_filter[2]} == {v_filter[2]})'
        return exec(f_s)

    def get_by_four_filter(self, k_filter: list = None, v_filter: list = None):
        f_s = f'self.session.query(Movie).filter(' \
              f'Movie.{k_filter[0]} == {v_filter[0]}, ' \
              f'Movie.{k_filter[1]} == {v_filter[1]}, ' \
              f'Movie.{k_filter[2]} == {v_filter[2]}, ' \
              f'Movie.{k_filter[3]} == {v_filter[3]})'
        return exec(f_s)

    def get_by_five_filter(self, k_filter: list = None, v_filter: list = None):
        f_s = f'self.session.query(Movie).filter(' \
              f'Movie.{k_filter[0]} == {v_filter[0]}, ' \
              f'Movie.{k_filter[1]} == {v_filter[1]}, ' \
              f'Movie.{k_filter[2]} == {v_filter[2]}, ' \
              f'Movie.{k_filter[3]} == {v_filter[3]}, ' \
              f'Movie.{k_filter[4]} == {v_filter[4]})'
        return exec(f_s)

    def get_by_six_filter(self, k_filter: list = None, v_filter: list = None):
        f_s = f'self.session.query(Movie).filter(' \
              f'Movie.{k_filter[0]} == {v_filter[0]}, ' \
              f'Movie.{k_filter[1]} == {v_filter[1]}, ' \
              f'Movie.{k_filter[2]} == {v_filter[2]}, ' \
              f'Movie.{k_filter[3]} == {v_filter[3]}, ' \
              f'Movie.{k_filter[4]} == {v_filter[4]}, ' \
              f'Movie.{k_filter[5]} == {v_filter[5]})'
        return exec(f_s)

    def get_one_movie(self, mid: int):
        return self.session.query(Movie).filter(Movie.id == mid).first()

    def add_movies(self, data):
        movies = Movie(**data)

        self.session.add(movies)
        self.session.commit()

    def update_movie(self, movie):

        self.session.add(movie)
        self.session.commit()

        return movie

    def update_partial(self, movie):

        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, movie):

        self.session.delete(movie)
        self.session.commit()
