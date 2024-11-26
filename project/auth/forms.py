from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from .models import User


class UserRegister(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Şifre', validators=[
        DataRequired(),
        EqualTo('pass_confirm', message='Şifre eşit değil'),
        Length(min=8, message='Şifre en az 8 karakter olmalıdır.')
    ])
    pass_confirm = PasswordField('Şifre eşleştir', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Kayıt Ol')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Bu kullanıcı adı daha önce alınmış.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Bu email daha önce alınmış.")


class UserLogin(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[DataRequired()])
    password = PasswordField('Şifre', validators=[DataRequired()])
    submit = SubmitField('Giriş Yap')


class UserProfileForm(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[DataRequired(), Length(max=150)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Yeni Şifre', validators=[Length(min=6), EqualTo('confirm_password', message='Şifre eşit değil.')])
    confirm_password = PasswordField('Şifreyi Doğrula')



