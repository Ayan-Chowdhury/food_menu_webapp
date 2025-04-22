from django.contrib import admin
from .models import Item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name','item_desc','item_price']


admin.site.register(Item,ItemAdmin)