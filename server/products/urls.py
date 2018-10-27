from django.urls import path

# Импортируем свою функцию
from .views import (catalog,
                        product_1,product_2, product_3,
                        )

urlpatterns = [
    path('', catalog, name="catalog"),
    path('product_1/', product_1, name="product_1"),
    path('product_2/', product_2, name="product_2"),
    path('product_3/', product_3, name="product_3"),

]

