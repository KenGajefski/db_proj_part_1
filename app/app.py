from flask import Flask, render_template
from app.form import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'the-penguin-is-a-most-serene-animal'


@app.route('/')
def index():
    form = LoginForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
