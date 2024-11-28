# project/app.py
from flask import Flask
from project.config import Config
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app():
    print("create_app fonksiyonu çalıştı!")
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'postgresql://postgres:pp123@localhost:5432/blog'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from project import auth
    app.register_blueprint(auth)

    from project import blog
    app.register_blueprint(blog)

    from project import admin
    app.register_blueprint(admin)

    print(app.config['SQLALCHEMY_DATABASE_URI'])
    return app



if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
