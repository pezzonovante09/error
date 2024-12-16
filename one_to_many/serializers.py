from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields ='__all__' # ['id', 'title', 'price']

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Цена не может быть отрицательной')
        return value

    # есть 2 метода для валидации в сериализаторе, validate, valitdate_<field>, validate(self, attrs) -
    # attr - словарь с данными из запроса, сам метод проверяет все данные, validate_<field>(self, <field>) - 
    # валидирует какое то определенное поле, если валидация прошла, то нужно обязательно вернуть поле

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price']