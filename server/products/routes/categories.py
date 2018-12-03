from django.urls import path

from products.views import CategoryJsonListView


app_name = 'rest_categories'

urlpatterns = [
    path('', CategoryJsonListView.as_view(), name='catalog'),
]