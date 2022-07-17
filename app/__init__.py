"""Initializing Flask Extensions"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
#app.config['SECRET_KEY'] = 'you-will-never-guess-my-life-moves'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models