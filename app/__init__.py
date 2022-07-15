"""Initializing Flask Application"""

from flask import Flask
#from app.config import Config


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
#app.config.from_object(Config)

from app import routes