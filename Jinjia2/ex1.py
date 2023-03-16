# pip3 install Jinja2

from jinja2 import Template
from markupsafe import escape # pip install jinja2==3.0.3 - escape не работает на новвой версии, только на 3.0.3

from jinja2 import Environment, FileSystemLoader, FunctionLoader # Загрузчик шаблонов 


# name = "Федор" 

# tm = Template("Привет {{name}}") # создаим экземплаяр класса tm на основе текстового шаблона через класс Template, который мы импортировали в самом начале. Для чего это нужно: Темплейт подставляет в фигурные скобки присвоенное значение нейму. То есть Темплейт подставляет в фигурные скобки вместо name то значение, которое мы name присвоили. Когда Теплейт это делает == он это делает это происходит через метод render, для этого мы должны создать переменную которой присваиваем наш экземпляр класса tm и применяем к нему метод render в котором мы говорим что наш {{name}} равен name = "Федор" и вот эта команда:

# msg = tm.render(name=name)

# и давайте просто распечатаем эту переменную:

# print(msg)

###################################
# конечно, в простых случаях мы можем и должны делать так:

# msg2 = f'Привет {name}'
# print(msg2)

# но сложные конструкции мы так не сделаем, поэтому надо делать через дзинза

###################################
"""
давайте рассмотрим какие контрукции у нас есть:

{%%} - спецификатор шаблона
{{}} - выражение для вставки конструкции пайтон в шаблон
{##} - блок комментариев
# ## - строковый комментарий
"""

######################
# расмотрим еще пример:

# name = "Федор" 
# age = 28
# tm = Template("Мне {{ a }} лет и зовут меня {{ n }}.")
# msg = tm.render(n=name, a=age)
# print(msg)

# Мне 28 лет и зовут меня Федор.

######################
# расмотрим еще пример:

# name = "Федор" 
# age = 28
# tm = Template("Мне {{ a*2 }} лет и зовут меня {{ n.upper() }}.")
# msg = tm.render(n=name, a=age)
# print(msg)

# Мне 56 лет и зовут меня ФЕДОР.

######################
# расмотрим еще пример:

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# per = Person("Федор", 33)

# tm = Template("Мне {{ p.age }} лет и зовут меня {{ p.name }}.")
# msg = tm.render(p=per)
# print(msg)

# Мне 33 лет и зовут меня Федор.

# расмотрим еще пример:

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def getName(self):
#         return self.name

#     def getAge(self):
#         return self.age

# per = Person("Федор", 33)

# tm = Template("Мне {{ p.getAge() }} лет и зовут меня {{ p.getName() }}.")
# msg = tm.render(p=per)
# print(msg)

# Мне 33 лет и зовут меня Федор.

# расмотрим еще пример:

# per = {'name': "Федор", 'age': 34}

# tm = Template("Мне {{ p.age }} лет и зовут меня {{ p.name }}.")
# msg = tm.render(p=per)
# print(msg)

# Мне 34 лет и зовут меня Федор.

# расмотрим еще пример:

# per = {'name': "Федор", 'age': 34}

# tm = Template("Мне {{ p['age'] }} лет и зовут меня {{ p['name'] }}.")
# msg = tm.render(p=per)
# print(msg)

# Мне 34 лет и зовут меня Федор.

# расмотрим еще пример:

# data = """Модуль Jinja вместо определения {{name}} подставляет соответствующее значение"""
# tm = Template(data)
# msg = tm.render(name='Федор')
# print(msg)

# Модуль Jinja вместо определения Федор подставляет соответствующее значение

"""
ЭКРАНИРОВАНИЕ:
что если мы не хотим, чтобы в фигурных скобках менялось значение и у нас оставались фмгурные скобки как сообзщение:

{%raw%} ... {%endraw%} - все что помещается между блоками вместо многоточия, то так и останется в неизменном виде


{%for<выражение>%}
    <повторяемый фрагмент> - позволяет формировать список на основе любого итерируемого объекта
{%endfor%}

"""

# расмотрим еще пример:

# data = """{%raw%}Модуль Jinja вместо определения {{name}} подставляет соответствующее значение{%endraw%}"""
# tm = Template(data)
# msg = tm.render(name='Федор')
# print(msg)

# Модуль Jinja вместо определения {{name}} подставляет соответствующее значение

# При работе с текстовыми хтмл шаблонами часто возникает необходимость в экранировании некоторых символов, котороые браузерами воспринимаются как определениями тегов, например:

# link = """В HTML документе ссылки определяются так: <a href="#">Ссылка</a>"""
# tm = Template(link)
# msg = tm.render()
# print(msg)
# мы получим вот такой результат
# В HTML документе ссылки определяются так: <a href="#">Ссылка</a>

# Но в хтмл документе мы не увидим всех этих символов, а будет написано только Ссылка и представлена в виде ссылки В HTML документе ссылки определяются так: Ссылка, и если нам надо вывсети не как ссылку а как текст данную запись, то нам необходимо применить экранирование:

# link = """В HTML документе ссылки определяются так: <a href="#">Ссылка</a>"""
# tm = Template("{{link | e}}") # e - escape экранирование в дзинза
# msg = tm.render(link=link)
# print(msg)

# В HTML документе ссылки определяются так: &lt;a href=&#34;#&#34;&gt;Ссылка&lt;/a&gt;

# а в хтмл файле будет отображаться так: В HTML документе ссылки определяются так: <a href="#">Ссылка</a>

############################

# экранирование можно получить и более простым кодом, импортировав escape, необходимо только импортировать ескейп:

# from markupsafe import escape # pip install jinja2==3.0.3 - escape не работает на новвой версии, только на 3.0.3

# link = """В HTML документе ссылки определяются так: <a href="#">Ссылка</a>"""
# msg = escape(link) 
# print(msg)

# В HTML документе ссылки определяются так: &lt;a href=&#34;#&#34;&gt;Ссылка&lt;/a&gt;

#####################

# cities = [
#         {'id':1, 'city':'Москва'},
#         {'id':2, 'city':'Тверь'},
#         {'id':3, 'city':'Минск'},
#         {'id':4, 'city':'Смоленск'},
#         {'id':5, 'city':'Калуга'}
# ]
# link = '''<select name="cities">
# {% for i in cities %}
#     <option value="{{i['id']}}">{{i['city']}}</option>
# {% endfor %}
# </select>'''

# tm = Template(link)
# msg = tm.render(cities=cities)
# print(msg)

# <select name="cities">

#     <option value="1">Москва</option>

#     <option value="2">Тверь</option>

#     <option value="3">Минск</option>

#     <option value="4">Смоленск</option>

#     <option value="5">Калуга</option>

# </select>

###############################
# при помощи минуса мы можем убирать пробелы и переносы строк:

# cities = [
#         {'id':1, 'city':'Москва'},
#         {'id':2, 'city':'Тверь'},
#         {'id':3, 'city':'Минск'},
#         {'id':4, 'city':'Смоленск'},
#         {'id':5, 'city':'Калуга'}
# ]
# link = '''<select name="cities">
# {% for i in cities -%}
#     <option value="{{i['id']}}">{{i['city']}}</option>
# {% endfor -%}
# </select>'''

# tm = Template(link)
# msg = tm.render(cities=cities)
# print(msg)

# <select name="cities">
# <option value="1">Москва</option>
# <option value="2">Тверь</option>
# <option value="3">Минск</option>
# <option value="4">Смоленск</option>
# <option value="5">Калуга</option>
# </select>

#############################
# при помощи минуса мы можем убирать пробелы и переносы строк и сделать вывод в одну строку:

# cities = [
#         {'id':1, 'city':'Москва'},
#         {'id':2, 'city':'Тверь'},
#         {'id':3, 'city':'Минск'},
#         {'id':4, 'city':'Смоленск'},
#         {'id':5, 'city':'Калуга'}
# ]
# link = '''<select name="cities">
# {% for i in cities -%}
#     <option value="{{i['id']}}">{{i['city']}}</option>{% endfor %}
# </select>'''

# tm = Template(link)
# msg = tm.render(cities=cities)
# print(msg)

# <select name="cities">
# <option value="1">Москва</option><option value="2">Тверь</option><option value="3">Минск</option><option value="4">Смоленск</option><option value="5">Калуга</option>
# </select>

###############################
# Также мы можем сделать и с логическими операторами иф:

# cities = [
#         {'id':1, 'city':'Москва'},
#         {'id':2, 'city':'Тверь'},
#         {'id':3, 'city':'Минск'},
#         {'id':4, 'city':'Смоленск'},
#         {'id':5, 'city':'Калуга'}
# ]
# link = '''<select name="cities">
# {% for i in cities -%}
# {% if i.id >4 -%}
#     <option value="{{i['id']}}">{{i['city']}}</option>
# {% endif -%}
# {% endfor -%}
# </select>'''

# tm = Template(link)
# msg = tm.render(cities=cities)
# print(msg)

# <select name="cities">
# <option value="5">Калуга</option>
# </select>

# Также мы можем сделать и с логическими операторами иф:

# cities = [
#         {'id':1, 'city':'Москва'},
#         {'id':2, 'city':'Тверь'},
#         {'id':3, 'city':'Минск'},
#         {'id':4, 'city':'Смоленск'},
#         {'id':5, 'city':'Калуга'}
# ]
# link = '''<select name="cities">
# {% for i in cities -%}
# {% if i.id >4 -%}
#     <option value="{{i['id']}}">{{i['city']}}</option>
# {% elif i.city == "Москва" -%}
#     <option>{{i['city']}}</option>
# {% else -%}
#     {{i['city']}}
# {% endif -%}
# {% endfor -%}
# </select>'''

# tm = Template(link)
# msg = tm.render(cities=cities)
# print(msg)

# <select name="cities">
# <option>Москва</option>
# Тверь
# Минск
# Смоленск
# <option value="5">Калуга</option>
# </select>

"""
Фильтры и макросы:

sum - вычисление суммы
sum(iterable, attribute=None, start=0) - можно проссумировать итерируемый объект, доп параметры указываются через атрибут, дополнительная прибака какойто суммы это старт)
и многие другие филтры

фильтры внутри шаблона:
{%filter<название фильтра>%}
<фрагмент для применения филттра>
{%endfilter%}


вложенные макросы:
{%call[(параметры)]<вызов макроса>%}
<вложенный шаблон>
{%endcall%}

"""

# cars = [
#     {'model': 'Ауди', 'price': 23000},
#     {'model': 'шкода', 'price': 17300},
#     {'model': 'вольво', 'price': 33400},
#     {'model': 'бмы', 'price': 22300}
# ]
# tpl = "Суммарная цена автомобилей {{ cs | sum(attribute='price') }}"
# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)

# Суммарная цена автомобилей 96000

##########################
# и еще пример

# cars = [15, 34, 44, 332]
# tpl = "Суммарная цена автомобилей {{ cs | sum + 56 }}"
# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)

# Суммарная цена автомобилей 481

##########################
# и еще пример

# cars = [
#     {'model': 'Ауди', 'price': 23000},
#     {'model': 'шкода', 'price': 17300},
#     {'model': 'вольво', 'price': 33400},
#     {'model': 'бмы', 'price': 22300}
# ]
# tpl = "Самый дороой автомобиль {{ cs | max(attribute='price') }}"
# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)

# Самый дороой автомобиль {'model': 'вольво', 'price': 33400}

##########################
# и еще пример

# cars = [
#     {'model': 'Ауди', 'price': 23000},
#     {'model': 'шкода', 'price': 17300},
#     {'model': 'вольво', 'price': 33400},
#     {'model': 'бмы', 'price': 22300}
# ]
# tpl = "Самый дороой автомобиль {{ (cs | max(attribute='price')).model }}" # обращаемся здесь как к словарю и вытаскиваем ключ
# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)

# Самый дороой автомобиль вольво

##########################
# и еще пример

# cars = [
#     {'model': 'Ауди', 'price': 23000},
#     {'model': 'шкода', 'price': 17300},
#     {'model': 'вольво', 'price': 33400},
#     {'model': 'бмы', 'price': 22300}
# ]
# tpl = "Самый дороой автомобиль {{ cs | random }}" # рандомная строка
# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)

# Самый дороой автомобиль {'model': 'вольво', 'price': 33400}

##########################
# и еще пример

# cars = [
#     {'model': 'Ауди', 'price': 23000},
#     {'model': 'шкода', 'price': 17300},
#     {'model': 'вольво', 'price': 33400},
#     {'model': 'бмы', 'price': 22300}
# ]
# tpl = 'Самый дороой автомобиль {{ cs | replace("o", "O") }}' # заменим букву в строке
# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)

# Самый дороой автомобиль [{'mOdel': 'Ауди', 'price': 23000}, {'mOdel': 'шкода', 'price': 17300}, {'mOdel': 'вольво', 'price': 33400}, {'mOdel': 'бмы', 'price': 22300}]

##########################
# и еще пример

# person = [
#     {"name": "Alex", "old": 18, "weight": 78.5},
#     {"name": "Nikol", "old": 29, "weight": 82.3},
#     {"name": "Ivan", "old": 33, "weigth": 94.0}
# ]
# tpl = '''
# {%- for i in users -%}
# {% filter upper %}{{i.name}}{% endfilter %}
# {% endfor -%}
# '''
# tm = Template(tpl)
# msg = tm.render(users=person)
# print(msg)

# ALEX
# NIKOL
# IVAN

###########################
# МАКРОСЫ и вложенные макросы

# html = '''
# {%- macro input(name, value='', type='text', size=20) -%}
#     <input type="{{ type }}" name="{{name}}" value="{{ value }}" size="{{size}}">
# {%- endmacro -%}
# <p>{{ input('username')}}
# <p>{{ input('email')}}
# <p>{{ input('password')}}
# '''
# tm = Template(html)
# msg = tm.render()
# print(msg)

# <p><input type="text" name="username" value="" size="20">
# <p><input type="text" name="email" value="" size="20">
# <p><input type="text" name="password" value="" size="20">

# еще пример:

# person = [
#     {"name": "Alex", "old": 18, "weight": 78.5},
#     {"name": "Nikol", "old": 29, "weight": 82.3},
#     {"name": "Ivan", "old": 33, "weigth": 94.0}
# ]
# и далее:
#что мы тут делаем: 1. формируем макро определение, которое называется list_users, и мы ему передаем некий список list_of_user, далее мы внутри этого макроопределения формируем список <ul> ... </ul> и внутри этого тега будут формироваться такие теги <li> при помощи цикла for по этому списку for i in list_of_user, и теги эти будут возвращать нам имена, а в конце мы вызываем макроопределение с параметром юзерс list_users(users), а юзерс соответственно берется из  msg = tm.render(users=person) где мы получается присваиваем значяение юзерс наше значение персон.
# html = '''
# {%- macro list_users(list_of_user) -%}
# <ul>
# {% for i in list_of_user -%}
#     <li>{{i.name}}
# {%- endfor %}
# </ul>
# {%- endmacro %}

# {{list_users(users)}}
# '''
# tm = Template(html)
# msg = tm.render(users=person)
# print(msg)

# <ul>
# <li>Alex<li>Nikol<li>Ivan
# </ul>

############################
# еще пример - создадим у макроса вложенный макрос:

# person = [
#     {"name": "Alex", "old": 18, "weight": 78.5},
#     {"name": "Nikol", "old": 29, "weight": 82.3},
#     {"name": "Ivan", "old": 33, "weigth": 94.0}
# ]
# чтобы создать вложенный макрос нам необходимо создать метод caller(i) к нашемуциклу и спомощью этого метода вызыввается наш вложенный макрос call(user) list_users(users)
# далее когда происходит вызовcall(user) list_users(users) то макрос call создает связь с list_users в макросе macro 
# html = '''
# {%- macro list_users(list_of_user) -%}
# <ul>
# {% for i in list_of_user -%}
#     <li>{{i.name}} {{caller(i)}} 
# {%- endfor %}
# </ul>
# {%- endmacro %}

# {% call(user) list_users(users) %}
#     <ul>
#     <li>age: {{user.old}}
#     <li>weight: {{user.weight}}
#     </ul>
# {% endcall -%}

# '''
# tm = Template(html)
# msg = tm.render(users=person)
# print(msg)

# <ul>
# <li>Alex 
#     <ul>
#     <li>age: 18
#     <li>weight: 78.5
#     </ul>
# <li>Nikol 
#     <ul>
#     <li>age: 29
#     <li>weight: 82.3
#     </ul>
# <li>Ivan 
#     <ul>
#     <li>age: 33
#     <li>weight: 
#     </ul>

# </ul>

##############################

"""
Загрузчик шаблонов:

FileSystemLoader - ...

PackageLoader - для загрузки шаблонов из пакета(то етсь когда мы формируем некий модуль в виде пакета и из этого пакета берем те или иные шаблоны, то для этого стоит использовать имеено этот загрузчик)

DictLoader - для загрузки шаблонов из словаря

FunctionLoader - для загнрузки на основе функций

ModuleLoader - загрузчик для скомпилированных шаблонов

ChoiceLoader - загрузчик, содержащий список других загрузчиков (если один не сработает, выбирается следующий)

PrefixLoader - загрузчик, использующий словарь для построения подкаталогов

FileSystemLoader - берет  шаблон непосредственно из файловой системы нашего устройства

"""
# рассмотри пример:

# создадим список для работы с шаблоном
# person = [
#     {"name": "Alex", "old": 18, "weight": 78.5},
#     {"name": "Nikol", "old": 29, "weight": 82.3},
#     {"name": "Ivan", "old": 33, "weigth": 94.0}
# ]
# чтобы загрузить шаблон нам нужно воспользоваться загрузчиком файловым, для этого мы воспользуемся загнрузчиком FileSystemLoader и пропишем маршрут из какой папки необходимо загрузить файл
# file_loader = FileSystemLoader('template') # пишется папка расположения файла(в данном случае файл лежит в папке проекта template) template - папка обязательно должна называтсья так!
# затем создаем класс окружения Environment - это такой специальный класс, через который происходит работы с API данного пакета и в качестве одного из параметров мы указываем вот такой параметр loader и ему присваиваем ссылку на наш загрузчик file_loader, то есть этот загрузчик будет брать все наши шаблоны вот из этого подкаталога 'template'
# env = Environment(loader=file_loader)

# далее мы должны получить наш шаблон 'main.htm' и воспользуемся методом get_template - как этот метод работает: он формирует экземпляр класса #Template на основе содержимого нашего файла 'main.htm', то есть переменная tm будет ссылаться на экземпляр класса #Template и уже у экземпляра этого класса мы будем вызывать метод render
# tm = env.get_template('main.htm') # пишется название файла

# здесь мы будем получать рендер для обработки нашего шаблона и получения на выходе текстовой строки уже преобразованного шаблона
# msg = tm.render(users=person)
# print(msg)


#####################
# рассмотри еще пример на функциях:

# person = [
#     {"name": "Alex", "old": 18, "weight": 78.5},
#     {"name": "Nikol", "old": 29, "weight": 82.3},
#     {"name": "Ivan", "old": 33, "weigth": 94.0}
# ]
# # создаем функцию и передаем ей шаблон, который хотим загрузить path, и создадим условия: если этот шаблон принимаент индекс, то мы вернем такую-то строку
# def loadTpl(path):
#     if path == 'index':
#         return '''Имя {{u.name}}, возраст {{u.old}}'''
#     else:
#         return '''Данные: {{u}}'''
# # используем наш загрузчик функций  FunctionLoader
# file_loader = FunctionLoader(loadTpl) # передаем ссылку на функцию
# env = Environment(loader=file_loader)
# tm = env.get_template('index')
# msg = tm.render(u=person[0])
# print(msg)

# Имя Alex, возраст 18

#########################

# Исходный шаблон нашей хтмл страницы мы можем разделить на 3 части: Headers + Content + Footer - и каждую часть мы можем поместить в свой отдельный файл и потом их соединить при помощи конструкции include

# создадим 3 отдельных файла, которые по итогу будут автоматически собираться в 1 страницу при помощи include, и расположим конструктор инклуд в файле контент, так как он посередине и будет собирать снизу и сверху хеадерс и футер

# если мы не хотим подключать какой-то фалй, то мы прописываем команду ignore missing, например у нас есть файл header2.htm то команда ьудет такой в контенте: {% include 'header2.htm' ignore missing %}

# person = [
#     {"name": "Alex", "old": 18, "weight": 78.5},
#     {"name": "Nikol", "old": 29, "weight": 82.3},
#     {"name": "Ivan", "old": 33, "weigth": 94.0}
# ]
# file_loader = FileSystemLoader('template')
# env = Environment(loader=file_loader)
# tm = env.get_template('content.htm') #собственно обращаемся к файлу при помощи которого будем делать контруктор, так как в этом файле содержится наш инклуд

# msg = tm.render(domain='https://www.iqair.com/kyrgyzstan/bishkek', title='Про сраный воздух')

# мы создадли ссылки внутри хтмл хеадерс, чтобы нам былдо удобно менять ссылки и заголовки

# print(msg)

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Про программирование</title>
# </head>
# <body>
# <p>Содержание страницы
# </body>
# </html>


# <!-- также мы можем создавать и другие страницы( несколько страниц) для объединения, не только хеадерс и футер, для этого необходимо создать список из страниц которые надо добавить в конструктор, но также важдно тогда прописать игнор миссинг, чтобы если из нашего списка не будет найден какой-то шаблон, то у нас не возникло ошибки {% include ['page1.html', 'header.htm', 'page2.html'] ignore vissing %} --> 

# также мы можем использовать конструкцию импорт import: для этого создадим файл диалогс  и там пропишем необходимые нам команды, а также для импорта нам необходимо добавить непосредственно сам импорт в файле контент {% from 'dialogs.htm' import dialog_1 as dlg %} и строчку {{ dlg('Внимание-внимание', 'Это тестовый пиздец')}}

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <base href="https://www.iqair.com/kyrgyzstan/bishkek">
#     <title>Про сраный воздух</title>
# </head>
# <body>
# <p>Содержание страницы
# <div class="dialog">
#     <p> class="title">Внимание-внимание </p>
#     <p> class="message">Это тестовый пиздец </p>
#     <p><input type="button" value="Close"> </p>
# </div>
# </body>
# </html>

############################

"""
НАСЛЕДОВАНИЕ

{% block <имя блока> %} 
<содержимое блока>
{% endblock %}

данные блоки используются для расширения базового шаблона нашей страницы, и само расширение делается так: создадим файл в нашем случае about.htm, в который поместим именованные блоки расширения, который будет расширять базовый шаблон ex_main.htm, далее {% extends 'ex_main.htm' %} мы обращаемся через нашу конструкцию через конструктор extends к тому файлу, который нам необходимо дополнить (мы можем прописать и маршрут этого файла, то есть наш необходимый файл лежит в другой папке, то мы тут в кавычках пишем маршут до данного файла включая название самого файла (можно это проверить на примере about2.html), но этот файл должен находится в обрасти папкок после папки template - то есть мы можем создать папки внутри папки template и от туда уже писать маршрут), далее {% block title%} мы говорим что во в этом именованном блоке title нам необходимо дополнить его информацией, далее {% block content %} в конкретном блоке мы дополняем необходимой информацией


{{ self.title() }} - с помощью такой конструкции мы можем обращаться к блоку( к любому блоку, но в данном случае блоку title, чтобы на мне дублировать информацию, если нам необходимпо прописать одно и тоже скажем внутри шаблона)


{{ super() }} - с помощью такой конструкции мы можем подсвтавить в блок (в тот блок, в который мы подставим, в нашем случае это блок content) 


также мы можем создавать вдложенные блоки в блоках (посмотрим на примере вложенного блока в нашем шаблоне default2):
{% block content %}
Блок контента и текст который мы можем пердать при помощи функции super() которую мы вызвали в about2.htm
        {% block table_contents %}
        <ul>
        {% for li in list_table -%}
        <li>{{li}}</li>
        {% endfor -%}
        </ul>
        {% endblock table_contents %}
{% endblock content %}


"""

# обратимся к файлу ex_main: в этом файле мы создадим в поле title именованный блок {% block title %} {$ endblock %} с именем title и также создадим такой же именованный блок {% block content %} {% endblock %} с именем content

# используем стандартный загрузчик FileSystemLoader и говорим в какой папке нам необходимо искать наш файл template что все шаблоны лежат в этом каталоге

# file_loader = FileSystemLoader('template')

# далее создаем вспомагательный объект чреез класс Environment при помощи параметра loader загрузчик

# env = Environment(loader=file_loader)

# затем мы получаем этот шаблон через экземпляр класса

# tm = env.get_template('about.htm')

# затем вызываем у этого шаблона метод редер для его обработки и получения непосредственного представления

# output = tm.render()
# print(output)

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title> Дополним информацию о сайте </title>
# </head>
# <body>  
# <h1>О сайте</h1>    
# <p>Это просто ппц как круто выглядит сайт</p>
# </body>
# </html>

####################
# еще пример с about2

subs = ["математика", "Физика", "Информатика", "Русский"]
file_loader = FileSystemLoader('template')
env = Environment(loader=file_loader)
tm = env.get_template('about2.htm')
output = tm.render(list_table=subs)
print(output)

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title> Дополним информацию о сайте </title>
# </head>
# <body>
#         <ul>
#         <li><p class="item">математика</p></li>
#         <li><p class="item">Физика</p></li>
#         <li><p class="item">Информатика</p></li>
#         <li><p class="item">Русский</p></li>
#         </ul>
# <h1> Дополним информацию о сайте </h1>  
# <h2>О сайте</h2>    
# <p>Это просто ппц как круто выглядит сайт</p>
# </body>
# </html>

############################

"""
Вложенное наследование шаблонов
Например у нас есть 3 шаблона: 
base.htm
child1.htm
child2.htm

файл base.htm - такой же как и ex_main.htm:
файл child1.htm: {% extends 'base.htm' %}...
файл child2.htm: {% extends 'child1.htm' %}...

шаблоны поддерживают вложенные наследования, то есть формирование итогового дочернего шаблона по цепочке от базового до корневого. Каждый файл по цепочке будет расширять предыдущий, такием образом главный корневой файл будет расширен за счет наследования
"""