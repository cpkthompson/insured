from rest_framework import serializers
from rest_framework import permissions

from calculator.models import InsuranceCalculator


# class CalculatorSerializer(serializers.Serializer):
#     TYPE_CHOICES = (
#         ('third', 'Third Party'),
#         ('compressive', 'Compressive'),
#     )
#     id = serializers.UUIDField(read_only=True)
#     type = serializers.ChoiceField(required=True, allow_blank=False, choices=TYPE_CHOICES)
#     insurance_price = serializers.DecimalField(decimal_places=2, read_only=True, max_digits=10)
#
#     def create(self, validated_data):
#         return InsuranceCalculator.objects.create(**validated_data)
class CalculatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = InsuranceCalculator
        fields = ('id', 'type', 'insurance_price')
