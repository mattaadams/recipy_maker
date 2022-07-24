from drf_yasg.utils import swagger_auto_schema

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
from recipes.models import Recipe

from .serializers import (
    UserCreateSerializer,
    UserListSerializer,
    UserDetailSerializer,
    UserFavoriteRecipeListSerializer

)


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    @swagger_auto_schema(tags=['Users'])
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    @swagger_auto_schema(operation_description="Return a list of users", tags=['Users'])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    @swagger_auto_schema(tags=['Users'])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# UNFINISHED

class UserFavoriteListAPIView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = UserFavoriteRecipeListSerializer

    @swagger_auto_schema(tags=['Users'])
    def get(self, request, *args, **kwargs):
        print(kwargs)
        return self.list(request, *args, **kwargs)

# User Created Recipe List View
# User Recommended Recipe List View
