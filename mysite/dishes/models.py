from django.db import models

# Create your models here.
class Cook(models.Model):
    name = models.CharField(max_length = 40)
    surname = models.CharField(max_length = 40)
    birth_year = models.DateField()
    dishes = models.ManyToManyField(
        'Dish',
        blank=True
    )
    salary = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(str(self.surname),str(self.name))


class Dish(models.Model):
    name = models.TextField(max_length=50)
    author = models.ForeignKey('Cook', on_delete=models.CASCADE )
    DISH_TYPES = (
        ('Bakery', 'Выпечка'),
        ('Breakfast', 'Завтрак'),
        ('Dessert', 'Десерт'),
        ('On coals', 'На углях'),
        ('Beverages', 'Напитки'),
        ('Soups', 'Супы'),
        ('Cold snacks','Холодные закуски'),
        ('Hot dishes', 'Горячие блюда'),
        ('Side dishes', 'Гарниры'),
    )
    dish_type = models.CharField(max_length=40, choices=DISH_TYPES)
    ingredients = models.ManyToManyField(
        'Ingredient',
        through='Composition',
        through_fields=('dish','ingredient'),
    )

    def __str__(self):
        return str(self.name)

class Ingredient(models.Model):
    name = models.CharField(max_length = 40)
    calorie_content = models.IntegerField()
    cost = models.SmallIntegerField()

    def __str__(self):
        return str(self.name)

class Composition(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    count = models.SmallIntegerField()

    