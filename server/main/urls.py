from django.urls import path

# Импортируем свою функцию
from main.views import (main, contact, )

app_name = 'main'

urlpatterns = [
    path('', main, name="main"),
    path('contact/', contact, name="contact"),

]

