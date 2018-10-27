from django.shortcuts import render
from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
import json

# Создаем функцию для главной страницы

# Создаем функцию для страницы about
def catalog(request):

   context = {}


   with open("products/data/products.json", 'r') as file:
      context = json.load(file)


   context['h1'] = 'Наши товары'
   context['footer'] = '© Сайт кампании "Товары почтой". Все права защищены. 2018 год.'

   response_string = render_to_string(
      'products/catalog.html', context
   )
   return HttpResponse(response_string)

# Создаем функцию для страницы product_1
def product_1(request):
   return render(request, 'products/product_1.html')

# Создаем функцию для страницы product_2
def product_2(request):
   return render(request, 'products/product_2.html')

# Создаем функцию для страницы product_3
def product_3(request):
   return render(request, 'products/product_3.html')

