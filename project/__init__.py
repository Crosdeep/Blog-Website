# project/__init__.py
from flask import Flask
from project.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy() #buraya app yazınca sqlalchmey yapılandırılmadı hatası veriyo, koymayınca db birden çok yerde kullanıldı diyo. Ve hatayı modelleri inite
# import edip app yazdığımda hata çözdüldü.
migrate = Migrate(app, db)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pp123@localhost:5432/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'SS1s2dLFrh4M'

from .auth.models import User,Role
from .blog.models import BlogPost, Comment, Contact
from .admin.models import EditCategories


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
