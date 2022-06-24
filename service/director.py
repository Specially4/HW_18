from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all_directors(self):
        return self.dao.get_all_directors()

    def get_one_director(self, did: int):
        return self.dao.get_one_director(did)

    def add_directors(self, data):
        return self.dao.add_directors(data)

    def update_director(self, data):
        did = data.get('id')
        director = self.get_one_director(did)

        director.name = data.get('name')

        self.dao.update_director(director)

    def update_partial(self, data):
        did = data.get('id')

        director = self.get_one_director(did)

        if 'name' in data:
            director.name = data.get('name')

        self.dao.update_director(director)

    def delete(self, did: int):
        director = self.get_one_director(did)

        self.dao.delete(director)
