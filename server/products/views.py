from django.shortcuts import render, redirect, get_object_or_404
from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
from django.http import Http404
from django.urls import reverse_lazy

import json

from .models import Product
from .forms import ProductForm


def product_delete(request, pk):

   obj = get_object_or_404(Product, pk = pk)
   success_url = reverse_lazy("main:main")

   if request.method == "POST":
      obj.delete()
      return redirect(success_url)

   return render(
      request,
      'products/delete.html',
      {'obj': obj }
   )



def product_update(request, pk):
   # try:
   #    obj = Product.objects.get(pk = pk)
   #
   # except Exception as err:
   #    raise Http404
   obj = get_object_or_404(Product, pk = pk)

   form = ProductForm(instance = obj)
   success_url = reverse_lazy("main:main")

   if request.method == "POST":

      form = ProductForm(request.POST,
                         files = request.FILES,
                         instance = obj)

      if form.is_valid():
         form.save()
         return redirect(success_url)

   return render(
      request,
      'products/update.html',
      {
         'form': form,
         'obj': obj
      }
   )




def product_create(request):
   form = ProductForm()
   success_url = reverse_lazy("main:main")

   if request.method == "POST":
      form = ProductForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect(success_url)



   return render(request, 'products/create.html', {'form': form})


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



