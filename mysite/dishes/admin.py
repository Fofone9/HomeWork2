from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from .models import Dish, Ingredient, Composition, Cook
# Register your models here.
admin.site.register(Dish)
admin.site.register(Ingredient)
admin.site.register(Composition)
admin.site.register(Cook)
TokenAdmin.raw_id_fields = ['user']
