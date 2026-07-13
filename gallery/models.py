from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class GalleryProject(models.Model):
    """
    """
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(
        max_length=250, editable=True
        )
    description = models.TextField(blank=True)
    year = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=0)

    def __str__(self):
        return f'{self.title}'
    

class GalleryImage(models.Model):
    """
    """
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(
        max_length=250, editable=True
        )
    description = models.TextField(blank=True)
    image = CloudinaryField('image', default='placeholder')
    image_2 = CloudinaryField('image', default='placeholder')
    project = models.ForeignKey(GalleryProject, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'