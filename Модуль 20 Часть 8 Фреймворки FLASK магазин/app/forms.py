from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class RegistrationFormSeller(FlaskForm):
    name = StringField('Имя:', validators=[DataRequired()])
    surname = StringField('Фамилия:', validators=[DataRequired()])
    phone = StringField('Контактный телефон:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired()])
    date_start = StringField('Дата приёма на работу:', validators=[DataRequired()])
    position = StringField('Позиция в фирме:', validators=[DataRequired()])
    submit = SubmitField('Зарегистрировать продавца')

class EditFormSeller(FlaskForm):
    name = StringField('Имя:', validators=[DataRequired()])
    surname = StringField('Фамилия:', validators=[DataRequired()])
    phone = StringField('Контактный телефон:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired()])
    date_start = StringField('Дата приёма на работу:', validators=[DataRequired()])
    position = StringField('Позиция в фирме:', validators=[DataRequired()])
    submit = SubmitField('Сохранить изменения')

class RegistrationFormBuyer(FlaskForm):
    name = StringField('Имя:', validators=[DataRequired()])
    surname = StringField('Фамилия:', validators=[DataRequired()])
    phone = StringField('Контактный телефон:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired()])
    submit = SubmitField('Зарегистрировать покупателя')

class EditFormBuyer(FlaskForm):
    name = StringField('Имя:', validators=[DataRequired()])
    surname = StringField('Фамилия:', validators=[DataRequired()])
    phone = StringField('Контактный телефон:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired()])
    submit = SubmitField('Сохранить изменения')

class RegistrationFormGood(FlaskForm):
    nameGood = StringField('Название товара:', validators=[DataRequired()])
    aboutGood = TextAreaField('Описание товара:', validators=[DataRequired()])
    submit = SubmitField('Зарегистрировать товар')

class EditFormGood(FlaskForm):
    nameGood = StringField('Название товара:', validators=[DataRequired()])
    aboutGood = TextAreaField('Описание товара:', validators=[DataRequired()])
    submit = SubmitField('Сохранить изменения')

class RegistrationFormSales(FlaskForm):
    buyer_id = StringField('ID покупателя:', validators=[DataRequired()])
    seller_id = StringField('ID продавца:', validators=[DataRequired()])
    good_id = StringField('ID товара:', validators=[DataRequired()])
    date_sel = StringField('Дата продажи:', validators=[DataRequired()])
    price_sel = StringField('Цена товара:', validators=[DataRequired()])
    submit = SubmitField('Зарегистрировать продажу')

class EditFormSales(FlaskForm):
    buyer_id = StringField('ID покупателя:', validators=[DataRequired()])
    seller_id = StringField('ID продавца:', validators=[DataRequired()])
    good_id = StringField('ID товара:', validators=[DataRequired()])
    date_sel = StringField('Дата продажи:', validators=[DataRequired()])
    price_sel = StringField('Цена товара:', validators=[DataRequired()])
    submit = SubmitField('Сохранить изменения')



class SearchForm(FlaskForm):
    search = StringField('Поиск:', validators=[DataRequired()])