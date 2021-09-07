from django.http import HttpRequest
from django.shortcuts import render 
from rows.models import Rows

def home(request):
    rows = Rows.objects.all()
    context= {
        'rows': rows
    }
    return render(request, 'home.html', context)