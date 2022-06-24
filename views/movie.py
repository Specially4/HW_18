from flask import request
from flask_restx import Namespace, Resource

from container import movie_service
from dao.model.movie import movies_schema, movie_schema

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        filters_dict = {
            "title": request.args.get('title'),
            "description": request.args.get('description'),
            "year": request.args.get('year'),
            "rating": request.args.get('rating'),
            "genre_id": request.args.get('genre_id'),
            "director_id": request.args.get('director_id')
        }
        movies = movie_service.get_all_movies(filter_dict=filters_dict)
        page = request.args.get('page')
        if page:
            movies = movie_service.get_all_movies(filter_dict=filters_dict, page=int(page))

        return movies_schema.dump(movies), 200

    def post(self):
        req_json = request.json
        movie_service.add_movies(req_json)

        return 'Movie appended', 201

    def delete(self):
        pass


@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        movie = movie_service.get_one_movie(mid)
        if movie:
            return movie_schema.dump(movie), 200
        return 'Movie not found', 404

    def path(self, mid: int):
        req_json = request.json
        req_json['id'] = mid
        movie = movie_service.update_partial(req_json)
        if movie:
            return 'Movie updated', 204
        return 'Movie not found', 404

    def put(self, mid: int):
        req_json = request.json
        req_json['id'] = mid
        movie = movie_service.update_movie(req_json)
        if movie:
            return 'Movie updated', 204
        return 'Movie not found', 404

    def delete(self, mid: int):
        movie = movie_service.delete(mid)
        if movie:
            return 'Movie not found', 404
        return 'Movie deleted', 204
