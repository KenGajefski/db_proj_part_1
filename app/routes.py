from flask import Flask, render_template, flash, redirect, Session
from app import app
from app.login_form import LoginForm
import mysql.connector
from mysql.connector import errorcode


app.config['SECRET_KEY'] = 'the-penguin-is-a-most-serene-animal'
# session is used for passing data between routes
session = {}


@app.route('/', methods=['GET', 'POST'])
def index():
    login_form = LoginForm()
    if login_form.is_submitted():
        session['user'] = login_form.username
        session['pass'] = login_form.password
        flash('Logging in as {}'.format(login_form.username.data))
        return redirect('main_page', login_form)
    return render_template('login.html', form=login_form)


@app.route('/main_page')
def main_page(form):
    cnx = mysql.connector.connect(user={{session['user']}}, password={{session['pass']}})
    cursor = cnx.cursor()
    # For each button that will be on the GUI for the project, a from will have to be created
    # i.e.: loginForm, createDB, addReviewers
    # Using the same xxx.is_submitted() function for each and flashing the message will be best
    # Main will always be the rendered template
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
