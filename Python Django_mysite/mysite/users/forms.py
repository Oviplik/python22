from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(
        attrs={'class': 'Radio'}), choices=(('Men', 'Men'), ('Women', 'Women'),))
    age = forms.IntegerField(label='Age', required=True)
    adres = forms.CharField(label='Adres', required=True)
    news = forms.BooleanField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'age', 'email', 'gender', 'adres','password1', 'password2','news']

