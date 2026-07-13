from django.shortcuts import render
from .models import GalleryImage

# Create your views here.

def gallery(request):

    images = GalleryImage.objects.all()

    context = {
        'images' : images,
    }

    return render(request, "gallery/gallery.html", context)