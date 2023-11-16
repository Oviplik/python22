from django import forms
from .models import *
from datetime import datetime

class ClientUpdateForm(forms.ModelForm):
    date_start_contract = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}),
                                           initial=date.today().strftime("%Y-%m-%d"))
    type_membership = forms.CharField(required=False, widget=forms.TextInput(attrs={'disabled': True,'placeholder':'Безлимитный'}))
    birthdate = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'+79998887766'}))
    class Meta:
        model = Client
        fields = ['lastname', 'firstname', 'patronymic', 'phone', 'email', 'num_contract', 'num_membership',
                  'date_start_contract', 'date_end_contract',
                  'type_membership', 'time_period', 'status_membership', 'birthdate', 'gender', 'passport', 'photo']

class ClientCreateForm(forms.ModelForm):
    date_start_contract = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}),
                                           initial=date.today().strftime("%Y-%m-%d"))
    type_membership = forms.CharField(required=False, widget=forms.TextInput(attrs={'disabled': True,'placeholder':'Безлимитный'}))
    birthdate = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'+79998887766'}))

    class Meta:
        model = Client
        fields = ['lastname', 'firstname', 'patronymic', 'phone', 'email', 'num_contract', 'num_membership',
                  'date_start_contract', 'date_end_contract',
                  'time_period', 'status_membership', 'birthdate', 'gender', 'passport', 'photo']

class journalVisitCreateForm(forms.ModelForm):
    date_start_visit = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),initial=datetime.now)
    date_end_visit = forms.DateTimeField(required=False, widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}))


    class Meta:
        model = journalVisit
        fields = ['num_membership', 'date_start_visit', 'date_end_visit', 'gender', 'locker_number']

class TrainCreateForm(forms.ModelForm):
    dateTime = forms.DateTimeField(required=False, widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Train
        fields = ['trener', 'membership_or_fio', 'type_trains', 'dateTime', 'visited']