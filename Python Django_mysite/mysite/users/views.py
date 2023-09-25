from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import UserData

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user=form.save()
			username = form.cleaned_data.get('username')
			age = form.cleaned_data.get('age')
			gender = form.cleaned_data.get('gender')
			adres = form.cleaned_data.get('adres')
			news = form.cleaned_data.get('news')
			UserData.objects.create(user=user, age=age, gender=gender, adres=adres, news=news)
			messages.success(request, f'{username} успешно зарегестрирован!')
			return redirect('/')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')