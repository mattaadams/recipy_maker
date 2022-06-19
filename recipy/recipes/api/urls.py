from django.urls import path, include

from .views import (
    RecipeListAPIView,
    IngredientListAPIView,
    CommentListAPIView
)


urlpatterns = [
    path('', RecipeListAPIView.as_view(), name='recipe-api-list'),
    path('ingredients',  IngredientListAPIView.as_view(), name='ingredients-api-list'),
    path('comments',   CommentListAPIView.as_view(), name='comments-api-list'),
]
