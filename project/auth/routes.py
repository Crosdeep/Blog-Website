from flask import render_template, redirect, url_for, flash
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from project import db, app


bcrypt = Bcrypt
migrate = Migrate(app, db)

from project.auth.models import User
from project.auth.forms import UserRegister, UserLogin, UserProfileForm
from project.blog.models import BlogPost, Comment
from flask_login import LoginManager

from . import auth

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  #Giriş yapmamış kullanıcıları yönlendirecek giriş sayfası

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth.route("/", methods=['POST','GET'])
def home():
    users = User.query.all()  # Kullanıcıları al
    blogs = BlogPost.query.all()  # Blogları al
    comments = Comment.query.all()  # Yorumları al
    return render_template('home.html', users=users, blogs=blogs, comments=comments)

from flask_login import LoginManager, login_required, current_user, login_user, logout_user

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = UserLogin()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()  #Kullanıcıyı veritabanında ara
        if user and user.check_password(form.password.data):  #Şifre doğrulaması
            login_user(user)
            flash('Giriş başarılı!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Kullanıcı adı veya şifre yanlış.', 'danger')

    return render_template('login.html', form=form)

@auth.route("/profile")
@login_required
def profile():
    form = UserProfileForm()
    if form.validate_on_submit():
        # Form verilerini işleme
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Profil güncellendi!', 'success')
        return redirect(url_for('profile'))
    return render_template('profile.html', form=form, user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()  #Kullanıcıyı çıkış yaptırıyoruz
    flash('Çıkış Yapıldı!', 'success')
    return redirect(url_for('home'))


@auth.route("/register", methods=['GET', 'POST'])
def register():
    form = UserRegister()
    if form.validate_on_submit():
        print(f"Username: {form.username.data}, Email: {form.email.data}, Password: {form.password.data}")
        new_user = User(
            username=form.username.data,
            email=form.email.data
        )

        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Kayıt başarılı, giriş yapabilirsiniz.', 'success')
        return redirect(url_for('login'))
    else:
        print("Form doğrulanamadı:", form.errors)
    return render_template('register.html', form=form)


@auth.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = UserProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        if form.password.data:
            current_user.set_password(form.password.data)
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))

    form.username.data = current_user.username
    form.email.data = current_user.email
    return render_template('edit_profile.html', form=form)


