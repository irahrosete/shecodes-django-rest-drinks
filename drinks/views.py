from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerialiser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request):
  if request.method == 'GET':
    drinks = Drink.objects.all()
    serializer = DrinkSerialiser(drinks, many=True)
    return JsonResponse({'drinks': serializer.data})

  if request.method == 'POST':
    serializer = DrinkSerialiser(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)