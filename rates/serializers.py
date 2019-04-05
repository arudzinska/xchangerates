from rest_framework import serializers

from .models import Currency, ExchangeRate


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = '__all__'


class ExchangeRateSerializer(serializers.ModelSerializer):

    currency = serializers.SlugRelatedField(
        slug_field='iso_code',
        read_only=True
    )

    class Meta:
        model = ExchangeRate
        exclude = ('id',)
