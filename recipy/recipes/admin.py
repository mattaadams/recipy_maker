from django.contrib import admin
# Register your models here.
from .models import Recipe, Ingredient, Comment


admin.site.register(Comment)


class RecipeIngredientInline(admin.StackedInline):
    model = Ingredient
    fields = ['name', 'quantity', 'unit']


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    readonly_fields = ['date_posted']


admin.site.register(Recipe, RecipeAdmin)
