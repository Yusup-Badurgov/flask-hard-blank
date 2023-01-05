from flask import request
from flask_restx import Resource, Namespace
from service.movie_service import MovieService
from dao.model.movie import MovieSchema

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):

    def get(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")

        data = {
            "director_id": director,
            "genre_id": genre,
            "year": year
        }

        all_movies = MovieService.filters(data)
        return MovieSchema(many=True).dump(all_movies), 200


    def post(self):
        print('post')
        data = request.json
        new_movie = MovieService.add_movie(data)
        return "", 201, {"location": f"/movies/{new_movie.id}"}



@movies_ns.route('/<int:mid>')
class MovieView(Resource):

    def get(self, mid):
        movie = MovieService.get_one(mid)
        return MovieSchema.dump(movie), 200

    def put(self, mid):
        data = request.json
        data['id'] = mid
        MovieService.update(data)
        return "Updated", 204

    def delete(self, mid):
        MovieService.delete(mid)
        return "Delete", 204
