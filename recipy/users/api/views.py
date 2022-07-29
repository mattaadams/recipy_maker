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

)
from recipes.api.serializers import RecipeListSerializer


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


class UserFavoriteListAPIView(ListAPIView):
    serializer_class = RecipeListSerializer

    @swagger_auto_schema(tags=['Users'])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        return Recipe.objects.filter(favorites=self.kwargs.get('pk'))


class UserRecipeListAPIView(ListAPIView):
    serializer_class = RecipeListSerializer

    @ swagger_auto_schema(tags=['Users'])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    #getattr(self, 'swagger_fake_view', False)

    def get_queryset(self):
        return Recipe.objects.filter(author=self.kwargs.get('pk'))

# User Recommended Recipe List View
