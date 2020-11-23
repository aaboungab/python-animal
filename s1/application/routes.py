from flask import render_template, url_for, Response
from application import app, db
from application.models import Animal
import requests
import random

@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    animalData = Animal.query.all()
    return render_template('home.html', title = 'Home', animals=animalData)

@app.route('/generateView', methods=['GET'])
def generate_view():
    return render_template('generate.html', title= 'Animal Name')

@app.route('/generate', methods=['GET'])
def generate_animal():
    name = requests.get('http://service2:5001/get/animal')
    noise = requests.get('http://service2:5001/get/animal')
    db_data = Animal(name=name.text, noise=noise.text)
    db.session.add(db_data)
    db.session.commit()
    animals_record=db_data.query.all()

    return render_template('generate.html', title='Animal')
