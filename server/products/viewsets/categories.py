from rest_framework.viewsets import ModelViewSet

from products.serializers import CategorySerializer
from products.models import Category


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
