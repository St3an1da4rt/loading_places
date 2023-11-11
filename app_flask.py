from flask import Flask, render_template
from jinja2 import Environment, FileSystemLoader
import json
import os

filename_json2 = ''
direct = os.listdir("json")
for i in direct:
    if i.split('.')[1] == 'json':
        filename_json2 = f"json/{i}"

class_school = {
    'hy': 'hydrogen-place',
    'ca': 'carbon-place',
    'su': 'surfur-place'
}

with open(filename_json2, 'r') as f:
    join = json.load(f)

join2 = {j: i for i, j in join.items()}


environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("index.html")

app = Flask(__name__)

@app.route('/main')
@app.route('/')
def index():
    return render_template("index.html", join2=join2)

@app.route('/about')
def about():
    return render_template("about.html")



if __name__ == '__main__':
    app.run(debug=True)