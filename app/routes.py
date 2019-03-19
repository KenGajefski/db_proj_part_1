from flask import Flask, render_template, flash, redirect
from app import app
from app.login_form import LoginForm


app.config['SECRET_KEY'] = 'the-penguin-is-a-most-serene-animal'


@app.route('/', methods=['GET', 'POST'])
def index():
    login_form = LoginForm()
    if login_form.is_submitted():
        flash('Logging in as {}'.format(login_form.username.data))
        return redirect('main_page')
    return render_template('login.html', form=login_form)


@app.route('/main_page')
def main_page():
    # For each button that will be on the GUI for the project, a from will have to be created
    # i.e.: loginForm, createDB, addReviewers
    # Using the same xxx.is_submitted() function for each and flashing the message will be best
    # Main will always be the rendered template
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
