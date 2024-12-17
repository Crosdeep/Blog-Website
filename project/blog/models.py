from project import db
from flask_bcrypt import Bcrypt
from datetime import datetime
from flask_wtf import FlaskForm
from sqlalchemy import ForeignKey

bcrypt = Bcrypt()


#BlogPost modelinin tanımı
class BlogPost(db.Model):
    __tablename__ = 'blog_posts'  #Tablo adı
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    task = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    view_count = db.Column(db.Integer, default=0)
    favorites_count = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('posts', lazy=True))
    categori = db.Column(db.String(50), ForeignKey('EditCategories.id'), nullable=False)

    #BlogPost'a ait yorumlar (comments)
    comments = db.relationship('Comment', backref='blog_posts', lazy=True)

    def __repr__(self):
        return f'<BlogPost {self.id}>'

class Favorites(db.Model):
    __tablename__ = "favorites"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)


# Comment modelinin tanımı
class Comment(db.Model):
    __tablename__ = 'comments'  # Tablo adı
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('blog_posts.user_id'))
    content = db.Column(db.String(200), nullable=False)
    #description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign key: Comment post_id, BlogPost id ile ilişkilendiriliyo
    post_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id'), nullable=False)

    def __repr__(self):
        return f'<Comment {self.id}>'


class Contact(db.Model):
    __tablename__ = "contact"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Contact :{self.name}"



