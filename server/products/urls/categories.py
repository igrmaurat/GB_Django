from django.urls import path

# Импортируем свою функцию
from products.views import (
    CategoryDetail, CategoryList,
    category_list, category_detail
)

app_name = 'categories'

urlpatterns = [
    path('<int:pk>/', CategoryDetail.as_view(), name="detail"),
    path('', CategoryList.as_view(), name="catalog"),

]
