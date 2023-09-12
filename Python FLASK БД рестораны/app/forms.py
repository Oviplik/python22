from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    username = StringField('Название ресторана:', validators=[DataRequired()])
    spec = StringField('Национальная кухня:', validators=[DataRequired()])
    adres = StringField('Где находиться:', validators=[DataRequired()])
    web = StringField('Веб-сайт:', validators=[DataRequired()])
    phone = StringField('Номер контактного телефона:', validators=[DataRequired()])
    submit = SubmitField('Добавить')

class EditForm(FlaskForm):
    username = StringField('Название ресторана:', validators=[DataRequired()])
    spec = StringField('Национальная кухня:', validators=[DataRequired()])
    adres = StringField('Где находиться:', validators=[DataRequired()])
    web = StringField('Веб-сайт:', validators=[DataRequired()])
    phone = StringField('Номер контактного телефона:', validators=[DataRequired()])
    submit = SubmitField('Сохранить изменения')

class SearchForm(FlaskForm):
    search = StringField('Поиск:', validators=[DataRequired()])