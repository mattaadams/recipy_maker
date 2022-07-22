from django.urls import path, include
from .views import (RecipeListView,
                    RecipeDetailView,
                    FavoriteAddView,
                    RecipeCreateView,
                    RecipeUpdateView,
                    RecipeDeleteView,
                    UserRecipeListView)
from recipes import views as recipe_views

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-home'),
    path('user/<username>', UserRecipeListView.as_view(), name='user-recipe'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/<int:recipe_id>/comment/<int:pk>/edit', recipe_views.comment_edit_form, name='comment-edit'),
    path('recipe/new/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/update', RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipe/<int:pk>/delete', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('fav/<int:pk>/', FavoriteAddView.as_view(), name='favorite-add')
]
