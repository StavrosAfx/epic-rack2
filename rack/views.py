from django.shortcuts import get_object_or_404, render
from .models import Rack
from rows.models import Rows
from item.models import Item

# Create your views here.

def rack(request, rows_slug=None):
    rows = None
    rack = None
    items = None
    

    if rows_slug != None:

        rows = get_object_or_404(Rows, slug = rows_slug)
        rack = Rack.objects.filter(rows=rows)
       
    else:
        rack = Rack.objects.all()
        items = Item.objects.all()
    
        

    context = {
        'rack': rack,
        'items': items
    }
    return render(request, 'rack/rack.html',context)


