from flask import render_template, redirect, request
from app import app, db, models
from forms import PostForm
import datetime
from slugify import slugify


@app.route('/')
@app.route('/index')
def index():
    posts = models.Post.query.order_by('timestamp desc').all()
    return render_template("index.html", posts=posts)


@app.route('/post/<slug>')
def view_post():
    post = models.Post.query.filter_by(slug=slug).first()
    if post:
        return render_template("post.html", post=post)
    else:
        page_not_found()


@app.route('/post/new', methods=['GET', 'POST'])
def post_new():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.post.data
        timestamp = datetime.datetime.utcnow()
        slug = slugify(title)
        p = models.Post(title=title, body=body, timestamp=timestamp, slug=slug)
        db.session.add(p)
        db.session.commit()
        return redirect('/index')
    return render_template('create-post.html', form=form)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
