from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all_genres(self):
        return self.dao.get_all_genres()

    def get_one_genre(self, gid: int):
        return self.dao.get_one_genre(gid)

    def add_genres(self, data):
        self.dao.add_genres(data)

    def update_genre(self, data):
        gid = data.get('id')
        genre = self.get_one_genre(gid)

        genre.name = data.get('name')

        self.dao.update_genre(genre)

    def update_partial(self, data):
        gid = data.get('id')
        genre = self.get_one_genre(gid)

        if 'name' in data:
            genre.name = data.get('name')

        self.dao.update_genre(genre)

    def delete(self, gid: int):
        genre = self.get_one_genre(gid)

        self.dao.delete(genre)