from dao.director_dao import DirectorDao
from dao.genre_dao import GenreDao
from dao.movie_dao import MovieDao

from service.director_sevice import DirectorService
from service.genre_service import GenreService
from service.movie_service import MovieService

from dao.model.director import DirectorSchema
from dao.model.genre import GenreSchema
from dao.model.movie import MovieSchema

from setup_db import db

# ______________Экземпляр DAO, Service и Схема для view - director
director_dao = DirectorDao(db.session)
director_service = DirectorService(director_dao)

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

# ______________Экземпляр DAO, Service и Схема для view - genre
genre_dao = GenreDao(db.session)
genre_service = GenreService(genre_dao)

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

# ______________Экземпляр DAO, Service и Схема для view - movie
movie_dao = MovieDao(db.session)
movie_service = MovieService(movie_dao)

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
