from project import db


class EditCategories(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    categori_name = db.Column(db.String(50), nullable=False, unique=True)
    posts = db.relationship('BlogPost', back_populates='categori')

    def __repr__(self):
        return f"Categori :{self.categori_name}"
