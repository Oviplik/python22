from django import forms
from .models import *

class FeedbackForm(forms.Form):
    name = forms.CharField( label = 'Введите имя:', widget = forms.TextInput(
                attrs = {'placeholder':'Ваше имя'}))
    phone = forms.CharField( label = 'Введите номер телефона:', widget = forms.TextInput(
                attrs = {'placeholder':'Ваш номер телефона'}))