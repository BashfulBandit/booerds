from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserRegistrationForm
from .models import User

# Create your views here.
def index(request):
    return redirect('/u/login/')

def user_login(request):
    # If user is already logged in then redirect to profile
    if request.user.is_authenticated:
        return redirect('/u/' + str(request.user.id))
    # If POST then check the form for validity and login user in.
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('/u/' + str(user.id))
    # Else(GET) construct login form and serve the login.html page.
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)

def user_logout(request):
    # Just logout, this doesn't fail.
    logout(request)
    return redirect('/')


def user_register(request):
    # If user is already logged in then redirect to profile.
    if request.user.is_authenticated:
        return redirect('/u/' + str(request.user.id))
    # If POST then check the form for validity and login user in.
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['email']
            raw_password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('/u/' + str(user.id))
    # Else(GET) construct register form and serve the register.html page with form.
    form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)

def user_profile(request, id):
    # If user is logged in then render their profile page.
    if request.user.is_authenticated:
        user = User.objects.get(pk=id)
        context = {
            'user': user,
        }
        return render(request, 'users/profile.html', context)
    # Else redirect them to login page.
    return redirect('/u/login/')
