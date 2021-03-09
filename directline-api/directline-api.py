from flask import Flask, request
import requests
from uuid import uuid4

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Microsoft Bot Framework Direct Line API</h1>"

@app.route('/api/directline/tokens/generate', methods=['GET'])
def generate_token():
    url = 'https://directline.botframework.com/v3/directline/tokens/generate'
    secret = 'uzEqtToqsAY.jFKlI0ltLDzLjq0Kj_lD2YPTDempUQdxriJ7g3GWB-g'
    body = {'user':{"id": str(uuid4())}}
    x = requests.post(url, data = body, headers = {"Authorization": "Bearer" + " " + secret})
    return x.json()

@app.route('/api/directline/tokens/refresh', methods=['GET'])
def refresh_token():
    url = 'https://directline.botframework.com/v3/directline/tokens/refresh'
    data = request.get_json(force=True)
    token = data['token']
    x = requests.post(url, headers = {"Authorization": "Bearer" + " " + token})
    return x.json()

app.run()