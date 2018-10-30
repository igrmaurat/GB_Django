from django.urls import path

# Импортируем свою функцию
from .views import (catalog,
                        product,
                    )

app_name = 'products'

urlpatterns = [
    path('', catalog, name="catalog"),
    path('<int:idx>/', product, name="product"),

]

