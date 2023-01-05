from dao.genre_dao import GenreDao


class GenreService:
    def __int__(self, dao: GenreDao):
        self.dao = GenreDao

    def get_all(self):
        all_genres = self.dao.get_all()
        return all_genres

    def get_by_id(self, did):
        genre = self.dao.get_one(did)
        return genre
