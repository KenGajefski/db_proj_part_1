from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://john:pass1234@localhost/mydatabase'

from app import routes