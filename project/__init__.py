
from flask import Flask
from project.auth import auth
from project.blog import blog
from project.config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from project.auth import auth
    app.register_blueprint(auth)

    from project.blog import blog
    app.register_blueprint(blog)

    return app

