from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    posts = [
        {'title': 'Hello',
            'permalink': 'google.com',
            'date': '12-5-13',
            'body': 'Testing post',

             },
        {'title': 'Hsdfsdfello',
            'permalink': 'google.com',
            'date': '12-5-13',
            'body': 'Testing post',

             }]  # fake post
    return render_template("index.html", posts=posts)


@app.route('/post/<slug>')
def post():
    pass


@app.route('/create/')
def create():
    pass
