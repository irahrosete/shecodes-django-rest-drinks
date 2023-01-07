from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerialiser

def drink_list(request):
  drinks = Drink.objects.all()
  serializer = DrinkSerialiser(drinks, many=True)
  return JsonResponse({'drinks': serializer.data})