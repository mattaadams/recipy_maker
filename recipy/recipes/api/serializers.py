from rest_framework import serializers
from recipes.models import Recipe, Ingredient, Comment


class IngredientListSerializer(serializers.ModelSerializer):
    recipe_title = serializers.CharField(source="recipe.title", read_only=True)
    author = serializers.CharField(source="recipe.author", read_only=True)

    class Meta:
        model = Ingredient
        fields = [
            'id',
            'name',
            'recipe',
            'recipe_title',
            'author'
        ]


class IngredientCreateUpdateSerializer(serializers.ModelSerializer):
    recipe_title = serializers.CharField(source="recipe.title", read_only=True)
    author = serializers.CharField(source="recipe.author", read_only=True)

    class Meta:
        model = Ingredient
        fields = [
            'id',
            'name',
            'recipe',
            'recipe_title',
            'author'

        ]


class IngredientDetailSerializer(serializers.ModelSerializer):
    recipe_title = serializers.CharField(source="recipe.title", read_only=True)
    author = serializers.CharField(source="recipe.author", read_only=True)

    class Meta:
        model = Ingredient
        fields = [
            'id',
            'name',
            'recipe',
            'recipe_title',
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

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        ingredients = list(instance.ingredients.all())

        instance.id = validated_data.get('id', instance.id)
        instance.save()

        # many ingredients
        for ingredient_data in ingredients_data:
            ingredient = ingredients.pop(0)
            ingredient.name = ingredient_data.get('name', ingredient.name)
            ingredient.save()

        return instance


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
    author = serializers.CharField(read_only=True)

    class Meta:

        model = Comment
        fields = [
            'id',
            'author',
            'body',
            'date_posted',
            'recipe'
        ]


class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)

    class Meta:

        model = Comment
        fields = [
            'id',
            'author',
            'body',
            'recipe'
        ]


class CommentDetailSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)

    class Meta:

        model = Comment
        fields = [
            'id',
            'author',
            'body',
            'date_posted',
            'recipe'
        ]
