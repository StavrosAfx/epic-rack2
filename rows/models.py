from place.models import Place
from django.db import models
from django.urls import reverse

# Create your models here.

class Rows(models.Model):
    row_name  = models.CharField(max_length=2, unique=True)
    slug      = models.SlugField(max_length=2, unique=True)
    images    = models.ImageField(upload_to='photos/rows')
    place     = models.ForeignKey(Place, on_delete=models.CASCADE)
    

   
    def get_url(self):
        return reverse('rack_by_rows', args= [self.slug])

    def __str__(self):
        return self.row_name

    