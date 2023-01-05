from flask_restx import Resource, Namespace
from service.director_sevice import DirectorService
from dao.model.director import DirectorSchema

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        directors = DirectorService.get_all()
        return DirectorSchema.dump(directors), 200


@directors_ns.route('/<int:did>')
class DirectorView(Resource):

    def get(self, did):
        director = DirectorService.get_by_id(did)
        return DirectorSchema.dump(director), 200
