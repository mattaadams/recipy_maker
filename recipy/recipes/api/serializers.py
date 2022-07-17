from rest_framework import serializers
from recipes.models import Recipe, Ingredient, Comment


class IngredientListSerializer(serializers.ModelSerializer):
    recipe = serializers.CharField(read_only=True)
    author = serializers.CharField(source="recipe.author", read_only=True)

    class Meta:
        model = Ingredient
        fields = [
            'id',
            'name',
            'recipe',
            'author'
        ]


class IngredientCreateUpdateSerializer(serializers.ModelSerializer):
    recipe = serializers.CharField(read_only=True)
    author = serializers.CharField(source="recipe.author", read_only=True)

    class Meta:
        model = Ingredient
        fields = [
            'id',
            'name',
            'recipe',
            'author'

        ]


class IngredientDetailSerializer(serializers.ModelSerializer):
    recipe = serializers.CharField(read_only=True)
    author = serializers.CharField(source="recipe.author", read_only=True)

    class Meta:
        model = Ingredient
        fields = [
            'id',
            'name',
            'recipe',
            'author'
        ]


class RecipeListSerializer(serializers.ModelSerializer):
    ingredients = IngredientListSerializer(many=True, read_only=True)
    author = serializers.CharField(read_only=True)

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
    ingredients = IngredientCreateUpdateSerializer(many=True)
    author = serializers.CharField(read_only=True)
    image_url = serializers.URLField(allow_blank=True, default=None)

    class Meta:

        model = Recipe
        fields = [
            'id',
            'author',
            'title',
            'image_url',
            'description',
            'ingredients',
            'instructions',
        ]

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            Ingredient.objects.create(recipe=recipe, **ingredient_data)
        return recipe


class RecipeDetailSerializer(serializers.ModelSerializer):
    ingredients = IngredientListSerializer(many=True, read_only=True)
    author = serializers.CharField(read_only=True)

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
    author = serializers.CharField(source="recipe.author", read_only=True)

    class Meta:

        model = Comment
        fields = [
            'id',
            'author',
            'body',
            'date_posted',
            'recipe',
        ]


class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    recipe = serializers.CharField(read_only=True)
    author = serializers.CharField(source="recipe.author", read_only=True)

    class Meta:

        model = Comment
        fields = [
            'id',
            'author',
            'body',
            'date_posted',
            'recipe',
        ]


class CommentDetailSerializer(serializers.ModelSerializer):
    recipe = serializers.CharField(read_only=True)
    author = serializers.CharField(source="recipe.author", read_only=True)

    class Meta:

        model = Comment
        fields = [
            'id',
            'author',
            'body',
            'date_posted',
            'recipe',
        ]
