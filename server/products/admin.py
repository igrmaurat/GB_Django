from datetime import datetime

from django.contrib import admin
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'h1', 'category',
        'picture', 'cost', 'modified', 'created', 'is_new'
    ]
    list_filter = [
        'category', 'image',
        'modified', 'created'
    ]
    search_fields = [
        'title', 'snippet', 'cost'
    ]
    fieldsets = (
        (
            None, {
                'fields': ('title', 'category',)
            },
        ),
        (
            "Context", {
                'fields': ('h1', 'image', 'snippet', 'cost',)
            },
        ),
    )
    def picture(self, obj):
        return render_to_string(
            'products/components/picture.html',
            {'url': obj.image.url}
        )
    def is_new(self, obj):
        return datetime.now().date() == obj.created.date()

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'h1', 'modified', 'created', 'is_new'
    ]
    list_filter = [
        'modified', 'created'
    ]
    search_fields = [
        'title', 'snippet'
    ]
    def is_new(self, obj):
        return datetime.now().date() == obj.created.date()



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
