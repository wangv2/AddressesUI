import os
import requests
from flask import Flask, render_template, json, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    try: 
        return render_template("index.html", data=json.loads(get_format_ids()))
    except Exception as e:
        return render_template("error.html", error = str(e))
    
@app.route('/test')
def test():
    try: 
        response = requests.get("http://localhost:5000/api").content
        return response
    except Exception as e:
        return render_template("error.html", error = str(e))

@app.route('/addForm', methods=['POST'])
def addForm():
    try: 
        country = request.form['country']
        return render_template("addForm.html", data=json.loads(api_get_format_by_id(country)))
    except Exception as e:
        return render_template("error.html", error = str(e))

@app.route('/searchByForm', methods=['POST'])
def searchByForm():
    try: 
        country = request.form['country']
        return render_template("searchByForm.html", data=json.loads(api_get_format_by_id(country)))
    except Exception as e:
        return render_template("error.html", error = str(e))

@app.route('/searchAcrossForm', methods=['POST'])
def searchAcrossForm():
    try: 
        country = 'GENERAL'
        return render_template("searchAcrossForm.html", data=json.loads(api_get_format_by_id(country)))
    except Exception as e:
        return render_template("error.html", error = str(e))

@app.route('/add', methods=['POST'])
def add():
    try: 
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
        response = json.loads(requests.post(url, json=addInput, headers=headers).content.decode("utf-8"))
        return render_template("addResults.html", data=response)
    except Exception as e:
        return render_template("error.html", error = str(e))

@app.route('/search', methods=['POST'])
def search():
    try: 
        searchInput = request.form.to_dict()
        searchInput = remove_empty_filters(searchInput)
        url = "http://localhost:5000/api/search"
        headers = {'Content-type': 'application/json'}
        response = json.loads(requests.post(url, json=searchInput, headers=headers).content.decode("utf-8"))
        return render_template("searchResults.html", data=response)
    except Exception as e:
        return render_template("error.html", error = str(e))
    
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
