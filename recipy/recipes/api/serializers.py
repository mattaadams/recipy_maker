from rest_framework.serializers import ModelSerializer

from recipes.models import Recipe, Ingredient


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = [
            'name',
            'quantity',
            'unit',
        ]


class RecipeSerializer(ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:

        model = Recipe
        fields = [
            'title',
            'description',
            'ingredients',
            'instructions',
        ]
