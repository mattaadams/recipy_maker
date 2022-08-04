from drf_yasg.utils import swagger_auto_schema
from django.db.models import Q

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView
)

from .pagination import (
    RecipePageNumberPagination,
    IngredientPageNumberPagination
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from .permissions import (
    IsOwnerOrReadOnly,
    IsParentOwnerOrReadOnly,
)
from recipes.models import Recipe, Ingredient, Comment
from .serializers import (
    RecipeListSerializer,
    RecipeCreateUpdateSerializer,
    RecipeDetailSerializer,
    RecipeFavoriteSerializer,
    IngredientListSerializer,
    IngredientDetailSerializer,
    CommentListSerializer,
    CommentCreateUpdateSerializer,
    CommentDetailSerializer
)


class RecipeListAPIView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'author__username', 'description', 'instructions']
    pagination_class = RecipePageNumberPagination

    @swagger_auto_schema(tags=['Recipes'])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def get_queryset(self):
    #     queryset_list = Recipe.objects.all()
    #     query = self.request.GET.get("q")
    #     if query:
    #         queryset_list = queryset_list.filter(
    #             Q(title__icontains=query) |
    #             Q(description__icontains=query) |
    #             Q(instructions__icontains=query) |
    #             Q(author__username__icontains=query)
    #         ).distinct()
    #     return queryset_list


class RecipeCreateAPIView(CreateAPIView):

    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['Recipes'])
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RecipeDetailAPIView(RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer

    @swagger_auto_schema(tags=['Recipes'])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class RecipeUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    @swagger_auto_schema(tags=['Recipes'], auto_schema=None)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Recipes'])
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Recipes'])
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class RecipeDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

    @swagger_auto_schema(tags=['Recipes'])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Recipes'], auto_schema=None)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class RecipeFavoriteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['Recipes'])
    def post(self, request, *args, **kwargs):
        data = self.request.data
        recipe = Recipe.objects.get(pk=self.kwargs.get('pk'))
        serializer = RecipeFavoriteSerializer(data=data)  # No data is actually being passed...
        if recipe.favorites.filter(id=self.request.user.id).exists():
            recipe.favorites.remove(self.request.user)
            message = f"Recipe {recipe.id} REMOVED to favorites"
        else:
            recipe.favorites.add(self.request.user)
            message = f"Recipe {recipe.id} ADDED to favorites"

        if serializer.is_valid(raise_exception=True):
            return Response(message, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class IngredientListAPIView(ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['recipe__author__username', 'name']
    pagination_class = IngredientPageNumberPagination

    @swagger_auto_schema(tags=['Ingredients'])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class IngredientDetailAPIView(RetrieveAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientDetailSerializer

    def get_object(self):
        obj = super().get_object()
        return obj

    @swagger_auto_schema(tags=['Ingredients'])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class RecipeCommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer

    @swagger_auto_schema(tags=['Recipes'])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        return Comment.objects.filter(recipe=self.kwargs.get('pk'))


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['author__username', 'body', 'recipe__title']
    pagination_class = RecipePageNumberPagination

    @swagger_auto_schema(tags=['Comments'])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CommentCreateAPIView(CreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['Comments'])
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer

    @swagger_auto_schema(tags=['Comments'])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CommentUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    @swagger_auto_schema(tags=['Comments'], auto_schema=None)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Comments'])
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Comments'])
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    @swagger_auto_schema(tags=['Comments'])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Comments'], auto_schema=None)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
