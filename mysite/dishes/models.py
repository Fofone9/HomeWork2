from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

        
class Cook(models.Model):
    name = models.CharField(max_length = 40)
    surname = models.CharField(max_length = 40)
    birth_year = models.DateField()
    salary = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(str(self.surname),str(self.name))


class Dish(models.Model):
    name = models.TextField(max_length=50)
    author = models.ForeignKey('Cook', on_delete=models.CASCADE )
    dish_type = models.CharField(max_length=40)
    ingredients = models.ManyToManyField('Ingredient')
    price = models.IntegerField()
    def __str__(self):
        return str(self.name)

class Ingredient(models.Model):
    name = models.CharField(max_length = 40)
    calorie_content = models.IntegerField()
    cost = models.SmallIntegerField()

    def __str__(self):
        return str(self.name)

# class Composition(models.Model):
#     dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
#     ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
#     count = models.SmallIntegerField()

    