from django.urls import path, include

from .views import (
    RecipeListAPIView,
    RecipeCreateAPIView,
    RecipeDetailAPIView,
    RecipeUpdateAPIView,
    RecipeDeleteAPIView,
    IngredientListAPIView,
    IngredientCreateAPIView,
    IngredientDetailAPIView,
    IngredientUpdateAPIView,
    IngredientDeleteAPIView,
    CommentListAPIView,
    CommentDetailAPIView,
    CommentUpdateAPIView,
    CommentDeleteAPIView,
)


urlpatterns = [
    path('', RecipeListAPIView.as_view(), name='recipe-api-list'),
    path('<int:pk>', RecipeDetailAPIView.as_view(), name='recipe-api-detail'),
    path('create', RecipeCreateAPIView.as_view(), name='recipe-api-create'),

    path('<int:pk>/update', RecipeUpdateAPIView.as_view(), name='recipe-api-update'),
    path('<int:pk>/delete', RecipeDeleteAPIView.as_view(), name='recipe-api-delete'),
    path('ingredients',  IngredientListAPIView.as_view(), name='ingredients-api-list'),
    path('ingredients/<int:pk>',  IngredientDetailAPIView.as_view(), name='ingredients-api-detail'),
    path('ingredients/<int:pk>/update',  IngredientUpdateAPIView.as_view(), name='ingredients-api-update'),
    path('ingredients/<int:pk>/delete',  IngredientDeleteAPIView.as_view(), name='ingredients-api-delete'),
    path('comments',   CommentListAPIView.as_view(), name='comments-api-list'),
    path('comments/<int:pk>',   CommentDetailAPIView.as_view(), name='comments-api-detail'),
    path('comments/<int:pk>/update',   CommentUpdateAPIView.as_view(), name='comments-api-update'),
    path('comments/<int:pk>/delete',   CommentDeleteAPIView.as_view(), name='comments-api-delete'),

]
