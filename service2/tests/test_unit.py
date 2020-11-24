from flask import url_for 
from flask_testing import Testcase

from app import app

class TestBase(Testcase):
    def test_animal(self):
        animals = [b'Lion', b'Snake', b'Cow']
        response = self.client.get(url_for('animal'))
        self.assertIn(response.data, animals)

    def test_noise_lion(self):
        response = self.client.post(
            url_for('noise'),
            data="Lion",
            follow_redirects=True
        )
        self.assertIn(b'Roar!', response.data)
    
    def test_noise_snake(self):
        response = self.client.post(
            url_for('noise'),
            data="Snake",
            follow_redirects=True
        )
        self.assertIn(b'Ssss!', response.data)
    
    def test_noise_cow(self):
        response = self.client.post(
            url_for('noise'),
            data="Cow",
            follow_redirects=True
        )
        self.assertIn(b'Mooo!', response.data)