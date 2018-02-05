from django.db import models
from django.utils.text import slugify
from djmoney.models.fields import MoneyField

class Risk(models.Model):
    name = models.CharField(max_length=140)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Risk, self).save(*args, **kwargs)



class ThirdPartyTarif(models.Model):
    risk = models.ForeignKey(Risk)
    total_basic_premium = MoneyField(max_digits=10, decimal_places=2, default_currency='GHS')
    def __str__(self):
        return "ThirdParty {} of {}".format(self.risk.name, self.total_basic_premium)


class ComprehensiveTarif(models.Model):
    risk = models.ForeignKey(Risk)
    total_basic_premium = MoneyField(max_digits=10, decimal_places=2, default_currency='GHS')

    def __str__(self):
        return "Comprehensive {} of {}".format(self.risk.name, self.total_basic_premium)
