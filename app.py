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

    if 'line1' not in addInput:
        addInput['line1'] = ""
    if 'city' not in addInput:
        addInput['city'] = ""
    if 'region' not in addInput:
        addInput['region'] = ""
    if 'postalCode' not in addInput:
        addInput['postalCode'] = ""
    if 'other' not in addInput:
        addInput['other'] = ""

    url = "http://localhost:5000/api/add"
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, json=addInput, headers=headers)
    response_content = response.content.decode("utf-8")
    response_status = response.status_code

    if response_status == 200: 
        return render_template("addResults.html", data=json.loads(response_content))
    else: 
        error_message = "ERROR: " + str(response_status) + " - " + response_content
        return render_template("error.html", data=error_message)

@app.route('/search', methods=['POST'])
def search():
    searchInput = request.form.to_dict()
    searchInput = remove_empty_filters(searchInput)

    url = "http://localhost:5000/api/search"
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, json=searchInput, headers=headers)
    response_content = response.content.decode("utf-8")
    response_status = response.status_code

    if response_status == 200: 
        return render_template("searchResults.html", data=json.loads(response_content))
    else: 
        error_message = "ERROR: " + str(response_status) + " - " + response_content
        return render_template("error.html", data=error_message)
    
# broken - added inside add() function and it works  ¯\_(ツ)_/¯
# def api_add(addInput):
#     url = "http://localhost:5000/api/add"
#     headers = {'Content-type': 'application/json'}
#     response = requests.post(url, json=addInput, headers=headers)
#     return response

def remove_empty_filters(filters):
    for key in list(filters):
        if filters.get(key) == "":
            del filters[key]
    return filters

def api_get_format_by_id(country):
    url = "http://localhost:5000/api/formats/" + country
    response = requests.get(url).content
    return response

def get_format_ids(): 
    response = requests.get("http://localhost:5000/api/formatIds").content
    return response

if __name__ == '__main__':
    app.run() # to run: flask run -h localhost -p 5005
