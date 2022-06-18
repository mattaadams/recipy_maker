from django.urls import path, include

from .views import (
    RecipeListAPIView,
    IngredientListAPIView
)


urlpatterns = [
    path('', RecipeListAPIView.as_view(), name='recipe-api-list'),
]
