#project/__init__.py
import os.path

from flask import Flask
from project.auth import auth
from project.blog import blog
from project.admin import admin
from project.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'very_secret_key'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://'+os.path.join(basedir, 'data.postgresql')
app.config['DATABASE_TRACT_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


def create_app():

    app.config.from_object(Config)
    db.init_app(app)

    from project.auth import auth
    app.register_blueprint(auth)

    from project.blog import blog
    app.register_blueprint(blog)

    from project.admin import admin
    app.register_blueprint(admin)

    return app

