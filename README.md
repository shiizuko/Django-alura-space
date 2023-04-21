# Django - Criando aplicações em python 
![Capa do projeto, com um astronauta no espaço com o texto "Alura Space Django"](https://user-images.githubusercontent.com/87834766/233518757-089582c3-7155-4b9d-809f-773d798d7f9f.png)

 ### Templates e Boas Práticas
## Alura-Space
> O Django é uma ótima ferramenta para fazer front-end e back-end trabalharem em sintonia.

# Ambiente de desenvolvimento

## IDE
Vscode

## Extensões 
SQlite Viewer - [Florian Klampfer](https://qwtel.com/)

## Linguagem
Python **3.10.9**

### Instalação Pip 
(Sistema Windows)
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
```
python get-pip.py 
``` 
### Ambiente Virtualizado 
[virtualenv](https://github.com/pypa/virtualenv)
```
pip install virtualenv
```
### Template 
[Link para baixar o Template](https://github.com/alura-cursos/alura_space/archive/refs/heads/projeto_front.zip)

> Django é um framework escrito em  Python e focado no desenvolvimento de projetos. Ele é uma espécie de “caixa de ferramentas” com várias soluções para o desenvolvimento de projetos.

# Virtualenv
``` 
python3 --version
virtualenv --version
```

```
venv/Scripts/Activate 
``` 
```
pip install django
```
<small>Instalar o Django com o pip, um programa de gerenciamento de pacotes do Python.</small>
# Servidor
>  Visualizar todas as dependências do projeto e os módulos que precisam ser instalados para que o projeto funcione: 
```
pip freeze 
```
<small>
Informa a versão de <b>Django, sqlparse, sgireft</b></small>

>asgiref==3.6.0
Django==4.2
sqlparse==0.4.3
tzdata==2023.3
> 
Execute o comando: 
```
pipfreeze > requiriments.txt 
```

# Setup
~~~
Django-admin startproject setup . 
~~~
<small>Será criado uma pasta chamada "setup", dentro de "alura-space" , com as configurações do projeto</small>

~~~
pip install -r requirements.txt
~~~
<small> o pip garante a instalação de todos os pacotes e módulos incluídos no arquivo "requirements.txt".</small>

## manage.py
Responsável por realizar a maioria dos comandos que utilizaremos para o desenvolvimento de aplicações Django e também por subir servidores.
 <br />

⚠️ Utilizar a versão do Python da <i>venv</i>

~~~
python manage.py runserver 
~~~

# Idioma Principal e Fuso Horário
**setup > setting.py** 
## setting.py 
Arquivo que contém todas as configurações do projeto
- dependências;
- <i>templates</i>;
- e mais. <br/>

Linhas 106 e 108 - <i>LANGUAGE_CODE</i> e <i>TIME_ZONE</i>

# Versionamento
Dependência python-dotenv
```
pip install python-dotenv
pip freeze > requirements.txt
```
[gitignore.io](https://www.toptal.com/developers/gitignore/)
Digitando "Django", irá gerar a definição de cada arquivo que por motivos de segurança, não podemos enviar para o Github.

# Criação do primeiro app
```
python manage.py startapp galeria 
```
Para sinalizar que o app "galeria" faz parte do nosso projeto.
"setup > settings.py"

Em INSTALLED_APPS, vamos passar o app: 
~~~
INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'galeria', <-- o app que acabamos de criar!
~~~
# Persistência de dados e Admin
> Django ORM --> O Django traduz uma classe para uma tabela no banco de dados - Bruno Divino
~~~
python manage.py makemigrations
python manage.py migrate
~~~
<small>Com o (.venv)</small>
## Criando Dados
Para adicionar um item 
~~~
python manage.py shell 
~~~
Para importar photography 
~~~
from galeria.models import photography
~~~
Após importar, a criação do dado:
~~~
picture = photography(name="NOME_DA_FOTOGRAFIA, legend="LEGENDA_DA_FOTOGRAFIA")
~~~
Para salvar
~~~
picture.save() 
~~~
Exibir os objetos criados no <i>model</i> de photography
~~~
photography.objects.all() 
~~~
## Criação do Administrator
~~~
python manage.py createsuperuser 
~~~


# Instrutor
[Guilherme Lima](https://cursos.alura.com.br/user/guilhermelima) e [Bruno Divino](https://github.com/BrunoDivino)
