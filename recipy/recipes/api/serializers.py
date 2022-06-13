from rest_framework.serializers import ModelSerializer

from recipes.models import Recipe


class RecipeSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'description',
            'instructions',
            'ingredients'
        ]
