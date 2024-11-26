# project/app.py
from flask import Flask
from project.config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    print("create_app fonksiyonu çalıştı!")
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from project import auth
    app.register_blueprint(auth)

    from project import blog
    app.register_blueprint(blog)

    print(app.config['SQLALCHEMY_DATABASE_URI'])
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
