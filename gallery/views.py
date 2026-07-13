from django.shortcuts import render, get_object_or_404
from .models import GalleryImage, GalleryProject

# Create your views here.

def gallery(request):

    projects = GalleryProject.objects.all().order_by('-year')

    context = {
        'projects': projects,
    }

    return render(request, "gallery/gallery.html", context)


def project(request, slug):
    """
    """
    project = get_object_or_404(GalleryProject, slug=slug)
    images = GalleryImage.objects.filter(project=project)

    context = {
        'project': project,
        'images': images,
    }

    return render(request, "gallery/project-view.html", context)


def image(request, slug, id):
    """
    """
    project = get_object_or_404(GalleryProject, slug=slug)
    image = get_object_or_404(GalleryImage, id=id)

    context = {
        'image': image,
        'project': project,
    }

    return render(request, "gallery/image-view.html", context)