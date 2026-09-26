import os
from django.contrib.auth import authenticate , logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm


def heder(request):
    context = {}
    return render(request, 'base/heder.html', context)


def foter(request):
    context = {}
    return render(request, 'base/foter.html', context)


def home(request):
    print(request.user.is_authenticated)
    context = {}
    return render(request, 'home_page.html', context)


def contact_us(request):
    context = {}
    return render(request, 'contact_us_page.html', context)


def login(request):
    loginform = LoginForm(request.POST or None)
    if loginform.is_valid():
        username = loginform.cleaned_data.get('username')
        password = loginform.cleaned_data.get('password')
        if password == 'amir' and username == 'amir':
            os.system('cls')

        user = authenticate(request, username=username, password=password)
        print(loginform.errors)
        if user:
            auth_login(request, user)
            return redirect('/')
        else:
            print('error')
    context = {
        'login_form': loginform
    }
    return render(request, 'AUTH/login.html', context)

def log_out(request):
    logout(request)
    return redirect('/login')


def register(request):
    registerform = RegisterForm(request.POST or None)
    if registerform.is_valid():
        username = registerform.cleaned_data.get('username')
        password = registerform.cleaned_data.get('password')
        email = registerform.cleaned_data.get('email')
        new_user = User.objects.create_user(username=username, password=password, email=email)
        print(new_user)
        return redirect('/')
    context = {
        "registerform": registerform
    }
    return render(request, 'AUTH/register.html', context)
