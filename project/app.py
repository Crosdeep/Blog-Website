# project/app.py
from flask import render_template
from project import create_app, app
from project.auth.models import User
from project.blog.models import BlogPost,Comment

create_app()

@app.route("/", methods=['POST','GET'])
def home():
    users = User.query.all()  #Kullanıcıları al
    blogs = BlogPost.query.all()  #Blogları al
    return render_template('home.html', users=users, blogs=blogs, comments=comments)


if __name__ == '__main__':
    app.run(debug=True)