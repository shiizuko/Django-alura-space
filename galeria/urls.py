from django.urls import path
from galeria.views import index

#criando uma lista que possui todos os endpoints da aplicação relacionada a galeria:

urlpatterns = [
    path('', index)
]