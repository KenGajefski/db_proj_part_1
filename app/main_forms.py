from flask_wtf import FlaskForm
from wtforms import Form, FormField, StringField, SubmitField
from wtforms.validators import DataRequired

class CreateDB():
    submit = SubmitField('Create and Initialize Database')

