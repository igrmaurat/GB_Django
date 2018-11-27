from django.urls import path

# Импортируем свою функцию
from products.views import (
    ProductDetail,
    ProductList,
    ProductDelete,
    ProductUpdate,
    ProductCreate,
    catalog,
    product,
    product_create,
    product_update,
    product_delete
)

app_name = 'products'

urlpatterns = [
    path('<int:pk>/delete', ProductDelete.as_view(), name = 'delete'),
    path('<int:pk>/update', ProductUpdate.as_view(), name = 'update'),
    path('create/', ProductCreate.as_view(), name = 'create'),
    path('', ProductList.as_view(), name="catalog"),
    path('<int:pk>/', ProductDetail.as_view(), name="product"),

]

