from django.urls import path, include
from .views import (
    UserCreateAPIView,
    UserListAPIView,
    UserDetailAPIView,
    UserFavoriteListAPIView

)

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='user-api-create'),
    path('', UserListAPIView.as_view(), name='user-api-list'),
    path('<int:pk>', UserDetailAPIView.as_view(), name='user-api-detail'),
    path('<int:pk>/favorites', UserFavoriteListAPIView.as_view(), name='user-api-favorites'),


]
