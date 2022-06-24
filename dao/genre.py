from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all_genres(self):
        return self.session.query(Genre).all()

    def get_one_genre(self, gid: int):
        return self.session.query(Genre).filter(Genre.id == gid).first()

    def add_genres(self, data):
        genres = Genre(**data)

        self.session.add(genres)
        self.session.commit()

    def update_genre(self, genre):

        self.session.add(genre)
        self.session.commit()

        return genre

    def delete(self, genre):

        self.session.delete(genre)
        self.session.commit()
