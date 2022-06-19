from rest_framework import serializers
from recipes.models import Recipe, Ingredient, Comment


class IngredientSerializer(serializers.ModelSerializer):
    recipe = serializers.CharField(read_only=True)

    class Meta:
        model = Ingredient
        fields = [
            'name',
            'quantity',
            'unit',
            'recipe'
        ]


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:

        model = Recipe
        fields = [
            'title',
            'description',
            'ingredients',
            'instructions',
            'date_posted'
        ]


class CommentSerializer(serializers.ModelSerializer):
    recipe = serializers.CharField(read_only=True)

    class Meta:

        model = Comment
        fields = [
            'name',
            'body',
            'date_posted',
            'recipe',
        ]
