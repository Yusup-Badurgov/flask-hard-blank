from dao.movie_dao import MovieDao


class MovieService:

    def __init__(self, dao: MovieDao):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()

    def update(self, data_dict):
        mid = data_dict.get('id')
        movie = self.get_one(mid)
        movie.title = data_dict.get("title")
        movie.description = data_dict.get("description")
        movie.trailer = data_dict.get("trailer")
        movie.year = data_dict.get("year")
        movie.rating = data_dict.get("rating")
        movie.genre_id = data_dict.get("genre_id")
        movie.director_id = data_dict.get("director_id")

        return self.dao.update(movie)

    def add_movie(self, data_dict):
        new_movie = self.dao.create(data_dict)
        return new_movie

    def filters(self, data_dict):
        if data_dict.get('director_id') is not None:
            return self.dao.get_by_director_id(data_dict.get('director_id'))
        elif data_dict.get('genre_id') is not None:
            return self.dao.get_by_genre_id(data_dict.get("genre_id"))
        elif data_dict.get('year') is not None:
            return self.dao.get_by_year(data_dict.get("year"))
        else:
            return self.get_all()
    def delete(self, mid):
        movie = self.get_one(mid)
        return self.dao.delete(movie)

