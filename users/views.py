from django.shortcuts import render
from users.forms import LoginForms, RegisterForm

def login(request):
    form = LoginForms()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    form  = RegisterForm()
    return render(request, 'users/register.html', {'form': form})
    