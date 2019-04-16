from django.db import models
from account.models import Client


class Dish(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='dish_images')
    ingredients = models.ManyToManyField(
        'Ingredient',
        related_name='dishes',
        through='RecipeRecord'
    )

    def __str__(self):
        return self.name

    @property
    def price(self):
        total_price = 0
        for record in self.recipe_records.all():
            total_price += record.ingredient.price * record.amount
        return total_price


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    measure = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=9, decimal_places=4, default=0)

    def __str__(self):
        return f'{self.name}, {self.measure}'


class RecipeRecord(models.Model):
    dish = models.ForeignKey('Dish', related_name='recipe_records', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', related_name='recipe_records', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = (('dish', 'ingredient'),)
        ordering = ('dish__name', 'ingredient__name')

    def __str__(self):
        return f'{self.dish} - {self.ingredient}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.customer}: {self.dish.name}'



