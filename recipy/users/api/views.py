from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .pagination import UserPageNumberPagination
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
from recipes.models import Recipe, Comment

from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
    UserListSerializer,
    UserDetailSerializer,
    UserCommentListSerializer

)
from recipes.api.serializers import RecipeListSerializer


class UserCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    @swagger_auto_schema(tags=['Users'])
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    pagination_class = UserPageNumberPagination

    @swagger_auto_schema(operation_description="Return a list of users", tags=['Users'])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    @swagger_auto_schema(tags=['Users'])
    def post(self, request, *args, **kwargs):
        data = self.request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


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

    @swagger_auto_schema(tags=['Users'])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    #getattr(self, 'swagger_fake_view', False)

    def get_queryset(self):
        return Recipe.objects.filter(author=self.kwargs.get('pk'))


class UserCommentListAPIView(ListAPIView):
    serializer_class = UserCommentListSerializer

    @swagger_auto_schema(tags=['Users'])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    #getattr(self, 'swagger_fake_view', False)

    def get_queryset(self):
        return Comment.objects.filter(author=self.kwargs.get('pk'))
# User Recommended Recipe List View
