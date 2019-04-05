import feedparser
from decimal import Decimal

from .models import Currency, ExchangeRate


def get_exchange_rates_and_save(currencies):
    for currency in currencies:
        f = feedparser.parse(currency.url)
        ExchangeRate.objects.create(currency=currency, rate=Decimal(f['entries'][0]['cb_exchangerate'].split()[0]))
