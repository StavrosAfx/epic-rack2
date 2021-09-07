from rack.models import Rack
from django.db import models
from rack.models import Rack
# Create your models here.

class Item(models.Model):
    slot        = models.IntegerField()
    ending_slot = models.IntegerField()
    item_name   = models.CharField(max_length=100, unique=True)
    slug        = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=100, unique=True)
    rack        = models.ForeignKey(Rack, on_delete=models.CASCADE)
    item_AC     = models.CharField(max_length=50)
    item_DC     = models.CharField(max_length=50)

def __str__(self):
    return self.item_name

