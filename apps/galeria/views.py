from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Photography
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in")
        return redirect('login')
    
    photographys = Photography.objects.order_by("date_picture").filter(published=True)
    return render(request, "galeria/index.html", {"cards": photographys})


def imagem(request, picture_id):
    picture = get_object_or_404(Photography, pk=picture_id)
    return render(request, "galeria/imagem.html", {"photography": picture})

def search(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in")
        return redirect('login')
    
    photographys = Photography.objects.order_by("date_picture").filter(published=True)
    if "search" in request.GET:
        search_name = request.GET["search"]
        if search_name:
            photographys = photographys.filter(name__icontains=search_name)
    return render(request, "galeria/search.html", {"cards": photographys})

def new_image(request):
    return render(request, 'galeria/new_image.html')

def edit_image(request):
    pass

def delete_image(request):
    pass