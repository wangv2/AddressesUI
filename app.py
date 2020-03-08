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
    print("IN SEARCH")
    return render_template("searchResults.html")

@app.route('/addForm', methods=['POST'])
def addForm():
    country = request.form['country']
    return render_template("addForm.html", data=json.loads(api_get_format_by_id(country)))

@app.route('/searchByForm', methods=['POST'])
def searchByForm():
    country = request.form['country']
    return render_template("searchByForm.html", data=json.loads(api_get_format_by_id(country)))

@app.route('/searchAcrossForm', methods=['POST'])
def searchAcrossForm():
    country = 'GENERAL'
    return render_template("searchAcrossForm.html", data=json.loads(api_get_format_by_id(country)))

@app.route('/add', methods=['POST'])
def add():
    addInput = request.form.to_dict()
    print(addInput)
    url = "http://localhost:5000/api/add"
    headers = {'Content-type': 'application/json'}
    response = json.loads(requests.post(url, json=addInput, headers=headers).content.decode("utf-8"))
    print(response)
    return render_template("addResults.html", data=response)

# broken - added inside add() function and it works  ¯\_(ツ)_/¯
# def api_add(addInput):
#     url = "http://localhost:5000/api/add"
#     headers = {'Content-type': 'application/json'}
#     response = requests.post(url, json=addInput, headers=headers)
#     return response


def api_get_format_by_id(country):
    url = "http://localhost:5000/api/formats/" + country
    response = requests.get(url).content
    return response


def get_format_ids():
    response = requests.get("http://localhost:5000/api/formatIds").content
    print(response)
    return response


if __name__ == '__main__':
    app.run() # to run: flask run -h localhost -p 5005
