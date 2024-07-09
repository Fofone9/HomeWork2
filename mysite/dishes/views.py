from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Dish, Cook, Ingredient
from .serializers import DishSerializer, CookSerializer, IngredientSerializer
# Create your views here.

@csrf_exempt
def cook_list(request):
    if request.method == 'GET':
        cooks = Cook.objects.all()
        serializer = CookSerializer(cooks, many = True)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CookSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
    
@csrf_exempt
def cook_detail(request, pk):
    try:
        cook = Cook.objects.get(pk = pk)
    except Cook.DoesNotExist:
        return HttpResponse(status = 404)
    if request.method == "GET":
        serializer = CookSerializer(cook)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = CookSerializer(cook, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)
    elif request.method =="DELETE":
        cook.delete()
        return HttpResponse(status = 204)
    
