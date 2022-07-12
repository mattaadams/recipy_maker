from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

)
from django.contrib.auth.models import User
from .serializers import (
    UserListSerializer,
    UserDetailSerializer
)


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
