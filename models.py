import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from dotenv import load_dotenv

load_dotenv()

database_path = os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    with app.app_context():
        db.create_all()

class Movie(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(120), nullable=False)
    release_date = Column(db.Date, nullable=False)
    actors = db.relationship('Actor', backref='movie', lazy=True)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'actors': [actor.format() for actor in self.actors]
        }

    def __repr__(self):
        return f'<Movie {self.title}>'

class Actor(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)
    movie_id = Column(Integer, db.ForeignKey('movie.id'), nullable=True)

    def __init__(self, name, age, gender, movie_id=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.movie_id = movie_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'movie_id': self.movie_id
        }

    def __repr__(self):
        return f'<Actor {self.name}>'
