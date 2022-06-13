from django.urls import path, include

from .views import (
    RecipeListAPIView
)


urlpatterns = [
    path('', RecipeListAPIView.as_view(), name='recipe-api-list')
]
