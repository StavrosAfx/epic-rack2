from django.contrib import admin
from .models import Rack
# Register your models here.

class RackAdmin(admin.ModelAdmin):
    list_display = ('rack_name', 'rows')
    prepopulated_fields = {'slug' : ('rack_name',)}

admin.site.register(Rack, RackAdmin)