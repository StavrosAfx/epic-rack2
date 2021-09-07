from django.db.models.deletion import CASCADE
from rows.models import Rows
from django.db import models
from rows.models import Rows
# Create your models here.
class Rack(models.Model):
    rack_name   = models.CharField(max_length=4, unique=True)
    slug        = models.SlugField(max_length=4, unique=True)
    front_image = models.ImageField(upload_to='photos/front_rack')
    back_image  = models.ImageField(upload_to='photos/back_rack')
    rows        = models.ForeignKey(Rows, on_delete=models.CASCADE)

    def __str__(self):
        return self.rack_name
    
