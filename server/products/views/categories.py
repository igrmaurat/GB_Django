import json

from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.generic import (
    ListView, DetailView
)
from django.urls import reverse_lazy
from django.core.paginator import Paginator

from products.forms import ProductForm

from products.serializers import CategorySerializer
from products.forms import ProductForm
from products.models import Category

class CategoryList(ListView):
    model = Category
    template_name = 'categories/categories.html'
    paginate_by = 10

class CategoryDetail(DetailView):
    model = Category
    template_name = 'categories/detail.html'

    def get_context_data(self, **kwargs):
        obj = kwargs.get('object')
        page = self.request.GET.get('page')
        paginator = Paginator(obj.product_set.all(), 10)

        page_object = paginator.get_page(page)

        return {
            'object': obj,
            'object_list': page_object.object_list,
            'paginator': paginator,
            'page_obj': page_object,

        }

class CategoryJsonListView(ListView):
    model = Category
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(CategoryJsonListView, self).get_context_data(**kwargs)

        data = {}
        page = context.get('page_obj')
        route_url = reverse('rest_products:catalog')

        data['next_url'] = None
        data['previous_url'] = None
        data['page'] = page.number
        data['count'] = page.paginator.count
        data['results'] = CategorySerializer(page.object_list, many=True).data

        if page.has_next():
            data['next_url'] = f'{route_url}?page={page.next_page_number()}'

        if page.has_previous():
            data['previous_url'] = f'{route_url}?page={page.previous_page_number()}'

        return data

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)

def category_list(request):
    query = get_list_or_404(Category)
    page = request.GET.get('page')
    paginator = Paginator(query, 10)

    categories = paginator.get_page(page)

    return render(request, 'categories/categories.html', {'categories': categories})

def category_detail(request, pk):
    obj = get_object_or_404(Category, pk = pk)

    page = request.GET.get('page')
    paginator = Paginator(obj.product_set.all(), 10)

    results = paginator.get_page(page)

    return render(
        request,
        'categories/detail.html',
        {
            'object': obj,
            'results': results
        }
    )
