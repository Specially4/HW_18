from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        return self.session.query(Director).all()

    def get_one_director(self, did: int):
        return self.session.query(Director).filter(Director.id == did).first()

    def add_directors(self, data):
        directors = Director(**data)

        self.session.add(directors)
        self.session.commit()

    def update_director(self, director):

        self.session.add(director)
        self.session.commit()

        return director

    def delete(self, director):

        self.session.delete(director)
        self.session.commit()
