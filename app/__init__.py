from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

STATIC_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
TEMPLATE_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))

app = Flask(__name__, static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from app.views import *
