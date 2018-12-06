import json
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.generic import (
    CreateView, UpdateView, DeleteView,
    ListView, DetailView
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.http import Http404, JsonResponse

from accounts.mixins import AdminRoleRequired
from products.forms import ProductForm
from products.models import Product
from functools import reduce
from django.db.models import Q
from django.http import JsonResponse


class ProductJsonListView(ListView):
   model = Product
   paginate_by = 10

   def serialize_object_list(self, queryset):
      return list(
         map(
            lambda itm: {
               'id': itm.id,
               'title': itm.title,
               'category': str(itm.category) if itm.category else None,
               'image': itm.image.url,
               'cost': itm.cost,
            },
            queryset
         )
      )
   def get_context_data(self, **kwargs):
      context = super(ProductJsonListView, self).get_context_data(**kwargs)

      data = {}
      page = context.get('page_obj')
      route_url = reverse('rest_products:catalog')

      data['next_url'] = None
      data['previous_url'] = None
      data['page'] = page.number
      data['count'] = page.paginator.count
      data['results'] = self.serialize_object_list(page.object_list)

      if page.has_next():
         data['next_url'] = f'{route_url}?page={page.next_page_number()}'

      if page.has_previous():
         data['previous_url'] = f'{route_url}?page={page.previous_page_number()}'

      return data

   def render_to_response(self, context, **response_kwargs):
      return JsonResponse(context)

class ProductCreateView(LoginRequiredMixin, AdminRoleRequired, CreateView):
   model = Product
   fields = [
      'title', 'h1', 'category',
      'image', 'snippet', 'cost'
   ]
   template_name = 'products/create.html'
   success_url = reverse_lazy("products:catalog")
   login_url = reverse_lazy('accounts:login')

class ProductUpdateView(LoginRequiredMixin, AdminRoleRequired, UpdateView):
   model = Product
   fields = [
      'title', 'h1', 'category',
      'image', 'snippet', 'cost'
   ]
   template_name = 'products/update.html'
   success_url = reverse_lazy("products:catalog")
   login_url = reverse_lazy('accounts:login')


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = Product
   template_name = 'products/delete.html'
   success_url = reverse_lazy('products:catalog')
   login_url = reverse_lazy('accounts:login')

   def test_func(self):
      return self.request.user.is_superuser



class ProductListView(ListView):
   model = Product
   template_name = 'products/catalog.html'
   context_object_name = 'products'
   paginate_by = 10

class ProductDetailView(DetailView):
   model = Product
   template_name = 'products/detail.html'
   context_object_name = 'products'

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


@login_required(login_url=reverse_lazy('accounts:login'))
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


def product_list(request):
   # context = {}

   # with open('products/data/products.json', 'r') as file:
   #     context = json.load(file)

   # return render(request, 'products/list.html', context)

   # query = Product.objects.all()

   query = get_list_or_404(Product)
   page = request.GET.get('page')
   paginator = Paginator(query, 10)

   products = paginator.get_page(page)

   return render(request, 'products/catalog.html', {'products': products})


def product_detail(request, pk):
   # context = {}

   # with open('products/data/products.json', 'r') as file:
   #     context = json.load(file)

   # return render(
   #     request,
   #     'products/detail.html',
   #     {
   #         'object': context['products'][idx]
   #     }
   # )

   # obj = Product.objects.get(id=pk)

   obj = get_object_or_404(Product, pk=pk)

   return render(request, 'products/detail.html', {'object': obj})

def product_json_list(request):
   query_params = (
      (key, list(map(int, value.split(',')))) if key.endswith('_in') else val
      for key, value in request.GET.items()
   )
   query = get_list_or_404(
      Product,
      reduce(
         lambda store, itm: store | Q(**{itm[0]: itm[1]}),
         query_params,
         Q()
      )
   )
   return JsonResponse(
      list(
         map(
            lambda itm: {
               'id': itm.id,
               'title': itm.title
            },
            query
         )
      ),
      safe = False
   )