



from django import forms



class Exc2(forms.Form):
    value1 = forms.IntegerField(label='Значение 1')
    value2 = forms.IntegerField(label='Значение 2')
    value3 = forms.IntegerField(label='Значение 3')
    choice = forms.ChoiceField(required=True, widget=forms.RadioSelect(
        attrs={'class': 'Radio'}), choices=(('min', 'Minimum'), ('max', 'Maximum'), ('avg', 'Average'),))

class Exc4(forms.Form):
    year = forms.IntegerField(label='Год')