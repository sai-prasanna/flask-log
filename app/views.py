from flask import render_template, redirect
from app import app
from forms import PostForm


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


@app.route('/new', methods=['GET', 'POST'])
def new():
    form = PostForm()
    if form.validate_on_submit():
        print form
        return redirect('/index')
    return render_template('create-post.html', form=form)
