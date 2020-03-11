from flask import Flask
from pet.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
app.jinja_env.auto_reload = True 
db = SQLAlchemy(app)

from pet import routes, models