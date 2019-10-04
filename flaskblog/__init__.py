from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
with open('skey.txt','r') as f:
    app.config['SECRET_KEY'] = f.read()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
