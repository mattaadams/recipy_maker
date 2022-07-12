from django.urls import path, include
from .views import (
    UserListAPIView,
    UserDetailAPIView
)

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-api-list'),
    path('<int:pk>', UserDetailAPIView.as_view(), name='user-api-detail'),
]
