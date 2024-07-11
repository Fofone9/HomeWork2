from .models import Dish, Ingredient, Cook
from rest_framework import serializers

class CookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length = 40)
    surname = serializers.CharField(max_length = 40)
    birth_year = serializers.DateField()
    salary = serializers.IntegerField()

    def create(self, validated_data):
        return Cook.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.birth_year = validated_data.get('birth_year', instance.birth_year)
        instance.salary = validated_data.get('salaty', instance.salary)
        instance.save()
        return instance
    

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id','name', 'author', 'dish_type', 'ingredients']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'calorie_content', 'cost']