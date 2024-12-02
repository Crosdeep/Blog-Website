# project/app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from project.admin import admin
from project.blog import blog
from project.auth import auth

db = SQLAlchemy()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:pp123@localhost/blog"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


app.register_blueprint(auth)
app.register_blueprint(blog)
app.register_blueprint(admin)


if __name__ == '__main__':
    app.run(debug=True)
