from django.shortcuts import render
from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
import json

from .models import Product

# Создаем функцию для главной страницы

# Создаем функцию для страницы about
def catalog(request):

   context = {}


   # with open("products/data/products.json", 'r') as file:
   #    context = json.load(file)
   #
   #
   # context['h1'] = 'Наши товары'
   # context['footer'] = '© Сайт кампании "Товары почтой". Все права защищены. 2018 год.'
   #
   # response_string = render_to_string(
   #    'products/catalog.html', context
   # )
   # return HttpResponse(response_string)

   query = Product.objects.all()
   return render(request, 'products/catalog.html', {'products': query} )

# Создаем функцию для страницы product_1
def product(request, pk):
   context = {}

   # with open("products/data/products.json", 'r') as file:
   #    context = json.load(file)
   #
   # return render(request, 'products/detail.html',
   #               {
   #                  'object': context['products'][idx]
   #               })

   obj = Product.objects.get(id=pk)
   return render(request, 'products/detail.html', {'products': obj})



