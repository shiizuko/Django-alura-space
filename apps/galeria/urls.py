from django.contrib import admin
from django.urls import path
from apps.galeria.views import \
     index, imagem, search, new_image, edit_image, delete_image

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
    
     path('new-image',
         new_image,
         name='new_image'),
     
     path('edit-image/<int:picture_id>',
         edit_image,
         name='edit_image'),
     
     path('delete-image',
         delete_image,
         name='delete_image'),
]