from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, HiddenField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed


class CreateBlog(FlaskForm):
    title = StringField('Gönderi Başlığı', validators=[DataRequired(), Length(max=200)])
    task = StringField('Görev', validators=[DataRequired()])
    description = TextAreaField('Açıklama', validators=[DataRequired()])
    submit = SubmitField('Oluştur')


class PostForm(FlaskForm):
    title = StringField('Başlık')
    content = StringField('İçerik')
    submit = SubmitField('Gönder')



class CommentForm(FlaskForm):
    title = StringField('Yorum', validators=[DataRequired()])
    description = TextAreaField('İçerik', validators=[DataRequired()])
    post_id = HiddenField('Post ID')  # Post ID, gizli alan olarak formda olacak
    user = HiddenField('User ID')  # Kullanıcı ID'si
    submit = SubmitField('Gönder')


from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired



class UpdatePostForm(FlaskForm):
    title = StringField('Başlık', validators=[DataRequired()])
    description = TextAreaField('Açıklama', validators=[DataRequired()])
    picture = FileField('Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Güncelle')


class ContactForm(FlaskForm):
    name = StringField('Ad/Soyad', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    content = TextAreaField('Açıklama', validators=[DataRequired()])
    submit = SubmitField('Gönder')



