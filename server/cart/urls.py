from django.urls import path

# Импортируем свою функцию
from cart.views import (
    cart_view,
)

app_name = 'cart'

urlpatterns = [
    path('', cart_view, name='cart')
]

