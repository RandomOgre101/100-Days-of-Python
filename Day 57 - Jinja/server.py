from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__, template_folder='../Day 57 - Jinja/templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<name>')
def name_page(name):
    r1 = requests.get(f'https://api.genderize.io?name={name}')
    r2 = requests.get(f'https://api.agify.io?name={name}')
    person_name = r1.json()["name"]
    person_age = r2.json()["age"]
    person_gender = r1.json()["gender"]
    return render_template('guess.html', name=person_name, age=person_age, gender=person_gender)


@app.route('/blog/<int:num>')
def get_blog(num):
    r = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    all_posts = r.json()
    return render_template('blog.html', posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)