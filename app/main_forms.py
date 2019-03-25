from flask_wtf import FlaskForm
from wtforms import Form, FormField, StringField, SubmitField
from wtforms.validators import DataRequired


class CreateDB(FlaskForm):
    submit = SubmitField('Create and Initialize Database')


class AssignReviewers(FlaskForm):
    reviewer1 = StringField('Reviewer 1:')
    reviewer2 = StringField('Reviewer 2:')
    reviewer3 = StringField('Reviewer 3:')
    submit = SubmitField('Assign Reviewers')

