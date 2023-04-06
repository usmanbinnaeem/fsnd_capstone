# app.py
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import setup_db, db, Movie, Actor
from auth import requires_auth, AuthError


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    migrate = Migrate(app, db)
    with app.app_context():
        setup_db(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/')
    def hello():
        return 'Hello, Casting Agency!'

    # GET /movies
    @app.route('/movies', methods=['GET'])
    @requires_auth('read:movies')
    def get_movies():
        movies = Movie.query.all()
        return jsonify({"success": True, "movies": [movie.title for movie in movies]})

    # POST /movies
    @app.route('/movies', methods=['POST'])
    @requires_auth('create:movies')
    def add_movie():
        data = request.get_json()

        if not data:
            abort(400)

        title = data.get('title')
        release_date = data.get('release_date')

        if not title or not release_date:
            abort(400)

        movie = Movie(title=title, release_date=release_date)
        db.session.add(movie)
        db.session.commit()

        return jsonify({"success": True, "movie": movie.title})


    # PATCH /movies/<int:movie_id>
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('update:movies')
    def update_movie(payload, movie_id):
        movie = Movie.query.get(movie_id)

        if not movie:
            abort(404)

        data = request.get_json()

        if not data:
            abort(400)

        title = data.get('title')
        release_date = data.get('release_date')

        if title:
            movie.title = title
        if release_date:
            movie.release_date = release_date

        db.session.commit()
        movie.update()

        return jsonify({"success": True, "movie": movie.format()})


    # DELETE /movies/<int:movie_id>
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, movie_id):
        movie = Movie.query.get(movie_id)

        if not movie:
            abort(404)

        db.session.delete(movie)
        db.session.commit()

        return jsonify({"success": True, "movie": movie.title})

    # GET /actors
    @app.route('/actors', methods=['GET'])
    @requires_auth('read:actors')
    def get_actors():
        actors = Actor.query.all()
        return jsonify({"success": True, "actors": [actor.name for actor in actors]})

    # POST /actors
    @app.route('/actors', methods=['POST'])
    @requires_auth('create:actors')
    def add_actor():
        data = request.get_json()

        if not data:
            abort(400)

        name = data.get('name')
        age = data.get('age')
        gender = data.get('gender')
        movie_id = data.get('movie_id')

        if not name or not age or not gender:
            abort(400)

        actor = Actor(name=name, age=age, gender=gender, movie_id=movie_id)
        db.session.add(actor)
        db.session.commit()

        return jsonify({"success": True, "actor": actor.name})


    # PATCH /actors/<int:actor_id>
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('update:actors')
    def update_actor(payload, actor_id):
        actor = Actor.query.get(actor_id)

        if not actor:
            abort(404)

        data = request.get_json()
        name = data.get('name', actor.name)
        age = data.get('age', actor.age)
        gender = data.get('gender', actor.gender)
        movie_id = data.get('movie_id', actor.movie_id)

        actor.name = name
        actor.age = age
        actor.gender = gender
        actor.movie_id = movie_id

        actor.update()

        return jsonify({
            'success': True,
            'actor': actor.format()
        })

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, actor_id):  # Add the 'payload' argument
        actor = Actor.query.get(actor_id)

        if not actor:
            abort(404)

        db.session.delete(actor)
        db.session.commit()

        return jsonify({"success": True, "actor": actor.name})


    ##Error handling

    @app.errorhandler(AuthError)
    def handle_auth_error(exception):
        response = jsonify(exception.error)
        response.status_code = exception.status_code
        return response


    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "error": 400, "message": "Bad request"}), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"success": False, "error": 404, "message": "Resource not found"}), 404

    return app

app=create_app()
if __name__ == '__main__':
    app.run(debug=True)
