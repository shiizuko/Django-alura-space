from django.shortcuts import render
from galeria.models import photography

def index(request):
    photographys = photography.objects.all()
    return render(request, "galeria/index.html", {"cards": photographys})


def imagem(request):
    return render(request, "galeria/imagem.html")
