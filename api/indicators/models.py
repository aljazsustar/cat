from django.db import models


class Indicator(models.Model):
    symbol = models.CharField(max_length=50)
    company_name = models.CharField(max_length=255)
    type = models.CharField(max_length=100, null=True, blank=True)
