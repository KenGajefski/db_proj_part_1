from flask import Flask, render_template, flash, redirect, Session, request
from app import app
from app.login_form import LoginForm
from app.main_forms import CreateDB, AssignReviewers, EditPaper, ViewTable
from database import DBCreation, Results
from search import SearchFunc
import mysql.connector
from mysql.connector import errorcode


# This is necessary for the app
app.config['SECRET_KEY'] = 'the-penguin-is-a-most-serene-animal'
# session is used for passing data between routes
session = {}


@app.route('/', methods=['GET', 'POST'])
def index():
    login_form = LoginForm()
    # This is clearly not secure, but is a quick and nasty auth method for the purpose of this project
    # All this does is check that the input for the username and password are equal to the credentials for user 'john'
    if login_form.is_submitted() and login_form.username.data == 'john' and login_form.password.data == 'pass1234':
        session['user'] = login_form.username.data
        session['pass'] = login_form.password.data
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
    createDB = CreateDB()
    assignReviewers = AssignReviewers()
    # Added edit paper button -Nick
    editPaper = EditPaper()
    printTable = ViewTable()
    dbSearch = SearchFunc()
    # Need to figure out how to get this to work with session[]
    # database initialization and creation functions contained here

    # This is how you differentiate which button is pressed on the page
    if request.method == 'POST':
        if "create-database" in request.form:
            dbInit = DBCreation
            dbInit.drop_database(cursor)
            dbInit.create_database(cursor, cnx)
            dbInit.create_table(cursor)
            dbInit.init_values(cursor, cnx)
            flash('Database created and initialized')
            return redirect('main_page')
        elif "assign-reviewers" in request.form:
            flash('Assign button under construction')
            return redirect('main_page')
        elif "edit-paper" in request.form:
            dbEdit = DBCreation
            dbEdit.edit_Paper(cursor, cnx)
            flash('Paper edited')
            return redirect('main_page')
        elif "search-paper" in request.form:
            dbSearch = SearchFunc
            dbSearch.searchFotouhi(cursor, cnx)
            return redirect('main_page')
        elif "print-table" in request.form:
            dbPrint = Results
            dbPrint.print()
            return redirect('main_page')

    return render_template('main.html', createForm=createDB, assignReviewForm=assignReviewers, editPaperForm=editPaper,
                           viewDB=printTable, searchForm=dbSearch)

if __name__ == '__main__':
    app.run(debug=True)
