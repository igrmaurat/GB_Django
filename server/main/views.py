from django.shortcuts import render

# Создаем функцию для главной страницы
def main(request):
   return render(request, 'main/index.html')

# Создаем функцию для страницы контактов
def contact(request):
   return render(request, 'main/contact.html')

# Создаем функцию для страницы about
def catalog(request):
   return render(request, 'main/catalog.html')

# Создаем функцию для страницы product_1
def product_1(request):
   return render(request, 'main/product_1.html')

# Создаем функцию для страницы product_2
def product_2(request):
   return render(request, 'main/product_2.html')

# Создаем функцию для страницы product_3
def product_3(request):
   return render(request, 'main/product_3.html')

