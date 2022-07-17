
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
from .permissions import IsOwnerOrReadOnly, IsParentOwnerOrReadOnly
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

    @swagger_auto_schema(tags=['Recipes'])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


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

    @swagger_auto_schema(tags=['Recipes'])
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

    @swagger_auto_schema(tags=['Recipes'])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class IngredientListAPIView(ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientListSerializer

    @swagger_auto_schema(tags=['Ingredients'])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class IngredientCreateAPIView(CreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['Ingredients'])
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class IngredientDetailAPIView(RetrieveAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientDetailSerializer

    def get_object(self):
        obj = super().get_object()
        print(obj.__dict__)
        return obj

    @swagger_auto_schema(tags=['Ingredients'])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class IngredientUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientCreateUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsParentOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    @swagger_auto_schema(tags=['Ingredients'])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Ingredients'])
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Ingredients'])
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class IngredientDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsParentOwnerOrReadOnly]

    @swagger_auto_schema(tags=['Ingredients'])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Ingredients'])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def get_object(self):
        obj = super().get_object()
        print(obj)
        return obj


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer

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
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['Comments'])
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
    permission_classes = [IsAuthenticated]\


    @swagger_auto_schema(tags=['Comments'])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Comments'])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
