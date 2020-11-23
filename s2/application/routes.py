from flask import request, Response
import requests
from application import app
import random

@app.route('/get/animal',methods=['GET','POST'])
def get_name():
    names = ['Lion', 'Snake', 'Cow']
    name = names[random.randrange(0,3)]
    if name == 'Lion':
        noise = 'Raaar!'
        return Response(name, noise, mimetype='text/plain')
    elif name == 'Snake':
        noise = 'Ssss!'
        return Response(name, noise, mimetype='text/plain')
    elif name == 'Cow':
        noise = 'Mooow!'
        return Response(name, noise, mimetype='text/plain')
    else:
        return 'Animal not found!'

