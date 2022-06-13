from rest_framework.generics import ListAPIView
from recipes.models import Recipe
from .serializers import RecipeSerializer


class RecipeListAPIView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
