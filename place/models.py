from django.db import models

# Create your models here.
class Place(models.Model):
    place_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    rack_line_image = models.ImageField(upload_to = 'photos/racklines', blank=True)


    def __str__(self):  
        return self.place_name 
