#from django.utils.datastructures import MultiValueDictKeyError


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Currency, ExchangeRate
from .services import get_exchange_rates_and_save
from .serializers import CurrencySerializer, ExchangeRateSerializer


class ExchangeRateAPIView(APIView):
    """
    ?
    """

    def get(self, request):

        get_exchange_rates_and_save(currencies=[*Currency.objects.all()])
        exchangerate_serializer = ExchangeRateSerializer(ExchangeRate.objects.all(), many=True)

        return Response(exchangerate_serializer.data)
