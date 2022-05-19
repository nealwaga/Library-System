# External modules
import os
from app.views import views, books, contacts, checklist


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
ENV ='dev'

if ENV == 'dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
    app.config['SECRET_KEY'] = ''
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQL_DATABASE_URL']
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY'] 

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
