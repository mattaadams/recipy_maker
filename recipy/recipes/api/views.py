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
    RecipeCreateUpdateSerializer,
    RecipeDetailSerializer,
    IngredientListSerializer,
    IngredientCreateUpdateSerializer,
    IngredientDetailSerializer,
    CommentListSerializer,
    CommentCreateUpdateSerializer,
    CommentDetailSerializer
)


class RecipeListAPIView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer


class RecipeCreateAPIView(CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateUpdateSerializer


class RecipeDetailAPIView(RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer


class RecipeUpdateAPIView(UpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateUpdateSerializer


class RecipeDeleteAPIView(DestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer


class IngredientListAPIView(ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientListSerializer


class IngredientCreateAPIView(CreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientCreateUpdateSerializer


class IngredientDetailAPIView(RetrieveAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientDetailSerializer


class IngredientUpdateAPIView(UpdateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientCreateUpdateSerializer


class IngredientDeleteAPIView(DestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientDetailSerializer


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateUpdateSerializer


class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer


class CommentUpdateAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateUpdateSerializer


class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
