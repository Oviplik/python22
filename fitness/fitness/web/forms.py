from django import forms
from .models import *

class FeedbackForm(forms.Form):
    name = forms.CharField( label = 'Введите имя:', widget = forms.TextInput(
                attrs = {'class':'form-control','placeholder':'Ваше имя'}))
    phone = forms.CharField( label = 'Введите номер телефона:', widget = forms.TextInput(
                attrs = {'class':'form-control','placeholder':'Ваш номер телефона'}))