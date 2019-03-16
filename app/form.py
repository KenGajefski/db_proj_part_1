from flask_wtf import FlaskForm
from wtforms import Form, FormField, StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired])
    password = StringField('Password', validators=[DataRequired])
    submit = SubmitField('Submit')
