from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email
from app.models import Book
    
class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=140, message='Title text is too long!')])
    author = StringField('Author', validators=[DataRequired(), Length(max=64, message='Author text is too long!')])
    date_purchased = DateField('Date Purchased', format='%Y-%m-%d')
    notes = TextAreaField('Notes', validators=[Length(max=200, message='Notes text is too long!')])
    submit = SubmitField('Submit')

class ShareBookListForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Share')