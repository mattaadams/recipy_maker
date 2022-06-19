from rest_framework.generics import ListAPIView
from recipes.models import Recipe, Ingredient, Comment
from .serializers import (
    RecipeSerializer,
    IngredientSerializer,
    CommentSerializer)


class RecipeListAPIView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class IngredientListAPIView(ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
