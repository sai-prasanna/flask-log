from flask import render_template, redirect, request
from app import app, db, models
from forms import PostForm
import datetime


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


@app.route('/post/new', methods=['GET', 'POST'])
def post_new():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.post.data
        timestamp = datetime.datetime.utcnow()
        p = models.Post(title=title, body=body, timestamp=timestamp)
        db.session.add(p)
        db.session.commit()
        return redirect('/index')
    return render_template('create-post.html', form=form)
