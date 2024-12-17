# project/__init__.py
from flask import Flask
from project.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pp123@localhost/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


def create_app():
    app.config.from_object(Config)
    db.init_app(app)

    from project.auth import auth
    from project.blog import blog
    from project.admin import admin

    app.register_blueprint(auth)
    app.register_blueprint(blog)
    app.register_blueprint(admin)

    return app
