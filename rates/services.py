import feedparser
from decimal import Decimal
from datetime import datetime

from .models import ExchangeRate


def get_exchange_rates_and_save(currencies):

    for currency in currencies:
        if no_rate_from_today(currency):
            f = feedparser.parse(currency.url)
            ExchangeRate.objects.create(currency=currency, rate=Decimal(f['entries'][0]['cb_exchangerate'].split()[0]))


def no_rate_from_today(currency):

    if not ExchangeRate.objects.filter(currency=currency, created__date=datetime.now().date()):
        return True

    return False
