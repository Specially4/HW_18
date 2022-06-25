from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all_movies(self, filters_dict: dict = None, page: int = 1, length_list: int = 10):
        filter_dict = filters_dict
        if 'genre_id' in filter_dict.keys():
            filter_dict.update(genre_id=int(filter_dict['genre_id']))
        if 'director_id' in filter_dict.keys():
            filter_dict.update(director_id=int(filter_dict['director_id']))
        if 'rating' in filter_dict.keys():
            filter_dict.update(rating=float(filter_dict['rating']))
        if 'year' in filter_dict.keys():
            filter_dict.update(year=int(filter_dict['year']))
        limit = round(page * length_list)  # can set any length of the movie list
        offset = limit - length_list
        movies = self.dao.get_all_movies(limit=limit, offset=offset)

        if len(filter_dict) > 0:
            movies = self.dao.get_by_filter(filter_dict)

        return movies

    def get_one_movie(self, mid: int):
        return self.dao.get_one_movie(mid)

    def add_movies(self, data):
        self.dao.add_movies(data)

    def update_movie(self, data):
        mid = data.get('id')

        movie = self.get_one_movie(mid)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')

        self.dao.update_movie(movie)

        return movie

    def update_partial(self, data):
        mid = data.get('id')

        movie = self.get_one_movie(mid)

        if 'title' in data:
            movie.title = data.get('title')
        if 'description' in data:
            movie.description = data.get('description')
        if 'trailer' in data:
            movie.trailer = data.get('trailer')
        if 'year' in data:
            movie.year = data.get('year')
        if 'rating' in data:
            movie.rating = data.get('rating')
        if 'genre_id' in data:
            movie.genre_id = data.get('genre_id')
        if 'director_id' in data:
            movie.director_id = data.get('director_id')

        self.dao.update_movie(movie)

        return movie

    def delete(self, mid: int):
        movie = self.get_one_movie(mid)

        self.dao.delete(movie)
