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
            'recipe'
        ]


class IngredientCreateSerializer(serializers.ModelSerializer):
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

    class Meta:

        model = Recipe
        fields = [
            'id',
            'title',
            'description',
            'ingredients',
            'instructions',
            'date_posted'
        ]


class RecipeCreateSerializer(serializers.ModelSerializer):
    ingredients = IngredientCreateSerializer(many=True, read_only=True)

    class Meta:

        model = Recipe
        fields = [
            'id',
            'title',
            'description',
            'ingredients',
            'instructions',
            'date_posted'
        ]


class RecipeDetailSerializer(serializers.ModelSerializer):
    ingredients = IngredientListSerializer(many=True, read_only=True)

    class Meta:

        model = Recipe
        fields = [
            'id',
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
