from crypt import methods
from functools import wraps
from flask import url_for, flash, redirect, g, render_template
from project.auth.models import User
from project.blog.models import BlogPost, Comment
from flask_sqlalchemy import SQLAlchemy
from project.app import app


db = SQLAlchemy()


def admin_required():
    @wraps(f)
    def decorated_function(*args, **kwargs):
        #Kullanıcı oturumunda role kontrolü
        if not g.User:
            flash('Lütfen giriş yapın', 'danger')
            return redirect(url_for('auth.login')) , 404

        #Kullanıcı bilgilerini veritabanından kontrol et
        user = User.query.filter_by(id=g.User.id).first()

        if not user or user.role != 'admin':
            flash('Yetkiniz yok', 'danger')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function()



from .models import EditCategories
from .forms import EditCategories


@app.route("/admin")
@admin_required
def admin_panel():
    users = User.query.all()
    blogs = BlogPost.query.all()
    comments = Comment.query.all()
    return render_template('admin_home.html', users=users, blogs=blogs, comments=comments)

@app.route("/edit_categories", methods=['GET','POST'])
@admin_required
def edit_categories():

    form = EditCategories()

    if form.validate_on_submit():
        categorie_name = form.categori_name.data
        new_categorie = EditCategories( categorie_name=categorie_name)
        db.session.add(new_categorie)
        db.session.commit()

        flash('Kategori Başarıyla Eklendi', 'success')
        return render_template("edit_categories.html", form=form)

@app.route("/blog-and-comment-management", methods=['GET','POST'])
def management():
    blogs = BlogPost.query.all()
    comments = Comment.query.all()

    return render_template("blog_and_comment_management.html", blogs=blogs, comments=comments)








