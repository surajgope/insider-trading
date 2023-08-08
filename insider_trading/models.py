
from django.db import models


class InsiderTrading(models.Model):
    fill_date       = models.DateField(blank=True, null=True)
    time            = models.DateTimeField(blank=True, null=True)
    ticker          = models.TextField(blank=True, null=True)
    company         = models.TextField(blank=True, null=True)
    insider_name    = models.TextField(blank=True, null=True)
    title           = models.TextField(blank=True, null=True)
    trade_type      = models.TextField(blank=True, null=True)
    price           = models.FloatField(blank=True, null=True)
    qty             = models.FloatField(blank=True, null=True)
    value           = models.FloatField(blank=True, null=True)
    form4_url       = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'insider_trading'