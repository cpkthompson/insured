from django.contrib import admin

from calculator.models import InsuranceCalculator


class InsuranceCalculatorAdmin(admin.ModelAdmin):
    pass

admin.site.register(InsuranceCalculator, InsuranceCalculatorAdmin)
