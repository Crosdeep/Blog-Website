from flask_bcrypt import Bcrypt
from datetime import datetime
from sqlalchemy import ForeignKey
from project import db

bcrypt = Bcrypt()


# BlogPost modelinin tanımı
class BlogPost(db.Model):
    __tablename__ = 'blog_posts'  # Tablo adı
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    task = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    view_count = db.Column(db.Integer, default=0)
    favorites_count = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('posts', lazy=True))
    # ForeignKey kullanarak ilişkili kategoriyi belirtiriz
    categori_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    # 'back_populates' ile EditCategories ile ilişkiyi belirtiriz
    categori = db.relationship('EditCategories', back_populates='posts')


    # BlogPost'a ait yorumlar (comments)
    comments = db.relationship('Comment', backref='blog_post', lazy=True)

    def __repr__(self):
        return f'<BlogPost {self.id}>'


# Favorites modelinin tanımı
class Favorites(db.Model):
    __tablename__ = "favorites"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # 'users' tablosuna referans
    post_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id'), nullable=False)  # 'blog_posts' tablosuna referans

    def __repr__(self):
        return f"<Favorite {self.id}>"


# Comment modelinin tanımı
class Comment(db.Model):
    __tablename__ = 'comments'  # Tablo adı
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    blog_post_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id'), nullable=False)  # BlogPost'a referans


class Contact(db.Model):
    __tablename__ = "contact"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Contact :{self.name}"



