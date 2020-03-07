import os
import requests
from flask import Flask, render_template, json, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", data=json.loads(get_format_ids()))

@app.route('/test')
def test():
    response = requests.get("http://localhost:5000/api").content
    return response

@app.route('/search')
def search():
    # response = requests.post("http://localhost:5000/search").content
    # return response
    # return json.dumps(data)
    print(':)') # just needed a placeholder to get it to build :)

@app.route('/add', methods=['POST'])
def add():
    # response = requests.post("http://localhost:5000/add").content
    # return response
    country = request.form['country']
    return render_template("add.html", data=json.loads(get_format_by_id(country)))


def get_format_by_id(country):
    url = "http://localhost:5000/api/formatIds/" + country
    response = requests.get(url).content
    return response


def get_format_ids():
    response = requests.get("http://localhost:5000/api/formatIds").content
    return response


if __name__ == '__main__':
    app.run() # to run: flask run -h localhost -p 5005
