
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Q

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView
)

from .pagination import RecipePageNumberPagination
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

)
from .permissions import (
    IsOwnerOrReadOnly,
    IsParentOwnerOrReadOnly,
    IsCommentOwnerOrReadOnly)
from recipes.models import Recipe, Ingredient, Comment
from .serializers import (
    RecipeListSerializer,
    RecipeCreateUpdateSerializer,
    RecipeDetailSerializer,
    IngredientListSerializer,
    IngredientCreateUpdateSerializer,
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
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

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
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @swagger_auto_schema(tags=['Recipes'])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Recipes'], auto_schema=None)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class IngredientListAPIView(ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['recipe__author__username', 'name']
    pagination_class = RecipePageNumberPagination

    @swagger_auto_schema(tags=['Ingredients'])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# class IngredientCreateAPIView(CreateAPIView):
#     queryset = Ingredient.objects.all()
#     serializer_class = IngredientCreateUpdateSerializer
#     permission_classes = [IsAuthenticated]

#     @swagger_auto_schema(tags=['Ingredients'])
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)


class IngredientDetailAPIView(RetrieveAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientDetailSerializer

    def get_object(self):
        obj = super().get_object()
        return obj

    @swagger_auto_schema(tags=['Ingredients'])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# class IngredientUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = Ingredient.objects.all()
#     serializer_class = IngredientCreateUpdateSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly, IsParentOwnerOrReadOnly]

#     def perform_update(self, serializer):
#         serializer.save(author=self.request.user)

#     @swagger_auto_schema(tags=['Ingredients'], auto_schema=None)
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     @swagger_auto_schema(tags=['Ingredients'])
#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)

#     @swagger_auto_schema(tags=['Ingredients'])
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)


# class IngredientDeleteAPIView(RetrieveDestroyAPIView):
#     queryset = Ingredient.objects.all()
#     serializer_class = IngredientDetailSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly, IsParentOwnerOrReadOnly]

#     @swagger_auto_schema(tags=['Ingredients'])
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

#     @swagger_auto_schema(tags=['Ingredients'], auto_schema=None)
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def get_object(self):
#         obj = super().get_object()
#         print(obj)
#         return obj


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
    permission_classes = [IsAuthenticated, IsCommentOwnerOrReadOnly]

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
    permission_classes = [IsAuthenticated, IsCommentOwnerOrReadOnly]

    @swagger_auto_schema(tags=['Comments'])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Comments'], auto_schema=None)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
