from django.urls import path

# Импортируем свою функцию
from main.views import (main, contact, catalog,
                        product_1,product_2, product_3,
                        )

urlpatterns = [
    path('', main, name="main"),
    path('contact/', contact, name="contact"),
    path('catalog/', catalog, name="catalog"),
    path('catalog/product_1/', product_1, name="product_1"),
    path('catalog/product_2/', product_2, name="product_2"),
    path('catalog/product_3/', product_3, name="product_3"),

]

