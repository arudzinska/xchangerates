from decimal import Decimal

from django.db import models


class Currency(models.Model):
    name = models.CharField("Name", max_length=50, null=False, blank=False)
    iso_code = models.CharField("ISO code", max_length=5, null=False, blank=False, unique=True)
    url = models.URLField("URL", null=False, blank=False)

    def __str__(self):
        return "{} ({})".format(self.name, self.iso_code)


class ExchangeRate(models.Model):
    currency = models.ForeignKey(Currency, verbose_name="Currency", null=False, blank=False, on_delete=models.CASCADE)
    rate = models.DecimalField("Exchange rate", max_digits=12, decimal_places=3, default=Decimal(0.0), null=False,
                               blank=False)
    created = models.DateTimeField("Created", null=False, auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.currency, self.rate)
