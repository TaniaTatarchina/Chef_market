from django.contrib import admin
from chef_market_app.models import Dish, Ingredient, RecipeRecord, Order


class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'measure', 'price']
    list_filter = ('name',)
    ordering = ('name',)


class DishAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    ordering = ('name',)


class RecipeRecordAdmin(admin.ModelAdmin):
    list_filter = ('dish',)


admin.site.register(Dish, DishAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeRecord, RecipeRecordAdmin)
admin.site.register(Order)

