from datetime import datetime
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.urls import reverse_lazy

from .models import Category, Product


class Productserializer(ModelSerializer):
    category = SerializerMethodField()
    image = SerializerMethodField()

    class Meta:
        model = Product
        fields = fields = [
            'url', 'title', 'h1','category',
            'image', 'snippet', 'cost'
        ]

    def get_category(self, obj):
        return obj.category.title if obj.category else ''

    def get_image(self, obj):
        return obj.image.url


class CategorySerializer(ModelSerializer):
    site_url = SerializerMethodField()
    is_new = SerializerMethodField()

    class Meta:
        model = Category
        fields = ['url', 'title', 'snippet', 'site_url', 'is_new']


    def get_is_new(self, obj):
        return datetime.now().date == obj.created.date

    def get_site_url(self, obj):
        return str(reverse_lazy('categories:detail', kwargs={'pk': obj.id}))

    # def to_representation(self, instance):
    #     context = super(CategorySerializer, self).to_representation(instance)
    #     context['site_url'] = str(reverse_lazy('categories:detail', kwargs={'pk':instance.id}))
    #     context['is_new'] = datetime.now().date == instance.created.date
    #     return context
