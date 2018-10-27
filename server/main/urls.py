from django.urls import path

# Импортируем свою функцию
from main.views import (main, contact, )

urlpatterns = [
    path('', main, name="main"),
    path('contact/', contact, name="contact"),

]

