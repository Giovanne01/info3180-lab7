# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, FileField
from wtforms.validators import InputRequired

class UploadForm(FlaskForm):
    description = StringField('Description', validators=[InputRequired()])
    photo= FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'])])