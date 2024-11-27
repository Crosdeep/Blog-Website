from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class EditCategories(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    categori_name = db.Column(db.String(50), nullable=False, unique=True)
    posts = db.relationship('BlogPost', backref='blogpost.id')

    def __repr__(self):
        return f"Categori :{self.categori_name}"
