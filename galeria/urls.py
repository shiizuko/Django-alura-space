from django.contrib import admin
from django.urls import path
from galeria.views import index, imagem, search

#criando uma lista que possui todos os endpoints da aplicação relacionada a galeria:

urlpatterns = [
    path('', 
         index,
         name='index'),
    path('imagem/<int:picture_id>',
          imagem, 
          name='imagem'),
    path('admin/',
         admin.site.urls),
    path('search',
         search,
         name='search'),
]