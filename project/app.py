from flask import Flask, render_template, redirect, url_for, flash
from .models import db, User
from .forms import UserRegister, UserLogin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'verysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pp123@localhost/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = UserLogin()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = UserRegister()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
