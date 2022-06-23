from rest_framework import serializers
from recipes.models import Recipe, Ingredient, Comment


class IngredientListSerializer(serializers.ModelSerializer):
    recipe = serializers.CharField(read_only=True)

    class Meta:
        model = Ingredient
        fields = [
            'id',
            'name',
            'quantity',
            'recipe',
        ]


class IngredientCreateUpdateSerializer(serializers.ModelSerializer):
    recipe = serializers.CharField(read_only=True)

    class Meta:
        model = Ingredient
        fields = [
            'id',
            'name',
            'quantity',
            'recipe'
        ]


class IngredientDetailSerializer(serializers.ModelSerializer):
    recipe = serializers.CharField(read_only=True)

    class Meta:
        model = Ingredient
        fields = [
            'id',
            'name',
            'quantity',
            'recipe'
        ]


class RecipeListSerializer(serializers.ModelSerializer):
    ingredients = IngredientListSerializer(many=True, read_only=True)
    author = serializers.CharField()

    class Meta:

        model = Recipe
        fields = [
            'id',
            'author',
            'title',
            'description',
            'ingredients',
            'instructions',
            'date_posted'
        ]


class RecipeCreateUpdateSerializer(serializers.ModelSerializer):
    ingredients = IngredientCreateUpdateSerializer(many=True, read_only=True)
    author = serializers.CharField()

    class Meta:

        model = Recipe
        fields = [
            'id',
            'author',
            'title',
            'description',
            'ingredients',
            'instructions',
            'date_posted'
        ]
        read_only_fields = ['author']


class RecipeDetailSerializer(serializers.ModelSerializer):
    ingredients = IngredientListSerializer(many=True, read_only=True)
    author = serializers.CharField()

    class Meta:

        model = Recipe
        fields = [
            'id',
            'author',
            'title',
            'description',
            'ingredients',
            'instructions',
            'date_posted'
        ]


class CommentListSerializer(serializers.ModelSerializer):
    recipe = serializers.CharField(read_only=True)

    class Meta:

        model = Comment
        fields = [
            'id',
            'name',
            'body',
            'date_posted',
            'recipe',
        ]


class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    recipe = serializers.CharField(read_only=True)

    class Meta:

        model = Comment
        fields = [
            'id',
            'name',
            'body',
            'date_posted',
            'recipe',
        ]


class CommentDetailSerializer(serializers.ModelSerializer):
    recipe = serializers.CharField(read_only=True)

    class Meta:

        model = Comment
        fields = [
            'id',
            'name',
            'body',
            'date_posted',
            'recipe',
        ]
