from django.db import models
import uuid

from django.db import models
from djmoney.models.fields import MoneyField

from risk.models import ThirdPartyTarif, Risk


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


class Vehicle(models.Model):
    number_of_seats = models.IntegerField()
    USAGE_CHOICES = (
        ('private', 'Private'),
        ('commercial', 'Commercial'),
    )
    EXTRA_SEAT_CHOICES = (
        ('x1_and_x4', 'X1 and X4'),
        ('hiring', 'Hiring and Other Commercial Vehicles'),
    )
    VEHICLE_AGE_CHOICES = {
        ('one', '1 to 5 years'),
        ('five', '5 to 10 years'),
        ('above', 'Above 10 years'),
    }
    CUBIC_CAPACITY_CHOICES = {
        ('up_to_1600', 'Up to 1600'),
        ('1600_to_2000', '1600 to 2000'),
        ('Above_2000', 'Above 2000'),
    }
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    risk = models.ForeignKey(Risk)
    extra_seating = models.CharField(max_length=50, choices=EXTRA_SEAT_CHOICES, null=False, blank=False)
    cubic_capacity = models.CharField(max_length=50, choices=CUBIC_CAPACITY_CHOICES, null=False, blank=False)
    usage = models.CharField(max_length=50, choices=USAGE_CHOICES, null=False, blank=False)
    age = models.CharField(max_length=50, choices=VEHICLE_AGE_CHOICES, null=False, blank=False)


class InsurancePayout(models.Model):
    ADDITIONAL_PERIL_CHOICES = (
        ('motor', 'Motor Cycles & Ambulances'),
        ('others', 'All Others'),
    )
    TYPE_CHOICES = (
        ('third', 'Third Party'),
        ('compressive', 'Compressive'),
    )
    AGE_RANGE_CHOICES = (
        ('below_18', 'Below 18'),
        ('between_18_and_21', 'Between 18 and 21'),
        ('above_21', 'Above 21'),
    )
    FLEET_REBATES_CHOICES = (
        ('up_to_4', 'Up to 4'),
        ('5_to_10', '5 to 10'),
        ('11_to_20', '11 to 20'),
        ('above_20', 'Above 20'),
    )
    ecowas_peril = models.BooleanField(default=False)
    vehicle = models.ForeignKey(Vehicle)
    additional_peril = models.CharField(max_length=50, choices=ADDITIONAL_PERIL_CHOICES, null=False, blank=False)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, null=False, blank=False)
    age_range = models.CharField(max_length=50, choices=AGE_RANGE_CHOICES, null=False, blank=False)
    fleet_rebates_discount = models.CharField(max_length=50, choices=FLEET_REBATES_CHOICES, null=False, blank=False)
    insurance_price = MoneyField(max_digits=10, decimal_places=2, default_currency='GHS')

    def save(self, *args, **kwargs):
        if self.type == 'compressive':

            self.insurance_price = 1000

        elif self.type == 'third':

            third_party_tarif = ThirdPartyTarif.objects.get(risk__slug=self.vehicle.risk.slug)
            tp_basic_premium = third_party_tarif.total_basic_premium
            initial = int
            if self.vehicle.age == 'one':
                _initial = tp_basic_premium
                intital = _initial


            elif self.vehicle.age == 'five':
                old_age_loading = 0.05
                _initial = tp_basic_premium + (tp_basic_premium * old_age_loading)
                intital = _initial

            elif self.vehicle.age == 'above':
                old_age_loading = 0.075
                _initial = tp_basic_premium + (tp_basic_premium * old_age_loading)
                intital = _initial

            # Calculations
            # if car has more than one seat 5 cedi per extra seat if private or 8 cedi if private
            extra_seat_loading = int
            if self.vehicle.number_of_seats > 5:
                if self.vehicle.usage == 'Private':
                    _extra_seat_loading = (self.vehicle.number_of_seats - 5) * 5
                    extra_seat_loading = _extra_seat_loading
                elif self.vehicle.usage == 'Commercial':
                    _extra_seat_loading = (self.vehicle.number_of_seats - 5) * 8
                    extra_seat_loading = _extra_seat_loading
            self.insurance_price = initial + extra_seat_loading

            # To be considered
            inexperienced_driver_loading = int
            extra_tppd_cover = int
            additional_peril = int
            ecowas_peril = int
            pa_benefits = int
            nic_nhis_nrsc_ecowas_bc = int

            self.insurance_price = 1000
        super(InsurancePayout, self).save(*args, **kwargs)
