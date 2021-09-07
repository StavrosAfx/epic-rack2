from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.rack, name='rack'),
    path('<slug:rows_slug>/', views.rack, name='rack_by_rows'),
] 