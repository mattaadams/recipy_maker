from rest_framework.generics import ListAPIView
from recipes.models import Recipe, Ingredient
from .serializers import RecipeSerializer, IngredientSerializer


class RecipeListAPIView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class IngredientListAPIView(ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
