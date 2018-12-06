from django.contrib import admin

# Register your models here.
from .models import Purchase, PurchaseItem

admin.site.register(Purchase)
admin.site.register(PurchaseItem)