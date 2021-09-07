from django.shortcuts import render

# Create your views here.


from django.shortcuts import get_object_or_404, render
from .models import Item
from rack.models import Rack

# Create your views here.

def item(request,  rack_slug=None):

    rack = None
    item = None

    #a1 == A1 false A == A 

  

 
        

    if rack_slug != None:
        item = get_object_or_404(Rack, rack = rack_slug)
        item = Item.objects.filter(rack = rack)
        
    else:
        item = Item.objects.all()
        

    context= {
        
        'item' : item
    }
    return render(request, 'rack/rack.html',context)
        