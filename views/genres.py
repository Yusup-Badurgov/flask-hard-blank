from flask_restx import Resource, Namespace
from service.genre_service import GenreService
from dao.model.genre import GenreSchema
genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):

    def get(self):
        genres = GenreService.get_all()
        return GenreSchema.dump(genres), 200


@genres_ns.route('/<int:gid>')
class GenreView(Resource):

    def get(self, gid):
        genre = GenreService.get_by_id(gid)
        return GenreSchema.dump(genre), 200
