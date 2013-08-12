from flask.ext.wtf import Form, TextField, TextAreaField 
from flask.ext.wtf import Required

class PostForm(Form):
    title = TextField('title', validators=[Required()])
    post  = TextAreaField('post', validators=[Required()])
