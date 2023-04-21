from django.shortcuts import render, get_object_or_404
from galeria.models import Photography

def index(request):
    photographys = Photography.objects.filter(published=True)
    return render(request, "galeria/index.html", {"cards": photographys})


def imagem(request, picture_id):
    picture = get_object_or_404(Photography, pk=picture_id)
    return render(request, "galeria/imagem.html", {"photography": picture})
