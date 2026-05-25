from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

class KitapForm(FlaskForm):
    baslik = StringField('Kitap Başlığı', validators=[DataRequired(), Length(min=1, max=128)])
    yazar = StringField('Yazar', validators=[DataRequired(), Length(min=1, max=128)])
    yayin_yili = IntegerField('Yayın Yılı (İsteğe Bağlı)', validators=[Optional()])
    submit = SubmitField('Kaydet')
