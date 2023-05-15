from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Photography
from apps.galeria.forms import PhotographyForms
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
    
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in")
        return redirect('login')
    
    form = PhotographyForms
    if request.method == 'POST':
        form = PhotographyForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Image published successfully")
            return redirect('index')
    return render(request, 'galeria/new_image.html', {'form': form})

def edit_image(request, picture_id):
    photography = Photography.objects.get(id=picture_id)
    form = PhotographyForms(instance=photography)
    if request.method == 'POST':
        form = PhotographyForms(request.POST, request.FILES, instance=photography)
        if form.is_valid():
            form.save()
            messages.success(request, "Image updated successfully ")
            return redirect('index')
    return render(request, 'galeria/edit_image.html', { 'form': form, 'picture_id': picture_id})

def delete_image(request, picture_id):
    photography = Photography.objects.get(id=picture_id)
    photography.delete()
    messages.success(request, "Image deleted successfully")
    return redirect('index')