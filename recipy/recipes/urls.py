from django.urls import path
from .views import (RecipeListView,
                    RecipeDetailView,
                    RecipeCreateView,
                    RecipeUpdateView,
                    RecipeDeleteView,
                    UserRecipeListView)
from recipes import views as recipe_views

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-home'),
    path('user/<username>', UserRecipeListView.as_view(), name='user-recipe'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/new/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/update', RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipe/<int:pk>/delete', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('fav/<int:id>/', recipe_views.favorite_add, name='favorite-add')
]
