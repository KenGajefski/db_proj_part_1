from flask import Flask, render_template, flash, redirect, Session, request
from app import app
from app.login_form import LoginForm
from app.main_forms import CreateDB, AssignReviewers
from database import DBCreation
import mysql.connector
from mysql.connector import errorcode


app.config['SECRET_KEY'] = 'the-penguin-is-a-most-serene-animal'
# session is used for passing data between routes
session = {}


@app.route('/', methods=['GET', 'POST'])
def index():
    login_form = LoginForm()
    # This is clearly not secure, but is a quick and nasty auth method for the purpose of this project
    if login_form.is_submitted() and login_form.username.data == 'john' and login_form.password.data == 'pass1234':
        session['user'] = login_form.username.data
        session['pass'] = login_form.password.data
        flash('Logging in as {}'.format(login_form.username.data))
        return redirect('main_page')
    return render_template('login.html', form=login_form)


@app.route('/main_page', methods=['GET', 'POST'])
def main_page():
    # For each button that will be on the GUI for the project, a from will have to be created
    # i.e.: loginForm, createDB, addReviewers
    # Using the same <form_name>.is_submitted() function for each and flashing the message will be best
    # Main will always be the rendered template
    cnx = mysql.connector.connect(user='john', password='pass1234')
    cursor = cnx.cursor()
    createDB = CreateDB()
    assignReviewers = AssignReviewers()
    # Need to figure out how to get this to work with session[]
    # database initialization and creation functions contained here

    # This is how you differentiate which button is pressed on the page
    if request.method == 'POST':
        if "create-database" in request.form:
            dbInit = DBCreation()
            dbInit.create_database(cursor, cnx)
            dbInit.create_table(cursor)
            dbInit.init_values(cursor, cnx)
            flash('Database created and initialized')
            return redirect('main_page')
        elif "assign-reviewers" in request.form:
            flash('Assign button under construction')
            return redirect('main_page')

    return render_template('main.html', createForm=createDB, assignReviewForm=assignReviewers)

# This page will have fields in the form for adding a reviewer to a paper
@app.route('/assign_reviewers', methods=['GET', 'POST'])
def assign_reviewers_page():
    assignReviewers = AssignReviewers()
    return render_template('assign_reviewers.html', assignReviewForm=assignReviewers)


if __name__ == '__main__':
    app.run(debug=True)
