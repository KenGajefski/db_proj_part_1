from flask_wtf import FlaskForm
from wtforms import Form, FormField, StringField, SubmitField


class CreateDB(FlaskForm):
    submit = SubmitField('Create and Initialize Database')

class AssignReviewers(FlaskForm):
    submit = SubmitField('Assign Reviewers')

