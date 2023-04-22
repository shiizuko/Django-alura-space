from django.shortcuts import render, get_object_or_404
from galeria.models import Photography

def index(request):
    photographys = Photography.objects.order_by("date_picture").filter(published=True)
    return render(request, "galeria/index.html", {"cards": photographys})


def imagem(request, picture_id):
    picture = get_object_or_404(Photography, pk=picture_id)
    return render(request, "galeria/imagem.html", {"photography": picture})

def search(request):
    photographys = Photography.objects.order_by("date_picture").filter(published=True)
    if "search" in request.GET:
        search_name = request.GET["search"]
        if search_name:
            photographys = photographys.filter(name__icontains=search_name)
    return render(request, "galeria/search.html", {"cards": photographys})