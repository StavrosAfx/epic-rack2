from django.contrib import admin
from .models import Rows
# Register your models here.
class RowsAdmin(admin.ModelAdmin):
    list_display = ('row_name' , 'place')
    prepopulated_fields = {'slug': ('row_name',)}

admin.site.register(Rows, RowsAdmin)