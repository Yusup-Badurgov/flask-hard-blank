from dao.director_dao import DirectorDao


class DirectorService:
    def __int__(self, dao: DirectorDao):
        self.dao = DirectorDao

    def get_all(self):
        all_directors = self.dao.get_all()
        return all_directors

    def get_by_id(self, did):
        director = self.dao.get_one(did)
        return director
