from rest_framework import serializers

from .models import Currency, ExchangeRate


class Currency(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = '__all__'


class ExchangeRate(serializers.ModelSerializer):

    class Meta:
        model = ExchangeRate
        fields = '__all__'
