from datetime import datetime

from wtforms import StringField, SelectField,SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class EditCategories(FlaskForm):
    categorie = SelectField('Kategori Oluştur', choices=[(1, 'Teklonoji',) ,(2 ,'Sağlık') ,(3 ,'Yaşam'), (4 ,'Ev'), (5 ,'Donanım')
                                     ,(6 ,'Sosyal Medya')], coerce=int, validators=[DataRequired()])
    submit = SubmitField('Seç')
