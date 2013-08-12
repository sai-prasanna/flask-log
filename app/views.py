from flask import render_template, redirect, request, url_for, flash
from app import app, db, models
from forms import PostForm, CommentForm


@app.route('/')
@app.route('/index')
def index():
    posts = models.Post.query.order_by('timestamp desc').all()
    return render_template("index.html", posts=posts)


@app.route('/post/<id>/', methods=['GET', 'POST'])
@app.route('/post/<id>/<slug>', methods=['GET', 'POST'])
def view_post(id, slug=None):
    post = models.Post.query.get_or_404(id)
    comment_form = CommentForm()
    if post.slug != slug:
        return redirect(url_for('view_post', id=id, slug=post.slug))
    if request.method == 'POST':
        if comment_form.validate_on_submit():
            body = comment_form.body.data
            c = models.Comment(body=body)
            post.comments.append(c)
            db.session.add(post)
            db.session.add(c)
            db.session.commit()
            flash('Comment created')
            return redirect(url_for('view_post', id=id, slug=post.slug))
    return render_template("post.html", post=post, comment_form=comment_form)


@app.route('/new', methods=['GET', 'POST'])
def post_new():
    form = PostForm()
    if request.method == 'POST':
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
