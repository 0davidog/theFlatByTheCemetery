from django.db import models

# Create your models here.
class GalleryProject(models.Model):
    """
    """
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(
        max_length=250, editable=True
        )
    description = models.TextField(blank=True)

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
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return f'{self.title}'