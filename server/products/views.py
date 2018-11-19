from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
from django.http import Http404
from django.urls import reverse_lazy
from django.core.paginator import Paginator

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

   #query = Product.objects.all() # этот вариант выведет список, даже если он пустой
   query = get_list_or_404(Product) # этот вариант отдаст 404 ответ, если в списке нет элементов

   # Пагинация ?page=2
   page = request.GET.get('page')
   paginator = Paginator(query, 10)
   products = paginator.get_page(page)

   return render(request, 'products/catalog.html', {'products': products} )

# Создаем функцию для страницы карточки товара detail
def product(request, pk):

   #obj = Product.objects.get(id=pk)
   obj = get_object_or_404(Product, pk=pk)

   return render(request, 'products/detail.html', {'products': obj})