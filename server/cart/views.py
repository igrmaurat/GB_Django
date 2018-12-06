import json
from functools import reduce
from django.apps import apps
from django.db.models import Q
from django.shortcuts import render
#from django.http import JsonResponce
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import (
    View, CreateView, DetailView
)

from . models import Purchase

def cart_view(request):
    return render(request, 'cart/cart.html')

class PurchaseCreateView(LoginRequiredMixin, View):
    login_url = ''
    product_model = apps.get_model('products', 'product')

    def post(self, request):
        data = json.loads(request.body)

        product_list = self.product_model.objects.filter(
            reduce(
                lambda store, key: store | Q(pk=key),
                data.keys(),
                Q()
            )
        )
        obj = Purchase.objects.create(
            user=request.user,
        )

        for product in product_list:
            obj.items.create(
                product = product,
                value = data[str(product.id)],
            )

        return JsonResponce(
            {
                'success_url': reverse(
                    'cart:detail',
                    kwargs = {'pk': obj.id}
                )
            }
        )
class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = 'cart/detail.html'


