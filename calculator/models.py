import uuid

from django.db import models
from djmoney.models.fields import MoneyField


class InsuranceCalculator(models.Model):
    TYPE_CHOICES = (
        ('third', 'Third Party'),
        ('compressive', 'Compressive'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, null=False, blank=False)
    insurance_price = MoneyField(max_digits=10, decimal_places=2, default_currency='GHS')

    def save(self, *args, **kwargs):
        if self.type == 'compressive':
            self.insurance_price = 1000
        elif self.type == 'third':
            self.insurance_price = 3000
        super(InsuranceCalculator, self).save(*args, **kwargs)
