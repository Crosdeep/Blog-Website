from functools import wraps
from flask import url_for, flash, redirect, g, render_template, session
from project.auth.models import User
from project.blog.models import BlogPost, Comment
from project import db, app

from . import admin

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('is_admin'):  # Admin kontrolü
            return redirect(url_for('auth.login'))  # Admin değilse giriş sayfasına yönlendir
        return f(*args, **kwargs)  # Admin ise fonksiyonu çalıştır
    return decorated_function


from .models import EditCategories
from .forms import EditCategories


@app.route("/admin")
@admin_required
def admin_panel():
    users = User.query.all()
    blogs = BlogPost.query.all()
    comments = Comment.query.all()
    return render_template('admin_home.html', users=users, blogs=blogs, comments=comments)


@app.route("/edit_categories", methods=['GET', 'POST'])
@admin_required
def edit_categories():
    form = EditCategories()

    if form.validate_on_submit():
        categorie_name = form.categori_name.data
        new_categorie = EditCategories(categorie_name=categorie_name)
        db.session.add(new_categorie)
        db.session.commit()

        flash('Kategori Başarıyla Eklendi', 'success')
        return render_template("edit_categories.html", form=form)


@app.route("/blog-and-comment-management", methods=['GET', 'POST'])
def management():
    blogs = BlogPost.query.all()
    comments = Comment.query.all()
    return render_template("blog_and_comment_management.html", blogs=blogs, comments=comments)
