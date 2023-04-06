import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from config import TestingConfig
from app import create_app
from dotenv import load_dotenv
from models import setup_db, Actor, Movie

load_dotenv()

ASSISTANT_TOKEN = os.environ['ASSISTANT_TOKEN']
DIRECTOR_TOKEN = os.environ['DIRECTOR_TOKEN']
PRODUCER_TOKEN = os.environ['PRODUCER_TOKEN']


class CastingAgencyTestCase(unittest.TestCase):
    def setUp(self):
       
        self.app = create_app()
        self.client = self.app.test_client

        self.new_actor = {
            'name': 'John Doe',
            'age': 30,
            'gender': 'Male'
        }

        self.new_movie = {
            'title': 'Example Movie',
            'release_date': '2020-01-01'
        }

    def tearDown(self):
        pass

    def get_auth_header(self, token):
        return {'Authorization': f'Bearer {token}'}

    # Test GET /actors
    def test_get_actors_casting_assistant(self):
        res = self.client().get('/actors', headers=self.get_auth_header(ASSISTANT_TOKEN))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsInstance(data['actors'], list)

    def test_get_actors_unauthorized(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected')

    # Test POST /actors
    def test_post_actor_casting_director(self):
        res = self.client().post('/actors', json=self.new_actor, headers=self.get_auth_header(DIRECTOR_TOKEN))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIn('actor', data)
        self.assertEqual(data['actor'], 'John Doe')

    def test_post_actor_unauthorized(self):
        res = self.client().post('/actors', json=self.new_actor, headers=self.get_auth_header(ASSISTANT_TOKEN))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found')

    # Test DELETE /actors/<int:actor_id>
    def test_delete_actor_casting_director(self):
        # Create an actor to delete
        with self.app.app_context():
            actor = Actor(name='Test Actor', age=35, gender='Male')
            actor.insert()
            actor_id = actor.id

        res = self.client().delete(f'/actors/{actor_id}', headers=self.get_auth_header(DIRECTOR_TOKEN))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['actor'], actor.name)

    def test_delete_actor_unauthorized(self):
        res = self.client().delete('/actors/1', headers=self.get_auth_header(ASSISTANT_TOKEN))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found')

    # # Test GET /movies
    def test_get_movies_casting_assistant(self):
        res = self.client().get('/movies', headers=self.get_auth_header(ASSISTANT_TOKEN))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsInstance(data['movies'], list)

    def test_get_movies_unauthorized(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected')

    # # Test POST /movies
    def test_post_movie_executive_producer(self):
        res = self.client().post('/movies', json=self.new_movie, headers=self.get_auth_header(PRODUCER_TOKEN))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIn('movie', data)
        self.assertEqual(data['movie'], 'Example Movie')

    def test_post_movie_unauthorized(self):
        res = self.client().post('/movies', json=self.new_movie, headers=self.get_auth_header(DIRECTOR_TOKEN))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found')

    # Test DELETE /movies/<int:movie_id>
    def test_delete_movie_executive_producer(self):
        # Create a movie to delete
        with self.app.app_context():
            movie = Movie(title='Test Movie', release_date='2020-01-01')
            movie.insert()
            movie_id = movie.id

        res = self.client().delete(f'/movies/{movie_id}', headers=self.get_auth_header(PRODUCER_TOKEN))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['movie'], movie.title)

    def test_delete_movie_unauthorized(self):
        res = self.client().delete('/movies/1', headers=self.get_auth_header(DIRECTOR_TOKEN))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found')

    # Test PATCH /actors/<int:actor_id>
    def test_patch_actor_casting_director(self):
        # Create an actor to update
        with self.app.app_context():
            actor = Actor(name='Test Actor', age=35, gender='Male')
            actor.insert()
            actor_id = actor.id

        update_data = {
            'name': 'Updated Actor'
        }

        res = self.client().patch(f'/actors/{actor_id}', json=update_data, headers=self.get_auth_header(DIRECTOR_TOKEN))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsInstance(data['actor'], dict)
        self.assertEqual(data['actor']['name'], update_data['name'])

    def test_patch_actor_unauthorized(self):
        res = self.client().patch('/actors/1', json={'name': 'New Name'}, headers=self.get_auth_header(ASSISTANT_TOKEN))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found')

    def test_patch_movie_executive_producer(self):
        # Create a movie to update
        with self.app.app_context():
            movie = Movie(title='Test Movie', release_date='2020-01-01')
            movie.insert()
            movie_id = movie.id

        update_data = {
            'title': 'Updated Movie'
        }
        res = self.client().patch(f'/movies/{movie_id}', json=update_data, headers=self.get_auth_header(PRODUCER_TOKEN))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsInstance(data['movie'], dict)
        self.assertEqual(data['movie']['title'], update_data['title'])

    def test_patch_movie_unauthorized(self):
        res = self.client().patch('/movies/1', json={'title': 'New Title'}, headers=self.get_auth_header(DIRECTOR_TOKEN))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()
