import os
import requests
from flask import Flask, render_template, json, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    configFile = formats()
    # countries as dict
    countries = json.loads(json.dumps({'R':'Red', 'Be':'Blue', 'Bk':'Black', 'O':'Orange'}))          # json.loads(configFile).keys())
    print(type(countries))
    return render_template("index.html", data=countries)
   
@app.route('/test')
def test():
    response = requests.get("http://localhost:5000/api").content
    return response

@app.route('/search')
def search():
    # response = requests.post("http://localhost:5000/search").content
    # return response
    return json.dumps(data)

@app.route('/add')
def add():
    response = requests.post("http://localhost:5000/add").content
    return response


def formats():
    response = requests.get("http://localhost:5000/api/formats").content
    return response


if __name__ == '__main__':
    app.run(host="localhost", port=5005, debug=True)