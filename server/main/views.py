from django.shortcuts import render
from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse

# Создаем функцию для главной страницы
def main(request):
   template = get_template('main/index.html')
   context = {
      'h1': 'Магазин "Товары почтой"',
      'page_text': [
         'Рады приветствовать вас на сайте "Товары почтой". Здесь вы можете купить всякую всячину!',
         "Здоровье есть безусловная ценность. Состояние окружающей нас среды имеет огромное влияние на наше здоровье.",
         """Экологические показатели окружающей среды зависят от географического расположения, 
         от культуры общества (мы никогда по собственной воле не откажемся от автомобилей), 
         экономико-политических условий государства. На все на эти «внешние» факторы наше персональное влияние незначительно. 
         При этом, современный человек в среднем около 90% времени проводит в закрытых помещениях: дом, спальни, рабочие кабинеты. 
         Поэтому экологические показатели микроклимата влияют на нас даже больше, чем экология во вне.""",
         """Практика показывает, что даже в экологически чистых зонах часто условия внутри жилья оказываются крайне 
         неблагоприятными исключительно по внутренним причинам: плохая вентиляция, некачественные отделочные материалы, 
         дым от печи, сигарет и т.п. На экологию и условия конкретных помещений мы имеем гораздо больше влияния, чем в
          целом на экологию района проживания. И даже более того, мы сам ответственны за качество экологических 
          показателей нашего жилья или нашего рабочего места. Мы можем создавать комфортные и здоровые условия для себя 
          и для жизни наших близких. Центр экологии жилья предлагает комплексный подход к улучшению и оздоровлению 
          условий нашей жизни внутри помещений. Окружающая нас среда имеет множество «точек» влияния на нас. 
          Это и качество воздуха, и качество воды, и электромагнитные поля, и микробиология, и шум, и освещение, и даже
           психологический климат. """,
         """И все это имеет влияние на нас, на наше здоровье, на успеваемость и работоспособность, на наше психическое 
         состояние. Качество воздуха один из важнейших экологических параметров. Хотя Центр экологии жилья предлагает
          услуги и по оценке электромагнитных полей, шума и освещение, улучшение качества воздуха – первая наша 
          специализация. Если обеспечение чистой водой уже развитая отрасль, то осознание необходимости 
          чистого воздуха часто ускользает от нашего внимания. Воды мы потребляем около 2-х литров в день, воздуха 
          около 10 тысяч литров. Воду мы чистим, смягчаем, покупаем. В отличие от воды воздух, часто неочищенный, мы 
          потребляем с помощью наиболее нежного органа – легких, а из легких все его содержимое сразу попадает нам в 
          кровь. Поэтому нельзя переоценить важность качества воздуха для нашего здоровья. И даже малейшие концентрации
           токсических веществ в воздухе оказывают существенное влияние на наш организм.""",
      ],
      'footer': '© Сайт кампании "Товары почтой". Все права защищены. 2018 год.',
   }
   response_string = template.render(context)

   return HttpResponse(response_string)

# Создаем функцию для страницы контактов
def contact(request):
   context = {
      'contacts': [ 'г.Москва, улица Ленина, дом 1 ',
                    'Наш телефон 8 - 800 - 100 - 1000',
                    'Наша почта pochta @ mail.ru',

      ],
      'footer': '© Сайт кампании "Товары почтой". Все права защищены. 2018 год.',
   }
   response_string = render_to_string(
      'main/contact.html' , context
   )
   return HttpResponse(response_string)

# Создаем функцию для страницы about
def catalog(request):

   context = {
      'footer': '© Сайт кампании "Товары почтой". Все права защищены. 2018 год.',
   }
   response_string = render_to_string(
      'main/catalog.html', context
   )
   return HttpResponse(response_string)

# Создаем функцию для страницы product_1
def product_1(request):
   return render(request, 'main/product_1.html')

# Создаем функцию для страницы product_2
def product_2(request):
   return render(request, 'main/product_2.html')

# Создаем функцию для страницы product_3
def product_3(request):
   return render(request, 'main/product_3.html')

