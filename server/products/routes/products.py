from django.urls import path
from products.views import ProductJsonListView
#from products.views import product_json_list

app_name = 'rest_products'

urlpatterns = [
    path('', ProductJsonListView.as_view(), name='catalog'),
    #path('cart_list', product_json_list, name='catalog')
]