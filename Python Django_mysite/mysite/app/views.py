from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime
import calendar
from .forms import Exc2, Exc4

def index(request):
	data={'Admin':'Логин: Admin, Пароль: test1234'}
	return render(request, 'app/index.html', context=data)

def exc2(request):
	if request.method == 'POST':
		form = Exc2(request.POST)
		if form.is_valid():
			value1 = form.cleaned_data.get('value1')
			value2 = form.cleaned_data.get('value2')
			value3 = form.cleaned_data.get('value3')
			choice = form.cleaned_data.get('choice')
			list123 = [value1, value2, value3]
			if choice == 'min':
				result=min(list123)
			elif choice == 'max':
				result=max(list123)
			else:
				result = sum(list123)/3

			return HttpResponse(f"<h2>Результат: {result}</h2><br><a href='exc2'>Вернуться назад</a>")
	else:
		form = Exc2()
	return render(request, 'app/exc2.html', {'form': form})

def exc4(request):
	if request.method == 'POST':
		form = Exc4(request.POST)
		if form.is_valid():
			year = form.cleaned_data.get('year')
			if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
				data = {'data': f'12/09/{year}'}
			else:
				data = {'data': f'13/09/{year}'}
			return render(request, "app/exc4.html",context=data)
	else:
		form = Exc4()
	return render(request, 'app/exc4.html', {'form': form})
