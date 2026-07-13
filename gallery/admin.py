from django.contrib import admin
from .models import GalleryImage, GalleryProject
# Register your models here.

class GalleryImageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


class GalleryProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}

admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(GalleryProject, GalleryProjectAdmin)