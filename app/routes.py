from flask import Flask, render_template, flash, redirect
from app import app
from app.login_form import LoginForm


app.config['SECRET_KEY'] = 'the-penguin-is-a-most-serene-animal'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.is_submitted():
        flash('Logging in as {}'.format(form.username.data))
        return redirect('main_page')
    return render_template('login.html', form=form)


@app.route('/main_page')
def main_page():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
