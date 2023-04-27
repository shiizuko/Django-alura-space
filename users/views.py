from django.shortcuts import redirect, render
from users.forms import LoginForms, RegisterForm
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    form = LoginForms()
    
    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            name = form['name_login'].value()
            password = form['password_login'].value()
            
        user = auth.authenticate(
            request,
            username = name,
            password = password,
        )
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return redirect('login')
            
        
        
    return render(request, 'users/login.html', {'form': form})

def register(request):
    # verificando a validação do formulário
    form  = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            if form["password_1"].value() != form["password_2"].value():#verificação das senhas (se são iguais) 
                return redirect('register')
            #inserimos as infos recebidas no formulário nas variaveis (name, emai, password), para tornar esses dados mais maleaveis na logica
            name=form["name_register"].value()
            email=form["email_register"].value()
            password=form["password_1"].value()
            
            #verificando se a informação do username corresponde a algo já existente no banco de dados
            if User.objects.filter(username=name).exists():
                return redirect('register')

            #Criando usuário com as informações inseridas no formulário
            user = User.objects.create_user(
                username = name,
                email    = email,
                password = password
            )
            user.save()
            return redirect('login')
        
    return render(request, 'users/register.html', {'form': form})
    