from django.shortcuts import (
	render,
	redirect
)
from django.contrib.auth import (
	authenticate,
	login,
	logout
)
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import MyUserCreationForm
from .models import MyUser

# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'shop/home.html', context)

def login(request):
	# If user is already logged in then redirect to profil.
	if request.user.is_authenticated:
		return redirect('/u/' + str(request.user.id))
	# If POST then check the form for validity and login user in.
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form_is_valid():
			username = form.cleaned_data['username']
			raw_password = form.cleaned_data['password']
			user = authenticate(request, username=username, password=raw_password)
			if user is not None:
				login(request, user)
				return redirect('/u/' + str(user.id))
	form = AuthenticationForm()
	context = {
		'form_name': 'Login',
		'form': form,
	}
	return render(request, 'shop/login.html', context)

def logout(request):
	# Just logout, this doesn't fail.
	logout(request)
	return redirect('/')

def register(request):
	# If user is already logged in then redirect to profile.
	if request.user.is_authenticated:
		return redirect('/u/' + str(request.user.id))
	if request.method == 'POST':
		form = MyUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data['email']
			raw_password = form.cleaned_data['password1']
			user = authenticate(request, username=email, password=raw_password)
			if user is not None:
				login(request, user)
				return redirect('/u/' + str(user.id))
	form = MyUserCreationForm()
	context = {
		'form_name': 'Register',
		'form': form,
	}
	return render(request, 'shop/register.html', context)

def profile(request, id):
	context = {

	}
	return render(request, 'shop/profile.html', context)
