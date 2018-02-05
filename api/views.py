from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import CalculatorSerializer
from calculator.models import InsuranceCalculator


@api_view(['GET', 'POST'])
def calculation(request, id=None, Format=None):
    if request.method == 'GET':
        calculation_object = InsuranceCalculator.objects.get(id=id)
        serializer = CalculatorSerializer(calculation_object, many=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CalculatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
