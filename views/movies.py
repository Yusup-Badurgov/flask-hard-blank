from flask import request
from flask_restx import Resource, Namespace
from implemented import movie_service, movies_schema, movie_schema

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):

    def get(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")

        data_dict = {
            "director_id": director,
            "genre_id": genre,
            "year": year
        }

        all_movies = movie_service.filters(data_dict)
        return movies_schema.dump(all_movies), 200

    def post(self):
        print('post')
        data = request.json
        new_movie = movie_service.add_movie(data)
        return "", 201, {"location": f"/movies/{new_movie.id}"}


@movies_ns.route('/<int:mid>')
class MovieView(Resource):

    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        data = request.json
        data['id'] = mid
        movie_service.update(data)
        return "Updated", 204

    def delete(self, mid):
        movie_service.delete(mid)
        return "Delete", 204
