from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from recipes.models import Recipe, Ingredient, Comment
from .serializers import (
    RecipeListSerializer,
    RecipeCreateSerializer,
    RecipeDetailSerializer,
    IngredientListSerializer,
    IngredientCreateSerializer,
    IngredientDetailSerializer,
    CommentListSerializer,
    CommentDetailSerializer
)


class RecipeListAPIView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer


class RecipeCreateAPIView(CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateSerializer


class RecipeDetailAPIView(RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer


class RecipeUpdateAPIView(UpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer


class RecipeDeleteAPIView(DestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer


class IngredientListAPIView(ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientListSerializer


class IngredientCreateAPIView(CreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientCreateSerializer


class IngredientDetailAPIView(RetrieveAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientDetailSerializer


class IngredientUpdateAPIView(UpdateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientDetailSerializer


class IngredientDeleteAPIView(DestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientDetailSerializer


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer


class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer


class CommentUpdateAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer


class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
