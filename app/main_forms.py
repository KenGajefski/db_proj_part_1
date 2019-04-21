from flask_wtf import FlaskForm
from wtforms import Form, FormField, StringField, SubmitField, DateField, TextAreaField, IntegerField
from wtforms.validators import DataRequired


class CreateDB(FlaskForm):
    submit = SubmitField('Create and Initialize Database')


class AssignReviewers(FlaskForm):
    reviewer1 = StringField('Reviewer 1:', validators=[DataRequired()])
    reviewer2 = StringField('Reviewer 2:')
    reviewer3 = StringField('Reviewer 3:')
    submit = SubmitField('Assign Reviewers')


class PaperChanges(FlaskForm):
    # paperId needs to be handled in front end since auto_increment doesn't work
    abstractPaper = StringField('Abstract:', validators=[DataRequired()])
    titlePaper = StringField('Title:', validators=[DataRequired()])
    pdfPaper = StringField('PDF Link:', validators=[DataRequired()])
    create = SubmitField('Create Paper')
    delete = SubmitField('Delete Paper')
    update = SubmitField('Update Paper')


class PCMemberChanges(FlaskForm):
    # memberid needs to be handled in front end since auto_increment doesn't work
    pcName = StringField('Name:', validators=[DataRequired()])
    pcEmail = StringField('Email:', validators=[DataRequired()])
    create = SubmitField('Create PC Member')
    delete = SubmitField('Delete PC Member')
    update = SubmitField('Update PC Member')


class ReviewChanges(FlaskForm):
    revDate = DateField('Review Date:', validators=[DataRequired()])
    revRecc = StringField('Recommendation (Y/N):', validators=[DataRequired()])
    revComment = TextAreaField('Comments:', validators=[DataRequired()])
    revPaperid = IntegerField('Paper ID:', validators=[DataRequired()])
    revEmail = StringField('PC Member Email:', validators=[DataRequired()])
    create = SubmitField('Create Review')
    delete = SubmitField('Delete Review')
    update = SubmitField('Update Review')
