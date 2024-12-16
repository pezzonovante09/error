**admin.py**
-
admin.py - файл, которые отвечает за обнаружение ваших моделей в админской панели
**пример простого отображения моделей**
-

from django.contrib import admin
from .models import Product, Category

admin.site.register(Product)
admin.site.register(Category)

**Если вы хотите улучшить отображение**
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'quantity', 'category'] # это то, что будет отображаться при листинге объектов
    list_filter = ['price'] # поля, по которым можно будет проходить фильтром
    search_fields = ['title'] # поле, по которому мы можем провести поиск по нашим объектам

admin.site.register(Product, ProductAdmin)

**Настройка отображения объектов в админке**
1) Если у вас django автоматически неправильно подставляет окончание (Например Categorys вместо Categories) то вы можете настроить это отображение путем создания class Meta: внутри класса модели (Например модель category), и внутри определить verbose_name, verbose_name_plural

2) Чтобы исправить отображение (в случае с моделькой Product)"Product object(1)", и отображать нужные данные, можно: 1) переопределить метод __str__, 2) определить list_display