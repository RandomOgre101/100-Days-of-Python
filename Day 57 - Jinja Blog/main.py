from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../Day 57 - Jinja Blog/templates')

@app.route('/')
def home():
    r = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    all_posts = r.json()
    return render_template("index.html", posts=all_posts)

@app.route('/blog/<int:num>')
def get_blog(num):
    r = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    all_posts = r.json()
    req_post = None
    for post in all_posts:
        if post['id'] == num:
            req_post = post
    return render_template("post.html", post=req_post)

if __name__ == "__main__":
    app.run(debug=True)
