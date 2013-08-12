from flask import render_template, redirect, request, url_for, flash
from app import app, db, models
from forms import PostForm


@app.route('/')
@app.route('/index')
def index():
    posts = models.Post.query.order_by('timestamp desc').all()
    return render_template("index.html", posts=posts)


@app.route('/post/<id>')
@app.route('/post/<id>/<slug>')
def view_post(id, slug=None):
    post = models.Post.query.get_or_404(id)
    if post.slug != slug:
        return redirect(url_for('post', id=id, slug=post.slug))
    return render_template("post.html", post=post)


@app.route('/post/new', methods=['GET', 'POST'])
def post_new():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.post.data
        p = models.Post(title=title, body=body)
        db.session.add(p)
        db.session.commit()
        flash('Post created')
        return redirect(url_for('index'))
    return render_template('create-post.html', form=form)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
