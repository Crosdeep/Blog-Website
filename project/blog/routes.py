from flask import Flask, render_template, redirect, url_for, flash, request, Blueprint
from flask_migrate import Migrate
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

app = Flask(__name__)
db.init_app(app)
migrate = Migrate(app, db)

from project.auth.models import User
from project.auth.forms import UserRegister, UserLogin, UserProfileForm
from project.blog.forms import CreateBlog, ContactForm, CommentForm, UpdatePostForm
from project.blog.models import BlogPost,Comment,Contact
from flask_login import LoginManager, login_required, current_user


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  #Giriş yapmamış kullanıcıları yönlendirecek giriş sayfası


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/", methods=['POST','GET'])
def home():
    users = User.query.all()  # Kullanıcıları al
    blogs = BlogPost.query.all()  # Blogları al
    comments = Comment.query.all()  # Yorumları al
    return render_template('home.html', users=users, blogs=blogs, comments=comments)


@app.route("/create-blog", methods=['GET', 'POST'])
@login_required #Sadece giriş yapan kullanıcılar girebilir.
def create_blog():
    form = CreateBlog()
    if form.validate_on_submit():
        if current_user.is_authenticated:  #Kullanıcı giriş yapmış mı
            new_post = BlogPost(
                title=form.title.data,
                task=form.task.data,
                description=form.description.data,
                user_id=current_user.id  #Kullanıcıyı ilişkilendir
            )
            db.session.add(new_post)
            db.session.commit()
            flash('Blog Kaydedildi :)', 'success')
            return redirect(url_for('posts'))
        else:
            flash('Giriş yapmanız gerekiyor.', 'danger')
            return redirect(url_for('login'))  # Giriş sayfasına yönlendir
    return render_template('create_blog.html', form=form)


@app.route('/create-comment', methods=['POST','GET'])
@login_required
def create_comment():
    form = CommentForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_comment = Comment(
                content=form.content.data,
                description=form.description.data,
                post_id=request.args.get('post_id'),
                user_id=current_user.id
            )
            db.session.add(new_comment)
            db.session.commit()
            flash('Yorumunuz başarıyla eklendi!', 'success')
            return redirect(url_for('post_detail', post_id=request.args.get('post_id')))

        #Formu görüntülemek için get isteği
    return render_template('create_comment.html', form=form)


@app.route('/posts')
def posts():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(
            content=form.content.data,
            description=form.description.data,
            post_id=form.post_id.data
        )
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('posts'))

    all_posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return render_template('posts.html', posts=all_posts, form=form)

@app.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post başarıyla silindi.', 'success')
    return redirect(url_for('posts'))

@app.route('/update_post/<int:post_id>', methods=['GET', 'POST'])
def update_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    form = UpdatePostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.description = form.description.data
        db.session.commit()
        flash('Post başarıyla güncellendi.', 'success')
        return redirect(url_for('posts'))
    elif request.method == 'GET':
        form.title.data = post.title
        form.description.data = post.description
    return render_template('update_post.html', form=form)



@app.route("/forum", methods=['GET', 'POST'])
def forum():
    form = CommentForm()

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        comment = Comment(title=title, description=description)
        db.session.add(comment)
        db.session.commit()

        flash('Yorum başarıyla eklendi!', 'success')
        return redirect(url_for('forum'))

    forums = Comment.query.all()  #Tüm yorumları çek
    return render_template('forum.html', forums=forums, form=form)

@app.route("/forum/<int:forum_id>")
def view_forum(forum_id):
    #Forum ID'sine göre forumu bul
    forum = Comment.query.get_or_404(forum_id)
    return render_template('view_forum.html', forum=forum)


@app.route("/contact", methods=['GET','POST'])
@login_required
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')


        return redirect(url_for("contact"))
    return render_template("contact.html", form=form)

