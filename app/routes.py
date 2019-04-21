from flask import Flask, render_template, flash, redirect, session, request
from app import app
from app.login_form import LoginForm
from app.main_forms import AssignReviewers, PaperChanges, PCMemberChanges, ReviewChanges
from database import DBCreation
import mysql.connector
from mysql.connector import errorcode


# This is necessary for the app
app.config['SECRET_KEY'] = 'the-penguin-is-a-most-serene-animal'


@app.route('/', methods=['GET', 'POST'])
def index():
    login_form = LoginForm()
    # This is clearly not secure, but is a quick and nasty auth method for the purpose of this project
    # All this does is check that the input for the username and password are equal to the credentials for user 'john'
    if login_form.is_submitted() and login_form.username.data == 'john' and login_form.password.data == 'pass1234':
        flash('Logging in as {}'.format(login_form.username.data))
        return redirect('main_page')
    return render_template('login.html', form=login_form)


@app.route('/main_page', methods=['GET', 'POST'])
def main_page():
    # For each button that will be on the GUI for the project, a form will have to be created
    # i.e.: loginForm, createDB, addReviewers
    # Using the same <form_name>.is_submitted() function for each and flashing the message will be best
    # Main will always be the rendered template
    cnx = mysql.connector.connect(user='john', password='pass1234')
    cursor = cnx.cursor()
    assignReviewers = AssignReviewers()
    paperChanges = PaperChanges()
    pcMemberChanges = PCMemberChanges()
    reviewChanges = ReviewChanges()
    # Need to figure out how to get this to work with session[]
    # database initialization and creation functions contained here

    # This is how you differentiate which button is pressed on the page. It's clearly ugly, but it'll do, pig.
    if request.method == 'POST':
        if "create-database" in request.form:
            dbInit = DBCreation()
            # Drops database so it doesn't crash if already exists
            dbInit.drop_database(cursor)
            dbInit.create_database(cursor, cnx)
            dbInit.create_table(cursor)
            dbInit.init_values(cursor, cnx)
            flash('Database created and initialized')
            return redirect('main_page')
        # Assign Reviewers
        elif "assign-reviewers" in request.form:
            flash('Assign button under construction')
            return redirect('main_page')
        # Paper change block
        elif "paper-changes-add" in request.form:
            flash('Paper additions under construction')
            return redirect('main_page')
        elif "paper-changes-del" in request.form:
            flash('Paper deletions under construction')
            return redirect('main_page')
        elif "paper-changes-upd" in request.form:
            flash('Paper updates under construction')
            return redirect('main_page')
        # END Paper change block
        # PC Member change block
        elif "pcmem-changes-add" in request.form:
            flash('PC Member additions under construction')
            # TODO: Capture the rest of field data for other queries like this
            # session['name'] = pcMemberChanges.pcName.data
            # session['email'] = pcMemberChanges.pcEmail.data
            return redirect('main_page')
        elif "pcmem-changes-del" in request.form:
            flash('PC Member deletions under construction')
            return redirect('main_page')
        elif "pcmem-changes-upd" in request.form:
            flash('PC Member updates under construction')
            return redirect('main_page')
        # END PC Member change block
        # Review change block
        elif "review-changes-add" in request.form:
            flash('Review additions under construction')
            return redirect('main_page')
        elif "review-changes-add" in request.form:
            flash('Review deletions under construction')
            return redirect('main_page')
        elif "review-changes-add" in request.form:
            flash('Review updates under construction')
            return redirect('main_page')
        # End Review change block
        # Project problem block
        elif "prob-four" in request.form:

            flash('Problem 4 under construction')
            return redirect('main_page')
        elif "prob-five" in request.form:
            flash('Problem 5 under construction')
            return redirect('main_page')
        elif "prob-six" in request.form:
            flash('Problem 6 under construction')
            return redirect('main_page')
        elif "prob-seven" in request.form:
            flash('Problem 7 under construction')
            return redirect('main_page')
        elif "prob-eight" in request.form:
            flash('Problem 8 under construction')
            return redirect('main_page')
        elif "prob-nine" in request.form:
            flash('Problem 9 under construction')
            return redirect('main_page')
        elif "prob-ten" in request.form:
            flash('Problem 10 under construction')
            return redirect('main_page')

    return render_template('main.html', assignReviewForm=assignReviewers,
                           paperChangesForm=paperChanges, pcMemberChangesForm=pcMemberChanges,
                           reviewChangesForm=reviewChanges)


if __name__ == '__main__':
    app.run(debug=True)
