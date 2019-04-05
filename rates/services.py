import feedparser
from decimal import Decimal
from datetime import datetime

from .models import ExchangeRate


def update_exchange_rates(currencies):
    """
    Retrieves newest exchange rates from European Central Bank using an RSS feed reader for the chosen currencies if
    there is no entry existing yet for today's day in the database.

    :param currencies: iterable
    :return: None
    """

    for currency in currencies:
        if no_rate_from_today(currency):
            f = feedparser.parse(currency.url)
            ExchangeRate.objects.create(currency=currency, rate=Decimal(f['entries'][0]['cb_exchangerate'].split()[0]))


def no_rate_from_today(currency):
    """
    Checks if there is already an exchange rate for the given currency and today's day existing in the database.

    :param currency: <class 'rates.models.Currency'>
    :return: <class 'bool'>
    """

    return True if not ExchangeRate.objects.filter(currency=currency, created__date=datetime.now().date()) else False
