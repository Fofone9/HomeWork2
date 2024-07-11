from django.shortcuts import render
from .models import Dish, Cook, Ingredient
from .serializers import DishSerializer, CookSerializer, IngredientSerializer
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class CookList(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, format = None):
        cooks = Cook.objects.all()
        serializer = CookSerializer(cooks, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CookDetail(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, pk):
        try:
            return Cook.objects.get(pk=pk)
        except Cook.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        cook = self.get_object(pk)
        serializer = CookSerializer(cook)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        cook = self.get_object(pk)
        serializer = CookSerializer(cook, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        cook = self.get_object(pk)
        cook.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

   
class DishList(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class DishDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    