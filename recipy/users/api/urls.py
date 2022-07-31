from django.urls import path, include
from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
    UserListAPIView,
    UserDetailAPIView,
    UserFavoriteListAPIView,
    UserRecipeListAPIView,
    UserCommentListAPIView


)

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='user-api-create'),
    path('login/', UserLoginAPIView.as_view(), name='user-api-login'),
    path('', UserListAPIView.as_view(), name='user-api-list'),
    path('<int:pk>', UserDetailAPIView.as_view(), name='user-api-detail'),
    path('<int:pk>/favorites', UserFavoriteListAPIView.as_view(), name='user-api-favorites'),
    path('<int:pk>/recipes', UserRecipeListAPIView.as_view(), name='user-api-recipes'),
    path('<int:pk>/comments', UserCommentListAPIView.as_view(), name='user-api-comments'),


]
