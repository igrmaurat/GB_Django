from rest_framework.viewsets import ModelViewSet

from products.serializers import Productserializer
from products.models import Product


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Productserializer