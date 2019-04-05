
from django.conf.urls import url

from .views import ExchangeRateAPIView


urlpatterns = [
    url(r'^exchangerate$', ExchangeRateAPIView.as_view(), name="exchangerate"),
]
