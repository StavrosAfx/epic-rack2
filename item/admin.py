from django.contrib import admin
from .models import Item
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ('rack','slot','ending_slot', 'item_name', 'description' , 'item_AC', 'item_DC')
    prepopulated_fields = {'slug': ('item_name',)}

admin.site.register(Item,ItemAdmin )