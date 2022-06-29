from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

)
from .permissions import IsOwnerOrReadOnly
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


class RecipeCreateAPIView(CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RecipeDetailAPIView(RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer


class RecipeUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class RecipeDeleteAPIView(DestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer
    permission_classes = [IsAuthenticated]


class IngredientListAPIView(ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientListSerializer


class IngredientCreateAPIView(CreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientCreateUpdateSerializer
    permission_classes = [IsAuthenticated]


class IngredientDetailAPIView(RetrieveAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientDetailSerializer


class IngredientUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientCreateUpdateSerializer
    permission_classes = [IsAuthenticated]


class IngredientDeleteAPIView(DestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientDetailSerializer
    permission_classes = [IsAuthenticated]


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateUpdateSerializer
    permission_classes = [IsAuthenticated]


class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer


class CommentUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateUpdateSerializer
    permission_classes = [IsAuthenticated]


class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = [IsAuthenticated]
