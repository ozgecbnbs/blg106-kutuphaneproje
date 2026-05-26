from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional

class KitapForm(FlaskForm):
    baslik = StringField('Kitap Başlığı', validators=[DataRequired(), Length(min=1, max=128)])
    yazar = StringField('Yazar', validators=[DataRequired(), Length(min=1, max=128)])
    yayin_yili = IntegerField('Yayın Yılı (İsteğe Bağlı)', validators=[Optional()])
    submit = SubmitField('Kaydet')

class IncelemeForm(FlaskForm):
    puan = SelectField('Puan (1-5)', choices=[(str(i), str(i)) for i in range(1, 6)], validators=[DataRequired()])
    icerik = TextAreaField('İnceleme (Yorum)', validators=[DataRequired(), Length(min=5, max=1000)])
    submit = SubmitField('İncelemeyi Kaydet')
