from django.urls import path

# Импортируем свою функцию
from .views import (
    catalog,
    product,
    product_create,
    product_update,
    product_delete
)

app_name = 'products'

urlpatterns = [
path('<int:pk>/delete', product_delete, name = 'delete'),
    path('<int:pk>/update', product_update, name = 'update'),
    path('create/', product_create, name = 'create'),
    path('', catalog, name="catalog"),
    path('<int:pk>/', product, name="product"),

]

