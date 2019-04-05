from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Currency, ExchangeRate
from .services import update_exchange_rates
from .serializers import CurrencySerializer, ExchangeRateSerializer


class ExchangeRateAPIView(APIView):
    """
    Lists all newest exchange rates (one per each currency).
    """

    def get(self, request):

        update_exchange_rates(currencies=Currency.objects.all())
        exchangerate_serializer = \
            ExchangeRateSerializer(ExchangeRate.objects.filter(created__date=datetime.now().date()), many=True)

        return Response(exchangerate_serializer.data)
