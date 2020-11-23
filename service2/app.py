from flask import Flask, Response, request
import random

app = Flask(__name__)

@app.route('/animal', methods=['GET'])
def animal():
    animals = ["Lion", "Snake", "Cow"]
    return Response(random.choice(animals), mimetype="text/plain")

@app.route('/animal/noise', methods=['POST'])
def noise():
    animal = request.data.decode('utf-8')
    if animal == "Lion":
        noise = "Roar!"
    elif animal == "Snake":
        noise = "Ssss!"
    elif animal == "Cow":
        noise = "Mooo!"
    else:
        return "Animal noise not found!"
    return Response(noise, mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
