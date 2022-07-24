from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .forms import UserRegisterForm
# Create your views here.


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect("todo-home")

	else:
		form = UserRegisterForm()

	context = {
			"form": form,
	}

	return render(request, "accounts/register.html", context)


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('todo-home')
		else:
			messages.warning(request, 'invalid credentials')
			return redirect('login')

	form = AuthenticationForm()
	context = {
			'form': form
	}
	return render(request, 'accounts/login.html', context)	



def user_logout(request):
	logout(request)
	return redirect('todo-home')