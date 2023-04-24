from django.shortcuts import redirect, render
from users.forms import LoginForms, RegisterForm

def login(request):
    form = LoginForms()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    form  = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form["password_1"].value() != form["password_2"].value():
            return redirect('register')
        
    return render(request, 'users/register.html', {'form': form})
    